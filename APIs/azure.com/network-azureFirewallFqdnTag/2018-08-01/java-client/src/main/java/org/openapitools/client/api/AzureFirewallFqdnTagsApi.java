/*
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-08-01
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


import org.openapitools.client.model.AzureFirewallFqdnTagListResult;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AzureFirewallFqdnTagsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public AzureFirewallFqdnTagsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public AzureFirewallFqdnTagsApi(ApiClient apiClient) {
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
     * Build call for azureFirewallFqdnTagsListAll
     * @param apiVersion Client API version. (required)
     * @param subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success. The operation returns a list of Azure Firewall FQDN Tag resources. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call azureFirewallFqdnTagsListAllCall(String apiVersion, String subscriptionId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/providers/Microsoft.Network/azureFirewallFqdnTags"
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
    private okhttp3.Call azureFirewallFqdnTagsListAllValidateBeforeCall(String apiVersion, String subscriptionId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling azureFirewallFqdnTagsListAll(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling azureFirewallFqdnTagsListAll(Async)");
        }

        return azureFirewallFqdnTagsListAllCall(apiVersion, subscriptionId, _callback);

    }

    /**
     * 
     * Gets all the Azure Firewall FQDN Tags in a subscription.
     * @param apiVersion Client API version. (required)
     * @param subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. (required)
     * @return AzureFirewallFqdnTagListResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success. The operation returns a list of Azure Firewall FQDN Tag resources. </td><td>  -  </td></tr>
     </table>
     */
    public AzureFirewallFqdnTagListResult azureFirewallFqdnTagsListAll(String apiVersion, String subscriptionId) throws ApiException {
        ApiResponse<AzureFirewallFqdnTagListResult> localVarResp = azureFirewallFqdnTagsListAllWithHttpInfo(apiVersion, subscriptionId);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets all the Azure Firewall FQDN Tags in a subscription.
     * @param apiVersion Client API version. (required)
     * @param subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. (required)
     * @return ApiResponse&lt;AzureFirewallFqdnTagListResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success. The operation returns a list of Azure Firewall FQDN Tag resources. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AzureFirewallFqdnTagListResult> azureFirewallFqdnTagsListAllWithHttpInfo(String apiVersion, String subscriptionId) throws ApiException {
        okhttp3.Call localVarCall = azureFirewallFqdnTagsListAllValidateBeforeCall(apiVersion, subscriptionId, null);
        Type localVarReturnType = new TypeToken<AzureFirewallFqdnTagListResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets all the Azure Firewall FQDN Tags in a subscription.
     * @param apiVersion Client API version. (required)
     * @param subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success. The operation returns a list of Azure Firewall FQDN Tag resources. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call azureFirewallFqdnTagsListAllAsync(String apiVersion, String subscriptionId, final ApiCallback<AzureFirewallFqdnTagListResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = azureFirewallFqdnTagsListAllValidateBeforeCall(apiVersion, subscriptionId, _callback);
        Type localVarReturnType = new TypeToken<AzureFirewallFqdnTagListResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
