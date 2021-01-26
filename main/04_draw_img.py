import pygame

# 初始化pygame
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 加载背景图像数据
bg = pygame.image.load("./images/background.png")
# 绘制背景图像
screen.blit(bg, (0, 0))
# 刷新屏幕显示
# pygame.display.update()

# 加载英雄图像数据
hero = pygame.image.load("./images/me1.png")
# 绘制英雄图像
screen.blit(hero, (200, 500))
# 刷新屏幕显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环
i = 0
while True:
    # 设置刷新帧率
    clock.tick(60)
    print(i)
    i += 1
    pass

# 卸载pygame
pygame.quit()
