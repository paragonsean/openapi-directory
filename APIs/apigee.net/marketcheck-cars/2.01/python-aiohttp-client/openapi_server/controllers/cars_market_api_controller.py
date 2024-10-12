from typing import List, Dict
from aiohttp import web

from openapi_server.models.daily_stats import DailyStats
from openapi_server.models.error import Error
from openapi_server.models.fare_value import FareValue
from openapi_server.models.mds import Mds
from openapi_server.models.popular_cars import PopularCars
from openapi_server.models.price_prediction import PricePrediction
from openapi_server.models.sales import Sales
from openapi_server import util


async def fare_value(request: web.Request, api_key=None, vrm=None, year=None, make=None, model=None, variant=None, miles=None, postal_code=None, radius=None) -> web.Response:
    """Predict fare value of car for UK based on YMMT &amp; miles

    Predict fare value of car for UK based on YMMT &amp; miles

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param vrm: Predict price for a VRM
    :type vrm: str
    :param year: Car manufacturing year
    :type year: int
    :param make: Car&#39;s make
    :type make: str
    :param model: Car&#39;s model
    :type model: str
    :param variant: Car&#39;s variant
    :type variant: str
    :param miles: miles vehicle has driven in total
    :type miles: int
    :param postal_code: Postal code of the car
    :type postal_code: str
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int

    """
    return web.Response(status=200)


async def get_daily_stats(request: web.Request, api_key=None, country=None, car_type=None, ymm=None, ymmt=None, taxonomy_vin=None, vin=None, state=None, city_state=None) -> web.Response:
    """Price, Miles and Days on Market stats

    National, state and city level stats for price, miles and dom

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param country: Country for which the stats are to be searched
    :type country: str
    :param car_type: Inventory type for which stats are to be searched, default is used
    :type car_type: str
    :param ymm: Year, Make, Model of the car, Separated by pipe e.g. ymm&#x3D;2015|ford|f-150
    :type ymm: str
    :param ymmt: Year, Make, Model, Trim of the car, Separated by pipe e.g. ymmt&#x3D;2015|ford|f-150|platinum
    :type ymmt: str
    :param taxonomy_vin: Taxonomy vin for referance to find stats of similar cars
    :type taxonomy_vin: str
    :param vin: VIN that will be transformed to taxonomy_vin
    :type vin: str
    :param state: State level stats
    :type state: str
    :param city_state: City level stats, pipe seperated like city_state&#x3D;jacksonville|FL
    :type city_state: str

    """
    return web.Response(status=200)


