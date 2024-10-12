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
import org.openapitools.client.model.APIPagedResponseUpdateSystemModelsBundle;
import org.openapitools.client.model.UpdateSystemModelsBundle;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BundlesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public BundlesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public BundlesApi(ApiClient apiClient) {
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
     * Build call for bundlesDeleteBundle
     * @param ID The Bundle ID to Delete (required)
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
    public okhttp3.Call bundlesDeleteBundleCall(String ID, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v2/Bundles/{ID}"
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
    private okhttp3.Call bundlesDeleteBundleValidateBeforeCall(String ID, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ID' is set
        if (ID == null) {
            throw new ApiException("Missing the required parameter 'ID' when calling bundlesDeleteBundle(Async)");
        }

        return bundlesDeleteBundleCall(ID, _callback);

    }

    /**
     * Delete a Bundle.
     * No Documentation Found.
     * @param ID The Bundle ID to Delete (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public void bundlesDeleteBundle(String ID) throws ApiException {
        bundlesDeleteBundleWithHttpInfo(ID);
    }

    /**
     * Delete a Bundle.
     * No Documentation Found.
     * @param ID The Bundle ID to Delete (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> bundlesDeleteBundleWithHttpInfo(String ID) throws ApiException {
        okhttp3.Call localVarCall = bundlesDeleteBundleValidateBeforeCall(ID, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a Bundle. (asynchronously)
     * No Documentation Found.
     * @param ID The Bundle ID to Delete (required)
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
    public okhttp3.Call bundlesDeleteBundleAsync(String ID, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = bundlesDeleteBundleValidateBeforeCall(ID, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for bundlesGetBundle
     * @param ID The Bundle ID (required)
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
    public okhttp3.Call bundlesGetBundleCall(String ID, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v2/Bundles/{ID}"
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
    private okhttp3.Call bundlesGetBundleValidateBeforeCall(String ID, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ID' is set
        if (ID == null) {
            throw new ApiException("Missing the required parameter 'ID' when calling bundlesGetBundle(Async)");
        }

        return bundlesGetBundleCall(ID, _callback);

    }

    /**
     * Get a specific Bundle by ID.
     * No Documentation Found.
     * @param ID The Bundle ID (required)
     * @return UpdateSystemModelsBundle
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public UpdateSystemModelsBundle bundlesGetBundle(String ID) throws ApiException {
        ApiResponse<UpdateSystemModelsBundle> localVarResp = bundlesGetBundleWithHttpInfo(ID);
        return localVarResp.getData();
    }

    /**
     * Get a specific Bundle by ID.
     * No Documentation Found.
     * @param ID The Bundle ID (required)
     * @return ApiResponse&lt;UpdateSystemModelsBundle&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateSystemModelsBundle> bundlesGetBundleWithHttpInfo(String ID) throws ApiException {
        okhttp3.Call localVarCall = bundlesGetBundleValidateBeforeCall(ID, null);
        Type localVarReturnType = new TypeToken<UpdateSystemModelsBundle>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a specific Bundle by ID. (asynchronously)
     * No Documentation Found.
     * @param ID The Bundle ID (required)
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
    public okhttp3.Call bundlesGetBundleAsync(String ID, final ApiCallback<UpdateSystemModelsBundle> _callback) throws ApiException {

        okhttp3.Call localVarCall = bundlesGetBundleValidateBeforeCall(ID, _callback);
        Type localVarReturnType = new TypeToken<UpdateSystemModelsBundle>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for bundlesGetBundles
     * @param updateGroupID Optional. Filter by UpdateGroup ID. (optional)
     * @param active Optional. Filter by active status. (optional)
     * @param limit Optional. The page limit. The default page limit is 10. (optional)
     * @param offset Optional. The page offset. The default page offset is 0. (optional)
     * @param bundleNumber Optional. If provided, filters by BundleNumber. (optional)
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
    public okhttp3.Call bundlesGetBundlesCall(String updateGroupID, Boolean active, Integer limit, Integer offset, Integer bundleNumber, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v2/Bundles";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (updateGroupID != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("UpdateGroupID", updateGroupID));
        }

        if (active != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("Active", active));
        }

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
        }

        if (bundleNumber != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("BundleNumber", bundleNumber));
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
    private okhttp3.Call bundlesGetBundlesValidateBeforeCall(String updateGroupID, Boolean active, Integer limit, Integer offset, Integer bundleNumber, final ApiCallback _callback) throws ApiException {
        return bundlesGetBundlesCall(updateGroupID, active, limit, offset, bundleNumber, _callback);

    }

    /**
     * Get the list of bundles.
     * No Documentation Found.
     * @param updateGroupID Optional. Filter by UpdateGroup ID. (optional)
     * @param active Optional. Filter by active status. (optional)
     * @param limit Optional. The page limit. The default page limit is 10. (optional)
     * @param offset Optional. The page offset. The default page offset is 0. (optional)
     * @param bundleNumber Optional. If provided, filters by BundleNumber. (optional)
     * @return APIPagedResponseUpdateSystemModelsBundle
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public APIPagedResponseUpdateSystemModelsBundle bundlesGetBundles(String updateGroupID, Boolean active, Integer limit, Integer offset, Integer bundleNumber) throws ApiException {
        ApiResponse<APIPagedResponseUpdateSystemModelsBundle> localVarResp = bundlesGetBundlesWithHttpInfo(updateGroupID, active, limit, offset, bundleNumber);
        return localVarResp.getData();
    }

    /**
     * Get the list of bundles.
     * No Documentation Found.
     * @param updateGroupID Optional. Filter by UpdateGroup ID. (optional)
     * @param active Optional. Filter by active status. (optional)
     * @param limit Optional. The page limit. The default page limit is 10. (optional)
     * @param offset Optional. The page offset. The default page offset is 0. (optional)
     * @param bundleNumber Optional. If provided, filters by BundleNumber. (optional)
     * @return ApiResponse&lt;APIPagedResponseUpdateSystemModelsBundle&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<APIPagedResponseUpdateSystemModelsBundle> bundlesGetBundlesWithHttpInfo(String updateGroupID, Boolean active, Integer limit, Integer offset, Integer bundleNumber) throws ApiException {
        okhttp3.Call localVarCall = bundlesGetBundlesValidateBeforeCall(updateGroupID, active, limit, offset, bundleNumber, null);
        Type localVarReturnType = new TypeToken<APIPagedResponseUpdateSystemModelsBundle>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get the list of bundles. (asynchronously)
     * No Documentation Found.
     * @param updateGroupID Optional. Filter by UpdateGroup ID. (optional)
     * @param active Optional. Filter by active status. (optional)
     * @param limit Optional. The page limit. The default page limit is 10. (optional)
     * @param offset Optional. The page offset. The default page offset is 0. (optional)
     * @param bundleNumber Optional. If provided, filters by BundleNumber. (optional)
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
    public okhttp3.Call bundlesGetBundlesAsync(String updateGroupID, Boolean active, Integer limit, Integer offset, Integer bundleNumber, final ApiCallback<APIPagedResponseUpdateSystemModelsBundle> _callback) throws ApiException {

        okhttp3.Call localVarCall = bundlesGetBundlesValidateBeforeCall(updateGroupID, active, limit, offset, bundleNumber, _callback);
        Type localVarReturnType = new TypeToken<APIPagedResponseUpdateSystemModelsBundle>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for bundlesPostBundle
     * @param updateSystemModelsBundle The bundle to add (required)
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
    public okhttp3.Call bundlesPostBundleCall(UpdateSystemModelsBundle updateSystemModelsBundle, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateSystemModelsBundle;

        // create path and map variables
        String localVarPath = "/api/v2/Bundles";

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
    private okhttp3.Call bundlesPostBundleValidateBeforeCall(UpdateSystemModelsBundle updateSystemModelsBundle, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'updateSystemModelsBundle' is set
        if (updateSystemModelsBundle == null) {
            throw new ApiException("Missing the required parameter 'updateSystemModelsBundle' when calling bundlesPostBundle(Async)");
        }

        return bundlesPostBundleCall(updateSystemModelsBundle, _callback);

    }

    /**
     * Add a Bundle to the Update System.
     * No Documentation Found.
     * @param updateSystemModelsBundle The bundle to add (required)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public String bundlesPostBundle(UpdateSystemModelsBundle updateSystemModelsBundle) throws ApiException {
        ApiResponse<String> localVarResp = bundlesPostBundleWithHttpInfo(updateSystemModelsBundle);
        return localVarResp.getData();
    }

    /**
     * Add a Bundle to the Update System.
     * No Documentation Found.
     * @param updateSystemModelsBundle The bundle to add (required)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> bundlesPostBundleWithHttpInfo(UpdateSystemModelsBundle updateSystemModelsBundle) throws ApiException {
        okhttp3.Call localVarCall = bundlesPostBundleValidateBeforeCall(updateSystemModelsBundle, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add a Bundle to the Update System. (asynchronously)
     * No Documentation Found.
     * @param updateSystemModelsBundle The bundle to add (required)
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
    public okhttp3.Call bundlesPostBundleAsync(UpdateSystemModelsBundle updateSystemModelsBundle, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = bundlesPostBundleValidateBeforeCall(updateSystemModelsBundle, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for bundlesPutBundle
     * @param ID The unique ID of the Bundle (required)
     * @param updateSystemModelsBundle The bundle to modify (required)
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
    public okhttp3.Call bundlesPutBundleCall(String ID, UpdateSystemModelsBundle updateSystemModelsBundle, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateSystemModelsBundle;

        // create path and map variables
        String localVarPath = "/api/v2/Bundles/{ID}"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call bundlesPutBundleValidateBeforeCall(String ID, UpdateSystemModelsBundle updateSystemModelsBundle, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'ID' is set
        if (ID == null) {
            throw new ApiException("Missing the required parameter 'ID' when calling bundlesPutBundle(Async)");
        }

        // verify the required parameter 'updateSystemModelsBundle' is set
        if (updateSystemModelsBundle == null) {
            throw new ApiException("Missing the required parameter 'updateSystemModelsBundle' when calling bundlesPutBundle(Async)");
        }

        return bundlesPutBundleCall(ID, updateSystemModelsBundle, _callback);

    }

    /**
     * Modify a Bundle in the Update System.
     * No Documentation Found.
     * @param ID The unique ID of the Bundle (required)
     * @param updateSystemModelsBundle The bundle to modify (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public void bundlesPutBundle(String ID, UpdateSystemModelsBundle updateSystemModelsBundle) throws ApiException {
        bundlesPutBundleWithHttpInfo(ID, updateSystemModelsBundle);
    }

    /**
     * Modify a Bundle in the Update System.
     * No Documentation Found.
     * @param ID The unique ID of the Bundle (required)
     * @param updateSystemModelsBundle The bundle to modify (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> bundlesPutBundleWithHttpInfo(String ID, UpdateSystemModelsBundle updateSystemModelsBundle) throws ApiException {
        okhttp3.Call localVarCall = bundlesPutBundleValidateBeforeCall(ID, updateSystemModelsBundle, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Modify a Bundle in the Update System. (asynchronously)
     * No Documentation Found.
     * @param ID The unique ID of the Bundle (required)
     * @param updateSystemModelsBundle The bundle to modify (required)
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
    public okhttp3.Call bundlesPutBundleAsync(String ID, UpdateSystemModelsBundle updateSystemModelsBundle, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = bundlesPutBundleValidateBeforeCall(ID, updateSystemModelsBundle, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
