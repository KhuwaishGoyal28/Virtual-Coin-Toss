import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QFont, QIcon, QMovie
from PyQt6.QtCore import Qt, QTimer

class CoinTossApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Virtual Coin Toss - Professional Edition")
        self.setGeometry(100, 100, 400, 450)
        self.setStyleSheet("background-color: #1E1E1E; color: white; border-radius: 10px;")  # Dark theme
        self.setWindowIcon(QIcon("coin_icon.png"))  # Set custom icon

        # Coin Label (GIF Animation)
        self.coin_label = QLabel(self)
        self.coin_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.coin_label.setFixedSize(150, 150)

        # Load Coin Animation (GIF)
        self.coin_movie = QMovie("coin_flip.gif")  # Use an animated coin GIF
        self.coin_label.setMovie(self.coin_movie)

        # Flip Button
        self.flip_button = QPushButton("🎲 Flip Coin", self)
        self.flip_button.setFont(QFont("Arial", 14))
        self.flip_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 10px; padding: 10px;")
        self.flip_button.clicked.connect(self.animate_flip)

        # Result Label
        self.result_label = QLabel("Heads: 0 | Tails: 0", self)
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Reset Button
        self.reset_button = QPushButton("🔄 Reset", self)
        self.reset_button.setFont(QFont("Arial", 12))
        self.reset_button.setStyleSheet("background-color: #FF5733; color: white; border-radius: 10px; padding: 10px;")
        self.reset_button.clicked.connect(self.reset_counts)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.coin_label)
        layout.addWidget(self.flip_button)
        layout.addWidget(self.result_label)

        # Button Layout (Flip & Reset)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.flip_button)
        button_layout.addWidget(self.reset_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # Stats
        self.count_heads = 0
        self.count_tails = 0
        self.flipping_animation_timer = QTimer()
        self.flipping_animation_timer.timeout.connect(self.complete_flip)

    def animate_flip(self):
        """Creates a small delay effect before showing the result"""
        self.coin_movie.start()  # Start the animation
        self.result_label.setText("Flipping...")
        self.flipping_animation_timer.start(2000)  # 2 seconds animation

    def complete_flip(self):
        """Finalizes the coin flip and updates the stats"""
        self.flipping_animation_timer.stop()
        self.coin_movie.stop()  # Stop animation
        result = random.choice(["Heads", "Tails"])
        self.coin_label.setPixmap(QIcon(f"{result.lower()}.png").pixmap(150, 150))  # Show static result image

        if result == "Heads":
            self.count_heads += 1
        else:
            self.count_tails += 1

        total_flips = self.count_heads + self.count_tails
        heads_percent = (self.count_heads / total_flips) * 100 if total_flips > 0 else 0
        tails_percent = (self.count_tails / total_flips) * 100 if total_flips > 0 else 0
        self.result_label.setText(f"Heads: {self.count_heads} ({heads_percent:.1f}%) | Tails: {self.count_tails} ({tails_percent:.1f}%)")

    def reset_counts(self):
        """Resets the counter and updates the display"""
        self.count_heads = 0
        self.count_tails = 0
        self.coin_label.setPixmap(QIcon("coin_icon.png").pixmap(150, 150))
        self.result_label.setText("Heads: 0 | Tails: 0")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoinTossApp()
    window.show()
    sys.exit(app.exec())