async def get_mds(request: web.Request, api_key=None, vin=None, exact=None, latitude=None, longitude=None, radius=None, zip=None, msa_code=None, debug=None, include_sold=None, country=None, state=None, city=None, ymmt=None, car_type=None, lease_term=None, lease_down_payment=None, lease_emp=None, finance_loan_term=None, finance_loan_apr=None, finance_emp=None, finance_down_payment=None, finance_down_payment_per=None, carfax_1_owner=None, carfax_clean_title=None, year=None, make=None, model=None, trim=None, dealer_id=None, source=None, body_type=None, body_subtype=None, vehicle_type=None, cylinders=None, transmission=None, doors=None, drivetrain=None, exterior_color=None, interior_color=None, base_exterior_color=None, base_interior_color=None, engine=None, engine_size=None, engine_aspiration=None, engine_block=None, highway_mpg_range=None, city_mpg_range=None, miles_range=None, price_range=None, msrp_range=None, dom_range=None, dealership_group_name=None, dom_active_range=None, dom_180_range=None, fuel_type=None, dealer_type=None, engine_size_range=None) -> web.Response:
    """Market Days Supply

    Get the basic information on specifications for a car identified by a valid VIN

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param vin: VIN to decode
    :type vin: str
    :param exact: Exact parameter
    :type exact: bool
    :param latitude: Latitude component of location
    :type latitude: float
    :param longitude: Longitude component of location
    :type longitude: float
    :param radius: Radius around the search location (Unit - Miles)
    :type radius: int
    :param zip: To filter listing on ZIP around which they are listed
    :type zip: str
    :param msa_code: To filter listing on msa code in which they are listed
    :type msa_code: str
    :param debug: Debug parameter
    :type debug: bool
    :param include_sold: To fetch sold vins
    :type include_sold: bool
    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param state: To filter listing on State in which they are listed
    :type state: str
    :param city: To filter listing on City in which they are listed
    :type city: str
    :param ymmt: Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations.
    :type ymmt: str
    :param car_type: Car type. Allowed values are - new / used / certified
    :type car_type: str
    :param lease_term: Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60
    :type lease_term: str
    :param lease_down_payment: Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60
    :type lease_down_payment: str
    :param lease_emp: Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60
    :type lease_emp: str
    :param finance_loan_term: Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60
    :type finance_loan_term: str
    :param finance_loan_apr: Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60
    :type finance_loan_apr: str
    :param finance_emp: Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60
    :type finance_emp: str
    :param finance_down_payment: Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60
    :type finance_down_payment: str
    :param finance_down_payment_per: Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60
    :type finance_down_payment_per: str
    :param carfax_1_owner: Indicates whether car has had only one owner or not
    :type carfax_1_owner: str
    :param carfax_clean_title: Indicates whether car has clean ownership records
    :type carfax_clean_title: str
    :param year: To filter listing on their year
    :type year: str
    :param make: To filter listings on their make
    :type make: str
    :param model: To filter listings on their model
    :type model: str
    :param trim: To filter listing on their trim
    :type trim: str
    :param dealer_id: Dealer id to filter the listings.
    :type dealer_id: str
    :param source: To filter listing on their source
    :type source: str
    :param body_type: To filter listing on their body type
    :type body_type: str
    :param body_subtype: Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    :type body_subtype: str
    :param vehicle_type: To filter listing on their vehicle type
    :type vehicle_type: str
    :param cylinders: To filter listing on their cylinders
    :type cylinders: str
    :param transmission: To filter listing on their transmission
    :type transmission: str
    :param doors: Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    :type doors: str
    :param drivetrain: To filter listing on their drivetrain
    :type drivetrain: str
    :param exterior_color: Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    :type exterior_color: str
    :param interior_color: Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    :type interior_color: str
    :param base_exterior_color: Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    :type base_exterior_color: str
    :param base_interior_color: Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    :type base_interior_color: str
    :param engine: To filter listing on their engine
    :type engine: str
    :param engine_size: Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    :type engine_size: str
    :param engine_aspiration: Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    :type engine_aspiration: str
    :param engine_block: Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    :type engine_block: str
    :param highway_mpg_range: Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type highway_mpg_range: str
    :param city_mpg_range: City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type city_mpg_range: str
    :param miles_range: Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    :type miles_range: str
    :param price_range: Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type price_range: str
    :param msrp_range: MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    :type msrp_range: str
    :param dom_range: Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_range: str
    :param dealership_group_name: Name of the dealership group to search for
    :type dealership_group_name: str
    :param dom_active_range: Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_active_range: str
    :param dom_180_range: Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    :type dom_180_range: str
    :param fuel_type: To filter listing on their fuel type
    :type fuel_type: str
    :param dealer_type: Filter based on dealer type independant or franchise
    :type dealer_type: str
    :param engine_size_range: Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    :type engine_size_range: str

    """
    return web.Response(status=200)


async def get_popular_cars(request: web.Request, car_type, api_key=None, state=None, city_state=None, country=None) -> web.Response:
    """Get make model wise top 50 popular cars on national, state, city level

    Get make model wise top 50 popular cars on national, state, city level

    :param car_type: Inventory type for which popular count is to be searched
    :type car_type: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param state: State level sales count
    :type state: str
    :param city_state: City level sales count, pipe seperated like city_state&#x3D;jacksonville|FL
    :type city_state: str
    :param country: Country for which the popular cars are to be searched
    :type country: str

    """
    return web.Response(status=200)


async def get_sales_count(request: web.Request, api_key=None, car_type=None, make=None, mm=None, ymm=None, ymmt=None, taxonomy_vin=None, state=None, city_state=None, vin=None, country=None) -> web.Response:
    """Get sales count by make, model, year, trim or taxonomy vin

    Get a sales count for city, state or national level by make, model, year, trim or taxonomy vin

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param car_type: Inventory type for which sales count is to be searched, default is used
    :type car_type: str
    :param make: Make for which sales count is to be searched
    :type make: str
    :param mm: Make-Model for which sales count is to be searched, pipe seperated like mm&#x3D;ford|f-150
    :type mm: str
    :param ymm: Year-Make-Model for which sales count is to be searched, pipe seperated like ymm&#x3D;2015|ford|f-150
    :type ymm: str
    :param ymmt: Year-Make-Model-Trim for which sales count is to be searched, pipe seperated like ymmt&#x3D;2015|ford|f-150|platinum
    :type ymmt: str
    :param taxonomy_vin: taxonomy_vin for which sales count is to be searched
    :type taxonomy_vin: str
    :param state: State level sales count
    :type state: str
    :param city_state: City level sales count, pipe seperated like city_state&#x3D;jacksonville|FL
    :type city_state: str
    :param vin: VIN that will be transformed to taxonomy_vin
    :type vin: str
    :param country: Country for which the sales records are to be searched
    :type country: str

    """
    return web.Response(status=200)


