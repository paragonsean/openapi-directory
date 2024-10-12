/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
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


import org.openapitools.client.model.ErrorSchema;
import org.openapitools.client.model.Run;
import org.openapitools.client.model.RunRequest;
import org.openapitools.client.model.SourceUploadDefinition;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class RegistriesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public RegistriesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public RegistriesApi(ApiClient apiClient) {
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
     * Build call for registriesGetBuildSourceUploadUrl
     * @param subscriptionId The Microsoft Azure subscription ID. (required)
     * @param resourceGroupName The name of the resource group to which the container registry belongs. (required)
     * @param registryName The name of the container registry. (required)
     * @param apiVersion The client API version. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful; the request was well-formed and received properly. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. If the registry doesn&#39;t exist, 404 (Not found) is returned. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call registriesGetBuildSourceUploadUrlCall(String subscriptionId, String resourceGroupName, String registryName, String apiVersion, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/listBuildSourceUploadUrl"
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()))
            .replace("{" + "resourceGroupName" + "}", localVarApiClient.escapeString(resourceGroupName.toString()))
            .replace("{" + "registryName" + "}", localVarApiClient.escapeString(registryName.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call registriesGetBuildSourceUploadUrlValidateBeforeCall(String subscriptionId, String resourceGroupName, String registryName, String apiVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling registriesGetBuildSourceUploadUrl(Async)");
        }

        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling registriesGetBuildSourceUploadUrl(Async)");
        }

        // verify the required parameter 'registryName' is set
        if (registryName == null) {
            throw new ApiException("Missing the required parameter 'registryName' when calling registriesGetBuildSourceUploadUrl(Async)");
        }

        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling registriesGetBuildSourceUploadUrl(Async)");
        }

        return registriesGetBuildSourceUploadUrlCall(subscriptionId, resourceGroupName, registryName, apiVersion, _callback);

    }

    /**
     * 
     * Get the upload location for the user to be able to upload the source.
     * @param subscriptionId The Microsoft Azure subscription ID. (required)
     * @param resourceGroupName The name of the resource group to which the container registry belongs. (required)
     * @param registryName The name of the container registry. (required)
     * @param apiVersion The client API version. (required)
     * @return SourceUploadDefinition
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful; the request was well-formed and received properly. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. If the registry doesn&#39;t exist, 404 (Not found) is returned. </td><td>  -  </td></tr>
     </table>
     */
    public SourceUploadDefinition registriesGetBuildSourceUploadUrl(String subscriptionId, String resourceGroupName, String registryName, String apiVersion) throws ApiException {
        ApiResponse<SourceUploadDefinition> localVarResp = registriesGetBuildSourceUploadUrlWithHttpInfo(subscriptionId, resourceGroupName, registryName, apiVersion);
        return localVarResp.getData();
    }

    /**
     * 
     * Get the upload location for the user to be able to upload the source.
     * @param subscriptionId The Microsoft Azure subscription ID. (required)
     * @param resourceGroupName The name of the resource group to which the container registry belongs. (required)
     * @param registryName The name of the container registry. (required)
     * @param apiVersion The client API version. (required)
     * @return ApiResponse&lt;SourceUploadDefinition&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful; the request was well-formed and received properly. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. If the registry doesn&#39;t exist, 404 (Not found) is returned. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SourceUploadDefinition> registriesGetBuildSourceUploadUrlWithHttpInfo(String subscriptionId, String resourceGroupName, String registryName, String apiVersion) throws ApiException {
        okhttp3.Call localVarCall = registriesGetBuildSourceUploadUrlValidateBeforeCall(subscriptionId, resourceGroupName, registryName, apiVersion, null);
        Type localVarReturnType = new TypeToken<SourceUploadDefinition>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Get the upload location for the user to be able to upload the source.
     * @param subscriptionId The Microsoft Azure subscription ID. (required)
     * @param resourceGroupName The name of the resource group to which the container registry belongs. (required)
     * @param registryName The name of the container registry. (required)
     * @param apiVersion The client API version. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful; the request was well-formed and received properly. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. If the registry doesn&#39;t exist, 404 (Not found) is returned. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call registriesGetBuildSourceUploadUrlAsync(String subscriptionId, String resourceGroupName, String registryName, String apiVersion, final ApiCallback<SourceUploadDefinition> _callback) throws ApiException {

        okhttp3.Call localVarCall = registriesGetBuildSourceUploadUrlValidateBeforeCall(subscriptionId, resourceGroupName, registryName, apiVersion, _callback);
        Type localVarReturnType = new TypeToken<SourceUploadDefinition>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for registriesScheduleRun
     * @param subscriptionId The Microsoft Azure subscription ID. (required)
     * @param resourceGroupName The name of the resource group to which the container registry belongs. (required)
     * @param registryName The name of the container registry. (required)
     * @param apiVersion The client API version. (required)
     * @param runRequest The parameters of a run that needs to scheduled. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful; the request was well-formed and received properly. </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> The request was successfully accepted; the operation will complete asynchronously. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. If the registry/run doesn&#39;t exist, 404 (Not found) is returned. If any of the input parameters is wrong, 400(Bad Request) is returned. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call registriesScheduleRunCall(String subscriptionId, String resourceGroupName, String registryName, String apiVersion, RunRequest runRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = runRequest;

        // create path and map variables
        String localVarPath = "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/scheduleRun"
            .replace("{" + "subscriptionId" + "}", localVarApiClient.escapeString(subscriptionId.toString()))
            .replace("{" + "resourceGroupName" + "}", localVarApiClient.escapeString(resourceGroupName.toString()))
            .replace("{" + "registryName" + "}", localVarApiClient.escapeString(registryName.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call registriesScheduleRunValidateBeforeCall(String subscriptionId, String resourceGroupName, String registryName, String apiVersion, RunRequest runRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling registriesScheduleRun(Async)");
        }

        // verify the required parameter 'resourceGroupName' is set
        if (resourceGroupName == null) {
            throw new ApiException("Missing the required parameter 'resourceGroupName' when calling registriesScheduleRun(Async)");
        }

        // verify the required parameter 'registryName' is set
        if (registryName == null) {
            throw new ApiException("Missing the required parameter 'registryName' when calling registriesScheduleRun(Async)");
        }

        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling registriesScheduleRun(Async)");
        }

        // verify the required parameter 'runRequest' is set
        if (runRequest == null) {
            throw new ApiException("Missing the required parameter 'runRequest' when calling registriesScheduleRun(Async)");
        }

        return registriesScheduleRunCall(subscriptionId, resourceGroupName, registryName, apiVersion, runRequest, _callback);

    }

    /**
     * 
     * Schedules a new run based on the request parameters and add it to the run queue.
     * @param subscriptionId The Microsoft Azure subscription ID. (required)
     * @param resourceGroupName The name of the resource group to which the container registry belongs. (required)
     * @param registryName The name of the container registry. (required)
     * @param apiVersion The client API version. (required)
     * @param runRequest The parameters of a run that needs to scheduled. (required)
     * @return Run
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful; the request was well-formed and received properly. </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> The request was successfully accepted; the operation will complete asynchronously. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. If the registry/run doesn&#39;t exist, 404 (Not found) is returned. If any of the input parameters is wrong, 400(Bad Request) is returned. </td><td>  -  </td></tr>
     </table>
     */
    public Run registriesScheduleRun(String subscriptionId, String resourceGroupName, String registryName, String apiVersion, RunRequest runRequest) throws ApiException {
        ApiResponse<Run> localVarResp = registriesScheduleRunWithHttpInfo(subscriptionId, resourceGroupName, registryName, apiVersion, runRequest);
        return localVarResp.getData();
    }

    /**
     * 
     * Schedules a new run based on the request parameters and add it to the run queue.
     * @param subscriptionId The Microsoft Azure subscription ID. (required)
     * @param resourceGroupName The name of the resource group to which the container registry belongs. (required)
     * @param registryName The name of the container registry. (required)
     * @param apiVersion The client API version. (required)
     * @param runRequest The parameters of a run that needs to scheduled. (required)
     * @return ApiResponse&lt;Run&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful; the request was well-formed and received properly. </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> The request was successfully accepted; the operation will complete asynchronously. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. If the registry/run doesn&#39;t exist, 404 (Not found) is returned. If any of the input parameters is wrong, 400(Bad Request) is returned. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Run> registriesScheduleRunWithHttpInfo(String subscriptionId, String resourceGroupName, String registryName, String apiVersion, RunRequest runRequest) throws ApiException {
        okhttp3.Call localVarCall = registriesScheduleRunValidateBeforeCall(subscriptionId, resourceGroupName, registryName, apiVersion, runRequest, null);
        Type localVarReturnType = new TypeToken<Run>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Schedules a new run based on the request parameters and add it to the run queue.
     * @param subscriptionId The Microsoft Azure subscription ID. (required)
     * @param resourceGroupName The name of the resource group to which the container registry belongs. (required)
     * @param registryName The name of the container registry. (required)
     * @param apiVersion The client API version. (required)
     * @param runRequest The parameters of a run that needs to scheduled. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The request was successful; the request was well-formed and received properly. </td><td>  -  </td></tr>
        <tr><td> 202 </td><td> The request was successfully accepted; the operation will complete asynchronously. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. If the registry/run doesn&#39;t exist, 404 (Not found) is returned. If any of the input parameters is wrong, 400(Bad Request) is returned. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call registriesScheduleRunAsync(String subscriptionId, String resourceGroupName, String registryName, String apiVersion, RunRequest runRequest, final ApiCallback<Run> _callback) throws ApiException {

        okhttp3.Call localVarCall = registriesScheduleRunValidateBeforeCall(subscriptionId, resourceGroupName, registryName, apiVersion, runRequest, _callback);
        Type localVarReturnType = new TypeToken<Run>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
