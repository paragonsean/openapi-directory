/*
 * ApiManagementClient
 * Use this REST API to get all the issues across an Azure Api Management service.
 *
 * The version of the OpenAPI document: 2018-01-01
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


import org.openapitools.client.model.IssueListByService200Response;
import org.openapitools.client.model.IssueListByServiceDefaultResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class IssuesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public IssuesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public IssuesApi(ApiClient apiClient) {
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
     * Build call for issueListByService
     * @param resourceGroupName The name of the resource group. (required)
     * @param serviceName The name of the API Management service. (required)
     * @param apiVersion Version of the API to be used with the client request. (required)
     * @param subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. (required)
     * @param $filter | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | state        | eq                     |                                   | | userId          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | (optional)
     * @param $top Number of records to return. (optional)
     * @param $skip Number of records to skip. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Lists a collection of Issue entities. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call issueListByServiceCall(String resourceGroupName, String serviceName, String apiVersion, String subscriptionId, String $filter, Integer $top, Integer $skip, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/issues"
            .replace("{" + "resourceGroupName" + "}", localVarApiClient.escapeString(resourceGroupName.toString()))
            .replace("{" + "serviceName" + "}", localVarApiClient.escapeString(serviceName.toString()))
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if ($filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("$filter", $filter));
        }

        if ($top != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("$top", $top));
        }

        if ($skip != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("$skip", $skip));
        }

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
    private okhttp3.Call issueListByServiceValidateBeforeCall(String resourceGroupName, String serviceName, String apiVersion, String subscriptionId, String $filter, Integer $top, Integer $skip, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling issueListByService(Async)");
        }

        // verify the required parameter 'serviceName' is set
        if (serviceName == null) {
            throw new ApiException("Missing the required parameter 'serviceName' when calling issueListByService(Async)");
        }

        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling issueListByService(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling issueListByService(Async)");
        }

        return issueListByServiceCall(resourceGroupName, serviceName, apiVersion, subscriptionId, $filter, $top, $skip, _callback);

    }

    /**
     * 
     * Lists a collection of issues in the specified service instance.
     * @param resourceGroupName The name of the resource group. (required)
     * @param serviceName The name of the API Management service. (required)
     * @param apiVersion Version of the API to be used with the client request. (required)
     * @param subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. (required)
     * @param $filter | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | state        | eq                     |                                   | | userId          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | (optional)
     * @param $top Number of records to return. (optional)
     * @param $skip Number of records to skip. (optional)
     * @return IssueListByService200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Lists a collection of Issue entities. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public IssueListByService200Response issueListByService(String resourceGroupName, String serviceName, String apiVersion, String subscriptionId, String $filter, Integer $top, Integer $skip) throws ApiException {
        ApiResponse<IssueListByService200Response> localVarResp = issueListByServiceWithHttpInfo(resourceGroupName, serviceName, apiVersion, subscriptionId, $filter, $top, $skip);
        return localVarResp.getData();
    }

    /**
     * 
     * Lists a collection of issues in the specified service instance.
     * @param resourceGroupName The name of the resource group. (required)
     * @param serviceName The name of the API Management service. (required)
     * @param apiVersion Version of the API to be used with the client request. (required)
     * @param subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. (required)
     * @param $filter | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | state        | eq                     |                                   | | userId          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | (optional)
     * @param $top Number of records to return. (optional)
     * @param $skip Number of records to skip. (optional)
     * @return ApiResponse&lt;IssueListByService200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Lists a collection of Issue entities. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<IssueListByService200Response> issueListByServiceWithHttpInfo(String resourceGroupName, String serviceName, String apiVersion, String subscriptionId, String $filter, Integer $top, Integer $skip) throws ApiException {
        okhttp3.Call localVarCall = issueListByServiceValidateBeforeCall(resourceGroupName, serviceName, apiVersion, subscriptionId, $filter, $top, $skip, null);
        Type localVarReturnType = new TypeToken<IssueListByService200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Lists a collection of issues in the specified service instance.
     * @param resourceGroupName The name of the resource group. (required)
     * @param serviceName The name of the API Management service. (required)
     * @param apiVersion Version of the API to be used with the client request. (required)
     * @param subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. (required)
     * @param $filter | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | state        | eq                     |                                   | | userId          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | (optional)
     * @param $top Number of records to return. (optional)
     * @param $skip Number of records to skip. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Lists a collection of Issue entities. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call issueListByServiceAsync(String resourceGroupName, String serviceName, String apiVersion, String subscriptionId, String $filter, Integer $top, Integer $skip, final ApiCallback<IssueListByService200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = issueListByServiceValidateBeforeCall(resourceGroupName, serviceName, apiVersion, subscriptionId, $filter, $top, $skip, _callback);
        Type localVarReturnType = new TypeToken<IssueListByService200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
