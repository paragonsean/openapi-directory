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


import org.openapitools.client.model.BatchItemSalesInvoiceCreditNoteDto;
import org.openapitools.client.model.PageResultSalesCreditNoteQueryDto;
import org.openapitools.client.model.SalesInvoiceCreditNoteDto;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SalesCreditNotesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SalesCreditNotesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SalesCreditNotesApi(ApiClient apiClient) {
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
     * Build call for salesCreditNotesDelete
     * @param id Id of Sales Credit Note to remove. (required)
     * @param timestamp Timestamp of Sales Credit Note to remove. Should be encoded in Base64. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call salesCreditNotesDeleteCall(Long id, String timestamp, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/salesCreditNotes/{id}"
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
    private okhttp3.Call salesCreditNotesDeleteValidateBeforeCall(Long id, String timestamp, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling salesCreditNotesDelete(Async)");
        }

        // verify the required parameter 'timestamp' is set
        if (timestamp == null) {
            throw new ApiException("Missing the required parameter 'timestamp' when calling salesCreditNotesDelete(Async)");
        }

        return salesCreditNotesDeleteCall(id, timestamp, _callback);

    }

    /**
     * Removes an existing Sales Credit Note.
     * 
     * @param id Id of Sales Credit Note to remove. (required)
     * @param timestamp Timestamp of Sales Credit Note to remove. Should be encoded in Base64. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object salesCreditNotesDelete(Long id, String timestamp) throws ApiException {
        ApiResponse<Object> localVarResp = salesCreditNotesDeleteWithHttpInfo(id, timestamp);
        return localVarResp.getData();
    }

    /**
     * Removes an existing Sales Credit Note.
     * 
     * @param id Id of Sales Credit Note to remove. (required)
     * @param timestamp Timestamp of Sales Credit Note to remove. Should be encoded in Base64. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> salesCreditNotesDeleteWithHttpInfo(Long id, String timestamp) throws ApiException {
        okhttp3.Call localVarCall = salesCreditNotesDeleteValidateBeforeCall(id, timestamp, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Removes an existing Sales Credit Note. (asynchronously)
     * 
     * @param id Id of Sales Credit Note to remove. (required)
     * @param timestamp Timestamp of Sales Credit Note to remove. Should be encoded in Base64. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call salesCreditNotesDeleteAsync(Long id, String timestamp, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = salesCreditNotesDeleteValidateBeforeCall(id, timestamp, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for salesCreditNotesGet
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call salesCreditNotesGetCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/salesCreditNotes";

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
    private okhttp3.Call salesCreditNotesGetValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return salesCreditNotesGetCall(_callback);

    }

    /**
     * Returns a list of company&#39;s Sales Credit Notes. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.
     * 
     * @return PageResultSalesCreditNoteQueryDto
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public PageResultSalesCreditNoteQueryDto salesCreditNotesGet() throws ApiException {
        ApiResponse<PageResultSalesCreditNoteQueryDto> localVarResp = salesCreditNotesGetWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Returns a list of company&#39;s Sales Credit Notes. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.
     * 
     * @return ApiResponse&lt;PageResultSalesCreditNoteQueryDto&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PageResultSalesCreditNoteQueryDto> salesCreditNotesGetWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = salesCreditNotesGetValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<PageResultSalesCreditNoteQueryDto>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Returns a list of company&#39;s Sales Credit Notes. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field. (asynchronously)
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
    public okhttp3.Call salesCreditNotesGetAsync(final ApiCallback<PageResultSalesCreditNoteQueryDto> _callback) throws ApiException {

        okhttp3.Call localVarCall = salesCreditNotesGetValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<PageResultSalesCreditNoteQueryDto>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for salesCreditNotesPost
     * @param salesInvoiceCreditNoteDto Information of Sales Credit Note to create. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call salesCreditNotesPostCall(SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = salesInvoiceCreditNoteDto;

        // create path and map variables
        String localVarPath = "/v1/salesCreditNotes";

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
    private okhttp3.Call salesCreditNotesPostValidateBeforeCall(SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'salesInvoiceCreditNoteDto' is set
        if (salesInvoiceCreditNoteDto == null) {
            throw new ApiException("Missing the required parameter 'salesInvoiceCreditNoteDto' when calling salesCreditNotesPost(Async)");
        }

        return salesCreditNotesPostCall(salesInvoiceCreditNoteDto, _callback);

    }

    /**
     * Creates a new Sales Credit Note.
     * 
     * @param salesInvoiceCreditNoteDto Information of Sales Credit Note to create. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object salesCreditNotesPost(SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto) throws ApiException {
        ApiResponse<Object> localVarResp = salesCreditNotesPostWithHttpInfo(salesInvoiceCreditNoteDto);
        return localVarResp.getData();
    }

    /**
     * Creates a new Sales Credit Note.
     * 
     * @param salesInvoiceCreditNoteDto Information of Sales Credit Note to create. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> salesCreditNotesPostWithHttpInfo(SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto) throws ApiException {
        okhttp3.Call localVarCall = salesCreditNotesPostValidateBeforeCall(salesInvoiceCreditNoteDto, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Creates a new Sales Credit Note. (asynchronously)
     * 
     * @param salesInvoiceCreditNoteDto Information of Sales Credit Note to create. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call salesCreditNotesPostAsync(SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = salesCreditNotesPostValidateBeforeCall(salesInvoiceCreditNoteDto, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for salesCreditNotesProcessBatch
     * @param batchItemSalesInvoiceCreditNoteDto Batch of Sales Credit Notes to process. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call salesCreditNotesProcessBatchCall(List<BatchItemSalesInvoiceCreditNoteDto> batchItemSalesInvoiceCreditNoteDto, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = batchItemSalesInvoiceCreditNoteDto;

        // create path and map variables
        String localVarPath = "/v1/salesCreditNotes/batch";

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
    private okhttp3.Call salesCreditNotesProcessBatchValidateBeforeCall(List<BatchItemSalesInvoiceCreditNoteDto> batchItemSalesInvoiceCreditNoteDto, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'batchItemSalesInvoiceCreditNoteDto' is set
        if (batchItemSalesInvoiceCreditNoteDto == null) {
            throw new ApiException("Missing the required parameter 'batchItemSalesInvoiceCreditNoteDto' when calling salesCreditNotesProcessBatch(Async)");
        }

        return salesCreditNotesProcessBatchCall(batchItemSalesInvoiceCreditNoteDto, _callback);

    }

    /**
     * Processes a batch of Sales Credit Notes.
     * 
     * @param batchItemSalesInvoiceCreditNoteDto Batch of Sales Credit Notes to process. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object salesCreditNotesProcessBatch(List<BatchItemSalesInvoiceCreditNoteDto> batchItemSalesInvoiceCreditNoteDto) throws ApiException {
        ApiResponse<Object> localVarResp = salesCreditNotesProcessBatchWithHttpInfo(batchItemSalesInvoiceCreditNoteDto);
        return localVarResp.getData();
    }

    /**
     * Processes a batch of Sales Credit Notes.
     * 
     * @param batchItemSalesInvoiceCreditNoteDto Batch of Sales Credit Notes to process. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> salesCreditNotesProcessBatchWithHttpInfo(List<BatchItemSalesInvoiceCreditNoteDto> batchItemSalesInvoiceCreditNoteDto) throws ApiException {
        okhttp3.Call localVarCall = salesCreditNotesProcessBatchValidateBeforeCall(batchItemSalesInvoiceCreditNoteDto, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Processes a batch of Sales Credit Notes. (asynchronously)
     * 
     * @param batchItemSalesInvoiceCreditNoteDto Batch of Sales Credit Notes to process. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call salesCreditNotesProcessBatchAsync(List<BatchItemSalesInvoiceCreditNoteDto> batchItemSalesInvoiceCreditNoteDto, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = salesCreditNotesProcessBatchValidateBeforeCall(batchItemSalesInvoiceCreditNoteDto, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for salesCreditNotesPut
     * @param id Id of Sales Credit Note to update. (required)
     * @param salesInvoiceCreditNoteDto Information of Sales Credit Note to update. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call salesCreditNotesPutCall(Long id, SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = salesInvoiceCreditNoteDto;

        // create path and map variables
        String localVarPath = "/v1/salesCreditNotes/{id}"
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
    private okhttp3.Call salesCreditNotesPutValidateBeforeCall(Long id, SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling salesCreditNotesPut(Async)");
        }

        // verify the required parameter 'salesInvoiceCreditNoteDto' is set
        if (salesInvoiceCreditNoteDto == null) {
            throw new ApiException("Missing the required parameter 'salesInvoiceCreditNoteDto' when calling salesCreditNotesPut(Async)");
        }

        return salesCreditNotesPutCall(id, salesInvoiceCreditNoteDto, _callback);

    }

    /**
     * Updates an existing Sales Credit Note.
     * 
     * @param id Id of Sales Credit Note to update. (required)
     * @param salesInvoiceCreditNoteDto Information of Sales Credit Note to update. (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object salesCreditNotesPut(Long id, SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto) throws ApiException {
        ApiResponse<Object> localVarResp = salesCreditNotesPutWithHttpInfo(id, salesInvoiceCreditNoteDto);
        return localVarResp.getData();
    }

    /**
     * Updates an existing Sales Credit Note.
     * 
     * @param id Id of Sales Credit Note to update. (required)
     * @param salesInvoiceCreditNoteDto Information of Sales Credit Note to update. (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> salesCreditNotesPutWithHttpInfo(Long id, SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto) throws ApiException {
        okhttp3.Call localVarCall = salesCreditNotesPutValidateBeforeCall(id, salesInvoiceCreditNoteDto, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Updates an existing Sales Credit Note. (asynchronously)
     * 
     * @param id Id of Sales Credit Note to update. (required)
     * @param salesInvoiceCreditNoteDto Information of Sales Credit Note to update. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call salesCreditNotesPutAsync(Long id, SalesInvoiceCreditNoteDto salesInvoiceCreditNoteDto, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = salesCreditNotesPutValidateBeforeCall(id, salesInvoiceCreditNoteDto, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for v1SalesCreditNotesIdGet
     * @param id Id of Sales Credit Note to return. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call v1SalesCreditNotesIdGetCall(Long id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/salesCreditNotes/{id}"
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
    private okhttp3.Call v1SalesCreditNotesIdGetValidateBeforeCall(Long id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling v1SalesCreditNotesIdGet(Async)");
        }

        return v1SalesCreditNotesIdGetCall(id, _callback);

    }

    /**
     * Returns information about a single Sales Credit Note.
     * 
     * @param id Id of Sales Credit Note to return. (required)
     * @return SalesInvoiceCreditNoteDto
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public SalesInvoiceCreditNoteDto v1SalesCreditNotesIdGet(Long id) throws ApiException {
        ApiResponse<SalesInvoiceCreditNoteDto> localVarResp = v1SalesCreditNotesIdGetWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Returns information about a single Sales Credit Note.
     * 
     * @param id Id of Sales Credit Note to return. (required)
     * @return ApiResponse&lt;SalesInvoiceCreditNoteDto&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SalesInvoiceCreditNoteDto> v1SalesCreditNotesIdGetWithHttpInfo(Long id) throws ApiException {
        okhttp3.Call localVarCall = v1SalesCreditNotesIdGetValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<SalesInvoiceCreditNoteDto>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Returns information about a single Sales Credit Note. (asynchronously)
     * 
     * @param id Id of Sales Credit Note to return. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call v1SalesCreditNotesIdGetAsync(Long id, final ApiCallback<SalesInvoiceCreditNoteDto> _callback) throws ApiException {

        okhttp3.Call localVarCall = v1SalesCreditNotesIdGetValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<SalesInvoiceCreditNoteDto>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
