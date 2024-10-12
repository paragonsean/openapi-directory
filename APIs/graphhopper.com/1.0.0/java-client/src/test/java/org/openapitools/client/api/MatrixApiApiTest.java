/*
 * GraphHopper Directions API
 *  With the [GraphHopper Directions API](https://www.graphhopper.com/products/) you can integrate A-to-B route planning, turn-by-turn navigation, route optimization, isochrone calculations and other tools in your application.  The GraphHopper Directions API consists of the following RESTful web services:   * [Routing API](#tag/Routing-API),  * [Route Optimization API](#tag/Route-Optimization-API),  * [Isochrone API](#tag/Isochrone-API),  * [Map Matching API](#tag/Map-Matching-API),  * [Matrix API](#tag/Matrix-API),  * [Geocoding API](#tag/Geocoding-API) and  * [Cluster API](#tag/Cluster-API).  # Explore our APIs  ## Get started  1. [Sign up for GraphHopper](https://support.graphhopper.com/a/solutions/articles/44001976025) 2. [Create an API key](https://support.graphhopper.com/a/solutions/articles/44001976027)  Each API part has its own documentation. Jump to the desired API part and learn about the API through the given examples and tutorials.  In addition, for each API there are specific sample requests that you can send via Insomnia or Postman to see what the requests and responses look like.  ## Insomnia  To explore our APIs with [Insomnia](https://insomnia.rest/), follow these steps:  1. Open Insomnia and Import [our workspace](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/GraphHopper-Direction-API-Insomnia.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your workspace: Manage Environments -> Base Environment -> `\"api_key\": your API key` 3. Start exploring  ![Insomnia](./img/insomnia.png)  ## Postman  To explore our APIs with [Postman](https://www.getpostman.com/), follow these steps:  1. Import our [request collections](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_collection.json) as well as our [environment file](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_environment.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your environment: `\"api_key\": your API key` 3. Start exploring  ![Postman](./img/postman.png)  ## API Client Libraries  To speed up development and make coding easier, we offer the following client libraries:   * [JavaScript client](https://github.com/graphhopper/directions-api-js-client) - try the [live examples](https://graphhopper.com/api/1/examples/)  * [Others](https://github.com/graphhopper/directions-api-clients) like C#, Ruby, PHP, Python, ... automatically created for the Route Optimization API  ### Bandwidth reduction  If you create your own client, make sure it supports http/2 and gzipped responses for best speed.  If you use the Matrix, the Route Optimization API or the Cluster API and want to solve large problems, we recommend you to reduce bandwidth by [compressing your POST request](https://gist.github.com/karussell/82851e303ea7b3459b2dea01f18949f4) and specifying the header as follows: `Content-Encoding: gzip`. This will also avoid the HTTP 413 error \"Request Entity Too Large\".  ## Contact Us  If you have problems or questions, please read the following information:  - [FAQ](https://graphhopper.com/api/1/docs/FAQ/) - [Public forum](https://discuss.graphhopper.com/c/directions-api) - [Contact us](https://www.graphhopper.com/contact-form/) - [GraphHopper Status Page](https://status.graphhopper.com/)  To stay informed about the latest developments, you can  - follow us on [twitter](https://twitter.com/graphhopper/), - read [our blog](https://graphhopper.com/blog/), - watch [our documentation repository](https://github.com/graphhopper/directions-api-doc), - sign up for our newsletter or - [our forum](https://discuss.graphhopper.com/c/directions-api).  Select the channel you like the most.   # Map Data and Routing Profiles  Currently, our main data source is [OpenStreetMap](https://www.openstreetmap.org). We also integrated other network data providers. This chapter gives an overview about the options you have.  ## OpenStreetMap  #### Geographical Coverage  [OpenStreetMap](https://www.openstreetmap.org) covers the whole world. If you want to see for yourself if we can provide data suitable for your region, please visit [GraphHopper Maps](https://graphhopper.com/maps/). You can edit and modify OpenStreetMap data if you find that important information is missing, e.g. a weight limit for a bridge. [Here](https://wiki.openstreetmap.org/wiki/Beginners%27_guide) is a beginner's guide that shows how to add data. If you have edited data, we usually consider your data after 1 week at the latest.  #### Supported Vehicle Profiles  The Routing, Matrix and Route Optimization APIs support the following vehicle profiles:  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) truck      | Truck like a MAN or Mercedes-Benz Actros | height=3.7m, width=2.6+0.5m, length=12m, weight=13000 + 13000 kg, hgv=yes, 3 Axes | ![truck image](https://graphhopper.com/maps/img/truck.png) scooter    | Moped mode | Fast inner city, often used for food delivery, is able to ignore certain bollards, maximum speed of roughly 50km/h | ![scooter image](https://graphhopper.com/maps/img/scooter.png) foot       | Pedestrian or walking without dangerous [SAC-scales](https://wiki.openstreetmap.org/wiki/Key:sac_scale) | foot access         | ![foot image](https://graphhopper.com/maps/img/foot.png) hike       | Pedestrian or walking with priority for more beautiful hiking tours and potentially a bit longer than `foot`. Walking duration is influenced by elevation differences.  | foot access         | ![hike image](https://graphhopper.com/maps/img/hike.png) bike       | Trekking bike avoiding hills | bike access  | ![bike image](https://graphhopper.com/maps/img/bike.png) mtb        | Mountainbike          | bike access         | ![Mountainbike image](https://graphhopper.com/maps/img/mtb.png) racingbike| Bike preferring roads | bike access         | ![racingbike image](https://graphhopper.com/maps/img/racingbike.png)  Please note:   * all motor vehicles (`car`, `small_truck`, `truck` and `scooter`) support turn restrictions via `turn_costs=true`  * the free package supports only the vehicle profiles `car`, `bike` or `foot`  * up to 2 different vehicle profiles can be used in a single optimization request. The number of vehicles is unaffected and depends on your subscription.  * we offer custom vehicle profiles with different properties, different speed profiles or different access options. To find out more about custom profiles, please [contact us](https://www.graphhopper.com/contact-form/).  * a sophisticated `motorcycle` profile is available up on request. It is powered by the [Kurviger](https://kurviger.de/en) Routing API and favors curves and slopes while avoiding cities and highways.   ## TomTom  If you want to include traffic, you can purchase the TomTom Add-on. This Add-on only uses TomTom's road network and historical traffic information. Live traffic is not yet considered. If you are interested to learn how we consider traffic information, we recommend that you read [this article](https://www.graphhopper.com/blog/2017/11/06/time-dependent-optimization/).  Please note the following:   * Currently we only offer this for our [Route Optimization API](#tag/Route-Optimization-API).  * In addition to our terms, you need to accept TomTom's [End User License Aggreement](https://www.graphhopper.com/tomtom-end-user-license-agreement/).  * We do *not* use TomTom's web services. We only use their data with our software.   [Contact us](https://www.graphhopper.com/contact-form/) for more details.  #### Geographical Coverage  We offer  - Europe including Russia - North, Central and South America - Saudi Arabia - United Arab Emirates - South Africa - Australia  #### Supported Vehicle Profiles  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@graphhopper.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.GHError;
import org.openapitools.client.model.JobId;
import org.openapitools.client.model.MatrixResponse;
import org.openapitools.client.model.PostMatrixRequest;
import org.openapitools.client.model.VehicleProfileId;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for MatrixApiApi
 */
