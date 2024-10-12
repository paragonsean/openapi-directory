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


import org.openapitools.client.model.AddHostHeaderRequest;
import org.openapitools.client.model.AddSshKeyRequest;
import org.openapitools.client.model.AddSubsiteRequest;
import org.openapitools.client.model.AutoRedirectConfig;
import org.openapitools.client.model.FtpConfiguration;
import org.openapitools.client.model.GzipConfig;
import org.openapitools.client.model.Http2Configuration;
import org.openapitools.client.model.LetsEncryptConfig;
import org.openapitools.client.model.LinuxHosting;
import org.openapitools.client.model.LinuxHostingDetail;
import org.openapitools.client.model.PhpVersion;
import org.openapitools.client.model.ScheduledTask;
import org.openapitools.client.model.SshConfiguration;
import org.openapitools.client.model.SshKey;
import org.openapitools.client.model.UpdatePhpAPcuRequest;
import org.openapitools.client.model.UpdatePhpMemoryLimitRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LinuxHostingsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public LinuxHostingsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public LinuxHostingsApi(ApiClient apiClient) {
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
     * Build call for addScheduledTasks
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTask  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call addScheduledTasksCall(String domainName, String domainName2, ScheduledTask scheduledTask, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = scheduledTask;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/scheduledtasks"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call addScheduledTasksValidateBeforeCall(String domainName, String domainName2, ScheduledTask scheduledTask, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling addScheduledTasks(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling addScheduledTasks(Async)");
        }

        return addScheduledTasksCall(domainName, domainName2, scheduledTask, _callback);

    }

    /**
     * Add a scheduled task
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTask  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public void addScheduledTasks(String domainName, String domainName2, ScheduledTask scheduledTask) throws ApiException {
        addScheduledTasksWithHttpInfo(domainName, domainName2, scheduledTask);
    }

    /**
     * Add a scheduled task
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTask  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Void> addScheduledTasksWithHttpInfo(String domainName, String domainName2, ScheduledTask scheduledTask) throws ApiException {
        okhttp3.Call localVarCall = addScheduledTasksValidateBeforeCall(domainName, domainName2, scheduledTask, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Add a scheduled task (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTask  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call addScheduledTasksAsync(String domainName, String domainName2, ScheduledTask scheduledTask, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = addScheduledTasksValidateBeforeCall(domainName, domainName2, scheduledTask, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for addSshKey
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param addSshKeyRequest SSH key public key. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call addSshKeyCall(String domainName, String domainName2, AddSshKeyRequest addSshKeyRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addSshKeyRequest;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/ssh/keys"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call addSshKeyValidateBeforeCall(String domainName, String domainName2, AddSshKeyRequest addSshKeyRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling addSshKey(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling addSshKey(Async)");
        }

        return addSshKeyCall(domainName, domainName2, addSshKeyRequest, _callback);

    }

    /**
     * Add a SSH key
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param addSshKeyRequest SSH key public key. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public void addSshKey(String domainName, String domainName2, AddSshKeyRequest addSshKeyRequest) throws ApiException {
        addSshKeyWithHttpInfo(domainName, domainName2, addSshKeyRequest);
    }

    /**
     * Add a SSH key
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param addSshKeyRequest SSH key public key. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Void> addSshKeyWithHttpInfo(String domainName, String domainName2, AddSshKeyRequest addSshKeyRequest) throws ApiException {
        okhttp3.Call localVarCall = addSshKeyValidateBeforeCall(domainName, domainName2, addSshKeyRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Add a SSH key (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param addSshKeyRequest SSH key public key. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call addSshKeyAsync(String domainName, String domainName2, AddSshKeyRequest addSshKeyRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = addSshKeyValidateBeforeCall(domainName, domainName2, addSshKeyRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for changeApcu
     * @param domainName Linux hosting domain name (required)
     * @param domainName2 Automatically added (required)
     * @param updatePhpAPcuRequest Php APcu config (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeApcuCall(String domainName, String domainName2, UpdatePhpAPcuRequest updatePhpAPcuRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updatePhpAPcuRequest;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/phpsettings/apcu"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
    private okhttp3.Call changeApcuValidateBeforeCall(String domainName, String domainName2, UpdatePhpAPcuRequest updatePhpAPcuRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling changeApcu(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling changeApcu(Async)");
        }

        return changeApcuCall(domainName, domainName2, updatePhpAPcuRequest, _callback);

    }

    /**
     * Configure PHP APCu setting
     * 
     * @param domainName Linux hosting domain name (required)
     * @param domainName2 Automatically added (required)
     * @param updatePhpAPcuRequest Php APcu config (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void changeApcu(String domainName, String domainName2, UpdatePhpAPcuRequest updatePhpAPcuRequest) throws ApiException {
        changeApcuWithHttpInfo(domainName, domainName2, updatePhpAPcuRequest);
    }

    /**
     * Configure PHP APCu setting
     * 
     * @param domainName Linux hosting domain name (required)
     * @param domainName2 Automatically added (required)
     * @param updatePhpAPcuRequest Php APcu config (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> changeApcuWithHttpInfo(String domainName, String domainName2, UpdatePhpAPcuRequest updatePhpAPcuRequest) throws ApiException {
        okhttp3.Call localVarCall = changeApcuValidateBeforeCall(domainName, domainName2, updatePhpAPcuRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure PHP APCu setting (asynchronously)
     * 
     * @param domainName Linux hosting domain name (required)
     * @param domainName2 Automatically added (required)
     * @param updatePhpAPcuRequest Php APcu config (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeApcuAsync(String domainName, String domainName2, UpdatePhpAPcuRequest updatePhpAPcuRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = changeApcuValidateBeforeCall(domainName, domainName2, updatePhpAPcuRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for changeAutoRedirect
     * @param domainName Linux hosting domain name. (required)
     * @param hostname Specific hostname. (required)
     * @param domainName2 Automatically added (required)
     * @param autoRedirectConfig Auto redirect config. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeAutoRedirectCall(String domainName, String hostname, String domainName2, AutoRedirectConfig autoRedirectConfig, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = autoRedirectConfig;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/sslsettings/{hostname}/autoredirect"
            .replace("{" + "hostname" + "}", localVarApiClient.escapeString(hostname.toString()))
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
    private okhttp3.Call changeAutoRedirectValidateBeforeCall(String domainName, String hostname, String domainName2, AutoRedirectConfig autoRedirectConfig, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling changeAutoRedirect(Async)");
        }

        // verify the required parameter 'hostname' is set
        if (hostname == null) {
            throw new ApiException("Missing the required parameter 'hostname' when calling changeAutoRedirect(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling changeAutoRedirect(Async)");
        }

        return changeAutoRedirectCall(domainName, hostname, domainName2, autoRedirectConfig, _callback);

    }

    /**
     * Configure auto redirect
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param hostname Specific hostname. (required)
     * @param domainName2 Automatically added (required)
     * @param autoRedirectConfig Auto redirect config. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void changeAutoRedirect(String domainName, String hostname, String domainName2, AutoRedirectConfig autoRedirectConfig) throws ApiException {
        changeAutoRedirectWithHttpInfo(domainName, hostname, domainName2, autoRedirectConfig);
    }

    /**
     * Configure auto redirect
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param hostname Specific hostname. (required)
     * @param domainName2 Automatically added (required)
     * @param autoRedirectConfig Auto redirect config. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> changeAutoRedirectWithHttpInfo(String domainName, String hostname, String domainName2, AutoRedirectConfig autoRedirectConfig) throws ApiException {
        okhttp3.Call localVarCall = changeAutoRedirectValidateBeforeCall(domainName, hostname, domainName2, autoRedirectConfig, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure auto redirect (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param hostname Specific hostname. (required)
     * @param domainName2 Automatically added (required)
     * @param autoRedirectConfig Auto redirect config. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeAutoRedirectAsync(String domainName, String hostname, String domainName2, AutoRedirectConfig autoRedirectConfig, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = changeAutoRedirectValidateBeforeCall(domainName, hostname, domainName2, autoRedirectConfig, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for changeGzipCompression
     * @param domainName Linux hosting domain name (required)
     * @param domainName2 Automatically added (required)
     * @param gzipConfig Whether GZIP compression is enabled or not. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeGzipCompressionCall(String domainName, String domainName2, GzipConfig gzipConfig, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = gzipConfig;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/settings/gzipcompression"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
    private okhttp3.Call changeGzipCompressionValidateBeforeCall(String domainName, String domainName2, GzipConfig gzipConfig, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling changeGzipCompression(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling changeGzipCompression(Async)");
        }

        return changeGzipCompressionCall(domainName, domainName2, gzipConfig, _callback);

    }

    /**
     * Enable/disable GZIP compression
     * 
     * @param domainName Linux hosting domain name (required)
     * @param domainName2 Automatically added (required)
     * @param gzipConfig Whether GZIP compression is enabled or not. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void changeGzipCompression(String domainName, String domainName2, GzipConfig gzipConfig) throws ApiException {
        changeGzipCompressionWithHttpInfo(domainName, domainName2, gzipConfig);
    }

    /**
     * Enable/disable GZIP compression
     * 
     * @param domainName Linux hosting domain name (required)
     * @param domainName2 Automatically added (required)
     * @param gzipConfig Whether GZIP compression is enabled or not. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> changeGzipCompressionWithHttpInfo(String domainName, String domainName2, GzipConfig gzipConfig) throws ApiException {
        okhttp3.Call localVarCall = changeGzipCompressionValidateBeforeCall(domainName, domainName2, gzipConfig, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Enable/disable GZIP compression (asynchronously)
     * 
     * @param domainName Linux hosting domain name (required)
     * @param domainName2 Automatically added (required)
     * @param gzipConfig Whether GZIP compression is enabled or not. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeGzipCompressionAsync(String domainName, String domainName2, GzipConfig gzipConfig, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = changeGzipCompressionValidateBeforeCall(domainName, domainName2, gzipConfig, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for changeLetsEncrypt
     * @param domainName Linux hosting domain name. (required)
     * @param hostname Specific hostname. (required)
     * @param domainName2 Automatically added (required)
     * @param letsEncryptConfig Let&#39;s encrypt config. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeLetsEncryptCall(String domainName, String hostname, String domainName2, LetsEncryptConfig letsEncryptConfig, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = letsEncryptConfig;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/sslsettings/{hostname}/letsencrypt"
            .replace("{" + "hostname" + "}", localVarApiClient.escapeString(hostname.toString()))
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
    private okhttp3.Call changeLetsEncryptValidateBeforeCall(String domainName, String hostname, String domainName2, LetsEncryptConfig letsEncryptConfig, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling changeLetsEncrypt(Async)");
        }

        // verify the required parameter 'hostname' is set
        if (hostname == null) {
            throw new ApiException("Missing the required parameter 'hostname' when calling changeLetsEncrypt(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling changeLetsEncrypt(Async)");
        }

        return changeLetsEncryptCall(domainName, hostname, domainName2, letsEncryptConfig, _callback);

    }

    /**
     * Configure let&#39;s encrypt
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param hostname Specific hostname. (required)
     * @param domainName2 Automatically added (required)
     * @param letsEncryptConfig Let&#39;s encrypt config. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void changeLetsEncrypt(String domainName, String hostname, String domainName2, LetsEncryptConfig letsEncryptConfig) throws ApiException {
        changeLetsEncryptWithHttpInfo(domainName, hostname, domainName2, letsEncryptConfig);
    }

    /**
     * Configure let&#39;s encrypt
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param hostname Specific hostname. (required)
     * @param domainName2 Automatically added (required)
     * @param letsEncryptConfig Let&#39;s encrypt config. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> changeLetsEncryptWithHttpInfo(String domainName, String hostname, String domainName2, LetsEncryptConfig letsEncryptConfig) throws ApiException {
        okhttp3.Call localVarCall = changeLetsEncryptValidateBeforeCall(domainName, hostname, domainName2, letsEncryptConfig, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure let&#39;s encrypt (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param hostname Specific hostname. (required)
     * @param domainName2 Automatically added (required)
     * @param letsEncryptConfig Let&#39;s encrypt config. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeLetsEncryptAsync(String domainName, String hostname, String domainName2, LetsEncryptConfig letsEncryptConfig, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = changeLetsEncryptValidateBeforeCall(domainName, hostname, domainName2, letsEncryptConfig, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for changePhpMemoryLimit
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param updatePhpMemoryLimitRequest Memory limit config (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changePhpMemoryLimitCall(String domainName, String domainName2, UpdatePhpMemoryLimitRequest updatePhpMemoryLimitRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updatePhpMemoryLimitRequest;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/phpsettings/memorylimit"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
    private okhttp3.Call changePhpMemoryLimitValidateBeforeCall(String domainName, String domainName2, UpdatePhpMemoryLimitRequest updatePhpMemoryLimitRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling changePhpMemoryLimit(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling changePhpMemoryLimit(Async)");
        }

        return changePhpMemoryLimitCall(domainName, domainName2, updatePhpMemoryLimitRequest, _callback);

    }

    /**
     * Configure PHP memory limit
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param updatePhpMemoryLimitRequest Memory limit config (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void changePhpMemoryLimit(String domainName, String domainName2, UpdatePhpMemoryLimitRequest updatePhpMemoryLimitRequest) throws ApiException {
        changePhpMemoryLimitWithHttpInfo(domainName, domainName2, updatePhpMemoryLimitRequest);
    }

    /**
     * Configure PHP memory limit
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param updatePhpMemoryLimitRequest Memory limit config (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> changePhpMemoryLimitWithHttpInfo(String domainName, String domainName2, UpdatePhpMemoryLimitRequest updatePhpMemoryLimitRequest) throws ApiException {
        okhttp3.Call localVarCall = changePhpMemoryLimitValidateBeforeCall(domainName, domainName2, updatePhpMemoryLimitRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure PHP memory limit (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param updatePhpMemoryLimitRequest Memory limit config (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changePhpMemoryLimitAsync(String domainName, String domainName2, UpdatePhpMemoryLimitRequest updatePhpMemoryLimitRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = changePhpMemoryLimitValidateBeforeCall(domainName, domainName2, updatePhpMemoryLimitRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for changePhpVersion
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param phpVersion The new PHP version. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changePhpVersionCall(String domainName, String domainName2, PhpVersion phpVersion, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = phpVersion;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/phpsettings/version"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
    private okhttp3.Call changePhpVersionValidateBeforeCall(String domainName, String domainName2, PhpVersion phpVersion, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling changePhpVersion(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling changePhpVersion(Async)");
        }

        return changePhpVersionCall(domainName, domainName2, phpVersion, _callback);

    }

    /**
     * Change the Linux hosting PHP version.
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param phpVersion The new PHP version. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void changePhpVersion(String domainName, String domainName2, PhpVersion phpVersion) throws ApiException {
        changePhpVersionWithHttpInfo(domainName, domainName2, phpVersion);
    }

    /**
     * Change the Linux hosting PHP version.
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param phpVersion The new PHP version. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> changePhpVersionWithHttpInfo(String domainName, String domainName2, PhpVersion phpVersion) throws ApiException {
        okhttp3.Call localVarCall = changePhpVersionValidateBeforeCall(domainName, domainName2, phpVersion, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Change the Linux hosting PHP version. (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param phpVersion The new PHP version. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changePhpVersionAsync(String domainName, String domainName2, PhpVersion phpVersion, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = changePhpVersionValidateBeforeCall(domainName, domainName2, phpVersion, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for configureFtp
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param ftpConfiguration  (optional)
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
    public okhttp3.Call configureFtpCall(String domainName, String domainName2, FtpConfiguration ftpConfiguration, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = ftpConfiguration;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/ftp/configuration"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
    private okhttp3.Call configureFtpValidateBeforeCall(String domainName, String domainName2, FtpConfiguration ftpConfiguration, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling configureFtp(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling configureFtp(Async)");
        }

        return configureFtpCall(domainName, domainName2, ftpConfiguration, _callback);

    }

    /**
     * Configure FTP
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param ftpConfiguration  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void configureFtp(String domainName, String domainName2, FtpConfiguration ftpConfiguration) throws ApiException {
        configureFtpWithHttpInfo(domainName, domainName2, ftpConfiguration);
    }

    /**
     * Configure FTP
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param ftpConfiguration  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> configureFtpWithHttpInfo(String domainName, String domainName2, FtpConfiguration ftpConfiguration) throws ApiException {
        okhttp3.Call localVarCall = configureFtpValidateBeforeCall(domainName, domainName2, ftpConfiguration, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure FTP (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param ftpConfiguration  (optional)
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
    public okhttp3.Call configureFtpAsync(String domainName, String domainName2, FtpConfiguration ftpConfiguration, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = configureFtpValidateBeforeCall(domainName, domainName2, ftpConfiguration, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for configureHttp2
     * @param domainName Linux hosting domain name. (required)
     * @param siteName Site name where HTTP/2 should be configured.&lt;br /&gt;  For HTTP/2 to work correctly, the site must have ssl enabled. (required)
     * @param domainName2 Automatically added (required)
     * @param siteName2 Automatically added (required)
     * @param http2Configuration  (optional)
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
    public okhttp3.Call configureHttp2Call(String domainName, String siteName, String domainName2, String siteName2, Http2Configuration http2Configuration, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = http2Configuration;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/sites/{siteName}/http2/configuration"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()))
            .replace("{" + "siteName" + "}", localVarApiClient.escapeString(siteName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
        }

        if (siteName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("site_name", siteName));
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
    private okhttp3.Call configureHttp2ValidateBeforeCall(String domainName, String siteName, String domainName2, String siteName2, Http2Configuration http2Configuration, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling configureHttp2(Async)");
        }

        // verify the required parameter 'siteName' is set
        if (siteName == null) {
            throw new ApiException("Missing the required parameter 'siteName' when calling configureHttp2(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling configureHttp2(Async)");
        }

        // verify the required parameter 'siteName2' is set
        if (siteName2 == null) {
            throw new ApiException("Missing the required parameter 'siteName2' when calling configureHttp2(Async)");
        }

        return configureHttp2Call(domainName, siteName, domainName2, siteName2, http2Configuration, _callback);

    }

    /**
     * Configure HTTP/2
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param siteName Site name where HTTP/2 should be configured.&lt;br /&gt;  For HTTP/2 to work correctly, the site must have ssl enabled. (required)
     * @param domainName2 Automatically added (required)
     * @param siteName2 Automatically added (required)
     * @param http2Configuration  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void configureHttp2(String domainName, String siteName, String domainName2, String siteName2, Http2Configuration http2Configuration) throws ApiException {
        configureHttp2WithHttpInfo(domainName, siteName, domainName2, siteName2, http2Configuration);
    }

    /**
     * Configure HTTP/2
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param siteName Site name where HTTP/2 should be configured.&lt;br /&gt;  For HTTP/2 to work correctly, the site must have ssl enabled. (required)
     * @param domainName2 Automatically added (required)
     * @param siteName2 Automatically added (required)
     * @param http2Configuration  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> configureHttp2WithHttpInfo(String domainName, String siteName, String domainName2, String siteName2, Http2Configuration http2Configuration) throws ApiException {
        okhttp3.Call localVarCall = configureHttp2ValidateBeforeCall(domainName, siteName, domainName2, siteName2, http2Configuration, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure HTTP/2 (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param siteName Site name where HTTP/2 should be configured.&lt;br /&gt;  For HTTP/2 to work correctly, the site must have ssl enabled. (required)
     * @param domainName2 Automatically added (required)
     * @param siteName2 Automatically added (required)
     * @param http2Configuration  (optional)
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
    public okhttp3.Call configureHttp2Async(String domainName, String siteName, String domainName2, String siteName2, Http2Configuration http2Configuration, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = configureHttp2ValidateBeforeCall(domainName, siteName, domainName2, siteName2, http2Configuration, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for configureScheduledTask
     * @param domainName Linux hosting domain name. (required)
     * @param scheduledTaskId Id of the scheduled task. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTaskId2 Automatically added (required)
     * @param scheduledTask  (optional)
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
    public okhttp3.Call configureScheduledTaskCall(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2, ScheduledTask scheduledTask, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = scheduledTask;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId}"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()))
            .replace("{" + "scheduledTaskId" + "}", localVarApiClient.escapeString(scheduledTaskId2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
        }

        if (scheduledTaskId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("scheduled_task_id", scheduledTaskId));
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
    private okhttp3.Call configureScheduledTaskValidateBeforeCall(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2, ScheduledTask scheduledTask, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling configureScheduledTask(Async)");
        }

        // verify the required parameter 'scheduledTaskId' is set
        if (scheduledTaskId == null) {
            throw new ApiException("Missing the required parameter 'scheduledTaskId' when calling configureScheduledTask(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling configureScheduledTask(Async)");
        }

        // verify the required parameter 'scheduledTaskId2' is set
        if (scheduledTaskId2 == null) {
            throw new ApiException("Missing the required parameter 'scheduledTaskId2' when calling configureScheduledTask(Async)");
        }

        return configureScheduledTaskCall(domainName, scheduledTaskId, domainName2, scheduledTaskId2, scheduledTask, _callback);

    }

    /**
     * Configure a scheduled task
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param scheduledTaskId Id of the scheduled task. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTaskId2 Automatically added (required)
     * @param scheduledTask  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void configureScheduledTask(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2, ScheduledTask scheduledTask) throws ApiException {
        configureScheduledTaskWithHttpInfo(domainName, scheduledTaskId, domainName2, scheduledTaskId2, scheduledTask);
    }

    /**
     * Configure a scheduled task
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param scheduledTaskId Id of the scheduled task. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTaskId2 Automatically added (required)
     * @param scheduledTask  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> configureScheduledTaskWithHttpInfo(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2, ScheduledTask scheduledTask) throws ApiException {
        okhttp3.Call localVarCall = configureScheduledTaskValidateBeforeCall(domainName, scheduledTaskId, domainName2, scheduledTaskId2, scheduledTask, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure a scheduled task (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param scheduledTaskId Id of the scheduled task. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTaskId2 Automatically added (required)
     * @param scheduledTask  (optional)
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
    public okhttp3.Call configureScheduledTaskAsync(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2, ScheduledTask scheduledTask, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = configureScheduledTaskValidateBeforeCall(domainName, scheduledTaskId, domainName2, scheduledTaskId2, scheduledTask, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for configureSsh
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param sshConfiguration  (optional)
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
    public okhttp3.Call configureSshCall(String domainName, String domainName2, SshConfiguration sshConfiguration, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = sshConfiguration;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/ssh/configuration"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
    private okhttp3.Call configureSshValidateBeforeCall(String domainName, String domainName2, SshConfiguration sshConfiguration, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling configureSsh(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling configureSsh(Async)");
        }

        return configureSshCall(domainName, domainName2, sshConfiguration, _callback);

    }

    /**
     * Configure SSH
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param sshConfiguration  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void configureSsh(String domainName, String domainName2, SshConfiguration sshConfiguration) throws ApiException {
        configureSshWithHttpInfo(domainName, domainName2, sshConfiguration);
    }

    /**
     * Configure SSH
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param sshConfiguration  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> configureSshWithHttpInfo(String domainName, String domainName2, SshConfiguration sshConfiguration) throws ApiException {
        okhttp3.Call localVarCall = configureSshValidateBeforeCall(domainName, domainName2, sshConfiguration, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure SSH (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param sshConfiguration  (optional)
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
    public okhttp3.Call configureSshAsync(String domainName, String domainName2, SshConfiguration sshConfiguration, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = configureSshValidateBeforeCall(domainName, domainName2, sshConfiguration, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for createHostHeader
     * @param domainName Linux hosting domain name. (required)
     * @param siteName Name of the site on the linux hosting. (required)
     * @param domainName2 Automatically added (required)
     * @param siteName2 Automatically added (required)
     * @param addHostHeaderRequest Add host header request (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call createHostHeaderCall(String domainName, String siteName, String domainName2, String siteName2, AddHostHeaderRequest addHostHeaderRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addHostHeaderRequest;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/sites/{siteName}/hostheaders"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()))
            .replace("{" + "siteName" + "}", localVarApiClient.escapeString(siteName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
        }

        if (siteName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("site_name", siteName));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createHostHeaderValidateBeforeCall(String domainName, String siteName, String domainName2, String siteName2, AddHostHeaderRequest addHostHeaderRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling createHostHeader(Async)");
        }

        // verify the required parameter 'siteName' is set
        if (siteName == null) {
            throw new ApiException("Missing the required parameter 'siteName' when calling createHostHeader(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling createHostHeader(Async)");
        }

        // verify the required parameter 'siteName2' is set
        if (siteName2 == null) {
            throw new ApiException("Missing the required parameter 'siteName2' when calling createHostHeader(Async)");
        }

        return createHostHeaderCall(domainName, siteName, domainName2, siteName2, addHostHeaderRequest, _callback);

    }

    /**
     * Create a host header
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param siteName Name of the site on the linux hosting. (required)
     * @param domainName2 Automatically added (required)
     * @param siteName2 Automatically added (required)
     * @param addHostHeaderRequest Add host header request (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public void createHostHeader(String domainName, String siteName, String domainName2, String siteName2, AddHostHeaderRequest addHostHeaderRequest) throws ApiException {
        createHostHeaderWithHttpInfo(domainName, siteName, domainName2, siteName2, addHostHeaderRequest);
    }

    /**
     * Create a host header
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param siteName Name of the site on the linux hosting. (required)
     * @param domainName2 Automatically added (required)
     * @param siteName2 Automatically added (required)
     * @param addHostHeaderRequest Add host header request (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Void> createHostHeaderWithHttpInfo(String domainName, String siteName, String domainName2, String siteName2, AddHostHeaderRequest addHostHeaderRequest) throws ApiException {
        okhttp3.Call localVarCall = createHostHeaderValidateBeforeCall(domainName, siteName, domainName2, siteName2, addHostHeaderRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Create a host header (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param siteName Name of the site on the linux hosting. (required)
     * @param domainName2 Automatically added (required)
     * @param siteName2 Automatically added (required)
     * @param addHostHeaderRequest Add host header request (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call createHostHeaderAsync(String domainName, String siteName, String domainName2, String siteName2, AddHostHeaderRequest addHostHeaderRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = createHostHeaderValidateBeforeCall(domainName, siteName, domainName2, siteName2, addHostHeaderRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for createSubsite
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param addSubsiteRequest Add subsite request (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call createSubsiteCall(String domainName, String domainName2, AddSubsiteRequest addSubsiteRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addSubsiteRequest;

        // create path and map variables
        String localVarPath = "/linuxhostings/{domainName}/subsites"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createSubsiteValidateBeforeCall(String domainName, String domainName2, AddSubsiteRequest addSubsiteRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling createSubsite(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling createSubsite(Async)");
        }

        return createSubsiteCall(domainName, domainName2, addSubsiteRequest, _callback);

    }

    /**
     * Create a subsite
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param addSubsiteRequest Add subsite request (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public void createSubsite(String domainName, String domainName2, AddSubsiteRequest addSubsiteRequest) throws ApiException {
        createSubsiteWithHttpInfo(domainName, domainName2, addSubsiteRequest);
    }

    /**
     * Create a subsite
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param addSubsiteRequest Add subsite request (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Void> createSubsiteWithHttpInfo(String domainName, String domainName2, AddSubsiteRequest addSubsiteRequest) throws ApiException {
        okhttp3.Call localVarCall = createSubsiteValidateBeforeCall(domainName, domainName2, addSubsiteRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Create a subsite (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param addSubsiteRequest Add subsite request (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call createSubsiteAsync(String domainName, String domainName2, AddSubsiteRequest addSubsiteRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = createSubsiteValidateBeforeCall(domainName, domainName2, addSubsiteRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteScheduledTask
     * @param domainName Linux hosting domain name. (required)
     * @param scheduledTaskId Id of the scheduled task. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTaskId2 Automatically added (required)
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
    public okhttp3.Call deleteScheduledTaskCall(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId}"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()))
            .replace("{" + "scheduledTaskId" + "}", localVarApiClient.escapeString(scheduledTaskId2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
        }

        if (scheduledTaskId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("scheduled_task_id", scheduledTaskId));
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
    private okhttp3.Call deleteScheduledTaskValidateBeforeCall(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling deleteScheduledTask(Async)");
        }

        // verify the required parameter 'scheduledTaskId' is set
        if (scheduledTaskId == null) {
            throw new ApiException("Missing the required parameter 'scheduledTaskId' when calling deleteScheduledTask(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling deleteScheduledTask(Async)");
        }

        // verify the required parameter 'scheduledTaskId2' is set
        if (scheduledTaskId2 == null) {
            throw new ApiException("Missing the required parameter 'scheduledTaskId2' when calling deleteScheduledTask(Async)");
        }

        return deleteScheduledTaskCall(domainName, scheduledTaskId, domainName2, scheduledTaskId2, _callback);

    }

    /**
     * Delete a scheduled task
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param scheduledTaskId Id of the scheduled task. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTaskId2 Automatically added (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void deleteScheduledTask(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2) throws ApiException {
        deleteScheduledTaskWithHttpInfo(domainName, scheduledTaskId, domainName2, scheduledTaskId2);
    }

    /**
     * Delete a scheduled task
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param scheduledTaskId Id of the scheduled task. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTaskId2 Automatically added (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteScheduledTaskWithHttpInfo(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2) throws ApiException {
        okhttp3.Call localVarCall = deleteScheduledTaskValidateBeforeCall(domainName, scheduledTaskId, domainName2, scheduledTaskId2, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a scheduled task (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param scheduledTaskId Id of the scheduled task. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTaskId2 Automatically added (required)
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
    public okhttp3.Call deleteScheduledTaskAsync(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteScheduledTaskValidateBeforeCall(domainName, scheduledTaskId, domainName2, scheduledTaskId2, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteSshKey
     * @param domainName Linux hosting domain name. (required)
     * @param fingerprint Fingerprint of public key. (required)
     * @param domainName2 Automatically added (required)
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
    public okhttp3.Call deleteSshKeyCall(String domainName, String fingerprint, String domainName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/linuxhostings/{domainName}/ssh/keys/{fingerprint}"
            .replace("{" + "fingerprint" + "}", localVarApiClient.escapeString(fingerprint.toString()))
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
    private okhttp3.Call deleteSshKeyValidateBeforeCall(String domainName, String fingerprint, String domainName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling deleteSshKey(Async)");
        }

        // verify the required parameter 'fingerprint' is set
        if (fingerprint == null) {
            throw new ApiException("Missing the required parameter 'fingerprint' when calling deleteSshKey(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling deleteSshKey(Async)");
        }

        return deleteSshKeyCall(domainName, fingerprint, domainName2, _callback);

    }

    /**
     * Delete a SSH key
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param fingerprint Fingerprint of public key. (required)
     * @param domainName2 Automatically added (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void deleteSshKey(String domainName, String fingerprint, String domainName2) throws ApiException {
        deleteSshKeyWithHttpInfo(domainName, fingerprint, domainName2);
    }

    /**
     * Delete a SSH key
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param fingerprint Fingerprint of public key. (required)
     * @param domainName2 Automatically added (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteSshKeyWithHttpInfo(String domainName, String fingerprint, String domainName2) throws ApiException {
        okhttp3.Call localVarCall = deleteSshKeyValidateBeforeCall(domainName, fingerprint, domainName2, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a SSH key (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param fingerprint Fingerprint of public key. (required)
     * @param domainName2 Automatically added (required)
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
    public okhttp3.Call deleteSshKeyAsync(String domainName, String fingerprint, String domainName2, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteSshKeyValidateBeforeCall(domainName, fingerprint, domainName2, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteSubsite
     * @param domainName Linux hosting domain name. (required)
     * @param siteName Name of the site on the linux hosting. (required)
     * @param domainName2 Automatically added (required)
     * @param siteName2 Automatically added (required)
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
    public okhttp3.Call deleteSubsiteCall(String domainName, String siteName, String domainName2, String siteName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/linuxhostings/{domainName}/subsites/{siteName}"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()))
            .replace("{" + "siteName" + "}", localVarApiClient.escapeString(siteName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
        }

        if (siteName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("site_name", siteName));
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
    private okhttp3.Call deleteSubsiteValidateBeforeCall(String domainName, String siteName, String domainName2, String siteName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling deleteSubsite(Async)");
        }

        // verify the required parameter 'siteName' is set
        if (siteName == null) {
            throw new ApiException("Missing the required parameter 'siteName' when calling deleteSubsite(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling deleteSubsite(Async)");
        }

        // verify the required parameter 'siteName2' is set
        if (siteName2 == null) {
            throw new ApiException("Missing the required parameter 'siteName2' when calling deleteSubsite(Async)");
        }

        return deleteSubsiteCall(domainName, siteName, domainName2, siteName2, _callback);

    }

    /**
     * Delete a subsite
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param siteName Name of the site on the linux hosting. (required)
     * @param domainName2 Automatically added (required)
     * @param siteName2 Automatically added (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void deleteSubsite(String domainName, String siteName, String domainName2, String siteName2) throws ApiException {
        deleteSubsiteWithHttpInfo(domainName, siteName, domainName2, siteName2);
    }

    /**
     * Delete a subsite
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param siteName Name of the site on the linux hosting. (required)
     * @param domainName2 Automatically added (required)
     * @param siteName2 Automatically added (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteSubsiteWithHttpInfo(String domainName, String siteName, String domainName2, String siteName2) throws ApiException {
        okhttp3.Call localVarCall = deleteSubsiteValidateBeforeCall(domainName, siteName, domainName2, siteName2, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a subsite (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param siteName Name of the site on the linux hosting. (required)
     * @param domainName2 Automatically added (required)
     * @param siteName2 Automatically added (required)
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
    public okhttp3.Call deleteSubsiteAsync(String domainName, String siteName, String domainName2, String siteName2, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteSubsiteValidateBeforeCall(domainName, siteName, domainName2, siteName2, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getAvailablePhpVersions
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAvailablePhpVersionsCall(String domainName, String domainName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/linuxhostings/{domainName}/phpsettings/availableversions"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
    private okhttp3.Call getAvailablePhpVersionsValidateBeforeCall(String domainName, String domainName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling getAvailablePhpVersions(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling getAvailablePhpVersions(Async)");
        }

        return getAvailablePhpVersionsCall(domainName, domainName2, _callback);

    }

    /**
     * Get the available PHP versions.
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @return List&lt;PhpVersion&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public List<PhpVersion> getAvailablePhpVersions(String domainName, String domainName2) throws ApiException {
        ApiResponse<List<PhpVersion>> localVarResp = getAvailablePhpVersionsWithHttpInfo(domainName, domainName2);
        return localVarResp.getData();
    }

    /**
     * Get the available PHP versions.
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @return ApiResponse&lt;List&lt;PhpVersion&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<PhpVersion>> getAvailablePhpVersionsWithHttpInfo(String domainName, String domainName2) throws ApiException {
        okhttp3.Call localVarCall = getAvailablePhpVersionsValidateBeforeCall(domainName, domainName2, null);
        Type localVarReturnType = new TypeToken<List<PhpVersion>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get the available PHP versions. (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAvailablePhpVersionsAsync(String domainName, String domainName2, final ApiCallback<List<PhpVersion>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAvailablePhpVersionsValidateBeforeCall(domainName, domainName2, _callback);
        Type localVarReturnType = new TypeToken<List<PhpVersion>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinuxHosting
     * @param domainName The Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinuxHostingCall(String domainName, String domainName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/linuxhostings/{domainName}"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
    private okhttp3.Call getLinuxHostingValidateBeforeCall(String domainName, String domainName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling getLinuxHosting(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling getLinuxHosting(Async)");
        }

        return getLinuxHostingCall(domainName, domainName2, _callback);

    }

    /**
     * Linux hosting detail
     * 
     * @param domainName The Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @return LinuxHostingDetail
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public LinuxHostingDetail getLinuxHosting(String domainName, String domainName2) throws ApiException {
        ApiResponse<LinuxHostingDetail> localVarResp = getLinuxHostingWithHttpInfo(domainName, domainName2);
        return localVarResp.getData();
    }

    /**
     * Linux hosting detail
     * 
     * @param domainName The Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @return ApiResponse&lt;LinuxHostingDetail&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LinuxHostingDetail> getLinuxHostingWithHttpInfo(String domainName, String domainName2) throws ApiException {
        okhttp3.Call localVarCall = getLinuxHostingValidateBeforeCall(domainName, domainName2, null);
        Type localVarReturnType = new TypeToken<LinuxHostingDetail>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Linux hosting detail (asynchronously)
     * 
     * @param domainName The Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLinuxHostingAsync(String domainName, String domainName2, final ApiCallback<LinuxHostingDetail> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinuxHostingValidateBeforeCall(domainName, domainName2, _callback);
        Type localVarReturnType = new TypeToken<LinuxHostingDetail>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLinuxHostings
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
    public okhttp3.Call getLinuxHostingsCall(Integer skip, Integer take, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/linuxhostings";

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
    private okhttp3.Call getLinuxHostingsValidateBeforeCall(Integer skip, Integer take, final ApiCallback _callback) throws ApiException {
        return getLinuxHostingsCall(skip, take, _callback);

    }

    /**
     * Overview of linux hostings
     * 
     * @param skip The number of items to skip in the resultset. (optional)
     * @param take The number of items to return in the resultset. The returned count can be equal or less than this number. (optional)
     * @return List&lt;LinuxHosting&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  </td></tr>
     </table>
     */
    public List<LinuxHosting> getLinuxHostings(Integer skip, Integer take) throws ApiException {
        ApiResponse<List<LinuxHosting>> localVarResp = getLinuxHostingsWithHttpInfo(skip, take);
        return localVarResp.getData();
    }

    /**
     * Overview of linux hostings
     * 
     * @param skip The number of items to skip in the resultset. (optional)
     * @param take The number of items to return in the resultset. The returned count can be equal or less than this number. (optional)
     * @return ApiResponse&lt;List&lt;LinuxHosting&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  </td></tr>
     </table>
     */
    public ApiResponse<List<LinuxHosting>> getLinuxHostingsWithHttpInfo(Integer skip, Integer take) throws ApiException {
        okhttp3.Call localVarCall = getLinuxHostingsValidateBeforeCall(skip, take, null);
        Type localVarReturnType = new TypeToken<List<LinuxHosting>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Overview of linux hostings (asynchronously)
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
    public okhttp3.Call getLinuxHostingsAsync(Integer skip, Integer take, final ApiCallback<List<LinuxHosting>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLinuxHostingsValidateBeforeCall(skip, take, _callback);
        Type localVarReturnType = new TypeToken<List<LinuxHosting>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getScheduledTask
     * @param domainName Linux hosting domain name. (required)
     * @param scheduledTaskId Id of the scheduled task. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTaskId2 Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getScheduledTaskCall(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId}"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()))
            .replace("{" + "scheduledTaskId" + "}", localVarApiClient.escapeString(scheduledTaskId2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
        }

        if (scheduledTaskId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("scheduled_task_id", scheduledTaskId));
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
    private okhttp3.Call getScheduledTaskValidateBeforeCall(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling getScheduledTask(Async)");
        }

        // verify the required parameter 'scheduledTaskId' is set
        if (scheduledTaskId == null) {
            throw new ApiException("Missing the required parameter 'scheduledTaskId' when calling getScheduledTask(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling getScheduledTask(Async)");
        }

        // verify the required parameter 'scheduledTaskId2' is set
        if (scheduledTaskId2 == null) {
            throw new ApiException("Missing the required parameter 'scheduledTaskId2' when calling getScheduledTask(Async)");
        }

        return getScheduledTaskCall(domainName, scheduledTaskId, domainName2, scheduledTaskId2, _callback);

    }

    /**
     * Get scheduled task detail
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param scheduledTaskId Id of the scheduled task. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTaskId2 Automatically added (required)
     * @return ScheduledTask
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ScheduledTask getScheduledTask(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2) throws ApiException {
        ApiResponse<ScheduledTask> localVarResp = getScheduledTaskWithHttpInfo(domainName, scheduledTaskId, domainName2, scheduledTaskId2);
        return localVarResp.getData();
    }

    /**
     * Get scheduled task detail
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param scheduledTaskId Id of the scheduled task. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTaskId2 Automatically added (required)
     * @return ApiResponse&lt;ScheduledTask&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ScheduledTask> getScheduledTaskWithHttpInfo(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2) throws ApiException {
        okhttp3.Call localVarCall = getScheduledTaskValidateBeforeCall(domainName, scheduledTaskId, domainName2, scheduledTaskId2, null);
        Type localVarReturnType = new TypeToken<ScheduledTask>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get scheduled task detail (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param scheduledTaskId Id of the scheduled task. (required)
     * @param domainName2 Automatically added (required)
     * @param scheduledTaskId2 Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getScheduledTaskAsync(String domainName, String scheduledTaskId, String domainName2, String scheduledTaskId2, final ApiCallback<ScheduledTask> _callback) throws ApiException {

        okhttp3.Call localVarCall = getScheduledTaskValidateBeforeCall(domainName, scheduledTaskId, domainName2, scheduledTaskId2, _callback);
        Type localVarReturnType = new TypeToken<ScheduledTask>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getScheduledTasks
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getScheduledTasksCall(String domainName, String domainName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/linuxhostings/{domainName}/scheduledtasks"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
    private okhttp3.Call getScheduledTasksValidateBeforeCall(String domainName, String domainName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling getScheduledTasks(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling getScheduledTasks(Async)");
        }

        return getScheduledTasksCall(domainName, domainName2, _callback);

    }

    /**
     * Overview of scheduled tasks
     * Manage scheduled tasks which are also manageable via the control panel.
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @return List&lt;ScheduledTask&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public List<ScheduledTask> getScheduledTasks(String domainName, String domainName2) throws ApiException {
        ApiResponse<List<ScheduledTask>> localVarResp = getScheduledTasksWithHttpInfo(domainName, domainName2);
        return localVarResp.getData();
    }

    /**
     * Overview of scheduled tasks
     * Manage scheduled tasks which are also manageable via the control panel.
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @return ApiResponse&lt;List&lt;ScheduledTask&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ScheduledTask>> getScheduledTasksWithHttpInfo(String domainName, String domainName2) throws ApiException {
        okhttp3.Call localVarCall = getScheduledTasksValidateBeforeCall(domainName, domainName2, null);
        Type localVarReturnType = new TypeToken<List<ScheduledTask>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Overview of scheduled tasks (asynchronously)
     * Manage scheduled tasks which are also manageable via the control panel.
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getScheduledTasksAsync(String domainName, String domainName2, final ApiCallback<List<ScheduledTask>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getScheduledTasksValidateBeforeCall(domainName, domainName2, _callback);
        Type localVarReturnType = new TypeToken<List<ScheduledTask>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSshKeys
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSshKeysCall(String domainName, String domainName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/linuxhostings/{domainName}/ssh/keys"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
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
    private okhttp3.Call getSshKeysValidateBeforeCall(String domainName, String domainName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling getSshKeys(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling getSshKeys(Async)");
        }

        return getSshKeysCall(domainName, domainName2, _callback);

    }

    /**
     * Overview of SSH keys
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @return List&lt;SshKey&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public List<SshKey> getSshKeys(String domainName, String domainName2) throws ApiException {
        ApiResponse<List<SshKey>> localVarResp = getSshKeysWithHttpInfo(domainName, domainName2);
        return localVarResp.getData();
    }

    /**
     * Overview of SSH keys
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @return ApiResponse&lt;List&lt;SshKey&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<SshKey>> getSshKeysWithHttpInfo(String domainName, String domainName2) throws ApiException {
        okhttp3.Call localVarCall = getSshKeysValidateBeforeCall(domainName, domainName2, null);
        Type localVarReturnType = new TypeToken<List<SshKey>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Overview of SSH keys (asynchronously)
     * 
     * @param domainName Linux hosting domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSshKeysAsync(String domainName, String domainName2, final ApiCallback<List<SshKey>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSshKeysValidateBeforeCall(domainName, domainName2, _callback);
        Type localVarReturnType = new TypeToken<List<SshKey>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
