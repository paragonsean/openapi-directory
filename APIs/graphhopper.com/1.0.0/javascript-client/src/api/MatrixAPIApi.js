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


import ApiClient from "../ApiClient";
import GHError from '../model/GHError';
import JobId from '../model/JobId';
import MatrixResponse from '../model/MatrixResponse';
import PostMatrixRequest from '../model/PostMatrixRequest';
import VehicleProfileId from '../model/VehicleProfileId';

/**
* MatrixAPI service.
* @module api/MatrixAPIApi
* @version 1.0.0
*/
export default class MatrixAPIApi {

    /**
    * Constructs a new MatrixAPIApi. 
    * @alias module:api/MatrixAPIApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the calculateMatrix operation.
     * @callback module:api/MatrixAPIApi~calculateMatrixCallback
     * @param {String} error Error message, if any.
     * @param {module:model/JobId} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Batch Matrix Endpoint
     * Prefer the [synchronous endpoint](#operation/postMatrix) and use this Batch endpoint for long running problems only.  The Batch Matrix endpoint allows using matrices with more locations and works asynchronously - similar to the [Batch Route Optimization endpoint](#operation/asyncVRP):  * Create a HTTP POST request against `/matrix/calculate` and add the key in the URL: `/matrix/calculate?key=[YOUR_KEY]`. This will give you the `job_id` from the response json like `{ \"job_id\": \"7ac65787-fb99-4e02-a832-2c3010c70097\" }`  * Poll via HTTP GET requests every 500ms against `/matrix/solution/[job_id]`  Here are some full examples via curl: ```bash $ curl -X POST -H \"Content-Type: application/json\" \"https://graphhopper.com/api/1/matrix/calculate?key=[YOUR_KEY]\" -d '{\"points\":[[13.29895,52.48696],[13.370876,52.489575],[13.439026,52.511206]]}' {\"job_id\":\"7ac65787-fb99-4e02-a832-2c3010c70097\"} ```  Pick the returned `job_id` and use it in the next GET requests: ```bash $ curl -X GET \"https://graphhopper.com/api/1/matrix/solution/7ac65787-fb99-4e02-a832-2c3010c70097?key=[YOUR_KEY]\" {\"status\":\"waiting\"} ```  When the calculation is finished (`status:finished`) the JSON response will contain the full matrix JSON under `solution`: ```bash $ curl -X GET \"https://graphhopper.com/api/1/matrix/solution/7ac65787-fb99-4e02-a832-2c3010c70097?key=[YOUR_KEY]\" {\"solution\":{\"weights\":[[0.0,470.453,945.414],[503.793,0.0,580.871],[970.49,569.511,0.0]],\"info\":{\"copyrights\":[\"GraphHopper\",\"OpenStreetMap contributors\"]}},\"status\":\"finished\"} ```  Please note that if an error occured while calculation the JSON will not have a status but contain directly the error message e.g.: ```json {\"message\":\"Cannot find from_points: 1\"} ``` And the optional `hints` array. 
     * @param {Object} opts Optional parameters
     * @param {module:model/PostMatrixRequest} [postMatrixRequest] 
     * @param {module:api/MatrixAPIApi~calculateMatrixCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/JobId}
     */
    calculateMatrix(opts, callback) {
      opts = opts || {};
      let postBody = opts['postMatrixRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = JobId;
      return this.apiClient.callApi(
        '/matrix/calculate', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMatrix operation.
     * @callback module:api/MatrixAPIApi~getMatrixCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MatrixResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * GET Matrix Endpoint
     * With this Matrix Endpoint you submit the points and parameters via URL parameters and is the most convenient as it works out-of-the-box in the browser. If possible you should prefer using the [POST Matrix Endpoint](#operation/postMatrix) that avoids problems with many locations and can also gzip the **request**. (Note, that all endpoints return gzipped responses). 
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} [point] Specify multiple points in `latitude,longitude` for which the weight-, route-, time- or distance-matrix should be calculated. In this case the starts are identical to the destinations. If there are N points, then NxN entries will be calculated. The order of the point parameter is important. Specify at least three points. Cannot be used together with from_point or to_point.
     * @param {Array.<String>} [fromPoint] The starting points for the routes in `latitude,longitude`. E.g. if you want to calculate the three routes A-&gt;1, A-&gt;2, A-&gt;3 then you have one from_point parameter and three to_point parameters.
     * @param {Array.<String>} [toPoint] The destination points for the routes in `latitude,longitude`.
     * @param {Array.<String>} [pointHint] Optional parameter. Specifies a hint for each `point` parameter to prefer a certain street for the closest location lookup. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up.
     * @param {Array.<String>} [fromPointHint] For the from_point parameter. See point_hint
     * @param {Array.<String>} [toPointHint] For the to_point parameter. See point_hint
     * @param {Array.<String>} [snapPrevention] Optional parameter to avoid snapping to a certain road class or road environment. Current supported values `motorway`, `trunk`, `ferry`, `tunnel`, `bridge` and `ford`. Multiple values are specified like `snap_prevention=ferry&snap_prevention=motorway` 
     * @param {Array.<module:model/String>} [curbside] Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap.
     * @param {Array.<module:model/String>} [fromCurbside] Curbside setting for the from_point parameter. See curbside.
     * @param {Array.<module:model/String>} [toCurbside] Curbside setting for the to_point parameter. See curbside.
     * @param {Array.<String>} [outArray] Specifies which arrays should be included in the response. Specify one or more of the following options 'weights', 'times', 'distances'. To specify more than one array use e.g. out_array=times&out_array=distances. The units of the entries of distances are meters, of times are seconds and of weights is arbitrary and it can differ for different vehicles or versions of this API.
     * @param {module:model/VehicleProfileId} [vehicle] The vehicle profile for which the matrix should be calculated.
     * @param {Boolean} [failFast = true)] Specifies whether or not the matrix calculation should return with an error as soon as possible in case some points cannot be found or some points are not connected. If set to `false` the time/weight/distance matrix will be calculated for all valid points and contain the `null` value for all entries that could not be calculated. The `hint` field of the response will also contain additional information about what went wrong (see its documentation).
     * @param {Boolean} [turnCosts = false)] Specifies if turn restrictions should be considered. Enabling this option increases the matrix computation time. Only supported for motor vehicles and OpenStreetMap.
     * @param {module:api/MatrixAPIApi~getMatrixCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MatrixResponse}
     */
    getMatrix(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'point': this.apiClient.buildCollectionParam(opts['point'], 'multi'),
        'from_point': this.apiClient.buildCollectionParam(opts['fromPoint'], 'multi'),
        'to_point': this.apiClient.buildCollectionParam(opts['toPoint'], 'multi'),
        'point_hint': this.apiClient.buildCollectionParam(opts['pointHint'], 'multi'),
        'from_point_hint': this.apiClient.buildCollectionParam(opts['fromPointHint'], 'multi'),
        'to_point_hint': this.apiClient.buildCollectionParam(opts['toPointHint'], 'multi'),
        'snap_prevention': this.apiClient.buildCollectionParam(opts['snapPrevention'], 'multi'),
        'curbside': this.apiClient.buildCollectionParam(opts['curbside'], 'multi'),
        'from_curbside': this.apiClient.buildCollectionParam(opts['fromCurbside'], 'multi'),
        'to_curbside': this.apiClient.buildCollectionParam(opts['toCurbside'], 'multi'),
        'out_array': this.apiClient.buildCollectionParam(opts['outArray'], 'multi'),
        'vehicle': opts['vehicle'],
        'fail_fast': opts['failFast'],
        'turn_costs': opts['turnCosts']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = MatrixResponse;
      return this.apiClient.callApi(
        '/matrix', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMatrixSolution operation.
     * @callback module:api/MatrixAPIApi~getMatrixSolutionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MatrixResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * GET Batch Matrix Endpoint
     * This endpoint returns the solution of a JSON submitted to the Batch Matrix endpoint. You can fetch it with the job_id, you have been sent. 
     * @param {String} jobId Request solution with jobId
     * @param {module:api/MatrixAPIApi~getMatrixSolutionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MatrixResponse}
     */
    getMatrixSolution(jobId, callback) {
      let postBody = null;
      // verify the required parameter 'jobId' is set
      if (jobId === undefined || jobId === null) {
        throw new Error("Missing the required parameter 'jobId' when calling getMatrixSolution");
      }

      let pathParams = {
        'jobId': jobId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = MatrixResponse;
      return this.apiClient.callApi(
        '/matrix/solution/{jobId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postMatrix operation.
     * @callback module:api/MatrixAPIApi~postMatrixCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MatrixResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * POST Matrix Endpoint
     *  The [GET endpoint](#operation/getMatrix) has an URL length limitation, which hurts for many locations per request. In those cases use this POST endpoint with a JSON as input. The only parameter in the URL will be the key. Both request scenarios are identical except that all singular parameter names are named as their plural for a POST request. The effected parameters are: `points`, `from_points`, `to_points`, and `out_arrays`. For the remaining parameters please refer to the [guide of the GET endpoint](#operation/getMatrix).  **Please note that in contrast to GET endpoint the points have to be specified as `[longitude, latitude]` array (in that order, similar to [GeoJson](http://geojson.org/geojson-spec.html#examples))**.  For example the query `point=10,11&point=20,22&vehicle=car` will be converted to the following JSON: ```json { \"points\": [[11,10], [22,20]], \"vehicle\": \"car\" } ```  A complete curl Example: ```bash curl -X POST -H \"Content-Type: application/json\" \"https://graphhopper.com/api/1/matrix?key=[YOUR_KEY]\" -d '{\"elevation\":false,\"out_arrays\":[\"weights\", \"times\"],\"from_points\":[[-0.087891,51.534377],[-0.090637,51.467697],[-0.171833,51.521241],[-0.211487,51.473685]],\"to_points\":[[-0.087891,51.534377],[-0.090637,51.467697],[-0.171833,51.521241],[-0.211487,51.473685]],\"vehicle\":\"car\"}' ``` 
     * @param {Object} opts Optional parameters
     * @param {module:model/PostMatrixRequest} [postMatrixRequest] 
     * @param {module:api/MatrixAPIApi~postMatrixCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MatrixResponse}
     */
    postMatrix(opts, callback) {
      opts = opts || {};
      let postBody = opts['postMatrixRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = MatrixResponse;
      return this.apiClient.callApi(
        '/matrix', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
