import os, pdb, json

# parameters for the pipeline
pipeline_parameters = {
    'processing_module' : "standard",
    'registration_module' : "teaser",
    'evaluation_metrics' : ["rms", "chamfer"]
}

# data list
variables_as_list = []
demo_options = {
    'DrinkBottle': {
        'num_of_points': 30000,
        'to': 100,
        'tb': 0.1,
        'dil': 0.005,
        'thre': 0.93,
        'N': 15
    },
    'FigurineS4': {
        'num_of_points': 30000,
        'to': 100,
        'tb': 50,
        'dil': 0.0035,
        'thre': 0.93,
        'N': 15
    },
    'Pot': {
        'num_of_points': 50000,
        'to': 10,
        'tb': 30,
        'dil': 0.0005,
        'thre': 0.93,
        'N': 15
    },
    'WineGlass': {
        'num_of_points': 30000,
        'to': 100,
        'tb': 5,
        'dil': 0.001,
        'thre': 0.93,
        'N': 15
    }
}

output_dir = f'results'
os.makedirs(output_dir, exist_ok=True)

# list of broken objects (for now pairs)
data_folder = 'data_demo'
data_list = []

for category_folder in os.listdir(data_folder):
    cat_ff = os.path.join(data_folder, category_folder)
    for fracture_folder in os.listdir(cat_ff):
        objects_folder = os.path.join(cat_ff, fracture_folder, 'objects')
        p_o1 = os.path.join(objects_folder, 'obj1_challenge.ply')
        p_o2 = os.path.join(objects_folder, 'obj2_challenge.ply')
        solution_folder = os.path.join(cat_ff, fracture_folder, 'solution')
        broken_obj_dict = {
            "path_obj1": p_o1,
            "path_obj2": p_o2,
            "category": category_folder,
            "fracture": fracture_folder
        }
        if os.path.exists(solution_folder):
            with open(os.path.join(solution_folder, 'solution.json'), 'r') as sj:
                solution = json.load(sj)
            broken_obj_dict['solution'] = solution

        data_list.append(broken_obj_dict)
