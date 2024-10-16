/*
 * Chain49 API
 * Kickstart your next crypto project - extended trezor/blockbook API with 10+ blockchains available instantly and 50+ possible on request running on the finest hardware in Germany's best datacenters at Hetzner  Websocket only via api.chain49.com endpoint possible (RapidAPI does not support it yet)
 *
 * The version of the OpenAPI document: 2.0
 * Contact: contact@chain49.com
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


import org.openapitools.client.model.GetMempoolV2200Response;
import org.openapitools.client.model.GetTransactionV2200Response;
import org.openapitools.client.model.PostSendTxV2200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TransactionsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public TransactionsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TransactionsApi(ApiClient apiClient) {
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
     * Build call for getMempoolV2
     * @param blockchain Blockchain name (required)
     * @param page specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page. (optional)
     * @param pageSize number of transactions returned by call (default and maximum 1000) (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMempoolV2Call(String blockchain, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{blockchain}/v2/mempool/"
            .replace("{" + "blockchain" + "}", localVarApiClient.escapeString(blockchain.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("pageSize", pageSize));
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

        String[] localVarAuthNames = new String[] { "X-RapidAPI-Host", "X-API-Key", "X-RapidAPI-Key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getMempoolV2ValidateBeforeCall(String blockchain, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'blockchain' is set
        if (blockchain == null) {
            throw new ApiException("Missing the required parameter 'blockchain' when calling getMempoolV2(Async)");
        }

        return getMempoolV2Call(blockchain, page, pageSize, _callback);

    }

    /**
     * Get Mempool V2
     * Get a list of transaction IDs currently in the mempool of the node (meaning unconfirmed transactions not included in any block yet)  Note: this route was implemented by us and is therefore not yet supported by existing blockbook clients.
     * @param blockchain Blockchain name (required)
     * @param page specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page. (optional)
     * @param pageSize number of transactions returned by call (default and maximum 1000) (optional)
     * @return GetMempoolV2200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetMempoolV2200Response getMempoolV2(String blockchain, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetMempoolV2200Response> localVarResp = getMempoolV2WithHttpInfo(blockchain, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Get Mempool V2
     * Get a list of transaction IDs currently in the mempool of the node (meaning unconfirmed transactions not included in any block yet)  Note: this route was implemented by us and is therefore not yet supported by existing blockbook clients.
     * @param blockchain Blockchain name (required)
     * @param page specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page. (optional)
     * @param pageSize number of transactions returned by call (default and maximum 1000) (optional)
     * @return ApiResponse&lt;GetMempoolV2200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetMempoolV2200Response> getMempoolV2WithHttpInfo(String blockchain, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getMempoolV2ValidateBeforeCall(blockchain, page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetMempoolV2200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Mempool V2 (asynchronously)
     * Get a list of transaction IDs currently in the mempool of the node (meaning unconfirmed transactions not included in any block yet)  Note: this route was implemented by us and is therefore not yet supported by existing blockbook clients.
     * @param blockchain Blockchain name (required)
     * @param page specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page. (optional)
     * @param pageSize number of transactions returned by call (default and maximum 1000) (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMempoolV2Async(String blockchain, Integer page, Integer pageSize, final ApiCallback<GetMempoolV2200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getMempoolV2ValidateBeforeCall(blockchain, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetMempoolV2200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSendTxV2
     * @param blockchain Blockchain name (required)
     * @param hex Transaction hex data (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSendTxV2Call(String blockchain, String hex, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{blockchain}/v2/sendtx/{hex}"
            .replace("{" + "blockchain" + "}", localVarApiClient.escapeString(blockchain.toString()))
            .replace("{" + "hex" + "}", localVarApiClient.escapeString(hex.toString()));

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

        String[] localVarAuthNames = new String[] { "X-RapidAPI-Host", "X-API-Key", "X-RapidAPI-Key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getSendTxV2ValidateBeforeCall(String blockchain, String hex, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'blockchain' is set
        if (blockchain == null) {
            throw new ApiException("Missing the required parameter 'blockchain' when calling getSendTxV2(Async)");
        }

        // verify the required parameter 'hex' is set
        if (hex == null) {
            throw new ApiException("Missing the required parameter 'hex' when calling getSendTxV2(Async)");
        }

        return getSendTxV2Call(blockchain, hex, _callback);

    }

    /**
     * Send transaction (in URL) V2
     * Sends new transaction to backend  It is recommended to use POST for sending transactions as there is a limit on how much data can be sent in the URL itself.
     * @param blockchain Blockchain name (required)
     * @param hex Transaction hex data (required)
     * @return PostSendTxV2200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public PostSendTxV2200Response getSendTxV2(String blockchain, String hex) throws ApiException {
        ApiResponse<PostSendTxV2200Response> localVarResp = getSendTxV2WithHttpInfo(blockchain, hex);
        return localVarResp.getData();
    }

    /**
     * Send transaction (in URL) V2
     * Sends new transaction to backend  It is recommended to use POST for sending transactions as there is a limit on how much data can be sent in the URL itself.
     * @param blockchain Blockchain name (required)
     * @param hex Transaction hex data (required)
     * @return ApiResponse&lt;PostSendTxV2200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PostSendTxV2200Response> getSendTxV2WithHttpInfo(String blockchain, String hex) throws ApiException {
        okhttp3.Call localVarCall = getSendTxV2ValidateBeforeCall(blockchain, hex, null);
        Type localVarReturnType = new TypeToken<PostSendTxV2200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Send transaction (in URL) V2 (asynchronously)
     * Sends new transaction to backend  It is recommended to use POST for sending transactions as there is a limit on how much data can be sent in the URL itself.
     * @param blockchain Blockchain name (required)
     * @param hex Transaction hex data (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSendTxV2Async(String blockchain, String hex, final ApiCallback<PostSendTxV2200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSendTxV2ValidateBeforeCall(blockchain, hex, _callback);
        Type localVarReturnType = new TypeToken<PostSendTxV2200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getTransactionV2
     * @param blockchain Blockchain name (required)
     * @param txId Transaction ID (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTransactionV2Call(String blockchain, String txId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{blockchain}/v2/tx/{txId}"
            .replace("{" + "blockchain" + "}", localVarApiClient.escapeString(blockchain.toString()))
            .replace("{" + "txId" + "}", localVarApiClient.escapeString(txId.toString()));

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

        String[] localVarAuthNames = new String[] { "X-RapidAPI-Host", "X-API-Key", "X-RapidAPI-Key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getTransactionV2ValidateBeforeCall(String blockchain, String txId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'blockchain' is set
        if (blockchain == null) {
            throw new ApiException("Missing the required parameter 'blockchain' when calling getTransactionV2(Async)");
        }

        // verify the required parameter 'txId' is set
        if (txId == null) {
            throw new ApiException("Missing the required parameter 'txId' when calling getTransactionV2(Async)");
        }

        return getTransactionV2Call(blockchain, txId, _callback);

    }

    /**
     * Get transaction V2
     * Get transaction returns \&quot;normalized\&quot; data about transaction, which has the same general structure for all supported coins. It does not return coin specific fields (for example information about Zcash shielded addresses).  A note about the blockTime field: for already mined transaction (confirmations &gt; 0), the field blockTime contains time of the block for transactions in mempool (confirmations &#x3D;&#x3D; 0), the field contains time when the running instance of Blockbook was first time notified about the transaction. This time may be different in different instances of Blockbook.
     * @param blockchain Blockchain name (required)
     * @param txId Transaction ID (required)
     * @return GetTransactionV2200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetTransactionV2200Response getTransactionV2(String blockchain, String txId) throws ApiException {
        ApiResponse<GetTransactionV2200Response> localVarResp = getTransactionV2WithHttpInfo(blockchain, txId);
        return localVarResp.getData();
    }

    /**
     * Get transaction V2
     * Get transaction returns \&quot;normalized\&quot; data about transaction, which has the same general structure for all supported coins. It does not return coin specific fields (for example information about Zcash shielded addresses).  A note about the blockTime field: for already mined transaction (confirmations &gt; 0), the field blockTime contains time of the block for transactions in mempool (confirmations &#x3D;&#x3D; 0), the field contains time when the running instance of Blockbook was first time notified about the transaction. This time may be different in different instances of Blockbook.
     * @param blockchain Blockchain name (required)
     * @param txId Transaction ID (required)
     * @return ApiResponse&lt;GetTransactionV2200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetTransactionV2200Response> getTransactionV2WithHttpInfo(String blockchain, String txId) throws ApiException {
        okhttp3.Call localVarCall = getTransactionV2ValidateBeforeCall(blockchain, txId, null);
        Type localVarReturnType = new TypeToken<GetTransactionV2200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get transaction V2 (asynchronously)
     * Get transaction returns \&quot;normalized\&quot; data about transaction, which has the same general structure for all supported coins. It does not return coin specific fields (for example information about Zcash shielded addresses).  A note about the blockTime field: for already mined transaction (confirmations &gt; 0), the field blockTime contains time of the block for transactions in mempool (confirmations &#x3D;&#x3D; 0), the field contains time when the running instance of Blockbook was first time notified about the transaction. This time may be different in different instances of Blockbook.
     * @param blockchain Blockchain name (required)
     * @param txId Transaction ID (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTransactionV2Async(String blockchain, String txId, final ApiCallback<GetTransactionV2200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getTransactionV2ValidateBeforeCall(blockchain, txId, _callback);
        Type localVarReturnType = new TypeToken<GetTransactionV2200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getTxSpecificV2
     * @param blockchain Blockchain name (required)
     * @param txId Transaction ID (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTxSpecificV2Call(String blockchain, String txId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{blockchain}/v2/tx-specific/{txId}"
            .replace("{" + "blockchain" + "}", localVarApiClient.escapeString(blockchain.toString()))
            .replace("{" + "txId" + "}", localVarApiClient.escapeString(txId.toString()));

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

        String[] localVarAuthNames = new String[] { "X-RapidAPI-Host", "X-API-Key", "X-RapidAPI-Key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getTxSpecificV2ValidateBeforeCall(String blockchain, String txId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'blockchain' is set
        if (blockchain == null) {
            throw new ApiException("Missing the required parameter 'blockchain' when calling getTxSpecificV2(Async)");
        }

        // verify the required parameter 'txId' is set
        if (txId == null) {
            throw new ApiException("Missing the required parameter 'txId' when calling getTxSpecificV2(Async)");
        }

        return getTxSpecificV2Call(blockchain, txId, _callback);

    }

    /**
     * Get transaction (as is from Backend) V2
     * Returns transaction data in the exact format as returned by backend, including all coin specific fields
     * @param blockchain Blockchain name (required)
     * @param txId Transaction ID (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Object getTxSpecificV2(String blockchain, String txId) throws ApiException {
        ApiResponse<Object> localVarResp = getTxSpecificV2WithHttpInfo(blockchain, txId);
        return localVarResp.getData();
    }

    /**
     * Get transaction (as is from Backend) V2
     * Returns transaction data in the exact format as returned by backend, including all coin specific fields
     * @param blockchain Blockchain name (required)
     * @param txId Transaction ID (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> getTxSpecificV2WithHttpInfo(String blockchain, String txId) throws ApiException {
        okhttp3.Call localVarCall = getTxSpecificV2ValidateBeforeCall(blockchain, txId, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get transaction (as is from Backend) V2 (asynchronously)
     * Returns transaction data in the exact format as returned by backend, including all coin specific fields
     * @param blockchain Blockchain name (required)
     * @param txId Transaction ID (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTxSpecificV2Async(String blockchain, String txId, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = getTxSpecificV2ValidateBeforeCall(blockchain, txId, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postSendTxV2
     * @param blockchain Blockchain name (required)
     * @param body Transaction hex as plain text (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postSendTxV2Call(String blockchain, Object body, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = body;

        // create path and map variables
        String localVarPath = "/{blockchain}/v2/sendtx/"
            .replace("{" + "blockchain" + "}", localVarApiClient.escapeString(blockchain.toString()));

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
            "text/plain"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "X-RapidAPI-Host", "X-API-Key", "X-RapidAPI-Key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postSendTxV2ValidateBeforeCall(String blockchain, Object body, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'blockchain' is set
        if (blockchain == null) {
            throw new ApiException("Missing the required parameter 'blockchain' when calling postSendTxV2(Async)");
        }

        return postSendTxV2Call(blockchain, body, _callback);

    }

    /**
     * Send transaction (POST) V2
     * Sends new transaction to backend for broadcasting  The trailing slash &#39;/&#39; at the end is mandatory 
     * @param blockchain Blockchain name (required)
     * @param body Transaction hex as plain text (optional)
     * @return PostSendTxV2200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public PostSendTxV2200Response postSendTxV2(String blockchain, Object body) throws ApiException {
        ApiResponse<PostSendTxV2200Response> localVarResp = postSendTxV2WithHttpInfo(blockchain, body);
        return localVarResp.getData();
    }

    /**
     * Send transaction (POST) V2
     * Sends new transaction to backend for broadcasting  The trailing slash &#39;/&#39; at the end is mandatory 
     * @param blockchain Blockchain name (required)
     * @param body Transaction hex as plain text (optional)
     * @return ApiResponse&lt;PostSendTxV2200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PostSendTxV2200Response> postSendTxV2WithHttpInfo(String blockchain, Object body) throws ApiException {
        okhttp3.Call localVarCall = postSendTxV2ValidateBeforeCall(blockchain, body, null);
        Type localVarReturnType = new TypeToken<PostSendTxV2200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Send transaction (POST) V2 (asynchronously)
     * Sends new transaction to backend for broadcasting  The trailing slash &#39;/&#39; at the end is mandatory 
     * @param blockchain Blockchain name (required)
     * @param body Transaction hex as plain text (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postSendTxV2Async(String blockchain, Object body, final ApiCallback<PostSendTxV2200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = postSendTxV2ValidateBeforeCall(blockchain, body, _callback);
        Type localVarReturnType = new TypeToken<PostSendTxV2200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
