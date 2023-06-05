import pickle
import glob

def get_model():
    list_of_files = glob.glob("models/Stores-model_*.pkl")
    list_of_files.sort(reverse=True)
    try:
        model = pickle.load(open(list_of_files[0], "rb"))
    except IndexError:
        print("No model found")
        exit(1)
    return model