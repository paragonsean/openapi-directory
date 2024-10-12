/*
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
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


import org.openapitools.client.model.CloudError;
import org.openapitools.client.model.Job;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class JobsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public JobsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public JobsApi(ApiClient apiClient) {
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
     * Build call for jobsGet
     * @param deviceName The device name. (required)
     * @param name The job name. (required)
     * @param subscriptionId The subscription ID. (required)
     * @param resourceGroupName The resource group name. (required)
     * @param apiVersion The API version. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The job details. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call jobsGetCall(String deviceName, String name, String subscriptionId, String resourceGroupName, String apiVersion, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/jobs/{name}"
            .replace("{" + "deviceName" + "}", localVarApiClient.escapeString(deviceName.toString()))
            .replace("{" + "name" + "}", localVarApiClient.escapeString(name.toString()))
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()))
            .replace("{" + "resourceGroupName" + "}", localVarApiClient.escapeString(resourceGroupName.toString()));

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
    private okhttp3.Call jobsGetValidateBeforeCall(String deviceName, String name, String subscriptionId, String resourceGroupName, String apiVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'deviceName' is set
        if (deviceName == null) {
            throw new ApiException("Missing the required parameter 'deviceName' when calling jobsGet(Async)");
        }

        // verify the required parameter 'name' is set
        if (name == null) {
            throw new ApiException("Missing the required parameter 'name' when calling jobsGet(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling jobsGet(Async)");
        }

        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling jobsGet(Async)");
        }

        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling jobsGet(Async)");
        }

        return jobsGetCall(deviceName, name, subscriptionId, resourceGroupName, apiVersion, _callback);

    }

    /**
     * Gets the details of a specified job on a data box edge/gateway device.
     * 
     * @param deviceName The device name. (required)
     * @param name The job name. (required)
     * @param subscriptionId The subscription ID. (required)
     * @param resourceGroupName The resource group name. (required)
     * @param apiVersion The API version. (required)
     * @return Job
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The job details. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public Job jobsGet(String deviceName, String name, String subscriptionId, String resourceGroupName, String apiVersion) throws ApiException {
        ApiResponse<Job> localVarResp = jobsGetWithHttpInfo(deviceName, name, subscriptionId, resourceGroupName, apiVersion);
        return localVarResp.getData();
    }

    /**
     * Gets the details of a specified job on a data box edge/gateway device.
     * 
     * @param deviceName The device name. (required)
     * @param name The job name. (required)
     * @param subscriptionId The subscription ID. (required)
     * @param resourceGroupName The resource group name. (required)
     * @param apiVersion The API version. (required)
     * @return ApiResponse&lt;Job&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The job details. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Job> jobsGetWithHttpInfo(String deviceName, String name, String subscriptionId, String resourceGroupName, String apiVersion) throws ApiException {
        okhttp3.Call localVarCall = jobsGetValidateBeforeCall(deviceName, name, subscriptionId, resourceGroupName, apiVersion, null);
        Type localVarReturnType = new TypeToken<Job>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Gets the details of a specified job on a data box edge/gateway device. (asynchronously)
     * 
     * @param deviceName The device name. (required)
     * @param name The job name. (required)
     * @param subscriptionId The subscription ID. (required)
     * @param resourceGroupName The resource group name. (required)
     * @param apiVersion The API version. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The job details. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call jobsGetAsync(String deviceName, String name, String subscriptionId, String resourceGroupName, String apiVersion, final ApiCallback<Job> _callback) throws ApiException {

        okhttp3.Call localVarCall = jobsGetValidateBeforeCall(deviceName, name, subscriptionId, resourceGroupName, apiVersion, _callback);
        Type localVarReturnType = new TypeToken<Job>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
