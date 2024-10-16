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

import ApiClient from '../ApiClient';

/**
 * The Metadata1 model module.
 * @module model/Metadata1
 * @version 1.0
 */
class Metadata1 {
    /**
     * Constructs a new <code>Metadata1</code>.
     * @alias module:model/Metadata1
     * @param bearing {String} 
     * @param columns {Array.<String>} 
     * @param name {String} 
     * @param rows {Array.<String>} 
     * @param segmentId {String} 
     * @param state {String} 
     */
    constructor(bearing, columns, name, rows, segmentId, state) { 
        
        Metadata1.initialize(this, bearing, columns, name, rows, segmentId, state);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, bearing, columns, name, rows, segmentId, state) { 
        obj['bearing'] = bearing;
        obj['columns'] = columns;
        obj['name'] = name;
        obj['rows'] = rows;
        obj['segment_id'] = segmentId;
        obj['state'] = state;
    }

    /**
     * Constructs a <code>Metadata1</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Metadata1} obj Optional instance to populate.
     * @return {module:model/Metadata1} The populated <code>Metadata1</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Metadata1();

            if (data.hasOwnProperty('bearing')) {
                obj['bearing'] = ApiClient.convertToType(data['bearing'], 'String');
            }
            if (data.hasOwnProperty('columns')) {
                obj['columns'] = ApiClient.convertToType(data['columns'], ['String']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('rows')) {
                obj['rows'] = ApiClient.convertToType(data['rows'], ['String']);
            }
            if (data.hasOwnProperty('segment_id')) {
                obj['segment_id'] = ApiClient.convertToType(data['segment_id'], 'String');
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Metadata1</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Metadata1</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Metadata1.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['bearing'] && !(typeof data['bearing'] === 'string' || data['bearing'] instanceof String)) {
            throw new Error("Expected the field `bearing` to be a primitive type in the JSON string but got " + data['bearing']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['columns'])) {
            throw new Error("Expected the field `columns` to be an array in the JSON data but got " + data['columns']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['rows'])) {
            throw new Error("Expected the field `rows` to be an array in the JSON data but got " + data['rows']);
        }
        // ensure the json data is a string
        if (data['segment_id'] && !(typeof data['segment_id'] === 'string' || data['segment_id'] instanceof String)) {
            throw new Error("Expected the field `segment_id` to be a primitive type in the JSON string but got " + data['segment_id']);
        }
        // ensure the json data is a string
        if (data['state'] && !(typeof data['state'] === 'string' || data['state'] instanceof String)) {
            throw new Error("Expected the field `state` to be a primitive type in the JSON string but got " + data['state']);
        }

        return true;
    }


}

Metadata1.RequiredProperties = ["bearing", "columns", "name", "rows", "segment_id", "state"];

/**
 * @member {String} bearing
 */
Metadata1.prototype['bearing'] = undefined;

/**
 * @member {Array.<String>} columns
 */
Metadata1.prototype['columns'] = undefined;

/**
 * @member {String} name
 */
Metadata1.prototype['name'] = undefined;

/**
 * @member {Array.<String>} rows
 */
Metadata1.prototype['rows'] = undefined;

/**
 * @member {String} segment_id
 */
Metadata1.prototype['segment_id'] = undefined;

/**
 * @member {String} state
 */
Metadata1.prototype['state'] = undefined;






export default Metadata1;

