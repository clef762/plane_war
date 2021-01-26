import pygame

# 创建矩形区域
hero_rect = pygame.Rect(100, 500, 102, 126)

# 输出英雄原始坐标原点
print("%d %d" % (hero_rect.x, hero_rect.y))
# 英雄大小
print("%d %d" % (hero_rect.width, hero_rect.height))
# size表示矩形区域宽和高
print("%d %d" % hero_rect.size)
