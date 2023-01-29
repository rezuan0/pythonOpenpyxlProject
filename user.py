class User:
    def __int__(self, name, email, password, job_title):
        self.name = name
        self.email = email
        self.password = password
        self.job_title = job_title

    def get_user_info(self):
        print(f"{self.name} & {self.email} & {self.job_title}")


app_user_one = User("Md.Rezuan Hussen", "rezu@rh.com", "DebOps Engineer", "psw1")

