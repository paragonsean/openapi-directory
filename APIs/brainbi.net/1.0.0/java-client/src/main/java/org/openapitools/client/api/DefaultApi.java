/*
 * brainbi
 * Welcome to the official API of the brainbi platform. Using this API you can freely integrate our analytics platform with any other solution.  Please refer to the following documentation and in case of any issues, please contact us at service@brainbi.net.  Please note: for this API you will use your email and password from the brainbi.net platform to gather a Bearer Token for any API calls (use Login and get token). Once you are finished with your calls, please do a logout to remove your token and keep your account safe (use logout).
 *
 * The version of the OpenAPI document: 1.0.0
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



import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DefaultApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DefaultApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DefaultApi(ApiClient apiClient) {
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
     * Build call for loginAndGetBearerToken
     * @param email The same email you use for our platform. (optional)
     * @param password The password email you use for our platform. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loginAndGetBearerTokenCall(String email, String password, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/login";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (email != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("email", email));
        }

        if (password != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("password", password));
        }

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call loginAndGetBearerTokenValidateBeforeCall(String email, String password, final ApiCallback _callback) throws ApiException {
        return loginAndGetBearerTokenCall(email, password, _callback);

    }

    /**
     * Login and get bearer token
     * Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.
     * @param email The same email you use for our platform. (optional)
     * @param password The password email you use for our platform. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void loginAndGetBearerToken(String email, String password) throws ApiException {
        loginAndGetBearerTokenWithHttpInfo(email, password);
    }

    /**
     * Login and get bearer token
     * Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.
     * @param email The same email you use for our platform. (optional)
     * @param password The password email you use for our platform. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> loginAndGetBearerTokenWithHttpInfo(String email, String password) throws ApiException {
        okhttp3.Call localVarCall = loginAndGetBearerTokenValidateBeforeCall(email, password, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Login and get bearer token (asynchronously)
     * Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.
     * @param email The same email you use for our platform. (optional)
     * @param password The password email you use for our platform. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call loginAndGetBearerTokenAsync(String email, String password, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = loginAndGetBearerTokenValidateBeforeCall(email, password, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for logout
     * @param email The same email you use for our platform. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call logoutCall(String email, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/logout";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (email != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("email", email));
        }

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call logoutValidateBeforeCall(String email, final ApiCallback _callback) throws ApiException {
        return logoutCall(email, _callback);

    }

    /**
     * Logout
     * Once you are done, call this endpoint to lock your account!
     * @param email The same email you use for our platform. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void logout(String email) throws ApiException {
        logoutWithHttpInfo(email);
    }

    /**
     * Logout
     * Once you are done, call this endpoint to lock your account!
     * @param email The same email you use for our platform. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> logoutWithHttpInfo(String email) throws ApiException {
        okhttp3.Call localVarCall = logoutValidateBeforeCall(email, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Logout (asynchronously)
     * Once you are done, call this endpoint to lock your account!
     * @param email The same email you use for our platform. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call logoutAsync(String email, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = logoutValidateBeforeCall(email, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for register
     * @param firstName required (optional)
     * @param lastName required (optional)
     * @param companyName required (optional)
     * @param shopUrl required (optional)
     * @param email required (optional)
     * @param storeName required (optional)
     * @param storeUrl required (optional)
     * @param password required (optional)
     * @param fromuser required (always 1) (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call registerCall(String firstName, String lastName, String companyName, String shopUrl, String email, String storeName, String storeUrl, String password, String fromuser, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/register";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (firstName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("first_name", firstName));
        }

        if (lastName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("last_name", lastName));
        }

        if (companyName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("company_name", companyName));
        }

        if (shopUrl != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("shop_url", shopUrl));
        }

        if (email != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("email", email));
        }

        if (storeName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("store_name", storeName));
        }

        if (storeUrl != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("store_url", storeUrl));
        }

        if (password != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("password", password));
        }

        if (fromuser != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("fromuser", fromuser));
        }

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call registerValidateBeforeCall(String firstName, String lastName, String companyName, String shopUrl, String email, String storeName, String storeUrl, String password, String fromuser, final ApiCallback _callback) throws ApiException {
        return registerCall(firstName, lastName, companyName, shopUrl, email, storeName, storeUrl, password, fromuser, _callback);

    }

    /**
     * Register
     * Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.
     * @param firstName required (optional)
     * @param lastName required (optional)
     * @param companyName required (optional)
     * @param shopUrl required (optional)
     * @param email required (optional)
     * @param storeName required (optional)
     * @param storeUrl required (optional)
     * @param password required (optional)
     * @param fromuser required (always 1) (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void register(String firstName, String lastName, String companyName, String shopUrl, String email, String storeName, String storeUrl, String password, String fromuser) throws ApiException {
        registerWithHttpInfo(firstName, lastName, companyName, shopUrl, email, storeName, storeUrl, password, fromuser);
    }

    /**
     * Register
     * Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.
     * @param firstName required (optional)
     * @param lastName required (optional)
     * @param companyName required (optional)
     * @param shopUrl required (optional)
     * @param email required (optional)
     * @param storeName required (optional)
     * @param storeUrl required (optional)
     * @param password required (optional)
     * @param fromuser required (always 1) (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> registerWithHttpInfo(String firstName, String lastName, String companyName, String shopUrl, String email, String storeName, String storeUrl, String password, String fromuser) throws ApiException {
        okhttp3.Call localVarCall = registerValidateBeforeCall(firstName, lastName, companyName, shopUrl, email, storeName, storeUrl, password, fromuser, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Register (asynchronously)
     * Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.
     * @param firstName required (optional)
     * @param lastName required (optional)
     * @param companyName required (optional)
     * @param shopUrl required (optional)
     * @param email required (optional)
     * @param storeName required (optional)
     * @param storeUrl required (optional)
     * @param password required (optional)
     * @param fromuser required (always 1) (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call registerAsync(String firstName, String lastName, String companyName, String shopUrl, String email, String storeName, String storeUrl, String password, String fromuser, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = registerValidateBeforeCall(firstName, lastName, companyName, shopUrl, email, storeName, storeUrl, password, fromuser, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for registerAndCreateStoreConnectionForWooCommerce
     * @param firstName required (optional)
     * @param lastName required (optional)
     * @param companyName required (optional)
     * @param shopUrl required (optional)
     * @param email required (optional)
     * @param storeName required (optional)
     * @param storeUrl required (optional)
     * @param password required (optional)
     * @param fromuser required (always 1) (optional)
     * @param apiUrl required (optional)
     * @param consumerKey required (optional)
     * @param consumerSecret required (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call registerAndCreateStoreConnectionForWooCommerceCall(String firstName, String lastName, String companyName, String shopUrl, String email, String storeName, String storeUrl, String password, String fromuser, String apiUrl, String consumerKey, String consumerSecret, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/register_woocommerce";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (firstName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("first_name", firstName));
        }

        if (lastName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("last_name", lastName));
        }

        if (companyName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("company_name", companyName));
        }

        if (shopUrl != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("shop_url", shopUrl));
        }

        if (email != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("email", email));
        }

        if (storeName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("store_name", storeName));
        }

        if (storeUrl != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("store_url", storeUrl));
        }

        if (password != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("password", password));
        }

        if (fromuser != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("fromuser", fromuser));
        }

        if (apiUrl != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("api_url", apiUrl));
        }

        if (consumerKey != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("consumer_key", consumerKey));
        }

        if (consumerSecret != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("consumer_secret", consumerSecret));
        }

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call registerAndCreateStoreConnectionForWooCommerceValidateBeforeCall(String firstName, String lastName, String companyName, String shopUrl, String email, String storeName, String storeUrl, String password, String fromuser, String apiUrl, String consumerKey, String consumerSecret, final ApiCallback _callback) throws ApiException {
        return registerAndCreateStoreConnectionForWooCommerceCall(firstName, lastName, companyName, shopUrl, email, storeName, storeUrl, password, fromuser, apiUrl, consumerKey, consumerSecret, _callback);

    }

    /**
     * Register and Create Store Connection for WooCommerce
     * Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.
     * @param firstName required (optional)
     * @param lastName required (optional)
     * @param companyName required (optional)
     * @param shopUrl required (optional)
     * @param email required (optional)
     * @param storeName required (optional)
     * @param storeUrl required (optional)
     * @param password required (optional)
     * @param fromuser required (always 1) (optional)
     * @param apiUrl required (optional)
     * @param consumerKey required (optional)
     * @param consumerSecret required (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void registerAndCreateStoreConnectionForWooCommerce(String firstName, String lastName, String companyName, String shopUrl, String email, String storeName, String storeUrl, String password, String fromuser, String apiUrl, String consumerKey, String consumerSecret) throws ApiException {
        registerAndCreateStoreConnectionForWooCommerceWithHttpInfo(firstName, lastName, companyName, shopUrl, email, storeName, storeUrl, password, fromuser, apiUrl, consumerKey, consumerSecret);
    }

    /**
     * Register and Create Store Connection for WooCommerce
     * Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.
     * @param firstName required (optional)
     * @param lastName required (optional)
     * @param companyName required (optional)
     * @param shopUrl required (optional)
     * @param email required (optional)
     * @param storeName required (optional)
     * @param storeUrl required (optional)
     * @param password required (optional)
     * @param fromuser required (always 1) (optional)
     * @param apiUrl required (optional)
     * @param consumerKey required (optional)
     * @param consumerSecret required (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> registerAndCreateStoreConnectionForWooCommerceWithHttpInfo(String firstName, String lastName, String companyName, String shopUrl, String email, String storeName, String storeUrl, String password, String fromuser, String apiUrl, String consumerKey, String consumerSecret) throws ApiException {
        okhttp3.Call localVarCall = registerAndCreateStoreConnectionForWooCommerceValidateBeforeCall(firstName, lastName, companyName, shopUrl, email, storeName, storeUrl, password, fromuser, apiUrl, consumerKey, consumerSecret, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Register and Create Store Connection for WooCommerce (asynchronously)
     * Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.
     * @param firstName required (optional)
     * @param lastName required (optional)
     * @param companyName required (optional)
     * @param shopUrl required (optional)
     * @param email required (optional)
     * @param storeName required (optional)
     * @param storeUrl required (optional)
     * @param password required (optional)
     * @param fromuser required (always 1) (optional)
     * @param apiUrl required (optional)
     * @param consumerKey required (optional)
     * @param consumerSecret required (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call registerAndCreateStoreConnectionForWooCommerceAsync(String firstName, String lastName, String companyName, String shopUrl, String email, String storeName, String storeUrl, String password, String fromuser, String apiUrl, String consumerKey, String consumerSecret, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = registerAndCreateStoreConnectionForWooCommerceValidateBeforeCall(firstName, lastName, companyName, shopUrl, email, storeName, storeUrl, password, fromuser, apiUrl, consumerKey, consumerSecret, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
