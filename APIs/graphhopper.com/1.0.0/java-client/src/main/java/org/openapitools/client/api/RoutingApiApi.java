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

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import java.math.BigDecimal;
import org.openapitools.client.model.GHError;
import org.openapitools.client.model.InfoResponse;
import org.openapitools.client.model.RouteRequest;
import org.openapitools.client.model.RouteResponse;
import org.openapitools.client.model.VehicleProfileId;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class RoutingApiApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public RoutingApiApi() {
        this(Configuration.getDefaultApiClient());
    }

    public RoutingApiApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for getRoute
     * @param point The points for which the route should be calculated. Format: &#x60;[latitude,longitude]&#x60;. Specify at least an origin and a destination. Via points are possible. The maximum number depends on your plan.  (required)
     * @param pointHint The &#x60;point_hint&#x60; is typically a road name to which the associated &#x60;point&#x60; parameter should be snapped to. Specify no &#x60;point_hint&#x60; parameter or the same number as you have &#x60;point&#x60; parameters.  (optional)
     * @param snapPrevention Optional parameter to avoid snapping to a certain road class or road environment. Currently supported values are &#x60;motorway&#x60;, &#x60;trunk&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60;, &#x60;bridge&#x60; and &#x60;ford&#x60;. Multiple values are specified like &#x60;snap_prevention&#x3D;ferry&amp;snap_prevention&#x3D;motorway&#x60;.  (optional)
     * @param vehicle The vehicle profile for which the route should be calculated.  (optional, default to car)
     * @param curbside Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap.  (optional)
     * @param turnCosts Specifies if turn restrictions should be considered. Enabling this option increases the route computation time. Only supported for motor vehicles and OpenStreetMap.  (optional, default to false)
     * @param locale The locale of the resulting turn instructions. E.g. &#x60;pt_PT&#x60; for Portuguese or &#x60;de&#x60; for German.  (optional, default to en)
     * @param elevation If &#x60;true&#x60;, a third coordinate, the altitude, is included with all positions in the response. This changes the format of the &#x60;points&#x60; and &#x60;snapped_waypoints&#x60; fields of the response, in both their encodings. Unless you switch off the &#x60;points_encoded&#x60; parameter, you need special code on the client side that can handle three-dimensional coordinates. A request can fail if the vehicle profile does not support elevation. See the features object for every vehicle profile.  (optional, default to false)
     * @param details Optional parameter to retrieve path details. You can request additional details for the route: &#x60;street_name&#x60;,  &#x60;time&#x60;, &#x60;distance&#x60;, &#x60;max_speed&#x60;, &#x60;toll&#x60;, &#x60;road_class&#x60;, &#x60;road_class_link&#x60;, &#x60;road_access&#x60;, &#x60;road_environment&#x60;, &#x60;lanes&#x60;, and &#x60;surface&#x60;. Read more about the usage of path details [here](https://discuss.graphhopper.com/t/2539).  (optional)
     * @param optimize Normally, the calculated route will visit the points in the order you specified them. If you have more than two points, you can set this parameter to &#x60;\&quot;true\&quot;&#x60; and the points may be re-ordered to minimize the total travel time. Keep in mind that the limits on the number of locations of the Route Optimization API applies, and the request costs more credits.  (optional, default to false)
     * @param instructions If instructions should be calculated and returned  (optional, default to true)
     * @param calcPoints If the points for the route should be calculated at all.  (optional, default to true)
     * @param debug If &#x60;true&#x60;, the output will be formatted.  (optional, default to false)
     * @param pointsEncoded Allows changing the encoding of location data in the response. The default is polyline encoding, which is compact but requires special client code to unpack. (We provide it in our JavaScript client library!) Set this parameter to &#x60;false&#x60; to switch the encoding to simple coordinate pairs like &#x60;[lon,lat]&#x60;, or &#x60;[lon,lat,elevation]&#x60;. See the description of the response format for more information.  (optional, default to true)
     * @param chDisable Use this parameter in combination with one or more parameters from below.  (optional, default to false)
     * @param weighting Determines the way the \&quot;best\&quot; route is calculated. Besides &#x60;fastest&#x60; you can use &#x60;short_fastest&#x60; which finds a reasonable balance between the distance influence (&#x60;shortest&#x60;) and the time (&#x60;fastest&#x60;). You could also use &#x60;shortest&#x60; but is deprecated and not recommended for motor vehicles. All except &#x60;fastest&#x60; require &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to fastest)
     * @param heading Favour a heading direction for a certain point. Specify either one heading for the start point or as many as there are points. In this case headings are associated by their order to the specific points. Headings are given as north based clockwise angle between 0 and 360 degree. This parameter also influences the tour generated with &#x60;algorithm&#x3D;round_trip&#x60; and forces the initial direction.  Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional)
     * @param headingPenalty Time penalty in seconds for not obeying a specified heading. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to 120)
     * @param passThrough If &#x60;true&#x60;, u-turns are avoided at via-points with regard to the &#x60;heading_penalty&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to false)
     * @param blockArea Block road access by specifying a point close to the road segment to be blocked, with the format &#x60;lat,lon&#x60;. You can also block all road segments crossing a geometric shape. Specify a circle using the format &#x60;lat,lon,radius&#x60;, or a polygon using the format &#x60;lat1,lon1,lat2,lon2,...,latN,lonN&#x60;. You can specify several shapes, separating them with &#x60;;&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional)
     * @param avoid Specify which road classes and environments you would like to avoid.  Possible values are &#x60;motorway&#x60;, &#x60;steps&#x60;, &#x60;track&#x60;, &#x60;toll&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60; and &#x60;bridge&#x60;. Separate several values with &#x60;;&#x60;. Obviously not all the values make sense for all vehicle profiles e.g. &#x60;bike&#x60; is already forbidden on a &#x60;motorway&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional)
     * @param algorithm Rather than looking for the shortest or fastest path, this parameter lets you solve two different problems related to routing: With &#x60;alternative_route&#x60;, we give you not one but several routes that are close to optimal, but not too similar to each other.  With &#x60;round_trip&#x60;, the route will get you back to where you started. This is meant for fun (think of a bike trip), so we will add some randomness. The &#x60;round_trip&#x60; option requires &#x60;ch.disable&#x3D;true&#x60;. You can control both of these features with additional parameters, see below.   (optional)
     * @param roundTripDistance If &#x60;algorithm&#x3D;round_trip&#x60;, this parameter configures approximative length of the resulting round trip. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to 10000)
     * @param roundTripSeed If &#x60;algorithm&#x3D;round_trip&#x60;, this sets the random seed. Change this to get a different tour for each value.  (optional)
     * @param alternativeRouteMaxPaths If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the number of maximum paths which should be calculated. Increasing can lead to worse alternatives.  (optional, default to 2)
     * @param alternativeRouteMaxWeightFactor If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the factor by which the alternatives routes can be longer than the optimal route. Increasing can lead to worse alternatives.  (optional, default to 1.4)
     * @param alternativeRouteMaxShareFactor If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter specifies how similar an alternative route can be to the optimal route. Increasing can lead to worse alternatives.  (optional, default to 0.6)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Routing Result </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Your request is not valid. For example, you specified too few or too many points. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 401 </td><td> Authentication necessary </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 429 </td><td> API limit reached. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal server error. We get notified automatically and fix this asap. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 501 </td><td> Only a special list of vehicles is supported. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getRouteCall(List<String> point, List<String> pointHint, List<String> snapPrevention, VehicleProfileId vehicle, List<String> curbside, Boolean turnCosts, String locale, Boolean elevation, List<String> details, String optimize, Boolean instructions, Boolean calcPoints, Boolean debug, Boolean pointsEncoded, Boolean chDisable, String weighting, List<Integer> heading, Integer headingPenalty, Boolean passThrough, String blockArea, String avoid, String algorithm, Integer roundTripDistance, Long roundTripSeed, Integer alternativeRouteMaxPaths, BigDecimal alternativeRouteMaxWeightFactor, BigDecimal alternativeRouteMaxShareFactor, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/route";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (point != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "point", point));
        }

        if (pointHint != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "point_hint", pointHint));
        }

        if (snapPrevention != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "snap_prevention", snapPrevention));
        }

        if (vehicle != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("vehicle", vehicle));
        }

        if (curbside != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "curbside", curbside));
        }

        if (turnCosts != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("turn_costs", turnCosts));
        }

        if (locale != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("locale", locale));
        }

        if (elevation != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("elevation", elevation));
        }

        if (details != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "details", details));
        }

        if (optimize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("optimize", optimize));
        }

        if (instructions != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("instructions", instructions));
        }

        if (calcPoints != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("calc_points", calcPoints));
        }

        if (debug != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("debug", debug));
        }

        if (pointsEncoded != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("points_encoded", pointsEncoded));
        }

        if (chDisable != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("ch.disable", chDisable));
        }

        if (weighting != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("weighting", weighting));
        }

        if (heading != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "heading", heading));
        }

        if (headingPenalty != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("heading_penalty", headingPenalty));
        }

        if (passThrough != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("pass_through", passThrough));
        }

        if (blockArea != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("block_area", blockArea));
        }

        if (avoid != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("avoid", avoid));
        }

        if (algorithm != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("algorithm", algorithm));
        }

        if (roundTripDistance != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("round_trip.distance", roundTripDistance));
        }

        if (roundTripSeed != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("round_trip.seed", roundTripSeed));
        }

        if (alternativeRouteMaxPaths != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("alternative_route.max_paths", alternativeRouteMaxPaths));
        }

        if (alternativeRouteMaxWeightFactor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("alternative_route.max_weight_factor", alternativeRouteMaxWeightFactor));
        }

        if (alternativeRouteMaxShareFactor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("alternative_route.max_share_factor", alternativeRouteMaxShareFactor));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "api_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getRouteValidateBeforeCall(List<String> point, List<String> pointHint, List<String> snapPrevention, VehicleProfileId vehicle, List<String> curbside, Boolean turnCosts, String locale, Boolean elevation, List<String> details, String optimize, Boolean instructions, Boolean calcPoints, Boolean debug, Boolean pointsEncoded, Boolean chDisable, String weighting, List<Integer> heading, Integer headingPenalty, Boolean passThrough, String blockArea, String avoid, String algorithm, Integer roundTripDistance, Long roundTripSeed, Integer alternativeRouteMaxPaths, BigDecimal alternativeRouteMaxWeightFactor, BigDecimal alternativeRouteMaxShareFactor, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'point' is set
        if (point == null) {
            throw new ApiException("Missing the required parameter 'point' when calling getRoute(Async)");
        }

        return getRouteCall(point, pointHint, snapPrevention, vehicle, curbside, turnCosts, locale, elevation, details, optimize, instructions, calcPoints, debug, pointsEncoded, chDisable, weighting, heading, headingPenalty, passThrough, blockArea, avoid, algorithm, roundTripDistance, roundTripSeed, alternativeRouteMaxPaths, alternativeRouteMaxWeightFactor, alternativeRouteMaxShareFactor, _callback);

    }

    /**
     * GET Route Endpoint
     * The GET request is the most simple one: just specify the parameter in the URL and you are done. Can be tried directly in every browser. 
     * @param point The points for which the route should be calculated. Format: &#x60;[latitude,longitude]&#x60;. Specify at least an origin and a destination. Via points are possible. The maximum number depends on your plan.  (required)
     * @param pointHint The &#x60;point_hint&#x60; is typically a road name to which the associated &#x60;point&#x60; parameter should be snapped to. Specify no &#x60;point_hint&#x60; parameter or the same number as you have &#x60;point&#x60; parameters.  (optional)
     * @param snapPrevention Optional parameter to avoid snapping to a certain road class or road environment. Currently supported values are &#x60;motorway&#x60;, &#x60;trunk&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60;, &#x60;bridge&#x60; and &#x60;ford&#x60;. Multiple values are specified like &#x60;snap_prevention&#x3D;ferry&amp;snap_prevention&#x3D;motorway&#x60;.  (optional)
     * @param vehicle The vehicle profile for which the route should be calculated.  (optional, default to car)
     * @param curbside Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap.  (optional)
     * @param turnCosts Specifies if turn restrictions should be considered. Enabling this option increases the route computation time. Only supported for motor vehicles and OpenStreetMap.  (optional, default to false)
     * @param locale The locale of the resulting turn instructions. E.g. &#x60;pt_PT&#x60; for Portuguese or &#x60;de&#x60; for German.  (optional, default to en)
     * @param elevation If &#x60;true&#x60;, a third coordinate, the altitude, is included with all positions in the response. This changes the format of the &#x60;points&#x60; and &#x60;snapped_waypoints&#x60; fields of the response, in both their encodings. Unless you switch off the &#x60;points_encoded&#x60; parameter, you need special code on the client side that can handle three-dimensional coordinates. A request can fail if the vehicle profile does not support elevation. See the features object for every vehicle profile.  (optional, default to false)
     * @param details Optional parameter to retrieve path details. You can request additional details for the route: &#x60;street_name&#x60;,  &#x60;time&#x60;, &#x60;distance&#x60;, &#x60;max_speed&#x60;, &#x60;toll&#x60;, &#x60;road_class&#x60;, &#x60;road_class_link&#x60;, &#x60;road_access&#x60;, &#x60;road_environment&#x60;, &#x60;lanes&#x60;, and &#x60;surface&#x60;. Read more about the usage of path details [here](https://discuss.graphhopper.com/t/2539).  (optional)
     * @param optimize Normally, the calculated route will visit the points in the order you specified them. If you have more than two points, you can set this parameter to &#x60;\&quot;true\&quot;&#x60; and the points may be re-ordered to minimize the total travel time. Keep in mind that the limits on the number of locations of the Route Optimization API applies, and the request costs more credits.  (optional, default to false)
     * @param instructions If instructions should be calculated and returned  (optional, default to true)
     * @param calcPoints If the points for the route should be calculated at all.  (optional, default to true)
     * @param debug If &#x60;true&#x60;, the output will be formatted.  (optional, default to false)
     * @param pointsEncoded Allows changing the encoding of location data in the response. The default is polyline encoding, which is compact but requires special client code to unpack. (We provide it in our JavaScript client library!) Set this parameter to &#x60;false&#x60; to switch the encoding to simple coordinate pairs like &#x60;[lon,lat]&#x60;, or &#x60;[lon,lat,elevation]&#x60;. See the description of the response format for more information.  (optional, default to true)
     * @param chDisable Use this parameter in combination with one or more parameters from below.  (optional, default to false)
     * @param weighting Determines the way the \&quot;best\&quot; route is calculated. Besides &#x60;fastest&#x60; you can use &#x60;short_fastest&#x60; which finds a reasonable balance between the distance influence (&#x60;shortest&#x60;) and the time (&#x60;fastest&#x60;). You could also use &#x60;shortest&#x60; but is deprecated and not recommended for motor vehicles. All except &#x60;fastest&#x60; require &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to fastest)
     * @param heading Favour a heading direction for a certain point. Specify either one heading for the start point or as many as there are points. In this case headings are associated by their order to the specific points. Headings are given as north based clockwise angle between 0 and 360 degree. This parameter also influences the tour generated with &#x60;algorithm&#x3D;round_trip&#x60; and forces the initial direction.  Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional)
     * @param headingPenalty Time penalty in seconds for not obeying a specified heading. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to 120)
     * @param passThrough If &#x60;true&#x60;, u-turns are avoided at via-points with regard to the &#x60;heading_penalty&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to false)
     * @param blockArea Block road access by specifying a point close to the road segment to be blocked, with the format &#x60;lat,lon&#x60;. You can also block all road segments crossing a geometric shape. Specify a circle using the format &#x60;lat,lon,radius&#x60;, or a polygon using the format &#x60;lat1,lon1,lat2,lon2,...,latN,lonN&#x60;. You can specify several shapes, separating them with &#x60;;&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional)
     * @param avoid Specify which road classes and environments you would like to avoid.  Possible values are &#x60;motorway&#x60;, &#x60;steps&#x60;, &#x60;track&#x60;, &#x60;toll&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60; and &#x60;bridge&#x60;. Separate several values with &#x60;;&#x60;. Obviously not all the values make sense for all vehicle profiles e.g. &#x60;bike&#x60; is already forbidden on a &#x60;motorway&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional)
     * @param algorithm Rather than looking for the shortest or fastest path, this parameter lets you solve two different problems related to routing: With &#x60;alternative_route&#x60;, we give you not one but several routes that are close to optimal, but not too similar to each other.  With &#x60;round_trip&#x60;, the route will get you back to where you started. This is meant for fun (think of a bike trip), so we will add some randomness. The &#x60;round_trip&#x60; option requires &#x60;ch.disable&#x3D;true&#x60;. You can control both of these features with additional parameters, see below.   (optional)
     * @param roundTripDistance If &#x60;algorithm&#x3D;round_trip&#x60;, this parameter configures approximative length of the resulting round trip. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to 10000)
     * @param roundTripSeed If &#x60;algorithm&#x3D;round_trip&#x60;, this sets the random seed. Change this to get a different tour for each value.  (optional)
     * @param alternativeRouteMaxPaths If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the number of maximum paths which should be calculated. Increasing can lead to worse alternatives.  (optional, default to 2)
     * @param alternativeRouteMaxWeightFactor If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the factor by which the alternatives routes can be longer than the optimal route. Increasing can lead to worse alternatives.  (optional, default to 1.4)
     * @param alternativeRouteMaxShareFactor If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter specifies how similar an alternative route can be to the optimal route. Increasing can lead to worse alternatives.  (optional, default to 0.6)
     * @return RouteResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Routing Result </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Your request is not valid. For example, you specified too few or too many points. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 401 </td><td> Authentication necessary </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 429 </td><td> API limit reached. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal server error. We get notified automatically and fix this asap. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 501 </td><td> Only a special list of vehicles is supported. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
     </table>
     */
    public RouteResponse getRoute(List<String> point, List<String> pointHint, List<String> snapPrevention, VehicleProfileId vehicle, List<String> curbside, Boolean turnCosts, String locale, Boolean elevation, List<String> details, String optimize, Boolean instructions, Boolean calcPoints, Boolean debug, Boolean pointsEncoded, Boolean chDisable, String weighting, List<Integer> heading, Integer headingPenalty, Boolean passThrough, String blockArea, String avoid, String algorithm, Integer roundTripDistance, Long roundTripSeed, Integer alternativeRouteMaxPaths, BigDecimal alternativeRouteMaxWeightFactor, BigDecimal alternativeRouteMaxShareFactor) throws ApiException {
        ApiResponse<RouteResponse> localVarResp = getRouteWithHttpInfo(point, pointHint, snapPrevention, vehicle, curbside, turnCosts, locale, elevation, details, optimize, instructions, calcPoints, debug, pointsEncoded, chDisable, weighting, heading, headingPenalty, passThrough, blockArea, avoid, algorithm, roundTripDistance, roundTripSeed, alternativeRouteMaxPaths, alternativeRouteMaxWeightFactor, alternativeRouteMaxShareFactor);
        return localVarResp.getData();
    }

    /**
     * GET Route Endpoint
     * The GET request is the most simple one: just specify the parameter in the URL and you are done. Can be tried directly in every browser. 
     * @param point The points for which the route should be calculated. Format: &#x60;[latitude,longitude]&#x60;. Specify at least an origin and a destination. Via points are possible. The maximum number depends on your plan.  (required)
     * @param pointHint The &#x60;point_hint&#x60; is typically a road name to which the associated &#x60;point&#x60; parameter should be snapped to. Specify no &#x60;point_hint&#x60; parameter or the same number as you have &#x60;point&#x60; parameters.  (optional)
     * @param snapPrevention Optional parameter to avoid snapping to a certain road class or road environment. Currently supported values are &#x60;motorway&#x60;, &#x60;trunk&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60;, &#x60;bridge&#x60; and &#x60;ford&#x60;. Multiple values are specified like &#x60;snap_prevention&#x3D;ferry&amp;snap_prevention&#x3D;motorway&#x60;.  (optional)
     * @param vehicle The vehicle profile for which the route should be calculated.  (optional, default to car)
     * @param curbside Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap.  (optional)
     * @param turnCosts Specifies if turn restrictions should be considered. Enabling this option increases the route computation time. Only supported for motor vehicles and OpenStreetMap.  (optional, default to false)
     * @param locale The locale of the resulting turn instructions. E.g. &#x60;pt_PT&#x60; for Portuguese or &#x60;de&#x60; for German.  (optional, default to en)
     * @param elevation If &#x60;true&#x60;, a third coordinate, the altitude, is included with all positions in the response. This changes the format of the &#x60;points&#x60; and &#x60;snapped_waypoints&#x60; fields of the response, in both their encodings. Unless you switch off the &#x60;points_encoded&#x60; parameter, you need special code on the client side that can handle three-dimensional coordinates. A request can fail if the vehicle profile does not support elevation. See the features object for every vehicle profile.  (optional, default to false)
     * @param details Optional parameter to retrieve path details. You can request additional details for the route: &#x60;street_name&#x60;,  &#x60;time&#x60;, &#x60;distance&#x60;, &#x60;max_speed&#x60;, &#x60;toll&#x60;, &#x60;road_class&#x60;, &#x60;road_class_link&#x60;, &#x60;road_access&#x60;, &#x60;road_environment&#x60;, &#x60;lanes&#x60;, and &#x60;surface&#x60;. Read more about the usage of path details [here](https://discuss.graphhopper.com/t/2539).  (optional)
     * @param optimize Normally, the calculated route will visit the points in the order you specified them. If you have more than two points, you can set this parameter to &#x60;\&quot;true\&quot;&#x60; and the points may be re-ordered to minimize the total travel time. Keep in mind that the limits on the number of locations of the Route Optimization API applies, and the request costs more credits.  (optional, default to false)
     * @param instructions If instructions should be calculated and returned  (optional, default to true)
     * @param calcPoints If the points for the route should be calculated at all.  (optional, default to true)
     * @param debug If &#x60;true&#x60;, the output will be formatted.  (optional, default to false)
     * @param pointsEncoded Allows changing the encoding of location data in the response. The default is polyline encoding, which is compact but requires special client code to unpack. (We provide it in our JavaScript client library!) Set this parameter to &#x60;false&#x60; to switch the encoding to simple coordinate pairs like &#x60;[lon,lat]&#x60;, or &#x60;[lon,lat,elevation]&#x60;. See the description of the response format for more information.  (optional, default to true)
     * @param chDisable Use this parameter in combination with one or more parameters from below.  (optional, default to false)
     * @param weighting Determines the way the \&quot;best\&quot; route is calculated. Besides &#x60;fastest&#x60; you can use &#x60;short_fastest&#x60; which finds a reasonable balance between the distance influence (&#x60;shortest&#x60;) and the time (&#x60;fastest&#x60;). You could also use &#x60;shortest&#x60; but is deprecated and not recommended for motor vehicles. All except &#x60;fastest&#x60; require &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to fastest)
     * @param heading Favour a heading direction for a certain point. Specify either one heading for the start point or as many as there are points. In this case headings are associated by their order to the specific points. Headings are given as north based clockwise angle between 0 and 360 degree. This parameter also influences the tour generated with &#x60;algorithm&#x3D;round_trip&#x60; and forces the initial direction.  Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional)
     * @param headingPenalty Time penalty in seconds for not obeying a specified heading. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to 120)
     * @param passThrough If &#x60;true&#x60;, u-turns are avoided at via-points with regard to the &#x60;heading_penalty&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to false)
     * @param blockArea Block road access by specifying a point close to the road segment to be blocked, with the format &#x60;lat,lon&#x60;. You can also block all road segments crossing a geometric shape. Specify a circle using the format &#x60;lat,lon,radius&#x60;, or a polygon using the format &#x60;lat1,lon1,lat2,lon2,...,latN,lonN&#x60;. You can specify several shapes, separating them with &#x60;;&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional)
     * @param avoid Specify which road classes and environments you would like to avoid.  Possible values are &#x60;motorway&#x60;, &#x60;steps&#x60;, &#x60;track&#x60;, &#x60;toll&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60; and &#x60;bridge&#x60;. Separate several values with &#x60;;&#x60;. Obviously not all the values make sense for all vehicle profiles e.g. &#x60;bike&#x60; is already forbidden on a &#x60;motorway&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional)
     * @param algorithm Rather than looking for the shortest or fastest path, this parameter lets you solve two different problems related to routing: With &#x60;alternative_route&#x60;, we give you not one but several routes that are close to optimal, but not too similar to each other.  With &#x60;round_trip&#x60;, the route will get you back to where you started. This is meant for fun (think of a bike trip), so we will add some randomness. The &#x60;round_trip&#x60; option requires &#x60;ch.disable&#x3D;true&#x60;. You can control both of these features with additional parameters, see below.   (optional)
     * @param roundTripDistance If &#x60;algorithm&#x3D;round_trip&#x60;, this parameter configures approximative length of the resulting round trip. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to 10000)
     * @param roundTripSeed If &#x60;algorithm&#x3D;round_trip&#x60;, this sets the random seed. Change this to get a different tour for each value.  (optional)
     * @param alternativeRouteMaxPaths If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the number of maximum paths which should be calculated. Increasing can lead to worse alternatives.  (optional, default to 2)
     * @param alternativeRouteMaxWeightFactor If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the factor by which the alternatives routes can be longer than the optimal route. Increasing can lead to worse alternatives.  (optional, default to 1.4)
     * @param alternativeRouteMaxShareFactor If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter specifies how similar an alternative route can be to the optimal route. Increasing can lead to worse alternatives.  (optional, default to 0.6)
     * @return ApiResponse&lt;RouteResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Routing Result </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Your request is not valid. For example, you specified too few or too many points. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 401 </td><td> Authentication necessary </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 429 </td><td> API limit reached. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal server error. We get notified automatically and fix this asap. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 501 </td><td> Only a special list of vehicles is supported. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
     </table>
     */
    public ApiResponse<RouteResponse> getRouteWithHttpInfo(List<String> point, List<String> pointHint, List<String> snapPrevention, VehicleProfileId vehicle, List<String> curbside, Boolean turnCosts, String locale, Boolean elevation, List<String> details, String optimize, Boolean instructions, Boolean calcPoints, Boolean debug, Boolean pointsEncoded, Boolean chDisable, String weighting, List<Integer> heading, Integer headingPenalty, Boolean passThrough, String blockArea, String avoid, String algorithm, Integer roundTripDistance, Long roundTripSeed, Integer alternativeRouteMaxPaths, BigDecimal alternativeRouteMaxWeightFactor, BigDecimal alternativeRouteMaxShareFactor) throws ApiException {
        okhttp3.Call localVarCall = getRouteValidateBeforeCall(point, pointHint, snapPrevention, vehicle, curbside, turnCosts, locale, elevation, details, optimize, instructions, calcPoints, debug, pointsEncoded, chDisable, weighting, heading, headingPenalty, passThrough, blockArea, avoid, algorithm, roundTripDistance, roundTripSeed, alternativeRouteMaxPaths, alternativeRouteMaxWeightFactor, alternativeRouteMaxShareFactor, null);
        Type localVarReturnType = new TypeToken<RouteResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * GET Route Endpoint (asynchronously)
     * The GET request is the most simple one: just specify the parameter in the URL and you are done. Can be tried directly in every browser. 
     * @param point The points for which the route should be calculated. Format: &#x60;[latitude,longitude]&#x60;. Specify at least an origin and a destination. Via points are possible. The maximum number depends on your plan.  (required)
     * @param pointHint The &#x60;point_hint&#x60; is typically a road name to which the associated &#x60;point&#x60; parameter should be snapped to. Specify no &#x60;point_hint&#x60; parameter or the same number as you have &#x60;point&#x60; parameters.  (optional)
     * @param snapPrevention Optional parameter to avoid snapping to a certain road class or road environment. Currently supported values are &#x60;motorway&#x60;, &#x60;trunk&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60;, &#x60;bridge&#x60; and &#x60;ford&#x60;. Multiple values are specified like &#x60;snap_prevention&#x3D;ferry&amp;snap_prevention&#x3D;motorway&#x60;.  (optional)
     * @param vehicle The vehicle profile for which the route should be calculated.  (optional, default to car)
     * @param curbside Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap.  (optional)
     * @param turnCosts Specifies if turn restrictions should be considered. Enabling this option increases the route computation time. Only supported for motor vehicles and OpenStreetMap.  (optional, default to false)
     * @param locale The locale of the resulting turn instructions. E.g. &#x60;pt_PT&#x60; for Portuguese or &#x60;de&#x60; for German.  (optional, default to en)
     * @param elevation If &#x60;true&#x60;, a third coordinate, the altitude, is included with all positions in the response. This changes the format of the &#x60;points&#x60; and &#x60;snapped_waypoints&#x60; fields of the response, in both their encodings. Unless you switch off the &#x60;points_encoded&#x60; parameter, you need special code on the client side that can handle three-dimensional coordinates. A request can fail if the vehicle profile does not support elevation. See the features object for every vehicle profile.  (optional, default to false)
     * @param details Optional parameter to retrieve path details. You can request additional details for the route: &#x60;street_name&#x60;,  &#x60;time&#x60;, &#x60;distance&#x60;, &#x60;max_speed&#x60;, &#x60;toll&#x60;, &#x60;road_class&#x60;, &#x60;road_class_link&#x60;, &#x60;road_access&#x60;, &#x60;road_environment&#x60;, &#x60;lanes&#x60;, and &#x60;surface&#x60;. Read more about the usage of path details [here](https://discuss.graphhopper.com/t/2539).  (optional)
     * @param optimize Normally, the calculated route will visit the points in the order you specified them. If you have more than two points, you can set this parameter to &#x60;\&quot;true\&quot;&#x60; and the points may be re-ordered to minimize the total travel time. Keep in mind that the limits on the number of locations of the Route Optimization API applies, and the request costs more credits.  (optional, default to false)
     * @param instructions If instructions should be calculated and returned  (optional, default to true)
     * @param calcPoints If the points for the route should be calculated at all.  (optional, default to true)
     * @param debug If &#x60;true&#x60;, the output will be formatted.  (optional, default to false)
     * @param pointsEncoded Allows changing the encoding of location data in the response. The default is polyline encoding, which is compact but requires special client code to unpack. (We provide it in our JavaScript client library!) Set this parameter to &#x60;false&#x60; to switch the encoding to simple coordinate pairs like &#x60;[lon,lat]&#x60;, or &#x60;[lon,lat,elevation]&#x60;. See the description of the response format for more information.  (optional, default to true)
     * @param chDisable Use this parameter in combination with one or more parameters from below.  (optional, default to false)
     * @param weighting Determines the way the \&quot;best\&quot; route is calculated. Besides &#x60;fastest&#x60; you can use &#x60;short_fastest&#x60; which finds a reasonable balance between the distance influence (&#x60;shortest&#x60;) and the time (&#x60;fastest&#x60;). You could also use &#x60;shortest&#x60; but is deprecated and not recommended for motor vehicles. All except &#x60;fastest&#x60; require &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to fastest)
     * @param heading Favour a heading direction for a certain point. Specify either one heading for the start point or as many as there are points. In this case headings are associated by their order to the specific points. Headings are given as north based clockwise angle between 0 and 360 degree. This parameter also influences the tour generated with &#x60;algorithm&#x3D;round_trip&#x60; and forces the initial direction.  Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional)
     * @param headingPenalty Time penalty in seconds for not obeying a specified heading. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to 120)
     * @param passThrough If &#x60;true&#x60;, u-turns are avoided at via-points with regard to the &#x60;heading_penalty&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to false)
     * @param blockArea Block road access by specifying a point close to the road segment to be blocked, with the format &#x60;lat,lon&#x60;. You can also block all road segments crossing a geometric shape. Specify a circle using the format &#x60;lat,lon,radius&#x60;, or a polygon using the format &#x60;lat1,lon1,lat2,lon2,...,latN,lonN&#x60;. You can specify several shapes, separating them with &#x60;;&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional)
     * @param avoid Specify which road classes and environments you would like to avoid.  Possible values are &#x60;motorway&#x60;, &#x60;steps&#x60;, &#x60;track&#x60;, &#x60;toll&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60; and &#x60;bridge&#x60;. Separate several values with &#x60;;&#x60;. Obviously not all the values make sense for all vehicle profiles e.g. &#x60;bike&#x60; is already forbidden on a &#x60;motorway&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional)
     * @param algorithm Rather than looking for the shortest or fastest path, this parameter lets you solve two different problems related to routing: With &#x60;alternative_route&#x60;, we give you not one but several routes that are close to optimal, but not too similar to each other.  With &#x60;round_trip&#x60;, the route will get you back to where you started. This is meant for fun (think of a bike trip), so we will add some randomness. The &#x60;round_trip&#x60; option requires &#x60;ch.disable&#x3D;true&#x60;. You can control both of these features with additional parameters, see below.   (optional)
     * @param roundTripDistance If &#x60;algorithm&#x3D;round_trip&#x60;, this parameter configures approximative length of the resulting round trip. Requires &#x60;ch.disable&#x3D;true&#x60;.  (optional, default to 10000)
     * @param roundTripSeed If &#x60;algorithm&#x3D;round_trip&#x60;, this sets the random seed. Change this to get a different tour for each value.  (optional)
     * @param alternativeRouteMaxPaths If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the number of maximum paths which should be calculated. Increasing can lead to worse alternatives.  (optional, default to 2)
     * @param alternativeRouteMaxWeightFactor If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the factor by which the alternatives routes can be longer than the optimal route. Increasing can lead to worse alternatives.  (optional, default to 1.4)
     * @param alternativeRouteMaxShareFactor If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter specifies how similar an alternative route can be to the optimal route. Increasing can lead to worse alternatives.  (optional, default to 0.6)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Routing Result </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Your request is not valid. For example, you specified too few or too many points. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 401 </td><td> Authentication necessary </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 429 </td><td> API limit reached. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal server error. We get notified automatically and fix this asap. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 501 </td><td> Only a special list of vehicles is supported. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getRouteAsync(List<String> point, List<String> pointHint, List<String> snapPrevention, VehicleProfileId vehicle, List<String> curbside, Boolean turnCosts, String locale, Boolean elevation, List<String> details, String optimize, Boolean instructions, Boolean calcPoints, Boolean debug, Boolean pointsEncoded, Boolean chDisable, String weighting, List<Integer> heading, Integer headingPenalty, Boolean passThrough, String blockArea, String avoid, String algorithm, Integer roundTripDistance, Long roundTripSeed, Integer alternativeRouteMaxPaths, BigDecimal alternativeRouteMaxWeightFactor, BigDecimal alternativeRouteMaxShareFactor, final ApiCallback<RouteResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getRouteValidateBeforeCall(point, pointHint, snapPrevention, vehicle, curbside, turnCosts, locale, elevation, details, optimize, instructions, calcPoints, debug, pointsEncoded, chDisable, weighting, heading, headingPenalty, passThrough, blockArea, avoid, algorithm, roundTripDistance, roundTripSeed, alternativeRouteMaxPaths, alternativeRouteMaxWeightFactor, alternativeRouteMaxShareFactor, _callback);
        Type localVarReturnType = new TypeToken<RouteResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postRoute
     * @param routeRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Routing Result </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Your request is not valid. For example, you specified too few or too many points. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 401 </td><td> Authentication necessary </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 429 </td><td> API limit reached. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal server error. We get notified automatically and fix this asap. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 501 </td><td> Only a special list of vehicles is supported. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call postRouteCall(RouteRequest routeRequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = routeRequest;

        // create path and map variables
        String localVarPath = "/route";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "api_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postRouteValidateBeforeCall(RouteRequest routeRequest, final ApiCallback _callback) throws ApiException {
        return postRouteCall(routeRequest, _callback);

    }

    /**
     * POST Route Endpoint
     * Please see the [GET endpoint](#operation/getRoute) for a simpler method on how to get started. If you are familiar with POST requests and JSON then do not hesitate to continue here.  Especially when you use many locations you should get familiar with this POST endpoint as the GET endpoint has an URL length limitation. Additionally the request of this POST endpoint can be compressed and can slightly speed up the request.  To do a request you send JSON data. Both request scenarios GET and POST are identical except that all singular parameter names are named as their plural for a POST request. The effected parameters are: &#x60;points&#x60;, &#x60;point_hints&#x60; and &#x60;snap_preventions&#x60;.  **Please note that in opposite to the GET endpoint, points are specified in the order of &#x60;longitude, latitude&#x60;**.  For example &#x60;point&#x3D;10,11&amp;point&#x3D;20,22&#x60; will be converted to the &#x60;points&#x60; array (plural): &#x60;&#x60;&#x60;json { \&quot;points\&quot;: [[11,10], [22,20]] } &#x60;&#x60;&#x60; Note again that also the order changes from &#x60;[latitude,longitude]&#x60; to &#x60;[longitude,latitude]&#x60; similar to [GeoJson](http://geojson.org/geojson-spec.html#examples).  Example: &#x60;&#x60;&#x60;bash curl -X POST -H \&quot;Content-Type: application/json\&quot; \&quot;https://graphhopper.com/api/1/route?key&#x3D;[YOUR_KEY]\&quot; -d &#39;{\&quot;elevation\&quot;:false,\&quot;points\&quot;:[[-0.087891,51.534377],[-0.090637,51.467697]],\&quot;vehicle\&quot;:\&quot;car\&quot;}&#39; &#x60;&#x60;&#x60; 
     * @param routeRequest  (optional)
     * @return RouteResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Routing Result </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Your request is not valid. For example, you specified too few or too many points. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 401 </td><td> Authentication necessary </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 429 </td><td> API limit reached. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal server error. We get notified automatically and fix this asap. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 501 </td><td> Only a special list of vehicles is supported. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
     </table>
     */
    public RouteResponse postRoute(RouteRequest routeRequest) throws ApiException {
        ApiResponse<RouteResponse> localVarResp = postRouteWithHttpInfo(routeRequest);
        return localVarResp.getData();
    }

    /**
     * POST Route Endpoint
     * Please see the [GET endpoint](#operation/getRoute) for a simpler method on how to get started. If you are familiar with POST requests and JSON then do not hesitate to continue here.  Especially when you use many locations you should get familiar with this POST endpoint as the GET endpoint has an URL length limitation. Additionally the request of this POST endpoint can be compressed and can slightly speed up the request.  To do a request you send JSON data. Both request scenarios GET and POST are identical except that all singular parameter names are named as their plural for a POST request. The effected parameters are: &#x60;points&#x60;, &#x60;point_hints&#x60; and &#x60;snap_preventions&#x60;.  **Please note that in opposite to the GET endpoint, points are specified in the order of &#x60;longitude, latitude&#x60;**.  For example &#x60;point&#x3D;10,11&amp;point&#x3D;20,22&#x60; will be converted to the &#x60;points&#x60; array (plural): &#x60;&#x60;&#x60;json { \&quot;points\&quot;: [[11,10], [22,20]] } &#x60;&#x60;&#x60; Note again that also the order changes from &#x60;[latitude,longitude]&#x60; to &#x60;[longitude,latitude]&#x60; similar to [GeoJson](http://geojson.org/geojson-spec.html#examples).  Example: &#x60;&#x60;&#x60;bash curl -X POST -H \&quot;Content-Type: application/json\&quot; \&quot;https://graphhopper.com/api/1/route?key&#x3D;[YOUR_KEY]\&quot; -d &#39;{\&quot;elevation\&quot;:false,\&quot;points\&quot;:[[-0.087891,51.534377],[-0.090637,51.467697]],\&quot;vehicle\&quot;:\&quot;car\&quot;}&#39; &#x60;&#x60;&#x60; 
     * @param routeRequest  (optional)
     * @return ApiResponse&lt;RouteResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Routing Result </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Your request is not valid. For example, you specified too few or too many points. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 401 </td><td> Authentication necessary </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 429 </td><td> API limit reached. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal server error. We get notified automatically and fix this asap. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 501 </td><td> Only a special list of vehicles is supported. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
     </table>
     */
    public ApiResponse<RouteResponse> postRouteWithHttpInfo(RouteRequest routeRequest) throws ApiException {
        okhttp3.Call localVarCall = postRouteValidateBeforeCall(routeRequest, null);
        Type localVarReturnType = new TypeToken<RouteResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * POST Route Endpoint (asynchronously)
     * Please see the [GET endpoint](#operation/getRoute) for a simpler method on how to get started. If you are familiar with POST requests and JSON then do not hesitate to continue here.  Especially when you use many locations you should get familiar with this POST endpoint as the GET endpoint has an URL length limitation. Additionally the request of this POST endpoint can be compressed and can slightly speed up the request.  To do a request you send JSON data. Both request scenarios GET and POST are identical except that all singular parameter names are named as their plural for a POST request. The effected parameters are: &#x60;points&#x60;, &#x60;point_hints&#x60; and &#x60;snap_preventions&#x60;.  **Please note that in opposite to the GET endpoint, points are specified in the order of &#x60;longitude, latitude&#x60;**.  For example &#x60;point&#x3D;10,11&amp;point&#x3D;20,22&#x60; will be converted to the &#x60;points&#x60; array (plural): &#x60;&#x60;&#x60;json { \&quot;points\&quot;: [[11,10], [22,20]] } &#x60;&#x60;&#x60; Note again that also the order changes from &#x60;[latitude,longitude]&#x60; to &#x60;[longitude,latitude]&#x60; similar to [GeoJson](http://geojson.org/geojson-spec.html#examples).  Example: &#x60;&#x60;&#x60;bash curl -X POST -H \&quot;Content-Type: application/json\&quot; \&quot;https://graphhopper.com/api/1/route?key&#x3D;[YOUR_KEY]\&quot; -d &#39;{\&quot;elevation\&quot;:false,\&quot;points\&quot;:[[-0.087891,51.534377],[-0.090637,51.467697]],\&quot;vehicle\&quot;:\&quot;car\&quot;}&#39; &#x60;&#x60;&#x60; 
     * @param routeRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Routing Result </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Your request is not valid. For example, you specified too few or too many points. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 401 </td><td> Authentication necessary </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 429 </td><td> API limit reached. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal server error. We get notified automatically and fix this asap. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 501 </td><td> Only a special list of vehicles is supported. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call postRouteAsync(RouteRequest routeRequest, final ApiCallback<RouteResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = postRouteValidateBeforeCall(routeRequest, _callback);
        Type localVarReturnType = new TypeToken<RouteResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for routeInfoGet
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Coverage Information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call routeInfoGetCall(final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/route/info";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "api_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call routeInfoGetValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return routeInfoGetCall(_callback);

    }

    /**
     * Coverage information
     * Use this to find out details about the supported vehicle profiles and features, or if you just need to ping the server. 
     * @return InfoResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Coverage Information </td><td>  -  </td></tr>
     </table>
     */
    public InfoResponse routeInfoGet() throws ApiException {
        ApiResponse<InfoResponse> localVarResp = routeInfoGetWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Coverage information
     * Use this to find out details about the supported vehicle profiles and features, or if you just need to ping the server. 
     * @return ApiResponse&lt;InfoResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Coverage Information </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<InfoResponse> routeInfoGetWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = routeInfoGetValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<InfoResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Coverage information (asynchronously)
     * Use this to find out details about the supported vehicle profiles and features, or if you just need to ping the server. 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Coverage Information </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call routeInfoGetAsync(final ApiCallback<InfoResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = routeInfoGetValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<InfoResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
