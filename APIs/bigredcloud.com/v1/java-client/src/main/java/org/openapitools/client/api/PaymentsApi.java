/*
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
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


import org.openapitools.client.model.BatchItemPaymentDto;
import org.openapitools.client.model.PageResultPaymentQueryDto;
import org.openapitools.client.model.PaymentDto;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PaymentsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public PaymentsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public PaymentsApi(ApiClient apiClient) {
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
     * Build call for paymentsDelete
     * @param id Id of Payment to remove. (required)
     * @param timestamp Timestamp of Payment to remove. Should be encoded in Base64. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentsDeleteCall(Long id, String timestamp, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/payments/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (timestamp != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("timestamp", timestamp));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call paymentsDeleteValidateBeforeCall(Long id, String timestamp, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling paymentsDelete(Async)");
        }

        // verify the required parameter 'timestamp' is set
        if (timestamp == null) {
            throw new ApiException("Missing the required parameter 'timestamp' when calling paymentsDelete(Async)");
        }

        return paymentsDeleteCall(id, timestamp, _callback);

    }

    /**
     * Removes an existing Payment.
     * 
     * @param id Id of Payment to remove. (required)
     * @param timestamp Timestamp of Payment to remove. Should be encoded in Base64. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object paymentsDelete(Long id, String timestamp) throws ApiException {
        ApiResponse<Object> localVarResp = paymentsDeleteWithHttpInfo(id, timestamp);
        return localVarResp.getData();
    }

    /**
     * Removes an existing Payment.
     * 
     * @param id Id of Payment to remove. (required)
     * @param timestamp Timestamp of Payment to remove. Should be encoded in Base64. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> paymentsDeleteWithHttpInfo(Long id, String timestamp) throws ApiException {
        okhttp3.Call localVarCall = paymentsDeleteValidateBeforeCall(id, timestamp, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Removes an existing Payment. (asynchronously)
     * 
     * @param id Id of Payment to remove. (required)
     * @param timestamp Timestamp of Payment to remove. Should be encoded in Base64. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentsDeleteAsync(Long id, String timestamp, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = paymentsDeleteValidateBeforeCall(id, timestamp, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for paymentsGet
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentsGetCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/payments";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
    private okhttp3.Call paymentsGetValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return paymentsGetCall(_callback);

    }

    /**
     * Returns a list of company&#39;s Payments. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.
     * 
     * @return PageResultPaymentQueryDto
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public PageResultPaymentQueryDto paymentsGet() throws ApiException {
        ApiResponse<PageResultPaymentQueryDto> localVarResp = paymentsGetWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Returns a list of company&#39;s Payments. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.
     * 
     * @return ApiResponse&lt;PageResultPaymentQueryDto&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PageResultPaymentQueryDto> paymentsGetWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = paymentsGetValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<PageResultPaymentQueryDto>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Returns a list of company&#39;s Payments. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field. (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentsGetAsync(final ApiCallback<PageResultPaymentQueryDto> _callback) throws ApiException {

        okhttp3.Call localVarCall = paymentsGetValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<PageResultPaymentQueryDto>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for paymentsPost
     * @param paymentDto Information of Payment to create. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentsPostCall(PaymentDto paymentDto, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = paymentDto;

        // create path and map variables
        String localVarPath = "/v1/payments";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call paymentsPostValidateBeforeCall(PaymentDto paymentDto, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'paymentDto' is set
        if (paymentDto == null) {
            throw new ApiException("Missing the required parameter 'paymentDto' when calling paymentsPost(Async)");
        }

        return paymentsPostCall(paymentDto, _callback);

    }

    /**
     * Creates a new Payment.
     * 
     * @param paymentDto Information of Payment to create. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object paymentsPost(PaymentDto paymentDto) throws ApiException {
        ApiResponse<Object> localVarResp = paymentsPostWithHttpInfo(paymentDto);
        return localVarResp.getData();
    }

    /**
     * Creates a new Payment.
     * 
     * @param paymentDto Information of Payment to create. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> paymentsPostWithHttpInfo(PaymentDto paymentDto) throws ApiException {
        okhttp3.Call localVarCall = paymentsPostValidateBeforeCall(paymentDto, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Creates a new Payment. (asynchronously)
     * 
     * @param paymentDto Information of Payment to create. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentsPostAsync(PaymentDto paymentDto, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = paymentsPostValidateBeforeCall(paymentDto, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for paymentsProcessBatch
     * @param batchItemPaymentDto Batch of Payments to process. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentsProcessBatchCall(List<BatchItemPaymentDto> batchItemPaymentDto, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = batchItemPaymentDto;

        // create path and map variables
        String localVarPath = "/v1/payments/batch";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
    private okhttp3.Call paymentsProcessBatchValidateBeforeCall(List<BatchItemPaymentDto> batchItemPaymentDto, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'batchItemPaymentDto' is set
        if (batchItemPaymentDto == null) {
            throw new ApiException("Missing the required parameter 'batchItemPaymentDto' when calling paymentsProcessBatch(Async)");
        }

        return paymentsProcessBatchCall(batchItemPaymentDto, _callback);

    }

    /**
     * Processes a batch of Payments.
     * 
     * @param batchItemPaymentDto Batch of Payments to process. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object paymentsProcessBatch(List<BatchItemPaymentDto> batchItemPaymentDto) throws ApiException {
        ApiResponse<Object> localVarResp = paymentsProcessBatchWithHttpInfo(batchItemPaymentDto);
        return localVarResp.getData();
    }

    /**
     * Processes a batch of Payments.
     * 
     * @param batchItemPaymentDto Batch of Payments to process. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> paymentsProcessBatchWithHttpInfo(List<BatchItemPaymentDto> batchItemPaymentDto) throws ApiException {
        okhttp3.Call localVarCall = paymentsProcessBatchValidateBeforeCall(batchItemPaymentDto, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Processes a batch of Payments. (asynchronously)
     * 
     * @param batchItemPaymentDto Batch of Payments to process. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentsProcessBatchAsync(List<BatchItemPaymentDto> batchItemPaymentDto, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = paymentsProcessBatchValidateBeforeCall(batchItemPaymentDto, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for paymentsPut
     * @param id Id of Payment to update. (required)
     * @param paymentDto Information of Payment to update. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentsPutCall(Long id, PaymentDto paymentDto, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = paymentDto;

        // create path and map variables
        String localVarPath = "/v1/payments/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
    private okhttp3.Call paymentsPutValidateBeforeCall(Long id, PaymentDto paymentDto, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling paymentsPut(Async)");
        }

        // verify the required parameter 'paymentDto' is set
        if (paymentDto == null) {
            throw new ApiException("Missing the required parameter 'paymentDto' when calling paymentsPut(Async)");
        }

        return paymentsPutCall(id, paymentDto, _callback);

    }

    /**
     * Updates an existing Payment.
     * 
     * @param id Id of Payment to update. (required)
     * @param paymentDto Information of Payment to update. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object paymentsPut(Long id, PaymentDto paymentDto) throws ApiException {
        ApiResponse<Object> localVarResp = paymentsPutWithHttpInfo(id, paymentDto);
        return localVarResp.getData();
    }

    /**
     * Updates an existing Payment.
     * 
     * @param id Id of Payment to update. (required)
     * @param paymentDto Information of Payment to update. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> paymentsPutWithHttpInfo(Long id, PaymentDto paymentDto) throws ApiException {
        okhttp3.Call localVarCall = paymentsPutValidateBeforeCall(id, paymentDto, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Updates an existing Payment. (asynchronously)
     * 
     * @param id Id of Payment to update. (required)
     * @param paymentDto Information of Payment to update. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentsPutAsync(Long id, PaymentDto paymentDto, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = paymentsPutValidateBeforeCall(id, paymentDto, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for v1PaymentsIdGet
     * @param id Id of Payment to return. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call v1PaymentsIdGetCall(Long id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/payments/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

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
    private okhttp3.Call v1PaymentsIdGetValidateBeforeCall(Long id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling v1PaymentsIdGet(Async)");
        }

        return v1PaymentsIdGetCall(id, _callback);

    }

    /**
     * Returns information about a single Payments.
     * 
     * @param id Id of Payment to return. (required)
     * @return PaymentDto
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public PaymentDto v1PaymentsIdGet(Long id) throws ApiException {
        ApiResponse<PaymentDto> localVarResp = v1PaymentsIdGetWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Returns information about a single Payments.
     * 
     * @param id Id of Payment to return. (required)
     * @return ApiResponse&lt;PaymentDto&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PaymentDto> v1PaymentsIdGetWithHttpInfo(Long id) throws ApiException {
        okhttp3.Call localVarCall = v1PaymentsIdGetValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<PaymentDto>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Returns information about a single Payments. (asynchronously)
     * 
     * @param id Id of Payment to return. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call v1PaymentsIdGetAsync(Long id, final ApiCallback<PaymentDto> _callback) throws ApiException {

        okhttp3.Call localVarCall = v1PaymentsIdGetValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<PaymentDto>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
