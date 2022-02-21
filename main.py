# core fastapi server
from fastapi import FastAPI, Request, Response, status, Depends, BackgroundTasks, HTTPException, File, UploadFile, security, Form
# ssr imports
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
# endpoints responses classes
from starlette.responses import RedirectResponse, Response, FileResponse, JSONResponse, StreamingResponse, HTMLResponse
from bs4 import BeautifulSoup
from requests import get, post, delete, put, patch, head, options, request, Response as ReqResponse, Session, exceptions
# security imports
from json import dumps, loads, JSONDecodeError, JSONDecoder, JSONEncoder, load, dump
from bcrypt import hashpw, gensalt, checkpw
from passlib import context, hash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from jose import jwt
# os imports
from os import mkdir, listdir, remove, rename, system, chdir, getcwd, stat, getenv
from os.path import getcwd
from shutil import copyfile, rmtree, copyfileobj
