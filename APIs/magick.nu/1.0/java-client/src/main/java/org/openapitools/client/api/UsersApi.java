/*
 * Tradeworks
 * Authentication is required to access all methods of the API. Enter username and password.                 Credentials are automatically set as you type.
 *
 * The version of the OpenAPI document: 1.0
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


import org.openapitools.client.model.PasswordDTO;
import org.openapitools.client.model.UserDTO;

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
     * Build call for getUsersEmailEmail
     * @param email  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getUsersEmailEmailCall(String email, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users/email/{email}"
            .replace("{" + "email" + "}", localVarApiClient.escapeString(email.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getUsersEmailEmailValidateBeforeCall(String email, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'email' is set
        if (email == null) {
            throw new ApiException("Missing the required parameter 'email' when calling getUsersEmailEmail(Async)");
        }

        return getUsersEmailEmailCall(email, _callback);

    }

    /**
     * Check if email is available
     * 
     * @param email  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public void getUsersEmailEmail(String email) throws ApiException {
        getUsersEmailEmailWithHttpInfo(email);
    }

    /**
     * Check if email is available
     * 
     * @param email  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> getUsersEmailEmailWithHttpInfo(String email) throws ApiException {
        okhttp3.Call localVarCall = getUsersEmailEmailValidateBeforeCall(email, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Check if email is available (asynchronously)
     * 
     * @param email  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getUsersEmailEmailAsync(String email, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getUsersEmailEmailValidateBeforeCall(email, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getUsersUsernameUsername
     * @param username  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getUsersUsernameUsernameCall(String username, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users/username/{username}"
            .replace("{" + "username" + "}", localVarApiClient.escapeString(username.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getUsersUsernameUsernameValidateBeforeCall(String username, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'username' is set
        if (username == null) {
            throw new ApiException("Missing the required parameter 'username' when calling getUsersUsernameUsername(Async)");
        }

        return getUsersUsernameUsernameCall(username, _callback);

    }

    /**
     * Check if username is available
     * 
     * @param username  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public void getUsersUsernameUsername(String username) throws ApiException {
        getUsersUsernameUsernameWithHttpInfo(username);
    }

    /**
     * Check if username is available
     * 
     * @param username  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> getUsersUsernameUsernameWithHttpInfo(String username) throws ApiException {
        okhttp3.Call localVarCall = getUsersUsernameUsernameValidateBeforeCall(username, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Check if username is available (asynchronously)
     * 
     * @param username  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getUsersUsernameUsernameAsync(String username, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getUsersUsernameUsernameValidateBeforeCall(username, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for postUsers
     * @param body  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postUsersCall(UserDTO body, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users";

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
    private okhttp3.Call postUsersValidateBeforeCall(UserDTO body, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'body' is set
        if (body == null) {
            throw new ApiException("Missing the required parameter 'body' when calling postUsers(Async)");
        }

        return postUsersCall(body, _callback);

    }

    /**
     * Create a new Tradeworks User
     * 
     * @param body  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public void postUsers(UserDTO body) throws ApiException {
        postUsersWithHttpInfo(body);
    }

    /**
     * Create a new Tradeworks User
     * 
     * @param body  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> postUsersWithHttpInfo(UserDTO body) throws ApiException {
        okhttp3.Call localVarCall = postUsersValidateBeforeCall(body, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Create a new Tradeworks User (asynchronously)
     * 
     * @param body  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postUsersAsync(UserDTO body, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = postUsersValidateBeforeCall(body, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for putUsersPasswordUsername
     * @param username  (required)
     * @param body  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putUsersPasswordUsernameCall(String username, PasswordDTO body, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/users/password/{username}"
            .replace("{" + "username" + "}", localVarApiClient.escapeString(username.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putUsersPasswordUsernameValidateBeforeCall(String username, PasswordDTO body, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'username' is set
        if (username == null) {
            throw new ApiException("Missing the required parameter 'username' when calling putUsersPasswordUsername(Async)");
        }

        // verify the required parameter 'body' is set
        if (body == null) {
            throw new ApiException("Missing the required parameter 'body' when calling putUsersPasswordUsername(Async)");
        }

        return putUsersPasswordUsernameCall(username, body, _callback);

    }

    /**
     * Update user&#39;s password
     * 
     * @param username  (required)
     * @param body  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public void putUsersPasswordUsername(String username, PasswordDTO body) throws ApiException {
        putUsersPasswordUsernameWithHttpInfo(username, body);
    }

    /**
     * Update user&#39;s password
     * 
     * @param username  (required)
     * @param body  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> putUsersPasswordUsernameWithHttpInfo(String username, PasswordDTO body) throws ApiException {
        okhttp3.Call localVarCall = putUsersPasswordUsernameValidateBeforeCall(username, body, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update user&#39;s password (asynchronously)
     * 
     * @param username  (required)
     * @param body  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> No response was specified </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putUsersPasswordUsernameAsync(String username, PasswordDTO body, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = putUsersPasswordUsernameValidateBeforeCall(username, body, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
