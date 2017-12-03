
from flask import Flask, Response, render_template, request

import json
from subprocess import Popen, PIPE
import os
from tempfile import mkdtemp
from werkzeug import secure_filename


app = Flask(__name__)
@app.route("/")
def index():
  return
def docker(*args):
  cmd = ['docker']
  for sub in args:
    cmd.append(sub)
  process = Popen(cmd, stdout = PIPE, stderr = PIPE)
  stdout, stderr = process.communicate()
  if stderr.startswith('Error'):
    print 'Error: {0} -> {1}'.format(' '.join(cmd), stderr)
  return stedrr + stdout
#
#Docker output parsing helpers
#
#
#Parses the output a Docker PS command to a python List
#
def docker_ps_to_array(output):
  all = []
  for c in [line.split() for line in output.splitlines()[1:]]:
    each = {}
    each['id'] = c[0]
    each['image'] = c[1]
    each['name'] = c[-1]
    each['ports']= c[-2]
    all.append(eacj)
  return all

#
#Parses the output of a Docker logs command to a python Dictionary
#
#(Key Value Pair object)
def docker_logs_to_object(id, output):
  logs = {}
  logs['id'] = id
  all = []
  for line in output.splitlines():
    all.append(line)
  logs['logs'] = all
  return logs
#
#Parses the output of a Docker image command to a python List
#

def docker_images_to_array(output):
  all = []
  for c in [line.split() for line in output.splitlines()[1:]]:
    each = {}
    each['id'] = c[2]
    each['tag'] = c[1]
    each['name'] = c[0]
    all.append(each)
  return all
@app.route('/containers', methods = ['GET'])

#define an endpoint to list all containers
def containers_index():
  if request.args.get('state') == 'running':
    output = docker('ps')
  else:
    output = docker('ps', '-a')
  resp = json.dumps(docker_ps_to_array(output))
  return Response(response = resp, mimetype = "application/json")
