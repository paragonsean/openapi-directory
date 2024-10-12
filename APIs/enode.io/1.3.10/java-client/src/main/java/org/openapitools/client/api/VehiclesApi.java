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


import org.openapitools.client.model.GetVehicleChargestate200Response;
import org.openapitools.client.model.GetVehiclesVehicleid200Response;
import org.openapitools.client.model.GetVehiclesVehicleidInformation200Response;
import org.openapitools.client.model.GetVehiclesVehicleidLocation200Response;
import org.openapitools.client.model.GetVehiclesVehicleidOdometer200Response;
import org.openapitools.client.model.PostVehiclesVehicleidWatchRequest;
import org.openapitools.client.model.PutVehiclesVehicleidSmartchargingpolicyRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class VehiclesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public VehiclesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public VehiclesApi(ApiClient apiClient) {
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
     * Build call for getVehicleChargestate
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehicleChargestateCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vehicles/{vehicleId}/charge-state";

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
    private okhttp3.Call getVehicleChargestateValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getVehicleChargestateCall(_callback);

    }

    /**
     * Get Vehicle Charge State
     * 
     * @return GetVehicleChargestate200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public GetVehicleChargestate200Response getVehicleChargestate() throws ApiException {
        ApiResponse<GetVehicleChargestate200Response> localVarResp = getVehicleChargestateWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get Vehicle Charge State
     * 
     * @return ApiResponse&lt;GetVehicleChargestate200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetVehicleChargestate200Response> getVehicleChargestateWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getVehicleChargestateValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetVehicleChargestate200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Vehicle Charge State (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehicleChargestateAsync(final ApiCallback<GetVehicleChargestate200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVehicleChargestateValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetVehicleChargestate200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVehicles
     * @param field An optional array of Vehicle fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;location&#x60;   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehiclesCall(List<Object> field, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vehicles";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (field != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "field[]", field));
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

        String[] localVarAuthNames = new String[] { "UserAccessToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getVehiclesValidateBeforeCall(List<Object> field, final ApiCallback _callback) throws ApiException {
        return getVehiclesCall(field, _callback);

    }

    /**
     * List Vehicles
     * 
     * @param field An optional array of Vehicle fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;location&#x60;   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request. (optional)
     * @return List&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public List<Object> getVehicles(List<Object> field) throws ApiException {
        ApiResponse<List<Object>> localVarResp = getVehiclesWithHttpInfo(field);
        return localVarResp.getData();
    }

    /**
     * List Vehicles
     * 
     * @param field An optional array of Vehicle fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;location&#x60;   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request. (optional)
     * @return ApiResponse&lt;List&lt;Object&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Object>> getVehiclesWithHttpInfo(List<Object> field) throws ApiException {
        okhttp3.Call localVarCall = getVehiclesValidateBeforeCall(field, null);
        Type localVarReturnType = new TypeToken<List<Object>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List Vehicles (asynchronously)
     * 
     * @param field An optional array of Vehicle fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;location&#x60;   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehiclesAsync(List<Object> field, final ApiCallback<List<Object>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVehiclesValidateBeforeCall(field, _callback);
        Type localVarReturnType = new TypeToken<List<Object>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVehiclesVehicleid
     * @param vehicleId ID of the Vehicle (required)
     * @param field An optional array of Vehicle fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;location&#x60;   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehiclesVehicleidCall(String vehicleId, List<String> field, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vehicles/{vehicleId}"
            .replace("{" + "vehicleId" + "}", localVarApiClient.escapeString(vehicleId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (field != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "field[]", field));
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

        String[] localVarAuthNames = new String[] { "UserAccessToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getVehiclesVehicleidValidateBeforeCall(String vehicleId, List<String> field, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'vehicleId' is set
        if (vehicleId == null) {
            throw new ApiException("Missing the required parameter 'vehicleId' when calling getVehiclesVehicleid(Async)");
        }

        return getVehiclesVehicleidCall(vehicleId, field, _callback);

    }

    /**
     * Get Vehicle
     * 
     * @param vehicleId ID of the Vehicle (required)
     * @param field An optional array of Vehicle fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;location&#x60;   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request. (optional)
     * @return GetVehiclesVehicleid200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public GetVehiclesVehicleid200Response getVehiclesVehicleid(String vehicleId, List<String> field) throws ApiException {
        ApiResponse<GetVehiclesVehicleid200Response> localVarResp = getVehiclesVehicleidWithHttpInfo(vehicleId, field);
        return localVarResp.getData();
    }

    /**
     * Get Vehicle
     * 
     * @param vehicleId ID of the Vehicle (required)
     * @param field An optional array of Vehicle fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;location&#x60;   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request. (optional)
     * @return ApiResponse&lt;GetVehiclesVehicleid200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetVehiclesVehicleid200Response> getVehiclesVehicleidWithHttpInfo(String vehicleId, List<String> field) throws ApiException {
        okhttp3.Call localVarCall = getVehiclesVehicleidValidateBeforeCall(vehicleId, field, null);
        Type localVarReturnType = new TypeToken<GetVehiclesVehicleid200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Vehicle (asynchronously)
     * 
     * @param vehicleId ID of the Vehicle (required)
     * @param field An optional array of Vehicle fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;location&#x60;   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehiclesVehicleidAsync(String vehicleId, List<String> field, final ApiCallback<GetVehiclesVehicleid200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVehiclesVehicleidValidateBeforeCall(vehicleId, field, _callback);
        Type localVarReturnType = new TypeToken<GetVehiclesVehicleid200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVehiclesVehicleidInformation
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Descriptive information about the Vehicle </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehiclesVehicleidInformationCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vehicles/{vehicleId}/information";

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
    private okhttp3.Call getVehiclesVehicleidInformationValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getVehiclesVehicleidInformationCall(_callback);

    }

    /**
     * Get Vehicle Information
     * 
     * @return GetVehiclesVehicleidInformation200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Descriptive information about the Vehicle </td><td>  -  </td></tr>
     </table>
     */
    public GetVehiclesVehicleidInformation200Response getVehiclesVehicleidInformation() throws ApiException {
        ApiResponse<GetVehiclesVehicleidInformation200Response> localVarResp = getVehiclesVehicleidInformationWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get Vehicle Information
     * 
     * @return ApiResponse&lt;GetVehiclesVehicleidInformation200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Descriptive information about the Vehicle </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetVehiclesVehicleidInformation200Response> getVehiclesVehicleidInformationWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getVehiclesVehicleidInformationValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetVehiclesVehicleidInformation200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Vehicle Information (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Descriptive information about the Vehicle </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehiclesVehicleidInformationAsync(final ApiCallback<GetVehiclesVehicleidInformation200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVehiclesVehicleidInformationValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetVehiclesVehicleidInformation200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVehiclesVehicleidLocation
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Vehicle&#39;s GPS coordinates with timestamp </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehiclesVehicleidLocationCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vehicles/{vehicleId}/location";

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
    private okhttp3.Call getVehiclesVehicleidLocationValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getVehiclesVehicleidLocationCall(_callback);

    }

    /**
     * Get Vehicle Location
     * 
     * @return GetVehiclesVehicleidLocation200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Vehicle&#39;s GPS coordinates with timestamp </td><td>  -  </td></tr>
     </table>
     */
    public GetVehiclesVehicleidLocation200Response getVehiclesVehicleidLocation() throws ApiException {
        ApiResponse<GetVehiclesVehicleidLocation200Response> localVarResp = getVehiclesVehicleidLocationWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get Vehicle Location
     * 
     * @return ApiResponse&lt;GetVehiclesVehicleidLocation200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Vehicle&#39;s GPS coordinates with timestamp </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetVehiclesVehicleidLocation200Response> getVehiclesVehicleidLocationWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getVehiclesVehicleidLocationValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetVehiclesVehicleidLocation200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Vehicle Location (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Vehicle&#39;s GPS coordinates with timestamp </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehiclesVehicleidLocationAsync(final ApiCallback<GetVehiclesVehicleidLocation200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVehiclesVehicleidLocationValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetVehiclesVehicleidLocation200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVehiclesVehicleidOdometer
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Vehicle&#39;s odometer with timestamp </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehiclesVehicleidOdometerCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vehicles/{vehicleId}/odometer";

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
    private okhttp3.Call getVehiclesVehicleidOdometerValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getVehiclesVehicleidOdometerCall(_callback);

    }

    /**
     * Get Vehicle Odometer
     * 
     * @return GetVehiclesVehicleidOdometer200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Vehicle&#39;s odometer with timestamp </td><td>  -  </td></tr>
     </table>
     */
    public GetVehiclesVehicleidOdometer200Response getVehiclesVehicleidOdometer() throws ApiException {
        ApiResponse<GetVehiclesVehicleidOdometer200Response> localVarResp = getVehiclesVehicleidOdometerWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get Vehicle Odometer
     * 
     * @return ApiResponse&lt;GetVehiclesVehicleidOdometer200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Vehicle&#39;s odometer with timestamp </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetVehiclesVehicleidOdometer200Response> getVehiclesVehicleidOdometerWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getVehiclesVehicleidOdometerValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<GetVehiclesVehicleidOdometer200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Vehicle Odometer (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Vehicle&#39;s odometer with timestamp </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehiclesVehicleidOdometerAsync(final ApiCallback<GetVehiclesVehicleidOdometer200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVehiclesVehicleidOdometerValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<GetVehiclesVehicleidOdometer200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getVehiclesVehicleidSmartchargingpolicy
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehiclesVehicleidSmartchargingpolicyCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vehicles/{vehicleId}/smart-charging-policy";

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
    private okhttp3.Call getVehiclesVehicleidSmartchargingpolicyValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return getVehiclesVehicleidSmartchargingpolicyCall(_callback);

    }

    /**
     * Get Vehicle Smart Charging Policy
     * 
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public Object getVehiclesVehicleidSmartchargingpolicy() throws ApiException {
        ApiResponse<Object> localVarResp = getVehiclesVehicleidSmartchargingpolicyWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Get Vehicle Smart Charging Policy
     * 
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> getVehiclesVehicleidSmartchargingpolicyWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = getVehiclesVehicleidSmartchargingpolicyValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Vehicle Smart Charging Policy (asynchronously)
     * 
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getVehiclesVehicleidSmartchargingpolicyAsync(final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = getVehiclesVehicleidSmartchargingpolicyValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postVehiclesVehicleidCharging
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postVehiclesVehicleidChargingCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vehicles/{vehicleId}/charging";

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postVehiclesVehicleidChargingValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return postVehiclesVehicleidChargingCall(_callback);

    }

    /**
     * Start / Stop Charging
     * Instruct the vehicle to start or stop charging.   #### Precedence over smart charging If the vehicle is at a charging location where smart charging is activated: - a request to &#x60;start&#x60; charging will override smart charging and charging will stay on until fully charged.  - a request to &#x60;stop&#x60; charging will override smart charging and charging will be kept off for the duration of the current smart charging cycle.  The smart charging settings are not altered by these actions.
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public void postVehiclesVehicleidCharging() throws ApiException {
        postVehiclesVehicleidChargingWithHttpInfo();
    }

    /**
     * Start / Stop Charging
     * Instruct the vehicle to start or stop charging.   #### Precedence over smart charging If the vehicle is at a charging location where smart charging is activated: - a request to &#x60;start&#x60; charging will override smart charging and charging will stay on until fully charged.  - a request to &#x60;stop&#x60; charging will override smart charging and charging will be kept off for the duration of the current smart charging cycle.  The smart charging settings are not altered by these actions.
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> postVehiclesVehicleidChargingWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = postVehiclesVehicleidChargingValidateBeforeCall(null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Start / Stop Charging (asynchronously)
     * Instruct the vehicle to start or stop charging.   #### Precedence over smart charging If the vehicle is at a charging location where smart charging is activated: - a request to &#x60;start&#x60; charging will override smart charging and charging will stay on until fully charged.  - a request to &#x60;stop&#x60; charging will override smart charging and charging will be kept off for the duration of the current smart charging cycle.  The smart charging settings are not altered by these actions.
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postVehiclesVehicleidChargingAsync(final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = postVehiclesVehicleidChargingValidateBeforeCall(_callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for postVehiclesVehicleidWatch
     * @param vehicleId ID of the Vehicle (required)
     * @param postVehiclesVehicleidWatchRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postVehiclesVehicleidWatchCall(String vehicleId, PostVehiclesVehicleidWatchRequest postVehiclesVehicleidWatchRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = postVehiclesVehicleidWatchRequest;

        // create path and map variables
        String localVarPath = "/vehicles/{vehicleId}/watch"
            .replace("{" + "vehicleId" + "}", localVarApiClient.escapeString(vehicleId.toString()));

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

        String[] localVarAuthNames = new String[] { "UserAccessToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postVehiclesVehicleidWatchValidateBeforeCall(String vehicleId, PostVehiclesVehicleidWatchRequest postVehiclesVehicleidWatchRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'vehicleId' is set
        if (vehicleId == null) {
            throw new ApiException("Missing the required parameter 'vehicleId' when calling postVehiclesVehicleidWatch(Async)");
        }

        return postVehiclesVehicleidWatchCall(vehicleId, postVehiclesVehicleidWatchRequest, _callback);

    }

    /**
     * Start Watching Vehicle
     * Temporarily triggers high-rate updates of the vehicle&#39;s properties, and this state expires automatically. This gives you a way to tell us that user may be interacting with your application and are expecting as-fast-as-possible updates on the status of their vehicle in your UI.  Any data changes resulting from this high-rate updating are reflected everywhere, whether you pull data from the &#x60;Vehicles&#x60; endpoint, or recieve it via the [Firehose Webhook](#tag/Webhooks)  The specifics of the expiration times, watch behaviors, and change thresholds are tuned by us to make sure that they work as expected, without causing undue interruption to the vehicle. For many vendors, it is not appropriate to let the high-rate monitoring last indefinitely, as it will keep systems within the car awake that should be allowed to fall into low-power/standby modes. 
     * @param vehicleId ID of the Vehicle (required)
     * @param postVehiclesVehicleidWatchRequest  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public Object postVehiclesVehicleidWatch(String vehicleId, PostVehiclesVehicleidWatchRequest postVehiclesVehicleidWatchRequest) throws ApiException {
        ApiResponse<Object> localVarResp = postVehiclesVehicleidWatchWithHttpInfo(vehicleId, postVehiclesVehicleidWatchRequest);
        return localVarResp.getData();
    }

    /**
     * Start Watching Vehicle
     * Temporarily triggers high-rate updates of the vehicle&#39;s properties, and this state expires automatically. This gives you a way to tell us that user may be interacting with your application and are expecting as-fast-as-possible updates on the status of their vehicle in your UI.  Any data changes resulting from this high-rate updating are reflected everywhere, whether you pull data from the &#x60;Vehicles&#x60; endpoint, or recieve it via the [Firehose Webhook](#tag/Webhooks)  The specifics of the expiration times, watch behaviors, and change thresholds are tuned by us to make sure that they work as expected, without causing undue interruption to the vehicle. For many vendors, it is not appropriate to let the high-rate monitoring last indefinitely, as it will keep systems within the car awake that should be allowed to fall into low-power/standby modes. 
     * @param vehicleId ID of the Vehicle (required)
     * @param postVehiclesVehicleidWatchRequest  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> postVehiclesVehicleidWatchWithHttpInfo(String vehicleId, PostVehiclesVehicleidWatchRequest postVehiclesVehicleidWatchRequest) throws ApiException {
        okhttp3.Call localVarCall = postVehiclesVehicleidWatchValidateBeforeCall(vehicleId, postVehiclesVehicleidWatchRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Start Watching Vehicle (asynchronously)
     * Temporarily triggers high-rate updates of the vehicle&#39;s properties, and this state expires automatically. This gives you a way to tell us that user may be interacting with your application and are expecting as-fast-as-possible updates on the status of their vehicle in your UI.  Any data changes resulting from this high-rate updating are reflected everywhere, whether you pull data from the &#x60;Vehicles&#x60; endpoint, or recieve it via the [Firehose Webhook](#tag/Webhooks)  The specifics of the expiration times, watch behaviors, and change thresholds are tuned by us to make sure that they work as expected, without causing undue interruption to the vehicle. For many vendors, it is not appropriate to let the high-rate monitoring last indefinitely, as it will keep systems within the car awake that should be allowed to fall into low-power/standby modes. 
     * @param vehicleId ID of the Vehicle (required)
     * @param postVehiclesVehicleidWatchRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postVehiclesVehicleidWatchAsync(String vehicleId, PostVehiclesVehicleidWatchRequest postVehiclesVehicleidWatchRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postVehiclesVehicleidWatchValidateBeforeCall(vehicleId, postVehiclesVehicleidWatchRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putVehiclesVehicleidSmartchargingpolicy
     * @param vehicleId ID of the Vehicle (required)
     * @param putVehiclesVehicleidSmartchargingpolicyRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putVehiclesVehicleidSmartchargingpolicyCall(String vehicleId, PutVehiclesVehicleidSmartchargingpolicyRequest putVehiclesVehicleidSmartchargingpolicyRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = putVehiclesVehicleidSmartchargingpolicyRequest;

        // create path and map variables
        String localVarPath = "/vehicles/{vehicleId}/smart-charging-policy"
            .replace("{" + "vehicleId" + "}", localVarApiClient.escapeString(vehicleId.toString()));

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

        String[] localVarAuthNames = new String[] { "UserAccessToken" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putVehiclesVehicleidSmartchargingpolicyValidateBeforeCall(String vehicleId, PutVehiclesVehicleidSmartchargingpolicyRequest putVehiclesVehicleidSmartchargingpolicyRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'vehicleId' is set
        if (vehicleId == null) {
            throw new ApiException("Missing the required parameter 'vehicleId' when calling putVehiclesVehicleidSmartchargingpolicy(Async)");
        }

        return putVehiclesVehicleidSmartchargingpolicyCall(vehicleId, putVehiclesVehicleidSmartchargingpolicyRequest, _callback);

    }

    /**
     * Update Vehicle Smart Charging Policy
     * Updates the Smart Charging settings for a vehicle
     * @param vehicleId ID of the Vehicle (required)
     * @param putVehiclesVehicleidSmartchargingpolicyRequest  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public Object putVehiclesVehicleidSmartchargingpolicy(String vehicleId, PutVehiclesVehicleidSmartchargingpolicyRequest putVehiclesVehicleidSmartchargingpolicyRequest) throws ApiException {
        ApiResponse<Object> localVarResp = putVehiclesVehicleidSmartchargingpolicyWithHttpInfo(vehicleId, putVehiclesVehicleidSmartchargingpolicyRequest);
        return localVarResp.getData();
    }

    /**
     * Update Vehicle Smart Charging Policy
     * Updates the Smart Charging settings for a vehicle
     * @param vehicleId ID of the Vehicle (required)
     * @param putVehiclesVehicleidSmartchargingpolicyRequest  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> putVehiclesVehicleidSmartchargingpolicyWithHttpInfo(String vehicleId, PutVehiclesVehicleidSmartchargingpolicyRequest putVehiclesVehicleidSmartchargingpolicyRequest) throws ApiException {
        okhttp3.Call localVarCall = putVehiclesVehicleidSmartchargingpolicyValidateBeforeCall(vehicleId, putVehiclesVehicleidSmartchargingpolicyRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update Vehicle Smart Charging Policy (asynchronously)
     * Updates the Smart Charging settings for a vehicle
     * @param vehicleId ID of the Vehicle (required)
     * @param putVehiclesVehicleidSmartchargingpolicyRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putVehiclesVehicleidSmartchargingpolicyAsync(String vehicleId, PutVehiclesVehicleidSmartchargingpolicyRequest putVehiclesVehicleidSmartchargingpolicyRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = putVehiclesVehicleidSmartchargingpolicyValidateBeforeCall(vehicleId, putVehiclesVehicleidSmartchargingpolicyRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
