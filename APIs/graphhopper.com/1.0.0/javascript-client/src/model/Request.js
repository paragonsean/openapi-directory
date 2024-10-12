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
import Algorithm from './Algorithm';
import Configuration from './Configuration';
import CostMatrix from './CostMatrix';
import Objective from './Objective';
import RequestRelationsInner from './RequestRelationsInner';
import Service from './Service';
import Shipment from './Shipment';
import Vehicle from './Vehicle';
import VehicleType from './VehicleType';

/**
 * The Request model module.
 * @module model/Request
 * @version 1.0.0
 */
class Request {
    /**
     * Constructs a new <code>Request</code>.
     * @alias module:model/Request
     */
    constructor() { 
        
        Request.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Request</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Request} obj Optional instance to populate.
     * @return {module:model/Request} The populated <code>Request</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Request();

            if (data.hasOwnProperty('algorithm')) {
                obj['algorithm'] = Algorithm.constructFromObject(data['algorithm']);
            }
            if (data.hasOwnProperty('configuration')) {
                obj['configuration'] = Configuration.constructFromObject(data['configuration']);
            }
            if (data.hasOwnProperty('cost_matrices')) {
                obj['cost_matrices'] = ApiClient.convertToType(data['cost_matrices'], [CostMatrix]);
            }
            if (data.hasOwnProperty('objectives')) {
                obj['objectives'] = ApiClient.convertToType(data['objectives'], [Objective]);
            }
            if (data.hasOwnProperty('relations')) {
                obj['relations'] = ApiClient.convertToType(data['relations'], [RequestRelationsInner]);
            }
            if (data.hasOwnProperty('services')) {
                obj['services'] = ApiClient.convertToType(data['services'], [Service]);
            }
            if (data.hasOwnProperty('shipments')) {
                obj['shipments'] = ApiClient.convertToType(data['shipments'], [Shipment]);
            }
            if (data.hasOwnProperty('vehicle_types')) {
                obj['vehicle_types'] = ApiClient.convertToType(data['vehicle_types'], [VehicleType]);
            }
            if (data.hasOwnProperty('vehicles')) {
                obj['vehicles'] = ApiClient.convertToType(data['vehicles'], [Vehicle]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Request</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Request</code>.
     */
    static validateJSON(data) {
        // validate the optional field `algorithm`
        if (data['algorithm']) { // data not null
          Algorithm.validateJSON(data['algorithm']);
        }
        // validate the optional field `configuration`
        if (data['configuration']) { // data not null
          Configuration.validateJSON(data['configuration']);
        }
        if (data['cost_matrices']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['cost_matrices'])) {
                throw new Error("Expected the field `cost_matrices` to be an array in the JSON data but got " + data['cost_matrices']);
            }
            // validate the optional field `cost_matrices` (array)
            for (const item of data['cost_matrices']) {
                CostMatrix.validateJSON(item);
            };
        }
        if (data['objectives']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['objectives'])) {
                throw new Error("Expected the field `objectives` to be an array in the JSON data but got " + data['objectives']);
            }
            // validate the optional field `objectives` (array)
            for (const item of data['objectives']) {
                Objective.validateJSON(item);
            };
        }
        if (data['relations']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['relations'])) {
                throw new Error("Expected the field `relations` to be an array in the JSON data but got " + data['relations']);
            }
            // validate the optional field `relations` (array)
            for (const item of data['relations']) {
                RequestRelationsInner.validateJSON(item);
            };
        }
        if (data['services']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['services'])) {
                throw new Error("Expected the field `services` to be an array in the JSON data but got " + data['services']);
            }
            // validate the optional field `services` (array)
            for (const item of data['services']) {
                Service.validateJSON(item);
            };
        }
        if (data['shipments']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['shipments'])) {
                throw new Error("Expected the field `shipments` to be an array in the JSON data but got " + data['shipments']);
            }
            // validate the optional field `shipments` (array)
            for (const item of data['shipments']) {
                Shipment.validateJSON(item);
            };
        }
        if (data['vehicle_types']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['vehicle_types'])) {
                throw new Error("Expected the field `vehicle_types` to be an array in the JSON data but got " + data['vehicle_types']);
            }
            // validate the optional field `vehicle_types` (array)
            for (const item of data['vehicle_types']) {
                VehicleType.validateJSON(item);
            };
        }
        if (data['vehicles']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['vehicles'])) {
                throw new Error("Expected the field `vehicles` to be an array in the JSON data but got " + data['vehicles']);
            }
            // validate the optional field `vehicles` (array)
            for (const item of data['vehicles']) {
                Vehicle.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/Algorithm} algorithm
 */
Request.prototype['algorithm'] = undefined;

/**
 * @member {module:model/Configuration} configuration
 */
Request.prototype['configuration'] = undefined;

/**
 * Specifies your own tranport time and distance matrices.
 * @member {Array.<module:model/CostMatrix>} cost_matrices
 */
Request.prototype['cost_matrices'] = undefined;

/**
 * Specifies an objective function. The vehicle routing problem is solved in such a way that this objective function is minimized.
 * @member {Array.<module:model/Objective>} objectives
 */
Request.prototype['objectives'] = undefined;

/**
 * Defines additional relationships between orders.
 * @member {Array.<module:model/RequestRelationsInner>} relations
 */
Request.prototype['relations'] = undefined;

/**
 * Specifies the orders of the type \"service\". These are, for example, pick-ups, deliveries or other stops that are to be approached by the specified vehicles. Each of these orders contains only one location.
 * @member {Array.<module:model/Service>} services
 */
Request.prototype['services'] = undefined;

/**
 * Specifies the available shipments. Each shipment contains a pickup and a delivery stop, which must be processed one after the other.
 * @member {Array.<module:model/Shipment>} shipments
 */
Request.prototype['shipments'] = undefined;

/**
 * Specifies the available vehicle types. These types can be assigned to vehicles.
 * @member {Array.<module:model/VehicleType>} vehicle_types
 */
Request.prototype['vehicle_types'] = undefined;

/**
 * Specifies the available vehicles.
 * @member {Array.<module:model/Vehicle>} vehicles
 */
Request.prototype['vehicles'] = undefined;






export default Request;

