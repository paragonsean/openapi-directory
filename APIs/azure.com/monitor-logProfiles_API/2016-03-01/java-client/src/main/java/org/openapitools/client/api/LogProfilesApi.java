/*
 * MonitorManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-03-01
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


import org.openapitools.client.model.ErrorResponse;
import org.openapitools.client.model.LogProfileCollection;
import org.openapitools.client.model.LogProfileResource;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LogProfilesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public LogProfilesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public LogProfilesApi(ApiClient apiClient) {
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
     * Build call for logProfilesCreateOrUpdate
     * @param logProfileName The name of the log profile. (required)
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @param parameters Parameters supplied to the operation. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to create or update a log profile </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call logProfilesCreateOrUpdateCall(String logProfileName, String apiVersion, String subscriptionId, LogProfileResource parameters, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = parameters;

        // create path and map variables
        String localVarPath = "/subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles/{logProfileName}"
            .replace("{" + "logProfileName" + "}", localVarApiClient.escapeString(logProfileName.toString()))
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (apiVersion != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("api-version", apiVersion));
        }

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

        String[] localVarAuthNames = new String[] { "azure_auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call logProfilesCreateOrUpdateValidateBeforeCall(String logProfileName, String apiVersion, String subscriptionId, LogProfileResource parameters, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'logProfileName' is set
        if (logProfileName == null) {
            throw new ApiException("Missing the required parameter 'logProfileName' when calling logProfilesCreateOrUpdate(Async)");
        }

        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling logProfilesCreateOrUpdate(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling logProfilesCreateOrUpdate(Async)");
        }

        // verify the required parameter 'parameters' is set
        if (parameters == null) {
            throw new ApiException("Missing the required parameter 'parameters' when calling logProfilesCreateOrUpdate(Async)");
        }

        return logProfilesCreateOrUpdateCall(logProfileName, apiVersion, subscriptionId, parameters, _callback);

    }

    /**
     * 
     * Create or update a log profile in Azure Monitoring REST API.
     * @param logProfileName The name of the log profile. (required)
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @param parameters Parameters supplied to the operation. (required)
     * @return LogProfileResource
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to create or update a log profile </td><td>  -  </td></tr>
     </table>
     */
    public LogProfileResource logProfilesCreateOrUpdate(String logProfileName, String apiVersion, String subscriptionId, LogProfileResource parameters) throws ApiException {
        ApiResponse<LogProfileResource> localVarResp = logProfilesCreateOrUpdateWithHttpInfo(logProfileName, apiVersion, subscriptionId, parameters);
        return localVarResp.getData();
    }

    /**
     * 
     * Create or update a log profile in Azure Monitoring REST API.
     * @param logProfileName The name of the log profile. (required)
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @param parameters Parameters supplied to the operation. (required)
     * @return ApiResponse&lt;LogProfileResource&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to create or update a log profile </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LogProfileResource> logProfilesCreateOrUpdateWithHttpInfo(String logProfileName, String apiVersion, String subscriptionId, LogProfileResource parameters) throws ApiException {
        okhttp3.Call localVarCall = logProfilesCreateOrUpdateValidateBeforeCall(logProfileName, apiVersion, subscriptionId, parameters, null);
        Type localVarReturnType = new TypeToken<LogProfileResource>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Create or update a log profile in Azure Monitoring REST API.
     * @param logProfileName The name of the log profile. (required)
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @param parameters Parameters supplied to the operation. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to create or update a log profile </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call logProfilesCreateOrUpdateAsync(String logProfileName, String apiVersion, String subscriptionId, LogProfileResource parameters, final ApiCallback<LogProfileResource> _callback) throws ApiException {

        okhttp3.Call localVarCall = logProfilesCreateOrUpdateValidateBeforeCall(logProfileName, apiVersion, subscriptionId, parameters, _callback);
        Type localVarReturnType = new TypeToken<LogProfileResource>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for logProfilesDelete
     * @param logProfileName The name of the log profile. (required)
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to delete a log profile </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call logProfilesDeleteCall(String logProfileName, String apiVersion, String subscriptionId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles/{logProfileName}"
            .replace("{" + "logProfileName" + "}", localVarApiClient.escapeString(logProfileName.toString()))
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (apiVersion != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("api-version", apiVersion));
        }

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

        String[] localVarAuthNames = new String[] { "azure_auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call logProfilesDeleteValidateBeforeCall(String logProfileName, String apiVersion, String subscriptionId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'logProfileName' is set
        if (logProfileName == null) {
            throw new ApiException("Missing the required parameter 'logProfileName' when calling logProfilesDelete(Async)");
        }

        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling logProfilesDelete(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling logProfilesDelete(Async)");
        }

        return logProfilesDeleteCall(logProfileName, apiVersion, subscriptionId, _callback);

    }

    /**
     * 
     * Deletes the log profile.
     * @param logProfileName The name of the log profile. (required)
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to delete a log profile </td><td>  -  </td></tr>
     </table>
     */
    public void logProfilesDelete(String logProfileName, String apiVersion, String subscriptionId) throws ApiException {
        logProfilesDeleteWithHttpInfo(logProfileName, apiVersion, subscriptionId);
    }

    /**
     * 
     * Deletes the log profile.
     * @param logProfileName The name of the log profile. (required)
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to delete a log profile </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> logProfilesDeleteWithHttpInfo(String logProfileName, String apiVersion, String subscriptionId) throws ApiException {
        okhttp3.Call localVarCall = logProfilesDeleteValidateBeforeCall(logProfileName, apiVersion, subscriptionId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Deletes the log profile.
     * @param logProfileName The name of the log profile. (required)
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to delete a log profile </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call logProfilesDeleteAsync(String logProfileName, String apiVersion, String subscriptionId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = logProfilesDeleteValidateBeforeCall(logProfileName, apiVersion, subscriptionId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for logProfilesGet
     * @param logProfileName The name of the log profile. (required)
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to get more information about a log profile. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call logProfilesGetCall(String logProfileName, String apiVersion, String subscriptionId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles/{logProfileName}"
            .replace("{" + "logProfileName" + "}", localVarApiClient.escapeString(logProfileName.toString()))
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (apiVersion != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("api-version", apiVersion));
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

        String[] localVarAuthNames = new String[] { "azure_auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call logProfilesGetValidateBeforeCall(String logProfileName, String apiVersion, String subscriptionId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'logProfileName' is set
        if (logProfileName == null) {
            throw new ApiException("Missing the required parameter 'logProfileName' when calling logProfilesGet(Async)");
        }

        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling logProfilesGet(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling logProfilesGet(Async)");
        }

        return logProfilesGetCall(logProfileName, apiVersion, subscriptionId, _callback);

    }

    /**
     * 
     * Gets the log profile.
     * @param logProfileName The name of the log profile. (required)
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @return LogProfileResource
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to get more information about a log profile. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public LogProfileResource logProfilesGet(String logProfileName, String apiVersion, String subscriptionId) throws ApiException {
        ApiResponse<LogProfileResource> localVarResp = logProfilesGetWithHttpInfo(logProfileName, apiVersion, subscriptionId);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets the log profile.
     * @param logProfileName The name of the log profile. (required)
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @return ApiResponse&lt;LogProfileResource&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to get more information about a log profile. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LogProfileResource> logProfilesGetWithHttpInfo(String logProfileName, String apiVersion, String subscriptionId) throws ApiException {
        okhttp3.Call localVarCall = logProfilesGetValidateBeforeCall(logProfileName, apiVersion, subscriptionId, null);
        Type localVarReturnType = new TypeToken<LogProfileResource>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets the log profile.
     * @param logProfileName The name of the log profile. (required)
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to get more information about a log profile. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call logProfilesGetAsync(String logProfileName, String apiVersion, String subscriptionId, final ApiCallback<LogProfileResource> _callback) throws ApiException {

        okhttp3.Call localVarCall = logProfilesGetValidateBeforeCall(logProfileName, apiVersion, subscriptionId, _callback);
        Type localVarReturnType = new TypeToken<LogProfileResource>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for logProfilesList
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to list log profiles </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call logProfilesListCall(String apiVersion, String subscriptionId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/providers/microsoft.insights/logprofiles"
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (apiVersion != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("api-version", apiVersion));
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

        String[] localVarAuthNames = new String[] { "azure_auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call logProfilesListValidateBeforeCall(String apiVersion, String subscriptionId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling logProfilesList(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling logProfilesList(Async)");
        }

        return logProfilesListCall(apiVersion, subscriptionId, _callback);

    }

    /**
     * 
     * List the log profiles.
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @return LogProfileCollection
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to list log profiles </td><td>  -  </td></tr>
     </table>
     */
    public LogProfileCollection logProfilesList(String apiVersion, String subscriptionId) throws ApiException {
        ApiResponse<LogProfileCollection> localVarResp = logProfilesListWithHttpInfo(apiVersion, subscriptionId);
        return localVarResp.getData();
    }

    /**
     * 
     * List the log profiles.
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @return ApiResponse&lt;LogProfileCollection&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to list log profiles </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LogProfileCollection> logProfilesListWithHttpInfo(String apiVersion, String subscriptionId) throws ApiException {
        okhttp3.Call localVarCall = logProfilesListValidateBeforeCall(apiVersion, subscriptionId, null);
        Type localVarReturnType = new TypeToken<LogProfileCollection>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * List the log profiles.
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId The Azure subscription Id. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful request to list log profiles </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call logProfilesListAsync(String apiVersion, String subscriptionId, final ApiCallback<LogProfileCollection> _callback) throws ApiException {

        okhttp3.Call localVarCall = logProfilesListValidateBeforeCall(apiVersion, subscriptionId, _callback);
        Type localVarReturnType = new TypeToken<LogProfileCollection>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
