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


import org.openapitools.client.model.UpdateNetworkClientSplashAuthorizationStatusRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SplashAuthorizationStatusApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SplashAuthorizationStatusApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SplashAuthorizationStatusApi(ApiClient apiClient) {
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
     * Build call for getNetworkClientSplashAuthorizationStatus_2
     * @param networkId  (required)
     * @param clientId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkClientSplashAuthorizationStatus_2Call(String networkId, String clientId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()))
            .replace("{" + "clientId" + "}", localVarApiClient.escapeString(clientId.toString()));

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
    private okhttp3.Call getNetworkClientSplashAuthorizationStatus_2ValidateBeforeCall(String networkId, String clientId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling getNetworkClientSplashAuthorizationStatus_2(Async)");
        }

        // verify the required parameter 'clientId' is set
        if (clientId == null) {
            throw new ApiException("Missing the required parameter 'clientId' when calling getNetworkClientSplashAuthorizationStatus_2(Async)");
        }

        return getNetworkClientSplashAuthorizationStatus_2Call(networkId, clientId, _callback);

    }

    /**
     * Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash
     * Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
     * @param networkId  (required)
     * @param clientId  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object getNetworkClientSplashAuthorizationStatus_2(String networkId, String clientId) throws ApiException {
        ApiResponse<Object> localVarResp = getNetworkClientSplashAuthorizationStatus_2WithHttpInfo(networkId, clientId);
        return localVarResp.getData();
    }

    /**
     * Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash
     * Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
     * @param networkId  (required)
     * @param clientId  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> getNetworkClientSplashAuthorizationStatus_2WithHttpInfo(String networkId, String clientId) throws ApiException {
        okhttp3.Call localVarCall = getNetworkClientSplashAuthorizationStatus_2ValidateBeforeCall(networkId, clientId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash (asynchronously)
     * Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
     * @param networkId  (required)
     * @param clientId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkClientSplashAuthorizationStatus_2Async(String networkId, String clientId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNetworkClientSplashAuthorizationStatus_2ValidateBeforeCall(networkId, clientId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateNetworkClientSplashAuthorizationStatus_2
     * @param networkId  (required)
     * @param clientId  (required)
     * @param updateNetworkClientSplashAuthorizationStatusRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkClientSplashAuthorizationStatus_2Call(String networkId, String clientId, UpdateNetworkClientSplashAuthorizationStatusRequest updateNetworkClientSplashAuthorizationStatusRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateNetworkClientSplashAuthorizationStatusRequest;

        // create path and map variables
        String localVarPath = "/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()))
            .replace("{" + "clientId" + "}", localVarApiClient.escapeString(clientId.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateNetworkClientSplashAuthorizationStatus_2ValidateBeforeCall(String networkId, String clientId, UpdateNetworkClientSplashAuthorizationStatusRequest updateNetworkClientSplashAuthorizationStatusRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling updateNetworkClientSplashAuthorizationStatus_2(Async)");
        }

        // verify the required parameter 'clientId' is set
        if (clientId == null) {
            throw new ApiException("Missing the required parameter 'clientId' when calling updateNetworkClientSplashAuthorizationStatus_2(Async)");
        }

        // verify the required parameter 'updateNetworkClientSplashAuthorizationStatusRequest' is set
        if (updateNetworkClientSplashAuthorizationStatusRequest == null) {
            throw new ApiException("Missing the required parameter 'updateNetworkClientSplashAuthorizationStatusRequest' when calling updateNetworkClientSplashAuthorizationStatus_2(Async)");
        }

        return updateNetworkClientSplashAuthorizationStatus_2Call(networkId, clientId, updateNetworkClientSplashAuthorizationStatusRequest, _callback);

    }

    /**
     * Update a client&#39;s splash authorization
     * Update a client&#39;s splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
     * @param networkId  (required)
     * @param clientId  (required)
     * @param updateNetworkClientSplashAuthorizationStatusRequest  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object updateNetworkClientSplashAuthorizationStatus_2(String networkId, String clientId, UpdateNetworkClientSplashAuthorizationStatusRequest updateNetworkClientSplashAuthorizationStatusRequest) throws ApiException {
        ApiResponse<Object> localVarResp = updateNetworkClientSplashAuthorizationStatus_2WithHttpInfo(networkId, clientId, updateNetworkClientSplashAuthorizationStatusRequest);
        return localVarResp.getData();
    }

    /**
     * Update a client&#39;s splash authorization
     * Update a client&#39;s splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
     * @param networkId  (required)
     * @param clientId  (required)
     * @param updateNetworkClientSplashAuthorizationStatusRequest  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> updateNetworkClientSplashAuthorizationStatus_2WithHttpInfo(String networkId, String clientId, UpdateNetworkClientSplashAuthorizationStatusRequest updateNetworkClientSplashAuthorizationStatusRequest) throws ApiException {
        okhttp3.Call localVarCall = updateNetworkClientSplashAuthorizationStatus_2ValidateBeforeCall(networkId, clientId, updateNetworkClientSplashAuthorizationStatusRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update a client&#39;s splash authorization (asynchronously)
     * Update a client&#39;s splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
     * @param networkId  (required)
     * @param clientId  (required)
     * @param updateNetworkClientSplashAuthorizationStatusRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkClientSplashAuthorizationStatus_2Async(String networkId, String clientId, UpdateNetworkClientSplashAuthorizationStatusRequest updateNetworkClientSplashAuthorizationStatusRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateNetworkClientSplashAuthorizationStatus_2ValidateBeforeCall(networkId, clientId, updateNetworkClientSplashAuthorizationStatusRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
