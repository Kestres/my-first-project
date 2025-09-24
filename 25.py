#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

class UserMetrics:
    def __init__(self, username):
        self.username = username
        self.registration_date = datetime.datetime.now()
        self.login_count = 1
        
    def get_metrics(self):
        return {
            "Имя пользователя": self.username,
            "Дата регистрации": self.registration_date.strftime("%Y-%m-%d %H:%M:%S"),
            "Количество входов": self.login_count,
            "Уровень": "Новичок"
        }

def main():
    print("🎉 === СИСТЕМА ПРИВЕТСТВИЯ ===")
    print("Командный проект GitHub")
    print("-" * 40)
    
    username = input("Введите ваше имя: ").strip()
    
    if not username:
        print("Ошибка: Имя не может быть пустым!")
        return
    
    user_metrics = UserMetrics(username)
    metrics = user_metrics.get_metrics()
    
    print("\n📊 ВАШИ МЕТРИКИ:")
    print("=" * 50)
    
    for key, value in metrics.items():
        print(f"{key}: {value}")
    
    print("=" * 50)
    print(f"✨ Привет, {username}! Рады видеть вас в команде! 🚀")
    print("Репозиторий: https://github.com/Fedor815/team")

if __name__ == "__main__":
    main()