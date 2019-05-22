from django.core.management.base import BaseCommand
from django.core.files import File
from django.utils import timezone

from users.models import CustomUser

import pandas as pd
import challonge




def main_loop():
    path_to_users_csv = "/Users/nikitazdanov/Desktop/Julia/Курсовая БД/Заполнение БД/Users.csv"

    df = pd.read_csv(path_to_users_csv)
    users_fio = [el for el in df["FIO"].values[:50]]
    users_usernames = [f"{el}{i}" for i, el in enumerate(df["login"].values[:50])]
    users_emails = [f"{el}{i}" for i, el in enumerate(df["email"].values[:50])]
    users_passwords = [el for el in df["pwd"].values[:50]]
    users_role = [CustomUser.PILOT for i in range(50)]
    users_datebirth = [el for el in df["date_birth"].values[:50]]
    users_phonenumbs = [el for el in df["phone_n"].values[:50]]


    for i in range(50):
        new_users = CustomUser.objects.create(
            username=users_usernames[i],
            password=users_passwords[i],
            date_of_birth=users_datebirth[i],
            phone_no=users_phonenumbs[i],
            full_name=users_fio[i],
            user_role=users_role[i],
        )


def challonge_add_users():
    username = "ybourkhanova"
    api_key = "VeiRWinHgxU3W77ZV2q2L70uTI0BnhNnq68iu8Oo"

    challonge.set_credentials(username, api_key)

    tournament = challonge.tournaments.show("ufy5bx0r")

    tournament_id = tournament["id"]
    tournament_name = tournament["name"]

    pilots_users = CustomUser.objects.filter(user_role=CustomUser.PILOT)
    for user in pilots_users:
        try:
            challonge.participants.create(tournament_id, user.full_name)
        except Exception as e:
            print(type(e), e)
            continue


class Command(BaseCommand):
    help = "Run attendance control loop"
    # Main Loop

    def handle(self, *args, **kwargs):

        self.stdout.write(
            self.style.SUCCESS(
                "Adding users loop is starting..."
            )
        )

        #main_loop()
        challonge_add_users()

        self.stdout.write(
            self.style.SUCCESS(
                "Done."
            )
        )
