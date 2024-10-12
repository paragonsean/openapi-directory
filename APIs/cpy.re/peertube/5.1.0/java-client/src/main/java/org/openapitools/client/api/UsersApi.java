/*
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
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


import org.openapitools.client.model.AddUser;
import org.openapitools.client.model.AddUserResponse;
import org.openapitools.client.model.ConfirmTwoFactorRequestRequest;
import org.openapitools.client.model.DisableTwoFactorRequest;
import org.openapitools.client.model.GetUser200Response;
import org.openapitools.client.model.RequestTwoFactorResponse;
import org.openapitools.client.model.ResendEmailToVerifyUserRequest;
import org.openapitools.client.model.UpdateUser;
import org.openapitools.client.model.User;
import org.openapitools.client.model.VerifyUserRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class UsersApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public UsersApi() {
        this(Configuration.getDefaultApiClient());
    }

    public UsersApi(ApiClient apiClient) {
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
     * Build call for addUser
     * @param addUser If the smtp server is configured, you can leave the password empty and an email will be sent asking the user to set it first.  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> user created </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> insufficient authority to create an admin or moderator </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addUserCall(AddUser addUser, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addUser;

        // create path and map variables
        String localVarPath = "/api/v1/users";

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call addUserValidateBeforeCall(AddUser addUser, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'addUser' is set
        if (addUser == null) {
            throw new ApiException("Missing the required parameter 'addUser' when calling addUser(Async)");
        }

        return addUserCall(addUser, _callback);

    }

    /**
     * Create a user
     * 
     * @param addUser If the smtp server is configured, you can leave the password empty and an email will be sent asking the user to set it first.  (required)
     * @return AddUserResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> user created </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> insufficient authority to create an admin or moderator </td><td>  -  </td></tr>
     </table>
     */
    public AddUserResponse addUser(AddUser addUser) throws ApiException {
        ApiResponse<AddUserResponse> localVarResp = addUserWithHttpInfo(addUser);
        return localVarResp.getData();
    }

    /**
     * Create a user
     * 
     * @param addUser If the smtp server is configured, you can leave the password empty and an email will be sent asking the user to set it first.  (required)
     * @return ApiResponse&lt;AddUserResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> user created </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> insufficient authority to create an admin or moderator </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<AddUserResponse> addUserWithHttpInfo(AddUser addUser) throws ApiException {
        okhttp3.Call localVarCall = addUserValidateBeforeCall(addUser, null);
        Type localVarReturnType = new TypeToken<AddUserResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a user (asynchronously)
     * 
     * @param addUser If the smtp server is configured, you can leave the password empty and an email will be sent asking the user to set it first.  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> user created </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> insufficient authority to create an admin or moderator </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addUserAsync(AddUser addUser, final ApiCallback<AddUserResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = addUserValidateBeforeCall(addUser, _callback);
        Type localVarReturnType = new TypeToken<AddUserResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for confirmTwoFactorRequest
     * @param id Entity id (required)
     * @param confirmTwoFactorRequestRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid request token or OTP token </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call confirmTwoFactorRequestCall(Integer id, ConfirmTwoFactorRequestRequest confirmTwoFactorRequestRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = confirmTwoFactorRequestRequest;

        // create path and map variables
        String localVarPath = "/api/v1/users/{id}/two-factor/confirm-request"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call confirmTwoFactorRequestValidateBeforeCall(Integer id, ConfirmTwoFactorRequestRequest confirmTwoFactorRequestRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling confirmTwoFactorRequest(Async)");
        }

        return confirmTwoFactorRequestCall(id, confirmTwoFactorRequestRequest, _callback);

    }

    /**
     * Confirm two factor auth
     * Confirm a two factor authentication request
     * @param id Entity id (required)
     * @param confirmTwoFactorRequestRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid request token or OTP token </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public void confirmTwoFactorRequest(Integer id, ConfirmTwoFactorRequestRequest confirmTwoFactorRequestRequest) throws ApiException {
        confirmTwoFactorRequestWithHttpInfo(id, confirmTwoFactorRequestRequest);
    }

    /**
     * Confirm two factor auth
     * Confirm a two factor authentication request
     * @param id Entity id (required)
     * @param confirmTwoFactorRequestRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid request token or OTP token </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> confirmTwoFactorRequestWithHttpInfo(Integer id, ConfirmTwoFactorRequestRequest confirmTwoFactorRequestRequest) throws ApiException {
        okhttp3.Call localVarCall = confirmTwoFactorRequestValidateBeforeCall(id, confirmTwoFactorRequestRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Confirm two factor auth (asynchronously)
     * Confirm a two factor authentication request
     * @param id Entity id (required)
     * @param confirmTwoFactorRequestRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid request token or OTP token </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call confirmTwoFactorRequestAsync(Integer id, ConfirmTwoFactorRequestRequest confirmTwoFactorRequestRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = confirmTwoFactorRequestValidateBeforeCall(id, confirmTwoFactorRequestRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for delUser
     * @param id Entity id (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call delUserCall(Integer id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/users/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call delUserValidateBeforeCall(Integer id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling delUser(Async)");
        }

        return delUserCall(id, _callback);

    }

    /**
     * Delete a user
     * 
     * @param id Entity id (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void delUser(Integer id) throws ApiException {
        delUserWithHttpInfo(id);
    }

    /**
     * Delete a user
     * 
     * @param id Entity id (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> delUserWithHttpInfo(Integer id) throws ApiException {
        okhttp3.Call localVarCall = delUserValidateBeforeCall(id, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a user (asynchronously)
     * 
     * @param id Entity id (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call delUserAsync(Integer id, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = delUserValidateBeforeCall(id, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for disableTwoFactor
     * @param id Entity id (required)
     * @param disableTwoFactorRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid password </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call disableTwoFactorCall(Integer id, DisableTwoFactorRequest disableTwoFactorRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = disableTwoFactorRequest;

        // create path and map variables
        String localVarPath = "/api/v1/users/{id}/two-factor/disable"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call disableTwoFactorValidateBeforeCall(Integer id, DisableTwoFactorRequest disableTwoFactorRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling disableTwoFactor(Async)");
        }

        return disableTwoFactorCall(id, disableTwoFactorRequest, _callback);

    }

    /**
     * Disable two factor auth
     * Disable two factor authentication of a user
     * @param id Entity id (required)
     * @param disableTwoFactorRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid password </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public void disableTwoFactor(Integer id, DisableTwoFactorRequest disableTwoFactorRequest) throws ApiException {
        disableTwoFactorWithHttpInfo(id, disableTwoFactorRequest);
    }

    /**
     * Disable two factor auth
     * Disable two factor authentication of a user
     * @param id Entity id (required)
     * @param disableTwoFactorRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid password </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> disableTwoFactorWithHttpInfo(Integer id, DisableTwoFactorRequest disableTwoFactorRequest) throws ApiException {
        okhttp3.Call localVarCall = disableTwoFactorValidateBeforeCall(id, disableTwoFactorRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Disable two factor auth (asynchronously)
     * Disable two factor authentication of a user
     * @param id Entity id (required)
     * @param disableTwoFactorRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid password </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call disableTwoFactorAsync(Integer id, DisableTwoFactorRequest disableTwoFactorRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = disableTwoFactorValidateBeforeCall(id, disableTwoFactorRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getUser
     * @param id Entity id (required)
     * @param withStats include statistics about the user (only available as a moderator/admin) (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> As an admin/moderator, you can request a response augmented with statistics about the user&#39;s moderation relations and videos usage, by using the &#x60;withStats&#x60; parameter.  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getUserCall(Integer id, Boolean withStats, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/users/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (withStats != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("withStats", withStats));
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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getUserValidateBeforeCall(Integer id, Boolean withStats, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getUser(Async)");
        }

        return getUserCall(id, withStats, _callback);

    }

    /**
     * Get a user
     * 
     * @param id Entity id (required)
     * @param withStats include statistics about the user (only available as a moderator/admin) (optional)
     * @return GetUser200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> As an admin/moderator, you can request a response augmented with statistics about the user&#39;s moderation relations and videos usage, by using the &#x60;withStats&#x60; parameter.  </td><td>  -  </td></tr>
     </table>
     */
    public GetUser200Response getUser(Integer id, Boolean withStats) throws ApiException {
        ApiResponse<GetUser200Response> localVarResp = getUserWithHttpInfo(id, withStats);
        return localVarResp.getData();
    }

    /**
     * Get a user
     * 
     * @param id Entity id (required)
     * @param withStats include statistics about the user (only available as a moderator/admin) (optional)
     * @return ApiResponse&lt;GetUser200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> As an admin/moderator, you can request a response augmented with statistics about the user&#39;s moderation relations and videos usage, by using the &#x60;withStats&#x60; parameter.  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetUser200Response> getUserWithHttpInfo(Integer id, Boolean withStats) throws ApiException {
        okhttp3.Call localVarCall = getUserValidateBeforeCall(id, withStats, null);
        Type localVarReturnType = new TypeToken<GetUser200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a user (asynchronously)
     * 
     * @param id Entity id (required)
     * @param withStats include statistics about the user (only available as a moderator/admin) (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> As an admin/moderator, you can request a response augmented with statistics about the user&#39;s moderation relations and videos usage, by using the &#x60;withStats&#x60; parameter.  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getUserAsync(Integer id, Boolean withStats, final ApiCallback<GetUser200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getUserValidateBeforeCall(id, withStats, _callback);
        Type localVarReturnType = new TypeToken<GetUser200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getUsers
     * @param search Plain text search that will match with user usernames or emails (optional)
     * @param blocked Filter results down to (un)banned users (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort users by criteria (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getUsersCall(String search, Boolean blocked, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/users";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (search != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("search", search));
        }

        if (blocked != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("blocked", blocked));
        }

        if (start != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start", start));
        }

        if (count != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("count", count));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getUsersValidateBeforeCall(String search, Boolean blocked, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
        return getUsersCall(search, blocked, start, count, sort, _callback);

    }

    /**
     * List users
     * 
     * @param search Plain text search that will match with user usernames or emails (optional)
     * @param blocked Filter results down to (un)banned users (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort users by criteria (optional)
     * @return List&lt;User&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public List<User> getUsers(String search, Boolean blocked, Integer start, Integer count, String sort) throws ApiException {
        ApiResponse<List<User>> localVarResp = getUsersWithHttpInfo(search, blocked, start, count, sort);
        return localVarResp.getData();
    }

    /**
     * List users
     * 
     * @param search Plain text search that will match with user usernames or emails (optional)
     * @param blocked Filter results down to (un)banned users (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort users by criteria (optional)
     * @return ApiResponse&lt;List&lt;User&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<User>> getUsersWithHttpInfo(String search, Boolean blocked, Integer start, Integer count, String sort) throws ApiException {
        okhttp3.Call localVarCall = getUsersValidateBeforeCall(search, blocked, start, count, sort, null);
        Type localVarReturnType = new TypeToken<List<User>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List users (asynchronously)
     * 
     * @param search Plain text search that will match with user usernames or emails (optional)
     * @param blocked Filter results down to (un)banned users (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort users by criteria (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getUsersAsync(String search, Boolean blocked, Integer start, Integer count, String sort, final ApiCallback<List<User>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getUsersValidateBeforeCall(search, blocked, start, count, sort, _callback);
        Type localVarReturnType = new TypeToken<List<User>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putUser
     * @param id Entity id (required)
     * @param updateUser  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putUserCall(Integer id, UpdateUser updateUser, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateUser;

        // create path and map variables
        String localVarPath = "/api/v1/users/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putUserValidateBeforeCall(Integer id, UpdateUser updateUser, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling putUser(Async)");
        }

        // verify the required parameter 'updateUser' is set
        if (updateUser == null) {
            throw new ApiException("Missing the required parameter 'updateUser' when calling putUser(Async)");
        }

        return putUserCall(id, updateUser, _callback);

    }

    /**
     * Update a user
     * 
     * @param id Entity id (required)
     * @param updateUser  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void putUser(Integer id, UpdateUser updateUser) throws ApiException {
        putUserWithHttpInfo(id, updateUser);
    }

    /**
     * Update a user
     * 
     * @param id Entity id (required)
     * @param updateUser  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> putUserWithHttpInfo(Integer id, UpdateUser updateUser) throws ApiException {
        okhttp3.Call localVarCall = putUserValidateBeforeCall(id, updateUser, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update a user (asynchronously)
     * 
     * @param id Entity id (required)
     * @param updateUser  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putUserAsync(Integer id, UpdateUser updateUser, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = putUserValidateBeforeCall(id, updateUser, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for requestTwoFactor
     * @param id Entity id (required)
     * @param disableTwoFactorRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid password </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call requestTwoFactorCall(Integer id, DisableTwoFactorRequest disableTwoFactorRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = disableTwoFactorRequest;

        // create path and map variables
        String localVarPath = "/api/v1/users/{id}/two-factor/request"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call requestTwoFactorValidateBeforeCall(Integer id, DisableTwoFactorRequest disableTwoFactorRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling requestTwoFactor(Async)");
        }

        return requestTwoFactorCall(id, disableTwoFactorRequest, _callback);

    }

    /**
     * Request two factor auth
     * Request two factor authentication for a user
     * @param id Entity id (required)
     * @param disableTwoFactorRequest  (optional)
     * @return List&lt;RequestTwoFactorResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid password </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public List<RequestTwoFactorResponse> requestTwoFactor(Integer id, DisableTwoFactorRequest disableTwoFactorRequest) throws ApiException {
        ApiResponse<List<RequestTwoFactorResponse>> localVarResp = requestTwoFactorWithHttpInfo(id, disableTwoFactorRequest);
        return localVarResp.getData();
    }

    /**
     * Request two factor auth
     * Request two factor authentication for a user
     * @param id Entity id (required)
     * @param disableTwoFactorRequest  (optional)
     * @return ApiResponse&lt;List&lt;RequestTwoFactorResponse&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid password </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<RequestTwoFactorResponse>> requestTwoFactorWithHttpInfo(Integer id, DisableTwoFactorRequest disableTwoFactorRequest) throws ApiException {
        okhttp3.Call localVarCall = requestTwoFactorValidateBeforeCall(id, disableTwoFactorRequest, null);
        Type localVarReturnType = new TypeToken<List<RequestTwoFactorResponse>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Request two factor auth (asynchronously)
     * Request two factor authentication for a user
     * @param id Entity id (required)
     * @param disableTwoFactorRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid password </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call requestTwoFactorAsync(Integer id, DisableTwoFactorRequest disableTwoFactorRequest, final ApiCallback<List<RequestTwoFactorResponse>> _callback) throws ApiException {

        okhttp3.Call localVarCall = requestTwoFactorValidateBeforeCall(id, disableTwoFactorRequest, _callback);
        Type localVarReturnType = new TypeToken<List<RequestTwoFactorResponse>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for resendEmailToVerifyUser
     * @param resendEmailToVerifyUserRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resendEmailToVerifyUserCall(ResendEmailToVerifyUserRequest resendEmailToVerifyUserRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = resendEmailToVerifyUserRequest;

        // create path and map variables
        String localVarPath = "/api/v1/users/ask-send-verify-email";

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call resendEmailToVerifyUserValidateBeforeCall(ResendEmailToVerifyUserRequest resendEmailToVerifyUserRequest, final ApiCallback _callback) throws ApiException {
        return resendEmailToVerifyUserCall(resendEmailToVerifyUserRequest, _callback);

    }

    /**
     * Resend user verification link
     * 
     * @param resendEmailToVerifyUserRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void resendEmailToVerifyUser(ResendEmailToVerifyUserRequest resendEmailToVerifyUserRequest) throws ApiException {
        resendEmailToVerifyUserWithHttpInfo(resendEmailToVerifyUserRequest);
    }

    /**
     * Resend user verification link
     * 
     * @param resendEmailToVerifyUserRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> resendEmailToVerifyUserWithHttpInfo(ResendEmailToVerifyUserRequest resendEmailToVerifyUserRequest) throws ApiException {
        okhttp3.Call localVarCall = resendEmailToVerifyUserValidateBeforeCall(resendEmailToVerifyUserRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Resend user verification link (asynchronously)
     * 
     * @param resendEmailToVerifyUserRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resendEmailToVerifyUserAsync(ResendEmailToVerifyUserRequest resendEmailToVerifyUserRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = resendEmailToVerifyUserValidateBeforeCall(resendEmailToVerifyUserRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for verifyUser
     * @param id Entity id (required)
     * @param verifyUserRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid verification string </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call verifyUserCall(Integer id, VerifyUserRequest verifyUserRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = verifyUserRequest;

        // create path and map variables
        String localVarPath = "/api/v1/users/{id}/verify-email"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call verifyUserValidateBeforeCall(Integer id, VerifyUserRequest verifyUserRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling verifyUser(Async)");
        }

        return verifyUserCall(id, verifyUserRequest, _callback);

    }

    /**
     * Verify a user
     * Following a user registration, the new user will receive an email asking to click a link containing a secret. This endpoint can also be used to verify a new email set in the user account. 
     * @param id Entity id (required)
     * @param verifyUserRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid verification string </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public void verifyUser(Integer id, VerifyUserRequest verifyUserRequest) throws ApiException {
        verifyUserWithHttpInfo(id, verifyUserRequest);
    }

    /**
     * Verify a user
     * Following a user registration, the new user will receive an email asking to click a link containing a secret. This endpoint can also be used to verify a new email set in the user account. 
     * @param id Entity id (required)
     * @param verifyUserRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid verification string </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> verifyUserWithHttpInfo(Integer id, VerifyUserRequest verifyUserRequest) throws ApiException {
        okhttp3.Call localVarCall = verifyUserValidateBeforeCall(id, verifyUserRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Verify a user (asynchronously)
     * Following a user registration, the new user will receive an email asking to click a link containing a secret. This endpoint can also be used to verify a new email set in the user account. 
     * @param id Entity id (required)
     * @param verifyUserRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid verification string </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> user not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call verifyUserAsync(Integer id, VerifyUserRequest verifyUserRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = verifyUserValidateBeforeCall(id, verifyUserRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
