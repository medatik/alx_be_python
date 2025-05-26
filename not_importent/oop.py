class person :
    def __init__(self, fname, lname, age, cin, date_of_birth, place_of_birth, nationality):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.cin = cin
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
        self.nationality = nationality

    def personal_infos(self):
            print(f"first name : {self.fname} \nlast name : {self.lname} \nage : {self.age} \ncin : {self.cin} \nwas born at : {self.date_of_birth} in : {self.place_of_birth} \nnationality : {self.nationality}")

class student(person):
    def __init__(self, fname, lname, age, cin, date_of_birth, place_of_birth, nationality, student_id, diploma, marks, branch):
        super().__init__(fname, lname, age, cin, date_of_birth, place_of_birth, nationality)
        self.id = student_id
        self.diploma = diploma
        self.marks = marks
        self.branch = branch

    def calc_avg(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)


    def student_infos(self):
        avg = self.calc_avg()
        print(f"id : {self.id} \nfirst name : {self.fname} \nlast name : {self.lname} \nage : {self.age} \nlast diploma : {self.diploma}  \nbranch : {self.branch} \naverage : {avg}")

class developer(student):
    def __init__(self, fname, lname, age, cin, date_of_birth, place_of_birth, nationality, student_id, diploma, marks, branch, years_of_experience, skills):
        super().__init__(fname, lname, age, cin, date_of_birth, place_of_birth, nationality, student_id, diploma, marks, branch)
        self.years = years_of_experience
        self.skills = skills

    def skills_list(self):
        i = 1
        print(f"skills : ")
        for skill in self.skills:
            print(f" {i} - {skill}")
            i +=1

    def developer_infos(self):
        print(f"first name : {self.fname} \nlast name : {self.lname} \nage : {self.age} \nexperience : {self.years} years \nlast diploma : {self.diploma} \nbranch studied : {self.branch}")
        self.skills_list()


ana = person("mohamed", "atikeddine", "21", "bh555", "2004", "casa", "moroccan")
ana.personal_infos()
print("--------------------------------------------------")
ana_tilmid = student("mohamed", "atikeddine", "21", "bh555", "2004", "casa", "moroccan", "12jk3LH8d88K", "bac+2", [13,14,7,17,9,10,11], "web dev")
ana_tilmid.student_infos()
print("--------------------------------------------------")
ana_developeur = developer("mohamed", "atikeddine", "21", "bh555", "2004", "casa", "moroccan", "12jk3LH8d88K", "bac+2", [13,14,7,17,9,10,11], "web dev", 2, ['html', 'css', 'js', 'php', 'mysql', 'mongodb', 'sql server', 'react', 'next', 'laravel', 'express', 'git', 'github'])
ana_developeur.developer_infos()

