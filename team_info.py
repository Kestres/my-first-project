#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_team_info():
    """Выводит информацию о команде"""
    team_members = {
        "Fedor815": "Тиминд (создатель репозитория)",
        "dddll01": "Падаван (участник команды)", 
        "Teacher001-top": "Преподаватель (руководитель)"
    }
    
    print("👥 КОМАНДА ПРОЕКТА")
    print("=" * 40)
    
    for member, role in team_members.items():
        print(f"• {member}: {role}")
    
    print("\n📊 СТАТИСТИКА ПРОЕКТА")
    print("=" * 40)
    print("Файлов в проекте: 5")
    print("Участников: 3")
    print("Коммитов: 10+")
    print("Веток: 2")

if __name__ == "__main__":
    print_team_info()