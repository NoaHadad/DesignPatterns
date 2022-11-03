from dataclasses import dataclass, field


@dataclass
class Person:

    name: str = None
    age: float = None


@dataclass
class PersonBuilder:

    person: Person = field(default_factory=(lambda: Person()))

    def set_name(self, name):
        self.person.name = name
        return self

    def set_age(self, age):
        self.person.age = age
        return self

    def create(self):
        return self.person


if __name__=='__main__':
    print(PersonBuilder().set_name('noa').set_age(26).create())