/*
 * Climate FieldView Platform APIs
 * **Last Modified**: Wed Jan  4 12:47:29 UTC 2023   All endpoints are only accessible via HTTPS.  * All API endpoints are located at `https://platform.climate.com` (e.g. `https://platform.climate.com/v4/fields`).  * The authorization token endpoint is located at `https://api.climate.com/api/oauth/token`.  ## Troubleshooting  `X-Http-Request-Id` response header will be returned on every call, successful or not. If you experience an issue with our api and need to contact technical support, please supply the value of the `X-Http-Request-Id` header along with an approximate time of when the request was made.  ## Request Limits  When you’re onboarded to Climate’s API platform, your `x-api-key` is assigned a custom usage plan. Usage plans are unique to each partner and have the following key attributes:   1. Throttling information     * burstLimit: Maximum rate limit over a period ranging from 1 second to a few seconds     * rateLimit: A steady-state rate limit  2. Quota information     * Limit: The maximum number of requests that can be made in a given month  When the request rate threshold is exceeded, a `429` response code is returned. Optionally, the [`Retry-After`](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37) header may be returned:   Following are examples of rate limit errors:  1. Rate limit exceeded:  <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 32     {\"message\":\"Too Many Requests\"}  2. Quota exhausted: <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 29      {\"message\":\"Limit Exceeded\"}  ## Pagination  Pagination is performed via headers. Any request which returns a `\"results\"` array may be paginated. The following figure shows how query results are laid out with X-Limit=4 and no filter applied.  <img style=\"width:70%;height:auto;\" src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/paging.png\">  * If there are no results, a response code of `304` will be returned.  * If the response is the last set of results, a response code of `200` or `206` will be returned.  * If there are more results, a response code of `206` will be returned.  * If `X-Next-Token` is provided in the request headers but the token has expired, a response code of `409` will be returned. This is only applicable for some endpoints; see specific endpoint documentation below.  #### X-Limit  The page size can be controlled with the `X-Limit` header. Valid values are `1-100` and defaults to `100`.  #### X-Next-Token  If the results are paginated, a response header of `X-Next-Token` will be returned. Use the associated value in the subsequent request (via the `X-Next-Token` request header) to retrieve the next page. The following sequence diagram shows how to use `X-Next-Token` to fetch all the records.  <img src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/x-next-token.svg\">   ## Chunked Uploads  Uploads larger than `5MiB` (`5242880 bytes`) must be done in `5MiB` chunks (with the exception of the final chunk). Each chunk request MUST contain a `Content-Range` header specifying the portion of the upload, and a `Content-Type` header specifying binary content type (`application/octet-stream`). Range uploads must be contiguous. The maximum upload size is capped at `500MiB` (`524288000 bytes`).  ## Chunked Downloads  Downloads larger than `5MiB` (`5242880 bytes`) must be done in `1-5MiB` chunks (with the exception of the final chunk, which may be less than `1MiB`). Each chunk request MUST contain a `Range` header specifying the requested portion of the download, and an `Accept` header specifying binary and json content types  (`application/octet-stream,application/json`) or all content types (`*_/_*`).  ## Drivers  If you need drivers to process agronomic data, download the ADAPT plugin below. We only support the plugin in the Windows environment, minimum is Windows 7 SP1.  For asPlanted, asHarvested and asApplied data: * [ADAPT Plugin](https://dev.fieldview.com/drivers/ClimateADAPTPlugin_latest.exe) <br>Release notes can be found [here](https://dev.fieldview.com/drivers/adapt-release-notes.txt). <br>Download and use of the ADAPT plugin means that you agree to the EULA for use of the ADAPT plugin.  <br>Please review the [EULA](https://dev.fieldview.com/EULA/ADAPT%20Plugin%20EULA-06-19.pdf) (last updated on June 6th, 2019) before download and use of the ADAPT plugin. <br>For more information, please refer to:   * [ADAPT Resources](https://adaptframework.org/)   * [ADAPT Overview](https://aggateway.atlassian.net/wiki/spaces/ADM/overview)   * [ADAPT FAQ](https://aggateway.atlassian.net/wiki/spaces/ADM/pages/165942474/ADAPT+Frequently-Asked+Questions+FAQ)   * [ADAPT Videos](https://adaptframework.org/adapt-videos/)  ## Sample Test Data  Sample agronomic data: * [asPlanted and asHarvested data](https://dev.fieldview.com/sample-agronomic-data/Planting_Harvesting_data_04_18_2018_21_46_18.zip) * [asApplied data set 1](https://dev.fieldview.com/sample-agronomic-data/as-applied-data1.zip) * [asApplied data set 2](https://dev.fieldview.com/sample-agronomic-data/as-applied-data2.zip) <br>To upload the sample data to your account, please follow the instructions in this [link](https://support.climate.com/kt#/kA02A000000AaxzSAC/en_US).  Sample soil data: * [Sample soil data](https://dev.fieldview.com/sample-soil-data/soil-sample.xml) --- 
 *
 * The version of the OpenAPI document: 4.0.11
 * Contact: developer@climate.com
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


import org.openapitools.client.model.ApplicationActivities;
import org.openapitools.client.model.ApplicationActivityContents;
import org.openapitools.client.model.Error;
import org.openapitools.client.model.HarvestActivities;
import org.openapitools.client.model.HarvestActivityContents;
import java.time.OffsetDateTime;
import org.openapitools.client.model.PlantingActivities;
import org.openapitools.client.model.PlantingActivityContents;
import org.openapitools.client.model.ScoutingObservation;
import org.openapitools.client.model.ScoutingObservationAttachmentContents;
import org.openapitools.client.model.ScoutingObservationAttachments;
import org.openapitools.client.model.ScoutingObservations;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LayersApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public LayersApi() {
        this(Configuration.getDefaultApiClient());
    }

    public LayersApi(ApiClient apiClient) {
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
     * Build call for v4LayersAsAppliedActivityIdContentsGet
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param activityId Unique identifier of the Application Activity. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersAsAppliedActivityIdContentsGetCall(String accept, UUID activityId, String range, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/layers/asApplied/{activityId}/contents"
            .replace("{" + "activityId" + "}", localVarApiClient.escapeString(activityId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        if (range != null) {
            localVarHeaderParams.put("Range", localVarApiClient.parameterToString(range));
        }

        final String[] localVarAccepts = {
            "application/octet-stream",
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

        String[] localVarAuthNames = new String[] { "api_key", "oauth2_authorization_code" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v4LayersAsAppliedActivityIdContentsGetValidateBeforeCall(String accept, UUID activityId, String range, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling v4LayersAsAppliedActivityIdContentsGet(Async)");
        }

        // verify the required parameter 'activityId' is set
        if (activityId == null) {
            throw new ApiException("Missing the required parameter 'activityId' when calling v4LayersAsAppliedActivityIdContentsGet(Async)");
        }

        // verify the required parameter 'range' is set
        if (range == null) {
            throw new ApiException("Missing the required parameter 'range' when calling v4LayersAsAppliedActivityIdContentsGet(Async)");
        }

        return v4LayersAsAppliedActivityIdContentsGetCall(accept, activityId, range, _callback);

    }

    /**
     * Retrieve the raw application activity
     * Retrieve an individual application activity by id.  Ids are retrieved via the  /layers/asApplied route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The data is compressed using .zip format.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param activityId Unique identifier of the Application Activity. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @return ApplicationActivityContents
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApplicationActivityContents v4LayersAsAppliedActivityIdContentsGet(String accept, UUID activityId, String range) throws ApiException {
        ApiResponse<ApplicationActivityContents> localVarResp = v4LayersAsAppliedActivityIdContentsGetWithHttpInfo(accept, activityId, range);
        return localVarResp.getData();
    }

    /**
     * Retrieve the raw application activity
     * Retrieve an individual application activity by id.  Ids are retrieved via the  /layers/asApplied route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The data is compressed using .zip format.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param activityId Unique identifier of the Application Activity. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @return ApiResponse&lt;ApplicationActivityContents&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<ApplicationActivityContents> v4LayersAsAppliedActivityIdContentsGetWithHttpInfo(String accept, UUID activityId, String range) throws ApiException {
        okhttp3.Call localVarCall = v4LayersAsAppliedActivityIdContentsGetValidateBeforeCall(accept, activityId, range, null);
        Type localVarReturnType = new TypeToken<ApplicationActivityContents>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve the raw application activity (asynchronously)
     * Retrieve an individual application activity by id.  Ids are retrieved via the  /layers/asApplied route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The data is compressed using .zip format.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param activityId Unique identifier of the Application Activity. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersAsAppliedActivityIdContentsGetAsync(String accept, UUID activityId, String range, final ApiCallback<ApplicationActivityContents> _callback) throws ApiException {

        okhttp3.Call localVarCall = v4LayersAsAppliedActivityIdContentsGetValidateBeforeCall(accept, activityId, range, _callback);
        Type localVarReturnType = new TypeToken<ApplicationActivityContents>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for v4LayersAsAppliedGet
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param resourceOwnerId Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param updatedAfter Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersAsAppliedGetCall(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/layers/asApplied";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (resourceOwnerId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("resourceOwnerId", resourceOwnerId));
        }

        if (occurredAfter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("occurredAfter", occurredAfter));
        }

        if (occurredBefore != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("occurredBefore", occurredBefore));
        }

        if (updatedAfter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("updatedAfter", updatedAfter));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        if (xNextToken != null) {
            localVarHeaderParams.put("X-Next-Token", localVarApiClient.parameterToString(xNextToken));
        }

        if (xLimit != null) {
            localVarHeaderParams.put("X-Limit", localVarApiClient.parameterToString(xLimit));
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

        String[] localVarAuthNames = new String[] { "api_key", "oauth2_authorization_code" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v4LayersAsAppliedGetValidateBeforeCall(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling v4LayersAsAppliedGet(Async)");
        }

        return v4LayersAsAppliedGetCall(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter, _callback);

    }

    /**
     * Retrieve a list of application activities
     * Retrieve a list of application activities. The id in the response is used for  GET /v4/layers/asApplied/{activityId}/contents.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param resourceOwnerId Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param updatedAfter Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. (optional)
     * @return ApplicationActivities
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApplicationActivities v4LayersAsAppliedGet(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter) throws ApiException {
        ApiResponse<ApplicationActivities> localVarResp = v4LayersAsAppliedGetWithHttpInfo(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter);
        return localVarResp.getData();
    }

    /**
     * Retrieve a list of application activities
     * Retrieve a list of application activities. The id in the response is used for  GET /v4/layers/asApplied/{activityId}/contents.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param resourceOwnerId Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param updatedAfter Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. (optional)
     * @return ApiResponse&lt;ApplicationActivities&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<ApplicationActivities> v4LayersAsAppliedGetWithHttpInfo(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter) throws ApiException {
        okhttp3.Call localVarCall = v4LayersAsAppliedGetValidateBeforeCall(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter, null);
        Type localVarReturnType = new TypeToken<ApplicationActivities>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a list of application activities (asynchronously)
     * Retrieve a list of application activities. The id in the response is used for  GET /v4/layers/asApplied/{activityId}/contents.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param resourceOwnerId Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param updatedAfter Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersAsAppliedGetAsync(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter, final ApiCallback<ApplicationActivities> _callback) throws ApiException {

        okhttp3.Call localVarCall = v4LayersAsAppliedGetValidateBeforeCall(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter, _callback);
        Type localVarReturnType = new TypeToken<ApplicationActivities>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for v4LayersAsHarvestedActivityIdContentsGet
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param activityId Unique identifier of the Harvest Activity. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersAsHarvestedActivityIdContentsGetCall(String accept, UUID activityId, String range, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/layers/asHarvested/{activityId}/contents"
            .replace("{" + "activityId" + "}", localVarApiClient.escapeString(activityId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        if (range != null) {
            localVarHeaderParams.put("Range", localVarApiClient.parameterToString(range));
        }

        final String[] localVarAccepts = {
            "application/octet-stream",
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

        String[] localVarAuthNames = new String[] { "api_key", "oauth2_authorization_code" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v4LayersAsHarvestedActivityIdContentsGetValidateBeforeCall(String accept, UUID activityId, String range, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling v4LayersAsHarvestedActivityIdContentsGet(Async)");
        }

        // verify the required parameter 'activityId' is set
        if (activityId == null) {
            throw new ApiException("Missing the required parameter 'activityId' when calling v4LayersAsHarvestedActivityIdContentsGet(Async)");
        }

        // verify the required parameter 'range' is set
        if (range == null) {
            throw new ApiException("Missing the required parameter 'range' when calling v4LayersAsHarvestedActivityIdContentsGet(Async)");
        }

        return v4LayersAsHarvestedActivityIdContentsGetCall(accept, activityId, range, _callback);

    }

    /**
     * Retrieve the raw harvest activity
     * Retrieve an individual harvest activity by id.  Ids are retrieved via the  /layers/asHarvested route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The data is compressed using .zip format.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param activityId Unique identifier of the Harvest Activity. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @return HarvestActivityContents
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public HarvestActivityContents v4LayersAsHarvestedActivityIdContentsGet(String accept, UUID activityId, String range) throws ApiException {
        ApiResponse<HarvestActivityContents> localVarResp = v4LayersAsHarvestedActivityIdContentsGetWithHttpInfo(accept, activityId, range);
        return localVarResp.getData();
    }

    /**
     * Retrieve the raw harvest activity
     * Retrieve an individual harvest activity by id.  Ids are retrieved via the  /layers/asHarvested route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The data is compressed using .zip format.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param activityId Unique identifier of the Harvest Activity. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @return ApiResponse&lt;HarvestActivityContents&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<HarvestActivityContents> v4LayersAsHarvestedActivityIdContentsGetWithHttpInfo(String accept, UUID activityId, String range) throws ApiException {
        okhttp3.Call localVarCall = v4LayersAsHarvestedActivityIdContentsGetValidateBeforeCall(accept, activityId, range, null);
        Type localVarReturnType = new TypeToken<HarvestActivityContents>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve the raw harvest activity (asynchronously)
     * Retrieve an individual harvest activity by id.  Ids are retrieved via the  /layers/asHarvested route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The data is compressed using .zip format.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param activityId Unique identifier of the Harvest Activity. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersAsHarvestedActivityIdContentsGetAsync(String accept, UUID activityId, String range, final ApiCallback<HarvestActivityContents> _callback) throws ApiException {

        okhttp3.Call localVarCall = v4LayersAsHarvestedActivityIdContentsGetValidateBeforeCall(accept, activityId, range, _callback);
        Type localVarReturnType = new TypeToken<HarvestActivityContents>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for v4LayersAsHarvestedGet
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param resourceOwnerId Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param updatedAfter Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersAsHarvestedGetCall(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/layers/asHarvested";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (resourceOwnerId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("resourceOwnerId", resourceOwnerId));
        }

        if (occurredAfter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("occurredAfter", occurredAfter));
        }

        if (occurredBefore != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("occurredBefore", occurredBefore));
        }

        if (updatedAfter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("updatedAfter", updatedAfter));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        if (xNextToken != null) {
            localVarHeaderParams.put("X-Next-Token", localVarApiClient.parameterToString(xNextToken));
        }

        if (xLimit != null) {
            localVarHeaderParams.put("X-Limit", localVarApiClient.parameterToString(xLimit));
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

        String[] localVarAuthNames = new String[] { "api_key", "oauth2_authorization_code" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v4LayersAsHarvestedGetValidateBeforeCall(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling v4LayersAsHarvestedGet(Async)");
        }

        return v4LayersAsHarvestedGetCall(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter, _callback);

    }

    /**
     * Retrieve a list of harvest activities
     * Retrieve a list of harvest activities. The id in the response is used for  GET /v4/layers/asHarvested/{activityId}/contents.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param resourceOwnerId Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param updatedAfter Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. (optional)
     * @return HarvestActivities
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public HarvestActivities v4LayersAsHarvestedGet(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter) throws ApiException {
        ApiResponse<HarvestActivities> localVarResp = v4LayersAsHarvestedGetWithHttpInfo(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter);
        return localVarResp.getData();
    }

    /**
     * Retrieve a list of harvest activities
     * Retrieve a list of harvest activities. The id in the response is used for  GET /v4/layers/asHarvested/{activityId}/contents.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param resourceOwnerId Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param updatedAfter Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. (optional)
     * @return ApiResponse&lt;HarvestActivities&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<HarvestActivities> v4LayersAsHarvestedGetWithHttpInfo(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter) throws ApiException {
        okhttp3.Call localVarCall = v4LayersAsHarvestedGetValidateBeforeCall(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter, null);
        Type localVarReturnType = new TypeToken<HarvestActivities>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a list of harvest activities (asynchronously)
     * Retrieve a list of harvest activities. The id in the response is used for  GET /v4/layers/asHarvested/{activityId}/contents.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param resourceOwnerId Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param updatedAfter Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersAsHarvestedGetAsync(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter, final ApiCallback<HarvestActivities> _callback) throws ApiException {

        okhttp3.Call localVarCall = v4LayersAsHarvestedGetValidateBeforeCall(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter, _callback);
        Type localVarReturnType = new TypeToken<HarvestActivities>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for v4LayersAsPlantedActivityIdContentsGet
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param activityId Unique identifier of the Planting Activity. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersAsPlantedActivityIdContentsGetCall(String accept, UUID activityId, String range, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/layers/asPlanted/{activityId}/contents"
            .replace("{" + "activityId" + "}", localVarApiClient.escapeString(activityId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        if (range != null) {
            localVarHeaderParams.put("Range", localVarApiClient.parameterToString(range));
        }

        final String[] localVarAccepts = {
            "application/octet-stream",
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

        String[] localVarAuthNames = new String[] { "api_key", "oauth2_authorization_code" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v4LayersAsPlantedActivityIdContentsGetValidateBeforeCall(String accept, UUID activityId, String range, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling v4LayersAsPlantedActivityIdContentsGet(Async)");
        }

        // verify the required parameter 'activityId' is set
        if (activityId == null) {
            throw new ApiException("Missing the required parameter 'activityId' when calling v4LayersAsPlantedActivityIdContentsGet(Async)");
        }

        // verify the required parameter 'range' is set
        if (range == null) {
            throw new ApiException("Missing the required parameter 'range' when calling v4LayersAsPlantedActivityIdContentsGet(Async)");
        }

        return v4LayersAsPlantedActivityIdContentsGetCall(accept, activityId, range, _callback);

    }

    /**
     * Retrieve the raw planting activity
     * Retrieve an individual planting activity by id.  Ids are retrieved via the  /layers/asPlanted route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).  The data is compressed using .zip format.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param activityId Unique identifier of the Planting Activity. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @return PlantingActivityContents
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public PlantingActivityContents v4LayersAsPlantedActivityIdContentsGet(String accept, UUID activityId, String range) throws ApiException {
        ApiResponse<PlantingActivityContents> localVarResp = v4LayersAsPlantedActivityIdContentsGetWithHttpInfo(accept, activityId, range);
        return localVarResp.getData();
    }

    /**
     * Retrieve the raw planting activity
     * Retrieve an individual planting activity by id.  Ids are retrieved via the  /layers/asPlanted route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).  The data is compressed using .zip format.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param activityId Unique identifier of the Planting Activity. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @return ApiResponse&lt;PlantingActivityContents&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<PlantingActivityContents> v4LayersAsPlantedActivityIdContentsGetWithHttpInfo(String accept, UUID activityId, String range) throws ApiException {
        okhttp3.Call localVarCall = v4LayersAsPlantedActivityIdContentsGetValidateBeforeCall(accept, activityId, range, null);
        Type localVarReturnType = new TypeToken<PlantingActivityContents>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve the raw planting activity (asynchronously)
     * Retrieve an individual planting activity by id.  Ids are retrieved via the  /layers/asPlanted route. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60;  (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).  The data is compressed using .zip format.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param activityId Unique identifier of the Planting Activity. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersAsPlantedActivityIdContentsGetAsync(String accept, UUID activityId, String range, final ApiCallback<PlantingActivityContents> _callback) throws ApiException {

        okhttp3.Call localVarCall = v4LayersAsPlantedActivityIdContentsGetValidateBeforeCall(accept, activityId, range, _callback);
        Type localVarReturnType = new TypeToken<PlantingActivityContents>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for v4LayersAsPlantedGet
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param resourceOwnerId Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param updatedAfter Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersAsPlantedGetCall(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/layers/asPlanted";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (resourceOwnerId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("resourceOwnerId", resourceOwnerId));
        }

        if (occurredAfter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("occurredAfter", occurredAfter));
        }

        if (occurredBefore != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("occurredBefore", occurredBefore));
        }

        if (updatedAfter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("updatedAfter", updatedAfter));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        if (xNextToken != null) {
            localVarHeaderParams.put("X-Next-Token", localVarApiClient.parameterToString(xNextToken));
        }

        if (xLimit != null) {
            localVarHeaderParams.put("X-Limit", localVarApiClient.parameterToString(xLimit));
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

        String[] localVarAuthNames = new String[] { "api_key", "oauth2_authorization_code" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v4LayersAsPlantedGetValidateBeforeCall(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling v4LayersAsPlantedGet(Async)");
        }

        return v4LayersAsPlantedGetCall(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter, _callback);

    }

    /**
     * Retrieve a list of planting activities
     * Retrieve a list of planting activities. The id in the response is used for  GET /v4/layers/asPlanted/{activityId}/contents.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param resourceOwnerId Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param updatedAfter Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. (optional)
     * @return PlantingActivities
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public PlantingActivities v4LayersAsPlantedGet(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter) throws ApiException {
        ApiResponse<PlantingActivities> localVarResp = v4LayersAsPlantedGetWithHttpInfo(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter);
        return localVarResp.getData();
    }

    /**
     * Retrieve a list of planting activities
     * Retrieve a list of planting activities. The id in the response is used for  GET /v4/layers/asPlanted/{activityId}/contents.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param resourceOwnerId Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param updatedAfter Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. (optional)
     * @return ApiResponse&lt;PlantingActivities&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<PlantingActivities> v4LayersAsPlantedGetWithHttpInfo(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter) throws ApiException {
        okhttp3.Call localVarCall = v4LayersAsPlantedGetValidateBeforeCall(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter, null);
        Type localVarReturnType = new TypeToken<PlantingActivities>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a list of planting activities (asynchronously)
     * Retrieve a list of planting activities. The id in the response is used for  GET /v4/layers/asPlanted/{activityId}/contents.
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param resourceOwnerId Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param updatedAfter Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersAsPlantedGetAsync(String accept, String xNextToken, Integer xLimit, UUID resourceOwnerId, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, OffsetDateTime updatedAfter, final ApiCallback<PlantingActivities> _callback) throws ApiException {

        okhttp3.Call localVarCall = v4LayersAsPlantedGetValidateBeforeCall(accept, xNextToken, xLimit, resourceOwnerId, occurredAfter, occurredBefore, updatedAfter, _callback);
        Type localVarReturnType = new TypeToken<PlantingActivities>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for v4LayersScoutingObservationsGet
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersScoutingObservationsGetCall(String xNextToken, Integer xLimit, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/layers/scoutingObservations";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (occurredAfter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("occurredAfter", occurredAfter));
        }

        if (occurredBefore != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("occurredBefore", occurredBefore));
        }

        if (xNextToken != null) {
            localVarHeaderParams.put("X-Next-Token", localVarApiClient.parameterToString(xNextToken));
        }

        if (xLimit != null) {
            localVarHeaderParams.put("X-Limit", localVarApiClient.parameterToString(xLimit));
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

        String[] localVarAuthNames = new String[] { "api_key", "oauth2_authorization_code" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v4LayersScoutingObservationsGetValidateBeforeCall(String xNextToken, Integer xLimit, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, final ApiCallback _callback) throws ApiException {
        return v4LayersScoutingObservationsGetCall(xNextToken, xLimit, occurredAfter, occurredBefore, _callback);

    }

    /**
     * Retrieve a list of scouting observations
     * Retrieve a list of scouting observations created or updated by the user identified by the Authorization header.
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @return ScoutingObservations
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ScoutingObservations v4LayersScoutingObservationsGet(String xNextToken, Integer xLimit, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore) throws ApiException {
        ApiResponse<ScoutingObservations> localVarResp = v4LayersScoutingObservationsGetWithHttpInfo(xNextToken, xLimit, occurredAfter, occurredBefore);
        return localVarResp.getData();
    }

    /**
     * Retrieve a list of scouting observations
     * Retrieve a list of scouting observations created or updated by the user identified by the Authorization header.
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @return ApiResponse&lt;ScoutingObservations&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<ScoutingObservations> v4LayersScoutingObservationsGetWithHttpInfo(String xNextToken, Integer xLimit, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore) throws ApiException {
        okhttp3.Call localVarCall = v4LayersScoutingObservationsGetValidateBeforeCall(xNextToken, xLimit, occurredAfter, occurredBefore, null);
        Type localVarReturnType = new TypeToken<ScoutingObservations>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a list of scouting observations (asynchronously)
     * Retrieve a list of scouting observations created or updated by the user identified by the Authorization header.
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param occurredAfter Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param occurredBefore Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be &lt;&#x3D; occurredBefore. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersScoutingObservationsGetAsync(String xNextToken, Integer xLimit, OffsetDateTime occurredAfter, OffsetDateTime occurredBefore, final ApiCallback<ScoutingObservations> _callback) throws ApiException {

        okhttp3.Call localVarCall = v4LayersScoutingObservationsGetValidateBeforeCall(xNextToken, xLimit, occurredAfter, occurredBefore, _callback);
        Type localVarReturnType = new TypeToken<ScoutingObservations>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param scoutingObservationId Unique identifier of the Scouting Observation. (required)
     * @param attachmentId Unique identifier of the attachment. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetCall(String accept, UUID scoutingObservationId, UUID attachmentId, String range, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/layers/scoutingObservations/{scoutingObservationId}/attachments/{attachmentId}/contents"
            .replace("{" + "scoutingObservationId" + "}", localVarApiClient.escapeString(scoutingObservationId.toString()))
            .replace("{" + "attachmentId" + "}", localVarApiClient.escapeString(attachmentId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        if (range != null) {
            localVarHeaderParams.put("Range", localVarApiClient.parameterToString(range));
        }

        final String[] localVarAccepts = {
            "image/jpeg",
            "image/png",
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

        String[] localVarAuthNames = new String[] { "api_key", "oauth2_authorization_code" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetValidateBeforeCall(String accept, UUID scoutingObservationId, UUID attachmentId, String range, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet(Async)");
        }

        // verify the required parameter 'scoutingObservationId' is set
        if (scoutingObservationId == null) {
            throw new ApiException("Missing the required parameter 'scoutingObservationId' when calling v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet(Async)");
        }

        // verify the required parameter 'attachmentId' is set
        if (attachmentId == null) {
            throw new ApiException("Missing the required parameter 'attachmentId' when calling v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet(Async)");
        }

        // verify the required parameter 'range' is set
        if (range == null) {
            throw new ApiException("Missing the required parameter 'range' when calling v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet(Async)");
        }

        return v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetCall(accept, scoutingObservationId, attachmentId, range, _callback);

    }

    /**
     * Retrieve the binary contents of a scouting observation’s attachment.
     * Photos added to scouting notes in the FieldView app are capped to &#x60;20MiB&#x60; (&#x60;20971520 bytes&#x60;), and we won’t store photos larger than that in a scouting note. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param scoutingObservationId Unique identifier of the Scouting Observation. (required)
     * @param attachmentId Unique identifier of the attachment. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @return ScoutingObservationAttachmentContents
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ScoutingObservationAttachmentContents v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet(String accept, UUID scoutingObservationId, UUID attachmentId, String range) throws ApiException {
        ApiResponse<ScoutingObservationAttachmentContents> localVarResp = v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetWithHttpInfo(accept, scoutingObservationId, attachmentId, range);
        return localVarResp.getData();
    }

    /**
     * Retrieve the binary contents of a scouting observation’s attachment.
     * Photos added to scouting notes in the FieldView app are capped to &#x60;20MiB&#x60; (&#x60;20971520 bytes&#x60;), and we won’t store photos larger than that in a scouting note. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param scoutingObservationId Unique identifier of the Scouting Observation. (required)
     * @param attachmentId Unique identifier of the attachment. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @return ApiResponse&lt;ScoutingObservationAttachmentContents&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<ScoutingObservationAttachmentContents> v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetWithHttpInfo(String accept, UUID scoutingObservationId, UUID attachmentId, String range) throws ApiException {
        okhttp3.Call localVarCall = v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetValidateBeforeCall(accept, scoutingObservationId, attachmentId, range, null);
        Type localVarReturnType = new TypeToken<ScoutingObservationAttachmentContents>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve the binary contents of a scouting observation’s attachment. (asynchronously)
     * Photos added to scouting notes in the FieldView app are capped to &#x60;20MiB&#x60; (&#x60;20971520 bytes&#x60;), and we won’t store photos larger than that in a scouting note. Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size, must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).
     * @param accept Must be either \\*_/_* or application/octet-stream,application/json (required)
     * @param scoutingObservationId Unique identifier of the Scouting Observation. (required)
     * @param attachmentId Unique identifier of the attachment. (required)
     * @param range Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 416 </td><td> Range Not Satisfiable </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetAsync(String accept, UUID scoutingObservationId, UUID attachmentId, String range, final ApiCallback<ScoutingObservationAttachmentContents> _callback) throws ApiException {

        okhttp3.Call localVarCall = v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetValidateBeforeCall(accept, scoutingObservationId, attachmentId, range, _callback);
        Type localVarReturnType = new TypeToken<ScoutingObservationAttachmentContents>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet
     * @param scoutingObservationId Unique identifier of the Scouting Observation. (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetCall(UUID scoutingObservationId, String xNextToken, Integer xLimit, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/layers/scoutingObservations/{scoutingObservationId}/attachments"
            .replace("{" + "scoutingObservationId" + "}", localVarApiClient.escapeString(scoutingObservationId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xNextToken != null) {
            localVarHeaderParams.put("X-Next-Token", localVarApiClient.parameterToString(xNextToken));
        }

        if (xLimit != null) {
            localVarHeaderParams.put("X-Limit", localVarApiClient.parameterToString(xLimit));
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

        String[] localVarAuthNames = new String[] { "api_key", "oauth2_authorization_code" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetValidateBeforeCall(UUID scoutingObservationId, String xNextToken, Integer xLimit, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'scoutingObservationId' is set
        if (scoutingObservationId == null) {
            throw new ApiException("Missing the required parameter 'scoutingObservationId' when calling v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet(Async)");
        }

        return v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetCall(scoutingObservationId, xNextToken, xLimit, _callback);

    }

    /**
     * Retrieve attachments associated with a given scouting observation.
     * Retrieve attachments associated with a given scouting observation. Photos added to scouting notes in the FieldView app are capped to 20MB, and we won’t store photos larger than that in a scouting note.
     * @param scoutingObservationId Unique identifier of the Scouting Observation. (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @return ScoutingObservationAttachments
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ScoutingObservationAttachments v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet(UUID scoutingObservationId, String xNextToken, Integer xLimit) throws ApiException {
        ApiResponse<ScoutingObservationAttachments> localVarResp = v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetWithHttpInfo(scoutingObservationId, xNextToken, xLimit);
        return localVarResp.getData();
    }

    /**
     * Retrieve attachments associated with a given scouting observation.
     * Retrieve attachments associated with a given scouting observation. Photos added to scouting notes in the FieldView app are capped to 20MB, and we won’t store photos larger than that in a scouting note.
     * @param scoutingObservationId Unique identifier of the Scouting Observation. (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @return ApiResponse&lt;ScoutingObservationAttachments&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<ScoutingObservationAttachments> v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetWithHttpInfo(UUID scoutingObservationId, String xNextToken, Integer xLimit) throws ApiException {
        okhttp3.Call localVarCall = v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetValidateBeforeCall(scoutingObservationId, xNextToken, xLimit, null);
        Type localVarReturnType = new TypeToken<ScoutingObservationAttachments>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve attachments associated with a given scouting observation. (asynchronously)
     * Retrieve attachments associated with a given scouting observation. Photos added to scouting notes in the FieldView app are capped to 20MB, and we won’t store photos larger than that in a scouting note.
     * @param scoutingObservationId Unique identifier of the Scouting Observation. (required)
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetAsync(UUID scoutingObservationId, String xNextToken, Integer xLimit, final ApiCallback<ScoutingObservationAttachments> _callback) throws ApiException {

        okhttp3.Call localVarCall = v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetValidateBeforeCall(scoutingObservationId, xNextToken, xLimit, _callback);
        Type localVarReturnType = new TypeToken<ScoutingObservationAttachments>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for v4LayersScoutingObservationsScoutingObservationIdGet
     * @param scoutingObservationId Unique identifier of the Scouting Observation. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the requested scouting observation. </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersScoutingObservationsScoutingObservationIdGetCall(UUID scoutingObservationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/layers/scoutingObservations/{scoutingObservationId}"
            .replace("{" + "scoutingObservationId" + "}", localVarApiClient.escapeString(scoutingObservationId.toString()));

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

        String[] localVarAuthNames = new String[] { "api_key", "oauth2_authorization_code" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call v4LayersScoutingObservationsScoutingObservationIdGetValidateBeforeCall(UUID scoutingObservationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'scoutingObservationId' is set
        if (scoutingObservationId == null) {
            throw new ApiException("Missing the required parameter 'scoutingObservationId' when calling v4LayersScoutingObservationsScoutingObservationIdGet(Async)");
        }

        return v4LayersScoutingObservationsScoutingObservationIdGetCall(scoutingObservationId, _callback);

    }

    /**
     * Retrieve individual scouting observation
     * Retrieve an individual scouting observation by id.  Ids are retrieved via the /layers/scoutingObservations route.
     * @param scoutingObservationId Unique identifier of the Scouting Observation. (required)
     * @return ScoutingObservation
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the requested scouting observation. </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ScoutingObservation v4LayersScoutingObservationsScoutingObservationIdGet(UUID scoutingObservationId) throws ApiException {
        ApiResponse<ScoutingObservation> localVarResp = v4LayersScoutingObservationsScoutingObservationIdGetWithHttpInfo(scoutingObservationId);
        return localVarResp.getData();
    }

    /**
     * Retrieve individual scouting observation
     * Retrieve an individual scouting observation by id.  Ids are retrieved via the /layers/scoutingObservations route.
     * @param scoutingObservationId Unique identifier of the Scouting Observation. (required)
     * @return ApiResponse&lt;ScoutingObservation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the requested scouting observation. </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<ScoutingObservation> v4LayersScoutingObservationsScoutingObservationIdGetWithHttpInfo(UUID scoutingObservationId) throws ApiException {
        okhttp3.Call localVarCall = v4LayersScoutingObservationsScoutingObservationIdGetValidateBeforeCall(scoutingObservationId, null);
        Type localVarReturnType = new TypeToken<ScoutingObservation>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve individual scouting observation (asynchronously)
     * Retrieve an individual scouting observation by id.  Ids are retrieved via the /layers/scoutingObservations route.
     * @param scoutingObservationId Unique identifier of the Scouting Observation. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the requested scouting observation. </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call v4LayersScoutingObservationsScoutingObservationIdGetAsync(UUID scoutingObservationId, final ApiCallback<ScoutingObservation> _callback) throws ApiException {

        okhttp3.Call localVarCall = v4LayersScoutingObservationsScoutingObservationIdGetValidateBeforeCall(scoutingObservationId, _callback);
        Type localVarReturnType = new TypeToken<ScoutingObservation>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
