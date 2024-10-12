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
 * The Objective model module.
 * @module model/Objective
 * @version 1.0.0
 */
class Objective {
    /**
     * Constructs a new <code>Objective</code>.
     * @alias module:model/Objective
     * @param type {module:model/Objective.TypeEnum} Type of objective function, i.e. `min` or `min-max`.   * `min`: Minimizes the objective value.  * `min-max`: Minimizes the maximum objective value.  For instance, `min` -> `vehicles` minimizes the number of employed vehicles. `min` -> `completion_time` minimizes the sum of your vehicle routes' completion time.  If you use, for example, `min-max` -> `completion_time`, it minimizes the maximum of your vehicle routes' completion time, i.e. it minimizes the overall makespan. This only makes sense if you have more than one vehicle. In case of one vehicle, switching from `min` to `min-max` should not have any impact. If you have more than one vehicle, then the algorithm tries to constantly move stops from one vehicle to another such that the completion time of longest vehicle route can be further reduced. For example, if you have one vehicle that takes 8 hours to serve all customers, adding another vehicle (and using `min-max`) might halve the time to serve all customers to 4 hours. However, this usually comes with higher transport costs.  If you want to minimize `vehicles` first and, second, `completion_time`, you can also combine different objectives like this:  ```json \"objectives\" : [    {       \"type\": \"min\",       \"value\": \"vehicles\"    },    {       \"type\": \"min\",       \"value\": \"completion_time\"    } ] ```  If you want to balance activities or the number of stops among all employed drivers, you need to specify it as follows:  ```json \"objectives\" : [    {       \"type\": \"min-max\",       \"value\": \"completion_time\"    },    {       \"type\": \"min-max\",       \"value\": \"activities\"    } ] ``` 
     * @param value {module:model/Objective.ValueEnum} The value of the objective function. The objective value `transport_time` solely considers the time your drivers spend on the road, i.e. transport time. In contrary to `transport_time`, `completion_time` also takes waiting times at customer sites into account. The `completion_time` of a route is defined as the time from starting to ending the route, i.e. the route's transport time, the sum of waiting times plus the sum of activity durations. Note that choosing `transport_time` or `completion_time` only makes a difference if you specified time windows for your services/shipments since only in scenarios with time windows waiting times can occur. The objective value `vehicles` can only be used along with `min` and minimizes vehicles. 
     */
    constructor(type, value) { 
        
        Objective.initialize(this, type, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, type, value) { 
        obj['type'] = type || 'min';
        obj['value'] = value || 'transport_time';
    }

    /**
     * Constructs a <code>Objective</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Objective} obj Optional instance to populate.
     * @return {module:model/Objective} The populated <code>Objective</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Objective();

            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Objective</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Objective</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Objective.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}

Objective.RequiredProperties = ["type", "value"];

/**
 * Type of objective function, i.e. `min` or `min-max`.   * `min`: Minimizes the objective value.  * `min-max`: Minimizes the maximum objective value.  For instance, `min` -> `vehicles` minimizes the number of employed vehicles. `min` -> `completion_time` minimizes the sum of your vehicle routes' completion time.  If you use, for example, `min-max` -> `completion_time`, it minimizes the maximum of your vehicle routes' completion time, i.e. it minimizes the overall makespan. This only makes sense if you have more than one vehicle. In case of one vehicle, switching from `min` to `min-max` should not have any impact. If you have more than one vehicle, then the algorithm tries to constantly move stops from one vehicle to another such that the completion time of longest vehicle route can be further reduced. For example, if you have one vehicle that takes 8 hours to serve all customers, adding another vehicle (and using `min-max`) might halve the time to serve all customers to 4 hours. However, this usually comes with higher transport costs.  If you want to minimize `vehicles` first and, second, `completion_time`, you can also combine different objectives like this:  ```json \"objectives\" : [    {       \"type\": \"min\",       \"value\": \"vehicles\"    },    {       \"type\": \"min\",       \"value\": \"completion_time\"    } ] ```  If you want to balance activities or the number of stops among all employed drivers, you need to specify it as follows:  ```json \"objectives\" : [    {       \"type\": \"min-max\",       \"value\": \"completion_time\"    },    {       \"type\": \"min-max\",       \"value\": \"activities\"    } ] ``` 
 * @member {module:model/Objective.TypeEnum} type
 * @default 'min'
 */
Objective.prototype['type'] = 'min';

/**
 * The value of the objective function. The objective value `transport_time` solely considers the time your drivers spend on the road, i.e. transport time. In contrary to `transport_time`, `completion_time` also takes waiting times at customer sites into account. The `completion_time` of a route is defined as the time from starting to ending the route, i.e. the route's transport time, the sum of waiting times plus the sum of activity durations. Note that choosing `transport_time` or `completion_time` only makes a difference if you specified time windows for your services/shipments since only in scenarios with time windows waiting times can occur. The objective value `vehicles` can only be used along with `min` and minimizes vehicles. 
 * @member {module:model/Objective.ValueEnum} value
 * @default 'transport_time'
 */
Objective.prototype['value'] = 'transport_time';





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
Objective['TypeEnum'] = {

    /**
     * value: "min"
     * @const
     */
    "min": "min",

    /**
     * value: "min-max"
     * @const
     */
    "min-max": "min-max"
};


/**
 * Allowed values for the <code>value</code> property.
 * @enum {String}
 * @readonly
 */
Objective['ValueEnum'] = {

    /**
     * value: "completion_time"
     * @const
     */
    "completion_time": "completion_time",

    /**
     * value: "transport_time"
     * @const
     */
    "transport_time": "transport_time",

    /**
     * value: "vehicles"
     * @const
     */
    "vehicles": "vehicles",

    /**
     * value: "activities"
     * @const
     */
    "activities": "activities"
};



export default Objective;

