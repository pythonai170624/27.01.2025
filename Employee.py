class Employee:
    created_counter: int = 0  # class-member

    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
        self.increase_count_instances()

    @classmethod
    def get_count_instances(cls):
        return cls.created_counter

    @classmethod
    def increase_count_instances(cls):
        cls.created_counter += 1

dan = Employee(1, 'dan')
shani = Employee(2, 'shani')
sharon = Employee(3, 'sharon')
dan.get_count_instances()  # bad practice !
print(Employee.get_count_instances())
print(Employee.created_counter)