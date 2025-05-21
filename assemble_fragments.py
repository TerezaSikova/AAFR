import argparse
import importlib
import pdb
from runner import fragment_reassembler
import os 

def prepare_demo(cfg, demo_name):
    if not hasattr(cfg, 'demo_options'):
        raise AttributeError(
            f"Please use a demo-compatible config file (assemble_cfg_demo.py)"
        )
    
    demo_options = cfg.demo_options

    if demo_name not in demo_options:
        raise ValueError(
            f"Demo '{demo_name}' not found. Available options are: {list(demo_options.keys())}"
        )
    p = demo_options[demo_name] #parameters for the demo

    cfg.variables_as_list = [
        p['num_of_points'], p['num_of_points'], p['N'], p['to'], p['to'],
        p['to'], p['tb'], p['tb'], p['tb'], p['dil'], p['thre']
    ]

    cfg.data_list = [entry for entry in cfg.data_list if entry["category"] == demo_name]
    cfg.name = demo_name

def main(args):

    print_line_length = 65
    module_name = f"configs.{args.cfg}"
    cfg = importlib.import_module(module_name)
    speed = args.f
    mode = args.mode

    if args.demo:
        prepare_demo(cfg, args.demo)

    print("\nWill try to assemble:")
    for i, broken_objects in enumerate(cfg.data_list):
        category = broken_objects["category"]
        fracture = broken_objects["fracture"]
        name = f"{category}_{fracture}"
        print(f"{i}) {name}")

    print()
    for i, broken_objects in enumerate(cfg.data_list):

        print('#' * print_line_length)
        category = broken_objects["category"]
        fracture = broken_objects["fracture"]
        name = f"{category}_{fracture}"
        print(f'Current broken object: {fracture} ({category})')
        fr_ass = fragment_reassembler(speed, mode, broken_objects, cfg.variables_as_list, cfg.pipeline_parameters, name, show_results = True, save_results=True)
        print('-' * print_line_length)
        # load object and move them (challenge_R_T) to have something to solve (without R and T they are loaded in the correct position)
        fr_ass.load_objects()

        # set output directory, save fragments and information there
        broken_objects_out_dir = os.path.join(cfg.output_dir, name)
        os.makedirs(broken_objects_out_dir, exist_ok=True)
        fr_ass.set_output_dir(broken_objects_out_dir)
        fr_ass.save_fragments(cfg.name)
        fr_ass.save_info()

        # 3.1) breaking curves
        print("___________________Breaking_Curves_Detection__________________")
        fr_ass.detect_breaking_curves()
        fr_ass.save_breaking_curves()

        # 3.2) segmentation
        print("_________________________Segmentation_________________________")
        fr_ass.segment_regions()
        fr_ass.save_segmented_regions()

        # 3.3) registration
        print("_________________________Registration_________________________")
        fr_ass.register_segmented_regions()
        fr_ass.save_registration_results()
        fr_ass.save_registered_pcls()

        # 4) evaluation
        print("__________________________Evaluation__________________________")
        if 'solution' in broken_objects.keys():
            fr_ass.load_gt()
            fr_ass.evaluate_against_gt()
            fr_ass.save_evaluation_results()
        else:
            print("Solution not available, skipping evaluation")


    #pdb.set_trace()
    return 1

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Reassembling broken objects')
    parser.add_argument('--cfg', type=str, default='assemble_cfg', help='config file (.py)')
    parser.add_argument('--f', type=str, default='SLOW', help='Operating speed (default: SLOW, FAST for fast mode)')
    parser.add_argument('--demo', type=str, help='Name of demo to run (e.g., figurineS3)')
    parser.add_argument('--mode', type=str, default='ALI', help='Mode of the run (SB for Sinlge breakage)')
    args = parser.parse_args()
    main(args)
