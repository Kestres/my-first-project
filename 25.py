#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import sys

class UserMetrics:
    def __init__(self, username):
        self.username = username
        self.registration_date = datetime.datetime.now()
        self.login_count = 1
        
    def get_metrics(self):
        metrics = {
            "👤 Имя пользователя": self.username,
            "📅 Дата регистрации": self.registration_date.strftime("%Y-%m-%d %H:%M:%S"),
            "🔢 Количество входов": self.login_count,
            "⭐ Уровень": "Новичок 🌱"
        }
        return metrics

def main():
    username = input("👤 Введите ваше имя: ").strip()
    
    if not username:
        print("❌ Имя не может быть пустым!")
        return
    
    user_metrics = UserMetrics(username)
    metrics = user_metrics.get_metrics()
    
    print("\n" + "=" * 50)
    print("📊 ВАШИ МЕТРИКИ")
    print("=" * 50)
    
    for key, value in metrics.items():
        print(f"{key}: {value}")
    
    print("=" * 50)
    print(f"✨ Привет, {username}! ✨")

if __name__ == "__main__":
    main()