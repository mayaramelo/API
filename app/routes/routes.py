from app import app
from flask import jsonify, request, abort
from app.models.models import Analysis, AnalysisSchema
from app.services.botometer_service import BotometerService


@app.get("/catch")
def catch():
    handle = str(request.args.get('profile'))
    botometer_service = BotometerService()
    response = botometer_service.catch(handle)
    return jsonify(response), 200


@app.get('/botprobability') # test only
def botprobability():
    handle = str(request.args.get('profile'))
    botometer_service = BotometerService()
    response = botometer_service.botProbability(handle)
    return jsonify(response), 200

@app.get('/complete')
def complete():
    handle = str(request.args.get('profile'))
    result = Analysis.query.filter_by(handle=handle).first()
    # result = Analysis.query.get(1);
    analysis_schema = AnalysisSchema()
    return jsonify(analysis_schema.dump(result))

@app.post('/feedback')
def feedback():
    return jsonify("feedback")

