"""Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:"""

import re

# Домашній номер телефону (тільки цифри та довжина номера)
def validate_home_phone(phone_number):
    pattern = r'^\d{1,5}$'
    return bool(re.match(pattern, phone_number))

home_phone = "53385"

print(f"Home phone number: {validate_home_phone(home_phone)}")


# Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
def validate_mobile_phone(phone_number):
    pattern = r'^\+?\d{1,12}$'
    return bool(re.match(pattern, phone_number))

mobile_phone = "+380930625735"

print(f"Mobile phone number: {validate_mobile_phone(mobile_phone)}")


# Email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

email = "imperator5544@gmail.com"

print(f"Email: {validate_email(email)}")


# ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
def validate_full_name(full_name):
    pattern = r'^[а-яА-Яa-zA-Z]{2,20}\s[а-яА-Яa-zA-Z]{2,20}\s[а-яА-Яa-zA-Z]{2,20}$'
    return bool(re.match(pattern, full_name))

full_name = "Werbytskiy Oleksandr Sergijowich"

print(f" Surname, first name, patronymic of the client: {validate_full_name(full_name)}")






