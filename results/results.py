#! /usr/local/bin/python3
import challonge
import pandas as pd


username = "ybourkhanova"
api_key = "VeiRWinHgxU3W77ZV2q2L70uTI0BnhNnq68iu8Oo"

challonge.set_credentials(username, api_key)

tournament = challonge.tournaments.show("ufy5bx0r")

tournament_id = tournament["id"] # 3272
tournament_name = tournament["name"] # My Awesome Tournament
print(tournament["started-at"])
print(tournament_id, tournament_name)


#participant_ivanov_name = 'Иванов'
#challonge.participants.create(tournament_id, participant_ivanov_name)



participants = challonge.participants.index(tournament_id)
participants_ids = [el.get('id') for el in participants]
participants_names = [el.get('name') for el in participants]
participants_zip = list(zip(participants_ids, participants_names))
#print(len(participants), participants, dir(participants), end='n')


print(participants_zip, )



#print(pilots_users)
path_to_users_csv = "/Users/nikitazdanov/Desktop/Julia/Курсовая БД/Заполнение БД/Users.csv"
PILOT = 'ПИ'

df = pd.read_csv(path_to_users_csv)
print(df.head(50))
users_fio = [el for el in df["FIO"].values[:50]]
users_usernames = [el for el in df["login"].values[:50]]
users_emails = [el for el in df["email"].values[:50]]
users_passwords = [el for el in df["pwd"].values[:50]]
#users_role = [CustomUser.PILOT for i in range(50)]
users_role = [PILOT for i in range(50)]
users_datebirth = [el for el in df["date_birth"].values[:50]]
users_phonenumbs = [el for el in df["phone_n"].values[:50]]

"""print(users_fio)
print(len(users_usernames))
print(users_usernames)
print(len(users_usernames))
print(users_emails)
print(len(users_emails))"""

#print(list(dict(zip(users_usernames, users_fio, users_emails))))
dict = {
    "full_name": users_fio,
    "date_of_birth": users_datebirth,
    "phone_no": users_phonenumbs,
    "username": users_usernames,
    "email": users_emails,
    "password": users_passwords,
    "user_role": users_role,

}
new_df = pd.DataFrame(dict)

print(new_df)
