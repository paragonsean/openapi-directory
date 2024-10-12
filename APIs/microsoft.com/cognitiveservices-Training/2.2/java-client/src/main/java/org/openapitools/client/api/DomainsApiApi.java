/*
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.2
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


import org.openapitools.client.model.Domain;
import java.util.UUID;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DomainsApiApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DomainsApiApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DomainsApiApi(ApiClient apiClient) {
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
     * Build call for getDomain
     * @param domainId The id of the domain to get information about. (required)
     * @param trainingKey  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainCall(UUID domainId, String trainingKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/domains/{domainId}"
            .replace("{" + "domainId" + "}", localVarApiClient.escapeString(domainId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (trainingKey != null) {
            localVarHeaderParams.put("Training-Key", localVarApiClient.parameterToString(trainingKey));
        }

        final String[] localVarAccepts = {
            "application/json",
            "application/xml",
            "text/json",
            "text/xml"
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
    private okhttp3.Call getDomainValidateBeforeCall(UUID domainId, String trainingKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainId' is set
        if (domainId == null) {
            throw new ApiException("Missing the required parameter 'domainId' when calling getDomain(Async)");
        }

        // verify the required parameter 'trainingKey' is set
        if (trainingKey == null) {
            throw new ApiException("Missing the required parameter 'trainingKey' when calling getDomain(Async)");
        }

        return getDomainCall(domainId, trainingKey, _callback);

    }

    /**
     * Get information about a specific domain.
     * 
     * @param domainId The id of the domain to get information about. (required)
     * @param trainingKey  (required)
     * @return Domain
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Domain getDomain(UUID domainId, String trainingKey) throws ApiException {
        ApiResponse<Domain> localVarResp = getDomainWithHttpInfo(domainId, trainingKey);
        return localVarResp.getData();
    }

    /**
     * Get information about a specific domain.
     * 
     * @param domainId The id of the domain to get information about. (required)
     * @param trainingKey  (required)
     * @return ApiResponse&lt;Domain&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Domain> getDomainWithHttpInfo(UUID domainId, String trainingKey) throws ApiException {
        okhttp3.Call localVarCall = getDomainValidateBeforeCall(domainId, trainingKey, null);
        Type localVarReturnType = new TypeToken<Domain>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get information about a specific domain. (asynchronously)
     * 
     * @param domainId The id of the domain to get information about. (required)
     * @param trainingKey  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainAsync(UUID domainId, String trainingKey, final ApiCallback<Domain> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDomainValidateBeforeCall(domainId, trainingKey, _callback);
        Type localVarReturnType = new TypeToken<Domain>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDomains
     * @param trainingKey  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainsCall(String trainingKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/domains";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (trainingKey != null) {
            localVarHeaderParams.put("Training-Key", localVarApiClient.parameterToString(trainingKey));
        }

        final String[] localVarAccepts = {
            "application/json",
            "application/xml",
            "text/json",
            "text/xml"
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
    private okhttp3.Call getDomainsValidateBeforeCall(String trainingKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'trainingKey' is set
        if (trainingKey == null) {
            throw new ApiException("Missing the required parameter 'trainingKey' when calling getDomains(Async)");
        }

        return getDomainsCall(trainingKey, _callback);

    }

    /**
     * Get a list of the available domains.
     * 
     * @param trainingKey  (required)
     * @return List&lt;Domain&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<Domain> getDomains(String trainingKey) throws ApiException {
        ApiResponse<List<Domain>> localVarResp = getDomainsWithHttpInfo(trainingKey);
        return localVarResp.getData();
    }

    /**
     * Get a list of the available domains.
     * 
     * @param trainingKey  (required)
     * @return ApiResponse&lt;List&lt;Domain&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Domain>> getDomainsWithHttpInfo(String trainingKey) throws ApiException {
        okhttp3.Call localVarCall = getDomainsValidateBeforeCall(trainingKey, null);
        Type localVarReturnType = new TypeToken<List<Domain>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a list of the available domains. (asynchronously)
     * 
     * @param trainingKey  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDomainsAsync(String trainingKey, final ApiCallback<List<Domain>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDomainsValidateBeforeCall(trainingKey, _callback);
        Type localVarReturnType = new TypeToken<List<Domain>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
