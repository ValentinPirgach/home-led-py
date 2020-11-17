from http import HTTPStatus
from flask import Blueprint, request, jsonify
from flasgger import swag_from
from api.model.strip import StripModel

strip_api = Blueprint('api', __name__)

strip = StripModel()

@strip_api.route('/strip/<stripName>/color', methods=['POST'])
def setColor(stripName):
    """
    Set strip color
    This will set stip color
    ---
    parameters:
      - name: stripName
        in: path
        type: string
        enum: ['stand', 'table']
        required: true
        default: table
      - name: r
        in: formData
        type: integer
      - name: g
        in: formData
        type: integer
      - name: b
        in: formData
        type: integer
    """

    strip.setColor(
        stripName,
        [
            (int)(request.form.get('r') or 0),
            (int)(request.form.get('g') or 0),
            (int)(request.form.get('b') or 0)
        ]
    )

    return jsonify(ok=True), 200


@strip_api.route('/strip/<stripName>/switch/<state>', methods=['POST'])
def switchStrip(stripName, state):
    """
    Set strip color
    This will set stip color
    ---
    parameters:
      - name: stripName
        in: path
        type: string
        enum: ['stand', 'table']
        required: true
        default: table
      - name: state
        in: path
        type: string
        enum: ['on', 'off']
        required: true
        default: on
    """

    if state == "on":
        strip.turnOn(stripName)
    else:
        strip.turnOff(stripName)

    return jsonify(state=state), 200


@strip_api.route('/strip/<stripName>/brightness', methods=['POST'])
def setBrightness(stripName):
    """
    Set strip color
    This will set stip color
    ---
    parameters:
      - name: brightness
        in: formData
        type: integer
        required: true
    """
    
    brightness = (int)(request.form.get('brightness') or 0)
    strip.setBrightness(stripName, brightness)

    return jsonify(brightness=brightness), 200
