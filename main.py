import random

# Класс героя
class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Наносит удар по другому герою"""
        damage = random.randint(10, self.attack_power)  # Урон случайный, чтобы добавить элемент неожиданности
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")
        if other.health < 0:
            other.health = 0

    def is_alive(self):
        """Проверяет, жив ли герой"""
        return self.health > 0

    def status(self):
        """Показывает текущее здоровье героя"""
        print(f"{self.name}: {self.health} здоровья")


# Класс игры
class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        """Запуск игры"""
        print("\n--- Начало битвы! ---")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player_turn()

            # Проверка, жив ли компьютер
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден! {self.player.name} выиграл!")
                break

            # Ход компьютера
            self.computer_turn()

            # Проверка, жив ли игрок
            if not self.player.is_alive():
                print(f"{self.player.name} побежден! {self.computer.name} выиграл!")
                break

    def player_turn(self):
        """Ход игрока"""
        print("\n--- Ход игрока ---")
        self.player.attack(self.computer)
        self.computer.status()

    def computer_turn(self):
        """Ход компьютера"""
        print("\n--- Ход компьютера ---")
        self.computer.attack(self.player)
        self.player.status()


if __name__ == "__main__":
    game = Game()
    game.start()
