/**
 * IdealSpot GeoData
 * Hyperlocal Demographics, Vehicle Traffic, Economic, Market Signals, and More. Use this API to request IdealSpot hyperlocal geospatial market insight and geometry data.   ## Detailed Description  Use this API as your **local economy microscope** by querying [IdealSpot](https://www.idealspot.com) hyperlocal market insight and geometry data. We offer the most precise, extensive, and frequently-updated local market data in the US. Our data is available across the entire US and can be queried at geographic scales ranging from the micro (Census block) through the macro (nation).  Better data and analysis leads to a better understanding of local market opportunities and risks. Integrate with your commercial real estate and marketing applications, machine learning workflows, and other investment analytics.  Our goal is to offer the most complete snapshot of the geographically distributed consumer and retail economy. We start with the fundamentals of consumers and business establishments. To connect retailers with consumers, we provide mobility data like vehicle traffic and mobile device data. To describe consumer intent, we provide geolocated digital marketing data.   We believe that accurate capital allocation through reliable local market data is foundational to creating robust, healthy, and livable communities for all. We hope you and your clients find tremendous value in this service.  ## Features  Query data and GeoJSON geometries at these scales for any US latitude and longitude:  * Rings (0.5 km+) * Drive time (1-60 minutes) * Bike time (3-60 minutes) * Walk time (5-60 minutes) * Public transit time (5-60 minutes) * Administrative region (US, states, core-based statistical areas, counties, Census-designated places, Census tracts, zipcodes, Census block groups, opportunity zones)  | Data Feature | Description | | ------- | ------------------------------| | Demographics, Housing, Spending | *Updated Quarterly*.  Current and historical market data including population, spending, and housing. Vendor (PopStats) is relied upon by Walgreens, Ulta Beauty, Blackstone, etc | | Labor, Business Establishments, Economic Conditions | *Updated Quarterly*.  Traditional market data including workforce, business establishment counts, and economic conditions like local GDP, unemployment rates. Vendor (PopStats) is relied upon by Walgreens, Ulta Beauty, Blackstone, etc | | Consumer segmentation | *Updated Annually*. Demographics grouped into narrative-oriented segments. | | Vehicle Traffic | *Updated semi-annually*. Gold standard in vehicle traffic data from INRIX. Counts by day of week, time of day and side of street. | | Rings and Travel time polygons | *Estimate in Real-time*. Rings alongside drive time, walk time, bike time, and public transit time polygons. Request as GeoJSON geometries for mapping or use with data queries | | Administrative region polygons | *Updated Annually*. GeoJSON administrative regions from US Census Bureau: block groups, tracts, counties, CBSAs, states, opportunity zones, USPS zipcodes | | Internet Search Volumes | 30 day rolling averages for geolocated advertising potential across 450 business categories from major search engines | | Social Media Interest | 30 day rolling average for geolocated advertising potential across 450 business categories from major social networks |  ### Coming Soon!  This API powers our local market research platform at [IdealSpot.com](https://www.idealspot.com). The functionality exposed so far is only a portion of our current capabilities. We will be exposing additional API features in time so watch this space!  | Data Feature | Description | | ------- | ------------------------------| Mobile device visit counts, points of interest, brands | Fresh point of interest data across 3000+ brands, millions of POI, and historical foot traffic counts using mobile data for those points of interest Origin/destination trips from mobile devices | Map origins and destinations of devices visiting an arbitrary catchment area Competition search | Search all major point-of-interest aggregators in one query Environment/climate | Expected weather patterns like temperature and precipitation Filter search API | Query data for all counties in state, all tracts in MSA, etc Road segment tiles | Plot road segments on maps in interactive applications  ## Developer Website  For more detail see https://developer.idealspot.com/
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Autocomplete from './model/Autocomplete';
import Category from './model/Category';
import Crs from './model/Crs';
import Data from './model/Data';
import Data1 from './model/Data1';
import Data2 from './model/Data2';
import Data3 from './model/Data3';
import Data4 from './model/Data4';
import Data5 from './model/Data5';
import Datum from './model/Datum';
import DescribeOccupationInsight from './model/DescribeOccupationInsight';
import Describetheregionwithin5minutedriveTimeofageographicpoint from './model/Describetheregionwithin5minutedriveTimeofageographicpoint';
import Feature from './model/Feature';
import Feature1 from './model/Feature1';
import FetchAdministrativeRegionsusingLatLng from './model/FetchAdministrativeRegionsusingLatLng';
import Geometry from './model/Geometry';
import Homevalueswithin1miRadiusofLocation from './model/Homevalueswithin1miRadiusofLocation';
import ListAllLocalInsights from './model/ListAllLocalInsights';
import Location1 from './model/Location1';
import Location3 from './model/Location3';
import LocationArray from './model/LocationArray';
import LocationArray2 from './model/LocationArray2';
import Metadata from './model/Metadata';
import Metadata1 from './model/Metadata1';
import Parameters from './model/Parameters';
import Properties from './model/Properties';
import Properties1 from './model/Properties1';
import Properties2 from './model/Properties2';
import Properties3 from './model/Properties3';
import Properties4 from './model/Properties4';
import Roadsegment from './model/Roadsegment';
import SearchRoadSegments from './model/SearchRoadSegments';
import Stats from './model/Stats';
import Units from './model/Units';
import VehicleTrafficCountsforRoadSegment from './model/VehicleTrafficCountsforRoadSegment';
import GeometriesAPIApi from './api/GeometriesAPIApi';
import InsightsAPIApi from './api/InsightsAPIApi';
import TrafficCountAPIApi from './api/TrafficCountAPIApi';


/**
* Hyperlocal Demographics, Vehicle Traffic, Economic, Market Signals, and More. Use this API to request IdealSpot hyperlocal geospatial market insight and geometry data.   ## Detailed Description  Use this API as your **local economy microscope** by querying [IdealSpot](https://www.idealspot.com) hyperlocal market insight and geometry data. We offer the most precise, extensive, and frequently-updated local market data in the US. Our data is available across the entire US and can be queried at geographic scales ranging from the micro (Census block) through the macro (nation).  Better data and analysis leads to a better understanding of local market opportunities and risks. Integrate with your commercial real estate and marketing applications, machine learning workflows, and other investment analytics.  Our goal is to offer the most complete snapshot of the geographically distributed consumer and retail economy. We start with the fundamentals of consumers and business establishments. To connect retailers with consumers, we provide mobility data like vehicle traffic and mobile device data. To describe consumer intent, we provide geolocated digital marketing data.   We believe that accurate capital allocation through reliable local market data is foundational to creating robust, healthy, and livable communities for all. We hope you and your clients find tremendous value in this service.  ## Features  Query data and GeoJSON geometries at these scales for any US latitude and longitude:  * Rings (0.5 km+) * Drive time (1-60 minutes) * Bike time (3-60 minutes) * Walk time (5-60 minutes) * Public transit time (5-60 minutes) * Administrative region (US, states, core-based statistical areas, counties, Census-designated places, Census tracts, zipcodes, Census block groups, opportunity zones)  | Data Feature | Description | | ------- | ------------------------------| | Demographics, Housing, Spending | *Updated Quarterly*.  Current and historical market data including population, spending, and housing. Vendor (PopStats) is relied upon by Walgreens, Ulta Beauty, Blackstone, etc | | Labor, Business Establishments, Economic Conditions | *Updated Quarterly*.  Traditional market data including workforce, business establishment counts, and economic conditions like local GDP, unemployment rates. Vendor (PopStats) is relied upon by Walgreens, Ulta Beauty, Blackstone, etc | | Consumer segmentation | *Updated Annually*. Demographics grouped into narrative-oriented segments. | | Vehicle Traffic | *Updated semi-annually*. Gold standard in vehicle traffic data from INRIX. Counts by day of week, time of day and side of street. | | Rings and Travel time polygons | *Estimate in Real-time*. Rings alongside drive time, walk time, bike time, and public transit time polygons. Request as GeoJSON geometries for mapping or use with data queries | | Administrative region polygons | *Updated Annually*. GeoJSON administrative regions from US Census Bureau: block groups, tracts, counties, CBSAs, states, opportunity zones, USPS zipcodes | | Internet Search Volumes | 30 day rolling averages for geolocated advertising potential across 450 business categories from major search engines | | Social Media Interest | 30 day rolling average for geolocated advertising potential across 450 business categories from major social networks |  ### Coming Soon!  This API powers our local market research platform at [IdealSpot.com](https://www.idealspot.com). The functionality exposed so far is only a portion of our current capabilities. We will be exposing additional API features in time so watch this space!  | Data Feature | Description | | ------- | ------------------------------| Mobile device visit counts, points of interest, brands | Fresh point of interest data across 3000+ brands, millions of POI, and historical foot traffic counts using mobile data for those points of interest Origin/destination trips from mobile devices | Map origins and destinations of devices visiting an arbitrary catchment area Competition search | Search all major point-of-interest aggregators in one query Environment/climate | Expected weather patterns like temperature and precipitation Filter search API | Query data for all counties in state, all tracts in MSA, etc Road segment tiles | Plot road segments on maps in interactive applications  ## Developer Website  For more detail see https://developer.idealspot.com/.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var IdealSpotGeoData = require('index'); // See note below*.
* var xxxSvc = new IdealSpotGeoData.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new IdealSpotGeoData.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new IdealSpotGeoData.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new IdealSpotGeoData.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Autocomplete model constructor.
     * @property {module:model/Autocomplete}
     */
    Autocomplete,

    /**
     * The Category model constructor.
     * @property {module:model/Category}
     */
    Category,

    /**
     * The Crs model constructor.
     * @property {module:model/Crs}
     */
    Crs,

    /**
     * The Data model constructor.
     * @property {module:model/Data}
     */
    Data,

    /**
     * The Data1 model constructor.
     * @property {module:model/Data1}
     */
    Data1,

    /**
     * The Data2 model constructor.
     * @property {module:model/Data2}
     */
    Data2,

    /**
     * The Data3 model constructor.
     * @property {module:model/Data3}
     */
    Data3,

    /**
     * The Data4 model constructor.
     * @property {module:model/Data4}
     */
    Data4,

    /**
     * The Data5 model constructor.
     * @property {module:model/Data5}
     */
    Data5,

    /**
     * The Datum model constructor.
     * @property {module:model/Datum}
     */
    Datum,

    /**
     * The DescribeOccupationInsight model constructor.
     * @property {module:model/DescribeOccupationInsight}
     */
    DescribeOccupationInsight,

    /**
     * The Describetheregionwithin5minutedriveTimeofageographicpoint model constructor.
     * @property {module:model/Describetheregionwithin5minutedriveTimeofageographicpoint}
     */
    Describetheregionwithin5minutedriveTimeofageographicpoint,

    /**
     * The Feature model constructor.
     * @property {module:model/Feature}
     */
    Feature,

    /**
     * The Feature1 model constructor.
     * @property {module:model/Feature1}
     */
    Feature1,

    /**
     * The FetchAdministrativeRegionsusingLatLng model constructor.
     * @property {module:model/FetchAdministrativeRegionsusingLatLng}
     */
    FetchAdministrativeRegionsusingLatLng,

    /**
     * The Geometry model constructor.
     * @property {module:model/Geometry}
     */
    Geometry,

    /**
     * The Homevalueswithin1miRadiusofLocation model constructor.
     * @property {module:model/Homevalueswithin1miRadiusofLocation}
     */
    Homevalueswithin1miRadiusofLocation,

    /**
     * The ListAllLocalInsights model constructor.
     * @property {module:model/ListAllLocalInsights}
     */
    ListAllLocalInsights,

    /**
     * The Location1 model constructor.
     * @property {module:model/Location1}
     */
    Location1,

    /**
     * The Location3 model constructor.
     * @property {module:model/Location3}
     */
    Location3,

    /**
     * The LocationArray model constructor.
     * @property {module:model/LocationArray}
     */
    LocationArray,

    /**
     * The LocationArray2 model constructor.
     * @property {module:model/LocationArray2}
     */
    LocationArray2,

    /**
     * The Metadata model constructor.
     * @property {module:model/Metadata}
     */
    Metadata,

    /**
     * The Metadata1 model constructor.
     * @property {module:model/Metadata1}
     */
    Metadata1,

    /**
     * The Parameters model constructor.
     * @property {module:model/Parameters}
     */
    Parameters,

    /**
     * The Properties model constructor.
     * @property {module:model/Properties}
     */
    Properties,

    /**
     * The Properties1 model constructor.
     * @property {module:model/Properties1}
     */
    Properties1,

    /**
     * The Properties2 model constructor.
     * @property {module:model/Properties2}
     */
    Properties2,

    /**
     * The Properties3 model constructor.
     * @property {module:model/Properties3}
     */
    Properties3,

    /**
     * The Properties4 model constructor.
     * @property {module:model/Properties4}
     */
    Properties4,

    /**
     * The Roadsegment model constructor.
     * @property {module:model/Roadsegment}
     */
    Roadsegment,

    /**
     * The SearchRoadSegments model constructor.
     * @property {module:model/SearchRoadSegments}
     */
    SearchRoadSegments,

    /**
     * The Stats model constructor.
     * @property {module:model/Stats}
     */
    Stats,

    /**
     * The Units model constructor.
     * @property {module:model/Units}
     */
    Units,

    /**
     * The VehicleTrafficCountsforRoadSegment model constructor.
     * @property {module:model/VehicleTrafficCountsforRoadSegment}
     */
    VehicleTrafficCountsforRoadSegment,

    /**
    * The GeometriesAPIApi service constructor.
    * @property {module:api/GeometriesAPIApi}
    */
    GeometriesAPIApi,

    /**
    * The InsightsAPIApi service constructor.
    * @property {module:api/InsightsAPIApi}
    */
    InsightsAPIApi,

    /**
    * The TrafficCountAPIApi service constructor.
    * @property {module:api/TrafficCountAPIApi}
    */
    TrafficCountAPIApi
};
