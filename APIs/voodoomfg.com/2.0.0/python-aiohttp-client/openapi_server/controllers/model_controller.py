from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_model_body import CreateModelBody
from openapi_server.models.model import Model
from openapi_server.models.model_quote import ModelQuote
from openapi_server import util


async def model_get(request: web.Request, ) -> web.Response:
    """Retrieve the models you&#39;ve created. 

    Lists all of the models you&#39;ve created. 


    """
    return web.Response(status=200)


async def model_model_id_get(request: web.Request, model_id) -> web.Response:
    """Retrieve a previously created model by its id. 

    In cases where you&#39;re ordering models you&#39;ve created previously, you can fetch a specific model by its id. 

    :param model_id: 
    :type model_id: int

    """
    return web.Response(status=200)


async def model_post(request: web.Request, body) -> web.Response:
    """Models represent 3D design files that you&#39;d like to produce. Creating models is generally the first step in creating an order. 

    Downloads the model data from the URL specified by file_url and saves it as a model. As a part of the model upload process, the file is run through a program that repairs the mesh (closing holes, flipping inverted normals, etc). In some cases, this may alter the geometry of your model. If you&#39;re noticing bad results for your created models, you might consider repairing your files before submitting them. 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateModelBody.from_dict(body)
    return web.Response(status=200)


async def model_quote_attrs_get(request: web.Request, x, y, z, volume, surface_area, material_id, quantity, units, options_orientation=None) -> web.Response:
    """Get a quote for a model with the given attributes. 

    This endpoint will provide a quote for a model matching the submitted parameters. Note that this quote may be different than the quote provided by /model/quote in the case that your attribute calculations differ from the ones used by Voodoo Manufacturing. 

    :param x: The calculated unitless x dimension of this model&#39;s bounding box.
    :type x: 
    :param y: The calculated unitless y dimension of this model&#39;s bounding box.
    :type y: 
    :param z: The calculated unitless z dimension of this model&#39;s bounding box.
    :type z: 
    :param volume: The calculated unitless volume of the model.
    :type volume: 
    :param surface_area: The calculated unitless surface area of the model.
    :type surface_area: 
    :param material_id: The unique id of the desired material.
    :type material_id: 
    :param quantity: The number of units in this quote.
    :type quantity: 
    :param units: The units of the model file. Either \&quot;mm\&quot;, \&quot;cm\&quot;, or \&quot;in\&quot;. The correct value to pass here depends on which design program you&#39;re using. Defaults to \&quot;mm\&quot;.
    :type units: str
    :param options_orientation: Indicates whether or not this model needs to be oriented prior to printing. If your model is already oriented for 3D printing, you can omit this flag (or set it to false) and it will not be re-oriented prior to printing. If true, it will be re-oriented prior to printing. If you&#39;re not sure if your model is oriented, you should set this flag to true. There is an additional charge for orientation.
    :type options_orientation: bool

    """
    return web.Response(status=200)


async def model_quote_get(request: web.Request, model_id, material_id, quantity, units, options_orientation=None) -> web.Response:
    """Get a quote a given model id. 

    Calculates a quote for the given model in the given material and quantity. This endpoint required that you&#39;ve already uploaded the model to our servers -- to get a quote for a model you haven&#39;t yet uploaded, you can try /model/quote_attrs. 

    :param model_id: The unique id of the model you&#39;d like to quote.
    :type model_id: int
    :param material_id: The unique id of the desired material.
    :type material_id: 
    :param quantity: The number of units in this quote.
    :type quantity: 
    :param units: The units of the model file. Either \&quot;mm\&quot;, \&quot;cm\&quot;, or \&quot;in\&quot;. The correct value to pass here depends on which design program you&#39;re using. Defaults to \&quot;mm\&quot;.
    :type units: str
    :param options_orientation: Indicates whether or not this model needs to be oriented prior to printing. If your model is already oriented for 3D printing, you can omit this flag (or set it to false) and it will not be re-oriented prior to printing. If true, it will be re-oriented prior to printing. If you&#39;re not sure if your model is oriented, you should set this flag to true. There is an additional charge for orientation.
    :type options_orientation: bool

    """
    return web.Response(status=200)
