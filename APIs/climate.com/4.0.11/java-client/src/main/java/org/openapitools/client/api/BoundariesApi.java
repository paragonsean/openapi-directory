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


import org.openapitools.client.model.Boundaries;
import org.openapitools.client.model.BoundariesQuery;
import org.openapitools.client.model.Boundary;
import org.openapitools.client.model.BoundaryUpload;
import org.openapitools.client.model.Error;
import java.util.UUID;
import org.openapitools.client.model.UploadedBoundaryId;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BoundariesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public BoundariesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public BoundariesApi(ApiClient apiClient) {
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
     * Build call for fetchBoundaries
     * @param boundariesQuery  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchBoundariesCall(BoundariesQuery boundariesQuery, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = boundariesQuery;

        // create path and map variables
        String localVarPath = "/v4/boundaries/query";

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

        String[] localVarAuthNames = new String[] { "api_key", "oauth2_authorization_code" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call fetchBoundariesValidateBeforeCall(BoundariesQuery boundariesQuery, final ApiCallback _callback) throws ApiException {
        return fetchBoundariesCall(boundariesQuery, _callback);

    }

    /**
     * Retrieve Boundaries in batch
     * Retrieve multiple **Boundaries** (up to 10 per request).
     * @param boundariesQuery  (optional)
     * @return Boundaries
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public Boundaries fetchBoundaries(BoundariesQuery boundariesQuery) throws ApiException {
        ApiResponse<Boundaries> localVarResp = fetchBoundariesWithHttpInfo(boundariesQuery);
        return localVarResp.getData();
    }

    /**
     * Retrieve Boundaries in batch
     * Retrieve multiple **Boundaries** (up to 10 per request).
     * @param boundariesQuery  (optional)
     * @return ApiResponse&lt;Boundaries&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Boundaries> fetchBoundariesWithHttpInfo(BoundariesQuery boundariesQuery) throws ApiException {
        okhttp3.Call localVarCall = fetchBoundariesValidateBeforeCall(boundariesQuery, null);
        Type localVarReturnType = new TypeToken<Boundaries>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve Boundaries in batch (asynchronously)
     * Retrieve multiple **Boundaries** (up to 10 per request).
     * @param boundariesQuery  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchBoundariesAsync(BoundariesQuery boundariesQuery, final ApiCallback<Boundaries> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchBoundariesValidateBeforeCall(boundariesQuery, _callback);
        Type localVarReturnType = new TypeToken<Boundaries>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for fetchBoundaryById
     * @param boundaryId Unique identifier of the Boundary (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchBoundaryByIdCall(UUID boundaryId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/boundaries/{boundaryId}"
            .replace("{" + "boundaryId" + "}", localVarApiClient.escapeString(boundaryId.toString()));

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
    private okhttp3.Call fetchBoundaryByIdValidateBeforeCall(UUID boundaryId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'boundaryId' is set
        if (boundaryId == null) {
            throw new ApiException("Missing the required parameter 'boundaryId' when calling fetchBoundaryById(Async)");
        }

        return fetchBoundaryByIdCall(boundaryId, _callback);

    }

    /**
     * Retrieve a Boundary by ID
     * Retrieve a **Boundary** by ID.
     * @param boundaryId Unique identifier of the Boundary (required)
     * @return Boundary
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public Boundary fetchBoundaryById(UUID boundaryId) throws ApiException {
        ApiResponse<Boundary> localVarResp = fetchBoundaryByIdWithHttpInfo(boundaryId);
        return localVarResp.getData();
    }

    /**
     * Retrieve a Boundary by ID
     * Retrieve a **Boundary** by ID.
     * @param boundaryId Unique identifier of the Boundary (required)
     * @return ApiResponse&lt;Boundary&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Boundary> fetchBoundaryByIdWithHttpInfo(UUID boundaryId) throws ApiException {
        okhttp3.Call localVarCall = fetchBoundaryByIdValidateBeforeCall(boundaryId, null);
        Type localVarReturnType = new TypeToken<Boundary>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a Boundary by ID (asynchronously)
     * Retrieve a **Boundary** by ID.
     * @param boundaryId Unique identifier of the Boundary (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchBoundaryByIdAsync(UUID boundaryId, final ApiCallback<Boundary> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchBoundaryByIdValidateBeforeCall(boundaryId, _callback);
        Type localVarReturnType = new TypeToken<Boundary>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for uploadBoundary
     * @param boundaryUpload  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call uploadBoundaryCall(BoundaryUpload boundaryUpload, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = boundaryUpload;

        // create path and map variables
        String localVarPath = "/v4/boundaries";

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

        String[] localVarAuthNames = new String[] { "api_key", "oauth2_authorization_code" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call uploadBoundaryValidateBeforeCall(BoundaryUpload boundaryUpload, final ApiCallback _callback) throws ApiException {
        return uploadBoundaryCall(boundaryUpload, _callback);

    }

    /**
     * Upload a boundary
     * Upload a **Boundary** entry by passing the geometry of the boundary. This will store the boundary but will not create field in Climate FieldView and will not link to an existing field in Climate FieldView. This is restricted to callers with **boundaries:write** scope. To upload a field boundary for field creation in Climate FieldView, please use **POST /v4/uploads**.
     * @param boundaryUpload  (optional)
     * @return UploadedBoundaryId
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public UploadedBoundaryId uploadBoundary(BoundaryUpload boundaryUpload) throws ApiException {
        ApiResponse<UploadedBoundaryId> localVarResp = uploadBoundaryWithHttpInfo(boundaryUpload);
        return localVarResp.getData();
    }

    /**
     * Upload a boundary
     * Upload a **Boundary** entry by passing the geometry of the boundary. This will store the boundary but will not create field in Climate FieldView and will not link to an existing field in Climate FieldView. This is restricted to callers with **boundaries:write** scope. To upload a field boundary for field creation in Climate FieldView, please use **POST /v4/uploads**.
     * @param boundaryUpload  (optional)
     * @return ApiResponse&lt;UploadedBoundaryId&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<UploadedBoundaryId> uploadBoundaryWithHttpInfo(BoundaryUpload boundaryUpload) throws ApiException {
        okhttp3.Call localVarCall = uploadBoundaryValidateBeforeCall(boundaryUpload, null);
        Type localVarReturnType = new TypeToken<UploadedBoundaryId>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Upload a boundary (asynchronously)
     * Upload a **Boundary** entry by passing the geometry of the boundary. This will store the boundary but will not create field in Climate FieldView and will not link to an existing field in Climate FieldView. This is restricted to callers with **boundaries:write** scope. To upload a field boundary for field creation in Climate FieldView, please use **POST /v4/uploads**.
     * @param boundaryUpload  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call uploadBoundaryAsync(BoundaryUpload boundaryUpload, final ApiCallback<UploadedBoundaryId> _callback) throws ApiException {

        okhttp3.Call localVarCall = uploadBoundaryValidateBeforeCall(boundaryUpload, _callback);
        Type localVarReturnType = new TypeToken<UploadedBoundaryId>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
