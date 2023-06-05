import pickle
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
def train() -> None:
    original_df = pd.read_csv("./insurance.csv")
    smoker = {"yes": 1, "no": 0}
    original_df["smoker"] = original_df["smoker"].map(smoker)
    sex = {"male":0,"female":1}
    original_df["sex"] = original_df["sex"].map(sex)
        
    x = original_df.iloc[:, 0:5].values
    y = original_df.iloc[:, 6].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    regrssor = LinearRegression()
    regrssor.fit(x_train, y_train)
    y_pred = regrssor.predict(x_test)
    predictions = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(predictions)
    print(regrssor.score(x_test, y_test))
    pickle.dump(
        regrssor,
        open(f'models/insurance-model_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.pkl', "wb"),
    )

if __name__ == "__main__":
    train()