# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        return f"{self.brand} {self.model} is powering on."


# Derived Class
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.os = os
        self.storage = storage

    def install_app(self, app_name):
        return f"Installing {app_name} on {self.brand} {self.model}."

    def display_specs(self):
        return f"Smartphone {self.brand} {self.model} runs {self.os} with {self.storage}GB storage."


# Testing the class
phone1 = Smartphone("Apple", "iPhone 16", "iOS", 128)
print(phone1.power_on())
print(phone1.install_app("Call Of Duty"))
print(phone1.display_specs())
