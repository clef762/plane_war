# 导入官方标准模块random
import random
# 导入第三方模块pygame
import pygame

# 定义屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义弹窗大小
OUT_SCREEN_RECT = pygame.Rect(0, 0, 480, 100)
# 定义刷新帧率
FRAME_PER_SEC = 60
# 定义创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 定义敌机出现的频率
ENEMY_PER_SEC = 600
# 定义敌机最小飞行速度
ENEMY_MIN_SPEED = 1
# 定义敌机最大飞行速度
ENEMY_MAX_SPEED = 6
# 定义英雄与底部距离
HERO_LEN = 120
# 定义英雄水平运动速度
HERO_HOR_SPEED = 3
# 定义英雄垂直运动速度
HERO_VER_SPEED = 3
# 定义发射子弹的定时器常量
FIRE_BULLET_EVENT = pygame.USEREVENT + 1
# 定义发射子弹的频率
BULLET_PER_SEC = 500
# 定义子弹飞行速度
BULLET_SPEED = 4
# 定义一组子弹的长度
BULLET_LEN = 20


class GameSprite(pygame.sprite.Sprite):
    """"飞机大战游戏精灵类"""

    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 让精灵在垂直方向运动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 调用父类初始化方法，指定背景图片
        super().__init__("./images/background.png")
        # 判断是否是交替图像，如果是，则设置起始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类update()方法，让背景在垂直方向运动
        super().update()
        # 判断背景图像是否移出屏幕，如果是，将其放到屏幕正上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵类"""

    def __init__(self):

        # 调用父类初始化方法，加载敌机图片
        if random.choice([True, False]):
            super().__init__("./images/enemy1.png")
        else:
            super().__init__("./images/enemy2.png")
        # 指定敌机的随机初始速度
        self.speed = random.randint(ENEMY_MIN_SPEED, ENEMY_MAX_SPEED)
        # 指定敌机的随机初始位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类update()方法，让敌机在垂直方向飞行
        super().update()
        # 判断敌机是否飞出屏幕，如果是，从精灵组中删除
        if self.rect.y >= SCREEN_RECT.height:
            print('飞出屏幕,删除敌机')
            # 将精灵从所有精灵组中删除，精灵被自动销毁
            self.kill()

    def __del__(self):
        print('敌机被销毁')


class Hero(GameSprite):
    """英雄精灵类"""

    def __init__(self):
        # 调用父类初始化方法，指定英雄图片和初始速度
        if random.choice([True, False]):
            super().__init__("./images/me1.png", 0)
        else:
            super().__init__("./images/me2.png", 0)
        self.check_fire = False
        self.speed_y = 0
        # 设置英雄初始位置
        # noinspection SpellCheckingInspection
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - HERO_LEN
        # 设置子弹精灵组属性
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        # 控制英雄在水平方向移动
        self.rect.x += self.speed
        self.rect.y += self.speed_y
        # 控制英雄不能离开水平边界
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        # 控制英雄不能离开垂直边界
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height

    def fire(self):
        if self.check_fire:
            print('发射子弹')
            for i in (0, 1, 2):
                # 创建子弹精灵
                bullet = Bullet()
                # noinspection SpellCheckingInspection
                bullet.rect.centerx = self.rect.centerx
                bullet.rect.bottom = self.rect.y - (BULLET_LEN * i)
                self.bullet_group.add(bullet)


class Bullet(GameSprite):
    """子弹精灵类"""

    def __init__(self):
        # 调用父类初始化方法，指定子弹图片和初始速度
        super().__init__("./images/bullet1.png", -BULLET_SPEED)

    def update(self):
        # 调用父类update()让子弹向上飞行
        super().update()
        # 判断是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print('子弹销毁')
