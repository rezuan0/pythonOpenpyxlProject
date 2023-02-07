
class User:
    def __init__(self, name, email, password, job_title):
        self.name = name
        self.email = email
        self.password = password
        self.job_title = job_title

    def get_user_info(self):
        print(f'Name is {self.name}, Email is {self.email} & Job Title is {self.job_title}.')


app_user = User("Md. Jone Deo", "hone@deo.com", "secret", "devOps Engineer")
app_user.get_user_info()

