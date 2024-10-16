/*
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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


import org.openapitools.client.model.APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest;
import org.openapitools.client.model.APIModelsApiError;
import org.openapitools.client.model.GlobalResourcesSharedModelsTranslationRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TranslationRequestsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public TranslationRequestsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TranslationRequestsApi(ApiClient apiClient) {
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
     * Build call for translationRequestsCreateTranslationRequest
     * @param globalResourcesSharedModelsTranslationRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call translationRequestsCreateTranslationRequestCall(GlobalResourcesSharedModelsTranslationRequest globalResourcesSharedModelsTranslationRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = globalResourcesSharedModelsTranslationRequest;

        // create path and map variables
        String localVarPath = "/api/v2/TranslationRequests";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
            "application/json",
            "application/x-www-form-urlencoded",
            "application/xml",
            "text/json",
            "text/xml"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call translationRequestsCreateTranslationRequestValidateBeforeCall(GlobalResourcesSharedModelsTranslationRequest globalResourcesSharedModelsTranslationRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'globalResourcesSharedModelsTranslationRequest' is set
        if (globalResourcesSharedModelsTranslationRequest == null) {
            throw new ApiException("Missing the required parameter 'globalResourcesSharedModelsTranslationRequest' when calling translationRequestsCreateTranslationRequest(Async)");
        }

        return translationRequestsCreateTranslationRequestCall(globalResourcesSharedModelsTranslationRequest, _callback);

    }

    /**
     * Create a translation request. Accepts a TranslationRequest object. Returns the Id of the created object. The state of the TranslationRequest must be ‘NotSubmitted’.
     * No Documentation Found.
     * @param globalResourcesSharedModelsTranslationRequest  (required)
     * @return Integer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public Integer translationRequestsCreateTranslationRequest(GlobalResourcesSharedModelsTranslationRequest globalResourcesSharedModelsTranslationRequest) throws ApiException {
        ApiResponse<Integer> localVarResp = translationRequestsCreateTranslationRequestWithHttpInfo(globalResourcesSharedModelsTranslationRequest);
        return localVarResp.getData();
    }

    /**
     * Create a translation request. Accepts a TranslationRequest object. Returns the Id of the created object. The state of the TranslationRequest must be ‘NotSubmitted’.
     * No Documentation Found.
     * @param globalResourcesSharedModelsTranslationRequest  (required)
     * @return ApiResponse&lt;Integer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Integer> translationRequestsCreateTranslationRequestWithHttpInfo(GlobalResourcesSharedModelsTranslationRequest globalResourcesSharedModelsTranslationRequest) throws ApiException {
        okhttp3.Call localVarCall = translationRequestsCreateTranslationRequestValidateBeforeCall(globalResourcesSharedModelsTranslationRequest, null);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a translation request. Accepts a TranslationRequest object. Returns the Id of the created object. The state of the TranslationRequest must be ‘NotSubmitted’. (asynchronously)
     * No Documentation Found.
     * @param globalResourcesSharedModelsTranslationRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call translationRequestsCreateTranslationRequestAsync(GlobalResourcesSharedModelsTranslationRequest globalResourcesSharedModelsTranslationRequest, final ApiCallback<Integer> _callback) throws ApiException {

        okhttp3.Call localVarCall = translationRequestsCreateTranslationRequestValidateBeforeCall(globalResourcesSharedModelsTranslationRequest, _callback);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for translationRequestsGetTranslationRequest
     * @param id  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call translationRequestsGetTranslationRequestCall(Integer id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v2/TranslationRequests/{Id}"
            .replace("{" + "Id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
    private okhttp3.Call translationRequestsGetTranslationRequestValidateBeforeCall(Integer id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling translationRequestsGetTranslationRequest(Async)");
        }

        return translationRequestsGetTranslationRequestCall(id, _callback);

    }

    /**
     * Get a TranslationRequest object by id. Returns TranslationRequest object with its language ids and string ids.
     * No Documentation Found.
     * @param id  (required)
     * @return GlobalResourcesSharedModelsTranslationRequest
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public GlobalResourcesSharedModelsTranslationRequest translationRequestsGetTranslationRequest(Integer id) throws ApiException {
        ApiResponse<GlobalResourcesSharedModelsTranslationRequest> localVarResp = translationRequestsGetTranslationRequestWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Get a TranslationRequest object by id. Returns TranslationRequest object with its language ids and string ids.
     * No Documentation Found.
     * @param id  (required)
     * @return ApiResponse&lt;GlobalResourcesSharedModelsTranslationRequest&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GlobalResourcesSharedModelsTranslationRequest> translationRequestsGetTranslationRequestWithHttpInfo(Integer id) throws ApiException {
        okhttp3.Call localVarCall = translationRequestsGetTranslationRequestValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<GlobalResourcesSharedModelsTranslationRequest>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a TranslationRequest object by id. Returns TranslationRequest object with its language ids and string ids. (asynchronously)
     * No Documentation Found.
     * @param id  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call translationRequestsGetTranslationRequestAsync(Integer id, final ApiCallback<GlobalResourcesSharedModelsTranslationRequest> _callback) throws ApiException {

        okhttp3.Call localVarCall = translationRequestsGetTranslationRequestValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<GlobalResourcesSharedModelsTranslationRequest>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for translationRequestsGetTranslationRequests
     * @param limit  (optional)
     * @param offset  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call translationRequestsGetTranslationRequestsCall(Integer limit, Integer offset, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v2/TranslationRequests";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
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
    private okhttp3.Call translationRequestsGetTranslationRequestsValidateBeforeCall(Integer limit, Integer offset, final ApiCallback _callback) throws ApiException {
        return translationRequestsGetTranslationRequestsCall(limit, offset, _callback);

    }

    /**
     * Get all TranslationRequest objects. Returns a PagedResponse of TranslationRequest objects with their language ids and string ids.
     * No Documentation Found.
     * @param limit  (optional)
     * @param offset  (optional)
     * @return APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest translationRequestsGetTranslationRequests(Integer limit, Integer offset) throws ApiException {
        ApiResponse<APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest> localVarResp = translationRequestsGetTranslationRequestsWithHttpInfo(limit, offset);
        return localVarResp.getData();
    }

    /**
     * Get all TranslationRequest objects. Returns a PagedResponse of TranslationRequest objects with their language ids and string ids.
     * No Documentation Found.
     * @param limit  (optional)
     * @param offset  (optional)
     * @return ApiResponse&lt;APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest> translationRequestsGetTranslationRequestsWithHttpInfo(Integer limit, Integer offset) throws ApiException {
        okhttp3.Call localVarCall = translationRequestsGetTranslationRequestsValidateBeforeCall(limit, offset, null);
        Type localVarReturnType = new TypeToken<APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get all TranslationRequest objects. Returns a PagedResponse of TranslationRequest objects with their language ids and string ids. (asynchronously)
     * No Documentation Found.
     * @param limit  (optional)
     * @param offset  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call translationRequestsGetTranslationRequestsAsync(Integer limit, Integer offset, final ApiCallback<APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest> _callback) throws ApiException {

        okhttp3.Call localVarCall = translationRequestsGetTranslationRequestsValidateBeforeCall(limit, offset, _callback);
        Type localVarReturnType = new TypeToken<APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for translationRequestsUpdateTranslationRequest
     * @param id  (required)
     * @param globalResourcesSharedModelsTranslationRequest  (required)
     * @param doResendRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call translationRequestsUpdateTranslationRequestCall(Integer id, GlobalResourcesSharedModelsTranslationRequest globalResourcesSharedModelsTranslationRequest, Boolean doResendRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = globalResourcesSharedModelsTranslationRequest;

        // create path and map variables
        String localVarPath = "/api/v2/TranslationRequests/{Id}"
            .replace("{" + "Id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (doResendRequest != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doResendRequest", doResendRequest));
        }

        final String[] localVarAccepts = {
            "*/*"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json",
            "application/x-www-form-urlencoded",
            "application/xml",
            "text/json",
            "text/xml"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call translationRequestsUpdateTranslationRequestValidateBeforeCall(Integer id, GlobalResourcesSharedModelsTranslationRequest globalResourcesSharedModelsTranslationRequest, Boolean doResendRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling translationRequestsUpdateTranslationRequest(Async)");
        }

        // verify the required parameter 'globalResourcesSharedModelsTranslationRequest' is set
        if (globalResourcesSharedModelsTranslationRequest == null) {
            throw new ApiException("Missing the required parameter 'globalResourcesSharedModelsTranslationRequest' when calling translationRequestsUpdateTranslationRequest(Async)");
        }

        return translationRequestsUpdateTranslationRequestCall(id, globalResourcesSharedModelsTranslationRequest, doResendRequest, _callback);

    }

    /**
     * Update a TranslationRequest object by id. Accepts a TranslationRequest object.
     * No Documentation Found.
     * @param id  (required)
     * @param globalResourcesSharedModelsTranslationRequest  (required)
     * @param doResendRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public void translationRequestsUpdateTranslationRequest(Integer id, GlobalResourcesSharedModelsTranslationRequest globalResourcesSharedModelsTranslationRequest, Boolean doResendRequest) throws ApiException {
        translationRequestsUpdateTranslationRequestWithHttpInfo(id, globalResourcesSharedModelsTranslationRequest, doResendRequest);
    }

    /**
     * Update a TranslationRequest object by id. Accepts a TranslationRequest object.
     * No Documentation Found.
     * @param id  (required)
     * @param globalResourcesSharedModelsTranslationRequest  (required)
     * @param doResendRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> translationRequestsUpdateTranslationRequestWithHttpInfo(Integer id, GlobalResourcesSharedModelsTranslationRequest globalResourcesSharedModelsTranslationRequest, Boolean doResendRequest) throws ApiException {
        okhttp3.Call localVarCall = translationRequestsUpdateTranslationRequestValidateBeforeCall(id, globalResourcesSharedModelsTranslationRequest, doResendRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update a TranslationRequest object by id. Accepts a TranslationRequest object. (asynchronously)
     * No Documentation Found.
     * @param id  (required)
     * @param globalResourcesSharedModelsTranslationRequest  (required)
     * @param doResendRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call translationRequestsUpdateTranslationRequestAsync(Integer id, GlobalResourcesSharedModelsTranslationRequest globalResourcesSharedModelsTranslationRequest, Boolean doResendRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = translationRequestsUpdateTranslationRequestValidateBeforeCall(id, globalResourcesSharedModelsTranslationRequest, doResendRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for translationRequestsUpdateTranslationRequestStrings
     * @param id  (required)
     * @param requestBody  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call translationRequestsUpdateTranslationRequestStringsCall(Integer id, List<String> requestBody, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = requestBody;

        // create path and map variables
        String localVarPath = "/api/v2/TranslationRequests/{Id}/Strings"
            .replace("{" + "Id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "*/*"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json",
            "application/x-www-form-urlencoded",
            "application/xml",
            "text/json",
            "text/xml"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call translationRequestsUpdateTranslationRequestStringsValidateBeforeCall(Integer id, List<String> requestBody, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling translationRequestsUpdateTranslationRequestStrings(Async)");
        }

        // verify the required parameter 'requestBody' is set
        if (requestBody == null) {
            throw new ApiException("Missing the required parameter 'requestBody' when calling translationRequestsUpdateTranslationRequestStrings(Async)");
        }

        return translationRequestsUpdateTranslationRequestStringsCall(id, requestBody, _callback);

    }

    /**
     * No Documentation Found.
     * No Documentation Found.
     * @param id  (required)
     * @param requestBody  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public void translationRequestsUpdateTranslationRequestStrings(Integer id, List<String> requestBody) throws ApiException {
        translationRequestsUpdateTranslationRequestStringsWithHttpInfo(id, requestBody);
    }

    /**
     * No Documentation Found.
     * No Documentation Found.
     * @param id  (required)
     * @param requestBody  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> translationRequestsUpdateTranslationRequestStringsWithHttpInfo(Integer id, List<String> requestBody) throws ApiException {
        okhttp3.Call localVarCall = translationRequestsUpdateTranslationRequestStringsValidateBeforeCall(id, requestBody, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * No Documentation Found. (asynchronously)
     * No Documentation Found.
     * @param id  (required)
     * @param requestBody  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> API Error Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call translationRequestsUpdateTranslationRequestStringsAsync(Integer id, List<String> requestBody, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = translationRequestsUpdateTranslationRequestStringsValidateBeforeCall(id, requestBody, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
