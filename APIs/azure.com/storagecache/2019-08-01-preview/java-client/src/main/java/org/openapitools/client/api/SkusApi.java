/*
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage caches.
 *
 * The version of the OpenAPI document: 2019-08-01-preview
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
import org.openapitools.client.model.ResourceSkusResult;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SkusApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SkusApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SkusApi(ApiClient apiClient) {
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
     * Build call for skusList
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of SKU descriptors. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call skusListCall(String apiVersion, String subscriptionId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{subscriptionId}/providers/Microsoft.StorageCache/skus"
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
    private okhttp3.Call skusListValidateBeforeCall(String apiVersion, String subscriptionId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'apiVersion' is set
        if (apiVersion == null) {
            throw new ApiException("Missing the required parameter 'apiVersion' when calling skusList(Async)");
        }

        // verify the required parameter 'subscriptionId' is set
        if (subscriptionId == null) {
            throw new ApiException("Missing the required parameter 'subscriptionId' when calling skusList(Async)");
        }

        return skusListCall(apiVersion, subscriptionId, _callback);

    }

    /**
     * 
     * Get the list of StorageCache.Cache SKUs available to this subscription.
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. (required)
     * @return ResourceSkusResult
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of SKU descriptors. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public ResourceSkusResult skusList(String apiVersion, String subscriptionId) throws ApiException {
        ApiResponse<ResourceSkusResult> localVarResp = skusListWithHttpInfo(apiVersion, subscriptionId);
        return localVarResp.getData();
    }

    /**
     * 
     * Get the list of StorageCache.Cache SKUs available to this subscription.
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. (required)
     * @return ApiResponse&lt;ResourceSkusResult&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of SKU descriptors. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ResourceSkusResult> skusListWithHttpInfo(String apiVersion, String subscriptionId) throws ApiException {
        okhttp3.Call localVarCall = skusListValidateBeforeCall(apiVersion, subscriptionId, null);
        Type localVarReturnType = new TypeToken<ResourceSkusResult>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Get the list of StorageCache.Cache SKUs available to this subscription.
     * @param apiVersion Client Api Version. (required)
     * @param subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of SKU descriptors. </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Error response describing why the operation failed. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call skusListAsync(String apiVersion, String subscriptionId, final ApiCallback<ResourceSkusResult> _callback) throws ApiException {

        okhttp3.Call localVarCall = skusListValidateBeforeCall(apiVersion, subscriptionId, _callback);
        Type localVarReturnType = new TypeToken<ResourceSkusResult>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
