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


import org.openapitools.client.model.GetBlockHashV2200Response;
import org.openapitools.client.model.GetBlockV2200Response;
import org.openapitools.client.model.GetRawBlockV2200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BlocksApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public BlocksApi() {
        this(Configuration.getDefaultApiClient());
    }

    public BlocksApi(ApiClient apiClient) {
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
     * Build call for getBlockHashV2
     * @param blockchain Blockchain name (required)
     * @param blockHeight Block height/index (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBlockHashV2Call(String blockchain, Integer blockHeight, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{blockchain}/v2/block-index/{blockHeight}"
            .replace("{" + "blockchain" + "}", localVarApiClient.escapeString(blockchain.toString()))
            .replace("{" + "blockHeight" + "}", localVarApiClient.escapeString(blockHeight.toString()));

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
    private okhttp3.Call getBlockHashV2ValidateBeforeCall(String blockchain, Integer blockHeight, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'blockchain' is set
        if (blockchain == null) {
            throw new ApiException("Missing the required parameter 'blockchain' when calling getBlockHashV2(Async)");
        }

        // verify the required parameter 'blockHeight' is set
        if (blockHeight == null) {
            throw new ApiException("Missing the required parameter 'blockHeight' when calling getBlockHashV2(Async)");
        }

        return getBlockHashV2Call(blockchain, blockHeight, _callback);

    }

    /**
     * Get block hash V2
     * Get block hash by its height  Note: Blockbook always follows the main chain of the backend it is attached to.
     * @param blockchain Blockchain name (required)
     * @param blockHeight Block height/index (required)
     * @return GetBlockHashV2200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetBlockHashV2200Response getBlockHashV2(String blockchain, Integer blockHeight) throws ApiException {
        ApiResponse<GetBlockHashV2200Response> localVarResp = getBlockHashV2WithHttpInfo(blockchain, blockHeight);
        return localVarResp.getData();
    }

    /**
     * Get block hash V2
     * Get block hash by its height  Note: Blockbook always follows the main chain of the backend it is attached to.
     * @param blockchain Blockchain name (required)
     * @param blockHeight Block height/index (required)
     * @return ApiResponse&lt;GetBlockHashV2200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetBlockHashV2200Response> getBlockHashV2WithHttpInfo(String blockchain, Integer blockHeight) throws ApiException {
        okhttp3.Call localVarCall = getBlockHashV2ValidateBeforeCall(blockchain, blockHeight, null);
        Type localVarReturnType = new TypeToken<GetBlockHashV2200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get block hash V2 (asynchronously)
     * Get block hash by its height  Note: Blockbook always follows the main chain of the backend it is attached to.
     * @param blockchain Blockchain name (required)
     * @param blockHeight Block height/index (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBlockHashV2Async(String blockchain, Integer blockHeight, final ApiCallback<GetBlockHashV2200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getBlockHashV2ValidateBeforeCall(blockchain, blockHeight, _callback);
        Type localVarReturnType = new TypeToken<GetBlockHashV2200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getBlockV2
     * @param blockchain Blockchain name (required)
     * @param blockHashOrHeight Block hash or height (required)
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
    public okhttp3.Call getBlockV2Call(String blockchain, String blockHashOrHeight, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{blockchain}/v2/block/{blockHashOrHeight}"
            .replace("{" + "blockchain" + "}", localVarApiClient.escapeString(blockchain.toString()))
            .replace("{" + "blockHashOrHeight" + "}", localVarApiClient.escapeString(blockHashOrHeight.toString()));

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
    private okhttp3.Call getBlockV2ValidateBeforeCall(String blockchain, String blockHashOrHeight, Integer page, Integer pageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'blockchain' is set
        if (blockchain == null) {
            throw new ApiException("Missing the required parameter 'blockchain' when calling getBlockV2(Async)");
        }

        // verify the required parameter 'blockHashOrHeight' is set
        if (blockHashOrHeight == null) {
            throw new ApiException("Missing the required parameter 'blockHashOrHeight' when calling getBlockV2(Async)");
        }

        return getBlockV2Call(blockchain, blockHashOrHeight, page, pageSize, _callback);

    }

    /**
     * Get Block V2
     * Returns information about block with transactions, subject to paging.  Note: Blockbook always follows the main chain of the backend it is attached to. If there is a rollback-reorg in the backend, Blockbook will also do rollback. When you ask for block by height, you will always get the main chain block. If you ask for block by hash, you may get the block from another fork but it is not guaranteed (backend may not keep it)
     * @param blockchain Blockchain name (required)
     * @param blockHashOrHeight Block hash or height (required)
     * @param page specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page. (optional)
     * @param pageSize number of transactions returned by call (default and maximum 1000) (optional)
     * @return GetBlockV2200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetBlockV2200Response getBlockV2(String blockchain, String blockHashOrHeight, Integer page, Integer pageSize) throws ApiException {
        ApiResponse<GetBlockV2200Response> localVarResp = getBlockV2WithHttpInfo(blockchain, blockHashOrHeight, page, pageSize);
        return localVarResp.getData();
    }

    /**
     * Get Block V2
     * Returns information about block with transactions, subject to paging.  Note: Blockbook always follows the main chain of the backend it is attached to. If there is a rollback-reorg in the backend, Blockbook will also do rollback. When you ask for block by height, you will always get the main chain block. If you ask for block by hash, you may get the block from another fork but it is not guaranteed (backend may not keep it)
     * @param blockchain Blockchain name (required)
     * @param blockHashOrHeight Block hash or height (required)
     * @param page specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page. (optional)
     * @param pageSize number of transactions returned by call (default and maximum 1000) (optional)
     * @return ApiResponse&lt;GetBlockV2200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetBlockV2200Response> getBlockV2WithHttpInfo(String blockchain, String blockHashOrHeight, Integer page, Integer pageSize) throws ApiException {
        okhttp3.Call localVarCall = getBlockV2ValidateBeforeCall(blockchain, blockHashOrHeight, page, pageSize, null);
        Type localVarReturnType = new TypeToken<GetBlockV2200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Block V2 (asynchronously)
     * Returns information about block with transactions, subject to paging.  Note: Blockbook always follows the main chain of the backend it is attached to. If there is a rollback-reorg in the backend, Blockbook will also do rollback. When you ask for block by height, you will always get the main chain block. If you ask for block by hash, you may get the block from another fork but it is not guaranteed (backend may not keep it)
     * @param blockchain Blockchain name (required)
     * @param blockHashOrHeight Block hash or height (required)
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
    public okhttp3.Call getBlockV2Async(String blockchain, String blockHashOrHeight, Integer page, Integer pageSize, final ApiCallback<GetBlockV2200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getBlockV2ValidateBeforeCall(blockchain, blockHashOrHeight, page, pageSize, _callback);
        Type localVarReturnType = new TypeToken<GetBlockV2200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getRawBlockV2
     * @param blockchain Blockchain name (required)
     * @param blockHashOrHeight Block hash or height (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRawBlockV2Call(String blockchain, String blockHashOrHeight, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{blockchain}/v2/rawblock/{blockHashOrHeight}"
            .replace("{" + "blockchain" + "}", localVarApiClient.escapeString(blockchain.toString()))
            .replace("{" + "blockHashOrHeight" + "}", localVarApiClient.escapeString(blockHashOrHeight.toString()));

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
    private okhttp3.Call getRawBlockV2ValidateBeforeCall(String blockchain, String blockHashOrHeight, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'blockchain' is set
        if (blockchain == null) {
            throw new ApiException("Missing the required parameter 'blockchain' when calling getRawBlockV2(Async)");
        }

        // verify the required parameter 'blockHashOrHeight' is set
        if (blockHashOrHeight == null) {
            throw new ApiException("Missing the required parameter 'blockHashOrHeight' when calling getRawBlockV2(Async)");
        }

        return getRawBlockV2Call(blockchain, blockHashOrHeight, _callback);

    }

    /**
     * Get raw block data V2
     * Returns the raw hex-encoded block data for a given block hash or height
     * @param blockchain Blockchain name (required)
     * @param blockHashOrHeight Block hash or height (required)
     * @return GetRawBlockV2200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetRawBlockV2200Response getRawBlockV2(String blockchain, String blockHashOrHeight) throws ApiException {
        ApiResponse<GetRawBlockV2200Response> localVarResp = getRawBlockV2WithHttpInfo(blockchain, blockHashOrHeight);
        return localVarResp.getData();
    }

    /**
     * Get raw block data V2
     * Returns the raw hex-encoded block data for a given block hash or height
     * @param blockchain Blockchain name (required)
     * @param blockHashOrHeight Block hash or height (required)
     * @return ApiResponse&lt;GetRawBlockV2200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetRawBlockV2200Response> getRawBlockV2WithHttpInfo(String blockchain, String blockHashOrHeight) throws ApiException {
        okhttp3.Call localVarCall = getRawBlockV2ValidateBeforeCall(blockchain, blockHashOrHeight, null);
        Type localVarReturnType = new TypeToken<GetRawBlockV2200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get raw block data V2 (asynchronously)
     * Returns the raw hex-encoded block data for a given block hash or height
     * @param blockchain Blockchain name (required)
     * @param blockHashOrHeight Block hash or height (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRawBlockV2Async(String blockchain, String blockHashOrHeight, final ApiCallback<GetRawBlockV2200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getRawBlockV2ValidateBeforeCall(blockchain, blockHashOrHeight, _callback);
        Type localVarReturnType = new TypeToken<GetRawBlockV2200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
