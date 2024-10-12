from typing import List, Dict
from aiohttp import web

from openapi_server.models.entity_data import EntityData
from openapi_server.models.error import Error
from openapi_server import util


async def entities_get(request: web.Request, ) -> web.Response:
    """Obtiene el listado de entidades soportadas

    Obtiene el listado de entidades soportadas y la información necesaria para dibujar el formulario de login de la entidad. 


    """
    return web.Response(status=200)


async def entities_post(request: web.Request, otp=None, session=None, api_key=None, code=None, contract_code=None, document_type=None, password=None, second_password=None, token=None, tokenize=None, user=None) -> web.Response:
    """Obtiene los activos financieros y el detalle de su composición

    Obtiene los activos financieros y el detalle de su composición de carteras de inversión compuestas por acciones o fondos, tarjetas de crédito, seguros y préstamos. Incluye información de titularidad de cada uno de los activos así como identificadores únicos que facilitan el tratamiento del dato. Es posible obtener datos Mock. Consulte con el equipo técnico cómo hacerlo. 

    :param otp: Solo necesario cuando se esté completando la seguda petición de un login con 2 factores de autenticación, si el tipo de desafío es OTP. Requiere la clave que la entidad le ha enviado al usario final
    :type otp: str
    :param session: Solo necesario cuando se esté completando la seguda petición de un login con 2 factores de autenticación. Requiere el valor de SESSION obtenido en la primera petición
    :type session: str
    :param api_key: Identifica al cliente en el servicio
    :type api_key: str
    :param code: Nombre de la entidad. El listado completo está disponible con GET
    :type code: str
    :param contract_code: Solo necesario cuando el usuario puede acceder a más de un contrato. El listado de contratos disponibles se obtiene al realizar una conexión con un usuario con opción a trabajar con varios contratos en su entidad (que al hacer login en su banca online ve como primera opción una pantalla de selección de contratos) y cuya llamada a la API no se le ha especificado un valor a contract_code
    :type contract_code: str
    :param document_type: Tipo de documento, requerido según la entidad. Si es requerido o no, está indicado en el listado de entidades. Ver definición.
    :type document_type: str
    :param password: Contraseña
    :type password: str
    :param second_password: Segunda contraseña, requerida según la entidad.
    :type second_password: str
    :param token: Valor para credenciales custodiadas, tokenizadas previamente mediante una llamada a este método con el valor de tokenize&#x3D;true. Están disponibles los siguientes usuarios Mock: MOCKDATA, respuesta OK; MOCKOTP, respuesta con desafío OTP; MOCKLOGINKO, respuesta con error de login
    :type token: str
    :param tokenize: Indica si Wealth Reader debe custodiar los credenciales, de tal manera que incluído en el body de respuesta estará un token que permite conectar con la entidad sin necesidad de conocer los credenciales: document_type, user, password, second_password, contract_code
    :type tokenize: bool
    :param user: Usuario. Están disponibles los siguientes usuarios Mock: MOCKDATA, respuesta OK; MOCKOTP, respuesta con desafío OTP; MOCKLOGINKO, respuesta con error de login
    :type user: str

    """
    return web.Response(status=200)


async def error_codes_get(request: web.Request, lang=None) -> web.Response:
    """Listado de códigos de error

    Listado de códigos de error. Presta especial atención a que no todos los códigos de error deben recibir el mismo tratamiento por parte de tu aplicación. Ante un error de password incorrecto no debes reintentar la llamada con los mismos parámetros, pero ante un error que te indique que la entidad está en mantenimiento sí puedes reintentarlo. Pide una sesión técnica con nuestro equipo para resolver cualquier duda sobre la gestión de errores. 

    :param lang: Idioma de la respuesta
    :type lang: str

    """
    return web.Response(status=200)
