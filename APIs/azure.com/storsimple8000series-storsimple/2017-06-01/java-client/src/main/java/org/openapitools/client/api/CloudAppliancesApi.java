/*
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
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


import org.openapitools.client.model.CloudAppliance;
import org.openapitools.client.model.CloudApplianceConfigurationList;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CloudAppliancesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CloudAppliancesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CloudAppliancesApi(ApiClient apiClient) {
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
     * Build call for cloudAppliancesListSupportedConfigurations
     * @param subscriptionId The subscription id (required)
     * @param resourceGroupName The resource group name (required)
     * @param managerName The manager name (required)
     * @param apiVersion The api version (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The collection of cloud appliance configuration. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cloudAppliancesListSupportedConfigurationsCall(String subscriptionId, String resourceGroupName, String managerName, String apiVersion, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/cloudApplianceConfigurations"
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()))
            .replace("{" + "resourceGroupName" + "}", localVarApiClient.escapeString(resourceGroupName.toString()))
            .replace("{" + "managerName" + "}", localVarApiClient.escapeString(managerName.toString()));

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
    private okhttp3.Call cloudAppliancesListSupportedConfigurationsValidateBeforeCall(String subscriptionId, String resourceGroupName, String managerName, String apiVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling cloudAppliancesListSupportedConfigurations(Async)");
        }

        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling cloudAppliancesListSupportedConfigurations(Async)");
        }

        // verify the required parameter 'managerName' is set
        if (managerName == null) {
            throw new ApiException("Missing the required parameter 'managerName' when calling cloudAppliancesListSupportedConfigurations(Async)");
        }

        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling cloudAppliancesListSupportedConfigurations(Async)");
        }

        return cloudAppliancesListSupportedConfigurationsCall(subscriptionId, resourceGroupName, managerName, apiVersion, _callback);

    }

    /**
     * 
     * Lists supported cloud appliance models and supported configurations.
     * @param subscriptionId The subscription id (required)
     * @param resourceGroupName The resource group name (required)
     * @param managerName The manager name (required)
     * @param apiVersion The api version (required)
     * @return CloudApplianceConfigurationList
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The collection of cloud appliance configuration. </td><td>  -  </td></tr>
     </table>
     */
    public CloudApplianceConfigurationList cloudAppliancesListSupportedConfigurations(String subscriptionId, String resourceGroupName, String managerName, String apiVersion) throws ApiException {
        ApiResponse<CloudApplianceConfigurationList> localVarResp = cloudAppliancesListSupportedConfigurationsWithHttpInfo(subscriptionId, resourceGroupName, managerName, apiVersion);
        return localVarResp.getData();
    }

    /**
     * 
     * Lists supported cloud appliance models and supported configurations.
     * @param subscriptionId The subscription id (required)
     * @param resourceGroupName The resource group name (required)
     * @param managerName The manager name (required)
     * @param apiVersion The api version (required)
     * @return ApiResponse&lt;CloudApplianceConfigurationList&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The collection of cloud appliance configuration. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CloudApplianceConfigurationList> cloudAppliancesListSupportedConfigurationsWithHttpInfo(String subscriptionId, String resourceGroupName, String managerName, String apiVersion) throws ApiException {
        okhttp3.Call localVarCall = cloudAppliancesListSupportedConfigurationsValidateBeforeCall(subscriptionId, resourceGroupName, managerName, apiVersion, null);
        Type localVarReturnType = new TypeToken<CloudApplianceConfigurationList>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Lists supported cloud appliance models and supported configurations.
     * @param subscriptionId The subscription id (required)
     * @param resourceGroupName The resource group name (required)
     * @param managerName The manager name (required)
     * @param apiVersion The api version (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The collection of cloud appliance configuration. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cloudAppliancesListSupportedConfigurationsAsync(String subscriptionId, String resourceGroupName, String managerName, String apiVersion, final ApiCallback<CloudApplianceConfigurationList> _callback) throws ApiException {

        okhttp3.Call localVarCall = cloudAppliancesListSupportedConfigurationsValidateBeforeCall(subscriptionId, resourceGroupName, managerName, apiVersion, _callback);
        Type localVarReturnType = new TypeToken<CloudApplianceConfigurationList>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for cloudAppliancesProvision
     * @param subscriptionId The subscription id (required)
     * @param resourceGroupName The resource group name (required)
     * @param managerName The manager name (required)
     * @param apiVersion The api version (required)
     * @param parameters The cloud appliance (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successfully created job for provision cloud appliance. </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Accepted the request to provision cloud appliance. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cloudAppliancesProvisionCall(String subscriptionId, String resourceGroupName, String managerName, String apiVersion, CloudAppliance parameters, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/provisionCloudAppliance"
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()))
            .replace("{" + "resourceGroupName" + "}", localVarApiClient.escapeString(resourceGroupName.toString()))
            .replace("{" + "managerName" + "}", localVarApiClient.escapeString(managerName.toString()));

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
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "azure_auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call cloudAppliancesProvisionValidateBeforeCall(String subscriptionId, String resourceGroupName, String managerName, String apiVersion, CloudAppliance parameters, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling cloudAppliancesProvision(Async)");
        }

        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling cloudAppliancesProvision(Async)");
        }

        // verify the required parameter 'managerName' is set
        if (managerName == null) {
            throw new ApiException("Missing the required parameter 'managerName' when calling cloudAppliancesProvision(Async)");
        }

        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling cloudAppliancesProvision(Async)");
        }

        // verify the required parameter 'parameters' is set
        if (parameters == null) {
            throw new ApiException("Missing the required parameter 'parameters' when calling cloudAppliancesProvision(Async)");
        }

        return cloudAppliancesProvisionCall(subscriptionId, resourceGroupName, managerName, apiVersion, parameters, _callback);

    }

    /**
     * 
     * Provisions cloud appliance.
     * @param subscriptionId The subscription id (required)
     * @param resourceGroupName The resource group name (required)
     * @param managerName The manager name (required)
     * @param apiVersion The api version (required)
     * @param parameters The cloud appliance (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successfully created job for provision cloud appliance. </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Accepted the request to provision cloud appliance. </td><td>  -  </td></tr>
     </table>
     */
    public void cloudAppliancesProvision(String subscriptionId, String resourceGroupName, String managerName, String apiVersion, CloudAppliance parameters) throws ApiException {
        cloudAppliancesProvisionWithHttpInfo(subscriptionId, resourceGroupName, managerName, apiVersion, parameters);
    }

    /**
     * 
     * Provisions cloud appliance.
     * @param subscriptionId The subscription id (required)
     * @param resourceGroupName The resource group name (required)
     * @param managerName The manager name (required)
     * @param apiVersion The api version (required)
     * @param parameters The cloud appliance (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successfully created job for provision cloud appliance. </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Accepted the request to provision cloud appliance. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> cloudAppliancesProvisionWithHttpInfo(String subscriptionId, String resourceGroupName, String managerName, String apiVersion, CloudAppliance parameters) throws ApiException {
        okhttp3.Call localVarCall = cloudAppliancesProvisionValidateBeforeCall(subscriptionId, resourceGroupName, managerName, apiVersion, parameters, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Provisions cloud appliance.
     * @param subscriptionId The subscription id (required)
     * @param resourceGroupName The resource group name (required)
     * @param managerName The manager name (required)
     * @param apiVersion The api version (required)
     * @param parameters The cloud appliance (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successfully created job for provision cloud appliance. </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Accepted the request to provision cloud appliance. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call cloudAppliancesProvisionAsync(String subscriptionId, String resourceGroupName, String managerName, String apiVersion, CloudAppliance parameters, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = cloudAppliancesProvisionValidateBeforeCall(subscriptionId, resourceGroupName, managerName, apiVersion, parameters, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
