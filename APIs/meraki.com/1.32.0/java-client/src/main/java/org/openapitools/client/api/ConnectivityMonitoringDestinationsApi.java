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


import org.openapitools.client.model.UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest;
import org.openapitools.client.model.UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ConnectivityMonitoringDestinationsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ConnectivityMonitoringDestinationsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ConnectivityMonitoringDestinationsApi(ApiClient apiClient) {
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
     * Build call for getNetworkApplianceConnectivityMonitoringDestinations_1
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
    public okhttp3.Call getNetworkApplianceConnectivityMonitoringDestinations_1Call(String networkId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/appliance/connectivityMonitoringDestinations"
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
    private okhttp3.Call getNetworkApplianceConnectivityMonitoringDestinations_1ValidateBeforeCall(String networkId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling getNetworkApplianceConnectivityMonitoringDestinations_1(Async)");
        }

        return getNetworkApplianceConnectivityMonitoringDestinations_1Call(networkId, _callback);

    }

    /**
     * Return the connectivity testing destinations for an MX network
     * Return the connectivity testing destinations for an MX network
     * @param networkId  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object getNetworkApplianceConnectivityMonitoringDestinations_1(String networkId) throws ApiException {
        ApiResponse<Object> localVarResp = getNetworkApplianceConnectivityMonitoringDestinations_1WithHttpInfo(networkId);
        return localVarResp.getData();
    }

    /**
     * Return the connectivity testing destinations for an MX network
     * Return the connectivity testing destinations for an MX network
     * @param networkId  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> getNetworkApplianceConnectivityMonitoringDestinations_1WithHttpInfo(String networkId) throws ApiException {
        okhttp3.Call localVarCall = getNetworkApplianceConnectivityMonitoringDestinations_1ValidateBeforeCall(networkId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return the connectivity testing destinations for an MX network (asynchronously)
     * Return the connectivity testing destinations for an MX network
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
    public okhttp3.Call getNetworkApplianceConnectivityMonitoringDestinations_1Async(String networkId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNetworkApplianceConnectivityMonitoringDestinations_1ValidateBeforeCall(networkId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNetworkCellularGatewayConnectivityMonitoringDestinations_1
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
    public okhttp3.Call getNetworkCellularGatewayConnectivityMonitoringDestinations_1Call(String networkId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations"
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
    private okhttp3.Call getNetworkCellularGatewayConnectivityMonitoringDestinations_1ValidateBeforeCall(String networkId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling getNetworkCellularGatewayConnectivityMonitoringDestinations_1(Async)");
        }

        return getNetworkCellularGatewayConnectivityMonitoringDestinations_1Call(networkId, _callback);

    }

    /**
     * Return the connectivity testing destinations for an MG network
     * Return the connectivity testing destinations for an MG network
     * @param networkId  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object getNetworkCellularGatewayConnectivityMonitoringDestinations_1(String networkId) throws ApiException {
        ApiResponse<Object> localVarResp = getNetworkCellularGatewayConnectivityMonitoringDestinations_1WithHttpInfo(networkId);
        return localVarResp.getData();
    }

    /**
     * Return the connectivity testing destinations for an MG network
     * Return the connectivity testing destinations for an MG network
     * @param networkId  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> getNetworkCellularGatewayConnectivityMonitoringDestinations_1WithHttpInfo(String networkId) throws ApiException {
        okhttp3.Call localVarCall = getNetworkCellularGatewayConnectivityMonitoringDestinations_1ValidateBeforeCall(networkId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return the connectivity testing destinations for an MG network (asynchronously)
     * Return the connectivity testing destinations for an MG network
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
    public okhttp3.Call getNetworkCellularGatewayConnectivityMonitoringDestinations_1Async(String networkId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNetworkCellularGatewayConnectivityMonitoringDestinations_1ValidateBeforeCall(networkId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateNetworkApplianceConnectivityMonitoringDestinations_1
     * @param networkId  (required)
     * @param updateNetworkApplianceConnectivityMonitoringDestinationsRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkApplianceConnectivityMonitoringDestinations_1Call(String networkId, UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest updateNetworkApplianceConnectivityMonitoringDestinationsRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateNetworkApplianceConnectivityMonitoringDestinationsRequest;

        // create path and map variables
        String localVarPath = "/networks/{networkId}/appliance/connectivityMonitoringDestinations"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateNetworkApplianceConnectivityMonitoringDestinations_1ValidateBeforeCall(String networkId, UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest updateNetworkApplianceConnectivityMonitoringDestinationsRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling updateNetworkApplianceConnectivityMonitoringDestinations_1(Async)");
        }

        return updateNetworkApplianceConnectivityMonitoringDestinations_1Call(networkId, updateNetworkApplianceConnectivityMonitoringDestinationsRequest, _callback);

    }

    /**
     * Update the connectivity testing destinations for an MX network
     * Update the connectivity testing destinations for an MX network
     * @param networkId  (required)
     * @param updateNetworkApplianceConnectivityMonitoringDestinationsRequest  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object updateNetworkApplianceConnectivityMonitoringDestinations_1(String networkId, UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest updateNetworkApplianceConnectivityMonitoringDestinationsRequest) throws ApiException {
        ApiResponse<Object> localVarResp = updateNetworkApplianceConnectivityMonitoringDestinations_1WithHttpInfo(networkId, updateNetworkApplianceConnectivityMonitoringDestinationsRequest);
        return localVarResp.getData();
    }

    /**
     * Update the connectivity testing destinations for an MX network
     * Update the connectivity testing destinations for an MX network
     * @param networkId  (required)
     * @param updateNetworkApplianceConnectivityMonitoringDestinationsRequest  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> updateNetworkApplianceConnectivityMonitoringDestinations_1WithHttpInfo(String networkId, UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest updateNetworkApplianceConnectivityMonitoringDestinationsRequest) throws ApiException {
        okhttp3.Call localVarCall = updateNetworkApplianceConnectivityMonitoringDestinations_1ValidateBeforeCall(networkId, updateNetworkApplianceConnectivityMonitoringDestinationsRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update the connectivity testing destinations for an MX network (asynchronously)
     * Update the connectivity testing destinations for an MX network
     * @param networkId  (required)
     * @param updateNetworkApplianceConnectivityMonitoringDestinationsRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkApplianceConnectivityMonitoringDestinations_1Async(String networkId, UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest updateNetworkApplianceConnectivityMonitoringDestinationsRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateNetworkApplianceConnectivityMonitoringDestinations_1ValidateBeforeCall(networkId, updateNetworkApplianceConnectivityMonitoringDestinationsRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateNetworkCellularGatewayConnectivityMonitoringDestinations_1
     * @param networkId  (required)
     * @param updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkCellularGatewayConnectivityMonitoringDestinations_1Call(String networkId, UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest;

        // create path and map variables
        String localVarPath = "/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateNetworkCellularGatewayConnectivityMonitoringDestinations_1ValidateBeforeCall(String networkId, UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling updateNetworkCellularGatewayConnectivityMonitoringDestinations_1(Async)");
        }

        return updateNetworkCellularGatewayConnectivityMonitoringDestinations_1Call(networkId, updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest, _callback);

    }

    /**
     * Update the connectivity testing destinations for an MG network
     * Update the connectivity testing destinations for an MG network
     * @param networkId  (required)
     * @param updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object updateNetworkCellularGatewayConnectivityMonitoringDestinations_1(String networkId, UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest) throws ApiException {
        ApiResponse<Object> localVarResp = updateNetworkCellularGatewayConnectivityMonitoringDestinations_1WithHttpInfo(networkId, updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest);
        return localVarResp.getData();
    }

    /**
     * Update the connectivity testing destinations for an MG network
     * Update the connectivity testing destinations for an MG network
     * @param networkId  (required)
     * @param updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> updateNetworkCellularGatewayConnectivityMonitoringDestinations_1WithHttpInfo(String networkId, UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest) throws ApiException {
        okhttp3.Call localVarCall = updateNetworkCellularGatewayConnectivityMonitoringDestinations_1ValidateBeforeCall(networkId, updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update the connectivity testing destinations for an MG network (asynchronously)
     * Update the connectivity testing destinations for an MG network
     * @param networkId  (required)
     * @param updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkCellularGatewayConnectivityMonitoringDestinations_1Async(String networkId, UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateNetworkCellularGatewayConnectivityMonitoringDestinations_1ValidateBeforeCall(networkId, updateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
