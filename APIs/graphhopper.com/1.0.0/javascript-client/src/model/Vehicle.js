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
import Address from './Address';
import VehicleBreak from './VehicleBreak';

/**
 * The Vehicle model module.
 * @module model/Vehicle
 * @version 1.0.0
 */
class Vehicle {
    /**
     * Constructs a new <code>Vehicle</code>.
     * @alias module:model/Vehicle
     * @param startAddress {module:model/Address} 
     * @param vehicleId {String} Specifies the ID of the vehicle. Ids must be unique, i.e. if there are two vehicles with the same ID, an error is returned.
     */
    constructor(startAddress, vehicleId) { 
        
        Vehicle.initialize(this, startAddress, vehicleId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, startAddress, vehicleId) { 
        obj['earliest_start'] = 0;
        obj['return_to_depot'] = true;
        obj['start_address'] = startAddress;
        obj['type_id'] = 'default-type';
        obj['vehicle_id'] = vehicleId;
    }

    /**
     * Constructs a <code>Vehicle</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Vehicle} obj Optional instance to populate.
     * @return {module:model/Vehicle} The populated <code>Vehicle</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Vehicle();

            if (data.hasOwnProperty('break')) {
                obj['break'] = VehicleBreak.constructFromObject(data['break']);
            }
            if (data.hasOwnProperty('earliest_start')) {
                obj['earliest_start'] = ApiClient.convertToType(data['earliest_start'], 'Number');
            }
            if (data.hasOwnProperty('end_address')) {
                obj['end_address'] = Address.constructFromObject(data['end_address']);
            }
            if (data.hasOwnProperty('latest_end')) {
                obj['latest_end'] = ApiClient.convertToType(data['latest_end'], 'Number');
            }
            if (data.hasOwnProperty('max_activities')) {
                obj['max_activities'] = ApiClient.convertToType(data['max_activities'], 'Number');
            }
            if (data.hasOwnProperty('max_distance')) {
                obj['max_distance'] = ApiClient.convertToType(data['max_distance'], 'Number');
            }
            if (data.hasOwnProperty('max_driving_time')) {
                obj['max_driving_time'] = ApiClient.convertToType(data['max_driving_time'], 'Number');
            }
            if (data.hasOwnProperty('max_jobs')) {
                obj['max_jobs'] = ApiClient.convertToType(data['max_jobs'], 'Number');
            }
            if (data.hasOwnProperty('min_jobs')) {
                obj['min_jobs'] = ApiClient.convertToType(data['min_jobs'], 'Number');
            }
            if (data.hasOwnProperty('move_to_end_address')) {
                obj['move_to_end_address'] = ApiClient.convertToType(data['move_to_end_address'], 'Boolean');
            }
            if (data.hasOwnProperty('return_to_depot')) {
                obj['return_to_depot'] = ApiClient.convertToType(data['return_to_depot'], 'Boolean');
            }
            if (data.hasOwnProperty('skills')) {
                obj['skills'] = ApiClient.convertToType(data['skills'], ['String']);
            }
            if (data.hasOwnProperty('start_address')) {
                obj['start_address'] = Address.constructFromObject(data['start_address']);
            }
            if (data.hasOwnProperty('type_id')) {
                obj['type_id'] = ApiClient.convertToType(data['type_id'], 'String');
            }
            if (data.hasOwnProperty('vehicle_id')) {
                obj['vehicle_id'] = ApiClient.convertToType(data['vehicle_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Vehicle</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Vehicle</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Vehicle.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `break`
        if (data['break']) { // data not null
          VehicleBreak.validateJSON(data['break']);
        }
        // validate the optional field `end_address`
        if (data['end_address']) { // data not null
          Address.validateJSON(data['end_address']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['skills'])) {
            throw new Error("Expected the field `skills` to be an array in the JSON data but got " + data['skills']);
        }
        // validate the optional field `start_address`
        if (data['start_address']) { // data not null
          Address.validateJSON(data['start_address']);
        }
        // ensure the json data is a string
        if (data['type_id'] && !(typeof data['type_id'] === 'string' || data['type_id'] instanceof String)) {
            throw new Error("Expected the field `type_id` to be a primitive type in the JSON string but got " + data['type_id']);
        }
        // ensure the json data is a string
        if (data['vehicle_id'] && !(typeof data['vehicle_id'] === 'string' || data['vehicle_id'] instanceof String)) {
            throw new Error("Expected the field `vehicle_id` to be a primitive type in the JSON string but got " + data['vehicle_id']);
        }

        return true;
    }


}

Vehicle.RequiredProperties = ["start_address", "vehicle_id"];

/**
 * @member {module:model/VehicleBreak} break
 */
Vehicle.prototype['break'] = undefined;

/**
 * Earliest start of vehicle in seconds. It is recommended to use the unix timestamp.
 * @member {Number} earliest_start
 * @default 0
 */
Vehicle.prototype['earliest_start'] = 0;

/**
 * @member {module:model/Address} end_address
 */
Vehicle.prototype['end_address'] = undefined;

/**
 * Latest end of vehicle in seconds, i.e. the time the vehicle needs to be at its end location at latest.
 * @member {Number} latest_end
 */
Vehicle.prototype['latest_end'] = undefined;

/**
 * Specifies the maximum number of activities a vehicle can conduct.
 * @member {Number} max_activities
 */
Vehicle.prototype['max_activities'] = undefined;

/**
 * Specifies the maximum distance (in meters) a vehicle can go.
 * @member {Number} max_distance
 */
Vehicle.prototype['max_distance'] = undefined;

/**
 * Specifies the maximum drive time (in seconds) a vehicle/driver can go, i.e. the maximum time on the road (service and waiting times are not included here)
 * @member {Number} max_driving_time
 */
Vehicle.prototype['max_driving_time'] = undefined;

/**
 * Specifies the maximum number of jobs a vehicle can load.
 * @member {Number} max_jobs
 */
Vehicle.prototype['max_jobs'] = undefined;

/**
 * Specifies the minimum number of jobs a vehicle should load. This is a soft constraint, i.e. if it is not possible to fulfill “min_jobs”, we will still try to get as close as possible to this constraint.
 * @member {Number} min_jobs
 */
Vehicle.prototype['min_jobs'] = undefined;

/**
 * Indicates whether a vehicle should be moved even though it has not been assigned any jobs.
 * @member {Boolean} move_to_end_address
 */
Vehicle.prototype['move_to_end_address'] = undefined;

/**
 * If it is false, the algorithm decides where to end the vehicle route. It ends in one of your customers' locations. The end is chosen such that it contributes to the overall objective function, e.g. min transport_time. If it is true, you can either specify a specific end location (which is then regarded as end depot) or you can leave it and the driver returns to its start location.
 * @member {Boolean} return_to_depot
 * @default true
 */
Vehicle.prototype['return_to_depot'] = true;

/**
 * Array of skills, i.e. array of string (not case sensitive).
 * @member {Array.<String>} skills
 */
Vehicle.prototype['skills'] = undefined;

/**
 * @member {module:model/Address} start_address
 */
Vehicle.prototype['start_address'] = undefined;

/**
 * The type ID assigns a vehicle type to this vehicle. You can specify types in the array of vehicle types. If you omit the type ID, the default type is used. The default type is a `car` with a capacity of 0.
 * @member {String} type_id
 * @default 'default-type'
 */
Vehicle.prototype['type_id'] = 'default-type';

/**
 * Specifies the ID of the vehicle. Ids must be unique, i.e. if there are two vehicles with the same ID, an error is returned.
 * @member {String} vehicle_id
 */
Vehicle.prototype['vehicle_id'] = undefined;






export default Vehicle;

