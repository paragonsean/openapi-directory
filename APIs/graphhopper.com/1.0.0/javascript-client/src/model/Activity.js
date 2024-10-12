/**
 * GraphHopper Directions API
 *  With the [GraphHopper Directions API](https://www.graphhopper.com/products/) you can integrate A-to-B route planning, turn-by-turn navigation, route optimization, isochrone calculations and other tools in your application.  The GraphHopper Directions API consists of the following RESTful web services:   * [Routing API](#tag/Routing-API),  * [Route Optimization API](#tag/Route-Optimization-API),  * [Isochrone API](#tag/Isochrone-API),  * [Map Matching API](#tag/Map-Matching-API),  * [Matrix API](#tag/Matrix-API),  * [Geocoding API](#tag/Geocoding-API) and  * [Cluster API](#tag/Cluster-API).  # Explore our APIs  ## Get started  1. [Sign up for GraphHopper](https://support.graphhopper.com/a/solutions/articles/44001976025) 2. [Create an API key](https://support.graphhopper.com/a/solutions/articles/44001976027)  Each API part has its own documentation. Jump to the desired API part and learn about the API through the given examples and tutorials.  In addition, for each API there are specific sample requests that you can send via Insomnia or Postman to see what the requests and responses look like.  ## Insomnia  To explore our APIs with [Insomnia](https://insomnia.rest/), follow these steps:  1. Open Insomnia and Import [our workspace](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/GraphHopper-Direction-API-Insomnia.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your workspace: Manage Environments -> Base Environment -> `\"api_key\": your API key` 3. Start exploring  ![Insomnia](./img/insomnia.png)  ## Postman  To explore our APIs with [Postman](https://www.getpostman.com/), follow these steps:  1. Import our [request collections](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_collection.json) as well as our [environment file](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_environment.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your environment: `\"api_key\": your API key` 3. Start exploring  ![Postman](./img/postman.png)  ## API Client Libraries  To speed up development and make coding easier, we offer the following client libraries:   * [JavaScript client](https://github.com/graphhopper/directions-api-js-client) - try the [live examples](https://graphhopper.com/api/1/examples/)  * [Others](https://github.com/graphhopper/directions-api-clients) like C#, Ruby, PHP, Python, ... automatically created for the Route Optimization API  ### Bandwidth reduction  If you create your own client, make sure it supports http/2 and gzipped responses for best speed.  If you use the Matrix, the Route Optimization API or the Cluster API and want to solve large problems, we recommend you to reduce bandwidth by [compressing your POST request](https://gist.github.com/karussell/82851e303ea7b3459b2dea01f18949f4) and specifying the header as follows: `Content-Encoding: gzip`. This will also avoid the HTTP 413 error \"Request Entity Too Large\".  ## Contact Us  If you have problems or questions, please read the following information:  - [FAQ](https://graphhopper.com/api/1/docs/FAQ/) - [Public forum](https://discuss.graphhopper.com/c/directions-api) - [Contact us](https://www.graphhopper.com/contact-form/) - [GraphHopper Status Page](https://status.graphhopper.com/)  To stay informed about the latest developments, you can  - follow us on [twitter](https://twitter.com/graphhopper/), - read [our blog](https://graphhopper.com/blog/), - watch [our documentation repository](https://github.com/graphhopper/directions-api-doc), - sign up for our newsletter or - [our forum](https://discuss.graphhopper.com/c/directions-api).  Select the channel you like the most.   # Map Data and Routing Profiles  Currently, our main data source is [OpenStreetMap](https://www.openstreetmap.org). We also integrated other network data providers. This chapter gives an overview about the options you have.  ## OpenStreetMap  #### Geographical Coverage  [OpenStreetMap](https://www.openstreetmap.org) covers the whole world. If you want to see for yourself if we can provide data suitable for your region, please visit [GraphHopper Maps](https://graphhopper.com/maps/). You can edit and modify OpenStreetMap data if you find that important information is missing, e.g. a weight limit for a bridge. [Here](https://wiki.openstreetmap.org/wiki/Beginners%27_guide) is a beginner's guide that shows how to add data. If you have edited data, we usually consider your data after 1 week at the latest.  #### Supported Vehicle Profiles  The Routing, Matrix and Route Optimization APIs support the following vehicle profiles:  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) truck      | Truck like a MAN or Mercedes-Benz Actros | height=3.7m, width=2.6+0.5m, length=12m, weight=13000 + 13000 kg, hgv=yes, 3 Axes | ![truck image](https://graphhopper.com/maps/img/truck.png) scooter    | Moped mode | Fast inner city, often used for food delivery, is able to ignore certain bollards, maximum speed of roughly 50km/h | ![scooter image](https://graphhopper.com/maps/img/scooter.png) foot       | Pedestrian or walking without dangerous [SAC-scales](https://wiki.openstreetmap.org/wiki/Key:sac_scale) | foot access         | ![foot image](https://graphhopper.com/maps/img/foot.png) hike       | Pedestrian or walking with priority for more beautiful hiking tours and potentially a bit longer than `foot`. Walking duration is influenced by elevation differences.  | foot access         | ![hike image](https://graphhopper.com/maps/img/hike.png) bike       | Trekking bike avoiding hills | bike access  | ![bike image](https://graphhopper.com/maps/img/bike.png) mtb        | Mountainbike          | bike access         | ![Mountainbike image](https://graphhopper.com/maps/img/mtb.png) racingbike| Bike preferring roads | bike access         | ![racingbike image](https://graphhopper.com/maps/img/racingbike.png)  Please note:   * all motor vehicles (`car`, `small_truck`, `truck` and `scooter`) support turn restrictions via `turn_costs=true`  * the free package supports only the vehicle profiles `car`, `bike` or `foot`  * up to 2 different vehicle profiles can be used in a single optimization request. The number of vehicles is unaffected and depends on your subscription.  * we offer custom vehicle profiles with different properties, different speed profiles or different access options. To find out more about custom profiles, please [contact us](https://www.graphhopper.com/contact-form/).  * a sophisticated `motorcycle` profile is available up on request. It is powered by the [Kurviger](https://kurviger.de/en) Routing API and favors curves and slopes while avoiding cities and highways.   ## TomTom  If you want to include traffic, you can purchase the TomTom Add-on. This Add-on only uses TomTom's road network and historical traffic information. Live traffic is not yet considered. If you are interested to learn how we consider traffic information, we recommend that you read [this article](https://www.graphhopper.com/blog/2017/11/06/time-dependent-optimization/).  Please note the following:   * Currently we only offer this for our [Route Optimization API](#tag/Route-Optimization-API).  * In addition to our terms, you need to accept TomTom's [End User License Aggreement](https://www.graphhopper.com/tomtom-end-user-license-agreement/).  * We do *not* use TomTom's web services. We only use their data with our software.   [Contact us](https://www.graphhopper.com/contact-form/) for more details.  #### Geographical Coverage  We offer  - Europe including Russia - North, Central and South America - Saudi Arabia - United Arab Emirates - South Africa - Australia  #### Supported Vehicle Profiles  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@graphhopper.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ResponseAddress from './ResponseAddress';

/**
 * The Activity model module.
 * @module model/Activity
 * @version 1.0.0
 */
