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
import VehicleProfileId from './VehicleProfileId';

/**
 * The RouteRequest model module.
 * @module model/RouteRequest
 * @version 1.0.0
 */
class RouteRequest {
    /**
     * Constructs a new <code>RouteRequest</code>.
     * @alias module:model/RouteRequest
     */
    constructor() { 
        
        RouteRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['alternative_route.max_paths'] = 2;
        obj['alternative_route.max_share_factor'] = 0.6;
        obj['alternative_route.max_weight_factor'] = 1.4;
        obj['calc_points'] = true;
        obj['ch.disable'] = false;
        obj['debug'] = false;
        obj['elevation'] = false;
        obj['heading_penalty'] = 120;
        obj['instructions'] = true;
        obj['locale'] = 'en';
        obj['optimize'] = 'false';
        obj['pass_through'] = false;
        obj['points_encoded'] = true;
        obj['round_trip.distance'] = 10000;
        obj['weighting'] = 'fastest';
    }

    /**
     * Constructs a <code>RouteRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RouteRequest} obj Optional instance to populate.
     * @return {module:model/RouteRequest} The populated <code>RouteRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RouteRequest();

            if (data.hasOwnProperty('algorithm')) {
                obj['algorithm'] = ApiClient.convertToType(data['algorithm'], 'String');
            }
            if (data.hasOwnProperty('alternative_route.max_paths')) {
                obj['alternative_route.max_paths'] = ApiClient.convertToType(data['alternative_route.max_paths'], 'Number');
            }
            if (data.hasOwnProperty('alternative_route.max_share_factor')) {
                obj['alternative_route.max_share_factor'] = ApiClient.convertToType(data['alternative_route.max_share_factor'], 'Number');
            }
            if (data.hasOwnProperty('alternative_route.max_weight_factor')) {
                obj['alternative_route.max_weight_factor'] = ApiClient.convertToType(data['alternative_route.max_weight_factor'], 'Number');
            }
            if (data.hasOwnProperty('avoid')) {
                obj['avoid'] = ApiClient.convertToType(data['avoid'], 'String');
            }
            if (data.hasOwnProperty('block_area')) {
                obj['block_area'] = ApiClient.convertToType(data['block_area'], 'String');
            }
            if (data.hasOwnProperty('calc_points')) {
                obj['calc_points'] = ApiClient.convertToType(data['calc_points'], 'Boolean');
            }
            if (data.hasOwnProperty('ch.disable')) {
                obj['ch.disable'] = ApiClient.convertToType(data['ch.disable'], 'Boolean');
            }
            if (data.hasOwnProperty('curbsides')) {
                obj['curbsides'] = ApiClient.convertToType(data['curbsides'], ['String']);
            }
            if (data.hasOwnProperty('debug')) {
                obj['debug'] = ApiClient.convertToType(data['debug'], 'Boolean');
            }
            if (data.hasOwnProperty('details')) {
                obj['details'] = ApiClient.convertToType(data['details'], ['String']);
            }
            if (data.hasOwnProperty('elevation')) {
                obj['elevation'] = ApiClient.convertToType(data['elevation'], 'Boolean');
            }
            if (data.hasOwnProperty('heading_penalty')) {
                obj['heading_penalty'] = ApiClient.convertToType(data['heading_penalty'], 'Number');
            }
            if (data.hasOwnProperty('headings')) {
                obj['headings'] = ApiClient.convertToType(data['headings'], ['Number']);
            }
            if (data.hasOwnProperty('instructions')) {
                obj['instructions'] = ApiClient.convertToType(data['instructions'], 'Boolean');
            }
            if (data.hasOwnProperty('locale')) {
                obj['locale'] = ApiClient.convertToType(data['locale'], 'String');
            }
            if (data.hasOwnProperty('optimize')) {
                obj['optimize'] = ApiClient.convertToType(data['optimize'], 'String');
            }
            if (data.hasOwnProperty('pass_through')) {
                obj['pass_through'] = ApiClient.convertToType(data['pass_through'], 'Boolean');
            }
            if (data.hasOwnProperty('point_hints')) {
                obj['point_hints'] = ApiClient.convertToType(data['point_hints'], ['String']);
            }
            if (data.hasOwnProperty('points')) {
                obj['points'] = ApiClient.convertToType(data['points'], [['Number']]);
            }
            if (data.hasOwnProperty('points_encoded')) {
                obj['points_encoded'] = ApiClient.convertToType(data['points_encoded'], 'Boolean');
            }
            if (data.hasOwnProperty('round_trip.distance')) {
                obj['round_trip.distance'] = ApiClient.convertToType(data['round_trip.distance'], 'Number');
            }
            if (data.hasOwnProperty('round_trip.seed')) {
                obj['round_trip.seed'] = ApiClient.convertToType(data['round_trip.seed'], 'Number');
            }
            if (data.hasOwnProperty('snap_preventions')) {
                obj['snap_preventions'] = ApiClient.convertToType(data['snap_preventions'], ['String']);
            }
            if (data.hasOwnProperty('vehicle')) {
                obj['vehicle'] = ApiClient.convertToType(data['vehicle'], VehicleProfileId);
            }
            if (data.hasOwnProperty('weighting')) {
                obj['weighting'] = ApiClient.convertToType(data['weighting'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RouteRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RouteRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['algorithm'] && !(typeof data['algorithm'] === 'string' || data['algorithm'] instanceof String)) {
            throw new Error("Expected the field `algorithm` to be a primitive type in the JSON string but got " + data['algorithm']);
        }
        // ensure the json data is a string
        if (data['avoid'] && !(typeof data['avoid'] === 'string' || data['avoid'] instanceof String)) {
            throw new Error("Expected the field `avoid` to be a primitive type in the JSON string but got " + data['avoid']);
        }
        // ensure the json data is a string
        if (data['block_area'] && !(typeof data['block_area'] === 'string' || data['block_area'] instanceof String)) {
            throw new Error("Expected the field `block_area` to be a primitive type in the JSON string but got " + data['block_area']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['curbsides'])) {
            throw new Error("Expected the field `curbsides` to be an array in the JSON data but got " + data['curbsides']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['details'])) {
            throw new Error("Expected the field `details` to be an array in the JSON data but got " + data['details']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['headings'])) {
            throw new Error("Expected the field `headings` to be an array in the JSON data but got " + data['headings']);
        }
        // ensure the json data is a string
        if (data['locale'] && !(typeof data['locale'] === 'string' || data['locale'] instanceof String)) {
            throw new Error("Expected the field `locale` to be a primitive type in the JSON string but got " + data['locale']);
        }
        // ensure the json data is a string
        if (data['optimize'] && !(typeof data['optimize'] === 'string' || data['optimize'] instanceof String)) {
            throw new Error("Expected the field `optimize` to be a primitive type in the JSON string but got " + data['optimize']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['point_hints'])) {
            throw new Error("Expected the field `point_hints` to be an array in the JSON data but got " + data['point_hints']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['points'])) {
            throw new Error("Expected the field `points` to be an array in the JSON data but got " + data['points']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['snap_preventions'])) {
            throw new Error("Expected the field `snap_preventions` to be an array in the JSON data but got " + data['snap_preventions']);
        }
        // validate the optional field `vehicle`
        if (data['vehicle']) { // data not null
          VehicleProfileId.validateJSON(data['vehicle']);
        }
        // ensure the json data is a string
        if (data['weighting'] && !(typeof data['weighting'] === 'string' || data['weighting'] instanceof String)) {
            throw new Error("Expected the field `weighting` to be a primitive type in the JSON string but got " + data['weighting']);
        }

        return true;
    }


}



/**
 * Rather than looking for the shortest or fastest path, this lets you solve two different problems related to routing: With `round_trip`, the route will get you back to where you started. This is meant for fun (think of a bike trip), so we will add some randomness. This requires `ch.disable=true`. With `alternative_route`, we give you not one but several routes that are close to optimal, but not too similar to each other. You can control both of these features with additional parameters, see below. 
 * @member {module:model/RouteRequest.AlgorithmEnum} algorithm
 */
RouteRequest.prototype['algorithm'] = undefined;

/**
 * If `algorithm=alternative_route`, this parameter sets the number of maximum paths which should be calculated. Increasing can lead to worse alternatives. 
 * @member {Number} alternative_route.max_paths
 * @default 2
 */
RouteRequest.prototype['alternative_route.max_paths'] = 2;

/**
 * If `algorithm=alternative_route`, this parameter specifies how similar an alternative route can be to the optimal route. Increasing can lead to worse alternatives. 
 * @member {Number} alternative_route.max_share_factor
 * @default 0.6
 */
RouteRequest.prototype['alternative_route.max_share_factor'] = 0.6;

/**
 * If `algorithm=alternative_route`, this parameter sets the factor by which the alternatives routes can be longer than the optimal route. Increasing can lead to worse alternatives. 
 * @member {Number} alternative_route.max_weight_factor
 * @default 1.4
 */
RouteRequest.prototype['alternative_route.max_weight_factor'] = 1.4;

/**
 * Specify which road classes and environments you would like to avoid. Possible values are `motorway`, `steps`, `track`, `toll`, `ferry`, `tunnel` and `bridge`. Separate several values with `;`. Obviously not all the values make sense for all vehicle profiles e.g. `bike` is already forbidden on a `motorway`. Requires `ch.disable=true`. 
 * @member {String} avoid
 */
RouteRequest.prototype['avoid'] = undefined;

/**
 * Block road access via a point with the format `latitude,longitude` or an area defined by a circle `lat,lon,radius` or a rectangle `lat1,lon1,lat2,lon2`. Separate several values with `;`. Requires `ch.disable=true`. 
 * @member {String} block_area
 */
RouteRequest.prototype['block_area'] = undefined;

/**
 * If the points for the route should be calculated at all. 
 * @member {Boolean} calc_points
 * @default true
 */
RouteRequest.prototype['calc_points'] = true;

/**
 * Use this parameter in combination with one or more parameters from below. 
 * @member {Boolean} ch.disable
 * @default false
 */
RouteRequest.prototype['ch.disable'] = false;

/**
 * Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap.
 * @member {Array.<module:model/RouteRequest.CurbsidesEnum>} curbsides
 */
RouteRequest.prototype['curbsides'] = undefined;

/**
 * If `true`, the output will be formatted. 
 * @member {Boolean} debug
 * @default false
 */
RouteRequest.prototype['debug'] = false;

/**
 * Optional parameter to retrieve path details. You can request additional details for the route: `street_name`, `time`, `distance`, `max_speed`, `toll`, `road_class`, `road_class_link`, `road_access`, `road_environment`, `lanes`, and `surface`. Read more about the usage of path details [here](https://discuss.graphhopper.com/t/2539). 
 * @member {Array.<String>} details
 */
RouteRequest.prototype['details'] = undefined;

/**
 * If `true`, a third coordinate, the altitude, is included with all positions in the response. This changes the format of the `points` and `snapped_waypoints` fields of the response, in both their encodings. Unless you switch off the `points_encoded` parameter, you need special code on the client side that can handle three-dimensional coordinates. A request can fail if the vehicle profile does not support elevation. See the features object for every vehicle profile. 
 * @member {Boolean} elevation
 * @default false
 */
RouteRequest.prototype['elevation'] = false;

/**
 * Time penalty in seconds for not obeying a specified heading. Requires `ch.disable=true`. 
 * @member {Number} heading_penalty
 * @default 120
 */
RouteRequest.prototype['heading_penalty'] = 120;

/**
 * Favour a heading direction for a certain point. Specify either one heading for the start point or as many as there are points. In this case headings are associated by their order to the specific points. Headings are given as north based clockwise angle between 0 and 360 degree. This parameter also influences the tour generated with `algorithm=round_trip` and forces the initial direction.  Requires `ch.disable=true`. 
 * @member {Array.<Number>} headings
 */
RouteRequest.prototype['headings'] = undefined;

/**
 * If instructions should be calculated and returned 
 * @member {Boolean} instructions
 * @default true
 */
RouteRequest.prototype['instructions'] = true;

/**
 * The locale of the resulting turn instructions. E.g. `pt_PT` for Portuguese or `de` for German. 
 * @member {String} locale
 * @default 'en'
 */
RouteRequest.prototype['locale'] = 'en';

/**
 * Normally, the calculated route will visit the points in the order you specified them. If you have more than two points, you can set this parameter to `\"true\"` and the points may be re-ordered to minimize the total travel time. Keep in mind that the limits on the number of locations of the Route Optimization API applies, and the request costs more credits. 
 * @member {String} optimize
 * @default 'false'
 */
RouteRequest.prototype['optimize'] = 'false';

/**
 * If `true`, u-turns are avoided at via-points with regard to the `heading_penalty`. Requires `ch.disable=true`. 
 * @member {Boolean} pass_through
 * @default false
 */
RouteRequest.prototype['pass_through'] = false;

/**
 * Optional parameter. Specifies a hint for each point in the `points` array to prefer a certain street for the closest location lookup. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up.
 * @member {Array.<String>} point_hints
 */
RouteRequest.prototype['point_hints'] = undefined;

/**
 * The points for the route in an array of `[longitude,latitude]`. For instance, if you want to calculate a route from point A to B to C then you specify `points: [ [A_longitude, A_latitude], [B_longitude, B_latitude], [C_longitude, C_latitude]] 
 * @member {Array.<Array.<Number>>} points
 */
RouteRequest.prototype['points'] = undefined;

/**
 * Allows changing the encoding of location data in the response. The default is polyline encoding, which is compact but requires special client code to unpack. (We provide it in our JavaScript client library!) Set this parameter to `false` to switch the encoding to simple coordinate pairs like `[lon,lat]`, or `[lon,lat,elevation]`. See the description of the response format for more information. 
 * @member {Boolean} points_encoded
 * @default true
 */
RouteRequest.prototype['points_encoded'] = true;

/**
 * If `algorithm=round_trip`, this parameter configures approximative length of the resulting round trip. Requires `ch.disable=true`. 
 * @member {Number} round_trip.distance
 * @default 10000
 */
RouteRequest.prototype['round_trip.distance'] = 10000;

/**
 * If `algorithm=round_trip`, this sets the random seed. Change this to get a different tour for each value. 
 * @member {Number} round_trip.seed
 */
RouteRequest.prototype['round_trip.seed'] = undefined;

/**
 * Optional parameter to avoid snapping to a certain road class or road environment. Current supported values `motorway`, `trunk`, `ferry`, `tunnel`, `bridge` and `ford`
 * @member {Array.<String>} snap_preventions
 */
RouteRequest.prototype['snap_preventions'] = undefined;

/**
 * @member {module:model/VehicleProfileId} vehicle
 */
RouteRequest.prototype['vehicle'] = undefined;

/**
 * Determines the way the ''best'' route is calculated. Default is `fastest`. Other options are `shortest` (e.g. for `vehicle=foot` or `bike`) and `short_fastest` which finds a reasonable balance between `shortest` and `fastest`. Requires `ch.disable=true`. 
 * @member {String} weighting
 * @default 'fastest'
 */
RouteRequest.prototype['weighting'] = 'fastest';





/**
 * Allowed values for the <code>algorithm</code> property.
 * @enum {String}
 * @readonly
 */
RouteRequest['AlgorithmEnum'] = {

    /**
     * value: "round_trip"
     * @const
     */
    "round_trip": "round_trip",

    /**
     * value: "alternative_route"
     * @const
     */
    "alternative_route": "alternative_route"
};


/**
 * Allowed values for the <code>curbsides</code> property.
 * @enum {String}
 * @readonly
 */
RouteRequest['CurbsidesEnum'] = {

    /**
     * value: "any"
     * @const
     */
    "any": "any",

    /**
     * value: "right"
     * @const
     */
    "right": "right",

    /**
     * value: "left"
     * @const
     */
    "left": "left"
};



export default RouteRequest;

