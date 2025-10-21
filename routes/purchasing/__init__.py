from flask import Blueprint

purchasing_bp = Blueprint(
    "purchasing",
    __name__,
    url_prefix="/purchasing",
    template_folder="../../templates"
)

from . import purchasing