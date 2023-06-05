from api import app
from train import train

def setup():
    train()
    
if __name__ == '__main__':
    setup()
    app.run(debug=True, host='localhost', port=5000)