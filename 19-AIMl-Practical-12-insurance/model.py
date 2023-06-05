import pickle
import glob

def get_model():
    list_of_files = glob.glob("models/insurance-model_*.pkl")
    list_of_files.sort(reverse=True)
    try:
        model = pickle.load(open(list_of_files[0], "rb"))
    except IndexError:
        print("No model found")
        exit(1)
    return model
# if __name__ == "__main__":
#     model = get_model()
#     age = int(input("Enter age: "))
#     sex = int(input("Enter sex(male=0/female=1): "))
#     bmi = float(input("Enter bmi: "))
#     children = int(input("Enter children: "))
#     smoker   = int(input("Enter smoker (yes=0/no=1): "))
#     print(get_model().predict([[age,sex,bmi,children,smoker]]))