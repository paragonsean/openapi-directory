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


import org.openapitools.client.model.ListRegistrations200Response;
import org.openapitools.client.model.RegisterUser;
import org.openapitools.client.model.ResendEmailToVerifyRegistrationRequest;
import org.openapitools.client.model.ResendEmailToVerifyUserRequest;
import org.openapitools.client.model.UserRegistration;
import org.openapitools.client.model.UserRegistrationAcceptOrReject;
import org.openapitools.client.model.UserRegistrationRequest;
import org.openapitools.client.model.VerifyRegistrationEmailRequest;
import org.openapitools.client.model.VerifyUserRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class RegisterApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public RegisterApi() {
        this(Configuration.getDefaultApiClient());
    }

    public RegisterApi(ApiClient apiClient) {
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
     * Build call for acceptRegistration
     * @param registrationId Registration ID (required)
     * @param userRegistrationAcceptOrReject  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call acceptRegistrationCall(Integer registrationId, UserRegistrationAcceptOrReject userRegistrationAcceptOrReject, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = userRegistrationAcceptOrReject;

        // create path and map variables
        String localVarPath = "/api/v1/users/registrations/{registrationId}/accept"
            .replace("{" + "registrationId" + "}", localVarApiClient.escapeString(registrationId.toString()));

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
    private okhttp3.Call acceptRegistrationValidateBeforeCall(Integer registrationId, UserRegistrationAcceptOrReject userRegistrationAcceptOrReject, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'registrationId' is set
        if (registrationId == null) {
            throw new ApiException("Missing the required parameter 'registrationId' when calling acceptRegistration(Async)");
        }

        return acceptRegistrationCall(registrationId, userRegistrationAcceptOrReject, _callback);

    }

    /**
     * Accept registration
     * 
     * @param registrationId Registration ID (required)
     * @param userRegistrationAcceptOrReject  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void acceptRegistration(Integer registrationId, UserRegistrationAcceptOrReject userRegistrationAcceptOrReject) throws ApiException {
        acceptRegistrationWithHttpInfo(registrationId, userRegistrationAcceptOrReject);
    }

    /**
     * Accept registration
     * 
     * @param registrationId Registration ID (required)
     * @param userRegistrationAcceptOrReject  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> acceptRegistrationWithHttpInfo(Integer registrationId, UserRegistrationAcceptOrReject userRegistrationAcceptOrReject) throws ApiException {
        okhttp3.Call localVarCall = acceptRegistrationValidateBeforeCall(registrationId, userRegistrationAcceptOrReject, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Accept registration (asynchronously)
     * 
     * @param registrationId Registration ID (required)
     * @param userRegistrationAcceptOrReject  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call acceptRegistrationAsync(Integer registrationId, UserRegistrationAcceptOrReject userRegistrationAcceptOrReject, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = acceptRegistrationValidateBeforeCall(registrationId, userRegistrationAcceptOrReject, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteRegistration
     * @param registrationId Registration ID (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRegistrationCall(Integer registrationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/users/registrations/{registrationId}"
            .replace("{" + "registrationId" + "}", localVarApiClient.escapeString(registrationId.toString()));

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
    private okhttp3.Call deleteRegistrationValidateBeforeCall(Integer registrationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'registrationId' is set
        if (registrationId == null) {
            throw new ApiException("Missing the required parameter 'registrationId' when calling deleteRegistration(Async)");
        }

        return deleteRegistrationCall(registrationId, _callback);

    }

    /**
     * Delete registration
     * Delete the registration entry. It will not remove the user associated with this registration (if any)
     * @param registrationId Registration ID (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void deleteRegistration(Integer registrationId) throws ApiException {
        deleteRegistrationWithHttpInfo(registrationId);
    }

    /**
     * Delete registration
     * Delete the registration entry. It will not remove the user associated with this registration (if any)
     * @param registrationId Registration ID (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteRegistrationWithHttpInfo(Integer registrationId) throws ApiException {
        okhttp3.Call localVarCall = deleteRegistrationValidateBeforeCall(registrationId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete registration (asynchronously)
     * Delete the registration entry. It will not remove the user associated with this registration (if any)
     * @param registrationId Registration ID (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRegistrationAsync(Integer registrationId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteRegistrationValidateBeforeCall(registrationId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for listRegistrations
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param search  (optional)
     * @param sort  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listRegistrationsCall(Integer start, Integer count, String search, String sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/v1/users/registrations";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (start != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("start", start));
        }

        if (count != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("count", count));
        }

        if (search != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("search", search));
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
    private okhttp3.Call listRegistrationsValidateBeforeCall(Integer start, Integer count, String search, String sort, final ApiCallback _callback) throws ApiException {
        return listRegistrationsCall(start, count, search, sort, _callback);

    }

    /**
     * List registrations
     * 
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param search  (optional)
     * @param sort  (optional)
     * @return ListRegistrations200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ListRegistrations200Response listRegistrations(Integer start, Integer count, String search, String sort) throws ApiException {
        ApiResponse<ListRegistrations200Response> localVarResp = listRegistrationsWithHttpInfo(start, count, search, sort);
        return localVarResp.getData();
    }

    /**
     * List registrations
     * 
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param search  (optional)
     * @param sort  (optional)
     * @return ApiResponse&lt;ListRegistrations200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListRegistrations200Response> listRegistrationsWithHttpInfo(Integer start, Integer count, String search, String sort) throws ApiException {
        okhttp3.Call localVarCall = listRegistrationsValidateBeforeCall(start, count, search, sort, null);
        Type localVarReturnType = new TypeToken<ListRegistrations200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List registrations (asynchronously)
     * 
     * @param start Offset used to paginate results (optional)
     * @param count Number of items to return (optional, default to 15)
     * @param search  (optional)
     * @param sort  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listRegistrationsAsync(Integer start, Integer count, String search, String sort, final ApiCallback<ListRegistrations200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = listRegistrationsValidateBeforeCall(start, count, search, sort, _callback);
        Type localVarReturnType = new TypeToken<ListRegistrations200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for registerUser
     * @param registerUser  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> request error </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> user registration is not enabled, user limit is reached, registration is not allowed for the ip, requires approval or blocked by a plugin </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> a user with this username, channel name or email already exists </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call registerUserCall(RegisterUser registerUser, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = registerUser;

        // create path and map variables
        String localVarPath = "/api/v1/users/register";

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
    private okhttp3.Call registerUserValidateBeforeCall(RegisterUser registerUser, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'registerUser' is set
        if (registerUser == null) {
            throw new ApiException("Missing the required parameter 'registerUser' when calling registerUser(Async)");
        }

        return registerUserCall(registerUser, _callback);

    }

    /**
     * Register a user
     * Signup has to be enabled and signup approval is not required
     * @param registerUser  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> request error </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> user registration is not enabled, user limit is reached, registration is not allowed for the ip, requires approval or blocked by a plugin </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> a user with this username, channel name or email already exists </td><td>  -  </td></tr>
     </table>
     */
    public void registerUser(RegisterUser registerUser) throws ApiException {
        registerUserWithHttpInfo(registerUser);
    }

    /**
     * Register a user
     * Signup has to be enabled and signup approval is not required
     * @param registerUser  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> request error </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> user registration is not enabled, user limit is reached, registration is not allowed for the ip, requires approval or blocked by a plugin </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> a user with this username, channel name or email already exists </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> registerUserWithHttpInfo(RegisterUser registerUser) throws ApiException {
        okhttp3.Call localVarCall = registerUserValidateBeforeCall(registerUser, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Register a user (asynchronously)
     * Signup has to be enabled and signup approval is not required
     * @param registerUser  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> request error </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> user registration is not enabled, user limit is reached, registration is not allowed for the ip, requires approval or blocked by a plugin </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> a user with this username, channel name or email already exists </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call registerUserAsync(RegisterUser registerUser, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = registerUserValidateBeforeCall(registerUser, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for rejectRegistration
     * @param registrationId Registration ID (required)
     * @param userRegistrationAcceptOrReject  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call rejectRegistrationCall(Integer registrationId, UserRegistrationAcceptOrReject userRegistrationAcceptOrReject, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = userRegistrationAcceptOrReject;

        // create path and map variables
        String localVarPath = "/api/v1/users/registrations/{registrationId}/reject"
            .replace("{" + "registrationId" + "}", localVarApiClient.escapeString(registrationId.toString()));

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
    private okhttp3.Call rejectRegistrationValidateBeforeCall(Integer registrationId, UserRegistrationAcceptOrReject userRegistrationAcceptOrReject, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'registrationId' is set
        if (registrationId == null) {
            throw new ApiException("Missing the required parameter 'registrationId' when calling rejectRegistration(Async)");
        }

        return rejectRegistrationCall(registrationId, userRegistrationAcceptOrReject, _callback);

    }

    /**
     * Reject registration
     * 
     * @param registrationId Registration ID (required)
     * @param userRegistrationAcceptOrReject  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void rejectRegistration(Integer registrationId, UserRegistrationAcceptOrReject userRegistrationAcceptOrReject) throws ApiException {
        rejectRegistrationWithHttpInfo(registrationId, userRegistrationAcceptOrReject);
    }

    /**
     * Reject registration
     * 
     * @param registrationId Registration ID (required)
     * @param userRegistrationAcceptOrReject  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> rejectRegistrationWithHttpInfo(Integer registrationId, UserRegistrationAcceptOrReject userRegistrationAcceptOrReject) throws ApiException {
        okhttp3.Call localVarCall = rejectRegistrationValidateBeforeCall(registrationId, userRegistrationAcceptOrReject, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Reject registration (asynchronously)
     * 
     * @param registrationId Registration ID (required)
     * @param userRegistrationAcceptOrReject  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call rejectRegistrationAsync(Integer registrationId, UserRegistrationAcceptOrReject userRegistrationAcceptOrReject, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = rejectRegistrationValidateBeforeCall(registrationId, userRegistrationAcceptOrReject, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for requestRegistration
     * @param userRegistrationRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> request error or signup approval is not enabled on the instance </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> user registration is not enabled, user limit is reached, registration is not allowed for the ip or blocked by a plugin </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> a user or registration with this username, channel name or email already exists </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call requestRegistrationCall(UserRegistrationRequest userRegistrationRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = userRegistrationRequest;

        // create path and map variables
        String localVarPath = "/api/v1/users/registrations/request";

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
    private okhttp3.Call requestRegistrationValidateBeforeCall(UserRegistrationRequest userRegistrationRequest, final ApiCallback _callback) throws ApiException {
        return requestRegistrationCall(userRegistrationRequest, _callback);

    }

    /**
     * Request registration
     * Signup has to be enabled and require approval on the instance
     * @param userRegistrationRequest  (optional)
     * @return UserRegistration
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> request error or signup approval is not enabled on the instance </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> user registration is not enabled, user limit is reached, registration is not allowed for the ip or blocked by a plugin </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> a user or registration with this username, channel name or email already exists </td><td>  -  </td></tr>
     </table>
     */
    public UserRegistration requestRegistration(UserRegistrationRequest userRegistrationRequest) throws ApiException {
        ApiResponse<UserRegistration> localVarResp = requestRegistrationWithHttpInfo(userRegistrationRequest);
        return localVarResp.getData();
    }

    /**
     * Request registration
     * Signup has to be enabled and require approval on the instance
     * @param userRegistrationRequest  (optional)
     * @return ApiResponse&lt;UserRegistration&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> request error or signup approval is not enabled on the instance </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> user registration is not enabled, user limit is reached, registration is not allowed for the ip or blocked by a plugin </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> a user or registration with this username, channel name or email already exists </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UserRegistration> requestRegistrationWithHttpInfo(UserRegistrationRequest userRegistrationRequest) throws ApiException {
        okhttp3.Call localVarCall = requestRegistrationValidateBeforeCall(userRegistrationRequest, null);
        Type localVarReturnType = new TypeToken<UserRegistration>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Request registration (asynchronously)
     * Signup has to be enabled and require approval on the instance
     * @param userRegistrationRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> request error or signup approval is not enabled on the instance </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> user registration is not enabled, user limit is reached, registration is not allowed for the ip or blocked by a plugin </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> a user or registration with this username, channel name or email already exists </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call requestRegistrationAsync(UserRegistrationRequest userRegistrationRequest, final ApiCallback<UserRegistration> _callback) throws ApiException {

        okhttp3.Call localVarCall = requestRegistrationValidateBeforeCall(userRegistrationRequest, _callback);
        Type localVarReturnType = new TypeToken<UserRegistration>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for resendEmailToVerifyRegistration
     * @param resendEmailToVerifyRegistrationRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resendEmailToVerifyRegistrationCall(ResendEmailToVerifyRegistrationRequest resendEmailToVerifyRegistrationRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = resendEmailToVerifyRegistrationRequest;

        // create path and map variables
        String localVarPath = "/api/v1/users/registrations/ask-send-verify-email";

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
    private okhttp3.Call resendEmailToVerifyRegistrationValidateBeforeCall(ResendEmailToVerifyRegistrationRequest resendEmailToVerifyRegistrationRequest, final ApiCallback _callback) throws ApiException {
        return resendEmailToVerifyRegistrationCall(resendEmailToVerifyRegistrationRequest, _callback);

    }

    /**
     * Resend verification link to registration email
     * 
     * @param resendEmailToVerifyRegistrationRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public void resendEmailToVerifyRegistration(ResendEmailToVerifyRegistrationRequest resendEmailToVerifyRegistrationRequest) throws ApiException {
        resendEmailToVerifyRegistrationWithHttpInfo(resendEmailToVerifyRegistrationRequest);
    }

    /**
     * Resend verification link to registration email
     * 
     * @param resendEmailToVerifyRegistrationRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> resendEmailToVerifyRegistrationWithHttpInfo(ResendEmailToVerifyRegistrationRequest resendEmailToVerifyRegistrationRequest) throws ApiException {
        okhttp3.Call localVarCall = resendEmailToVerifyRegistrationValidateBeforeCall(resendEmailToVerifyRegistrationRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Resend verification link to registration email (asynchronously)
     * 
     * @param resendEmailToVerifyRegistrationRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call resendEmailToVerifyRegistrationAsync(ResendEmailToVerifyRegistrationRequest resendEmailToVerifyRegistrationRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = resendEmailToVerifyRegistrationValidateBeforeCall(resendEmailToVerifyRegistrationRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for resendEmailToVerifyUser_0
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
    public okhttp3.Call resendEmailToVerifyUser_0Call(ResendEmailToVerifyUserRequest resendEmailToVerifyUserRequest, final ApiCallback _callback) throws ApiException {
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
    private okhttp3.Call resendEmailToVerifyUser_0ValidateBeforeCall(ResendEmailToVerifyUserRequest resendEmailToVerifyUserRequest, final ApiCallback _callback) throws ApiException {
        return resendEmailToVerifyUser_0Call(resendEmailToVerifyUserRequest, _callback);

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
    public void resendEmailToVerifyUser_0(ResendEmailToVerifyUserRequest resendEmailToVerifyUserRequest) throws ApiException {
        resendEmailToVerifyUser_0WithHttpInfo(resendEmailToVerifyUserRequest);
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
    public ApiResponse<Void> resendEmailToVerifyUser_0WithHttpInfo(ResendEmailToVerifyUserRequest resendEmailToVerifyUserRequest) throws ApiException {
        okhttp3.Call localVarCall = resendEmailToVerifyUser_0ValidateBeforeCall(resendEmailToVerifyUserRequest, null);
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
    public okhttp3.Call resendEmailToVerifyUser_0Async(ResendEmailToVerifyUserRequest resendEmailToVerifyUserRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = resendEmailToVerifyUser_0ValidateBeforeCall(resendEmailToVerifyUserRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for verifyRegistrationEmail
     * @param registrationId Registration ID (required)
     * @param verifyRegistrationEmailRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid verification string </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> registration not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call verifyRegistrationEmailCall(Integer registrationId, VerifyRegistrationEmailRequest verifyRegistrationEmailRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = verifyRegistrationEmailRequest;

        // create path and map variables
        String localVarPath = "/api/v1/users/registrations/{registrationId}/verify-email"
            .replace("{" + "registrationId" + "}", localVarApiClient.escapeString(registrationId.toString()));

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
    private okhttp3.Call verifyRegistrationEmailValidateBeforeCall(Integer registrationId, VerifyRegistrationEmailRequest verifyRegistrationEmailRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'registrationId' is set
        if (registrationId == null) {
            throw new ApiException("Missing the required parameter 'registrationId' when calling verifyRegistrationEmail(Async)");
        }

        return verifyRegistrationEmailCall(registrationId, verifyRegistrationEmailRequest, _callback);

    }

    /**
     * Verify a registration email
     * Following a user registration request, the user will receive an email asking to click a link containing a secret. 
     * @param registrationId Registration ID (required)
     * @param verifyRegistrationEmailRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid verification string </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> registration not found </td><td>  -  </td></tr>
     </table>
     */
    public void verifyRegistrationEmail(Integer registrationId, VerifyRegistrationEmailRequest verifyRegistrationEmailRequest) throws ApiException {
        verifyRegistrationEmailWithHttpInfo(registrationId, verifyRegistrationEmailRequest);
    }

    /**
     * Verify a registration email
     * Following a user registration request, the user will receive an email asking to click a link containing a secret. 
     * @param registrationId Registration ID (required)
     * @param verifyRegistrationEmailRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid verification string </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> registration not found </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> verifyRegistrationEmailWithHttpInfo(Integer registrationId, VerifyRegistrationEmailRequest verifyRegistrationEmailRequest) throws ApiException {
        okhttp3.Call localVarCall = verifyRegistrationEmailValidateBeforeCall(registrationId, verifyRegistrationEmailRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Verify a registration email (asynchronously)
     * Following a user registration request, the user will receive an email asking to click a link containing a secret. 
     * @param registrationId Registration ID (required)
     * @param verifyRegistrationEmailRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> successful operation </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> invalid verification string </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> registration not found </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call verifyRegistrationEmailAsync(Integer registrationId, VerifyRegistrationEmailRequest verifyRegistrationEmailRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = verifyRegistrationEmailValidateBeforeCall(registrationId, verifyRegistrationEmailRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for verifyUser_0
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
    public okhttp3.Call verifyUser_0Call(Integer id, VerifyUserRequest verifyUserRequest, final ApiCallback _callback) throws ApiException {
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
    private okhttp3.Call verifyUser_0ValidateBeforeCall(Integer id, VerifyUserRequest verifyUserRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling verifyUser_0(Async)");
        }

        return verifyUser_0Call(id, verifyUserRequest, _callback);

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
    public void verifyUser_0(Integer id, VerifyUserRequest verifyUserRequest) throws ApiException {
        verifyUser_0WithHttpInfo(id, verifyUserRequest);
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
    public ApiResponse<Void> verifyUser_0WithHttpInfo(Integer id, VerifyUserRequest verifyUserRequest) throws ApiException {
        okhttp3.Call localVarCall = verifyUser_0ValidateBeforeCall(id, verifyUserRequest, null);
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
    public okhttp3.Call verifyUser_0Async(Integer id, VerifyUserRequest verifyUserRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = verifyUser_0ValidateBeforeCall(id, verifyUserRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
