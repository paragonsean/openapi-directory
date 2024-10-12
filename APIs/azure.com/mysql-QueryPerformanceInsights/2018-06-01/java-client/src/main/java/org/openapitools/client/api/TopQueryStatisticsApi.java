/*
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01
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


import org.openapitools.client.model.QueryStatistic;
import org.openapitools.client.model.TopQueryStatisticsInput;
import org.openapitools.client.model.TopQueryStatisticsResultList;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TopQueryStatisticsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public TopQueryStatisticsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TopQueryStatisticsApi(ApiClient apiClient) {
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
     * Build call for topQueryStatisticsGet
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param queryStatisticId The Query Statistic identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call topQueryStatisticsGetCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String queryStatisticId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/topQueryStatistics/{queryStatisticId}"
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()))
            .replace("{" + "resourceGroupName" + "}", localVarApiClient.escapeString(resourceGroupName.toString()))
            .replace("{" + "serverName" + "}", localVarApiClient.escapeString(serverName.toString()))
            .replace("{" + "queryStatisticId" + "}", localVarApiClient.escapeString(queryStatisticId.toString()));

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
    private okhttp3.Call topQueryStatisticsGetValidateBeforeCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String queryStatisticId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling topQueryStatisticsGet(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling topQueryStatisticsGet(Async)");
        }

        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling topQueryStatisticsGet(Async)");
        }

        // verify the required parameter 'serverName' is set
        if (serverName == null) {
            throw new ApiException("Missing the required parameter 'serverName' when calling topQueryStatisticsGet(Async)");
        }

        // verify the required parameter 'queryStatisticId' is set
        if (queryStatisticId == null) {
            throw new ApiException("Missing the required parameter 'queryStatisticId' when calling topQueryStatisticsGet(Async)");
        }

        return topQueryStatisticsGetCall(apiVersion, subscriptionId, resourceGroupName, serverName, queryStatisticId, _callback);

    }

    /**
     * 
     * Retrieve the query statistic for specified identifier.
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param queryStatisticId The Query Statistic identifier. (required)
     * @return QueryStatistic
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public QueryStatistic topQueryStatisticsGet(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String queryStatisticId) throws ApiException {
        ApiResponse<QueryStatistic> localVarResp = topQueryStatisticsGetWithHttpInfo(apiVersion, subscriptionId, resourceGroupName, serverName, queryStatisticId);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve the query statistic for specified identifier.
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param queryStatisticId The Query Statistic identifier. (required)
     * @return ApiResponse&lt;QueryStatistic&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<QueryStatistic> topQueryStatisticsGetWithHttpInfo(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String queryStatisticId) throws ApiException {
        okhttp3.Call localVarCall = topQueryStatisticsGetValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, queryStatisticId, null);
        Type localVarReturnType = new TypeToken<QueryStatistic>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve the query statistic for specified identifier.
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param queryStatisticId The Query Statistic identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call topQueryStatisticsGetAsync(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String queryStatisticId, final ApiCallback<QueryStatistic> _callback) throws ApiException {

        okhttp3.Call localVarCall = topQueryStatisticsGetValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, queryStatisticId, _callback);
        Type localVarReturnType = new TypeToken<QueryStatistic>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for topQueryStatisticsListByServer
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param parameters The required parameters for retrieving top query statistics. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call topQueryStatisticsListByServerCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, TopQueryStatisticsInput parameters, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/topQueryStatistics"
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()))
            .replace("{" + "resourceGroupName" + "}", localVarApiClient.escapeString(resourceGroupName.toString()))
            .replace("{" + "serverName" + "}", localVarApiClient.escapeString(serverName.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call topQueryStatisticsListByServerValidateBeforeCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, TopQueryStatisticsInput parameters, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling topQueryStatisticsListByServer(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling topQueryStatisticsListByServer(Async)");
        }

        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling topQueryStatisticsListByServer(Async)");
        }

        // verify the required parameter 'serverName' is set
        if (serverName == null) {
            throw new ApiException("Missing the required parameter 'serverName' when calling topQueryStatisticsListByServer(Async)");
        }

        // verify the required parameter 'parameters' is set
        if (parameters == null) {
            throw new ApiException("Missing the required parameter 'parameters' when calling topQueryStatisticsListByServer(Async)");
        }

        return topQueryStatisticsListByServerCall(apiVersion, subscriptionId, resourceGroupName, serverName, parameters, _callback);

    }

    /**
     * 
     * Retrieve the Query-Store top queries for specified metric and aggregation.
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param parameters The required parameters for retrieving top query statistics. (required)
     * @return TopQueryStatisticsResultList
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public TopQueryStatisticsResultList topQueryStatisticsListByServer(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, TopQueryStatisticsInput parameters) throws ApiException {
        ApiResponse<TopQueryStatisticsResultList> localVarResp = topQueryStatisticsListByServerWithHttpInfo(apiVersion, subscriptionId, resourceGroupName, serverName, parameters);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve the Query-Store top queries for specified metric and aggregation.
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param parameters The required parameters for retrieving top query statistics. (required)
     * @return ApiResponse&lt;TopQueryStatisticsResultList&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<TopQueryStatisticsResultList> topQueryStatisticsListByServerWithHttpInfo(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, TopQueryStatisticsInput parameters) throws ApiException {
        okhttp3.Call localVarCall = topQueryStatisticsListByServerValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, parameters, null);
        Type localVarReturnType = new TypeToken<TopQueryStatisticsResultList>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve the Query-Store top queries for specified metric and aggregation.
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param parameters The required parameters for retrieving top query statistics. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call topQueryStatisticsListByServerAsync(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, TopQueryStatisticsInput parameters, final ApiCallback<TopQueryStatisticsResultList> _callback) throws ApiException {

        okhttp3.Call localVarCall = topQueryStatisticsListByServerValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, parameters, _callback);
        Type localVarReturnType = new TypeToken<TopQueryStatisticsResultList>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
