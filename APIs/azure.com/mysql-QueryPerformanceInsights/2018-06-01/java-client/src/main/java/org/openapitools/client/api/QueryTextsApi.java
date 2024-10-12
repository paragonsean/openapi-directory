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


import org.openapitools.client.model.QueryText;
import org.openapitools.client.model.QueryTextsResultList;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class QueryTextsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public QueryTextsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public QueryTextsApi(ApiClient apiClient) {
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
     * Build call for queryTextsGet
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param queryId The Query-Store query identifier. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call queryTextsGetCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String queryId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/queryTexts/{queryId}"
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()))
            .replace("{" + "resourceGroupName" + "}", localVarApiClient.escapeString(resourceGroupName.toString()))
            .replace("{" + "serverName" + "}", localVarApiClient.escapeString(serverName.toString()))
            .replace("{" + "queryId" + "}", localVarApiClient.escapeString(queryId.toString()));

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
    private okhttp3.Call queryTextsGetValidateBeforeCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String queryId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling queryTextsGet(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling queryTextsGet(Async)");
        }

        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling queryTextsGet(Async)");
        }

        // verify the required parameter 'serverName' is set
        if (serverName == null) {
            throw new ApiException("Missing the required parameter 'serverName' when calling queryTextsGet(Async)");
        }

        // verify the required parameter 'queryId' is set
        if (queryId == null) {
            throw new ApiException("Missing the required parameter 'queryId' when calling queryTextsGet(Async)");
        }

        return queryTextsGetCall(apiVersion, subscriptionId, resourceGroupName, serverName, queryId, _callback);

    }

    /**
     * 
     * Retrieve the Query-Store query texts for the queryId.
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param queryId The Query-Store query identifier. (required)
     * @return QueryText
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public QueryText queryTextsGet(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String queryId) throws ApiException {
        ApiResponse<QueryText> localVarResp = queryTextsGetWithHttpInfo(apiVersion, subscriptionId, resourceGroupName, serverName, queryId);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve the Query-Store query texts for the queryId.
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param queryId The Query-Store query identifier. (required)
     * @return ApiResponse&lt;QueryText&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<QueryText> queryTextsGetWithHttpInfo(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String queryId) throws ApiException {
        okhttp3.Call localVarCall = queryTextsGetValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, queryId, null);
        Type localVarReturnType = new TypeToken<QueryText>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve the Query-Store query texts for the queryId.
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param queryId The Query-Store query identifier. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call queryTextsGetAsync(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String queryId, final ApiCallback<QueryText> _callback) throws ApiException {

        okhttp3.Call localVarCall = queryTextsGetValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, queryId, _callback);
        Type localVarReturnType = new TypeToken<QueryText>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for queryTextsListByServer
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param queryIds The query identifiers (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call queryTextsListByServerCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, List<String> queryIds, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/queryTexts"
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

        if (queryIds != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "queryIds", queryIds));
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
    private okhttp3.Call queryTextsListByServerValidateBeforeCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, List<String> queryIds, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling queryTextsListByServer(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling queryTextsListByServer(Async)");
        }

        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling queryTextsListByServer(Async)");
        }

        // verify the required parameter 'serverName' is set
        if (serverName == null) {
            throw new ApiException("Missing the required parameter 'serverName' when calling queryTextsListByServer(Async)");
        }

        // verify the required parameter 'queryIds' is set
        if (queryIds == null) {
            throw new ApiException("Missing the required parameter 'queryIds' when calling queryTextsListByServer(Async)");
        }

        return queryTextsListByServerCall(apiVersion, subscriptionId, resourceGroupName, serverName, queryIds, _callback);

    }

    /**
     * 
     * Retrieve the Query-Store query texts for specified queryIds.
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param queryIds The query identifiers (required)
     * @return QueryTextsResultList
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public QueryTextsResultList queryTextsListByServer(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, List<String> queryIds) throws ApiException {
        ApiResponse<QueryTextsResultList> localVarResp = queryTextsListByServerWithHttpInfo(apiVersion, subscriptionId, resourceGroupName, serverName, queryIds);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve the Query-Store query texts for specified queryIds.
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param queryIds The query identifiers (required)
     * @return ApiResponse&lt;QueryTextsResultList&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<QueryTextsResultList> queryTextsListByServerWithHttpInfo(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, List<String> queryIds) throws ApiException {
        okhttp3.Call localVarCall = queryTextsListByServerValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, queryIds, null);
        Type localVarReturnType = new TypeToken<QueryTextsResultList>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve the Query-Store query texts for specified queryIds.
     * @param apiVersion The API version to use for this operation. (required)
     * @param subscriptionId The ID of the target subscription. (required)
     * @param resourceGroupName The name of the resource group. The name is case insensitive. (required)
     * @param serverName The name of the server. (required)
     * @param queryIds The query identifiers (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call queryTextsListByServerAsync(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, List<String> queryIds, final ApiCallback<QueryTextsResultList> _callback) throws ApiException {

        okhttp3.Call localVarCall = queryTextsListByServerValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, queryIds, _callback);
        Type localVarReturnType = new TypeToken<QueryTextsResultList>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
