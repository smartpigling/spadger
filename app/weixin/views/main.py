# -*- coding: utf-8 -*-
from flask import Blueprint, render_template,request, flash, abort, current_app
from jinja2 import TemplateNotFound
from app.weixin.models.general import Customer, MessageReply
from app import db
from flask_paginate import Pagination, get_page_args
from app.utils import get_pagination


weixin_blueprint = Blueprint('weixin', __name__, template_folder='../templates', static_folder='../static')


# @feature_blueprint.route('/index', defaults={'page': 'index'})
# def index(page):
#     try:
#         return render_template('weixin/%s.html' % page)
#     except TemplateNotFound:
#         abort(404)


@weixin_blueprint.route('/keyword_reply/', defaults={'page': 1})
@weixin_blueprint.route('/keyword_reply/page/<int:page>')
def keyword_reply(page):
    page, per_page, offset = get_page_args()

    query = MessageReply.query.filter_by()

    total = query.count()

    results = query.paginate(page, per_page)

    return render_template('weixin/test.html',
                           records=results.items,
                           pagination=get_pagination(page=page,per_page=per_page,total=total))
