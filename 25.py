#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import json
import os

class UserMetrics:
    """Класс для работы с метриками пользователя"""
    
    def __init__(self, username):
        self.username = username
        self.metrics_file = "user_metrics.json"
        self.load_existing_data()
        
    def load_existing_data(self):
        """Загружает существующие данные пользователя"""
        try:
            if os.path.exists(self.metrics_file):
                with open(self.metrics_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if self.username in data:
                        user_data = data[self.username]
                        self.registration_date = datetime.datetime.strptime(
                            user_data['registration_date'], '%Y-%m-%d %H:%M:%S')
                        self.login_count = user_data['login_count'] + 1
                    else:
                        self.registration_date = datetime.datetime.now()
                        self.login_count = 1
            else:
                self.registration_date = datetime.datetime.now()
                self.login_count = 1
        except:
            self.registration_date = datetime.datetime.now()
            self.login_count = 1
    
    def save_metrics(self):
        """Сохраняет метрики в файл"""
        try:
            if os.path.exists(self.metrics_file):
                with open(self.metrics_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = {}
                
            data[self.username] = {
                'registration_date': self.registration_date.strftime('%Y-%m-%d %H:%M:%S'),
                'login_count': self.login_count,
                'last_login': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            with open(self.metrics_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
    
    def get_metrics(self):
        """Возвращает метрики пользователя"""
        time_in_system = datetime.datetime.now() - self.registration_date
        days_in_system = time_in_system.days
        
        return {
            "👤 Имя пользователя": self.username,
            "📅 Дата регистрации": self.registration_date.strftime('%Y-%m-%d %H:%M:%S'),
            "🔢 Количество входов": self.login_count,
            "⏱️ В системе": f"{days_in_system} дней",
            "⭐ Уровень": self.get_user_level(),
            "🏆 Статус": self.get_user_status()
        }
    
    def get_user_level(self):
        """Определяет уровень пользователя"""
        if self.login_count > 15:
            return "Эксперт"
        elif self.login_count > 8:
            return "Продвинутый"
        elif self.login_count > 3:
            return "Активный"
        else:
            return "Новичок"
    
    def get_user_status(self):
        """Определяет статус пользователя"""
        if self.login_count > 10:
            return "Ветеран проекта 🏅"
        elif self.login_count > 5:
            return "Активный участник ⚡"
        else:
            return "Новый участник 🌱"

def print_separator():
    """Печатает разделитель"""
    print("═" * 50)

def main():
    """Основная функция программы"""
    print("\n🎉" + "═" * 46 + "🎉")
    print("           СИСТЕМА ПРИВЕТСТВИЯ КОМАНДЫ")
    print("🎉" + "═" * 46 + "🎉")
    
    print("\n👥 Участники проекта:")
    print("   • Fedor815 - Тиминд")
    print("   • dddll01 - Падаван")
    print("   • Teacher001-top - Преподаватель")
    print("🌐 Репозиторий: https://github.com/Fedor815/team")
    print_separator()
    
    # Получаем имя пользователя
    username = input("👤 Введите ваше имя: ").strip()
    
    if not username:
        print("❌ Ошибка: Имя не может быть пустым!")
        return
    
    # Создаем объект метрик
    user_metrics = UserMetrics(username)
    metrics = user_metrics.get_metrics()
    
    # Сохраняем метрики
    user_metrics.save_metrics()
    
    # Выводим метрики
    print_separator()
    print("📊 ПЕРСОНАЛЬНЫЕ МЕТРИКИ")
    print_separator()
    
    for key, value in metrics.items():
        print(f"{key:<20} : {value}")
    
    print_separator()
    
    # Визуализация прогресса
    progress = min(user_metrics.login_count, 10)
    progress_bar = "█" * progress + "░" * (10 - progress)
    print(f"\n📈 Прогресс активности: [{progress_bar}]")
    print(f"   Уровень завершенности: {progress * 10}%")
    
    # Персональное приветствие
    print(f"\n✨ Добро пожаловать, {username}!")
    print("   Рады видеть вас в нашем командном проекте! 🚀")
    
    # Информация о следующих шагах
    print_separator()
    print("💡 Следующие шаги:")
    print("   1. Изучите код проекта")
    print("   2. Предложите улучшения через Pull Request")
    print("   3. Присоединяйтесь к разработке!")
    print_separator()

if __name__ == "__main__":
    main()