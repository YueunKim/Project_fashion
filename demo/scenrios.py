"""
@auther Hyunwoong
@since 7/1/2020
@see https://github.com/gusdnd852
"""

from kocrawl.dust import DustCrawler
from kocrawl.map import MapCrawler
from kocrawl.retaurant import RestaurantCrawler
from kocrawl.weather import WeatherCrawler
from kochat.app import Scenario

weather = Scenario(
    intent='COLORSIZE',
    api=WeatherCrawler().request,
    # api={
    #     'SIZE': [],
    #     # 'COLOR': ['오늘']
    #     'COLOR': []
    # },
    scenario={
        'SIZE': [],
        # 'COLOR': ['오늘']
        'COLOR': []
    }
)


dust = Scenario(
    intent='KINDSIZE',
    api=DustCrawler().request_debug,
    scenario={
        'SIZE': [],
        'KIND': ['오늘']
    }
)

restaurant = Scenario(
    intent='COLORKIND',
    api=RestaurantCrawler().request,
    scenario={
        'KIND': [],
        'COLOR': ['유명한']
    }
)

travel = Scenario(
    intent='PAYSALE',
    api=MapCrawler().request_debug,
    scenario={
        'PAY': [],
        'SALE': ['관광지']
    }
)