class Activity {
    /**
     * Constructs a new <code>Activity</code>.
     * @alias module:model/Activity
     */
    constructor() { 
        
        Activity.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Activity</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Activity} obj Optional instance to populate.
     * @return {module:model/Activity} The populated <code>Activity</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Activity();

            if (data.hasOwnProperty('address')) {
                obj['address'] = ResponseAddress.constructFromObject(data['address']);
            }
            if (data.hasOwnProperty('arr_date_time')) {
                obj['arr_date_time'] = ApiClient.convertToType(data['arr_date_time'], 'Date');
            }
            if (data.hasOwnProperty('arr_time')) {
                obj['arr_time'] = ApiClient.convertToType(data['arr_time'], 'Number');
            }
            if (data.hasOwnProperty('distance')) {
                obj['distance'] = ApiClient.convertToType(data['distance'], 'Number');
            }
            if (data.hasOwnProperty('driving_time')) {
                obj['driving_time'] = ApiClient.convertToType(data['driving_time'], 'Number');
            }
            if (data.hasOwnProperty('end_date_time')) {
                obj['end_date_time'] = ApiClient.convertToType(data['end_date_time'], 'Date');
            }
            if (data.hasOwnProperty('end_time')) {
                obj['end_time'] = ApiClient.convertToType(data['end_time'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('load_after')) {
                obj['load_after'] = ApiClient.convertToType(data['load_after'], ['Number']);
            }
            if (data.hasOwnProperty('load_before')) {
                obj['load_before'] = ApiClient.convertToType(data['load_before'], ['Number']);
            }
            if (data.hasOwnProperty('location_id')) {
                obj['location_id'] = ApiClient.convertToType(data['location_id'], 'String');
            }
            if (data.hasOwnProperty('preparation_time')) {
                obj['preparation_time'] = ApiClient.convertToType(data['preparation_time'], 'Number');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('waiting_time')) {
                obj['waiting_time'] = ApiClient.convertToType(data['waiting_time'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Activity</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Activity</code>.
     */
    static validateJSON(data) {
        // validate the optional field `address`
        if (data['address']) { // data not null
          ResponseAddress.validateJSON(data['address']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['load_after'])) {
            throw new Error("Expected the field `load_after` to be an array in the JSON data but got " + data['load_after']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['load_before'])) {
            throw new Error("Expected the field `load_before` to be an array in the JSON data but got " + data['load_before']);
        }
        // ensure the json data is a string
        if (data['location_id'] && !(typeof data['location_id'] === 'string' || data['location_id'] instanceof String)) {
            throw new Error("Expected the field `location_id` to be a primitive type in the JSON string but got " + data['location_id']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {module:model/ResponseAddress} address
 */
Activity.prototype['address'] = undefined;

/**
 * Arrival date time with offset like this 1970-01-01T01:00+01:00. If you do not use time-dependent optimization, this is `null`.
 * @member {Date} arr_date_time
 */
Activity.prototype['arr_date_time'] = undefined;

/**
 * Arrival time at this activity in seconds. If type is `start`, this is not available (since it makes no sense to have `arr_time` at start). However, `end_time` is available and actually means \\\"departure time\\\" at start location. It is important to note that `arr_time` does not necessarily mean \\\"start of underlying activity\\\", it solely means arrival time at activity location. If this activity has no time windows and if there are no further preparation times, `arr_time` is equal to activity start time.
 * @member {Number} arr_time
 */
Activity.prototype['arr_time'] = undefined;

/**
 * cumulated distance from start to this activity in m
 * @member {Number} distance
 */
Activity.prototype['distance'] = undefined;

/**
 * cumulated driving time from start to this driver activity in seconds
 * @member {Number} driving_time
 */
Activity.prototype['driving_time'] = undefined;

/**
 * End date time with offset like this 1970-01-01T01:00+01:00. If you do not use time-dependent optimization, this is `null`.
 * @member {Date} end_date_time
 */
Activity.prototype['end_date_time'] = undefined;

/**
 * End time of and thus departure time at this activity. If type is `end`, this is not available (since it makes no sense to have an `end_time` at end) `end_time` at each activity is equal to the departure time at the activity location.
 * @member {Number} end_time
 */
Activity.prototype['end_time'] = undefined;

/**
 * Id referring to the underlying service or shipment, i.e. the shipment or service this activity belongs to
 * @member {String} id
 */
Activity.prototype['id'] = undefined;

/**
 * Array with size/capacity dimensions after this activity
 * @member {Array.<Number>} load_after
 */
Activity.prototype['load_after'] = undefined;

/**
 * Array with size/capacity dimensions before this activity
 * @member {Array.<Number>} load_before
 */
Activity.prototype['load_before'] = undefined;

/**
 * Id that refers to address
 * @member {String} location_id
 */
Activity.prototype['location_id'] = undefined;

/**
 * preparation time at this activity in seconds
 * @member {Number} preparation_time
 */
Activity.prototype['preparation_time'] = undefined;

/**
 * type of activity
 * @member {module:model/Activity.TypeEnum} type
 */
Activity.prototype['type'] = undefined;

/**
 * Waiting time at this activity in seconds. A waiting time can occur if the activity has at least one time window. If `arr_time` < `time_window.earliest` a waiting time of `time_window_earliest` - `arr_time` occurs.
 * @member {Number} waiting_time
 */
Activity.prototype['waiting_time'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
Activity['TypeEnum'] = {

    /**
     * value: "start"
     * @const
     */
    "start": "start",

    /**
     * value: "end"
     * @const
     */
    "end": "end",

    /**
     * value: "service"
     * @const
     */
    "service": "service",

    /**
     * value: "pickupShipment"
     * @const
     */
    "pickupShipment": "pickupShipment",

    /**
     * value: "deliverShipment"
     * @const
     */
    "deliverShipment": "deliverShipment",

    /**
     * value: "pickup"
     * @const
     */
    "pickup": "pickup",

    /**
     * value: "delivery"
     * @const
     */
    "delivery": "delivery",

    /**
     * value: "break"
     * @const
     */
    "break": "break"
};



export default Activity;

