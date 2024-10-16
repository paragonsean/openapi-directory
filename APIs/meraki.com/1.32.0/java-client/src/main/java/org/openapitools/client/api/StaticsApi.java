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


import org.openapitools.client.model.CreateNetworkAppliancePrefixesDelegatedStaticRequest;
import org.openapitools.client.model.GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner;
import org.openapitools.client.model.UpdateNetworkAppliancePrefixesDelegatedStaticRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class StaticsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public StaticsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public StaticsApi(ApiClient apiClient) {
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
     * Build call for createNetworkAppliancePrefixesDelegatedStatic_3
     * @param networkId  (required)
     * @param createNetworkAppliancePrefixesDelegatedStaticRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createNetworkAppliancePrefixesDelegatedStatic_3Call(String networkId, CreateNetworkAppliancePrefixesDelegatedStaticRequest createNetworkAppliancePrefixesDelegatedStaticRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createNetworkAppliancePrefixesDelegatedStaticRequest;

        // create path and map variables
        String localVarPath = "/networks/{networkId}/appliance/prefixes/delegated/statics"
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
    private okhttp3.Call createNetworkAppliancePrefixesDelegatedStatic_3ValidateBeforeCall(String networkId, CreateNetworkAppliancePrefixesDelegatedStaticRequest createNetworkAppliancePrefixesDelegatedStaticRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling createNetworkAppliancePrefixesDelegatedStatic_3(Async)");
        }

        // verify the required parameter 'createNetworkAppliancePrefixesDelegatedStaticRequest' is set
        if (createNetworkAppliancePrefixesDelegatedStaticRequest == null) {
            throw new ApiException("Missing the required parameter 'createNetworkAppliancePrefixesDelegatedStaticRequest' when calling createNetworkAppliancePrefixesDelegatedStatic_3(Async)");
        }

        return createNetworkAppliancePrefixesDelegatedStatic_3Call(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest, _callback);

    }

    /**
     * Add a static delegated prefix from a network
     * Add a static delegated prefix from a network
     * @param networkId  (required)
     * @param createNetworkAppliancePrefixesDelegatedStaticRequest  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object createNetworkAppliancePrefixesDelegatedStatic_3(String networkId, CreateNetworkAppliancePrefixesDelegatedStaticRequest createNetworkAppliancePrefixesDelegatedStaticRequest) throws ApiException {
        ApiResponse<Object> localVarResp = createNetworkAppliancePrefixesDelegatedStatic_3WithHttpInfo(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest);
        return localVarResp.getData();
    }

    /**
     * Add a static delegated prefix from a network
     * Add a static delegated prefix from a network
     * @param networkId  (required)
     * @param createNetworkAppliancePrefixesDelegatedStaticRequest  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> createNetworkAppliancePrefixesDelegatedStatic_3WithHttpInfo(String networkId, CreateNetworkAppliancePrefixesDelegatedStaticRequest createNetworkAppliancePrefixesDelegatedStaticRequest) throws ApiException {
        okhttp3.Call localVarCall = createNetworkAppliancePrefixesDelegatedStatic_3ValidateBeforeCall(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add a static delegated prefix from a network (asynchronously)
     * Add a static delegated prefix from a network
     * @param networkId  (required)
     * @param createNetworkAppliancePrefixesDelegatedStaticRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createNetworkAppliancePrefixesDelegatedStatic_3Async(String networkId, CreateNetworkAppliancePrefixesDelegatedStaticRequest createNetworkAppliancePrefixesDelegatedStaticRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = createNetworkAppliancePrefixesDelegatedStatic_3ValidateBeforeCall(networkId, createNetworkAppliancePrefixesDelegatedStaticRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteNetworkAppliancePrefixesDelegatedStatic_3
     * @param networkId  (required)
     * @param staticDelegatedPrefixId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteNetworkAppliancePrefixesDelegatedStatic_3Call(String networkId, String staticDelegatedPrefixId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()))
            .replace("{" + "staticDelegatedPrefixId" + "}", localVarApiClient.escapeString(staticDelegatedPrefixId.toString()));

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
    private okhttp3.Call deleteNetworkAppliancePrefixesDelegatedStatic_3ValidateBeforeCall(String networkId, String staticDelegatedPrefixId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling deleteNetworkAppliancePrefixesDelegatedStatic_3(Async)");
        }

        // verify the required parameter 'staticDelegatedPrefixId' is set
        if (staticDelegatedPrefixId == null) {
            throw new ApiException("Missing the required parameter 'staticDelegatedPrefixId' when calling deleteNetworkAppliancePrefixesDelegatedStatic_3(Async)");
        }

        return deleteNetworkAppliancePrefixesDelegatedStatic_3Call(networkId, staticDelegatedPrefixId, _callback);

    }

    /**
     * Delete a static delegated prefix from a network
     * Delete a static delegated prefix from a network
     * @param networkId  (required)
     * @param staticDelegatedPrefixId  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void deleteNetworkAppliancePrefixesDelegatedStatic_3(String networkId, String staticDelegatedPrefixId) throws ApiException {
        deleteNetworkAppliancePrefixesDelegatedStatic_3WithHttpInfo(networkId, staticDelegatedPrefixId);
    }

    /**
     * Delete a static delegated prefix from a network
     * Delete a static delegated prefix from a network
     * @param networkId  (required)
     * @param staticDelegatedPrefixId  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteNetworkAppliancePrefixesDelegatedStatic_3WithHttpInfo(String networkId, String staticDelegatedPrefixId) throws ApiException {
        okhttp3.Call localVarCall = deleteNetworkAppliancePrefixesDelegatedStatic_3ValidateBeforeCall(networkId, staticDelegatedPrefixId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a static delegated prefix from a network (asynchronously)
     * Delete a static delegated prefix from a network
     * @param networkId  (required)
     * @param staticDelegatedPrefixId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteNetworkAppliancePrefixesDelegatedStatic_3Async(String networkId, String staticDelegatedPrefixId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteNetworkAppliancePrefixesDelegatedStatic_3ValidateBeforeCall(networkId, staticDelegatedPrefixId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNetworkAppliancePrefixesDelegatedStatic_3
     * @param networkId  (required)
     * @param staticDelegatedPrefixId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkAppliancePrefixesDelegatedStatic_3Call(String networkId, String staticDelegatedPrefixId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()))
            .replace("{" + "staticDelegatedPrefixId" + "}", localVarApiClient.escapeString(staticDelegatedPrefixId.toString()));

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
    private okhttp3.Call getNetworkAppliancePrefixesDelegatedStatic_3ValidateBeforeCall(String networkId, String staticDelegatedPrefixId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling getNetworkAppliancePrefixesDelegatedStatic_3(Async)");
        }

        // verify the required parameter 'staticDelegatedPrefixId' is set
        if (staticDelegatedPrefixId == null) {
            throw new ApiException("Missing the required parameter 'staticDelegatedPrefixId' when calling getNetworkAppliancePrefixesDelegatedStatic_3(Async)");
        }

        return getNetworkAppliancePrefixesDelegatedStatic_3Call(networkId, staticDelegatedPrefixId, _callback);

    }

    /**
     * Return a static delegated prefix from a network
     * Return a static delegated prefix from a network
     * @param networkId  (required)
     * @param staticDelegatedPrefixId  (required)
     * @return GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner getNetworkAppliancePrefixesDelegatedStatic_3(String networkId, String staticDelegatedPrefixId) throws ApiException {
        ApiResponse<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner> localVarResp = getNetworkAppliancePrefixesDelegatedStatic_3WithHttpInfo(networkId, staticDelegatedPrefixId);
        return localVarResp.getData();
    }

    /**
     * Return a static delegated prefix from a network
     * Return a static delegated prefix from a network
     * @param networkId  (required)
     * @param staticDelegatedPrefixId  (required)
     * @return ApiResponse&lt;GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner> getNetworkAppliancePrefixesDelegatedStatic_3WithHttpInfo(String networkId, String staticDelegatedPrefixId) throws ApiException {
        okhttp3.Call localVarCall = getNetworkAppliancePrefixesDelegatedStatic_3ValidateBeforeCall(networkId, staticDelegatedPrefixId, null);
        Type localVarReturnType = new TypeToken<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return a static delegated prefix from a network (asynchronously)
     * Return a static delegated prefix from a network
     * @param networkId  (required)
     * @param staticDelegatedPrefixId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getNetworkAppliancePrefixesDelegatedStatic_3Async(String networkId, String staticDelegatedPrefixId, final ApiCallback<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNetworkAppliancePrefixesDelegatedStatic_3ValidateBeforeCall(networkId, staticDelegatedPrefixId, _callback);
        Type localVarReturnType = new TypeToken<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getNetworkAppliancePrefixesDelegatedStatics_3
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
    public okhttp3.Call getNetworkAppliancePrefixesDelegatedStatics_3Call(String networkId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/networks/{networkId}/appliance/prefixes/delegated/statics"
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
    private okhttp3.Call getNetworkAppliancePrefixesDelegatedStatics_3ValidateBeforeCall(String networkId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling getNetworkAppliancePrefixesDelegatedStatics_3(Async)");
        }

        return getNetworkAppliancePrefixesDelegatedStatics_3Call(networkId, _callback);

    }

    /**
     * List static delegated prefixes for a network
     * List static delegated prefixes for a network
     * @param networkId  (required)
     * @return List&lt;GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public List<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner> getNetworkAppliancePrefixesDelegatedStatics_3(String networkId) throws ApiException {
        ApiResponse<List<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner>> localVarResp = getNetworkAppliancePrefixesDelegatedStatics_3WithHttpInfo(networkId);
        return localVarResp.getData();
    }

    /**
     * List static delegated prefixes for a network
     * List static delegated prefixes for a network
     * @param networkId  (required)
     * @return ApiResponse&lt;List&lt;GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner>> getNetworkAppliancePrefixesDelegatedStatics_3WithHttpInfo(String networkId) throws ApiException {
        okhttp3.Call localVarCall = getNetworkAppliancePrefixesDelegatedStatics_3ValidateBeforeCall(networkId, null);
        Type localVarReturnType = new TypeToken<List<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List static delegated prefixes for a network (asynchronously)
     * List static delegated prefixes for a network
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
    public okhttp3.Call getNetworkAppliancePrefixesDelegatedStatics_3Async(String networkId, final ApiCallback<List<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getNetworkAppliancePrefixesDelegatedStatics_3ValidateBeforeCall(networkId, _callback);
        Type localVarReturnType = new TypeToken<List<GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateNetworkAppliancePrefixesDelegatedStatic_3
     * @param networkId  (required)
     * @param staticDelegatedPrefixId  (required)
     * @param updateNetworkAppliancePrefixesDelegatedStaticRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkAppliancePrefixesDelegatedStatic_3Call(String networkId, String staticDelegatedPrefixId, UpdateNetworkAppliancePrefixesDelegatedStaticRequest updateNetworkAppliancePrefixesDelegatedStaticRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateNetworkAppliancePrefixesDelegatedStaticRequest;

        // create path and map variables
        String localVarPath = "/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}"
            .replace("{" + "networkId" + "}", localVarApiClient.escapeString(networkId.toString()))
            .replace("{" + "staticDelegatedPrefixId" + "}", localVarApiClient.escapeString(staticDelegatedPrefixId.toString()));

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
    private okhttp3.Call updateNetworkAppliancePrefixesDelegatedStatic_3ValidateBeforeCall(String networkId, String staticDelegatedPrefixId, UpdateNetworkAppliancePrefixesDelegatedStaticRequest updateNetworkAppliancePrefixesDelegatedStaticRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'networkId' is set
        if (networkId == null) {
            throw new ApiException("Missing the required parameter 'networkId' when calling updateNetworkAppliancePrefixesDelegatedStatic_3(Async)");
        }

        // verify the required parameter 'staticDelegatedPrefixId' is set
        if (staticDelegatedPrefixId == null) {
            throw new ApiException("Missing the required parameter 'staticDelegatedPrefixId' when calling updateNetworkAppliancePrefixesDelegatedStatic_3(Async)");
        }

        return updateNetworkAppliancePrefixesDelegatedStatic_3Call(networkId, staticDelegatedPrefixId, updateNetworkAppliancePrefixesDelegatedStaticRequest, _callback);

    }

    /**
     * Update a static delegated prefix from a network
     * Update a static delegated prefix from a network
     * @param networkId  (required)
     * @param staticDelegatedPrefixId  (required)
     * @param updateNetworkAppliancePrefixesDelegatedStaticRequest  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public Object updateNetworkAppliancePrefixesDelegatedStatic_3(String networkId, String staticDelegatedPrefixId, UpdateNetworkAppliancePrefixesDelegatedStaticRequest updateNetworkAppliancePrefixesDelegatedStaticRequest) throws ApiException {
        ApiResponse<Object> localVarResp = updateNetworkAppliancePrefixesDelegatedStatic_3WithHttpInfo(networkId, staticDelegatedPrefixId, updateNetworkAppliancePrefixesDelegatedStaticRequest);
        return localVarResp.getData();
    }

    /**
     * Update a static delegated prefix from a network
     * Update a static delegated prefix from a network
     * @param networkId  (required)
     * @param staticDelegatedPrefixId  (required)
     * @param updateNetworkAppliancePrefixesDelegatedStaticRequest  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> updateNetworkAppliancePrefixesDelegatedStatic_3WithHttpInfo(String networkId, String staticDelegatedPrefixId, UpdateNetworkAppliancePrefixesDelegatedStaticRequest updateNetworkAppliancePrefixesDelegatedStaticRequest) throws ApiException {
        okhttp3.Call localVarCall = updateNetworkAppliancePrefixesDelegatedStatic_3ValidateBeforeCall(networkId, staticDelegatedPrefixId, updateNetworkAppliancePrefixesDelegatedStaticRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update a static delegated prefix from a network (asynchronously)
     * Update a static delegated prefix from a network
     * @param networkId  (required)
     * @param staticDelegatedPrefixId  (required)
     * @param updateNetworkAppliancePrefixesDelegatedStaticRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateNetworkAppliancePrefixesDelegatedStatic_3Async(String networkId, String staticDelegatedPrefixId, UpdateNetworkAppliancePrefixesDelegatedStaticRequest updateNetworkAppliancePrefixesDelegatedStaticRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateNetworkAppliancePrefixesDelegatedStatic_3ValidateBeforeCall(networkId, staticDelegatedPrefixId, updateNetworkAppliancePrefixesDelegatedStaticRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
