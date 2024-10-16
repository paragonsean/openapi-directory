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


import org.openapitools.client.model.GetNetworkSwitchAccessControlLists200Response;
import org.openapitools.client.model.UpdateNetworkSwitchAccessControlListsRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AccessControlListsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public AccessControlListsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public AccessControlListsApi(ApiClient apiClient) {
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
     * Build call for getNetworkSwitchAccessControlLists_1
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
    public okhttp3.Call getNetworkSwitchAccessControlLists_1Call(String networkId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/switch/accessControlLists"
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
    private okhttp3.Call getNetworkSwitchAccessControlLists_1ValidateBeforeCall(String networkId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling getNetworkSwitchAccessControlLists_1(Async)");
        }

        return getNetworkSwitchAccessControlLists_1Call(networkId, _callback);

    }

    /**
     * Return the access control lists for a MS network
     * Return the access control lists for a MS network
     * @param networkId  (required)
     * @return GetNetworkSwitchAccessControlLists200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public GetNetworkSwitchAccessControlLists200Response getNetworkSwitchAccessControlLists_1(String networkId) throws ApiException {
        ApiResponse<GetNetworkSwitchAccessControlLists200Response> localVarResp = getNetworkSwitchAccessControlLists_1WithHttpInfo(networkId);
        return localVarResp.getData();
    }

    /**
     * Return the access control lists for a MS network
     * Return the access control lists for a MS network
     * @param networkId  (required)
     * @return ApiResponse&lt;GetNetworkSwitchAccessControlLists200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetNetworkSwitchAccessControlLists200Response> getNetworkSwitchAccessControlLists_1WithHttpInfo(String networkId) throws ApiException {
        okhttp3.Call localVarCall = getNetworkSwitchAccessControlLists_1ValidateBeforeCall(networkId, null);
        Type localVarReturnType = new TypeToken<GetNetworkSwitchAccessControlLists200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return the access control lists for a MS network (asynchronously)
     * Return the access control lists for a MS network
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
    public okhttp3.Call getNetworkSwitchAccessControlLists_1Async(String networkId, final ApiCallback<GetNetworkSwitchAccessControlLists200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNetworkSwitchAccessControlLists_1ValidateBeforeCall(networkId, _callback);
        Type localVarReturnType = new TypeToken<GetNetworkSwitchAccessControlLists200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateNetworkSwitchAccessControlLists_1
     * @param networkId  (required)
     * @param updateNetworkSwitchAccessControlListsRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkSwitchAccessControlLists_1Call(String networkId, UpdateNetworkSwitchAccessControlListsRequest updateNetworkSwitchAccessControlListsRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateNetworkSwitchAccessControlListsRequest;

        // create path and map variables
        String localVarPath = "/networks/{networkId}/switch/accessControlLists"
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
    private okhttp3.Call updateNetworkSwitchAccessControlLists_1ValidateBeforeCall(String networkId, UpdateNetworkSwitchAccessControlListsRequest updateNetworkSwitchAccessControlListsRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling updateNetworkSwitchAccessControlLists_1(Async)");
        }

        // verify the required parameter 'updateNetworkSwitchAccessControlListsRequest' is set
        if (updateNetworkSwitchAccessControlListsRequest == null) {
            throw new ApiException("Missing the required parameter 'updateNetworkSwitchAccessControlListsRequest' when calling updateNetworkSwitchAccessControlLists_1(Async)");
        }

        return updateNetworkSwitchAccessControlLists_1Call(networkId, updateNetworkSwitchAccessControlListsRequest, _callback);

    }

    /**
     * Update the access control lists for a MS network
     * Update the access control lists for a MS network
     * @param networkId  (required)
     * @param updateNetworkSwitchAccessControlListsRequest  (required)
     * @return GetNetworkSwitchAccessControlLists200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public GetNetworkSwitchAccessControlLists200Response updateNetworkSwitchAccessControlLists_1(String networkId, UpdateNetworkSwitchAccessControlListsRequest updateNetworkSwitchAccessControlListsRequest) throws ApiException {
        ApiResponse<GetNetworkSwitchAccessControlLists200Response> localVarResp = updateNetworkSwitchAccessControlLists_1WithHttpInfo(networkId, updateNetworkSwitchAccessControlListsRequest);
        return localVarResp.getData();
    }

    /**
     * Update the access control lists for a MS network
     * Update the access control lists for a MS network
     * @param networkId  (required)
     * @param updateNetworkSwitchAccessControlListsRequest  (required)
     * @return ApiResponse&lt;GetNetworkSwitchAccessControlLists200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetNetworkSwitchAccessControlLists200Response> updateNetworkSwitchAccessControlLists_1WithHttpInfo(String networkId, UpdateNetworkSwitchAccessControlListsRequest updateNetworkSwitchAccessControlListsRequest) throws ApiException {
        okhttp3.Call localVarCall = updateNetworkSwitchAccessControlLists_1ValidateBeforeCall(networkId, updateNetworkSwitchAccessControlListsRequest, null);
        Type localVarReturnType = new TypeToken<GetNetworkSwitchAccessControlLists200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update the access control lists for a MS network (asynchronously)
     * Update the access control lists for a MS network
     * @param networkId  (required)
     * @param updateNetworkSwitchAccessControlListsRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkSwitchAccessControlLists_1Async(String networkId, UpdateNetworkSwitchAccessControlListsRequest updateNetworkSwitchAccessControlListsRequest, final ApiCallback<GetNetworkSwitchAccessControlLists200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateNetworkSwitchAccessControlLists_1ValidateBeforeCall(networkId, updateNetworkSwitchAccessControlListsRequest, _callback);
        Type localVarReturnType = new TypeToken<GetNetworkSwitchAccessControlLists200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
