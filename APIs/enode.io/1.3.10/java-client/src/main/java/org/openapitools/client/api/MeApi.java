/*
 * Enode API
 * Download [OpenAPI 3.0 Specification](/OpenAPI-Enode-v1.4.0.json)  Download [Postman Collection](/Postman-Enode-v1.4.0.json)  The Enode API is designed to make smart charging applications easy to develop. We provide an abstraction layer that reduces the complexity when extracting vehicle data and sending commands to vehicles from a variety of manufacturers.  The API has a RESTful architecture and utilizes OAuth2 authorization.  We are always available to handle any issues or just answer your questions. Feel free to reach out on post@enode.io   ## Registration for API access In order to use the API you will need a `client_id` and `client_secret`. Please contact us if you are interested in using our API in production, and we will provide these credentials.  # Authorization Vehicle / hardware access via the Enode API is granted to your application by the User in a standard OAuth `Authorization Code` flow.  > The authorization scheme documented here is the recommended approach for most situations. However, it is also possible to user other OAuth flows, non-confidential clients, and temporary users. Please feel free to contact us if you have any questions about your use-case or the integration of your existing infrastructure.  ### Preparation: Configure your OAuth client  Because Enode API implements the OAuth 2.0 spec completely and without modifications, you can avoid rolling your own OAuth client implementation and instead use a well-supported and battle-tested implementation. This is strongly recommended. Information on available OAuth clients for many languages is available [here](https://oauth.net/code/)  To configure your chosen OAuth client, you will need these details: - Your `client_id` - Your `client_secret` - Authorization URL: `https://link.test.enode.io/oauth2/auth` - Token URL: `https://link.test.enode.io/oauth2/token`  ```javascript // Node.js + openid-client example const enodeIssuer = await Issuer.discover('https://link.test.enode.io'); const client = new enodeIssuer.Client({   client_id: 'xyz',   client_secret: 'shhhhh',   redirect_uris: ['http://localhost:5000/callback'],   response_types: ['code'], }); ```   ### Preparation: Obtain a client access token via OAuth Client Credentials Grant Your OAuth client will have a method for using the `OAuth 2.0 Client Credentials Grant` to obtain an access token.  ```javascript // Node.js + openid-client example const clientAccessToken = await client.grant({grant_type: \"client_credentials\"}); ```  This access token belongs to your client and is used for administrative actions, such as the next step.  This token should be cached by your server and reused until it expires, at which point your server should request a new one.    ### Step 1. Generate an Enode Link session for your User and launch the OAuth flow  When your User indicates that they want to connect their hardware to your app, your server must call [Link User](#operation/postUsersUseridLink) to generate an Enode Link session for your User. The User ID can be any string that uniquely identifies the User, but it is recommended that you use the primary key by which you identify the User within your application.  Example Request: ``` POST /users/{userId}/link HTTP/1.1 Authorization: Bearer {access_token} {   \"forceLanguage\": \"nb-NO\",   \"vendor\": \"Tesla\", } ```  Example Response: ``` {     \"linkState\": \"ZjE2MzMxMGFiYmU4MzcxOTU1ZmRjMTU5NGU2ZmE4YTU3NjViMzIwY2YzNG\", } ```  The returned linkState must be stored by your server, attached to the session of the authenticated user for which it was generated.  Your OAuth client will provide a method to construct an authorization URL for your user. That method will require these details: - Redirect URI - The URI to which your user should be redirected when the Oauth flow completes - Scope - The OAuth scope(s) you wish to request access to (see list of valid values [here](#section/Authentication/AccessTokenBearer)) - State - The value of `linkState` from the request above  To launch the OAuth flow, send your user to the authorization URL constructed by your OAuth client. This can be done in an embedded webview within a native iOS/Android app, or in the system's default browser.  ```javascript // Node.js + openid-client + express example  // Construct an OAuth authorization URL const authorizationUrl = client.authorizationUrl({   scope: \"offline_access all\",   state: linkState });  // Redirect user to authorization URL res.redirect(authorizationUrl); ```   ### Step 2. User grants consent In the Link UI webapp the user will follow 3 steps:  1. Choose their hardware from a list of supported manufacturers (EVs and charging boxes). For certain EV makes it will be necessary to also select a charge box. 2. For each selection, the user will be presented with the login screen for that particular hardware. The user must successfully log in. 3. A summary of the requested scopes will be presented to the user. The user must choose whether to grant access to your application.   ### Step 3. OAuth flow concludes with a callback When the user has completed their interactions, they will be redirected to the `Redirect URI` you provided in Step 1, with various metadata appended as query parameters.  Your OAuth client will have a method to parse and validate that metadata, and fetch the granted access and refresh tokens.  Among that metadata will be a `state` value - you must verify that it is equal to the `linkState` value persisted in Step 1, as [a countermeasure against CSRF attacks](https://tools.ietf.org/html/rfc6819#section-4.4.1.8).  ```javascript // Node.js + openid-client + express example  // Fetch linkState from user session const linkState = get(req, 'session.linkState');  // Parse relevant parameters from request URL const params = client.callbackParams(req);  // Exchange authorization code for access and refresh tokens // In this example, openid-client does the linkState validation check for us const tokenSet = await client.oauthCallback('http://localhost:5000/callback', params, {state: linkState}) ```  With the access token in hand, you can now access resources on behalf of the user.   # Errors And Problems ## OAuth Authorization Request  When the User has completed the process of allowing/denying access in Enode Link, they will be redirected to your configured redirect URI. If something has gone wrong, query parameters `error` and `error_description` will be set as documented in [Section 4.1.2.1](https://tools.ietf.org/html/rfc6749#section-4.1.2.1) of the OAuth 2.0 spec:  |error                      |error_description| |---------------------------|-----------------| |invalid_request            |The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed.| |unauthorized_client        |The client is not authorized to request an authorization code using this method.| |access_denied              |The resource owner or authorization server denied the request.| |unsupported_response_type  |The authorization server does not support obtaining an authorization code using this method.| |invalid_scope              |The requested scope is invalid, unknown, or malformed.| |server_error               |The authorization server encountered an unexpected condition that prevented it from fulfilling the request.| |temporarily_unavailable    |The authorization server is currently unable to handle the request due to a temporary overloading or maintenance of the server|  Example: ``` https://website.example/oauth_callback?state=e0a86fe5&error=access_denied&error_description=The+resource+owner+or+authorization+server+denied+the+request. ```   ## Errors when accessing a User's resources  When using an `access_token` to access a User's resources, the following HTTP Status Codes in the 4XX range may be encountered:  |HTTP Status Code           |Explanation      | |---------------------------|-----------------| |400 Bad Request            |The request payload has failed schema validation / parsing |401 Unauthorized           |Authentication details are missing or invalid |403 Forbidden              |Authentication succeeded, but the authenticated user doesn't have access to the resource |404 Not Found              |A non-existent resource is requested |429 Too Many Requests      |Rate limiting by the vendor has prevented us from completing the request   In all cases, an [RFC7807 Problem Details](https://tools.ietf.org/html/rfc7807) body is returned to aid in debugging.  Example: ``` HTTP/1.1 400 Bad Request Content-Type: application/problem+json {   \"type\": \"https://docs.enode.io/problems/payload-validation-error\",   \"title\": \"Payload validation failed\",   \"detail\": \"\\\"authorizationRequest.scope\\\" is required\", } ```  
 *
 * The version of the OpenAPI document: 1.3.10
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


import org.openapitools.client.model.GetMe200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MeApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public MeApi() {
        this(Configuration.getDefaultApiClient());
    }

    public MeApi(ApiClient apiClient) {
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
     * Build call for disconnectVendor
     * @param vendor Vendor to be unlinked (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call disconnectVendorCall(String vendor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/me/vendors/{vendor}"
            .replace("{" + "vendor" + "}", localVarApiClient.escapeString(vendor.toString()));

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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "UserAccessToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call disconnectVendorValidateBeforeCall(String vendor, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'vendor' is set
        if (vendor == null) {
            throw new ApiException("Missing the required parameter 'vendor' when calling disconnectVendor(Async)");
        }

        return disconnectVendorCall(vendor, _callback);

    }

    /**
     * Disconnect Vendor
     * Disconnect a single Vendor from the User&#39;s account.  All stored data about their Vendor account will be deleted, and any vehicles that were provided by that Vendor will disappear from the system.
     * @param vendor Vendor to be unlinked (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public void disconnectVendor(String vendor) throws ApiException {
        disconnectVendorWithHttpInfo(vendor);
    }

    /**
     * Disconnect Vendor
     * Disconnect a single Vendor from the User&#39;s account.  All stored data about their Vendor account will be deleted, and any vehicles that were provided by that Vendor will disappear from the system.
     * @param vendor Vendor to be unlinked (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> disconnectVendorWithHttpInfo(String vendor) throws ApiException {
        okhttp3.Call localVarCall = disconnectVendorValidateBeforeCall(vendor, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Disconnect Vendor (asynchronously)
     * Disconnect a single Vendor from the User&#39;s account.  All stored data about their Vendor account will be deleted, and any vehicles that were provided by that Vendor will disappear from the system.
     * @param vendor Vendor to be unlinked (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call disconnectVendorAsync(String vendor, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = disconnectVendorValidateBeforeCall(vendor, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getMe
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMeCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/me";

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

        String[] localVarAuthNames = new String[] { "UserAccessToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getMeValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getMeCall(_callback);

    }

    /**
     * Get My User
     * Returns metadata about the authenticated User, including a list of vendors for which the user has provided credentials.
     * @return GetMe200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public GetMe200Response getMe() throws ApiException {
        ApiResponse<GetMe200Response> localVarResp = getMeWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get My User
     * Returns metadata about the authenticated User, including a list of vendors for which the user has provided credentials.
     * @return ApiResponse&lt;GetMe200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetMe200Response> getMeWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getMeValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetMe200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get My User (asynchronously)
     * Returns metadata about the authenticated User, including a list of vendors for which the user has provided credentials.
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMeAsync(final ApiCallback<GetMe200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getMeValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetMe200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
