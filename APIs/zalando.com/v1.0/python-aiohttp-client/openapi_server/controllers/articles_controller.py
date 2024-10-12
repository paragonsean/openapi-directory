from typing import List, Dict
from aiohttp import web

from openapi_server.models.article import Article
from openapi_server.models.article_media import ArticleMedia
from openapi_server.models.article_review import ArticleReview
from openapi_server.models.article_reviews import ArticleReviews
from openapi_server.models.article_reviews_summaries import ArticleReviewsSummaries
from openapi_server.models.article_reviews_summary import ArticleReviewsSummary
from openapi_server.models.article_unit import ArticleUnit
from openapi_server.models.articles import Articles
from openapi_server.models.error_message import ErrorMessage
from openapi_server import util


async def article_reviews_get(request: web.Request, article_id=None, article_model_id=None, min_star_rating=None, max_star_rating=None, sort=None, page=None, page_size=None, accept_language=None, fields=None) -> web.Response:
    """Get Article Reviews

    Zalando API Article Reviews Schema

    :param article_id: Article IDs. A list of config SKUs for which the article reviews will be returned. Required if articleModelId is empty. 
    :type article_id: List[str]
    :param article_model_id: Article model IDs. A list of model SKUs for which the article reviews will be returned. Required if articleId is empty. 
    :type article_model_id: List[str]
    :param min_star_rating: To get reviews with minimum star rating.
    :type min_star_rating: str
    :param max_star_rating: To get reviews with maximum star rating.
    :type max_star_rating: str
    :param sort: articles are sorted on reviews provided by customers (eg: best)
    :type sort: str
    :param page: to request with required page number or pagination
    :type page: str
    :param page_size: to request with required page size in a page
    :type page_size: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)


async def article_reviews_review_id_get(request: web.Request, review_id, accept_language=None, fields=None) -> web.Response:
    """Get Article Reviews by reviewId

    Zalando API ArticleReviews Schema

    :param review_id: To get unique review by review Id.
    :type review_id: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)


async def article_reviews_summaries_article_model_id_get(request: web.Request, article_model_id, accept_language=None, fields=None) -> web.Response:
    """Get Article Reviews Summaries by articleModelId

    Zalando API ArticleReviewsSummaries Schema

    :param article_model_id: To get unique reviews summary from article model Id.
    :type article_model_id: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)


async def article_reviews_summaries_get(request: web.Request, article_model_id, page=None, page_size=None, accept_language=None, fields=None) -> web.Response:
    """Get Article Reviews Summaries

    Zalando API Article Reviews Summaries Schema

    :param article_model_id: Article model IDs. A list of model SKUs for which the article review summaries will be returned.
    :type article_model_id: List[str]
    :param page: to request with required page number or pagination
    :type page: str
    :param page_size: to request with required page size in a page
    :type page_size: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)


async def articles_article_id_get(request: web.Request, article_id, accept_language=None, fields=None) -> web.Response:
    """Get Article by articleId

    Zalando API Article Schema

    :param article_id: To get unique article for article Id.
    :type article_id: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)


async def articles_article_id_media_get(request: web.Request, article_id, accept_language=None, fields=None) -> web.Response:
    """Get Article media by articleId

    Zalando API Article Schema

    :param article_id: To get unique article for article Id media.
    :type article_id: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)


async def articles_article_id_reviews_get(request: web.Request, article_id, min_star_rating=None, max_star_rating=None, sort=None, page=None, page_size=None, accept_language=None, fields=None) -> web.Response:
    """Get Article reviews by articleId

    Zalando API Article Schema

    :param article_id: To get unique article for article Id reviews.
    :type article_id: str
    :param min_star_rating: To get reviews with minimum star rating.
    :type min_star_rating: str
    :param max_star_rating: To get reviews with maximum star rating.
    :type max_star_rating: str
    :param sort: articles are sorted on reviews provided by customers (eg: best)
    :type sort: str
    :param page: to request with required page number or pagination
    :type page: str
    :param page_size: to request with required page size in a page
    :type page_size: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)


async def articles_article_id_reviews_summary_get(request: web.Request, article_id, accept_language=None, fields=None) -> web.Response:
    """Get Article reviews summary by articleId

    Zalando API Article Schema

    :param article_id: To get unique article for article Id reviews summary.
    :type article_id: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)


async def articles_article_id_units_get(request: web.Request, article_id, accept_language=None, fields=None) -> web.Response:
    """Get Article units by articleId

    Zalando API Article Schema

    :param article_id: To get unique article for article Id units.
    :type article_id: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)


async def articles_article_id_units_unit_id_get(request: web.Request, article_id, unit_id, accept_language=None, fields=None) -> web.Response:
    """Get Article units by articleId snd unitId

    Zalando API Article Schema

    :param article_id: To get unique article for article Id.
    :type article_id: str
    :param unit_id: To get unique article for article Id unit.
    :type unit_id: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)


async def articles_get(request: web.Request, article_id=None, article_model_id=None, article_unit_id=None, activation_date=None, age_group=None, assortment_area=None, brand=None, brandfamily=None, category=None, color=None, den=None, filling=None, full_text=None, gender=None, heel_form=None, heel_height=None, length=None, occasion=None, pattern=None, price=None, sale=None, season=None, shaft_height=None, shaft_width=None, shirt_collar=None, shoe_fastener=None, shoe_toecap=None, shop_area=None, size=None, sports=None, technology=None, trouser_rise=None, upper_material=None, volume=None, page=None, page_size=None, sort=None, accept_language=None, fields=None) -> web.Response:
    """Search for Articles

    Search for articles based on various different possible filter like e.g. the &#x60;brandFamily&#x60;, the &#x60;catagory&#x60; or a specific &#x60;color&#x60;. See [Filters](https://todo) for a list of all available filter options.  The default &#x60;pageSize&#x60; for responses is set to &#x60;20&#x60;. You can add a &#x60;pageSize&#x60; request parameter to adjust that. Please keep in mind that the maximum &#x60;pageSize&#x60; for this resource is &#x60;200&#x60;.  The endpoint also supports reducing the fields returned for each article via the &#x60;fields&#x60; parameter. Please refer to [fields parameter](https://todo) for more details.

    :param article_id: The &#x60;articleIds&#x60; to use use for filtering.  One or more &#x60;articleIds&#x60; might be used as a filter criteria. Submit multiple &#x60;articleId&#x60; request parameters for more than one to be used. They will be treated as &#x60;OR&#x60; criteria.
    :type article_id: List[str]
    :param article_model_id: filters by article ModelId
    :type article_model_id: List[str]
    :param article_unit_id: filters by article&#39;s unit id
    :type article_unit_id: List[str]
    :param activation_date: period or time the articles are activated for selling in the shop
    :type activation_date: List[str]
    :param age_group: filters by age group (eg: kids)
    :type age_group: List[str]
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
    :param full_text: filters by text (eg: search by &#39;as&#39; gives result with articles of brand Sass)
    :type full_text: str
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
    :param page: to request with required page number or pagination
    :type page: str
    :param page_size: to request with required page size in a page
    :type page_size: str
    :param sort: sorting order (eg: popularity)
    :type sort: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)
