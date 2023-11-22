from flask import Flask, render_template, request, redirect, url_for
from model import ListeTaches

application = Flask(__name__)

@application.route('/')
def home():
    """
    Page Home
    :param prenom:
    :return:
    """
    return render_template(template_name_or_list='home.html', title="HOME", prenom="Luc")


if __name__ == '__main__':
    application.run()
