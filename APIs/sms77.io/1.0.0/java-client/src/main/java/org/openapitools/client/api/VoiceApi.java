/*
 * seven.io API
 * seven.io Swagger API. Get your API-Key now at seven.io.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@seven.io
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


import java.math.BigDecimal;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class VoiceApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public VoiceApi() {
        this(Configuration.getDefaultApiClient());
    }

    public VoiceApi(ApiClient apiClient) {
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
     * Build call for voice
     * @param to Determines the receiver. Must be a valid phone number or contact from the address book. (required)
     * @param text The text to convert to a voice message. Accepts valid XML too. (required)
     * @param xml Decides whether the parameter \&quot;text\&quot; is plain text or XML. The default value is 0. (optional)
     * @param from Sets the sender. Must be a verified sender. Use an inbound number of yours or one of ours. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call voiceCall(String to, String text, BigDecimal xml, String from, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/voice";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (to != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("to", to));
        }

        if (text != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("text", text));
        }

        if (xml != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("xml", xml));
        }

        if (from != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("from", from));
        }

        final String[] localVarAccepts = {
            "text/plain"
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

        String[] localVarAuthNames = new String[] { "ApiKeyAuth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call voiceValidateBeforeCall(String to, String text, BigDecimal xml, String from, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'to' is set
        if (to == null) {
            throw new ApiException("Missing the required parameter 'to' when calling voice(Async)");
        }

        // verify the required parameter 'text' is set
        if (text == null) {
            throw new ApiException("Missing the required parameter 'text' when calling voice(Async)");
        }

        return voiceCall(to, text, xml, from, _callback);

    }

    /**
     * 
     * 
     * @param to Determines the receiver. Must be a valid phone number or contact from the address book. (required)
     * @param text The text to convert to a voice message. Accepts valid XML too. (required)
     * @param xml Decides whether the parameter \&quot;text\&quot; is plain text or XML. The default value is 0. (optional)
     * @param from Sets the sender. Must be a verified sender. Use an inbound number of yours or one of ours. (optional)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public String voice(String to, String text, BigDecimal xml, String from) throws ApiException {
        ApiResponse<String> localVarResp = voiceWithHttpInfo(to, text, xml, from);
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @param to Determines the receiver. Must be a valid phone number or contact from the address book. (required)
     * @param text The text to convert to a voice message. Accepts valid XML too. (required)
     * @param xml Decides whether the parameter \&quot;text\&quot; is plain text or XML. The default value is 0. (optional)
     * @param from Sets the sender. Must be a verified sender. Use an inbound number of yours or one of ours. (optional)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> voiceWithHttpInfo(String to, String text, BigDecimal xml, String from) throws ApiException {
        okhttp3.Call localVarCall = voiceValidateBeforeCall(to, text, xml, from, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param to Determines the receiver. Must be a valid phone number or contact from the address book. (required)
     * @param text The text to convert to a voice message. Accepts valid XML too. (required)
     * @param xml Decides whether the parameter \&quot;text\&quot; is plain text or XML. The default value is 0. (optional)
     * @param from Sets the sender. Must be a verified sender. Use an inbound number of yours or one of ours. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call voiceAsync(String to, String text, BigDecimal xml, String from, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = voiceValidateBeforeCall(to, text, xml, from, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
