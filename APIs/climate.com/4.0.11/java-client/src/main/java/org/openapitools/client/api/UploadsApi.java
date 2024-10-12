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
import java.util.UUID;
import org.openapitools.client.model.Upload;
import org.openapitools.client.model.UploadStatus;
import org.openapitools.client.model.UploadStatusQuery;
import org.openapitools.client.model.UploadStatuses;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class UploadsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public UploadsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public UploadsApi(ApiClient apiClient) {
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
     * Build call for chunkedUpload
     * @param contentRange Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). (required)
     * @param uploadId Unique identifier of an Upload. (required)
     * @param contentType Must be &#x60;application/octet-stream&#x60; (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call chunkedUploadCall(String contentRange, UUID uploadId, String contentType, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/uploads/{uploadId}"
            .replace("{" + "uploadId" + "}", localVarApiClient.escapeString(uploadId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (contentRange != null) {
            localVarHeaderParams.put("Content-Range", localVarApiClient.parameterToString(contentRange));
        }

        if (contentType != null) {
            localVarHeaderParams.put("Content-Type", localVarApiClient.parameterToString(contentType));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call chunkedUploadValidateBeforeCall(String contentRange, UUID uploadId, String contentType, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentRange' is set
        if (contentRange == null) {
            throw new ApiException("Missing the required parameter 'contentRange' when calling chunkedUpload(Async)");
        }

        // verify the required parameter 'uploadId' is set
        if (uploadId == null) {
            throw new ApiException("Missing the required parameter 'uploadId' when calling chunkedUpload(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling chunkedUpload(Async)");
        }

        return chunkedUploadCall(contentRange, uploadId, contentType, _callback);

    }

    /**
     * Chunked upload of data
     * Send chunked data for an **Upload**.
     * @param contentRange Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). (required)
     * @param uploadId Unique identifier of an Upload. (required)
     * @param contentType Must be &#x60;application/octet-stream&#x60; (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public void chunkedUpload(String contentRange, UUID uploadId, String contentType) throws ApiException {
        chunkedUploadWithHttpInfo(contentRange, uploadId, contentType);
    }

    /**
     * Chunked upload of data
     * Send chunked data for an **Upload**.
     * @param contentRange Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). (required)
     * @param uploadId Unique identifier of an Upload. (required)
     * @param contentType Must be &#x60;application/octet-stream&#x60; (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Void> chunkedUploadWithHttpInfo(String contentRange, UUID uploadId, String contentType) throws ApiException {
        okhttp3.Call localVarCall = chunkedUploadValidateBeforeCall(contentRange, uploadId, contentType, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Chunked upload of data (asynchronously)
     * Send chunked data for an **Upload**.
     * @param contentRange Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). (required)
     * @param uploadId Unique identifier of an Upload. (required)
     * @param contentType Must be &#x60;application/octet-stream&#x60; (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call chunkedUploadAsync(String contentRange, UUID uploadId, String contentType, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = chunkedUploadValidateBeforeCall(contentRange, uploadId, contentType, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for fetchUploadStatusById
     * @param uploadId Unique identifier of an Upload. (required)
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
    public okhttp3.Call fetchUploadStatusByIdCall(UUID uploadId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v4/uploads/{uploadId}/status"
            .replace("{" + "uploadId" + "}", localVarApiClient.escapeString(uploadId.toString()));

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
    private okhttp3.Call fetchUploadStatusByIdValidateBeforeCall(UUID uploadId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'uploadId' is set
        if (uploadId == null) {
            throw new ApiException("Missing the required parameter 'uploadId' when calling fetchUploadStatusById(Async)");
        }

        return fetchUploadStatusByIdCall(uploadId, _callback);

    }

    /**
     * Retrieve Upload status
     * Check the status of an **Upload** by ID.
     * @param uploadId Unique identifier of an Upload. (required)
     * @return UploadStatus
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
    public UploadStatus fetchUploadStatusById(UUID uploadId) throws ApiException {
        ApiResponse<UploadStatus> localVarResp = fetchUploadStatusByIdWithHttpInfo(uploadId);
        return localVarResp.getData();
    }

    /**
     * Retrieve Upload status
     * Check the status of an **Upload** by ID.
     * @param uploadId Unique identifier of an Upload. (required)
     * @return ApiResponse&lt;UploadStatus&gt;
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
    public ApiResponse<UploadStatus> fetchUploadStatusByIdWithHttpInfo(UUID uploadId) throws ApiException {
        okhttp3.Call localVarCall = fetchUploadStatusByIdValidateBeforeCall(uploadId, null);
        Type localVarReturnType = new TypeToken<UploadStatus>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve Upload status (asynchronously)
     * Check the status of an **Upload** by ID.
     * @param uploadId Unique identifier of an Upload. (required)
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
    public okhttp3.Call fetchUploadStatusByIdAsync(UUID uploadId, final ApiCallback<UploadStatus> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchUploadStatusByIdValidateBeforeCall(uploadId, _callback);
        Type localVarReturnType = new TypeToken<UploadStatus>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for fetchUploadStatuses
     * @param uploadStatusQuery  (optional)
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
    public okhttp3.Call fetchUploadStatusesCall(UploadStatusQuery uploadStatusQuery, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = uploadStatusQuery;

        // create path and map variables
        String localVarPath = "/v4/uploads/status/query";

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
    private okhttp3.Call fetchUploadStatusesValidateBeforeCall(UploadStatusQuery uploadStatusQuery, final ApiCallback _callback) throws ApiException {
        return fetchUploadStatusesCall(uploadStatusQuery, _callback);

    }

    /**
     * Retrieve Upload statuses in batch
     * Check the status of multiple **Uploads** (up to 100 per request).
     * @param uploadStatusQuery  (optional)
     * @return UploadStatuses
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
    public UploadStatuses fetchUploadStatuses(UploadStatusQuery uploadStatusQuery) throws ApiException {
        ApiResponse<UploadStatuses> localVarResp = fetchUploadStatusesWithHttpInfo(uploadStatusQuery);
        return localVarResp.getData();
    }

    /**
     * Retrieve Upload statuses in batch
     * Check the status of multiple **Uploads** (up to 100 per request).
     * @param uploadStatusQuery  (optional)
     * @return ApiResponse&lt;UploadStatuses&gt;
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
    public ApiResponse<UploadStatuses> fetchUploadStatusesWithHttpInfo(UploadStatusQuery uploadStatusQuery) throws ApiException {
        okhttp3.Call localVarCall = fetchUploadStatusesValidateBeforeCall(uploadStatusQuery, null);
        Type localVarReturnType = new TypeToken<UploadStatuses>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve Upload statuses in batch (asynchronously)
     * Check the status of multiple **Uploads** (up to 100 per request).
     * @param uploadStatusQuery  (optional)
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
    public okhttp3.Call fetchUploadStatusesAsync(UploadStatusQuery uploadStatusQuery, final ApiCallback<UploadStatuses> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchUploadStatusesValidateBeforeCall(uploadStatusQuery, _callback);
        Type localVarReturnType = new TypeToken<UploadStatuses>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postUpload
     * @param xRecipientEmail Email address associated with a Climate account, used when to sending to another user. (optional)
     * @param upload  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Returns a new upload with ID used to PUT file contents. </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call postUploadCall(String xRecipientEmail, Upload upload, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = upload;

        // create path and map variables
        String localVarPath = "/v4/uploads";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xRecipientEmail != null) {
            localVarHeaderParams.put("X-Recipient-Email", localVarApiClient.parameterToString(xRecipientEmail));
        }

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
    private okhttp3.Call postUploadValidateBeforeCall(String xRecipientEmail, Upload upload, final ApiCallback _callback) throws ApiException {
        return postUploadCall(xRecipientEmail, upload, _callback);

    }

    /**
     * Initiate a new upload
     * Step one in uploading a data product. The method will return an **Upload** ID which the caller will use in subsequent &#x60;PUT&#x60; requests. The following &#x60;contentTypes&#x60; may be uploaded:     &lt;details&gt;&lt;summary&gt;__image/vnd.climate.thermal.geotiff__&lt;/summary&gt;      Allows for the upload of a thermal image. The image is a single band geotiff with 64 bit signed floating point values in degrees Celsius. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt;__image/vnd.climate.ndvi.geotiff__&lt;/summary&gt;      Allows for the upload of a NDVI image. The image is a single band geotiff with 64 bit signed floating point values in the range of -1 to 1 inclusive. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __image/vnd.climate.rgb.geotiff__&lt;/summary&gt;      Allows for the upload of a true color image. The image is a multi band geotiff with 24-bit composite values. Each band is 8 bits with values in the range of 0 to 255. The Coordinate Reference System (CRS) must be UTM with WGS84 datum. The geotiff must contain 3 bands in the order Red, Green, Blue.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __image/vnd.climate.rgb-nir.geotiff__&lt;/summary&gt;      Allows for the upload of a Near Infrared (NIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt;__image/vnd.climate.rgb-cir.geotiff__&lt;/summary&gt;      Allows for the upload of a Color Infrared (CIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.rx.planting.shp__&lt;/summary&gt;      Allows for the upload of a planting prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      Requires either rx:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.prescription.zones.shp__&lt;/summary&gt;      Allows for the upload of a zones prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      The following metadata entries are required:       * fieldId - field identifier for prescription zones.          Requires either rxZones:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.modus.xml__&lt;/summary&gt;      Allows for the upload of a soil sampling file in the modus 1.0 format with some restrictions.  The upload must be a single xml file.      The following elements are required to be present in the modus file.       * EventCode - Max length of 64 bytes       * EventDate - Must be in ISO8601       * SoilSample - Has a maxOccurs of 20k       * Depth - Has a maxOccurs of 50       * LabName - Must be non-empty.       * StartingDepth - 0 to 36 inclusive, default 0       * EndingDepth - 1 - 36 inclusive, default 1       * ColumnDepth       * DepthUnit - must be inches       * Geometry - point in wgs84          Requires the soil:write scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.stand-count.geojson__&lt;/summary&gt;      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature&#39;s geometry field must be:       * Point      Requires &#x60;imagery:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.weed-count.geojson__&lt;/summary&gt;      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature&#39;s geometry field must be:       * Point      Requires &#x60;imagery:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-applied.zip__&lt;/summary&gt;      Allows for the upload of a valid application data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asApplied:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-planted.zip__&lt;/summary&gt;      Allows for the upload of a valid planting data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asPlanted:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-harvested.zip__&lt;/summary&gt;      Allows for the upload of a valid harvest data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asHarvested:write&#x60; scope.    &lt;/details&gt;
     * @param xRecipientEmail Email address associated with a Climate account, used when to sending to another user. (optional)
     * @param upload  (optional)
     * @return UUID
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Returns a new upload with ID used to PUT file contents. </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public UUID postUpload(String xRecipientEmail, Upload upload) throws ApiException {
        ApiResponse<UUID> localVarResp = postUploadWithHttpInfo(xRecipientEmail, upload);
        return localVarResp.getData();
    }

    /**
     * Initiate a new upload
     * Step one in uploading a data product. The method will return an **Upload** ID which the caller will use in subsequent &#x60;PUT&#x60; requests. The following &#x60;contentTypes&#x60; may be uploaded:     &lt;details&gt;&lt;summary&gt;__image/vnd.climate.thermal.geotiff__&lt;/summary&gt;      Allows for the upload of a thermal image. The image is a single band geotiff with 64 bit signed floating point values in degrees Celsius. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt;__image/vnd.climate.ndvi.geotiff__&lt;/summary&gt;      Allows for the upload of a NDVI image. The image is a single band geotiff with 64 bit signed floating point values in the range of -1 to 1 inclusive. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __image/vnd.climate.rgb.geotiff__&lt;/summary&gt;      Allows for the upload of a true color image. The image is a multi band geotiff with 24-bit composite values. Each band is 8 bits with values in the range of 0 to 255. The Coordinate Reference System (CRS) must be UTM with WGS84 datum. The geotiff must contain 3 bands in the order Red, Green, Blue.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __image/vnd.climate.rgb-nir.geotiff__&lt;/summary&gt;      Allows for the upload of a Near Infrared (NIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt;__image/vnd.climate.rgb-cir.geotiff__&lt;/summary&gt;      Allows for the upload of a Color Infrared (CIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.rx.planting.shp__&lt;/summary&gt;      Allows for the upload of a planting prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      Requires either rx:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.prescription.zones.shp__&lt;/summary&gt;      Allows for the upload of a zones prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      The following metadata entries are required:       * fieldId - field identifier for prescription zones.          Requires either rxZones:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.modus.xml__&lt;/summary&gt;      Allows for the upload of a soil sampling file in the modus 1.0 format with some restrictions.  The upload must be a single xml file.      The following elements are required to be present in the modus file.       * EventCode - Max length of 64 bytes       * EventDate - Must be in ISO8601       * SoilSample - Has a maxOccurs of 20k       * Depth - Has a maxOccurs of 50       * LabName - Must be non-empty.       * StartingDepth - 0 to 36 inclusive, default 0       * EndingDepth - 1 - 36 inclusive, default 1       * ColumnDepth       * DepthUnit - must be inches       * Geometry - point in wgs84          Requires the soil:write scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.stand-count.geojson__&lt;/summary&gt;      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature&#39;s geometry field must be:       * Point      Requires &#x60;imagery:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.weed-count.geojson__&lt;/summary&gt;      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature&#39;s geometry field must be:       * Point      Requires &#x60;imagery:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-applied.zip__&lt;/summary&gt;      Allows for the upload of a valid application data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asApplied:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-planted.zip__&lt;/summary&gt;      Allows for the upload of a valid planting data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asPlanted:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-harvested.zip__&lt;/summary&gt;      Allows for the upload of a valid harvest data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asHarvested:write&#x60; scope.    &lt;/details&gt;
     * @param xRecipientEmail Email address associated with a Climate account, used when to sending to another user. (optional)
     * @param upload  (optional)
     * @return ApiResponse&lt;UUID&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Returns a new upload with ID used to PUT file contents. </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public ApiResponse<UUID> postUploadWithHttpInfo(String xRecipientEmail, Upload upload) throws ApiException {
        okhttp3.Call localVarCall = postUploadValidateBeforeCall(xRecipientEmail, upload, null);
        Type localVarReturnType = new TypeToken<UUID>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Initiate a new upload (asynchronously)
     * Step one in uploading a data product. The method will return an **Upload** ID which the caller will use in subsequent &#x60;PUT&#x60; requests. The following &#x60;contentTypes&#x60; may be uploaded:     &lt;details&gt;&lt;summary&gt;__image/vnd.climate.thermal.geotiff__&lt;/summary&gt;      Allows for the upload of a thermal image. The image is a single band geotiff with 64 bit signed floating point values in degrees Celsius. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt;__image/vnd.climate.ndvi.geotiff__&lt;/summary&gt;      Allows for the upload of a NDVI image. The image is a single band geotiff with 64 bit signed floating point values in the range of -1 to 1 inclusive. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __image/vnd.climate.rgb.geotiff__&lt;/summary&gt;      Allows for the upload of a true color image. The image is a multi band geotiff with 24-bit composite values. Each band is 8 bits with values in the range of 0 to 255. The Coordinate Reference System (CRS) must be UTM with WGS84 datum. The geotiff must contain 3 bands in the order Red, Green, Blue.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __image/vnd.climate.rgb-nir.geotiff__&lt;/summary&gt;      Allows for the upload of a Near Infrared (NIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt;__image/vnd.climate.rgb-cir.geotiff__&lt;/summary&gt;      Allows for the upload of a Color Infrared (CIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.rx.planting.shp__&lt;/summary&gt;      Allows for the upload of a planting prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      Requires either rx:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.prescription.zones.shp__&lt;/summary&gt;      Allows for the upload of a zones prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      The following metadata entries are required:       * fieldId - field identifier for prescription zones.          Requires either rxZones:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.modus.xml__&lt;/summary&gt;      Allows for the upload of a soil sampling file in the modus 1.0 format with some restrictions.  The upload must be a single xml file.      The following elements are required to be present in the modus file.       * EventCode - Max length of 64 bytes       * EventDate - Must be in ISO8601       * SoilSample - Has a maxOccurs of 20k       * Depth - Has a maxOccurs of 50       * LabName - Must be non-empty.       * StartingDepth - 0 to 36 inclusive, default 0       * EndingDepth - 1 - 36 inclusive, default 1       * ColumnDepth       * DepthUnit - must be inches       * Geometry - point in wgs84          Requires the soil:write scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.stand-count.geojson__&lt;/summary&gt;      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature&#39;s geometry field must be:       * Point      Requires &#x60;imagery:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.weed-count.geojson__&lt;/summary&gt;      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature&#39;s geometry field must be:       * Point      Requires &#x60;imagery:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-applied.zip__&lt;/summary&gt;      Allows for the upload of a valid application data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asApplied:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-planted.zip__&lt;/summary&gt;      Allows for the upload of a valid planting data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asPlanted:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-harvested.zip__&lt;/summary&gt;      Allows for the upload of a valid harvest data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asHarvested:write&#x60; scope.    &lt;/details&gt;
     * @param xRecipientEmail Email address associated with a Climate account, used when to sending to another user. (optional)
     * @param upload  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Returns a new upload with ID used to PUT file contents. </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Input </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 403 </td><td> Forbidden </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 429 </td><td> Too Many Requests </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
        <tr><td> 503 </td><td> Server Busy </td><td>  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call postUploadAsync(String xRecipientEmail, Upload upload, final ApiCallback<UUID> _callback) throws ApiException {

        okhttp3.Call localVarCall = postUploadValidateBeforeCall(xRecipientEmail, upload, _callback);
        Type localVarReturnType = new TypeToken<UUID>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
