/*
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
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


import org.openapitools.client.model.Error;
import org.openapitools.client.model.OauthRevokePostRequest;
import org.openapitools.client.model.OauthTokenPost200Response;
import org.openapitools.client.model.OauthTokenPostRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class OauthApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public OauthApi() {
        this(Configuration.getDefaultApiClient());
    }

    public OauthApi(ApiClient apiClient) {
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
     * Build call for oauthAuthorizeGet
     * @param responseType Should be set equal to code. (required)
     * @param clientId Client ID, obtained during app registration. (required)
     * @param redirectUri Set a URI to redirect the user to. If this parameter is set to urn:ietf:wg:oauth:2.0:oob then the authorization code will be shown instead. Must match one of the redirect URIs declared during app registration. (required)
     * @param scope List of requested OAuth scopes, separated by spaces (or by pluses, if using query parameters). Must be a subset of scopes declared during app registration. If not provided, defaults to read. (optional)
     * @param forceLogin Added in 2.6.0. Forces the user to re-login, which is necessary for authorizing with multiple accounts from the same instance. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The authorization code will be returned as a query parameter named code. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> If the authorization code is incorrect or has been used already, the request will fail. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call oauthAuthorizeGetCall(String responseType, String clientId, String redirectUri, String scope, Boolean forceLogin, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/oauth/authorize";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (responseType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("response_type", responseType));
        }

        if (clientId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("client_id", clientId));
        }

        if (redirectUri != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("redirect_uri", redirectUri));
        }

        if (scope != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("scope", scope));
        }

        if (forceLogin != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("force_login", forceLogin));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call oauthAuthorizeGetValidateBeforeCall(String responseType, String clientId, String redirectUri, String scope, Boolean forceLogin, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'responseType' is set
        if (responseType == null) {
            throw new ApiException("Missing the required parameter 'responseType' when calling oauthAuthorizeGet(Async)");
        }

        // verify the required parameter 'clientId' is set
        if (clientId == null) {
            throw new ApiException("Missing the required parameter 'clientId' when calling oauthAuthorizeGet(Async)");
        }

        // verify the required parameter 'redirectUri' is set
        if (redirectUri == null) {
            throw new ApiException("Missing the required parameter 'redirectUri' when calling oauthAuthorizeGet(Async)");
        }

        return oauthAuthorizeGetCall(responseType, clientId, redirectUri, scope, forceLogin, _callback);

    }

    /**
     * 
     * Displays an authorization form to the user. If approved, it will create and return an authorization code, then redirect to the desired redirect_uri, or show the authorization code if urn:ietf:wg:oauth:2.0:oob was requested. The authorization code can be used while requesting a token to obtain access to user-level methods.
     * @param responseType Should be set equal to code. (required)
     * @param clientId Client ID, obtained during app registration. (required)
     * @param redirectUri Set a URI to redirect the user to. If this parameter is set to urn:ietf:wg:oauth:2.0:oob then the authorization code will be shown instead. Must match one of the redirect URIs declared during app registration. (required)
     * @param scope List of requested OAuth scopes, separated by spaces (or by pluses, if using query parameters). Must be a subset of scopes declared during app registration. If not provided, defaults to read. (optional)
     * @param forceLogin Added in 2.6.0. Forces the user to re-login, which is necessary for authorizing with multiple accounts from the same instance. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The authorization code will be returned as a query parameter named code. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> If the authorization code is incorrect or has been used already, the request will fail. </td><td>  -  </td></tr>
     </table>
     */
    public void oauthAuthorizeGet(String responseType, String clientId, String redirectUri, String scope, Boolean forceLogin) throws ApiException {
        oauthAuthorizeGetWithHttpInfo(responseType, clientId, redirectUri, scope, forceLogin);
    }

    /**
     * 
     * Displays an authorization form to the user. If approved, it will create and return an authorization code, then redirect to the desired redirect_uri, or show the authorization code if urn:ietf:wg:oauth:2.0:oob was requested. The authorization code can be used while requesting a token to obtain access to user-level methods.
     * @param responseType Should be set equal to code. (required)
     * @param clientId Client ID, obtained during app registration. (required)
     * @param redirectUri Set a URI to redirect the user to. If this parameter is set to urn:ietf:wg:oauth:2.0:oob then the authorization code will be shown instead. Must match one of the redirect URIs declared during app registration. (required)
     * @param scope List of requested OAuth scopes, separated by spaces (or by pluses, if using query parameters). Must be a subset of scopes declared during app registration. If not provided, defaults to read. (optional)
     * @param forceLogin Added in 2.6.0. Forces the user to re-login, which is necessary for authorizing with multiple accounts from the same instance. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The authorization code will be returned as a query parameter named code. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> If the authorization code is incorrect or has been used already, the request will fail. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> oauthAuthorizeGetWithHttpInfo(String responseType, String clientId, String redirectUri, String scope, Boolean forceLogin) throws ApiException {
        okhttp3.Call localVarCall = oauthAuthorizeGetValidateBeforeCall(responseType, clientId, redirectUri, scope, forceLogin, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Displays an authorization form to the user. If approved, it will create and return an authorization code, then redirect to the desired redirect_uri, or show the authorization code if urn:ietf:wg:oauth:2.0:oob was requested. The authorization code can be used while requesting a token to obtain access to user-level methods.
     * @param responseType Should be set equal to code. (required)
     * @param clientId Client ID, obtained during app registration. (required)
     * @param redirectUri Set a URI to redirect the user to. If this parameter is set to urn:ietf:wg:oauth:2.0:oob then the authorization code will be shown instead. Must match one of the redirect URIs declared during app registration. (required)
     * @param scope List of requested OAuth scopes, separated by spaces (or by pluses, if using query parameters). Must be a subset of scopes declared during app registration. If not provided, defaults to read. (optional)
     * @param forceLogin Added in 2.6.0. Forces the user to re-login, which is necessary for authorizing with multiple accounts from the same instance. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> The authorization code will be returned as a query parameter named code. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> If the authorization code is incorrect or has been used already, the request will fail. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call oauthAuthorizeGetAsync(String responseType, String clientId, String redirectUri, String scope, Boolean forceLogin, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = oauthAuthorizeGetValidateBeforeCall(responseType, clientId, redirectUri, scope, forceLogin, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for oauthRevokePost
     * @param oauthRevokePostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> If you own the provided token, the API call will provide an empty response. This operation is idempotent, so calling this API multiple times will still return OK. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> If you provide a token you do not own, or no token at all, the API call will return a 403 error. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call oauthRevokePostCall(OauthRevokePostRequest oauthRevokePostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = oauthRevokePostRequest;

        // create path and map variables
        String localVarPath = "/oauth/revoke";

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
            "application/form-data"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call oauthRevokePostValidateBeforeCall(OauthRevokePostRequest oauthRevokePostRequest, final ApiCallback _callback) throws ApiException {
        return oauthRevokePostCall(oauthRevokePostRequest, _callback);

    }

    /**
     * 
     * Revoke an access token to make it no longer valid for use.
     * @param oauthRevokePostRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> If you own the provided token, the API call will provide an empty response. This operation is idempotent, so calling this API multiple times will still return OK. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> If you provide a token you do not own, or no token at all, the API call will return a 403 error. </td><td>  -  </td></tr>
     </table>
     */
    public void oauthRevokePost(OauthRevokePostRequest oauthRevokePostRequest) throws ApiException {
        oauthRevokePostWithHttpInfo(oauthRevokePostRequest);
    }

    /**
     * 
     * Revoke an access token to make it no longer valid for use.
     * @param oauthRevokePostRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> If you own the provided token, the API call will provide an empty response. This operation is idempotent, so calling this API multiple times will still return OK. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> If you provide a token you do not own, or no token at all, the API call will return a 403 error. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> oauthRevokePostWithHttpInfo(OauthRevokePostRequest oauthRevokePostRequest) throws ApiException {
        okhttp3.Call localVarCall = oauthRevokePostValidateBeforeCall(oauthRevokePostRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Revoke an access token to make it no longer valid for use.
     * @param oauthRevokePostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> If you own the provided token, the API call will provide an empty response. This operation is idempotent, so calling this API multiple times will still return OK. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> If you provide a token you do not own, or no token at all, the API call will return a 403 error. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call oauthRevokePostAsync(OauthRevokePostRequest oauthRevokePostRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = oauthRevokePostValidateBeforeCall(oauthRevokePostRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for oauthTokenPost
     * @param oauthTokenPostRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Store this access_token for later use with auth-required methods. The token should be passed as an HTTP Authorization header when making API calls, with the value Bearer access_token </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> If you try to request a scope that was not included when registering the app, the request will fail. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> If client_id and client_secret do not match or are invalid, the request will fail. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call oauthTokenPostCall(OauthTokenPostRequest oauthTokenPostRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = oauthTokenPostRequest;

        // create path and map variables
        String localVarPath = "/oauth/token";

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
            "application/form-data"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call oauthTokenPostValidateBeforeCall(OauthTokenPostRequest oauthTokenPostRequest, final ApiCallback _callback) throws ApiException {
        return oauthTokenPostCall(oauthTokenPostRequest, _callback);

    }

    /**
     * 
     * Returns an access token, to be used during API calls that are not public.
     * @param oauthTokenPostRequest  (optional)
     * @return OauthTokenPost200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Store this access_token for later use with auth-required methods. The token should be passed as an HTTP Authorization header when making API calls, with the value Bearer access_token </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> If you try to request a scope that was not included when registering the app, the request will fail. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> If client_id and client_secret do not match or are invalid, the request will fail. </td><td>  -  </td></tr>
     </table>
     */
    public OauthTokenPost200Response oauthTokenPost(OauthTokenPostRequest oauthTokenPostRequest) throws ApiException {
        ApiResponse<OauthTokenPost200Response> localVarResp = oauthTokenPostWithHttpInfo(oauthTokenPostRequest);
        return localVarResp.getData();
    }

    /**
     * 
     * Returns an access token, to be used during API calls that are not public.
     * @param oauthTokenPostRequest  (optional)
     * @return ApiResponse&lt;OauthTokenPost200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Store this access_token for later use with auth-required methods. The token should be passed as an HTTP Authorization header when making API calls, with the value Bearer access_token </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> If you try to request a scope that was not included when registering the app, the request will fail. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> If client_id and client_secret do not match or are invalid, the request will fail. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<OauthTokenPost200Response> oauthTokenPostWithHttpInfo(OauthTokenPostRequest oauthTokenPostRequest) throws ApiException {
        okhttp3.Call localVarCall = oauthTokenPostValidateBeforeCall(oauthTokenPostRequest, null);
        Type localVarReturnType = new TypeToken<OauthTokenPost200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Returns an access token, to be used during API calls that are not public.
     * @param oauthTokenPostRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Store this access_token for later use with auth-required methods. The token should be passed as an HTTP Authorization header when making API calls, with the value Bearer access_token </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> If you try to request a scope that was not included when registering the app, the request will fail. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> If client_id and client_secret do not match or are invalid, the request will fail. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call oauthTokenPostAsync(OauthTokenPostRequest oauthTokenPostRequest, final ApiCallback<OauthTokenPost200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = oauthTokenPostValidateBeforeCall(oauthTokenPostRequest, _callback);
        Type localVarReturnType = new TypeToken<OauthTokenPost200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
