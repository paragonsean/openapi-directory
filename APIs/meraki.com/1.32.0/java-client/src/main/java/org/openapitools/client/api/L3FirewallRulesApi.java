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


import org.openapitools.client.model.UpdateNetworkApplianceFirewallInboundFirewallRulesRequest;
import org.openapitools.client.model.UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class L3FirewallRulesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public L3FirewallRulesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public L3FirewallRulesApi(ApiClient apiClient) {
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
     * Build call for getNetworkApplianceFirewallL3FirewallRules_2
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
    public okhttp3.Call getNetworkApplianceFirewallL3FirewallRules_2Call(String networkId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/appliance/firewall/l3FirewallRules"
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
    private okhttp3.Call getNetworkApplianceFirewallL3FirewallRules_2ValidateBeforeCall(String networkId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling getNetworkApplianceFirewallL3FirewallRules_2(Async)");
        }

        return getNetworkApplianceFirewallL3FirewallRules_2Call(networkId, _callback);

    }

    /**
     * Return the L3 firewall rules for an MX network
     * Return the L3 firewall rules for an MX network
     * @param networkId  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object getNetworkApplianceFirewallL3FirewallRules_2(String networkId) throws ApiException {
        ApiResponse<Object> localVarResp = getNetworkApplianceFirewallL3FirewallRules_2WithHttpInfo(networkId);
        return localVarResp.getData();
    }

    /**
     * Return the L3 firewall rules for an MX network
     * Return the L3 firewall rules for an MX network
     * @param networkId  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> getNetworkApplianceFirewallL3FirewallRules_2WithHttpInfo(String networkId) throws ApiException {
        okhttp3.Call localVarCall = getNetworkApplianceFirewallL3FirewallRules_2ValidateBeforeCall(networkId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return the L3 firewall rules for an MX network (asynchronously)
     * Return the L3 firewall rules for an MX network
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
    public okhttp3.Call getNetworkApplianceFirewallL3FirewallRules_2Async(String networkId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNetworkApplianceFirewallL3FirewallRules_2ValidateBeforeCall(networkId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNetworkWirelessSsidFirewallL3FirewallRules_3
     * @param networkId  (required)
     * @param number  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkWirelessSsidFirewallL3FirewallRules_3Call(String networkId, String number, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()))
            .replace("{" + "number" + "}", localVarApiClient.escapeString(number.toString()));

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
    private okhttp3.Call getNetworkWirelessSsidFirewallL3FirewallRules_3ValidateBeforeCall(String networkId, String number, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling getNetworkWirelessSsidFirewallL3FirewallRules_3(Async)");
        }

        // verify the required parameter 'number' is set
        if (number == null) {
            throw new ApiException("Missing the required parameter 'number' when calling getNetworkWirelessSsidFirewallL3FirewallRules_3(Async)");
        }

        return getNetworkWirelessSsidFirewallL3FirewallRules_3Call(networkId, number, _callback);

    }

    /**
     * Return the L3 firewall rules for an SSID on an MR network
     * Return the L3 firewall rules for an SSID on an MR network
     * @param networkId  (required)
     * @param number  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object getNetworkWirelessSsidFirewallL3FirewallRules_3(String networkId, String number) throws ApiException {
        ApiResponse<Object> localVarResp = getNetworkWirelessSsidFirewallL3FirewallRules_3WithHttpInfo(networkId, number);
        return localVarResp.getData();
    }

    /**
     * Return the L3 firewall rules for an SSID on an MR network
     * Return the L3 firewall rules for an SSID on an MR network
     * @param networkId  (required)
     * @param number  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> getNetworkWirelessSsidFirewallL3FirewallRules_3WithHttpInfo(String networkId, String number) throws ApiException {
        okhttp3.Call localVarCall = getNetworkWirelessSsidFirewallL3FirewallRules_3ValidateBeforeCall(networkId, number, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return the L3 firewall rules for an SSID on an MR network (asynchronously)
     * Return the L3 firewall rules for an SSID on an MR network
     * @param networkId  (required)
     * @param number  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkWirelessSsidFirewallL3FirewallRules_3Async(String networkId, String number, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNetworkWirelessSsidFirewallL3FirewallRules_3ValidateBeforeCall(networkId, number, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateNetworkApplianceFirewallL3FirewallRules_2
     * @param networkId  (required)
     * @param updateNetworkApplianceFirewallInboundFirewallRulesRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkApplianceFirewallL3FirewallRules_2Call(String networkId, UpdateNetworkApplianceFirewallInboundFirewallRulesRequest updateNetworkApplianceFirewallInboundFirewallRulesRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateNetworkApplianceFirewallInboundFirewallRulesRequest;

        // create path and map variables
        String localVarPath = "/networks/{networkId}/appliance/firewall/l3FirewallRules"
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
    private okhttp3.Call updateNetworkApplianceFirewallL3FirewallRules_2ValidateBeforeCall(String networkId, UpdateNetworkApplianceFirewallInboundFirewallRulesRequest updateNetworkApplianceFirewallInboundFirewallRulesRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling updateNetworkApplianceFirewallL3FirewallRules_2(Async)");
        }

        return updateNetworkApplianceFirewallL3FirewallRules_2Call(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest, _callback);

    }

    /**
     * Update the L3 firewall rules of an MX network
     * Update the L3 firewall rules of an MX network
     * @param networkId  (required)
     * @param updateNetworkApplianceFirewallInboundFirewallRulesRequest  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object updateNetworkApplianceFirewallL3FirewallRules_2(String networkId, UpdateNetworkApplianceFirewallInboundFirewallRulesRequest updateNetworkApplianceFirewallInboundFirewallRulesRequest) throws ApiException {
        ApiResponse<Object> localVarResp = updateNetworkApplianceFirewallL3FirewallRules_2WithHttpInfo(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest);
        return localVarResp.getData();
    }

    /**
     * Update the L3 firewall rules of an MX network
     * Update the L3 firewall rules of an MX network
     * @param networkId  (required)
     * @param updateNetworkApplianceFirewallInboundFirewallRulesRequest  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> updateNetworkApplianceFirewallL3FirewallRules_2WithHttpInfo(String networkId, UpdateNetworkApplianceFirewallInboundFirewallRulesRequest updateNetworkApplianceFirewallInboundFirewallRulesRequest) throws ApiException {
        okhttp3.Call localVarCall = updateNetworkApplianceFirewallL3FirewallRules_2ValidateBeforeCall(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update the L3 firewall rules of an MX network (asynchronously)
     * Update the L3 firewall rules of an MX network
     * @param networkId  (required)
     * @param updateNetworkApplianceFirewallInboundFirewallRulesRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkApplianceFirewallL3FirewallRules_2Async(String networkId, UpdateNetworkApplianceFirewallInboundFirewallRulesRequest updateNetworkApplianceFirewallInboundFirewallRulesRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateNetworkApplianceFirewallL3FirewallRules_2ValidateBeforeCall(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateNetworkWirelessSsidFirewallL3FirewallRules_3
     * @param networkId  (required)
     * @param number  (required)
     * @param updateNetworkWirelessSsidFirewallL3FirewallRulesRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkWirelessSsidFirewallL3FirewallRules_3Call(String networkId, String number, UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest updateNetworkWirelessSsidFirewallL3FirewallRulesRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateNetworkWirelessSsidFirewallL3FirewallRulesRequest;

        // create path and map variables
        String localVarPath = "/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()))
            .replace("{" + "number" + "}", localVarApiClient.escapeString(number.toString()));

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
    private okhttp3.Call updateNetworkWirelessSsidFirewallL3FirewallRules_3ValidateBeforeCall(String networkId, String number, UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest updateNetworkWirelessSsidFirewallL3FirewallRulesRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling updateNetworkWirelessSsidFirewallL3FirewallRules_3(Async)");
        }

        // verify the required parameter 'number' is set
        if (number == null) {
            throw new ApiException("Missing the required parameter 'number' when calling updateNetworkWirelessSsidFirewallL3FirewallRules_3(Async)");
        }

        return updateNetworkWirelessSsidFirewallL3FirewallRules_3Call(networkId, number, updateNetworkWirelessSsidFirewallL3FirewallRulesRequest, _callback);

    }

    /**
     * Update the L3 firewall rules of an SSID on an MR network
     * Update the L3 firewall rules of an SSID on an MR network
     * @param networkId  (required)
     * @param number  (required)
     * @param updateNetworkWirelessSsidFirewallL3FirewallRulesRequest  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object updateNetworkWirelessSsidFirewallL3FirewallRules_3(String networkId, String number, UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest updateNetworkWirelessSsidFirewallL3FirewallRulesRequest) throws ApiException {
        ApiResponse<Object> localVarResp = updateNetworkWirelessSsidFirewallL3FirewallRules_3WithHttpInfo(networkId, number, updateNetworkWirelessSsidFirewallL3FirewallRulesRequest);
        return localVarResp.getData();
    }

    /**
     * Update the L3 firewall rules of an SSID on an MR network
     * Update the L3 firewall rules of an SSID on an MR network
     * @param networkId  (required)
     * @param number  (required)
     * @param updateNetworkWirelessSsidFirewallL3FirewallRulesRequest  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> updateNetworkWirelessSsidFirewallL3FirewallRules_3WithHttpInfo(String networkId, String number, UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest updateNetworkWirelessSsidFirewallL3FirewallRulesRequest) throws ApiException {
        okhttp3.Call localVarCall = updateNetworkWirelessSsidFirewallL3FirewallRules_3ValidateBeforeCall(networkId, number, updateNetworkWirelessSsidFirewallL3FirewallRulesRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update the L3 firewall rules of an SSID on an MR network (asynchronously)
     * Update the L3 firewall rules of an SSID on an MR network
     * @param networkId  (required)
     * @param number  (required)
     * @param updateNetworkWirelessSsidFirewallL3FirewallRulesRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkWirelessSsidFirewallL3FirewallRules_3Async(String networkId, String number, UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest updateNetworkWirelessSsidFirewallL3FirewallRulesRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateNetworkWirelessSsidFirewallL3FirewallRules_3ValidateBeforeCall(networkId, number, updateNetworkWirelessSsidFirewallL3FirewallRulesRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
