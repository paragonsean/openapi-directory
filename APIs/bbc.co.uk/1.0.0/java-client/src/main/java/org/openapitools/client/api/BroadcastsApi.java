/*
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
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


import org.openapitools.client.model.BroadcastsResponse;
import org.openapitools.client.model.ErrorResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BroadcastsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public BroadcastsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public BroadcastsApi(ApiClient apiClient) {
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
     * Build call for broadcastsGet
     * @param xAPIKey API_KEY (required)
     * @param offset Paginated results offset (optional)
     * @param limit Paginated results limit (optional)
     * @param serviceId Filter by Service ID. E.g. bbc_radio_fourfm (optional)
     * @param date Filter by date. E.g. 2016-06-17 (optional)
     * @param sort Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> There was an error with the supplied &#x60;Authorization&#x60; header. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call broadcastsGetCall(String xAPIKey, Integer offset, Integer limit, String serviceId, String date, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/broadcasts";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
        }

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (serviceId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("service_id", serviceId));
        }

        if (date != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("date", date));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (xAPIKey != null) {
            localVarHeaderParams.put("X-API-Key", localVarApiClient.parameterToString(xAPIKey));
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call broadcastsGetValidateBeforeCall(String xAPIKey, Integer offset, Integer limit, String serviceId, String date, String sort, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAPIKey' is set
        if (xAPIKey == null) {
            throw new ApiException("Missing the required parameter 'xAPIKey' when calling broadcastsGet(Async)");
        }

        return broadcastsGetCall(xAPIKey, offset, limit, serviceId, date, sort, _callback);

    }

    /**
     * Broadcasts
     * All broadcasts 
     * @param xAPIKey API_KEY (required)
     * @param offset Paginated results offset (optional)
     * @param limit Paginated results limit (optional)
     * @param serviceId Filter by Service ID. E.g. bbc_radio_fourfm (optional)
     * @param date Filter by date. E.g. 2016-06-17 (optional)
     * @param sort Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order (optional)
     * @return BroadcastsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> There was an error with the supplied &#x60;Authorization&#x60; header. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public BroadcastsResponse broadcastsGet(String xAPIKey, Integer offset, Integer limit, String serviceId, String date, String sort) throws ApiException {
        ApiResponse<BroadcastsResponse> localVarResp = broadcastsGetWithHttpInfo(xAPIKey, offset, limit, serviceId, date, sort);
        return localVarResp.getData();
    }

    /**
     * Broadcasts
     * All broadcasts 
     * @param xAPIKey API_KEY (required)
     * @param offset Paginated results offset (optional)
     * @param limit Paginated results limit (optional)
     * @param serviceId Filter by Service ID. E.g. bbc_radio_fourfm (optional)
     * @param date Filter by date. E.g. 2016-06-17 (optional)
     * @param sort Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order (optional)
     * @return ApiResponse&lt;BroadcastsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> There was an error with the supplied &#x60;Authorization&#x60; header. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BroadcastsResponse> broadcastsGetWithHttpInfo(String xAPIKey, Integer offset, Integer limit, String serviceId, String date, String sort) throws ApiException {
        okhttp3.Call localVarCall = broadcastsGetValidateBeforeCall(xAPIKey, offset, limit, serviceId, date, sort, null);
        Type localVarReturnType = new TypeToken<BroadcastsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Broadcasts (asynchronously)
     * All broadcasts 
     * @param xAPIKey API_KEY (required)
     * @param offset Paginated results offset (optional)
     * @param limit Paginated results limit (optional)
     * @param serviceId Filter by Service ID. E.g. bbc_radio_fourfm (optional)
     * @param date Filter by date. E.g. 2016-06-17 (optional)
     * @param sort Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> There was an error with the supplied &#x60;Authorization&#x60; header. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call broadcastsGetAsync(String xAPIKey, Integer offset, Integer limit, String serviceId, String date, String sort, final ApiCallback<BroadcastsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = broadcastsGetValidateBeforeCall(xAPIKey, offset, limit, serviceId, date, sort, _callback);
        Type localVarReturnType = new TypeToken<BroadcastsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for broadcastsLatestGet
     * @param xAPIKey API_KEY (required)
     * @param offset Paginated results offset (optional)
     * @param limit Paginated results limit (optional)
     * @param serviceId Filter by Service ID. E.g. bbc_radio_fourfm (optional)
     * @param onAir Filter what is on air. E.g. &#39;now&#39; returns current programme being broadcasted. (optional)
     * @param next Filter what will be on air next in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the next four hurs (optional)
     * @param previous Filter what was on air previously in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the previous four hurs (optional)
     * @param sort Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> There was an error with the supplied &#x60;Authorization&#x60; header. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call broadcastsLatestGetCall(String xAPIKey, Integer offset, Integer limit, String serviceId, String onAir, String next, String previous, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/broadcasts/latest";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
        }

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (serviceId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("service_id", serviceId));
        }

        if (onAir != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("on_air", onAir));
        }

        if (next != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("next", next));
        }

        if (previous != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("previous", previous));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (xAPIKey != null) {
            localVarHeaderParams.put("X-API-Key", localVarApiClient.parameterToString(xAPIKey));
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call broadcastsLatestGetValidateBeforeCall(String xAPIKey, Integer offset, Integer limit, String serviceId, String onAir, String next, String previous, String sort, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAPIKey' is set
        if (xAPIKey == null) {
            throw new ApiException("Missing the required parameter 'xAPIKey' when calling broadcastsLatestGet(Async)");
        }

        return broadcastsLatestGetCall(xAPIKey, offset, limit, serviceId, onAir, next, previous, sort, _callback);

    }

    /**
     * Latest Broadcasts
     * Broadcasts for the current day 
     * @param xAPIKey API_KEY (required)
     * @param offset Paginated results offset (optional)
     * @param limit Paginated results limit (optional)
     * @param serviceId Filter by Service ID. E.g. bbc_radio_fourfm (optional)
     * @param onAir Filter what is on air. E.g. &#39;now&#39; returns current programme being broadcasted. (optional)
     * @param next Filter what will be on air next in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the next four hurs (optional)
     * @param previous Filter what was on air previously in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the previous four hurs (optional)
     * @param sort Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order (optional)
     * @return BroadcastsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> There was an error with the supplied &#x60;Authorization&#x60; header. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public BroadcastsResponse broadcastsLatestGet(String xAPIKey, Integer offset, Integer limit, String serviceId, String onAir, String next, String previous, String sort) throws ApiException {
        ApiResponse<BroadcastsResponse> localVarResp = broadcastsLatestGetWithHttpInfo(xAPIKey, offset, limit, serviceId, onAir, next, previous, sort);
        return localVarResp.getData();
    }

    /**
     * Latest Broadcasts
     * Broadcasts for the current day 
     * @param xAPIKey API_KEY (required)
     * @param offset Paginated results offset (optional)
     * @param limit Paginated results limit (optional)
     * @param serviceId Filter by Service ID. E.g. bbc_radio_fourfm (optional)
     * @param onAir Filter what is on air. E.g. &#39;now&#39; returns current programme being broadcasted. (optional)
     * @param next Filter what will be on air next in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the next four hurs (optional)
     * @param previous Filter what was on air previously in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the previous four hurs (optional)
     * @param sort Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order (optional)
     * @return ApiResponse&lt;BroadcastsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> There was an error with the supplied &#x60;Authorization&#x60; header. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BroadcastsResponse> broadcastsLatestGetWithHttpInfo(String xAPIKey, Integer offset, Integer limit, String serviceId, String onAir, String next, String previous, String sort) throws ApiException {
        okhttp3.Call localVarCall = broadcastsLatestGetValidateBeforeCall(xAPIKey, offset, limit, serviceId, onAir, next, previous, sort, null);
        Type localVarReturnType = new TypeToken<BroadcastsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Latest Broadcasts (asynchronously)
     * Broadcasts for the current day 
     * @param xAPIKey API_KEY (required)
     * @param offset Paginated results offset (optional)
     * @param limit Paginated results limit (optional)
     * @param serviceId Filter by Service ID. E.g. bbc_radio_fourfm (optional)
     * @param onAir Filter what is on air. E.g. &#39;now&#39; returns current programme being broadcasted. (optional)
     * @param next Filter what will be on air next in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the next four hurs (optional)
     * @param previous Filter what was on air previously in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the previous four hurs (optional)
     * @param sort Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> There was an error with the supplied &#x60;Authorization&#x60; header. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call broadcastsLatestGetAsync(String xAPIKey, Integer offset, Integer limit, String serviceId, String onAir, String next, String previous, String sort, final ApiCallback<BroadcastsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = broadcastsLatestGetValidateBeforeCall(xAPIKey, offset, limit, serviceId, onAir, next, previous, sort, _callback);
        Type localVarReturnType = new TypeToken<BroadcastsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getBroadcastByPid
     * @param xAPIKey API_KEY (required)
     * @param pid pid (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> There was an error with the supplied &#x60;Authorization&#x60; header. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBroadcastByPidCall(String xAPIKey, String pid, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/broadcasts/{pid}"
            .replace("{" + "pid" + "}", localVarApiClient.escapeString(pid.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAPIKey != null) {
            localVarHeaderParams.put("X-API-Key", localVarApiClient.parameterToString(xAPIKey));
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getBroadcastByPidValidateBeforeCall(String xAPIKey, String pid, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAPIKey' is set
        if (xAPIKey == null) {
            throw new ApiException("Missing the required parameter 'xAPIKey' when calling getBroadcastByPid(Async)");
        }

        // verify the required parameter 'pid' is set
        if (pid == null) {
            throw new ApiException("Missing the required parameter 'pid' when calling getBroadcastByPid(Async)");
        }

        return getBroadcastByPidCall(xAPIKey, pid, _callback);

    }

    /**
     * Broadcasts by PID
     * Find broadcast by PID 
     * @param xAPIKey API_KEY (required)
     * @param pid pid (required)
     * @return BroadcastsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> There was an error with the supplied &#x60;Authorization&#x60; header. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public BroadcastsResponse getBroadcastByPid(String xAPIKey, String pid) throws ApiException {
        ApiResponse<BroadcastsResponse> localVarResp = getBroadcastByPidWithHttpInfo(xAPIKey, pid);
        return localVarResp.getData();
    }

    /**
     * Broadcasts by PID
     * Find broadcast by PID 
     * @param xAPIKey API_KEY (required)
     * @param pid pid (required)
     * @return ApiResponse&lt;BroadcastsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> There was an error with the supplied &#x60;Authorization&#x60; header. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BroadcastsResponse> getBroadcastByPidWithHttpInfo(String xAPIKey, String pid) throws ApiException {
        okhttp3.Call localVarCall = getBroadcastByPidValidateBeforeCall(xAPIKey, pid, null);
        Type localVarReturnType = new TypeToken<BroadcastsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Broadcasts by PID (asynchronously)
     * Find broadcast by PID 
     * @param xAPIKey API_KEY (required)
     * @param pid pid (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> There was an error with the supplied &#x60;Authorization&#x60; header. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBroadcastByPidAsync(String xAPIKey, String pid, final ApiCallback<BroadcastsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getBroadcastByPidValidateBeforeCall(xAPIKey, pid, _callback);
        Type localVarReturnType = new TypeToken<BroadcastsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
