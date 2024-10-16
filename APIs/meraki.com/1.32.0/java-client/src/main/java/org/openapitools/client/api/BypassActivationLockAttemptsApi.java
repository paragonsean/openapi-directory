/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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


import org.openapitools.client.model.CreateNetworkSmBypassActivationLockAttemptRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BypassActivationLockAttemptsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public BypassActivationLockAttemptsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public BypassActivationLockAttemptsApi(ApiClient apiClient) {
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
     * Build call for createNetworkSmBypassActivationLockAttempt_1
     * @param networkId  (required)
     * @param createNetworkSmBypassActivationLockAttemptRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createNetworkSmBypassActivationLockAttempt_1Call(String networkId, CreateNetworkSmBypassActivationLockAttemptRequest createNetworkSmBypassActivationLockAttemptRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createNetworkSmBypassActivationLockAttemptRequest;

        // create path and map variables
        String localVarPath = "/networks/{networkId}/sm/bypassActivationLockAttempts"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()));

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

        String[] localVarAuthNames = new String[] { "meraki_api_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createNetworkSmBypassActivationLockAttempt_1ValidateBeforeCall(String networkId, CreateNetworkSmBypassActivationLockAttemptRequest createNetworkSmBypassActivationLockAttemptRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling createNetworkSmBypassActivationLockAttempt_1(Async)");
        }

        // verify the required parameter 'createNetworkSmBypassActivationLockAttemptRequest' is set
        if (createNetworkSmBypassActivationLockAttemptRequest == null) {
            throw new ApiException("Missing the required parameter 'createNetworkSmBypassActivationLockAttemptRequest' when calling createNetworkSmBypassActivationLockAttempt_1(Async)");
        }

        return createNetworkSmBypassActivationLockAttempt_1Call(networkId, createNetworkSmBypassActivationLockAttemptRequest, _callback);

    }

    /**
     * Bypass activation lock attempt
     * Bypass activation lock attempt
     * @param networkId  (required)
     * @param createNetworkSmBypassActivationLockAttemptRequest  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object createNetworkSmBypassActivationLockAttempt_1(String networkId, CreateNetworkSmBypassActivationLockAttemptRequest createNetworkSmBypassActivationLockAttemptRequest) throws ApiException {
        ApiResponse<Object> localVarResp = createNetworkSmBypassActivationLockAttempt_1WithHttpInfo(networkId, createNetworkSmBypassActivationLockAttemptRequest);
        return localVarResp.getData();
    }

    /**
     * Bypass activation lock attempt
     * Bypass activation lock attempt
     * @param networkId  (required)
     * @param createNetworkSmBypassActivationLockAttemptRequest  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> createNetworkSmBypassActivationLockAttempt_1WithHttpInfo(String networkId, CreateNetworkSmBypassActivationLockAttemptRequest createNetworkSmBypassActivationLockAttemptRequest) throws ApiException {
        okhttp3.Call localVarCall = createNetworkSmBypassActivationLockAttempt_1ValidateBeforeCall(networkId, createNetworkSmBypassActivationLockAttemptRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Bypass activation lock attempt (asynchronously)
     * Bypass activation lock attempt
     * @param networkId  (required)
     * @param createNetworkSmBypassActivationLockAttemptRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createNetworkSmBypassActivationLockAttempt_1Async(String networkId, CreateNetworkSmBypassActivationLockAttemptRequest createNetworkSmBypassActivationLockAttemptRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = createNetworkSmBypassActivationLockAttempt_1ValidateBeforeCall(networkId, createNetworkSmBypassActivationLockAttemptRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNetworkSmBypassActivationLockAttempt_1
     * @param networkId  (required)
     * @param attemptId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkSmBypassActivationLockAttempt_1Call(String networkId, String attemptId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/sm/bypassActivationLockAttempts/{attemptId}"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()))
            .replace("{" + "attemptId" + "}", localVarApiClient.escapeString(attemptId.toString()));

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

        String[] localVarAuthNames = new String[] { "meraki_api_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getNetworkSmBypassActivationLockAttempt_1ValidateBeforeCall(String networkId, String attemptId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling getNetworkSmBypassActivationLockAttempt_1(Async)");
        }

        // verify the required parameter 'attemptId' is set
        if (attemptId == null) {
            throw new ApiException("Missing the required parameter 'attemptId' when calling getNetworkSmBypassActivationLockAttempt_1(Async)");
        }

        return getNetworkSmBypassActivationLockAttempt_1Call(networkId, attemptId, _callback);

    }

    /**
     * Bypass activation lock attempt status
     * Bypass activation lock attempt status
     * @param networkId  (required)
     * @param attemptId  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object getNetworkSmBypassActivationLockAttempt_1(String networkId, String attemptId) throws ApiException {
        ApiResponse<Object> localVarResp = getNetworkSmBypassActivationLockAttempt_1WithHttpInfo(networkId, attemptId);
        return localVarResp.getData();
    }

    /**
     * Bypass activation lock attempt status
     * Bypass activation lock attempt status
     * @param networkId  (required)
     * @param attemptId  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> getNetworkSmBypassActivationLockAttempt_1WithHttpInfo(String networkId, String attemptId) throws ApiException {
        okhttp3.Call localVarCall = getNetworkSmBypassActivationLockAttempt_1ValidateBeforeCall(networkId, attemptId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Bypass activation lock attempt status (asynchronously)
     * Bypass activation lock attempt status
     * @param networkId  (required)
     * @param attemptId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkSmBypassActivationLockAttempt_1Async(String networkId, String attemptId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNetworkSmBypassActivationLockAttempt_1ValidateBeforeCall(networkId, attemptId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
