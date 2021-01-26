# noinspection PyUnresolvedReferences
import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战游戏主程序类"""

    # 游戏初始化
    def __init__(self):
        self.counts = 0
        print('游戏初始化')
        pygame.init()
        # 创建游戏窗口
        # self.screen = pygame.display.set_mode((480, 700))
        pygame.display.set_caption('Plane War')
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 创建精灵和精灵组
        self.__create_sprites()
        # 设置创建敌机的定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, ENEMY_PER_SEC)
        # 设置发射子弹的定时器事件
        pygame.time.set_timer(FIRE_BULLET_EVENT, BULLET_PER_SEC)

    # 游戏循环
    def start_game(self):
        print('游戏开始')
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprites()
            # 刷新屏幕显示
            pygame.display.update()

    # 创建精灵和精灵组
    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 事件监听
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over(self.counts)
            elif event.type == CREATE_ENEMY_EVENT:
                print('生成敌机')
                # 创建敌机
                enemy = Enemy()
                # 将敌机添加到精灵组中
                self.enemy_group.add(enemy)
            elif event.type == FIRE_BULLET_EVENT:
                self.hero.fire()

            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            # 通过键盘模块提供的方法获取按键元组
            keys_list = pygame.key.get_pressed()
            # 判断向右方向键是否被按下
            if keys_list[pygame.K_RIGHT]:
                # print('→')
                self.hero.speed = HERO_HOR_SPEED
            # 判断向左方向键是否被按下
            elif keys_list[pygame.K_LEFT]:
                self.hero.speed = -HERO_HOR_SPEED
            else:
                self.hero.speed = 0

            # 判断上下方向键
            if keys_list[pygame.K_UP]:
                self.hero.speed_y = -HERO_VER_SPEED
            elif keys_list[pygame.K_DOWN]:
                self.hero.speed_y = HERO_VER_SPEED
            else:
                self.hero.speed_y = 0

            # 判断空格键是否按下
            if keys_list[pygame.K_SPACE]:
                self.hero.check_fire = True
            else:
                self.hero.check_fire = False

    # 碰撞检测
    # noinspection SpellCheckingInspection
    def __check_collide(self):
        # 子弹销毁敌机
        # noinspection PyTypeChecker
        count = pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True,
                                           pygame.sprite.collide_mask)
        # 统计击中数
        if count:
            self.counts += 1
        # 敌机撞击英雄
        # noinspection PyTypeChecker
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True, pygame.sprite.collide_mask)
        # enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            print('英雄牺牲')
            self.hero.kill()
            PlaneGame.__game_over(self.counts)

    # 更新/绘制精灵组
    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    # 游戏结束
    @staticmethod
    def __game_over(counts):
        print('游戏结束')
        pygame.quit()
        pygame.screen = pygame.display.set_mode(OUT_SCREEN_RECT.size)
        while True:
            pygame.font.init()
            pygame.display.set_caption('你的得分')
            pygame.screen.fill([255, 255, 255])
            my_font = pygame.font.SysFont('None', 50)
            pygame.screen.blit(my_font.render('Your scores:%s' % counts, True, (0, 0, 0)), (0, 25))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
