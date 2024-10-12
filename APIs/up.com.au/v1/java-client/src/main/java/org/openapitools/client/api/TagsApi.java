/*
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
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


import org.openapitools.client.model.ListTagsResponse;
import org.openapitools.client.model.UpdateTransactionTagsRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TagsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public TagsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TagsApi(ApiClient apiClient) {
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
     * Build call for tagsGet
     * @param pageSize The number of records to return in each page.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call tagsGetCall(Integer pageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/tags";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page[size]", pageSize));
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

        String[] localVarAuthNames = new String[] { "bearer_auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call tagsGetValidateBeforeCall(Integer pageSize, final ApiCallback _callback) throws ApiException {
        return tagsGetCall(pageSize, _callback);

    }

    /**
     * List tags
     * Retrieve a list of all tags currently in use. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. Results are ordered lexicographically. The &#x60;transactions&#x60; relationship for each tag exposes a link to get the transactions with the given tag. 
     * @param pageSize The number of records to return in each page.  (optional)
     * @return ListTagsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful Response </td><td>  -  </td></tr>
     </table>
     */
    public ListTagsResponse tagsGet(Integer pageSize) throws ApiException {
        ApiResponse<ListTagsResponse> localVarResp = tagsGetWithHttpInfo(pageSize);
        return localVarResp.getData();
    }

    /**
     * List tags
     * Retrieve a list of all tags currently in use. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. Results are ordered lexicographically. The &#x60;transactions&#x60; relationship for each tag exposes a link to get the transactions with the given tag. 
     * @param pageSize The number of records to return in each page.  (optional)
     * @return ApiResponse&lt;ListTagsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListTagsResponse> tagsGetWithHttpInfo(Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = tagsGetValidateBeforeCall(pageSize, null);
        Type localVarReturnType = new TypeToken<ListTagsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List tags (asynchronously)
     * Retrieve a list of all tags currently in use. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. Results are ordered lexicographically. The &#x60;transactions&#x60; relationship for each tag exposes a link to get the transactions with the given tag. 
     * @param pageSize The number of records to return in each page.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call tagsGetAsync(Integer pageSize, final ApiCallback<ListTagsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = tagsGetValidateBeforeCall(pageSize, _callback);
        Type localVarReturnType = new TypeToken<ListTagsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for transactionsTransactionIdRelationshipsTagsDelete
     * @param transactionId The unique identifier for the transaction.  (required)
     * @param updateTransactionTagsRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call transactionsTransactionIdRelationshipsTagsDeleteCall(String transactionId, UpdateTransactionTagsRequest updateTransactionTagsRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateTransactionTagsRequest;

        // create path and map variables
        String localVarPath = "/transactions/{transactionId}/relationships/tags"
            .replace("{" + "transactionId" + "}", localVarApiClient.escapeString(transactionId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
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

        String[] localVarAuthNames = new String[] { "bearer_auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call transactionsTransactionIdRelationshipsTagsDeleteValidateBeforeCall(String transactionId, UpdateTransactionTagsRequest updateTransactionTagsRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'transactionId' is set
        if (transactionId == null) {
            throw new ApiException("Missing the required parameter 'transactionId' when calling transactionsTransactionIdRelationshipsTagsDelete(Async)");
        }

        return transactionsTransactionIdRelationshipsTagsDeleteCall(transactionId, updateTransactionTagsRequest, _callback);

    }

    /**
     * Remove tags from transaction
     * Disassociates one or more tags from a specific transaction. Tags that are not associated are silently ignored. An HTTP &#x60;204&#x60; is returned on success. The associated tags, along with this request URL, are also exposed via the &#x60;tags&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 
     * @param transactionId The unique identifier for the transaction.  (required)
     * @param updateTransactionTagsRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful Response </td><td>  -  </td></tr>
     </table>
     */
    public void transactionsTransactionIdRelationshipsTagsDelete(String transactionId, UpdateTransactionTagsRequest updateTransactionTagsRequest) throws ApiException {
        transactionsTransactionIdRelationshipsTagsDeleteWithHttpInfo(transactionId, updateTransactionTagsRequest);
    }

    /**
     * Remove tags from transaction
     * Disassociates one or more tags from a specific transaction. Tags that are not associated are silently ignored. An HTTP &#x60;204&#x60; is returned on success. The associated tags, along with this request URL, are also exposed via the &#x60;tags&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 
     * @param transactionId The unique identifier for the transaction.  (required)
     * @param updateTransactionTagsRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> transactionsTransactionIdRelationshipsTagsDeleteWithHttpInfo(String transactionId, UpdateTransactionTagsRequest updateTransactionTagsRequest) throws ApiException {
        okhttp3.Call localVarCall = transactionsTransactionIdRelationshipsTagsDeleteValidateBeforeCall(transactionId, updateTransactionTagsRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Remove tags from transaction (asynchronously)
     * Disassociates one or more tags from a specific transaction. Tags that are not associated are silently ignored. An HTTP &#x60;204&#x60; is returned on success. The associated tags, along with this request URL, are also exposed via the &#x60;tags&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 
     * @param transactionId The unique identifier for the transaction.  (required)
     * @param updateTransactionTagsRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call transactionsTransactionIdRelationshipsTagsDeleteAsync(String transactionId, UpdateTransactionTagsRequest updateTransactionTagsRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = transactionsTransactionIdRelationshipsTagsDeleteValidateBeforeCall(transactionId, updateTransactionTagsRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for transactionsTransactionIdRelationshipsTagsPost
     * @param transactionId The unique identifier for the transaction.  (required)
     * @param updateTransactionTagsRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call transactionsTransactionIdRelationshipsTagsPostCall(String transactionId, UpdateTransactionTagsRequest updateTransactionTagsRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateTransactionTagsRequest;

        // create path and map variables
        String localVarPath = "/transactions/{transactionId}/relationships/tags"
            .replace("{" + "transactionId" + "}", localVarApiClient.escapeString(transactionId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
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

        String[] localVarAuthNames = new String[] { "bearer_auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call transactionsTransactionIdRelationshipsTagsPostValidateBeforeCall(String transactionId, UpdateTransactionTagsRequest updateTransactionTagsRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'transactionId' is set
        if (transactionId == null) {
            throw new ApiException("Missing the required parameter 'transactionId' when calling transactionsTransactionIdRelationshipsTagsPost(Async)");
        }

        return transactionsTransactionIdRelationshipsTagsPostCall(transactionId, updateTransactionTagsRequest, _callback);

    }

    /**
     * Add tags to transaction
     * Associates one or more tags with a specific transaction. No more than 6 tags may be present on any single transaction. Duplicate tags are silently ignored. An HTTP &#x60;204&#x60; is returned on success. The associated tags, along with this request URL, are also exposed via the &#x60;tags&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 
     * @param transactionId The unique identifier for the transaction.  (required)
     * @param updateTransactionTagsRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful Response </td><td>  -  </td></tr>
     </table>
     */
    public void transactionsTransactionIdRelationshipsTagsPost(String transactionId, UpdateTransactionTagsRequest updateTransactionTagsRequest) throws ApiException {
        transactionsTransactionIdRelationshipsTagsPostWithHttpInfo(transactionId, updateTransactionTagsRequest);
    }

    /**
     * Add tags to transaction
     * Associates one or more tags with a specific transaction. No more than 6 tags may be present on any single transaction. Duplicate tags are silently ignored. An HTTP &#x60;204&#x60; is returned on success. The associated tags, along with this request URL, are also exposed via the &#x60;tags&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 
     * @param transactionId The unique identifier for the transaction.  (required)
     * @param updateTransactionTagsRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> transactionsTransactionIdRelationshipsTagsPostWithHttpInfo(String transactionId, UpdateTransactionTagsRequest updateTransactionTagsRequest) throws ApiException {
        okhttp3.Call localVarCall = transactionsTransactionIdRelationshipsTagsPostValidateBeforeCall(transactionId, updateTransactionTagsRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Add tags to transaction (asynchronously)
     * Associates one or more tags with a specific transaction. No more than 6 tags may be present on any single transaction. Duplicate tags are silently ignored. An HTTP &#x60;204&#x60; is returned on success. The associated tags, along with this request URL, are also exposed via the &#x60;tags&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 
     * @param transactionId The unique identifier for the transaction.  (required)
     * @param updateTransactionTagsRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Successful Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call transactionsTransactionIdRelationshipsTagsPostAsync(String transactionId, UpdateTransactionTagsRequest updateTransactionTagsRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = transactionsTransactionIdRelationshipsTagsPostValidateBeforeCall(transactionId, updateTransactionTagsRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
