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


import org.openapitools.client.model.Error;
import org.openapitools.client.model.Field;
import org.openapitools.client.model.Fields;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FieldsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public FieldsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public FieldsApi(ApiClient apiClient) {
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
     * Build call for fetchAllFields
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param fieldName Optional prefix filter for field name. Must be at least 3 characters. (optional)
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
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 409 </td><td> Conflict </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchAllFieldsCall(String xNextToken, Integer xLimit, String fieldName, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/fields/all";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (fieldName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("fieldName", fieldName));
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
    private okhttp3.Call fetchAllFieldsValidateBeforeCall(String xNextToken, Integer xLimit, String fieldName, final ApiCallback _callback) throws ApiException {
        return fetchAllFieldsCall(xNextToken, xLimit, fieldName, _callback);

    }

    /**
     * Retrieve list of all Fields the user has access to.
     * Retrieve all fields the authenticated user has access to, including fields shared with the authenticated user from other resource owners. Filter the results by field name if the &#x60;fieldName&#x60; query parameter is specified. A 409 will be returned if the X-Next-Token has expired. When receiving a 409, the client should discard the X-Next-Token, discard all currently persisted fields for the user, and re-fetch fields from /fields/all.
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param fieldName Optional prefix filter for field name. Must be at least 3 characters. (optional)
     * @return Fields
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 409 </td><td> Conflict </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public Fields fetchAllFields(String xNextToken, Integer xLimit, String fieldName) throws ApiException {
        ApiResponse<Fields> localVarResp = fetchAllFieldsWithHttpInfo(xNextToken, xLimit, fieldName);
        return localVarResp.getData();
    }

    /**
     * Retrieve list of all Fields the user has access to.
     * Retrieve all fields the authenticated user has access to, including fields shared with the authenticated user from other resource owners. Filter the results by field name if the &#x60;fieldName&#x60; query parameter is specified. A 409 will be returned if the X-Next-Token has expired. When receiving a 409, the client should discard the X-Next-Token, discard all currently persisted fields for the user, and re-fetch fields from /fields/all.
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param fieldName Optional prefix filter for field name. Must be at least 3 characters. (optional)
     * @return ApiResponse&lt;Fields&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 409 </td><td> Conflict </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Fields> fetchAllFieldsWithHttpInfo(String xNextToken, Integer xLimit, String fieldName) throws ApiException {
        okhttp3.Call localVarCall = fetchAllFieldsValidateBeforeCall(xNextToken, xLimit, fieldName, null);
        Type localVarReturnType = new TypeToken<Fields>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve list of all Fields the user has access to. (asynchronously)
     * Retrieve all fields the authenticated user has access to, including fields shared with the authenticated user from other resource owners. Filter the results by field name if the &#x60;fieldName&#x60; query parameter is specified. A 409 will be returned if the X-Next-Token has expired. When receiving a 409, the client should discard the X-Next-Token, discard all currently persisted fields for the user, and re-fetch fields from /fields/all.
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param fieldName Optional prefix filter for field name. Must be at least 3 characters. (optional)
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
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 409 </td><td> Conflict </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchAllFieldsAsync(String xNextToken, Integer xLimit, String fieldName, final ApiCallback<Fields> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchAllFieldsValidateBeforeCall(xNextToken, xLimit, fieldName, _callback);
        Type localVarReturnType = new TypeToken<Fields>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for fetchFieldById
     * @param fieldId Unique identifier of the Field. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the requested Field. </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchFieldByIdCall(UUID fieldId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/fields/{fieldId}"
            .replace("{" + "fieldId" + "}", localVarApiClient.escapeString(fieldId.toString()));

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
    private okhttp3.Call fetchFieldByIdValidateBeforeCall(UUID fieldId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'fieldId' is set
        if (fieldId == null) {
            throw new ApiException("Missing the required parameter 'fieldId' when calling fetchFieldById(Async)");
        }

        return fetchFieldByIdCall(fieldId, _callback);

    }

    /**
     * Retrieve a specific Field by ID
     * Retrieve a given **Field** by ID.
     * @param fieldId Unique identifier of the Field. (required)
     * @return Field
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the requested Field. </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public Field fetchFieldById(UUID fieldId) throws ApiException {
        ApiResponse<Field> localVarResp = fetchFieldByIdWithHttpInfo(fieldId);
        return localVarResp.getData();
    }

    /**
     * Retrieve a specific Field by ID
     * Retrieve a given **Field** by ID.
     * @param fieldId Unique identifier of the Field. (required)
     * @return ApiResponse&lt;Field&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the requested Field. </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Field> fetchFieldByIdWithHttpInfo(UUID fieldId) throws ApiException {
        okhttp3.Call localVarCall = fetchFieldByIdValidateBeforeCall(fieldId, null);
        Type localVarReturnType = new TypeToken<Field>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a specific Field by ID (asynchronously)
     * Retrieve a given **Field** by ID.
     * @param fieldId Unique identifier of the Field. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns the requested Field. </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchFieldByIdAsync(UUID fieldId, final ApiCallback<Field> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchFieldByIdValidateBeforeCall(fieldId, _callback);
        Type localVarReturnType = new TypeToken<Field>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for fetchFields
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param fieldName Optional prefix filter for field name. Must be at least 3 characters. (optional)
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
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchFieldsCall(String xNextToken, Integer xLimit, String fieldName, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/fields";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (fieldName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("fieldName", fieldName));
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
    private okhttp3.Call fetchFieldsValidateBeforeCall(String xNextToken, Integer xLimit, String fieldName, final ApiCallback _callback) throws ApiException {
        return fetchFieldsCall(xNextToken, xLimit, fieldName, _callback);

    }

    /**
     * Retrieve list of Fields
     * Retrieve list of **Fields**. Filter the results by field name if the &#x60;fieldName&#x60; query parameter is specified.
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param fieldName Optional prefix filter for field name. Must be at least 3 characters. (optional)
     * @return Fields
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public Fields fetchFields(String xNextToken, Integer xLimit, String fieldName) throws ApiException {
        ApiResponse<Fields> localVarResp = fetchFieldsWithHttpInfo(xNextToken, xLimit, fieldName);
        return localVarResp.getData();
    }

    /**
     * Retrieve list of Fields
     * Retrieve list of **Fields**. Filter the results by field name if the &#x60;fieldName&#x60; query parameter is specified.
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param fieldName Optional prefix filter for field name. Must be at least 3 characters. (optional)
     * @return ApiResponse&lt;Fields&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 206 </td><td> Partial Result </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 304 </td><td> Not Modified </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Fields> fetchFieldsWithHttpInfo(String xNextToken, Integer xLimit, String fieldName) throws ApiException {
        okhttp3.Call localVarCall = fetchFieldsValidateBeforeCall(xNextToken, xLimit, fieldName, null);
        Type localVarReturnType = new TypeToken<Fields>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve list of Fields (asynchronously)
     * Retrieve list of **Fields**. Filter the results by field name if the &#x60;fieldName&#x60; query parameter is specified.
     * @param xNextToken Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. (optional)
     * @param xLimit Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. (optional)
     * @param fieldName Optional prefix filter for field name. Must be at least 3 characters. (optional)
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
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call fetchFieldsAsync(String xNextToken, Integer xLimit, String fieldName, final ApiCallback<Fields> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchFieldsValidateBeforeCall(xNextToken, xLimit, fieldName, _callback);
        Type localVarReturnType = new TypeToken<Fields>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
