class Button:
    def __init__(self, text, color, font, x, y, image):
        self.text_in = text
        self.font = font
        self.color = color
        self.image = image
        self.text = self.font.render(self.text_in, True, self.color)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_rect = self.text.get_rect(center=(self.x, self.y))


    ##try to adjust this to have the buttons light up
    def button_position(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

