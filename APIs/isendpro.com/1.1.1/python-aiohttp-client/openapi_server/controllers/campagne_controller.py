from typing import List, Dict
from aiohttp import web

from openapi_server.models.erreur import Erreur
from openapi_server import util


async def get_campagne(request: web.Request, keyid, rapport_campagne, date_deb, date_fin) -> web.Response:
    """Retourne les SMS envoyés sur une période donnée

    Retourne les SMS envoyés sur une période donnée en fonction d&#39;une date de début et d&#39;une date de fin.   Les dates sont au format YYYY-MM-DD hh:mm.   Le fichier rapport de campagne est sous la forme d&#39;un fichier zip + contenant un fichier csv contenant le détail des envois. 

    :param keyid: Clé API
    :type keyid: str
    :param rapport_campagne: Doit valoir \&quot;1\&quot;
    :type rapport_campagne: str
    :param date_deb: date de debut au format YYYY-MM-DD hh:mm
    :type date_deb: str
    :param date_fin: date de fin au format YYYY-MM-DD hh:mm
    :type date_fin: str

    """
    return web.Response(status=200)
