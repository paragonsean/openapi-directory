from typing import List, Dict
from aiohttp import web

from openapi_server.models.intent_predict_request import IntentPredictRequest
from openapi_server.models.intent_predict_response import IntentPredictResponse
from openapi_server.models.prediction_error_response import PredictionErrorResponse
from openapi_server.models.sentiment_predict_request import SentimentPredictRequest
from openapi_server.models.sentiment_predict_response import SentimentPredictResponse
from openapi_server import util


async def intent_multipart(request: web.Request, body=None) -> web.Response:
    """Prediction for Intent

    Returns an intent prediction for the given string.

    :param body: 
    :type body: dict | bytes

    """
    body = IntentPredictRequest.from_dict(body)
    return web.Response(status=200)


async def sentiment_multipart(request: web.Request, body=None) -> web.Response:
    """Prediction for Sentiment

    Returns a sentiment prediction for the given string.

    :param body: 
    :type body: dict | bytes

    """
    body = SentimentPredictRequest.from_dict(body)
    return web.Response(status=200)