@Disabled
public class MatrixApiApiTest {

    private final MatrixApiApi api = new MatrixApiApi();

    /**
     * Batch Matrix Endpoint
     *
     * Prefer the [synchronous endpoint](#operation/postMatrix) and use this Batch endpoint for long running problems only.  The Batch Matrix endpoint allows using matrices with more locations and works asynchronously - similar to the [Batch Route Optimization endpoint](#operation/asyncVRP):  * Create a HTTP POST request against &#x60;/matrix/calculate&#x60; and add the key in the URL: &#x60;/matrix/calculate?key&#x3D;[YOUR_KEY]&#x60;. This will give you the &#x60;job_id&#x60; from the response json like &#x60;{ \&quot;job_id\&quot;: \&quot;7ac65787-fb99-4e02-a832-2c3010c70097\&quot; }&#x60;  * Poll via HTTP GET requests every 500ms against &#x60;/matrix/solution/[job_id]&#x60;  Here are some full examples via curl: &#x60;&#x60;&#x60;bash $ curl -X POST -H \&quot;Content-Type: application/json\&quot; \&quot;https://graphhopper.com/api/1/matrix/calculate?key&#x3D;[YOUR_KEY]\&quot; -d &#39;{\&quot;points\&quot;:[[13.29895,52.48696],[13.370876,52.489575],[13.439026,52.511206]]}&#39; {\&quot;job_id\&quot;:\&quot;7ac65787-fb99-4e02-a832-2c3010c70097\&quot;} &#x60;&#x60;&#x60;  Pick the returned &#x60;job_id&#x60; and use it in the next GET requests: &#x60;&#x60;&#x60;bash $ curl -X GET \&quot;https://graphhopper.com/api/1/matrix/solution/7ac65787-fb99-4e02-a832-2c3010c70097?key&#x3D;[YOUR_KEY]\&quot; {\&quot;status\&quot;:\&quot;waiting\&quot;} &#x60;&#x60;&#x60;  When the calculation is finished (&#x60;status:finished&#x60;) the JSON response will contain the full matrix JSON under &#x60;solution&#x60;: &#x60;&#x60;&#x60;bash $ curl -X GET \&quot;https://graphhopper.com/api/1/matrix/solution/7ac65787-fb99-4e02-a832-2c3010c70097?key&#x3D;[YOUR_KEY]\&quot; {\&quot;solution\&quot;:{\&quot;weights\&quot;:[[0.0,470.453,945.414],[503.793,0.0,580.871],[970.49,569.511,0.0]],\&quot;info\&quot;:{\&quot;copyrights\&quot;:[\&quot;GraphHopper\&quot;,\&quot;OpenStreetMap contributors\&quot;]}},\&quot;status\&quot;:\&quot;finished\&quot;} &#x60;&#x60;&#x60;  Please note that if an error occured while calculation the JSON will not have a status but contain directly the error message e.g.: &#x60;&#x60;&#x60;json {\&quot;message\&quot;:\&quot;Cannot find from_points: 1\&quot;} &#x60;&#x60;&#x60; And the optional &#x60;hints&#x60; array. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void calculateMatrixTest() throws ApiException {
        PostMatrixRequest postMatrixRequest = null;
        JobId response = api.calculateMatrix(postMatrixRequest);
        // TODO: test validations
    }

    /**
     * GET Matrix Endpoint
     *
     * With this Matrix Endpoint you submit the points and parameters via URL parameters and is the most convenient as it works out-of-the-box in the browser. If possible you should prefer using the [POST Matrix Endpoint](#operation/postMatrix) that avoids problems with many locations and can also gzip the **request**. (Note, that all endpoints return gzipped responses). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getMatrixTest() throws ApiException {
        List<String> point = null;
        List<String> fromPoint = null;
        List<String> toPoint = null;
        List<String> pointHint = null;
        List<String> fromPointHint = null;
        List<String> toPointHint = null;
        List<String> snapPrevention = null;
        List<String> curbside = null;
        List<String> fromCurbside = null;
        List<String> toCurbside = null;
        List<String> outArray = null;
        VehicleProfileId vehicle = null;
        Boolean failFast = null;
        Boolean turnCosts = null;
        MatrixResponse response = api.getMatrix(point, fromPoint, toPoint, pointHint, fromPointHint, toPointHint, snapPrevention, curbside, fromCurbside, toCurbside, outArray, vehicle, failFast, turnCosts);
        // TODO: test validations
    }

    /**
     * GET Batch Matrix Endpoint
     *
     * This endpoint returns the solution of a JSON submitted to the Batch Matrix endpoint. You can fetch it with the job_id, you have been sent. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getMatrixSolutionTest() throws ApiException {
        String jobId = null;
        MatrixResponse response = api.getMatrixSolution(jobId);
        // TODO: test validations
    }

    /**
     * POST Matrix Endpoint
     *
     *  The [GET endpoint](#operation/getMatrix) has an URL length limitation, which hurts for many locations per request. In those cases use this POST endpoint with a JSON as input. The only parameter in the URL will be the key. Both request scenarios are identical except that all singular parameter names are named as their plural for a POST request. The effected parameters are: &#x60;points&#x60;, &#x60;from_points&#x60;, &#x60;to_points&#x60;, and &#x60;out_arrays&#x60;. For the remaining parameters please refer to the [guide of the GET endpoint](#operation/getMatrix).  **Please note that in contrast to GET endpoint the points have to be specified as &#x60;[longitude, latitude]&#x60; array (in that order, similar to [GeoJson](http://geojson.org/geojson-spec.html#examples))**.  For example the query &#x60;point&#x3D;10,11&amp;point&#x3D;20,22&amp;vehicle&#x3D;car&#x60; will be converted to the following JSON: &#x60;&#x60;&#x60;json { \&quot;points\&quot;: [[11,10], [22,20]], \&quot;vehicle\&quot;: \&quot;car\&quot; } &#x60;&#x60;&#x60;  A complete curl Example: &#x60;&#x60;&#x60;bash curl -X POST -H \&quot;Content-Type: application/json\&quot; \&quot;https://graphhopper.com/api/1/matrix?key&#x3D;[YOUR_KEY]\&quot; -d &#39;{\&quot;elevation\&quot;:false,\&quot;out_arrays\&quot;:[\&quot;weights\&quot;, \&quot;times\&quot;],\&quot;from_points\&quot;:[[-0.087891,51.534377],[-0.090637,51.467697],[-0.171833,51.521241],[-0.211487,51.473685]],\&quot;to_points\&quot;:[[-0.087891,51.534377],[-0.090637,51.467697],[-0.171833,51.521241],[-0.211487,51.473685]],\&quot;vehicle\&quot;:\&quot;car\&quot;}&#39; &#x60;&#x60;&#x60; 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postMatrixTest() throws ApiException {
        PostMatrixRequest postMatrixRequest = null;
        MatrixResponse response = api.postMatrix(postMatrixRequest);
        // TODO: test validations
    }

}
