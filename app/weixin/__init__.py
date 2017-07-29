# -*- coding: utf-8 -*-
from app import robot


# client = robot.client
# client.create_menu({
#     'button': [
#         {
#             'type': 'view',
#             'name': '多彩商城',
#             'url': 'http://www.soso.com/'
#         },
#         {
#             'name': '优惠活动',
#             'sub_button': [
#                 {
#                     'type': 'click',
#                     'name': '团购信息',
#                     'key': 'about'
#                 },
#                 {
#                     'type': 'click',
#                     'name': '促销活动',
#                     'key': 'about'
#                 },
#                 {
#                     'type': 'click',
#                     'name': '新品展示',
#                     'key': 'about'
#                 }
#             ]
#         },
#         {
#             'name': '会员专享',
#             'sub_button': [
#                 {
#                     'type': 'click',
#                     'name': '积分查询',
#                     'key': 'about'
#                 },
#                 {
#                     'type': 'click',
#                     'name': '会员特惠',
#                     'key': 'about'
#                 }
#             ]
#         }
#     ]
# })



@robot.text
def hello(message):

    return 'Hello World!'


@robot.key_click('about')
def about():
    return 'about'


@robot.subscribe
def subscribe(message):
    """被关注 (Event)时触发"""
    return 'subscribe'

@robot.unsubscribe
def unsubscribe(message):
    """被取消关注 (Event)时触发"""
    return 'unsubscribe'


