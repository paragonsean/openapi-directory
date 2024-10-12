/*
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
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


import org.openapitools.client.model.EndpointGetMarkdownEmoticons;
import org.openapitools.client.model.EndpointPostMarkdown;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MarkdownApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public MarkdownApi() {
        this(Configuration.getDefaultApiClient());
    }

    public MarkdownApi(ApiClient apiClient) {
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
     * Build call for markdownEmoticonsGet
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call markdownEmoticonsGetCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/markdown/emoticons";

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

        String[] localVarAuthNames = new String[] { "implicit_flow", "explicit_flow" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call markdownEmoticonsGetValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return markdownEmoticonsGetCall(_callback);

    }

    /**
     * 
     * 
     * @return EndpointGetMarkdownEmoticons
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public EndpointGetMarkdownEmoticons markdownEmoticonsGet() throws ApiException {
        ApiResponse<EndpointGetMarkdownEmoticons> localVarResp = markdownEmoticonsGetWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @return ApiResponse&lt;EndpointGetMarkdownEmoticons&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EndpointGetMarkdownEmoticons> markdownEmoticonsGetWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = markdownEmoticonsGetValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<EndpointGetMarkdownEmoticons>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call markdownEmoticonsGetAsync(final ApiCallback<EndpointGetMarkdownEmoticons> _callback) throws ApiException {

        okhttp3.Call localVarCall = markdownEmoticonsGetValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<EndpointGetMarkdownEmoticons>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for markdownPost
     * @param textRaw  (required)
     * @param textEmoticons  (optional, default to false)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call markdownPostCall(String textRaw, Boolean textEmoticons, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/markdown";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (textEmoticons != null) {
            localVarFormParams.put("text_emoticons", textEmoticons);
        }

        if (textRaw != null) {
            localVarFormParams.put("text_raw", textRaw);
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "multipart/form-data"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "implicit_flow", "explicit_flow" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call markdownPostValidateBeforeCall(String textRaw, Boolean textEmoticons, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'textRaw' is set
        if (textRaw == null) {
            throw new ApiException("Missing the required parameter 'textRaw' when calling markdownPost(Async)");
        }

        return markdownPostCall(textRaw, textEmoticons, _callback);

    }

    /**
     * 
     * 
     * @param textRaw  (required)
     * @param textEmoticons  (optional, default to false)
     * @return EndpointPostMarkdown
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public EndpointPostMarkdown markdownPost(String textRaw, Boolean textEmoticons) throws ApiException {
        ApiResponse<EndpointPostMarkdown> localVarResp = markdownPostWithHttpInfo(textRaw, textEmoticons);
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @param textRaw  (required)
     * @param textEmoticons  (optional, default to false)
     * @return ApiResponse&lt;EndpointPostMarkdown&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EndpointPostMarkdown> markdownPostWithHttpInfo(String textRaw, Boolean textEmoticons) throws ApiException {
        okhttp3.Call localVarCall = markdownPostValidateBeforeCall(textRaw, textEmoticons, null);
        Type localVarReturnType = new TypeToken<EndpointPostMarkdown>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param textRaw  (required)
     * @param textEmoticons  (optional, default to false)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Valid Response </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call markdownPostAsync(String textRaw, Boolean textEmoticons, final ApiCallback<EndpointPostMarkdown> _callback) throws ApiException {

        okhttp3.Call localVarCall = markdownPostValidateBeforeCall(textRaw, textEmoticons, _callback);
        Type localVarReturnType = new TypeToken<EndpointPostMarkdown>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
