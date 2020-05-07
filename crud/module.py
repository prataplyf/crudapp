# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from crud import config
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from crud import app
from flask import Flask, render_template, redirect, url_for, request, jsonify, request, make_response
import jwt # @@@@@@@@@ PYJWT Token @@@@@@@@@@@
import datetime
currentdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# import pandas as pd
from functools import wraps
import pymongo
from bson.objectid import ObjectId  # Convert string into ObjectID
from flask import session
import string
import re
import jwt
import random
from random import randint, choice
import string
from socket import gaierror
# @@@@@@@@@@@@@@@@@@@ CROSS_ORIGIN ACCESS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from flask_cors import CORS, cross_origin


from flask_bcrypt import Bcrypt