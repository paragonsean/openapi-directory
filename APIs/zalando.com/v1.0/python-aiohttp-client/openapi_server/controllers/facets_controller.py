from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.facet import Facet
from openapi_server import util


async def facets_get(request: web.Request, age_group=None, article_id=None, activation_date=None, article_model_id=None, assortment_area=None, brand=None, brandfamily=None, category=None, color=None, den=None, filling=None, gender=None, heel_form=None, heel_height=None, length=None, occasion=None, pattern=None, price=None, sale=None, season=None, shaft_height=None, shaft_width=None, shirt_collar=None, shoe_fastener=None, shoe_toecap=None, shop_area=None, size=None, sports=None, technology=None, trouser_rise=None, upper_material=None, volume=None, accept_language=None, fields=None) -> web.Response:
    """Shop Facets

    Zalando API Facets Schema

    :param age_group: filters by age group (eg: kids)
    :type age_group: List[str]
    :param article_id: The &#x60;articleIds&#x60; to use use for filtering.  One or more &#x60;articleIds&#x60; might be used as a filter criteria. Submit multiple &#x60;articleId&#x60; request parameters for more than one to be used. They will be treated as &#x60;OR&#x60; criteria.
    :type article_id: List[str]
    :param activation_date: period or time the articles are activated for selling in the shop
    :type activation_date: List[str]
    :param article_model_id: filters by article ModelId
    :type article_model_id: List[str]
    :param assortment_area: filters by classification of articles (eg: maternity) 
    :type assortment_area: List[str]
    :param brand: filters by brand key given by user (eg: SA5)
    :type brand: List[str]
    :param brandfamily: filters by brand family key (eg: nike) 
    :type brandfamily: List[str]
    :param category: filters by category (eg: Socks, Rain Coats)
    :type category: List[str]
    :param color: filters by color (eg: red, blue)
    :type color: List[str]
    :param den: filters by den 
    :type den: List[str]
    :param filling: filters by different kinds of garment filling materials (eg: satin, wolle)
    :type filling: List[str]
    :param gender: filters by gender
    :type gender: List[str]
    :param heel_form: filters by heel form (eg: flat)
    :type heel_form: List[str]
    :param heel_height: filters by height of the heel size or length (eg: xs)
    :type heel_height: List[str]
    :param length: filters by garments length (eg: 3/4 length, knee-length)
    :type length: str
    :param occasion: filters by type of occasion (eg: party, business)
    :type occasion: List[str]
    :param pattern: filters by pattern on the garments (eg: animal print, plain)
    :type pattern: List[str]
    :param price: filters all articles in price range (eg: 9-90)
    :type price: str
    :param sale: filters discounted articles marked as sale
    :type sale: List[str]
    :param season: filters by season (Autumn/Winter or Spring/Summer)
    :type season: List[str]
    :param shaft_height: filters by shaft height (eg: s, xs)
    :type shaft_height: List[str]
    :param shaft_width: filters by shaft width (eg: s, l)
    :type shaft_width: List[str]
    :param shirt_collar: filters by shirt collar styles (eg: low V neck, lined collar)
    :type shirt_collar: List[str]
    :param shoe_fastener: filters by shoe fastener types (eg: buckle, lacing)
    :type shoe_fastener: List[str]
    :param shoe_toecap: filters by shoe toe cap variants (eg: pointed, square)
    :type shoe_toecap: List[str]
    :param shop_area: filters by classification of articles
    :type shop_area: List[str]
    :param size: filters by size
    :type size: str
    :param sports: filters by different sport activities (eg: football)
    :type sports: List[str]
    :param technology: filters by technology used to produce the articles
    :type technology: List[str]
    :param trouser_rise: filters by trouser rise
    :type trouser_rise: List[str]
    :param upper_material: filters by different type of upper material used on garments (eg: lace)
    :type upper_material: List[str]
    :param volume: filters by volume
    :type volume: List[str]
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)
