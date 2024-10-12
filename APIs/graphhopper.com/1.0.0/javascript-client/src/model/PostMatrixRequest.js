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
import MatrixRequest from './MatrixRequest';
import SymmetricalMatrixRequest from './SymmetricalMatrixRequest';
import VehicleProfileId from './VehicleProfileId';

/**
 * The PostMatrixRequest model module.
 * @module model/PostMatrixRequest
 * @version 1.0.0
 */
class PostMatrixRequest {
    /**
     * Constructs a new <code>PostMatrixRequest</code>.
     * @alias module:model/PostMatrixRequest
     * @param {(module:model/MatrixRequest|module:model/SymmetricalMatrixRequest)} instance The actual instance to initialize PostMatrixRequest.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "MatrixRequest") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                MatrixRequest.validateJSON(instance); // throw an exception if no match
                // create MatrixRequest from JS object
                this.actualInstance = MatrixRequest.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into MatrixRequest
            errorMessages.push("Failed to construct MatrixRequest: " + err)
        }

        try {
            if (typeof instance === "SymmetricalMatrixRequest") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                SymmetricalMatrixRequest.validateJSON(instance); // throw an exception if no match
                // create SymmetricalMatrixRequest from JS object
                this.actualInstance = SymmetricalMatrixRequest.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into SymmetricalMatrixRequest
            errorMessages.push("Failed to construct SymmetricalMatrixRequest: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `PostMatrixRequest` with oneOf schemas MatrixRequest, SymmetricalMatrixRequest. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `PostMatrixRequest` with oneOf schemas MatrixRequest, SymmetricalMatrixRequest. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>PostMatrixRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PostMatrixRequest} obj Optional instance to populate.
     * @return {module:model/PostMatrixRequest} The populated <code>PostMatrixRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        return new PostMatrixRequest(data);
    }

    /**
     * Gets the actual instance, which can be <code>MatrixRequest</code>, <code>SymmetricalMatrixRequest</code>.
     * @return {(module:model/MatrixRequest|module:model/SymmetricalMatrixRequest)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>MatrixRequest</code>, <code>SymmetricalMatrixRequest</code>.
     * @param {(module:model/MatrixRequest|module:model/SymmetricalMatrixRequest)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = PostMatrixRequest.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of PostMatrixRequest from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/PostMatrixRequest} An instance of PostMatrixRequest.
     */
    static fromJSON = function(json_string){
        return PostMatrixRequest.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * Specifies whether or not the matrix calculation should return with an error as soon as possible in case some points cannot be found or some points are not connected. If set to `false` the time/weight/distance matrix will be calculated for all valid points and contain the `null` value for all entries that could not be calculated. The `hint` field of the response will also contain additional information about what went wrong (see its documentation).
 * @member {Boolean} fail_fast
 * @default true
 */
PostMatrixRequest.prototype['fail_fast'] = true;

/**
 * See `curbsides`of symmetrical matrix
 * @member {Array.<String>} from_curbsides
 */
PostMatrixRequest.prototype['from_curbsides'] = undefined;

/**
 * See `point_hints`of symmetrical matrix
 * @member {Array.<String>} from_point_hints
 */
PostMatrixRequest.prototype['from_point_hints'] = undefined;

/**
 * The starting points for the routes in an array of `[longitude,latitude]`. For instance, if you want to calculate three routes from point A such as A->1, A->2, A->3 then you have one `from_point` parameter and three `to_point` parameters.
 * @member {Array.<Array.<Number>>} from_points
 */
PostMatrixRequest.prototype['from_points'] = undefined;

/**
 * Specifies which matrices should be included in the response. Specify one or more of the following options `weights`, `times`, `distances`. The units of the entries of `distances` are meters, of `times` are seconds and of `weights` is arbitrary and it can differ for different vehicles or versions of this API.
 * @member {Array.<String>} out_arrays
 */
PostMatrixRequest.prototype['out_arrays'] = undefined;

/**
 * Optional parameter to avoid snapping to a certain road class or road environment. Current supported values `motorway`, `trunk`, `ferry`, `tunnel`, `bridge` and `ford`
 * @member {Array.<String>} snap_preventions
 */
PostMatrixRequest.prototype['snap_preventions'] = undefined;

/**
 * See `curbsides`of symmetrical matrix
 * @member {Array.<String>} to_curbsides
 */
PostMatrixRequest.prototype['to_curbsides'] = undefined;

/**
 * See `point_hints`of symmetrical matrix
 * @member {Array.<String>} to_point_hints
 */
PostMatrixRequest.prototype['to_point_hints'] = undefined;

/**
 * The destination points for the routes in an array of `[longitude,latitude]`.
 * @member {Array.<Array.<Number>>} to_points
 */
PostMatrixRequest.prototype['to_points'] = undefined;

/**
 * Specifies if turn restrictions should be considered. Enabling this option increases the matrix computation time. Only supported for motor vehicles and OpenStreetMap.
 * @member {Boolean} turn_costs
 * @default false
 */
PostMatrixRequest.prototype['turn_costs'] = false;

/**
 * @member {module:model/VehicleProfileId} vehicle
 */
PostMatrixRequest.prototype['vehicle'] = undefined;

/**
 * Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap.
 * @member {Array.<String>} curbsides
 */
PostMatrixRequest.prototype['curbsides'] = undefined;

/**
 * Optional parameter. Specifies a hint for each point in the `points` array to prefer a certain street for the closest location lookup. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up.
 * @member {Array.<String>} point_hints
 */
PostMatrixRequest.prototype['point_hints'] = undefined;

/**
 * Specify multiple points for which the weight-, route-, time- or distance-matrix should be calculated as follows: `[longitude,latitude]`. In this case the origins are identical to the destinations. Thus, if there are N points, NxN entries are calculated. The order of the point parameter is important. Specify at least three points. Cannot be used together with `from_point` or `to_point.`.
 * @member {Array.<Array.<Number>>} points
 */
PostMatrixRequest.prototype['points'] = undefined;


PostMatrixRequest.OneOf = ["MatrixRequest", "SymmetricalMatrixRequest"];

export default PostMatrixRequest;

