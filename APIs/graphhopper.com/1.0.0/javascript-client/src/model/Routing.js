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

/**
 * The Routing model module.
 * @module model/Routing
 * @version 1.0.0
 */
class Routing {
    /**
     * Constructs a new <code>Routing</code>.
     * This contains all routing specific configurations.
     * @alias module:model/Routing
     */
    constructor() { 
        
        Routing.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['calc_points'] = false;
        obj['consider_traffic'] = false;
        obj['curbside_strictness'] = 'soft';
        obj['fail_fast'] = true;
        obj['network_data_provider'] = 'openstreetmap';
        obj['return_snapped_waypoints'] = false;
    }

    /**
     * Constructs a <code>Routing</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Routing} obj Optional instance to populate.
     * @return {module:model/Routing} The populated <code>Routing</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Routing();

            if (data.hasOwnProperty('calc_points')) {
                obj['calc_points'] = ApiClient.convertToType(data['calc_points'], 'Boolean');
            }
            if (data.hasOwnProperty('consider_traffic')) {
                obj['consider_traffic'] = ApiClient.convertToType(data['consider_traffic'], 'Boolean');
            }
            if (data.hasOwnProperty('curbside_strictness')) {
                obj['curbside_strictness'] = ApiClient.convertToType(data['curbside_strictness'], 'String');
            }
            if (data.hasOwnProperty('fail_fast')) {
                obj['fail_fast'] = ApiClient.convertToType(data['fail_fast'], 'Boolean');
            }
            if (data.hasOwnProperty('network_data_provider')) {
                obj['network_data_provider'] = ApiClient.convertToType(data['network_data_provider'], 'String');
            }
            if (data.hasOwnProperty('return_snapped_waypoints')) {
                obj['return_snapped_waypoints'] = ApiClient.convertToType(data['return_snapped_waypoints'], 'Boolean');
            }
            if (data.hasOwnProperty('snap_preventions')) {
                obj['snap_preventions'] = ApiClient.convertToType(data['snap_preventions'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Routing</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Routing</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['curbside_strictness'] && !(typeof data['curbside_strictness'] === 'string' || data['curbside_strictness'] instanceof String)) {
            throw new Error("Expected the field `curbside_strictness` to be a primitive type in the JSON string but got " + data['curbside_strictness']);
        }
        // ensure the json data is a string
        if (data['network_data_provider'] && !(typeof data['network_data_provider'] === 'string' || data['network_data_provider'] instanceof String)) {
            throw new Error("Expected the field `network_data_provider` to be a primitive type in the JSON string but got " + data['network_data_provider']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['snap_preventions'])) {
            throw new Error("Expected the field `snap_preventions` to be an array in the JSON data but got " + data['snap_preventions']);
        }

        return true;
    }


}



/**
 * It lets you specify whether the API should provide you with route geometries for vehicle routes or not. Thus, you do not need to do extra routing to get the polyline for each route.
 * @member {Boolean} calc_points
 * @default false
 */
Routing.prototype['calc_points'] = false;

/**
 * indicates whether historical traffic information should be considered
 * @member {Boolean} consider_traffic
 * @default false
 */
Routing.prototype['consider_traffic'] = false;

/**
 * In some cases curbside constraints cannot be fulfilled. For example in one-way streets you cannot arrive at a building that is on the left side of the street such that the building is to the right of you (unless you drove the one-way street the wrong/illegal way). You can set the `curbside_strictness` to `soft` to ignore the curbside constraint in such cases or set it to `strict` to get an error response instead. You can also set it to `ignore` to ignore all curbside constraints (this is useful to compare the results with and without constraints without modifying every single address).
 * @member {module:model/Routing.CurbsideStrictnessEnum} curbside_strictness
 * @default 'soft'
 */
Routing.prototype['curbside_strictness'] = 'soft';

/**
 * indicates whether matrix calculation should fail fast when points cannot be connected
 * @member {Boolean} fail_fast
 * @default true
 */
Routing.prototype['fail_fast'] = true;

/**
 * specifies the data provider, read more about it [here](#section/Map-Data-and-Routing-Profiles).
 * @member {module:model/Routing.NetworkDataProviderEnum} network_data_provider
 * @default 'openstreetmap'
 */
Routing.prototype['network_data_provider'] = 'openstreetmap';

/**
 * Indicates whether a solution includes snapped waypoints. In contrary to the address coordinate a snapped waypoint is the access point to the (road) network.
 * @member {Boolean} return_snapped_waypoints
 * @default false
 */
Routing.prototype['return_snapped_waypoints'] = false;

/**
 * Prevents snapping locations to road links of specified road types, e.g. to motorway.
 * @member {Array.<module:model/Routing.SnapPreventionsEnum>} snap_preventions
 */
Routing.prototype['snap_preventions'] = undefined;





/**
 * Allowed values for the <code>curbside_strictness</code> property.
 * @enum {String}
 * @readonly
 */
Routing['CurbsideStrictnessEnum'] = {

    /**
     * value: "ignore"
     * @const
     */
    "ignore": "ignore",

    /**
     * value: "soft"
     * @const
     */
    "soft": "soft",

    /**
     * value: "strict"
     * @const
     */
    "strict": "strict"
};


/**
 * Allowed values for the <code>network_data_provider</code> property.
 * @enum {String}
 * @readonly
 */
Routing['NetworkDataProviderEnum'] = {

    /**
     * value: "openstreetmap"
     * @const
     */
    "openstreetmap": "openstreetmap",

    /**
     * value: "tomtom"
     * @const
     */
    "tomtom": "tomtom"
};


/**
 * Allowed values for the <code>snapPreventions</code> property.
 * @enum {String}
 * @readonly
 */
Routing['SnapPreventionsEnum'] = {

    /**
     * value: "motorway"
     * @const
     */
    "motorway": "motorway",

    /**
     * value: "trunk"
     * @const
     */
    "trunk": "trunk",

    /**
     * value: "bridge"
     * @const
     */
    "bridge": "bridge",

    /**
     * value: "ford"
     * @const
     */
    "ford": "ford",

    /**
     * value: "tunnel"
     * @const
     */
    "tunnel": "tunnel",

    /**
     * value: "ferry"
     * @const
     */
    "ferry": "ferry"
};



export default Routing;

