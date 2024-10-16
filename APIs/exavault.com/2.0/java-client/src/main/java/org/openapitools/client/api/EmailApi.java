/*
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
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


import org.openapitools.client.model.EmptyResponse;
import org.openapitools.client.model.SendReferralEmailRequestBody;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class EmailApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public EmailApi() {
        this(Configuration.getDefaultApiClient());
    }

    public EmailApi(ApiClient apiClient) {
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
     * Build call for sendReferralEmail
     * @param evApiKey API Key required to make the API call. (required)
     * @param evAccessToken Access token required to make the API call. (required)
     * @param sendReferralEmailRequestBody  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful Operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call sendReferralEmailCall(String evApiKey, String evAccessToken, SendReferralEmailRequestBody sendReferralEmailRequestBody, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = sendReferralEmailRequestBody;

        // create path and map variables
        String localVarPath = "/email/referral";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (evApiKey != null) {
            localVarHeaderParams.put("ev-api-key", localVarApiClient.parameterToString(evApiKey));
        }

        if (evAccessToken != null) {
            localVarHeaderParams.put("ev-access-token", localVarApiClient.parameterToString(evAccessToken));
        }

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
    private okhttp3.Call sendReferralEmailValidateBeforeCall(String evApiKey, String evAccessToken, SendReferralEmailRequestBody sendReferralEmailRequestBody, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'evApiKey' is set
        if (evApiKey == null) {
            throw new ApiException("Missing the required parameter 'evApiKey' when calling sendReferralEmail(Async)");
        }

        // verify the required parameter 'evAccessToken' is set
        if (evAccessToken == null) {
            throw new ApiException("Missing the required parameter 'evAccessToken' when calling sendReferralEmail(Async)");
        }

        return sendReferralEmailCall(evApiKey, evAccessToken, sendReferralEmailRequestBody, _callback);

    }

    /**
     * Send referral email to a given address
     * Invite a friend to sign up for a free trial of ExaVault. Send a [referral](/lp/referafriend/) email to an email address. If the recipient signs up for ExaVault, we&#39;ll apply a credit to your account for the referral. 
     * @param evApiKey API Key required to make the API call. (required)
     * @param evAccessToken Access token required to make the API call. (required)
     * @param sendReferralEmailRequestBody  (optional)
     * @return EmptyResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful Operation </td><td>  -  </td></tr>
     </table>
     */
    public EmptyResponse sendReferralEmail(String evApiKey, String evAccessToken, SendReferralEmailRequestBody sendReferralEmailRequestBody) throws ApiException {
        ApiResponse<EmptyResponse> localVarResp = sendReferralEmailWithHttpInfo(evApiKey, evAccessToken, sendReferralEmailRequestBody);
        return localVarResp.getData();
    }

    /**
     * Send referral email to a given address
     * Invite a friend to sign up for a free trial of ExaVault. Send a [referral](/lp/referafriend/) email to an email address. If the recipient signs up for ExaVault, we&#39;ll apply a credit to your account for the referral. 
     * @param evApiKey API Key required to make the API call. (required)
     * @param evAccessToken Access token required to make the API call. (required)
     * @param sendReferralEmailRequestBody  (optional)
     * @return ApiResponse&lt;EmptyResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful Operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EmptyResponse> sendReferralEmailWithHttpInfo(String evApiKey, String evAccessToken, SendReferralEmailRequestBody sendReferralEmailRequestBody) throws ApiException {
        okhttp3.Call localVarCall = sendReferralEmailValidateBeforeCall(evApiKey, evAccessToken, sendReferralEmailRequestBody, null);
        Type localVarReturnType = new TypeToken<EmptyResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Send referral email to a given address (asynchronously)
     * Invite a friend to sign up for a free trial of ExaVault. Send a [referral](/lp/referafriend/) email to an email address. If the recipient signs up for ExaVault, we&#39;ll apply a credit to your account for the referral. 
     * @param evApiKey API Key required to make the API call. (required)
     * @param evAccessToken Access token required to make the API call. (required)
     * @param sendReferralEmailRequestBody  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful Operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call sendReferralEmailAsync(String evApiKey, String evAccessToken, SendReferralEmailRequestBody sendReferralEmailRequestBody, final ApiCallback<EmptyResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = sendReferralEmailValidateBeforeCall(evApiKey, evAccessToken, sendReferralEmailRequestBody, _callback);
        Type localVarReturnType = new TypeToken<EmptyResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for sendWelcomeEmail
     * @param evApiKey API Key required to make the API call. (required)
     * @param evAccessToken Access token required to make the API call. (required)
     * @param username A username to send the welcome email to. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call sendWelcomeEmailCall(String evApiKey, String evAccessToken, String username, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/email/welcome/{username}"
            .replace("{" + "username" + "}", localVarApiClient.escapeString(username.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (evApiKey != null) {
            localVarHeaderParams.put("ev-api-key", localVarApiClient.parameterToString(evApiKey));
        }

        if (evAccessToken != null) {
            localVarHeaderParams.put("ev-access-token", localVarApiClient.parameterToString(evAccessToken));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call sendWelcomeEmailValidateBeforeCall(String evApiKey, String evAccessToken, String username, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'evApiKey' is set
        if (evApiKey == null) {
            throw new ApiException("Missing the required parameter 'evApiKey' when calling sendWelcomeEmail(Async)");
        }

        // verify the required parameter 'evAccessToken' is set
        if (evAccessToken == null) {
            throw new ApiException("Missing the required parameter 'evAccessToken' when calling sendWelcomeEmail(Async)");
        }

        // verify the required parameter 'username' is set
        if (username == null) {
            throw new ApiException("Missing the required parameter 'username' when calling sendWelcomeEmail(Async)");
        }

        return sendWelcomeEmailCall(evApiKey, evAccessToken, username, _callback);

    }

    /**
     * Resend welcome email to specific user
     * Send a welcome email to a user. The contents of the welcome email can be set by [PATCH /accounts](#operation/updateAccount).
     * @param evApiKey API Key required to make the API call. (required)
     * @param evAccessToken Access token required to make the API call. (required)
     * @param username A username to send the welcome email to. (required)
     * @return EmptyResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public EmptyResponse sendWelcomeEmail(String evApiKey, String evAccessToken, String username) throws ApiException {
        ApiResponse<EmptyResponse> localVarResp = sendWelcomeEmailWithHttpInfo(evApiKey, evAccessToken, username);
        return localVarResp.getData();
    }

    /**
     * Resend welcome email to specific user
     * Send a welcome email to a user. The contents of the welcome email can be set by [PATCH /accounts](#operation/updateAccount).
     * @param evApiKey API Key required to make the API call. (required)
     * @param evAccessToken Access token required to make the API call. (required)
     * @param username A username to send the welcome email to. (required)
     * @return ApiResponse&lt;EmptyResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EmptyResponse> sendWelcomeEmailWithHttpInfo(String evApiKey, String evAccessToken, String username) throws ApiException {
        okhttp3.Call localVarCall = sendWelcomeEmailValidateBeforeCall(evApiKey, evAccessToken, username, null);
        Type localVarReturnType = new TypeToken<EmptyResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Resend welcome email to specific user (asynchronously)
     * Send a welcome email to a user. The contents of the welcome email can be set by [PATCH /accounts](#operation/updateAccount).
     * @param evApiKey API Key required to make the API call. (required)
     * @param evAccessToken Access token required to make the API call. (required)
     * @param username A username to send the welcome email to. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call sendWelcomeEmailAsync(String evApiKey, String evAccessToken, String username, final ApiCallback<EmptyResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = sendWelcomeEmailValidateBeforeCall(evApiKey, evAccessToken, username, _callback);
        Type localVarReturnType = new TypeToken<EmptyResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
