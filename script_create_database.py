from src.models import database
from src.models.account import Account as AccountModel


def create_all_table():
    database.create_tables([AccountModel])


if __name__ == "__main__":
    create_all_table()
