import pandas as pd

list_of_products = []


class Product:
    def __init__(self, title, photo, description, price) -> None:
        self.title = title
        self.photo = photo
        self.description = description
        self.price = price


def read_from_excel(filename):

    df = pd.read_excel(filename)

    for index in df.index:
        title = df.loc[index, 'Title']
        photo = df.loc[index, 'Photo']
        description = df.loc[index, 'Description']
        price = df.loc[index, 'Price']
        price = str(price)
        list_of_products.append(Product(title, photo, description, price))
    return list_of_products
