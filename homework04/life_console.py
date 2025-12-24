import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.border()

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        for y in range(self.life.rows):
            if y + 1 >= self.max_y - 1:
                break
            for x in range(self.life.cols):
                if x + 1 >= self.max_x - 1:
                    break
                char = "#" if self.life.curr_generation[y][x] == 1 else " "
                screen.addch(y + 1, x + 1, char)

    def run(self) -> None:
        screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        screen.keypad(True)
        screen.nodelay(True)

        try:
            self.max_y, self.max_x = screen.getmaxyx()
            while self.life.is_changing and not self.life.is_max_generations_exceeded:
                screen.clear()
                self.draw_borders(screen)
                self.draw_grid(screen)
                screen.refresh()

                key = screen.getch()
                if key == ord("q"):
                    break

                self.life.step()
                curses.napms(200)

        finally:
            curses.nocbreak()
            screen.keypad(False)
            curses.echo()
            curses.endwin()


if __name__ == "__main__":
    game = GameOfLife(size=(20, 20), randomize=True)
    console = Console(life=game)
    console.run()
