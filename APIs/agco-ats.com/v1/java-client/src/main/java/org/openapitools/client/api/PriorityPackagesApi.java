/*
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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


import org.openapitools.client.model.APIModelsApiError;
import org.openapitools.client.model.APIPagedResponseUpdateSystemModelsPriorityPackage;
import org.openapitools.client.model.UpdateSystemModelsPriorityPackage;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PriorityPackagesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public PriorityPackagesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public PriorityPackagesApi(ApiClient apiClient) {
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
     * Build call for priorityPackagesDeletePriorityPackages
     * @param ID The Priority Package ID (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call priorityPackagesDeletePriorityPackagesCall(String ID, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v2/PriorityPackages/{ID}"
            .replace("{" + "ID" + "}", localVarApiClient.escapeString(ID.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "*/*"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call priorityPackagesDeletePriorityPackagesValidateBeforeCall(String ID, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ID' is set
        if (ID == null) {
            throw new ApiException("Missing the required parameter 'ID' when calling priorityPackagesDeletePriorityPackages(Async)");
        }

        return priorityPackagesDeletePriorityPackagesCall(ID, _callback);

    }

    /**
     * Delete a Priority Package for a Client.
     * No Documentation Found.
     * @param ID The Priority Package ID (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public void priorityPackagesDeletePriorityPackages(String ID) throws ApiException {
        priorityPackagesDeletePriorityPackagesWithHttpInfo(ID);
    }

    /**
     * Delete a Priority Package for a Client.
     * No Documentation Found.
     * @param ID The Priority Package ID (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> priorityPackagesDeletePriorityPackagesWithHttpInfo(String ID) throws ApiException {
        okhttp3.Call localVarCall = priorityPackagesDeletePriorityPackagesValidateBeforeCall(ID, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a Priority Package for a Client. (asynchronously)
     * No Documentation Found.
     * @param ID The Priority Package ID (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call priorityPackagesDeletePriorityPackagesAsync(String ID, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = priorityPackagesDeletePriorityPackagesValidateBeforeCall(ID, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for priorityPackagesGetPriorityPackage
     * @param ID The Priority Package ID (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call priorityPackagesGetPriorityPackageCall(String ID, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v2/PriorityPackages/{ID}"
            .replace("{" + "ID" + "}", localVarApiClient.escapeString(ID.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json",
            "application/xml",
            "text/json",
            "text/xml"
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
    private okhttp3.Call priorityPackagesGetPriorityPackageValidateBeforeCall(String ID, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ID' is set
        if (ID == null) {
            throw new ApiException("Missing the required parameter 'ID' when calling priorityPackagesGetPriorityPackage(Async)");
        }

        return priorityPackagesGetPriorityPackageCall(ID, _callback);

    }

    /**
     * Get a Priority Packages for a Client.
     * No Documentation Found.
     * @param ID The Priority Package ID (required)
     * @return UpdateSystemModelsPriorityPackage
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public UpdateSystemModelsPriorityPackage priorityPackagesGetPriorityPackage(String ID) throws ApiException {
        ApiResponse<UpdateSystemModelsPriorityPackage> localVarResp = priorityPackagesGetPriorityPackageWithHttpInfo(ID);
        return localVarResp.getData();
    }

    /**
     * Get a Priority Packages for a Client.
     * No Documentation Found.
     * @param ID The Priority Package ID (required)
     * @return ApiResponse&lt;UpdateSystemModelsPriorityPackage&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateSystemModelsPriorityPackage> priorityPackagesGetPriorityPackageWithHttpInfo(String ID) throws ApiException {
        okhttp3.Call localVarCall = priorityPackagesGetPriorityPackageValidateBeforeCall(ID, null);
        Type localVarReturnType = new TypeToken<UpdateSystemModelsPriorityPackage>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a Priority Packages for a Client. (asynchronously)
     * No Documentation Found.
     * @param ID The Priority Package ID (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call priorityPackagesGetPriorityPackageAsync(String ID, final ApiCallback<UpdateSystemModelsPriorityPackage> _callback) throws ApiException {

        okhttp3.Call localVarCall = priorityPackagesGetPriorityPackageValidateBeforeCall(ID, _callback);
        Type localVarReturnType = new TypeToken<UpdateSystemModelsPriorityPackage>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for priorityPackagesGetPriorityPackages
     * @param clientID Optional. Filter priority packages by ClientID. (optional)
     * @param status Optional. Filter returned packages by status. By default only active packages will be returned. (optional)
     * @param limit Optional. The page limit. The default page limit is 10. (optional)
     * @param offset Optional. The page offset. The default page offset is 0. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call priorityPackagesGetPriorityPackagesCall(String clientID, String status, Integer limit, Integer offset, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v2/PriorityPackages";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (clientID != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("ClientID", clientID));
        }

        if (status != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("Status", status));
        }

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
        }

        final String[] localVarAccepts = {
            "application/json",
            "text/json"
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
    private okhttp3.Call priorityPackagesGetPriorityPackagesValidateBeforeCall(String clientID, String status, Integer limit, Integer offset, final ApiCallback _callback) throws ApiException {
        return priorityPackagesGetPriorityPackagesCall(clientID, status, limit, offset, _callback);

    }

    /**
     * Get a list of Priority Packages by Client.
     * No Documentation Found.
     * @param clientID Optional. Filter priority packages by ClientID. (optional)
     * @param status Optional. Filter returned packages by status. By default only active packages will be returned. (optional)
     * @param limit Optional. The page limit. The default page limit is 10. (optional)
     * @param offset Optional. The page offset. The default page offset is 0. (optional)
     * @return APIPagedResponseUpdateSystemModelsPriorityPackage
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public APIPagedResponseUpdateSystemModelsPriorityPackage priorityPackagesGetPriorityPackages(String clientID, String status, Integer limit, Integer offset) throws ApiException {
        ApiResponse<APIPagedResponseUpdateSystemModelsPriorityPackage> localVarResp = priorityPackagesGetPriorityPackagesWithHttpInfo(clientID, status, limit, offset);
        return localVarResp.getData();
    }

    /**
     * Get a list of Priority Packages by Client.
     * No Documentation Found.
     * @param clientID Optional. Filter priority packages by ClientID. (optional)
     * @param status Optional. Filter returned packages by status. By default only active packages will be returned. (optional)
     * @param limit Optional. The page limit. The default page limit is 10. (optional)
     * @param offset Optional. The page offset. The default page offset is 0. (optional)
     * @return ApiResponse&lt;APIPagedResponseUpdateSystemModelsPriorityPackage&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<APIPagedResponseUpdateSystemModelsPriorityPackage> priorityPackagesGetPriorityPackagesWithHttpInfo(String clientID, String status, Integer limit, Integer offset) throws ApiException {
        okhttp3.Call localVarCall = priorityPackagesGetPriorityPackagesValidateBeforeCall(clientID, status, limit, offset, null);
        Type localVarReturnType = new TypeToken<APIPagedResponseUpdateSystemModelsPriorityPackage>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a list of Priority Packages by Client. (asynchronously)
     * No Documentation Found.
     * @param clientID Optional. Filter priority packages by ClientID. (optional)
     * @param status Optional. Filter returned packages by status. By default only active packages will be returned. (optional)
     * @param limit Optional. The page limit. The default page limit is 10. (optional)
     * @param offset Optional. The page offset. The default page offset is 0. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call priorityPackagesGetPriorityPackagesAsync(String clientID, String status, Integer limit, Integer offset, final ApiCallback<APIPagedResponseUpdateSystemModelsPriorityPackage> _callback) throws ApiException {

        okhttp3.Call localVarCall = priorityPackagesGetPriorityPackagesValidateBeforeCall(clientID, status, limit, offset, _callback);
        Type localVarReturnType = new TypeToken<APIPagedResponseUpdateSystemModelsPriorityPackage>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for priorityPackagesPostPriorityPackages
     * @param updateSystemModelsPriorityPackage The PriorityPackage to add (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call priorityPackagesPostPriorityPackagesCall(UpdateSystemModelsPriorityPackage updateSystemModelsPriorityPackage, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateSystemModelsPriorityPackage;

        // create path and map variables
        String localVarPath = "/api/v2/PriorityPackages";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json",
            "application/xml",
            "text/json",
            "text/xml"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json",
            "application/x-www-form-urlencoded",
            "application/xml",
            "text/json",
            "text/xml"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call priorityPackagesPostPriorityPackagesValidateBeforeCall(UpdateSystemModelsPriorityPackage updateSystemModelsPriorityPackage, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'updateSystemModelsPriorityPackage' is set
        if (updateSystemModelsPriorityPackage == null) {
            throw new ApiException("Missing the required parameter 'updateSystemModelsPriorityPackage' when calling priorityPackagesPostPriorityPackages(Async)");
        }

        return priorityPackagesPostPriorityPackagesCall(updateSystemModelsPriorityPackage, _callback);

    }

    /**
     * Add a Priority Package for a Client.
     * No Documentation Found.
     * @param updateSystemModelsPriorityPackage The PriorityPackage to add (required)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public String priorityPackagesPostPriorityPackages(UpdateSystemModelsPriorityPackage updateSystemModelsPriorityPackage) throws ApiException {
        ApiResponse<String> localVarResp = priorityPackagesPostPriorityPackagesWithHttpInfo(updateSystemModelsPriorityPackage);
        return localVarResp.getData();
    }

    /**
     * Add a Priority Package for a Client.
     * No Documentation Found.
     * @param updateSystemModelsPriorityPackage The PriorityPackage to add (required)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> priorityPackagesPostPriorityPackagesWithHttpInfo(UpdateSystemModelsPriorityPackage updateSystemModelsPriorityPackage) throws ApiException {
        okhttp3.Call localVarCall = priorityPackagesPostPriorityPackagesValidateBeforeCall(updateSystemModelsPriorityPackage, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add a Priority Package for a Client. (asynchronously)
     * No Documentation Found.
     * @param updateSystemModelsPriorityPackage The PriorityPackage to add (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call priorityPackagesPostPriorityPackagesAsync(UpdateSystemModelsPriorityPackage updateSystemModelsPriorityPackage, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = priorityPackagesPostPriorityPackagesValidateBeforeCall(updateSystemModelsPriorityPackage, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
