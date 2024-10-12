/*
 * RecoveryServicesBackupClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-07-01
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


import org.openapitools.client.model.JobResourceList;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BackupJobsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public BackupJobsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public BackupJobsApi(ApiClient apiClient) {
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
     * Build call for backupJobsList
     * @param apiVersion Client Api Version. (required)
     * @param vaultName The name of the recovery services vault. (required)
     * @param resourceGroupName The name of the resource group where the recovery services vault is present. (required)
     * @param subscriptionId The subscription Id. (required)
     * @param $filter OData filter options. (optional)
     * @param $skipToken skipToken Filter. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call backupJobsListCall(String apiVersion, String vaultName, String resourceGroupName, String subscriptionId, String $filter, String $skipToken, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupJobs"
            .replace("{" + "vaultName" + "}", localVarApiClient.escapeString(vaultName.toString()))
            .replace("{" + "resourceGroupName" + "}", localVarApiClient.escapeString(resourceGroupName.toString()))
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (apiVersion != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("api-version", apiVersion));
        }

        if ($filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("$filter", $filter));
        }

        if ($skipToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("$skipToken", $skipToken));
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
    private okhttp3.Call backupJobsListValidateBeforeCall(String apiVersion, String vaultName, String resourceGroupName, String subscriptionId, String $filter, String $skipToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling backupJobsList(Async)");
        }

        // verify the required parameter 'vaultName' is set
        if (vaultName == null) {
            throw new ApiException("Missing the required parameter 'vaultName' when calling backupJobsList(Async)");
        }

        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling backupJobsList(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling backupJobsList(Async)");
        }

        return backupJobsListCall(apiVersion, vaultName, resourceGroupName, subscriptionId, $filter, $skipToken, _callback);

    }

    /**
     * 
     * Provides a pageable list of jobs.
     * @param apiVersion Client Api Version. (required)
     * @param vaultName The name of the recovery services vault. (required)
     * @param resourceGroupName The name of the resource group where the recovery services vault is present. (required)
     * @param subscriptionId The subscription Id. (required)
     * @param $filter OData filter options. (optional)
     * @param $skipToken skipToken Filter. (optional)
     * @return JobResourceList
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public JobResourceList backupJobsList(String apiVersion, String vaultName, String resourceGroupName, String subscriptionId, String $filter, String $skipToken) throws ApiException {
        ApiResponse<JobResourceList> localVarResp = backupJobsListWithHttpInfo(apiVersion, vaultName, resourceGroupName, subscriptionId, $filter, $skipToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Provides a pageable list of jobs.
     * @param apiVersion Client Api Version. (required)
     * @param vaultName The name of the recovery services vault. (required)
     * @param resourceGroupName The name of the resource group where the recovery services vault is present. (required)
     * @param subscriptionId The subscription Id. (required)
     * @param $filter OData filter options. (optional)
     * @param $skipToken skipToken Filter. (optional)
     * @return ApiResponse&lt;JobResourceList&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<JobResourceList> backupJobsListWithHttpInfo(String apiVersion, String vaultName, String resourceGroupName, String subscriptionId, String $filter, String $skipToken) throws ApiException {
        okhttp3.Call localVarCall = backupJobsListValidateBeforeCall(apiVersion, vaultName, resourceGroupName, subscriptionId, $filter, $skipToken, null);
        Type localVarReturnType = new TypeToken<JobResourceList>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Provides a pageable list of jobs.
     * @param apiVersion Client Api Version. (required)
     * @param vaultName The name of the recovery services vault. (required)
     * @param resourceGroupName The name of the resource group where the recovery services vault is present. (required)
     * @param subscriptionId The subscription Id. (required)
     * @param $filter OData filter options. (optional)
     * @param $skipToken skipToken Filter. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call backupJobsListAsync(String apiVersion, String vaultName, String resourceGroupName, String subscriptionId, String $filter, String $skipToken, final ApiCallback<JobResourceList> _callback) throws ApiException {

        okhttp3.Call localVarCall = backupJobsListValidateBeforeCall(apiVersion, vaultName, resourceGroupName, subscriptionId, $filter, $skipToken, _callback);
        Type localVarReturnType = new TypeToken<JobResourceList>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