async def predict_car_price(request: web.Request, car_type, api_key=None, vin=None, year=None, make=None, model=None, trim=None, is_certified=None, carfax_1_owner=None, carfax_clean_title=None, base_exterior_color=None, base_interior_color=None, transmission=None, drivetrain=None, engine_size=None, engine_block=None, cylinders=None, doors=None, highway_mpg=None, city_mpg=None, latitude=None, longitude=None, miles=None, zip=None, country=None) -> web.Response:
    """Predict car price based on it&#39;s specifications

    Predict car price based on it&#39;s specifications

    :param car_type: Car condition
    :type car_type: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param vin: Predict price for a VIN
    :type vin: str
    :param year: Car manufacturing year
    :type year: int
    :param make: Car&#39;s make
    :type make: str
    :param model: Car&#39;s model
    :type model: str
    :param trim: Car&#39;s trim
    :type trim: str
    :param is_certified: Boolean to indicate car is certified or not
    :type is_certified: bool
    :param carfax_1_owner: Boolean to indicate car is carfax one owner or not
    :type carfax_1_owner: bool
    :param carfax_clean_title: Boolean to indicate car has clean title or not
    :type carfax_clean_title: bool
    :param base_exterior_color: Base exterior color of the car
    :type base_exterior_color: str
    :param base_interior_color: Base interior color of the car
    :type base_interior_color: str
    :param transmission: Transmission on the car
    :type transmission: str
    :param drivetrain: Drivetrain on the car
    :type drivetrain: str
    :param engine_size: Engine Size of the car
    :type engine_size: 
    :param engine_block: Engine Block of the car
    :type engine_block: str
    :param cylinders: Number of cylinders in the vehicle
    :type cylinders: int
    :param doors: Number of doors in the vehicle
    :type doors: int
    :param highway_mpg: Highway mileage
    :type highway_mpg: int
    :param city_mpg: City mileage of the car
    :type city_mpg: int
    :param latitude: Latitude component of the location
    :type latitude: 
    :param longitude: Longitude component of the location
    :type longitude: 
    :param miles: miles vehicle has driven in total
    :type miles: int
    :param zip: Location zip
    :type zip: str
    :param country: Country for which car price will be predicted
    :type country: str

    """
    return web.Response(status=200)


async def predict_uk_car_price(request: web.Request, api_key=None, vrm=None, year=None, make=None, model=None, trim=None, base_exterior_color=None, transmission=None, drivetrain=None, engine_size=None, cylinders=None, doors=None, fuel_type=None, highway_mpg=None, city_mpg=None, combined_mpg=None, latitude=None, longitude=None, miles=None, zip=None) -> web.Response:
    """Predict car price for UK based on it&#39;s specifications

    Predict car price for UK based on it&#39;s specifications

    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param vrm: Predict price for a VRM
    :type vrm: str
    :param year: Car manufacturing year
    :type year: int
    :param make: Car&#39;s make
    :type make: str
    :param model: Car&#39;s model
    :type model: str
    :param trim: Car&#39;s trim
    :type trim: str
    :param base_exterior_color: Base exterior color of the car
    :type base_exterior_color: str
    :param transmission: Transmission on the car
    :type transmission: str
    :param drivetrain: Drivetrain on the car
    :type drivetrain: str
    :param engine_size: Engine Size of the car
    :type engine_size: float
    :param cylinders: Number of cylinders in the vehicle
    :type cylinders: int
    :param doors: Number of doors in the vehicle
    :type doors: int
    :param fuel_type: Fuel type of the car
    :type fuel_type: str
    :param highway_mpg: Highway mileage
    :type highway_mpg: float
    :param city_mpg: City mileage of the car
    :type city_mpg: float
    :param combined_mpg: Combiined mileage of the car
    :type combined_mpg: float
    :param latitude: Latitude component of the location
    :type latitude: 
    :param longitude: Longitude component of the location
    :type longitude: 
    :param miles: miles vehicle has driven in total
    :type miles: int
    :param zip: Location zip
    :type zip: str

    """
    return web.Response(status=200)
