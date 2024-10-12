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


import org.openapitools.client.model.BadRequest;
import org.openapitools.client.model.ClusterRequest;
import org.openapitools.client.model.ClusterResponse;
import org.openapitools.client.model.GetClusterSolution404Response;
import org.openapitools.client.model.InternalErrorMessage;
import org.openapitools.client.model.JobId;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ClusterApiApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ClusterApiApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ClusterApiApi(ApiClient apiClient) {
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
     * Build call for asyncClusteringProblem
     * @param clusterRequest Request object that contains the problem to be solved (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A jobId you can use to retrieve your solution from the server - see solution endpoint. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Error occurred when reading client request. Request is invalid. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Error occurred on server side. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call asyncClusteringProblemCall(ClusterRequest clusterRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = clusterRequest;

        // create path and map variables
        String localVarPath = "/cluster/calculate";

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
    private okhttp3.Call asyncClusteringProblemValidateBeforeCall(ClusterRequest clusterRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterRequest' is set
        if (clusterRequest == null) {
            throw new ApiException("Missing the required parameter 'clusterRequest' when calling asyncClusteringProblem(Async)");
        }

        return asyncClusteringProblemCall(clusterRequest, _callback);

    }

    /**
     * Batch Cluster Endpoint
     *  Prefer the [synchronous endpoint](#operation/solveClusteringProblem) and use this Batch Cluster endpoint for long running problems only. The work flow is asynchronous:  - send a POST request towards &#x60;https://graphhopper.com/api/1/cluster/calculate?key&#x3D;&lt;your_key&gt;&#x60; and fetch the job_id. - poll the solution every 500ms until it gives &#x60;status&#x3D;finished&#x60;. Do this with a GET request   towards &#x60;https://graphhopper.com/api/1/cluster/solution/&lt;job_id&gt;?key&#x3D;&lt;your_key&gt;&#x60;. 
     * @param clusterRequest Request object that contains the problem to be solved (required)
     * @return JobId
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A jobId you can use to retrieve your solution from the server - see solution endpoint. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Error occurred when reading client request. Request is invalid. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Error occurred on server side. </td><td>  -  </td></tr>
     </table>
     */
    public JobId asyncClusteringProblem(ClusterRequest clusterRequest) throws ApiException {
        ApiResponse<JobId> localVarResp = asyncClusteringProblemWithHttpInfo(clusterRequest);
        return localVarResp.getData();
    }

    /**
     * Batch Cluster Endpoint
     *  Prefer the [synchronous endpoint](#operation/solveClusteringProblem) and use this Batch Cluster endpoint for long running problems only. The work flow is asynchronous:  - send a POST request towards &#x60;https://graphhopper.com/api/1/cluster/calculate?key&#x3D;&lt;your_key&gt;&#x60; and fetch the job_id. - poll the solution every 500ms until it gives &#x60;status&#x3D;finished&#x60;. Do this with a GET request   towards &#x60;https://graphhopper.com/api/1/cluster/solution/&lt;job_id&gt;?key&#x3D;&lt;your_key&gt;&#x60;. 
     * @param clusterRequest Request object that contains the problem to be solved (required)
     * @return ApiResponse&lt;JobId&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A jobId you can use to retrieve your solution from the server - see solution endpoint. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Error occurred when reading client request. Request is invalid. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Error occurred on server side. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<JobId> asyncClusteringProblemWithHttpInfo(ClusterRequest clusterRequest) throws ApiException {
        okhttp3.Call localVarCall = asyncClusteringProblemValidateBeforeCall(clusterRequest, null);
        Type localVarReturnType = new TypeToken<JobId>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Batch Cluster Endpoint (asynchronously)
     *  Prefer the [synchronous endpoint](#operation/solveClusteringProblem) and use this Batch Cluster endpoint for long running problems only. The work flow is asynchronous:  - send a POST request towards &#x60;https://graphhopper.com/api/1/cluster/calculate?key&#x3D;&lt;your_key&gt;&#x60; and fetch the job_id. - poll the solution every 500ms until it gives &#x60;status&#x3D;finished&#x60;. Do this with a GET request   towards &#x60;https://graphhopper.com/api/1/cluster/solution/&lt;job_id&gt;?key&#x3D;&lt;your_key&gt;&#x60;. 
     * @param clusterRequest Request object that contains the problem to be solved (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A jobId you can use to retrieve your solution from the server - see solution endpoint. </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Error occurred when reading client request. Request is invalid. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Error occurred on server side. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call asyncClusteringProblemAsync(ClusterRequest clusterRequest, final ApiCallback<JobId> _callback) throws ApiException {

        okhttp3.Call localVarCall = asyncClusteringProblemValidateBeforeCall(clusterRequest, _callback);
        Type localVarReturnType = new TypeToken<JobId>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getClusterSolution
     * @param jobId Request solution with jobId (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A response containing the solution </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Error occurred on client side such as invalid input. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Requested solution could not be found. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Error occurred on server side. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClusterSolutionCall(String jobId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/cluster/solution/{jobId}"
            .replace("{" + "jobId" + "}", localVarApiClient.escapeString(jobId.toString()));

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
    private okhttp3.Call getClusterSolutionValidateBeforeCall(String jobId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'jobId' is set
        if (jobId == null) {
            throw new ApiException("Missing the required parameter 'jobId' when calling getClusterSolution(Async)");
        }

        return getClusterSolutionCall(jobId, _callback);

    }

    /**
     * GET Batch Solution Endpoint
     * This endpoint returns the solution of the clustering problems submitted to the [Batch Cluster endpoint](#operation/asyncClusteringProblem). You can fetch it with the job_id, you have been sent. 
     * @param jobId Request solution with jobId (required)
     * @return ClusterResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A response containing the solution </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Error occurred on client side such as invalid input. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Requested solution could not be found. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Error occurred on server side. </td><td>  -  </td></tr>
     </table>
     */
    public ClusterResponse getClusterSolution(String jobId) throws ApiException {
        ApiResponse<ClusterResponse> localVarResp = getClusterSolutionWithHttpInfo(jobId);
        return localVarResp.getData();
    }

    /**
     * GET Batch Solution Endpoint
     * This endpoint returns the solution of the clustering problems submitted to the [Batch Cluster endpoint](#operation/asyncClusteringProblem). You can fetch it with the job_id, you have been sent. 
     * @param jobId Request solution with jobId (required)
     * @return ApiResponse&lt;ClusterResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A response containing the solution </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Error occurred on client side such as invalid input. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Requested solution could not be found. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Error occurred on server side. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClusterResponse> getClusterSolutionWithHttpInfo(String jobId) throws ApiException {
        okhttp3.Call localVarCall = getClusterSolutionValidateBeforeCall(jobId, null);
        Type localVarReturnType = new TypeToken<ClusterResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * GET Batch Solution Endpoint (asynchronously)
     * This endpoint returns the solution of the clustering problems submitted to the [Batch Cluster endpoint](#operation/asyncClusteringProblem). You can fetch it with the job_id, you have been sent. 
     * @param jobId Request solution with jobId (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A response containing the solution </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Error occurred on client side such as invalid input. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Requested solution could not be found. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Error occurred on server side. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getClusterSolutionAsync(String jobId, final ApiCallback<ClusterResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getClusterSolutionValidateBeforeCall(jobId, _callback);
        Type localVarReturnType = new TypeToken<ClusterResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for solveClusteringProblem
     * @param clusterRequest Request object that contains the problem to be solved (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A response containing the solution </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Error occurred when reading the request. Request is invalid. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Error occurred on server side. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call solveClusteringProblemCall(ClusterRequest clusterRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = clusterRequest;

        // create path and map variables
        String localVarPath = "/cluster";

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
    private okhttp3.Call solveClusteringProblemValidateBeforeCall(ClusterRequest clusterRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'clusterRequest' is set
        if (clusterRequest == null) {
            throw new ApiException("Missing the required parameter 'clusterRequest' when calling solveClusteringProblem(Async)");
        }

        return solveClusteringProblemCall(clusterRequest, _callback);

    }

    /**
     * POST Cluster Endpoint
     *  The Cluster endpoint is used with a POST request towards &#x60;https://graphhopper.com/api/1/cluster?key&#x3D;&lt;your_key&gt;&#x60;. The solution will be provided in the JSON response. Please note that for problems that take longer than 10 seconds a bad request error is returned. In this case please use the asynchronous [Batch Cluster Endpoint](#operation/asyncClusteringProblem) instead. 
     * @param clusterRequest Request object that contains the problem to be solved (required)
     * @return ClusterResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A response containing the solution </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Error occurred when reading the request. Request is invalid. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Error occurred on server side. </td><td>  -  </td></tr>
     </table>
     */
    public ClusterResponse solveClusteringProblem(ClusterRequest clusterRequest) throws ApiException {
        ApiResponse<ClusterResponse> localVarResp = solveClusteringProblemWithHttpInfo(clusterRequest);
        return localVarResp.getData();
    }

    /**
     * POST Cluster Endpoint
     *  The Cluster endpoint is used with a POST request towards &#x60;https://graphhopper.com/api/1/cluster?key&#x3D;&lt;your_key&gt;&#x60;. The solution will be provided in the JSON response. Please note that for problems that take longer than 10 seconds a bad request error is returned. In this case please use the asynchronous [Batch Cluster Endpoint](#operation/asyncClusteringProblem) instead. 
     * @param clusterRequest Request object that contains the problem to be solved (required)
     * @return ApiResponse&lt;ClusterResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A response containing the solution </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Error occurred when reading the request. Request is invalid. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Error occurred on server side. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ClusterResponse> solveClusteringProblemWithHttpInfo(ClusterRequest clusterRequest) throws ApiException {
        okhttp3.Call localVarCall = solveClusteringProblemValidateBeforeCall(clusterRequest, null);
        Type localVarReturnType = new TypeToken<ClusterResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * POST Cluster Endpoint (asynchronously)
     *  The Cluster endpoint is used with a POST request towards &#x60;https://graphhopper.com/api/1/cluster?key&#x3D;&lt;your_key&gt;&#x60;. The solution will be provided in the JSON response. Please note that for problems that take longer than 10 seconds a bad request error is returned. In this case please use the asynchronous [Batch Cluster Endpoint](#operation/asyncClusteringProblem) instead. 
     * @param clusterRequest Request object that contains the problem to be solved (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A response containing the solution </td><td>  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  </td></tr>
        <tr><td> 400 </td><td> Error occurred when reading the request. Request is invalid. </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Error occurred on server side. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call solveClusteringProblemAsync(ClusterRequest clusterRequest, final ApiCallback<ClusterResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = solveClusteringProblemValidateBeforeCall(clusterRequest, _callback);
        Type localVarReturnType = new TypeToken<ClusterResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
