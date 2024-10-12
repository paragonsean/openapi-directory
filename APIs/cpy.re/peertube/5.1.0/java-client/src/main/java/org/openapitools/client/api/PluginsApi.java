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


import org.openapitools.client.model.AddPluginRequest;
import org.openapitools.client.model.ApiV1PluginsNpmNameSettingsPutRequest;
import org.openapitools.client.model.Plugin;
import org.openapitools.client.model.PluginResponse;
import org.openapitools.client.model.UninstallPluginRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PluginsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public PluginsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public PluginsApi(ApiClient apiClient) {
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
     * Build call for addPlugin
     * @param addPluginRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> should have either &#x60;npmName&#x60; or &#x60;path&#x60; set </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addPluginCall(AddPluginRequest addPluginRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addPluginRequest;

        // create path and map variables
        String localVarPath = "/api/v1/plugins/install";

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call addPluginValidateBeforeCall(AddPluginRequest addPluginRequest, final ApiCallback _callback) throws ApiException {
        return addPluginCall(addPluginRequest, _callback);

    }

    /**
     * Install a plugin
     * 
     * @param addPluginRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> should have either &#x60;npmName&#x60; or &#x60;path&#x60; set </td><td>  -  </td></tr>
     </table>
     */
    public void addPlugin(AddPluginRequest addPluginRequest) throws ApiException {
        addPluginWithHttpInfo(addPluginRequest);
    }

    /**
     * Install a plugin
     * 
     * @param addPluginRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> should have either &#x60;npmName&#x60; or &#x60;path&#x60; set </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> addPluginWithHttpInfo(AddPluginRequest addPluginRequest) throws ApiException {
        okhttp3.Call localVarCall = addPluginValidateBeforeCall(addPluginRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Install a plugin (asynchronously)
     * 
     * @param addPluginRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> should have either &#x60;npmName&#x60; or &#x60;path&#x60; set </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call addPluginAsync(AddPluginRequest addPluginRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = addPluginValidateBeforeCall(addPluginRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1PluginsNpmNamePublicSettingsGet
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1PluginsNpmNamePublicSettingsGetCall(String npmName, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/plugins/{npmName}/public-settings"
            .replace("{" + "npmName" + "}", localVarApiClient.escapeString(npmName.toString()));

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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV1PluginsNpmNamePublicSettingsGetValidateBeforeCall(String npmName, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'npmName' is set
        if (npmName == null) {
            throw new ApiException("Missing the required parameter 'npmName' when calling apiV1PluginsNpmNamePublicSettingsGet(Async)");
        }

        return apiV1PluginsNpmNamePublicSettingsGetCall(npmName, _callback);

    }

    /**
     * Get a plugin&#39;s public settings
     * 
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @return Map&lt;String, Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public Map<String, Object> apiV1PluginsNpmNamePublicSettingsGet(String npmName) throws ApiException {
        ApiResponse<Map<String, Object>> localVarResp = apiV1PluginsNpmNamePublicSettingsGetWithHttpInfo(npmName);
        return localVarResp.getData();
    }

    /**
     * Get a plugin&#39;s public settings
     * 
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @return ApiResponse&lt;Map&lt;String, Object&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Map<String, Object>> apiV1PluginsNpmNamePublicSettingsGetWithHttpInfo(String npmName) throws ApiException {
        okhttp3.Call localVarCall = apiV1PluginsNpmNamePublicSettingsGetValidateBeforeCall(npmName, null);
        Type localVarReturnType = new TypeToken<Map<String, Object>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a plugin&#39;s public settings (asynchronously)
     * 
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1PluginsNpmNamePublicSettingsGetAsync(String npmName, final ApiCallback<Map<String, Object>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1PluginsNpmNamePublicSettingsGetValidateBeforeCall(npmName, _callback);
        Type localVarReturnType = new TypeToken<Map<String, Object>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1PluginsNpmNameRegisteredSettingsGet
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1PluginsNpmNameRegisteredSettingsGetCall(String npmName, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/plugins/{npmName}/registered-settings"
            .replace("{" + "npmName" + "}", localVarApiClient.escapeString(npmName.toString()));

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiV1PluginsNpmNameRegisteredSettingsGetValidateBeforeCall(String npmName, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'npmName' is set
        if (npmName == null) {
            throw new ApiException("Missing the required parameter 'npmName' when calling apiV1PluginsNpmNameRegisteredSettingsGet(Async)");
        }

        return apiV1PluginsNpmNameRegisteredSettingsGetCall(npmName, _callback);

    }

    /**
     * Get a plugin&#39;s registered settings
     * 
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @return Map&lt;String, Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public Map<String, Object> apiV1PluginsNpmNameRegisteredSettingsGet(String npmName) throws ApiException {
        ApiResponse<Map<String, Object>> localVarResp = apiV1PluginsNpmNameRegisteredSettingsGetWithHttpInfo(npmName);
        return localVarResp.getData();
    }

    /**
     * Get a plugin&#39;s registered settings
     * 
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @return ApiResponse&lt;Map&lt;String, Object&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Map<String, Object>> apiV1PluginsNpmNameRegisteredSettingsGetWithHttpInfo(String npmName) throws ApiException {
        okhttp3.Call localVarCall = apiV1PluginsNpmNameRegisteredSettingsGetValidateBeforeCall(npmName, null);
        Type localVarReturnType = new TypeToken<Map<String, Object>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a plugin&#39;s registered settings (asynchronously)
     * 
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1PluginsNpmNameRegisteredSettingsGetAsync(String npmName, final ApiCallback<Map<String, Object>> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1PluginsNpmNameRegisteredSettingsGetValidateBeforeCall(npmName, _callback);
        Type localVarReturnType = new TypeToken<Map<String, Object>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for apiV1PluginsNpmNameSettingsPut
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @param apiV1PluginsNpmNameSettingsPutRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1PluginsNpmNameSettingsPutCall(String npmName, ApiV1PluginsNpmNameSettingsPutRequest apiV1PluginsNpmNameSettingsPutRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = apiV1PluginsNpmNameSettingsPutRequest;

        // create path and map variables
        String localVarPath = "/api/v1/plugins/{npmName}/settings"
            .replace("{" + "npmName" + "}", localVarApiClient.escapeString(npmName.toString()));

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
    private okhttp3.Call apiV1PluginsNpmNameSettingsPutValidateBeforeCall(String npmName, ApiV1PluginsNpmNameSettingsPutRequest apiV1PluginsNpmNameSettingsPutRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'npmName' is set
        if (npmName == null) {
            throw new ApiException("Missing the required parameter 'npmName' when calling apiV1PluginsNpmNameSettingsPut(Async)");
        }

        return apiV1PluginsNpmNameSettingsPutCall(npmName, apiV1PluginsNpmNameSettingsPutRequest, _callback);

    }

    /**
     * Set a plugin&#39;s settings
     * 
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @param apiV1PluginsNpmNameSettingsPutRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public void apiV1PluginsNpmNameSettingsPut(String npmName, ApiV1PluginsNpmNameSettingsPutRequest apiV1PluginsNpmNameSettingsPutRequest) throws ApiException {
        apiV1PluginsNpmNameSettingsPutWithHttpInfo(npmName, apiV1PluginsNpmNameSettingsPutRequest);
    }

    /**
     * Set a plugin&#39;s settings
     * 
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @param apiV1PluginsNpmNameSettingsPutRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> apiV1PluginsNpmNameSettingsPutWithHttpInfo(String npmName, ApiV1PluginsNpmNameSettingsPutRequest apiV1PluginsNpmNameSettingsPutRequest) throws ApiException {
        okhttp3.Call localVarCall = apiV1PluginsNpmNameSettingsPutValidateBeforeCall(npmName, apiV1PluginsNpmNameSettingsPutRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Set a plugin&#39;s settings (asynchronously)
     * 
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @param apiV1PluginsNpmNameSettingsPutRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiV1PluginsNpmNameSettingsPutAsync(String npmName, ApiV1PluginsNpmNameSettingsPutRequest apiV1PluginsNpmNameSettingsPutRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiV1PluginsNpmNameSettingsPutValidateBeforeCall(npmName, apiV1PluginsNpmNameSettingsPutRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAvailablePlugins
     * @param search  (optional)
     * @param pluginType  (optional)
     * @param currentPeerTubeEngine  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 503 </td><td> plugin index unavailable </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAvailablePluginsCall(String search, Integer pluginType, String currentPeerTubeEngine, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/plugins/available";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (search != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("search", search));
        }

        if (pluginType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("pluginType", pluginType));
        }

        if (currentPeerTubeEngine != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("currentPeerTubeEngine", currentPeerTubeEngine));
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
    private okhttp3.Call getAvailablePluginsValidateBeforeCall(String search, Integer pluginType, String currentPeerTubeEngine, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
        return getAvailablePluginsCall(search, pluginType, currentPeerTubeEngine, start, count, sort, _callback);

    }

    /**
     * List available plugins
     * 
     * @param search  (optional)
     * @param pluginType  (optional)
     * @param currentPeerTubeEngine  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return PluginResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 503 </td><td> plugin index unavailable </td><td>  -  </td></tr>
     </table>
     */
    public PluginResponse getAvailablePlugins(String search, Integer pluginType, String currentPeerTubeEngine, Integer start, Integer count, String sort) throws ApiException {
        ApiResponse<PluginResponse> localVarResp = getAvailablePluginsWithHttpInfo(search, pluginType, currentPeerTubeEngine, start, count, sort);
        return localVarResp.getData();
    }

    /**
     * List available plugins
     * 
     * @param search  (optional)
     * @param pluginType  (optional)
     * @param currentPeerTubeEngine  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return ApiResponse&lt;PluginResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 503 </td><td> plugin index unavailable </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PluginResponse> getAvailablePluginsWithHttpInfo(String search, Integer pluginType, String currentPeerTubeEngine, Integer start, Integer count, String sort) throws ApiException {
        okhttp3.Call localVarCall = getAvailablePluginsValidateBeforeCall(search, pluginType, currentPeerTubeEngine, start, count, sort, null);
        Type localVarReturnType = new TypeToken<PluginResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List available plugins (asynchronously)
     * 
     * @param search  (optional)
     * @param pluginType  (optional)
     * @param currentPeerTubeEngine  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 503 </td><td> plugin index unavailable </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAvailablePluginsAsync(String search, Integer pluginType, String currentPeerTubeEngine, Integer start, Integer count, String sort, final ApiCallback<PluginResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAvailablePluginsValidateBeforeCall(search, pluginType, currentPeerTubeEngine, start, count, sort, _callback);
        Type localVarReturnType = new TypeToken<PluginResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getPlugin
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPluginCall(String npmName, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/plugins/{npmName}"
            .replace("{" + "npmName" + "}", localVarApiClient.escapeString(npmName.toString()));

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

        String[] localVarAuthNames = new String[] { "OAuth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getPluginValidateBeforeCall(String npmName, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'npmName' is set
        if (npmName == null) {
            throw new ApiException("Missing the required parameter 'npmName' when calling getPlugin(Async)");
        }

        return getPluginCall(npmName, _callback);

    }

    /**
     * Get a plugin
     * 
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @return Plugin
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public Plugin getPlugin(String npmName) throws ApiException {
        ApiResponse<Plugin> localVarResp = getPluginWithHttpInfo(npmName);
        return localVarResp.getData();
    }

    /**
     * Get a plugin
     * 
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @return ApiResponse&lt;Plugin&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Plugin> getPluginWithHttpInfo(String npmName) throws ApiException {
        okhttp3.Call localVarCall = getPluginValidateBeforeCall(npmName, null);
        Type localVarReturnType = new TypeToken<Plugin>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a plugin (asynchronously)
     * 
     * @param npmName name of the plugin/theme on npmjs.com or in its package.json (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPluginAsync(String npmName, final ApiCallback<Plugin> _callback) throws ApiException {

        okhttp3.Call localVarCall = getPluginValidateBeforeCall(npmName, _callback);
        Type localVarReturnType = new TypeToken<Plugin>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getPlugins
     * @param pluginType  (optional)
     * @param uninstalled  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPluginsCall(Integer pluginType, Boolean uninstalled, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/plugins";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (pluginType != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("pluginType", pluginType));
        }

        if (uninstalled != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("uninstalled", uninstalled));
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
    private okhttp3.Call getPluginsValidateBeforeCall(Integer pluginType, Boolean uninstalled, Integer start, Integer count, String sort, final ApiCallback _callback) throws ApiException {
        return getPluginsCall(pluginType, uninstalled, start, count, sort, _callback);

    }

    /**
     * List plugins
     * 
     * @param pluginType  (optional)
     * @param uninstalled  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return PluginResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public PluginResponse getPlugins(Integer pluginType, Boolean uninstalled, Integer start, Integer count, String sort) throws ApiException {
        ApiResponse<PluginResponse> localVarResp = getPluginsWithHttpInfo(pluginType, uninstalled, start, count, sort);
        return localVarResp.getData();
    }

    /**
     * List plugins
     * 
     * @param pluginType  (optional)
     * @param uninstalled  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @return ApiResponse&lt;PluginResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PluginResponse> getPluginsWithHttpInfo(Integer pluginType, Boolean uninstalled, Integer start, Integer count, String sort) throws ApiException {
        okhttp3.Call localVarCall = getPluginsValidateBeforeCall(pluginType, uninstalled, start, count, sort, null);
        Type localVarReturnType = new TypeToken<PluginResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List plugins (asynchronously)
     * 
     * @param pluginType  (optional)
     * @param uninstalled  (optional)
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param sort Sort column (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPluginsAsync(Integer pluginType, Boolean uninstalled, Integer start, Integer count, String sort, final ApiCallback<PluginResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getPluginsValidateBeforeCall(pluginType, uninstalled, start, count, sort, _callback);
        Type localVarReturnType = new TypeToken<PluginResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for uninstallPlugin
     * @param uninstallPluginRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> existing plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call uninstallPluginCall(UninstallPluginRequest uninstallPluginRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = uninstallPluginRequest;

        // create path and map variables
        String localVarPath = "/api/v1/plugins/uninstall";

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call uninstallPluginValidateBeforeCall(UninstallPluginRequest uninstallPluginRequest, final ApiCallback _callback) throws ApiException {
        return uninstallPluginCall(uninstallPluginRequest, _callback);

    }

    /**
     * Uninstall a plugin
     * 
     * @param uninstallPluginRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> existing plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public void uninstallPlugin(UninstallPluginRequest uninstallPluginRequest) throws ApiException {
        uninstallPluginWithHttpInfo(uninstallPluginRequest);
    }

    /**
     * Uninstall a plugin
     * 
     * @param uninstallPluginRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> existing plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> uninstallPluginWithHttpInfo(UninstallPluginRequest uninstallPluginRequest) throws ApiException {
        okhttp3.Call localVarCall = uninstallPluginValidateBeforeCall(uninstallPluginRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Uninstall a plugin (asynchronously)
     * 
     * @param uninstallPluginRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> existing plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call uninstallPluginAsync(UninstallPluginRequest uninstallPluginRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = uninstallPluginValidateBeforeCall(uninstallPluginRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for updatePlugin
     * @param addPluginRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> should have either &#x60;npmName&#x60; or &#x60;path&#x60; set </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> existing plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updatePluginCall(AddPluginRequest addPluginRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addPluginRequest;

        // create path and map variables
        String localVarPath = "/api/v1/plugins/update";

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updatePluginValidateBeforeCall(AddPluginRequest addPluginRequest, final ApiCallback _callback) throws ApiException {
        return updatePluginCall(addPluginRequest, _callback);

    }

    /**
     * Update a plugin
     * 
     * @param addPluginRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> should have either &#x60;npmName&#x60; or &#x60;path&#x60; set </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> existing plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public void updatePlugin(AddPluginRequest addPluginRequest) throws ApiException {
        updatePluginWithHttpInfo(addPluginRequest);
    }

    /**
     * Update a plugin
     * 
     * @param addPluginRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> should have either &#x60;npmName&#x60; or &#x60;path&#x60; set </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> existing plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> updatePluginWithHttpInfo(AddPluginRequest addPluginRequest) throws ApiException {
        okhttp3.Call localVarCall = updatePluginValidateBeforeCall(addPluginRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update a plugin (asynchronously)
     * 
     * @param addPluginRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> should have either &#x60;npmName&#x60; or &#x60;path&#x60; set </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> existing plugin not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updatePluginAsync(AddPluginRequest addPluginRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = updatePluginValidateBeforeCall(addPluginRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
