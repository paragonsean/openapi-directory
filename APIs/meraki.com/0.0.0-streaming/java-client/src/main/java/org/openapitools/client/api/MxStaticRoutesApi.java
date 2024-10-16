/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
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


import org.openapitools.client.model.CreateNetworkStaticRouteRequest;
import org.openapitools.client.model.UpdateNetworkStaticRouteRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MxStaticRoutesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public MxStaticRoutesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public MxStaticRoutesApi(ApiClient apiClient) {
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
     * Build call for createNetworkStaticRoute
     * @param networkId  (required)
     * @param createNetworkStaticRouteRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createNetworkStaticRouteCall(String networkId, CreateNetworkStaticRouteRequest createNetworkStaticRouteRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createNetworkStaticRouteRequest;

        // create path and map variables
        String localVarPath = "/networks/{networkId}/staticRoutes"
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
    private okhttp3.Call createNetworkStaticRouteValidateBeforeCall(String networkId, CreateNetworkStaticRouteRequest createNetworkStaticRouteRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling createNetworkStaticRoute(Async)");
        }

        // verify the required parameter 'createNetworkStaticRouteRequest' is set
        if (createNetworkStaticRouteRequest == null) {
            throw new ApiException("Missing the required parameter 'createNetworkStaticRouteRequest' when calling createNetworkStaticRoute(Async)");
        }

        return createNetworkStaticRouteCall(networkId, createNetworkStaticRouteRequest, _callback);

    }

    /**
     * Add a static route for an MX or teleworker network
     * Add a static route for an MX or teleworker network
     * @param networkId  (required)
     * @param createNetworkStaticRouteRequest  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object createNetworkStaticRoute(String networkId, CreateNetworkStaticRouteRequest createNetworkStaticRouteRequest) throws ApiException {
        ApiResponse<Object> localVarResp = createNetworkStaticRouteWithHttpInfo(networkId, createNetworkStaticRouteRequest);
        return localVarResp.getData();
    }

    /**
     * Add a static route for an MX or teleworker network
     * Add a static route for an MX or teleworker network
     * @param networkId  (required)
     * @param createNetworkStaticRouteRequest  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> createNetworkStaticRouteWithHttpInfo(String networkId, CreateNetworkStaticRouteRequest createNetworkStaticRouteRequest) throws ApiException {
        okhttp3.Call localVarCall = createNetworkStaticRouteValidateBeforeCall(networkId, createNetworkStaticRouteRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add a static route for an MX or teleworker network (asynchronously)
     * Add a static route for an MX or teleworker network
     * @param networkId  (required)
     * @param createNetworkStaticRouteRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createNetworkStaticRouteAsync(String networkId, CreateNetworkStaticRouteRequest createNetworkStaticRouteRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = createNetworkStaticRouteValidateBeforeCall(networkId, createNetworkStaticRouteRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteNetworkStaticRoute
     * @param networkId  (required)
     * @param staticRouteId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteNetworkStaticRouteCall(String networkId, String staticRouteId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/staticRoutes/{staticRouteId}"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()))
            .replace("{" + "staticRouteId" + "}", localVarApiClient.escapeString(staticRouteId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteNetworkStaticRouteValidateBeforeCall(String networkId, String staticRouteId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling deleteNetworkStaticRoute(Async)");
        }

        // verify the required parameter 'staticRouteId' is set
        if (staticRouteId == null) {
            throw new ApiException("Missing the required parameter 'staticRouteId' when calling deleteNetworkStaticRoute(Async)");
        }

        return deleteNetworkStaticRouteCall(networkId, staticRouteId, _callback);

    }

    /**
     * Delete a static route from an MX or teleworker network
     * Delete a static route from an MX or teleworker network
     * @param networkId  (required)
     * @param staticRouteId  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void deleteNetworkStaticRoute(String networkId, String staticRouteId) throws ApiException {
        deleteNetworkStaticRouteWithHttpInfo(networkId, staticRouteId);
    }

    /**
     * Delete a static route from an MX or teleworker network
     * Delete a static route from an MX or teleworker network
     * @param networkId  (required)
     * @param staticRouteId  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteNetworkStaticRouteWithHttpInfo(String networkId, String staticRouteId) throws ApiException {
        okhttp3.Call localVarCall = deleteNetworkStaticRouteValidateBeforeCall(networkId, staticRouteId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a static route from an MX or teleworker network (asynchronously)
     * Delete a static route from an MX or teleworker network
     * @param networkId  (required)
     * @param staticRouteId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteNetworkStaticRouteAsync(String networkId, String staticRouteId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteNetworkStaticRouteValidateBeforeCall(networkId, staticRouteId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNetworkStaticRoute
     * @param networkId  (required)
     * @param staticRouteId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkStaticRouteCall(String networkId, String staticRouteId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/staticRoutes/{staticRouteId}"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()))
            .replace("{" + "staticRouteId" + "}", localVarApiClient.escapeString(staticRouteId.toString()));

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
    private okhttp3.Call getNetworkStaticRouteValidateBeforeCall(String networkId, String staticRouteId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling getNetworkStaticRoute(Async)");
        }

        // verify the required parameter 'staticRouteId' is set
        if (staticRouteId == null) {
            throw new ApiException("Missing the required parameter 'staticRouteId' when calling getNetworkStaticRoute(Async)");
        }

        return getNetworkStaticRouteCall(networkId, staticRouteId, _callback);

    }

    /**
     * Return a static route for an MX or teleworker network
     * Return a static route for an MX or teleworker network
     * @param networkId  (required)
     * @param staticRouteId  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object getNetworkStaticRoute(String networkId, String staticRouteId) throws ApiException {
        ApiResponse<Object> localVarResp = getNetworkStaticRouteWithHttpInfo(networkId, staticRouteId);
        return localVarResp.getData();
    }

    /**
     * Return a static route for an MX or teleworker network
     * Return a static route for an MX or teleworker network
     * @param networkId  (required)
     * @param staticRouteId  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> getNetworkStaticRouteWithHttpInfo(String networkId, String staticRouteId) throws ApiException {
        okhttp3.Call localVarCall = getNetworkStaticRouteValidateBeforeCall(networkId, staticRouteId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return a static route for an MX or teleworker network (asynchronously)
     * Return a static route for an MX or teleworker network
     * @param networkId  (required)
     * @param staticRouteId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkStaticRouteAsync(String networkId, String staticRouteId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNetworkStaticRouteValidateBeforeCall(networkId, staticRouteId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNetworkStaticRoutes
     * @param networkId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkStaticRoutesCall(String networkId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/staticRoutes"
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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "meraki_api_key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getNetworkStaticRoutesValidateBeforeCall(String networkId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling getNetworkStaticRoutes(Async)");
        }

        return getNetworkStaticRoutesCall(networkId, _callback);

    }

    /**
     * List the static routes for an MX or teleworker network
     * List the static routes for an MX or teleworker network
     * @param networkId  (required)
     * @return List&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public List<Object> getNetworkStaticRoutes(String networkId) throws ApiException {
        ApiResponse<List<Object>> localVarResp = getNetworkStaticRoutesWithHttpInfo(networkId);
        return localVarResp.getData();
    }

    /**
     * List the static routes for an MX or teleworker network
     * List the static routes for an MX or teleworker network
     * @param networkId  (required)
     * @return ApiResponse&lt;List&lt;Object&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Object>> getNetworkStaticRoutesWithHttpInfo(String networkId) throws ApiException {
        okhttp3.Call localVarCall = getNetworkStaticRoutesValidateBeforeCall(networkId, null);
        Type localVarReturnType = new TypeToken<List<Object>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List the static routes for an MX or teleworker network (asynchronously)
     * List the static routes for an MX or teleworker network
     * @param networkId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkStaticRoutesAsync(String networkId, final ApiCallback<List<Object>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNetworkStaticRoutesValidateBeforeCall(networkId, _callback);
        Type localVarReturnType = new TypeToken<List<Object>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateNetworkStaticRoute
     * @param networkId  (required)
     * @param staticRouteId  (required)
     * @param updateNetworkStaticRouteRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkStaticRouteCall(String networkId, String staticRouteId, UpdateNetworkStaticRouteRequest updateNetworkStaticRouteRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateNetworkStaticRouteRequest;

        // create path and map variables
        String localVarPath = "/networks/{networkId}/staticRoutes/{staticRouteId}"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()))
            .replace("{" + "staticRouteId" + "}", localVarApiClient.escapeString(staticRouteId.toString()));

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
    private okhttp3.Call updateNetworkStaticRouteValidateBeforeCall(String networkId, String staticRouteId, UpdateNetworkStaticRouteRequest updateNetworkStaticRouteRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling updateNetworkStaticRoute(Async)");
        }

        // verify the required parameter 'staticRouteId' is set
        if (staticRouteId == null) {
            throw new ApiException("Missing the required parameter 'staticRouteId' when calling updateNetworkStaticRoute(Async)");
        }

        return updateNetworkStaticRouteCall(networkId, staticRouteId, updateNetworkStaticRouteRequest, _callback);

    }

    /**
     * Update a static route for an MX or teleworker network
     * Update a static route for an MX or teleworker network
     * @param networkId  (required)
     * @param staticRouteId  (required)
     * @param updateNetworkStaticRouteRequest  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object updateNetworkStaticRoute(String networkId, String staticRouteId, UpdateNetworkStaticRouteRequest updateNetworkStaticRouteRequest) throws ApiException {
        ApiResponse<Object> localVarResp = updateNetworkStaticRouteWithHttpInfo(networkId, staticRouteId, updateNetworkStaticRouteRequest);
        return localVarResp.getData();
    }

    /**
     * Update a static route for an MX or teleworker network
     * Update a static route for an MX or teleworker network
     * @param networkId  (required)
     * @param staticRouteId  (required)
     * @param updateNetworkStaticRouteRequest  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> updateNetworkStaticRouteWithHttpInfo(String networkId, String staticRouteId, UpdateNetworkStaticRouteRequest updateNetworkStaticRouteRequest) throws ApiException {
        okhttp3.Call localVarCall = updateNetworkStaticRouteValidateBeforeCall(networkId, staticRouteId, updateNetworkStaticRouteRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update a static route for an MX or teleworker network (asynchronously)
     * Update a static route for an MX or teleworker network
     * @param networkId  (required)
     * @param staticRouteId  (required)
     * @param updateNetworkStaticRouteRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkStaticRouteAsync(String networkId, String staticRouteId, UpdateNetworkStaticRouteRequest updateNetworkStaticRouteRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateNetworkStaticRouteValidateBeforeCall(networkId, staticRouteId, updateNetworkStaticRouteRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
