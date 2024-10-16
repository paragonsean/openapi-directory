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


import org.openapitools.client.model.GetTickersListV2200Response;
import org.openapitools.client.model.GetTickersV2200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TickersApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public TickersApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TickersApi(ApiClient apiClient) {
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
     * Build call for getTickersListV2
     * @param blockchain Blockchain name (required)
     * @param timestamp specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTickersListV2Call(String blockchain, String timestamp, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{blockchain}/v2/tickers-list/"
            .replace("{" + "blockchain" + "}", localVarApiClient.escapeString(blockchain.toString()));

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

        String[] localVarAuthNames = new String[] { "X-RapidAPI-Host", "X-API-Key", "X-RapidAPI-Key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getTickersListV2ValidateBeforeCall(String blockchain, String timestamp, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'blockchain' is set
        if (blockchain == null) {
            throw new ApiException("Missing the required parameter 'blockchain' when calling getTickersListV2(Async)");
        }

        return getTickersListV2Call(blockchain, timestamp, _callback);

    }

    /**
     * Get Tickers list V2
     * Returns a list of available currency rate tickers (secondary currencies) for the specified date, along with an actual data timestamp.  Trailing slash &#39;/&#39; is mandatory
     * @param blockchain Blockchain name (required)
     * @param timestamp specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned. (optional)
     * @return GetTickersListV2200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetTickersListV2200Response getTickersListV2(String blockchain, String timestamp) throws ApiException {
        ApiResponse<GetTickersListV2200Response> localVarResp = getTickersListV2WithHttpInfo(blockchain, timestamp);
        return localVarResp.getData();
    }

    /**
     * Get Tickers list V2
     * Returns a list of available currency rate tickers (secondary currencies) for the specified date, along with an actual data timestamp.  Trailing slash &#39;/&#39; is mandatory
     * @param blockchain Blockchain name (required)
     * @param timestamp specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned. (optional)
     * @return ApiResponse&lt;GetTickersListV2200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetTickersListV2200Response> getTickersListV2WithHttpInfo(String blockchain, String timestamp) throws ApiException {
        okhttp3.Call localVarCall = getTickersListV2ValidateBeforeCall(blockchain, timestamp, null);
        Type localVarReturnType = new TypeToken<GetTickersListV2200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Tickers list V2 (asynchronously)
     * Returns a list of available currency rate tickers (secondary currencies) for the specified date, along with an actual data timestamp.  Trailing slash &#39;/&#39; is mandatory
     * @param blockchain Blockchain name (required)
     * @param timestamp specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTickersListV2Async(String blockchain, String timestamp, final ApiCallback<GetTickersListV2200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getTickersListV2ValidateBeforeCall(blockchain, timestamp, _callback);
        Type localVarReturnType = new TypeToken<GetTickersListV2200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getTickersV2
     * @param blockchain Blockchain name (required)
     * @param timestamp specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned. (optional)
     * @param currency specifies a currency of returned rate (\&quot;usd\&quot;, \&quot;eur\&quot;, \&quot;eth\&quot;...). If not specified, all available currencies will be returned (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTickersV2Call(String blockchain, String timestamp, String currency, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/{blockchain}/v2/tickers/"
            .replace("{" + "blockchain" + "}", localVarApiClient.escapeString(blockchain.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (timestamp != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("timestamp", timestamp));
        }

        if (currency != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("currency", currency));
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
    private okhttp3.Call getTickersV2ValidateBeforeCall(String blockchain, String timestamp, String currency, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'blockchain' is set
        if (blockchain == null) {
            throw new ApiException("Missing the required parameter 'blockchain' when calling getTickersV2(Async)");
        }

        return getTickersV2Call(blockchain, timestamp, currency, _callback);

    }

    /**
     * Get Tickers V2
     * Returns currency rate for the specified currency and date. If the currency is not available for that specific timestamp, the next closest rate will be returned. All responses contain an actual rate timestamp.
     * @param blockchain Blockchain name (required)
     * @param timestamp specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned. (optional)
     * @param currency specifies a currency of returned rate (\&quot;usd\&quot;, \&quot;eur\&quot;, \&quot;eth\&quot;...). If not specified, all available currencies will be returned (optional)
     * @return GetTickersV2200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public GetTickersV2200Response getTickersV2(String blockchain, String timestamp, String currency) throws ApiException {
        ApiResponse<GetTickersV2200Response> localVarResp = getTickersV2WithHttpInfo(blockchain, timestamp, currency);
        return localVarResp.getData();
    }

    /**
     * Get Tickers V2
     * Returns currency rate for the specified currency and date. If the currency is not available for that specific timestamp, the next closest rate will be returned. All responses contain an actual rate timestamp.
     * @param blockchain Blockchain name (required)
     * @param timestamp specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned. (optional)
     * @param currency specifies a currency of returned rate (\&quot;usd\&quot;, \&quot;eur\&quot;, \&quot;eth\&quot;...). If not specified, all available currencies will be returned (optional)
     * @return ApiResponse&lt;GetTickersV2200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetTickersV2200Response> getTickersV2WithHttpInfo(String blockchain, String timestamp, String currency) throws ApiException {
        okhttp3.Call localVarCall = getTickersV2ValidateBeforeCall(blockchain, timestamp, currency, null);
        Type localVarReturnType = new TypeToken<GetTickersV2200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Tickers V2 (asynchronously)
     * Returns currency rate for the specified currency and date. If the currency is not available for that specific timestamp, the next closest rate will be returned. All responses contain an actual rate timestamp.
     * @param blockchain Blockchain name (required)
     * @param timestamp specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned. (optional)
     * @param currency specifies a currency of returned rate (\&quot;usd\&quot;, \&quot;eur\&quot;, \&quot;eth\&quot;...). If not specified, all available currencies will be returned (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getTickersV2Async(String blockchain, String timestamp, String currency, final ApiCallback<GetTickersV2200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getTickersV2ValidateBeforeCall(blockchain, timestamp, currency, _callback);
        Type localVarReturnType = new TypeToken<GetTickersV2200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
