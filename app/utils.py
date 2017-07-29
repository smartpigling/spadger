from flask import current_app
from flask_paginate import Pagination


def get_pagination(**kwargs):
    kwargs.setdefault('record_name', 'records')
    return Pagination(css_framework=current_app.config.get('CSS_FRAMEWORK', 'bootstrap3'),
                      link_size=current_app.config.get('LINK_SIZE', 'sm'),
                      show_single_page=current_app.config.get('SHOW_SINGLE_PAGE', False),
                      **kwargs
                      )
