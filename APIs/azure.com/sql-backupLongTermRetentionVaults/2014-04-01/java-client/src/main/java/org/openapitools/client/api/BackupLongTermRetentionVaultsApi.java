/*
 * Azure SQL Server Backup Long Term Retention Vault
 * Provides read and update functionality for Azure SQL Server backup long term retention vault
 *
 * The version of the OpenAPI document: 2014-04-01
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


import org.openapitools.client.model.BackupLongTermRetentionVault;
import org.openapitools.client.model.BackupLongTermRetentionVaultListResult;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BackupLongTermRetentionVaultsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public BackupLongTermRetentionVaultsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public BackupLongTermRetentionVaultsApi(ApiClient apiClient) {
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
     * Build call for backupLongTermRetentionVaultsCreateOrUpdate
     * @param apiVersion The API version to use for the request. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. (required)
     * @param serverName The name of the server. (required)
     * @param backupLongTermRetentionVaultName The name of the backup long term retention vault (required)
     * @param parameters The required parameters to update a backup long term retention vault (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Accepted </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call backupLongTermRetentionVaultsCreateOrUpdateCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String backupLongTermRetentionVaultName, BackupLongTermRetentionVault parameters, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/backupLongTermRetentionVaults/{backupLongTermRetentionVaultName}"
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()))
            .replace("{" + "resourceGroupName" + "}", localVarApiClient.escapeString(resourceGroupName.toString()))
            .replace("{" + "serverName" + "}", localVarApiClient.escapeString(serverName.toString()))
            .replace("{" + "backupLongTermRetentionVaultName" + "}", localVarApiClient.escapeString(backupLongTermRetentionVaultName.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call backupLongTermRetentionVaultsCreateOrUpdateValidateBeforeCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String backupLongTermRetentionVaultName, BackupLongTermRetentionVault parameters, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling backupLongTermRetentionVaultsCreateOrUpdate(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling backupLongTermRetentionVaultsCreateOrUpdate(Async)");
        }

        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling backupLongTermRetentionVaultsCreateOrUpdate(Async)");
        }

        // verify the required parameter 'serverName' is set
        if (serverName == null) {
            throw new ApiException("Missing the required parameter 'serverName' when calling backupLongTermRetentionVaultsCreateOrUpdate(Async)");
        }

        // verify the required parameter 'backupLongTermRetentionVaultName' is set
        if (backupLongTermRetentionVaultName == null) {
            throw new ApiException("Missing the required parameter 'backupLongTermRetentionVaultName' when calling backupLongTermRetentionVaultsCreateOrUpdate(Async)");
        }

        // verify the required parameter 'parameters' is set
        if (parameters == null) {
            throw new ApiException("Missing the required parameter 'parameters' when calling backupLongTermRetentionVaultsCreateOrUpdate(Async)");
        }

        return backupLongTermRetentionVaultsCreateOrUpdateCall(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName, parameters, _callback);

    }

    /**
     * 
     * Updates a server backup long term retention vault
     * @param apiVersion The API version to use for the request. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. (required)
     * @param serverName The name of the server. (required)
     * @param backupLongTermRetentionVaultName The name of the backup long term retention vault (required)
     * @param parameters The required parameters to update a backup long term retention vault (required)
     * @return BackupLongTermRetentionVault
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Accepted </td><td>  -  </td></tr>
     </table>
     */
    public BackupLongTermRetentionVault backupLongTermRetentionVaultsCreateOrUpdate(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String backupLongTermRetentionVaultName, BackupLongTermRetentionVault parameters) throws ApiException {
        ApiResponse<BackupLongTermRetentionVault> localVarResp = backupLongTermRetentionVaultsCreateOrUpdateWithHttpInfo(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName, parameters);
        return localVarResp.getData();
    }

    /**
     * 
     * Updates a server backup long term retention vault
     * @param apiVersion The API version to use for the request. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. (required)
     * @param serverName The name of the server. (required)
     * @param backupLongTermRetentionVaultName The name of the backup long term retention vault (required)
     * @param parameters The required parameters to update a backup long term retention vault (required)
     * @return ApiResponse&lt;BackupLongTermRetentionVault&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Accepted </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BackupLongTermRetentionVault> backupLongTermRetentionVaultsCreateOrUpdateWithHttpInfo(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String backupLongTermRetentionVaultName, BackupLongTermRetentionVault parameters) throws ApiException {
        okhttp3.Call localVarCall = backupLongTermRetentionVaultsCreateOrUpdateValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName, parameters, null);
        Type localVarReturnType = new TypeToken<BackupLongTermRetentionVault>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Updates a server backup long term retention vault
     * @param apiVersion The API version to use for the request. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. (required)
     * @param serverName The name of the server. (required)
     * @param backupLongTermRetentionVaultName The name of the backup long term retention vault (required)
     * @param parameters The required parameters to update a backup long term retention vault (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> Accepted </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call backupLongTermRetentionVaultsCreateOrUpdateAsync(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String backupLongTermRetentionVaultName, BackupLongTermRetentionVault parameters, final ApiCallback<BackupLongTermRetentionVault> _callback) throws ApiException {

        okhttp3.Call localVarCall = backupLongTermRetentionVaultsCreateOrUpdateValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName, parameters, _callback);
        Type localVarReturnType = new TypeToken<BackupLongTermRetentionVault>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for backupLongTermRetentionVaultsGet
     * @param apiVersion The API version to use for the request. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. (required)
     * @param serverName The name of the server. (required)
     * @param backupLongTermRetentionVaultName The name of the Azure SQL Server backup LongTermRetention vault (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call backupLongTermRetentionVaultsGetCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String backupLongTermRetentionVaultName, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/backupLongTermRetentionVaults/{backupLongTermRetentionVaultName}"
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()))
            .replace("{" + "resourceGroupName" + "}", localVarApiClient.escapeString(resourceGroupName.toString()))
            .replace("{" + "serverName" + "}", localVarApiClient.escapeString(serverName.toString()))
            .replace("{" + "backupLongTermRetentionVaultName" + "}", localVarApiClient.escapeString(backupLongTermRetentionVaultName.toString()));

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
    private okhttp3.Call backupLongTermRetentionVaultsGetValidateBeforeCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String backupLongTermRetentionVaultName, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling backupLongTermRetentionVaultsGet(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling backupLongTermRetentionVaultsGet(Async)");
        }

        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling backupLongTermRetentionVaultsGet(Async)");
        }

        // verify the required parameter 'serverName' is set
        if (serverName == null) {
            throw new ApiException("Missing the required parameter 'serverName' when calling backupLongTermRetentionVaultsGet(Async)");
        }

        // verify the required parameter 'backupLongTermRetentionVaultName' is set
        if (backupLongTermRetentionVaultName == null) {
            throw new ApiException("Missing the required parameter 'backupLongTermRetentionVaultName' when calling backupLongTermRetentionVaultsGet(Async)");
        }

        return backupLongTermRetentionVaultsGetCall(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName, _callback);

    }

    /**
     * 
     * Gets a server backup long term retention vault
     * @param apiVersion The API version to use for the request. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. (required)
     * @param serverName The name of the server. (required)
     * @param backupLongTermRetentionVaultName The name of the Azure SQL Server backup LongTermRetention vault (required)
     * @return BackupLongTermRetentionVault
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public BackupLongTermRetentionVault backupLongTermRetentionVaultsGet(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String backupLongTermRetentionVaultName) throws ApiException {
        ApiResponse<BackupLongTermRetentionVault> localVarResp = backupLongTermRetentionVaultsGetWithHttpInfo(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets a server backup long term retention vault
     * @param apiVersion The API version to use for the request. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. (required)
     * @param serverName The name of the server. (required)
     * @param backupLongTermRetentionVaultName The name of the Azure SQL Server backup LongTermRetention vault (required)
     * @return ApiResponse&lt;BackupLongTermRetentionVault&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BackupLongTermRetentionVault> backupLongTermRetentionVaultsGetWithHttpInfo(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String backupLongTermRetentionVaultName) throws ApiException {
        okhttp3.Call localVarCall = backupLongTermRetentionVaultsGetValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName, null);
        Type localVarReturnType = new TypeToken<BackupLongTermRetentionVault>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets a server backup long term retention vault
     * @param apiVersion The API version to use for the request. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. (required)
     * @param serverName The name of the server. (required)
     * @param backupLongTermRetentionVaultName The name of the Azure SQL Server backup LongTermRetention vault (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call backupLongTermRetentionVaultsGetAsync(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, String backupLongTermRetentionVaultName, final ApiCallback<BackupLongTermRetentionVault> _callback) throws ApiException {

        okhttp3.Call localVarCall = backupLongTermRetentionVaultsGetValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName, _callback);
        Type localVarReturnType = new TypeToken<BackupLongTermRetentionVault>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for backupLongTermRetentionVaultsListByServer
     * @param apiVersion The API version to use for the request. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. (required)
     * @param serverName The name of the server. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call backupLongTermRetentionVaultsListByServerCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/backupLongTermRetentionVaults"
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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call backupLongTermRetentionVaultsListByServerValidateBeforeCall(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling backupLongTermRetentionVaultsListByServer(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling backupLongTermRetentionVaultsListByServer(Async)");
        }

        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling backupLongTermRetentionVaultsListByServer(Async)");
        }

        // verify the required parameter 'serverName' is set
        if (serverName == null) {
            throw new ApiException("Missing the required parameter 'serverName' when calling backupLongTermRetentionVaultsListByServer(Async)");
        }

        return backupLongTermRetentionVaultsListByServerCall(apiVersion, subscriptionId, resourceGroupName, serverName, _callback);

    }

    /**
     * 
     * Gets server backup long term retention vaults in a server
     * @param apiVersion The API version to use for the request. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. (required)
     * @param serverName The name of the server. (required)
     * @return BackupLongTermRetentionVaultListResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public BackupLongTermRetentionVaultListResult backupLongTermRetentionVaultsListByServer(String apiVersion, String subscriptionId, String resourceGroupName, String serverName) throws ApiException {
        ApiResponse<BackupLongTermRetentionVaultListResult> localVarResp = backupLongTermRetentionVaultsListByServerWithHttpInfo(apiVersion, subscriptionId, resourceGroupName, serverName);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets server backup long term retention vaults in a server
     * @param apiVersion The API version to use for the request. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. (required)
     * @param serverName The name of the server. (required)
     * @return ApiResponse&lt;BackupLongTermRetentionVaultListResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BackupLongTermRetentionVaultListResult> backupLongTermRetentionVaultsListByServerWithHttpInfo(String apiVersion, String subscriptionId, String resourceGroupName, String serverName) throws ApiException {
        okhttp3.Call localVarCall = backupLongTermRetentionVaultsListByServerValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, null);
        Type localVarReturnType = new TypeToken<BackupLongTermRetentionVaultListResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets server backup long term retention vaults in a server
     * @param apiVersion The API version to use for the request. (required)
     * @param subscriptionId The subscription ID that identifies an Azure subscription. (required)
     * @param resourceGroupName The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. (required)
     * @param serverName The name of the server. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call backupLongTermRetentionVaultsListByServerAsync(String apiVersion, String subscriptionId, String resourceGroupName, String serverName, final ApiCallback<BackupLongTermRetentionVaultListResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = backupLongTermRetentionVaultsListByServerValidateBeforeCall(apiVersion, subscriptionId, resourceGroupName, serverName, _callback);
        Type localVarReturnType = new TypeToken<BackupLongTermRetentionVaultListResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
