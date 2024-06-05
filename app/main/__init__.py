# -*- coding: utf-8 -*-  
# @Time    : 2024/6/5 22:40

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
