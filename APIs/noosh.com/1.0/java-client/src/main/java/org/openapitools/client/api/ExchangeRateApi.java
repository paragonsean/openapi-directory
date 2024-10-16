/*
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
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


import org.openapitools.client.model.HTTPStatusVO;
import org.openapitools.client.model.MultiExchangeRateListVO;
import org.openapitools.client.model.MultiExchangeRatePersistListVO;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ExchangeRateApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ExchangeRateApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ExchangeRateApi(ApiClient apiClient) {
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
     * Build call for getExchangeRateList
     * @param workgroupId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful updated </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getExchangeRateListCall(String workgroupId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/workgroups/{workgroup_id}/exchangeRate"
            .replace("{" + "workgroup_id" + "}", localVarApiClient.escapeString(workgroupId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "*/*",
            "application/json",
            "application/x-json-smile",
            "application/x-yaml",
            "application/xml",
            "text/csv",
            "text/x-yaml",
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
    private okhttp3.Call getExchangeRateListValidateBeforeCall(String workgroupId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'workgroupId' is set
        if (workgroupId == null) {
            throw new ApiException("Missing the required parameter 'workgroupId' when calling getExchangeRateList(Async)");
        }

        return getExchangeRateListCall(workgroupId, _callback);

    }

    /**
     * Get Exchange Rate List
     * Get Exchange Rate List
     * @param workgroupId  (required)
     * @return MultiExchangeRateListVO
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful updated </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public MultiExchangeRateListVO getExchangeRateList(String workgroupId) throws ApiException {
        ApiResponse<MultiExchangeRateListVO> localVarResp = getExchangeRateListWithHttpInfo(workgroupId);
        return localVarResp.getData();
    }

    /**
     * Get Exchange Rate List
     * Get Exchange Rate List
     * @param workgroupId  (required)
     * @return ApiResponse&lt;MultiExchangeRateListVO&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful updated </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<MultiExchangeRateListVO> getExchangeRateListWithHttpInfo(String workgroupId) throws ApiException {
        okhttp3.Call localVarCall = getExchangeRateListValidateBeforeCall(workgroupId, null);
        Type localVarReturnType = new TypeToken<MultiExchangeRateListVO>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Exchange Rate List (asynchronously)
     * Get Exchange Rate List
     * @param workgroupId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful updated </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getExchangeRateListAsync(String workgroupId, final ApiCallback<MultiExchangeRateListVO> _callback) throws ApiException {

        okhttp3.Call localVarCall = getExchangeRateListValidateBeforeCall(workgroupId, _callback);
        Type localVarReturnType = new TypeToken<MultiExchangeRateListVO>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postExchangeRate
     * @param workgroupId  (required)
     * @param multiExchangeRatePersistListVO  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful updated </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postExchangeRateCall(String workgroupId, MultiExchangeRatePersistListVO multiExchangeRatePersistListVO, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = multiExchangeRatePersistListVO;

        // create path and map variables
        String localVarPath = "/v1/workgroups/{workgroup_id}/exchangeRate"
            .replace("{" + "workgroup_id" + "}", localVarApiClient.escapeString(workgroupId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "*/*",
            "application/json",
            "application/x-json-smile",
            "application/x-yaml",
            "application/xml",
            "text/csv",
            "text/x-yaml",
            "text/xml"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json",
            "application/x-json-smile",
            "application/x-yaml",
            "application/xml",
            "text/csv",
            "text/x-yaml",
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
    private okhttp3.Call postExchangeRateValidateBeforeCall(String workgroupId, MultiExchangeRatePersistListVO multiExchangeRatePersistListVO, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'workgroupId' is set
        if (workgroupId == null) {
            throw new ApiException("Missing the required parameter 'workgroupId' when calling postExchangeRate(Async)");
        }

        return postExchangeRateCall(workgroupId, multiExchangeRatePersistListVO, _callback);

    }

    /**
     * Create Exchange Rates
     * Create Exchange Rates
     * @param workgroupId  (required)
     * @param multiExchangeRatePersistListVO  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful updated </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public Object postExchangeRate(String workgroupId, MultiExchangeRatePersistListVO multiExchangeRatePersistListVO) throws ApiException {
        ApiResponse<Object> localVarResp = postExchangeRateWithHttpInfo(workgroupId, multiExchangeRatePersistListVO);
        return localVarResp.getData();
    }

    /**
     * Create Exchange Rates
     * Create Exchange Rates
     * @param workgroupId  (required)
     * @param multiExchangeRatePersistListVO  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful updated </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postExchangeRateWithHttpInfo(String workgroupId, MultiExchangeRatePersistListVO multiExchangeRatePersistListVO) throws ApiException {
        okhttp3.Call localVarCall = postExchangeRateValidateBeforeCall(workgroupId, multiExchangeRatePersistListVO, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create Exchange Rates (asynchronously)
     * Create Exchange Rates
     * @param workgroupId  (required)
     * @param multiExchangeRatePersistListVO  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful updated </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> There are not any result matching your search condition </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal server error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postExchangeRateAsync(String workgroupId, MultiExchangeRatePersistListVO multiExchangeRatePersistListVO, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postExchangeRateValidateBeforeCall(workgroupId, multiExchangeRatePersistListVO, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
