/*
 * SqlManagementClient
 * The Azure SQL Database management API provides a RESTful set of web APIs that interact with Azure SQL Database services to manage your databases. The API enables users to create, retrieve, update, and delete databases, servers, and other entities.
 *
 * The version of the OpenAPI document: 2015-05-01
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


import org.openapitools.client.model.SubscriptionUsage;
import org.openapitools.client.model.SubscriptionUsageListResult;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SubscriptionUsagesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SubscriptionUsagesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SubscriptionUsagesApi(ApiClient apiClient) {
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
     * Build call for subscriptionUsagesGet
     * @param locationName The name of the region where the resource is located. (required)
     * @param usageName Name of usage metric to return. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param apiVersion The API version to use for the request. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successfully retrieved particular subscription location usage. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidLocation - An invalid location was specified. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call subscriptionUsagesGetCall(String locationName, String usageName, String subscriptionId, String apiVersion, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/usages/{usageName}"
            .replace("{" + "locationName" + "}", localVarApiClient.escapeString(locationName.toString()))
            .replace("{" + "usageName" + "}", localVarApiClient.escapeString(usageName.toString()))
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call subscriptionUsagesGetValidateBeforeCall(String locationName, String usageName, String subscriptionId, String apiVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'locationName' is set
        if (locationName == null) {
            throw new ApiException("Missing the required parameter 'locationName' when calling subscriptionUsagesGet(Async)");
        }

        // verify the required parameter 'usageName' is set
        if (usageName == null) {
            throw new ApiException("Missing the required parameter 'usageName' when calling subscriptionUsagesGet(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling subscriptionUsagesGet(Async)");
        }

        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling subscriptionUsagesGet(Async)");
        }

        return subscriptionUsagesGetCall(locationName, usageName, subscriptionId, apiVersion, _callback);

    }

    /**
     * 
     * Gets a subscription usage metric.
     * @param locationName The name of the region where the resource is located. (required)
     * @param usageName Name of usage metric to return. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param apiVersion The API version to use for the request. (required)
     * @return SubscriptionUsage
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successfully retrieved particular subscription location usage. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidLocation - An invalid location was specified. </td><td>  -  </td></tr>
     </table>
     */
    public SubscriptionUsage subscriptionUsagesGet(String locationName, String usageName, String subscriptionId, String apiVersion) throws ApiException {
        ApiResponse<SubscriptionUsage> localVarResp = subscriptionUsagesGetWithHttpInfo(locationName, usageName, subscriptionId, apiVersion);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets a subscription usage metric.
     * @param locationName The name of the region where the resource is located. (required)
     * @param usageName Name of usage metric to return. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param apiVersion The API version to use for the request. (required)
     * @return ApiResponse&lt;SubscriptionUsage&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successfully retrieved particular subscription location usage. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidLocation - An invalid location was specified. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SubscriptionUsage> subscriptionUsagesGetWithHttpInfo(String locationName, String usageName, String subscriptionId, String apiVersion) throws ApiException {
        okhttp3.Call localVarCall = subscriptionUsagesGetValidateBeforeCall(locationName, usageName, subscriptionId, apiVersion, null);
        Type localVarReturnType = new TypeToken<SubscriptionUsage>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets a subscription usage metric.
     * @param locationName The name of the region where the resource is located. (required)
     * @param usageName Name of usage metric to return. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param apiVersion The API version to use for the request. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successfully retrieved particular subscription location usage. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidLocation - An invalid location was specified. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call subscriptionUsagesGetAsync(String locationName, String usageName, String subscriptionId, String apiVersion, final ApiCallback<SubscriptionUsage> _callback) throws ApiException {

        okhttp3.Call localVarCall = subscriptionUsagesGetValidateBeforeCall(locationName, usageName, subscriptionId, apiVersion, _callback);
        Type localVarReturnType = new TypeToken<SubscriptionUsage>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for subscriptionUsagesListByLocation
     * @param locationName The name of the region where the resource is located. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param apiVersion The API version to use for the request. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successfully retrieved the subscription location usages. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidLocation - An invalid location was specified. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call subscriptionUsagesListByLocationCall(String locationName, String subscriptionId, String apiVersion, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/usages"
            .replace("{" + "locationName" + "}", localVarApiClient.escapeString(locationName.toString()))
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call subscriptionUsagesListByLocationValidateBeforeCall(String locationName, String subscriptionId, String apiVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'locationName' is set
        if (locationName == null) {
            throw new ApiException("Missing the required parameter 'locationName' when calling subscriptionUsagesListByLocation(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling subscriptionUsagesListByLocation(Async)");
        }

        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling subscriptionUsagesListByLocation(Async)");
        }

        return subscriptionUsagesListByLocationCall(locationName, subscriptionId, apiVersion, _callback);

    }

    /**
     * 
     * Gets all subscription usage metrics in a given location.
     * @param locationName The name of the region where the resource is located. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param apiVersion The API version to use for the request. (required)
     * @return SubscriptionUsageListResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successfully retrieved the subscription location usages. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidLocation - An invalid location was specified. </td><td>  -  </td></tr>
     </table>
     */
    public SubscriptionUsageListResult subscriptionUsagesListByLocation(String locationName, String subscriptionId, String apiVersion) throws ApiException {
        ApiResponse<SubscriptionUsageListResult> localVarResp = subscriptionUsagesListByLocationWithHttpInfo(locationName, subscriptionId, apiVersion);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets all subscription usage metrics in a given location.
     * @param locationName The name of the region where the resource is located. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param apiVersion The API version to use for the request. (required)
     * @return ApiResponse&lt;SubscriptionUsageListResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successfully retrieved the subscription location usages. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidLocation - An invalid location was specified. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SubscriptionUsageListResult> subscriptionUsagesListByLocationWithHttpInfo(String locationName, String subscriptionId, String apiVersion) throws ApiException {
        okhttp3.Call localVarCall = subscriptionUsagesListByLocationValidateBeforeCall(locationName, subscriptionId, apiVersion, null);
        Type localVarReturnType = new TypeToken<SubscriptionUsageListResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets all subscription usage metrics in a given location.
     * @param locationName The name of the region where the resource is located. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param apiVersion The API version to use for the request. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successfully retrieved the subscription location usages. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> *** Error Responses: ***   * 400 SubscriptionNotFound - The requested subscription was not found.   * 400 InvalidLocation - An invalid location was specified. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call subscriptionUsagesListByLocationAsync(String locationName, String subscriptionId, String apiVersion, final ApiCallback<SubscriptionUsageListResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = subscriptionUsagesListByLocationValidateBeforeCall(locationName, subscriptionId, apiVersion, _callback);
        Type localVarReturnType = new TypeToken<SubscriptionUsageListResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
