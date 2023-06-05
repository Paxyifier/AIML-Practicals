import pickle
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
def train() -> None:
    original_df = pd.read_csv("../Stores.csv")

    x = original_df.iloc[:, 1:4].values
    y = original_df.iloc[:, 4].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    regrssor = LinearRegression()
    regrssor.fit(x_train, y_train)
    regrssor.predict(x_test)
    print(regrssor.score(x_test, y_test))
    pickle.dump(
        regrssor,
        open(f'models/Stores-model_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.pkl', "wb"),
    )

if __name__ == "__main__":
    train()