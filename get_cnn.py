from utilities import get_articles


def get_cnn():
    get_articles('https://cnn.com', 'cnn')


if __name__ == '__main__':
    get_cnn()
