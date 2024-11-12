import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Наносит урон другому герою, отнимая у него здоровье на величину силы удара."""
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        """Проверяет, жив ли герой (если здоровье больше 0, возвращает True)."""
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        """Инициализирует игру с героем-игроком и героем-компьютером."""
        self.player = Hero(name=player_name)
        self.computer = Hero(name=computer_name)

    def start(self):
        """Запускает игровой процесс с чередованием ходов, пока один из героев не погибнет."""
        print(f"Добро пожаловать в игру! {self.player.name} сражается против {self.computer.name}!")

        # Цикл игры, пока оба героя живы
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            print(f"{self.computer.name} здоровье: {self.computer.health}")

            # Проверка, если компьютер побежден
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            print(f"{self.player.name} здоровье: {self.player.health}")

            # Проверка, если игрок побежден
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break


# Пример запуска игры
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
