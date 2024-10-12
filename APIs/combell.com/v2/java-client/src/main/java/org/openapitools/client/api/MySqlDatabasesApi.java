/*
 * Public Api
 * # Introduction  This API allows resellers to manage their resources in a simple, programmatic way using HTTP requests.  # Conventions  ## Requests  The API supports different methods depending on the required action.  | Method | Description | ---  | --- | GET  | Retrieve resources in a collection or get a single resource.<br/>Getters will never have any effect on the queried resources. | POST  | Create a new resource in a collection. | PUT  | Update an existing resource with its new representation. | DELETE | Delete an existing resource.  ## HTTP status codes  The API will reply with different HTTP statuscodes:  | StatusCode    | Description | ---      | --- | 200 OK     | The requests was processed and you receive data as a result. | 201 CREATED    | The resource has been created. Either the Location header contains a link to the created resource, or links are being returned in the response body. The applied method will be indicated in the documentation. | 202 ACCEPTED    | The request has been validated and accepted. Because we need to do some background processing prior to returning the result, we cannot send back a useful representation. | 204 NOCONTENT    | The request has been processed, but no details can be returned. | 400 BADREQUEST   | Your request is malformed. | 401 UNAUTHORIZED   | You are not authorized. Follow the instructions in the Authorization documentation. | 403 FORBIDDEN    | Access to the resource or operation is not allowed. | 404 NOTFOUND    | The resource cannot be found. | 410 GONE                  | The resource is permanently no longer available. | 429 TOOMANYREQUESTS  | The ratelimit has been exceeded. Please refer to the documentation on rate limiting for more details. | 500 INTERNALSERVERERROR | An error occurred during the processing of the request. The error is unexpected and most likely due to a bug in the api.  In the event of a problem, the body of the response will usually contain an errorcode and errormessage. In rare cases additional details about the error are reported.  Errorcodes 400-499 are considered to be client errors and indicate that there was an issue with the request. We will not take any action besides monitoring.   Errorcodes 500-599 are considered to be server errors. The errors are monitored AND action will be taken to resolve the error.  ## Formatting  Snake casing is applied on resources and query parameters. The API is strictly returning JSON. No other formats are supported.  Datetimes are returned in ISO-8601 format.  ## Pagination  Pagination is on by default on collections and is controlled by specifying *skip* and *take* parameters.   **Skip** indicates the number of results to skip and where to start the new take.   **Take** indicates the number of records to return. The returned number of items can be smaller than the requested take.  Paged results will have headers with useful information regarding the paging.  | Header    | Description | ---     | --- | X-Paging-Skipped  | The number of results that have been skipped. | X-Paging-Take   | The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. | X-Paging-TotalResults | The total number of results regardless of paging.  ## Rate limiting  The number of requests per interval is limited. Detailed information on the rate limiting can be found in specific headers which will be sent on each request.  | Header    | Description | ---     | --- | X-RateLimit-Limit  | The number of requests that can be made in a specific time interval. | X-RateLimit-Usage  | The number of requests already made in the current time interval. | X-RateLimit-Remaining | The number of requests remaining until the reset. | X-RateLimit-Reset  | The number of seconds until the reset.<br />After the reset you are allowed to make as many requests as specified by the X-RateLimit-Limit header. | Retry-After   | The number of seconds you have to wait until you can make new requests.<br />This header is only present when the rate limit has been reached. It is identical to X-RateLimit-Reset.  When the ratelimit has been reached, all requests will return with a HTTP statuscode 429 and ReasonPhrase '*Too many requests, retry later.*'.  # Authentication  The Api uses HMAC authentication.   Hash-based message authentication code (HMAC) is a mechanism for calculating a message authentication code involving a hash function in combination with a secret key.   Both the integrity and the authenticity of the message are verified this way.  ## Steps to generate the HMAC  1. Get your api key and secret from your controlpanel.   It is absolutely vital that the secret is never exposed. Once the secret is out, anyone would be able to generate hmacs to impersonate you.   In case your secret is compromised, you can generate a new api key and secret on your controlpanel. 2. Construct the input value for generating the hmac.   Concatenate:apikey, request method, path and querystring information, unix timestamp, nonce and content.  |          | Description | ---         | --- | apikey        | The key that is linked to your user. | request method      | lowercased (eg: get, post, delete,...) | path and querystring information  | urlencoding of the lowercased relative path and querystring.<br />The path **MUST start with the api version (/v2)**.<br />The hexadecimal codes (percent encoding) MUST be uppercased. | unix timestamp      | the unix timestamp in **seconds**. | nonce         | a unique string for each request. It should be a random string, not related to the request. The nonce (in combination with the unix timestamp) protects you from replay attacks in case anyone was able to intercept a request. | content        | When the request body is not empty, this should be the Base64 encoded Md5 hash of the request body.<br />An empty body should not be encoded.  3. Hash the concatenated string using your api secret and the SHA-256 algorithm. 4. Base64 encode the result of the hash function. This is the hmac signature you will need to send an authorized request.  ## Sending an authorized request  An authorized request can be made by sending the generated HMAC in the authorization header.   A correct authorizationheader uses the hmac authorization scheme and a correctly formatted authorization parameter.  Create the authorization parameter by concatenating:   * apikey   * colon ':'   * generated HMAC signature (see above)   * colon ':'   * nonce (the one used to generate the signature)   * colon ':'   * unix timestamp (the one used to generate the signature)  A sample (illustrated):  * The first line is the string you create to feed to the hashing algorithm. * The second line is the authorization header that should be sent in the request.  ![hmac authorization header illustrated](/v2/images/authentication_illustration.jpg \"authorization header illustrated\")  ## IP whitelisting  Access is by default restricted for all IP addresses. You need to explicitly whitelist an IP or an IP range in your controlpanel.  # Versioning  Because of breaking contract changes compared to v1, we released v2 of the API.   V1 will still be available, but you are strongly encouraged to migrate to the latest version.   New features will only be available on v2.  # Policy  ### Fair use policy  Please respect the rate limits and do not use the api for any purposes of abuse.   All requests are being monitored and logged.   Intentional abuse might result in api key revocation.  # Errors  The API attempts to return appropriate HTTP status codes for every request.   When the status code indicates failure, the API will also provide an error message in most cases.  An error message contains a machine-parseable error code accompanied by a descriptive error text.   The text for an error message might change over time, but codes will stay the same.  [An overview of error codes can be found here](/v2/documentation/errorcodes).  # Change log  [An overview of new changes can be found here](/v2/documentation/changelog).  # Provisioning information  ## Terminology  | Term   | Definition                | | ---   | ---                  | | Servicepack | Defines a set of assets that belong together. An example is a hosting package which offers Linux hosting, a domain name, a couple of mailboxes and databases.<br/>It also limits the size of individual assets within the same account. | | Account  | Represents an instance of the servicepack. It contains one or more assets. The number and size of assets is defined by the servicepack. | | Asset   | A manageable service. For example: a mysql database, a linux hosting, a mailbox,...<br/>Some assets are created at the moment when the account is created. Other assets can be created afterwards.   ## Common provisioning scenario  **Provisioning of an account with Linux hosting with one MySql database**  *Without a pre-existing account:*  1. Create a new account.<br/>Perform a POST on the accounts route and provide the desired servicepack id and identifier (domain name). 2. Read the Location header from the response and perform a GET of the provided resource (a provisioning job). 3. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).<br/> When the response returns 201(Created), you should read the response body. This will contain links to the created resources.<br/> This will usually hold only one link, but to be futureproof, this has been designed to return a collection. 4. The created resource will point to an account. You now know the account's Id and can continue with the provisioning of a MySql database on this account. 5. Perform a POST on the mysqldatabases route and provide the account id along with other requested information. 6. Read the Location header from the response and perform a GET of the provided resource (a provisioning job). 7. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).<br/> When the response returns 201(Created), you should read the response body. This will contain links to the created resources.<br/> This will usually hold only one link, but to be futureproof, this has been designed to return a collection. 8. The created resource will point to a MySql database resource.  ## SSL certificate requests  **Requesting an SSL certificate causes the purchase of a paying product.**  1. A certificate is created by adding an ssl certificate request. 2. Upon statuscode 201 you should query for certificate completion on the resource provided in the location response header. 3. The resource request can respond with different statuscodes: <ul>     <li>200: the certificate request is ongoing.<br/> Check the validations collection for validation values that are not auto_validated. Those should be set by you system.<br/> Call verify domain validations once all validation values are in place. It might take some time for verification to take place. It is not necessary to call this method more than once.</li>     <li>303: the certificate request is complete; there is no more certificate request resource available. Check the location header value to retrieve the representation of the resulting ssl certificate.</li>     <li>410: the certificate request does not exist anymore, there is no certificate created as a result of the request.</li> </ul>
 *
 * The version of the OpenAPI document: v2
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


import org.openapitools.client.model.BadRequestResponse;
import org.openapitools.client.model.CreateMySqlDatabase;
import org.openapitools.client.model.CreateMySqlUser;
import org.openapitools.client.model.MySqlDatabase;
import org.openapitools.client.model.MySqlUser;
import org.openapitools.client.model.UpdateUserPasswordRequest;
import org.openapitools.client.model.UpdateUserStatusRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MySqlDatabasesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public MySqlDatabasesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public MySqlDatabasesApi(ApiClient apiClient) {
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
     * Build call for changeDatabaseUserPassword
     * @param databaseName Name of the database. (required)
     * @param userName Name of the user. (required)
     * @param databaseName2 Automatically added (required)
     * @param userName2 Automatically added (required)
     * @param updateUserPasswordRequest Contains the new password. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeDatabaseUserPasswordCall(String databaseName, String userName, String databaseName2, String userName2, UpdateUserPasswordRequest updateUserPasswordRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateUserPasswordRequest;

        // create path and map variables
        String localVarPath = "/mysqldatabases/{databaseName}/users/{userName}/password"
            .replace("{" + "databaseName" + "}", localVarApiClient.escapeString(databaseName2.toString()))
            .replace("{" + "userName" + "}", localVarApiClient.escapeString(userName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (databaseName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("database_name", databaseName));
        }

        if (userName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("user_name", userName));
        }

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
    private okhttp3.Call changeDatabaseUserPasswordValidateBeforeCall(String databaseName, String userName, String databaseName2, String userName2, UpdateUserPasswordRequest updateUserPasswordRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'databaseName' is set
        if (databaseName == null) {
            throw new ApiException("Missing the required parameter 'databaseName' when calling changeDatabaseUserPassword(Async)");
        }

        // verify the required parameter 'userName' is set
        if (userName == null) {
            throw new ApiException("Missing the required parameter 'userName' when calling changeDatabaseUserPassword(Async)");
        }

        // verify the required parameter 'databaseName2' is set
        if (databaseName2 == null) {
            throw new ApiException("Missing the required parameter 'databaseName2' when calling changeDatabaseUserPassword(Async)");
        }

        // verify the required parameter 'userName2' is set
        if (userName2 == null) {
            throw new ApiException("Missing the required parameter 'userName2' when calling changeDatabaseUserPassword(Async)");
        }

        return changeDatabaseUserPasswordCall(databaseName, userName, databaseName2, userName2, updateUserPasswordRequest, _callback);

    }

    /**
     * Change password for mysql user
     * 
     * @param databaseName Name of the database. (required)
     * @param userName Name of the user. (required)
     * @param databaseName2 Automatically added (required)
     * @param userName2 Automatically added (required)
     * @param updateUserPasswordRequest Contains the new password. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void changeDatabaseUserPassword(String databaseName, String userName, String databaseName2, String userName2, UpdateUserPasswordRequest updateUserPasswordRequest) throws ApiException {
        changeDatabaseUserPasswordWithHttpInfo(databaseName, userName, databaseName2, userName2, updateUserPasswordRequest);
    }

    /**
     * Change password for mysql user
     * 
     * @param databaseName Name of the database. (required)
     * @param userName Name of the user. (required)
     * @param databaseName2 Automatically added (required)
     * @param userName2 Automatically added (required)
     * @param updateUserPasswordRequest Contains the new password. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> changeDatabaseUserPasswordWithHttpInfo(String databaseName, String userName, String databaseName2, String userName2, UpdateUserPasswordRequest updateUserPasswordRequest) throws ApiException {
        okhttp3.Call localVarCall = changeDatabaseUserPasswordValidateBeforeCall(databaseName, userName, databaseName2, userName2, updateUserPasswordRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Change password for mysql user (asynchronously)
     * 
     * @param databaseName Name of the database. (required)
     * @param userName Name of the user. (required)
     * @param databaseName2 Automatically added (required)
     * @param userName2 Automatically added (required)
     * @param updateUserPasswordRequest Contains the new password. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeDatabaseUserPasswordAsync(String databaseName, String userName, String databaseName2, String userName2, UpdateUserPasswordRequest updateUserPasswordRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = changeDatabaseUserPasswordValidateBeforeCall(databaseName, userName, databaseName2, userName2, updateUserPasswordRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for changeDatabaseUserStatus
     * @param databaseName Name of the database. (required)
     * @param userName Name of the user. (required)
     * @param databaseName2 Automatically added (required)
     * @param userName2 Automatically added (required)
     * @param updateUserStatusRequest Whether the user is enabled or not. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeDatabaseUserStatusCall(String databaseName, String userName, String databaseName2, String userName2, UpdateUserStatusRequest updateUserStatusRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateUserStatusRequest;

        // create path and map variables
        String localVarPath = "/mysqldatabases/{databaseName}/users/{userName}/status"
            .replace("{" + "databaseName" + "}", localVarApiClient.escapeString(databaseName2.toString()))
            .replace("{" + "userName" + "}", localVarApiClient.escapeString(userName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (databaseName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("database_name", databaseName));
        }

        if (userName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("user_name", userName));
        }

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
    private okhttp3.Call changeDatabaseUserStatusValidateBeforeCall(String databaseName, String userName, String databaseName2, String userName2, UpdateUserStatusRequest updateUserStatusRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'databaseName' is set
        if (databaseName == null) {
            throw new ApiException("Missing the required parameter 'databaseName' when calling changeDatabaseUserStatus(Async)");
        }

        // verify the required parameter 'userName' is set
        if (userName == null) {
            throw new ApiException("Missing the required parameter 'userName' when calling changeDatabaseUserStatus(Async)");
        }

        // verify the required parameter 'databaseName2' is set
        if (databaseName2 == null) {
            throw new ApiException("Missing the required parameter 'databaseName2' when calling changeDatabaseUserStatus(Async)");
        }

        // verify the required parameter 'userName2' is set
        if (userName2 == null) {
            throw new ApiException("Missing the required parameter 'userName2' when calling changeDatabaseUserStatus(Async)");
        }

        return changeDatabaseUserStatusCall(databaseName, userName, databaseName2, userName2, updateUserStatusRequest, _callback);

    }

    /**
     * Enable/disable mysql user
     * 
     * @param databaseName Name of the database. (required)
     * @param userName Name of the user. (required)
     * @param databaseName2 Automatically added (required)
     * @param userName2 Automatically added (required)
     * @param updateUserStatusRequest Whether the user is enabled or not. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void changeDatabaseUserStatus(String databaseName, String userName, String databaseName2, String userName2, UpdateUserStatusRequest updateUserStatusRequest) throws ApiException {
        changeDatabaseUserStatusWithHttpInfo(databaseName, userName, databaseName2, userName2, updateUserStatusRequest);
    }

    /**
     * Enable/disable mysql user
     * 
     * @param databaseName Name of the database. (required)
     * @param userName Name of the user. (required)
     * @param databaseName2 Automatically added (required)
     * @param userName2 Automatically added (required)
     * @param updateUserStatusRequest Whether the user is enabled or not. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> changeDatabaseUserStatusWithHttpInfo(String databaseName, String userName, String databaseName2, String userName2, UpdateUserStatusRequest updateUserStatusRequest) throws ApiException {
        okhttp3.Call localVarCall = changeDatabaseUserStatusValidateBeforeCall(databaseName, userName, databaseName2, userName2, updateUserStatusRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Enable/disable mysql user (asynchronously)
     * 
     * @param databaseName Name of the database. (required)
     * @param userName Name of the user. (required)
     * @param databaseName2 Automatically added (required)
     * @param userName2 Automatically added (required)
     * @param updateUserStatusRequest Whether the user is enabled or not. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeDatabaseUserStatusAsync(String databaseName, String userName, String databaseName2, String userName2, UpdateUserStatusRequest updateUserStatusRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = changeDatabaseUserStatusValidateBeforeCall(databaseName, userName, databaseName2, userName2, updateUserStatusRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for createMySqlDatabase
     * @param createMySqlDatabase  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createMySqlDatabaseCall(CreateMySqlDatabase createMySqlDatabase, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createMySqlDatabase;

        // create path and map variables
        String localVarPath = "/mysqldatabases";

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
    private okhttp3.Call createMySqlDatabaseValidateBeforeCall(CreateMySqlDatabase createMySqlDatabase, final ApiCallback _callback) throws ApiException {
        return createMySqlDatabaseCall(createMySqlDatabase, _callback);

    }

    /**
     * Create a new mysql database
     * 
     * @param createMySqlDatabase  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void createMySqlDatabase(CreateMySqlDatabase createMySqlDatabase) throws ApiException {
        createMySqlDatabaseWithHttpInfo(createMySqlDatabase);
    }

    /**
     * Create a new mysql database
     * 
     * @param createMySqlDatabase  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> createMySqlDatabaseWithHttpInfo(CreateMySqlDatabase createMySqlDatabase) throws ApiException {
        okhttp3.Call localVarCall = createMySqlDatabaseValidateBeforeCall(createMySqlDatabase, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Create a new mysql database (asynchronously)
     * 
     * @param createMySqlDatabase  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createMySqlDatabaseAsync(CreateMySqlDatabase createMySqlDatabase, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = createMySqlDatabaseValidateBeforeCall(createMySqlDatabase, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for createMySqlUser
     * @param databaseName Name of the database. (required)
     * @param databaseName2 Automatically added (required)
     * @param createMySqlUser  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createMySqlUserCall(String databaseName, String databaseName2, CreateMySqlUser createMySqlUser, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createMySqlUser;

        // create path and map variables
        String localVarPath = "/mysqldatabases/{databaseName}/users"
            .replace("{" + "databaseName" + "}", localVarApiClient.escapeString(databaseName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (databaseName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("database_name", databaseName));
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
    private okhttp3.Call createMySqlUserValidateBeforeCall(String databaseName, String databaseName2, CreateMySqlUser createMySqlUser, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'databaseName' is set
        if (databaseName == null) {
            throw new ApiException("Missing the required parameter 'databaseName' when calling createMySqlUser(Async)");
        }

        // verify the required parameter 'databaseName2' is set
        if (databaseName2 == null) {
            throw new ApiException("Missing the required parameter 'databaseName2' when calling createMySqlUser(Async)");
        }

        return createMySqlUserCall(databaseName, databaseName2, createMySqlUser, _callback);

    }

    /**
     * Create a new mysql user
     * The creation of a new mysql user will result in a user with read_only rights.
     * @param databaseName Name of the database. (required)
     * @param databaseName2 Automatically added (required)
     * @param createMySqlUser  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void createMySqlUser(String databaseName, String databaseName2, CreateMySqlUser createMySqlUser) throws ApiException {
        createMySqlUserWithHttpInfo(databaseName, databaseName2, createMySqlUser);
    }

    /**
     * Create a new mysql user
     * The creation of a new mysql user will result in a user with read_only rights.
     * @param databaseName Name of the database. (required)
     * @param databaseName2 Automatically added (required)
     * @param createMySqlUser  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> createMySqlUserWithHttpInfo(String databaseName, String databaseName2, CreateMySqlUser createMySqlUser) throws ApiException {
        okhttp3.Call localVarCall = createMySqlUserValidateBeforeCall(databaseName, databaseName2, createMySqlUser, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Create a new mysql user (asynchronously)
     * The creation of a new mysql user will result in a user with read_only rights.
     * @param databaseName Name of the database. (required)
     * @param databaseName2 Automatically added (required)
     * @param createMySqlUser  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createMySqlUserAsync(String databaseName, String databaseName2, CreateMySqlUser createMySqlUser, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = createMySqlUserValidateBeforeCall(databaseName, databaseName2, createMySqlUser, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDatabase
     * @param databaseName Name of the database. (required)
     * @param databaseName2 Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabaseCall(String databaseName, String databaseName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/mysqldatabases/{databaseName}"
            .replace("{" + "databaseName" + "}", localVarApiClient.escapeString(databaseName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (databaseName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("database_name", databaseName));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteDatabaseValidateBeforeCall(String databaseName, String databaseName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'databaseName' is set
        if (databaseName == null) {
            throw new ApiException("Missing the required parameter 'databaseName' when calling deleteDatabase(Async)");
        }

        // verify the required parameter 'databaseName2' is set
        if (databaseName2 == null) {
            throw new ApiException("Missing the required parameter 'databaseName2' when calling deleteDatabase(Async)");
        }

        return deleteDatabaseCall(databaseName, databaseName2, _callback);

    }

    /**
     * Delete a mysql database
     * 
     * @param databaseName Name of the database. (required)
     * @param databaseName2 Automatically added (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void deleteDatabase(String databaseName, String databaseName2) throws ApiException {
        deleteDatabaseWithHttpInfo(databaseName, databaseName2);
    }

    /**
     * Delete a mysql database
     * 
     * @param databaseName Name of the database. (required)
     * @param databaseName2 Automatically added (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteDatabaseWithHttpInfo(String databaseName, String databaseName2) throws ApiException {
        okhttp3.Call localVarCall = deleteDatabaseValidateBeforeCall(databaseName, databaseName2, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a mysql database (asynchronously)
     * 
     * @param databaseName Name of the database. (required)
     * @param databaseName2 Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabaseAsync(String databaseName, String databaseName2, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDatabaseValidateBeforeCall(databaseName, databaseName2, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteDatabaseUser
     * @param databaseName Name of the database. (required)
     * @param userName Name of the user. (required)
     * @param databaseName2 Automatically added (required)
     * @param userName2 Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabaseUserCall(String databaseName, String userName, String databaseName2, String userName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/mysqldatabases/{databaseName}/users/{userName}"
            .replace("{" + "databaseName" + "}", localVarApiClient.escapeString(databaseName2.toString()))
            .replace("{" + "userName" + "}", localVarApiClient.escapeString(userName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (databaseName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("database_name", databaseName));
        }

        if (userName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("user_name", userName));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteDatabaseUserValidateBeforeCall(String databaseName, String userName, String databaseName2, String userName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'databaseName' is set
        if (databaseName == null) {
            throw new ApiException("Missing the required parameter 'databaseName' when calling deleteDatabaseUser(Async)");
        }

        // verify the required parameter 'userName' is set
        if (userName == null) {
            throw new ApiException("Missing the required parameter 'userName' when calling deleteDatabaseUser(Async)");
        }

        // verify the required parameter 'databaseName2' is set
        if (databaseName2 == null) {
            throw new ApiException("Missing the required parameter 'databaseName2' when calling deleteDatabaseUser(Async)");
        }

        // verify the required parameter 'userName2' is set
        if (userName2 == null) {
            throw new ApiException("Missing the required parameter 'userName2' when calling deleteDatabaseUser(Async)");
        }

        return deleteDatabaseUserCall(databaseName, userName, databaseName2, userName2, _callback);

    }

    /**
     * Delete a mysql user
     * The deletion of a mysql user is allowed for users with read_only rights.
     * @param databaseName Name of the database. (required)
     * @param userName Name of the user. (required)
     * @param databaseName2 Automatically added (required)
     * @param userName2 Automatically added (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void deleteDatabaseUser(String databaseName, String userName, String databaseName2, String userName2) throws ApiException {
        deleteDatabaseUserWithHttpInfo(databaseName, userName, databaseName2, userName2);
    }

    /**
     * Delete a mysql user
     * The deletion of a mysql user is allowed for users with read_only rights.
     * @param databaseName Name of the database. (required)
     * @param userName Name of the user. (required)
     * @param databaseName2 Automatically added (required)
     * @param userName2 Automatically added (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteDatabaseUserWithHttpInfo(String databaseName, String userName, String databaseName2, String userName2) throws ApiException {
        okhttp3.Call localVarCall = deleteDatabaseUserValidateBeforeCall(databaseName, userName, databaseName2, userName2, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a mysql user (asynchronously)
     * The deletion of a mysql user is allowed for users with read_only rights.
     * @param databaseName Name of the database. (required)
     * @param userName Name of the user. (required)
     * @param databaseName2 Automatically added (required)
     * @param userName2 Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteDatabaseUserAsync(String databaseName, String userName, String databaseName2, String userName2, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteDatabaseUserValidateBeforeCall(databaseName, userName, databaseName2, userName2, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getDatabaseUsers
     * @param databaseName Name of the database. (required)
     * @param databaseName2 Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabaseUsersCall(String databaseName, String databaseName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/mysqldatabases/{databaseName}/users"
            .replace("{" + "databaseName" + "}", localVarApiClient.escapeString(databaseName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (databaseName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("database_name", databaseName));
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
    private okhttp3.Call getDatabaseUsersValidateBeforeCall(String databaseName, String databaseName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'databaseName' is set
        if (databaseName == null) {
            throw new ApiException("Missing the required parameter 'databaseName' when calling getDatabaseUsers(Async)");
        }

        // verify the required parameter 'databaseName2' is set
        if (databaseName2 == null) {
            throw new ApiException("Missing the required parameter 'databaseName2' when calling getDatabaseUsers(Async)");
        }

        return getDatabaseUsersCall(databaseName, databaseName2, _callback);

    }

    /**
     * Overview of mysql users
     * 
     * @param databaseName Name of the database. (required)
     * @param databaseName2 Automatically added (required)
     * @return List&lt;MySqlUser&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public List<MySqlUser> getDatabaseUsers(String databaseName, String databaseName2) throws ApiException {
        ApiResponse<List<MySqlUser>> localVarResp = getDatabaseUsersWithHttpInfo(databaseName, databaseName2);
        return localVarResp.getData();
    }

    /**
     * Overview of mysql users
     * 
     * @param databaseName Name of the database. (required)
     * @param databaseName2 Automatically added (required)
     * @return ApiResponse&lt;List&lt;MySqlUser&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<MySqlUser>> getDatabaseUsersWithHttpInfo(String databaseName, String databaseName2) throws ApiException {
        okhttp3.Call localVarCall = getDatabaseUsersValidateBeforeCall(databaseName, databaseName2, null);
        Type localVarReturnType = new TypeToken<List<MySqlUser>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Overview of mysql users (asynchronously)
     * 
     * @param databaseName Name of the database. (required)
     * @param databaseName2 Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getDatabaseUsersAsync(String databaseName, String databaseName2, final ApiCallback<List<MySqlUser>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getDatabaseUsersValidateBeforeCall(databaseName, databaseName2, _callback);
        Type localVarReturnType = new TypeToken<List<MySqlUser>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getMySqlDatabase
     * @param databaseName  (required)
     * @param databaseName2 Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMySqlDatabaseCall(String databaseName, String databaseName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/mysqldatabases/{databaseName}"
            .replace("{" + "databaseName" + "}", localVarApiClient.escapeString(databaseName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (databaseName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("database_name", databaseName));
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
    private okhttp3.Call getMySqlDatabaseValidateBeforeCall(String databaseName, String databaseName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'databaseName' is set
        if (databaseName == null) {
            throw new ApiException("Missing the required parameter 'databaseName' when calling getMySqlDatabase(Async)");
        }

        // verify the required parameter 'databaseName2' is set
        if (databaseName2 == null) {
            throw new ApiException("Missing the required parameter 'databaseName2' when calling getMySqlDatabase(Async)");
        }

        return getMySqlDatabaseCall(databaseName, databaseName2, _callback);

    }

    /**
     * Get a specific database
     * 
     * @param databaseName  (required)
     * @param databaseName2 Automatically added (required)
     * @return MySqlDatabase
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public MySqlDatabase getMySqlDatabase(String databaseName, String databaseName2) throws ApiException {
        ApiResponse<MySqlDatabase> localVarResp = getMySqlDatabaseWithHttpInfo(databaseName, databaseName2);
        return localVarResp.getData();
    }

    /**
     * Get a specific database
     * 
     * @param databaseName  (required)
     * @param databaseName2 Automatically added (required)
     * @return ApiResponse&lt;MySqlDatabase&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<MySqlDatabase> getMySqlDatabaseWithHttpInfo(String databaseName, String databaseName2) throws ApiException {
        okhttp3.Call localVarCall = getMySqlDatabaseValidateBeforeCall(databaseName, databaseName2, null);
        Type localVarReturnType = new TypeToken<MySqlDatabase>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a specific database (asynchronously)
     * 
     * @param databaseName  (required)
     * @param databaseName2 Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMySqlDatabaseAsync(String databaseName, String databaseName2, final ApiCallback<MySqlDatabase> _callback) throws ApiException {

        okhttp3.Call localVarCall = getMySqlDatabaseValidateBeforeCall(databaseName, databaseName2, _callback);
        Type localVarReturnType = new TypeToken<MySqlDatabase>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getMySqlDatabases
     * @param skip The number of items to skip in the resultset. (optional)
     * @param take The number of items to return in the resultset. The returned count can be equal or less than this number. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getMySqlDatabasesCall(Integer skip, Integer take, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/mysqldatabases";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (skip != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("skip", skip));
        }

        if (take != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("take", take));
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
    private okhttp3.Call getMySqlDatabasesValidateBeforeCall(Integer skip, Integer take, final ApiCallback _callback) throws ApiException {
        return getMySqlDatabasesCall(skip, take, _callback);

    }

    /**
     * Overview of mysql databases
     * 
     * @param skip The number of items to skip in the resultset. (optional)
     * @param take The number of items to return in the resultset. The returned count can be equal or less than this number. (optional)
     * @return List&lt;MySqlDatabase&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  </td></tr>
     </table>
     */
    public List<MySqlDatabase> getMySqlDatabases(Integer skip, Integer take) throws ApiException {
        ApiResponse<List<MySqlDatabase>> localVarResp = getMySqlDatabasesWithHttpInfo(skip, take);
        return localVarResp.getData();
    }

    /**
     * Overview of mysql databases
     * 
     * @param skip The number of items to skip in the resultset. (optional)
     * @param take The number of items to return in the resultset. The returned count can be equal or less than this number. (optional)
     * @return ApiResponse&lt;List&lt;MySqlDatabase&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  </td></tr>
     </table>
     */
    public ApiResponse<List<MySqlDatabase>> getMySqlDatabasesWithHttpInfo(Integer skip, Integer take) throws ApiException {
        okhttp3.Call localVarCall = getMySqlDatabasesValidateBeforeCall(skip, take, null);
        Type localVarReturnType = new TypeToken<List<MySqlDatabase>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Overview of mysql databases (asynchronously)
     * 
     * @param skip The number of items to skip in the resultset. (optional)
     * @param take The number of items to return in the resultset. The returned count can be equal or less than this number. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getMySqlDatabasesAsync(Integer skip, Integer take, final ApiCallback<List<MySqlDatabase>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getMySqlDatabasesValidateBeforeCall(skip, take, _callback);
        Type localVarReturnType = new TypeToken<List<MySqlDatabase>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
