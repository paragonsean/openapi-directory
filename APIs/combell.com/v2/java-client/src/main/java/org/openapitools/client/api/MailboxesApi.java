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


import org.openapitools.client.model.AutoForward;
import org.openapitools.client.model.AutoReply;
import org.openapitools.client.model.CreateMailboxRequest;
import org.openapitools.client.model.Mailbox;
import org.openapitools.client.model.MailboxDetail;
import org.openapitools.client.model.UpdateMailboxPasswordRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MailboxesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public MailboxesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public MailboxesApi(ApiClient apiClient) {
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
     * Build call for changeMailboxPassword
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param updateMailboxPasswordRequest Contains the new password. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeMailboxPasswordCall(String mailboxName, String mailboxName2, UpdateMailboxPasswordRequest updateMailboxPasswordRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateMailboxPasswordRequest;

        // create path and map variables
        String localVarPath = "/mailboxes/{mailboxName}/password"
            .replace("{" + "mailboxName" + "}", localVarApiClient.escapeString(mailboxName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (mailboxName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("mailbox_name", mailboxName));
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
    private okhttp3.Call changeMailboxPasswordValidateBeforeCall(String mailboxName, String mailboxName2, UpdateMailboxPasswordRequest updateMailboxPasswordRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'mailboxName' is set
        if (mailboxName == null) {
            throw new ApiException("Missing the required parameter 'mailboxName' when calling changeMailboxPassword(Async)");
        }

        // verify the required parameter 'mailboxName2' is set
        if (mailboxName2 == null) {
            throw new ApiException("Missing the required parameter 'mailboxName2' when calling changeMailboxPassword(Async)");
        }

        return changeMailboxPasswordCall(mailboxName, mailboxName2, updateMailboxPasswordRequest, _callback);

    }

    /**
     * Change password for mailbox
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param updateMailboxPasswordRequest Contains the new password. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void changeMailboxPassword(String mailboxName, String mailboxName2, UpdateMailboxPasswordRequest updateMailboxPasswordRequest) throws ApiException {
        changeMailboxPasswordWithHttpInfo(mailboxName, mailboxName2, updateMailboxPasswordRequest);
    }

    /**
     * Change password for mailbox
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param updateMailboxPasswordRequest Contains the new password. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> changeMailboxPasswordWithHttpInfo(String mailboxName, String mailboxName2, UpdateMailboxPasswordRequest updateMailboxPasswordRequest) throws ApiException {
        okhttp3.Call localVarCall = changeMailboxPasswordValidateBeforeCall(mailboxName, mailboxName2, updateMailboxPasswordRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Change password for mailbox (asynchronously)
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param updateMailboxPasswordRequest Contains the new password. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call changeMailboxPasswordAsync(String mailboxName, String mailboxName2, UpdateMailboxPasswordRequest updateMailboxPasswordRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = changeMailboxPasswordValidateBeforeCall(mailboxName, mailboxName2, updateMailboxPasswordRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for configureMailboxAutoForward
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param autoForward Contains the auto-forward information. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call configureMailboxAutoForwardCall(String mailboxName, String mailboxName2, AutoForward autoForward, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = autoForward;

        // create path and map variables
        String localVarPath = "/mailboxes/{mailboxName}/autoforward"
            .replace("{" + "mailboxName" + "}", localVarApiClient.escapeString(mailboxName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (mailboxName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("mailbox_name", mailboxName));
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
    private okhttp3.Call configureMailboxAutoForwardValidateBeforeCall(String mailboxName, String mailboxName2, AutoForward autoForward, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'mailboxName' is set
        if (mailboxName == null) {
            throw new ApiException("Missing the required parameter 'mailboxName' when calling configureMailboxAutoForward(Async)");
        }

        // verify the required parameter 'mailboxName2' is set
        if (mailboxName2 == null) {
            throw new ApiException("Missing the required parameter 'mailboxName2' when calling configureMailboxAutoForward(Async)");
        }

        return configureMailboxAutoForwardCall(mailboxName, mailboxName2, autoForward, _callback);

    }

    /**
     * Configure auto-forward for mailbox
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param autoForward Contains the auto-forward information. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void configureMailboxAutoForward(String mailboxName, String mailboxName2, AutoForward autoForward) throws ApiException {
        configureMailboxAutoForwardWithHttpInfo(mailboxName, mailboxName2, autoForward);
    }

    /**
     * Configure auto-forward for mailbox
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param autoForward Contains the auto-forward information. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> configureMailboxAutoForwardWithHttpInfo(String mailboxName, String mailboxName2, AutoForward autoForward) throws ApiException {
        okhttp3.Call localVarCall = configureMailboxAutoForwardValidateBeforeCall(mailboxName, mailboxName2, autoForward, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure auto-forward for mailbox (asynchronously)
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param autoForward Contains the auto-forward information. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call configureMailboxAutoForwardAsync(String mailboxName, String mailboxName2, AutoForward autoForward, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = configureMailboxAutoForwardValidateBeforeCall(mailboxName, mailboxName2, autoForward, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for configureMailboxAutoReply
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param autoReply Contains the auto-reply information. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call configureMailboxAutoReplyCall(String mailboxName, String mailboxName2, AutoReply autoReply, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = autoReply;

        // create path and map variables
        String localVarPath = "/mailboxes/{mailboxName}/autoreply"
            .replace("{" + "mailboxName" + "}", localVarApiClient.escapeString(mailboxName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (mailboxName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("mailbox_name", mailboxName));
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
    private okhttp3.Call configureMailboxAutoReplyValidateBeforeCall(String mailboxName, String mailboxName2, AutoReply autoReply, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'mailboxName' is set
        if (mailboxName == null) {
            throw new ApiException("Missing the required parameter 'mailboxName' when calling configureMailboxAutoReply(Async)");
        }

        // verify the required parameter 'mailboxName2' is set
        if (mailboxName2 == null) {
            throw new ApiException("Missing the required parameter 'mailboxName2' when calling configureMailboxAutoReply(Async)");
        }

        return configureMailboxAutoReplyCall(mailboxName, mailboxName2, autoReply, _callback);

    }

    /**
     * Configure auto-reply for mailbox
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param autoReply Contains the auto-reply information. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void configureMailboxAutoReply(String mailboxName, String mailboxName2, AutoReply autoReply) throws ApiException {
        configureMailboxAutoReplyWithHttpInfo(mailboxName, mailboxName2, autoReply);
    }

    /**
     * Configure auto-reply for mailbox
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param autoReply Contains the auto-reply information. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> configureMailboxAutoReplyWithHttpInfo(String mailboxName, String mailboxName2, AutoReply autoReply) throws ApiException {
        okhttp3.Call localVarCall = configureMailboxAutoReplyValidateBeforeCall(mailboxName, mailboxName2, autoReply, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure auto-reply for mailbox (asynchronously)
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param autoReply Contains the auto-reply information. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call configureMailboxAutoReplyAsync(String mailboxName, String mailboxName2, AutoReply autoReply, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = configureMailboxAutoReplyValidateBeforeCall(mailboxName, mailboxName2, autoReply, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for createMailbox
     * @param createMailboxRequest The add mailbox request. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call createMailboxCall(CreateMailboxRequest createMailboxRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createMailboxRequest;

        // create path and map variables
        String localVarPath = "/mailboxes";

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
    private okhttp3.Call createMailboxValidateBeforeCall(CreateMailboxRequest createMailboxRequest, final ApiCallback _callback) throws ApiException {
        return createMailboxCall(createMailboxRequest, _callback);

    }

    /**
     * Create a new mailbox.
     * 
     * @param createMailboxRequest The add mailbox request. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public void createMailbox(CreateMailboxRequest createMailboxRequest) throws ApiException {
        createMailboxWithHttpInfo(createMailboxRequest);
    }

    /**
     * Create a new mailbox.
     * 
     * @param createMailboxRequest The add mailbox request. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Void> createMailboxWithHttpInfo(CreateMailboxRequest createMailboxRequest) throws ApiException {
        okhttp3.Call localVarCall = createMailboxValidateBeforeCall(createMailboxRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Create a new mailbox. (asynchronously)
     * 
     * @param createMailboxRequest The add mailbox request. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call createMailboxAsync(CreateMailboxRequest createMailboxRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = createMailboxValidateBeforeCall(createMailboxRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteMailbox
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
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
    public okhttp3.Call deleteMailboxCall(String mailboxName, String mailboxName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/mailboxes/{mailboxName}"
            .replace("{" + "mailboxName" + "}", localVarApiClient.escapeString(mailboxName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (mailboxName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("mailbox_name", mailboxName));
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
    private okhttp3.Call deleteMailboxValidateBeforeCall(String mailboxName, String mailboxName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'mailboxName' is set
        if (mailboxName == null) {
            throw new ApiException("Missing the required parameter 'mailboxName' when calling deleteMailbox(Async)");
        }

        // verify the required parameter 'mailboxName2' is set
        if (mailboxName2 == null) {
            throw new ApiException("Missing the required parameter 'mailboxName2' when calling deleteMailbox(Async)");
        }

        return deleteMailboxCall(mailboxName, mailboxName2, _callback);

    }

    /**
     * Delete a mailbox
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void deleteMailbox(String mailboxName, String mailboxName2) throws ApiException {
        deleteMailboxWithHttpInfo(mailboxName, mailboxName2);
    }

    /**
     * Delete a mailbox
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteMailboxWithHttpInfo(String mailboxName, String mailboxName2) throws ApiException {
        okhttp3.Call localVarCall = deleteMailboxValidateBeforeCall(mailboxName, mailboxName2, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a mailbox (asynchronously)
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
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
    public okhttp3.Call deleteMailboxAsync(String mailboxName, String mailboxName2, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteMailboxValidateBeforeCall(mailboxName, mailboxName2, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getMailbox
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMailboxCall(String mailboxName, String mailboxName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/mailboxes/{mailboxName}"
            .replace("{" + "mailboxName" + "}", localVarApiClient.escapeString(mailboxName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (mailboxName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("mailbox_name", mailboxName));
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
    private okhttp3.Call getMailboxValidateBeforeCall(String mailboxName, String mailboxName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'mailboxName' is set
        if (mailboxName == null) {
            throw new ApiException("Missing the required parameter 'mailboxName' when calling getMailbox(Async)");
        }

        // verify the required parameter 'mailboxName2' is set
        if (mailboxName2 == null) {
            throw new ApiException("Missing the required parameter 'mailboxName2' when calling getMailbox(Async)");
        }

        return getMailboxCall(mailboxName, mailboxName2, _callback);

    }

    /**
     * Get a specific mailbox
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @return MailboxDetail
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public MailboxDetail getMailbox(String mailboxName, String mailboxName2) throws ApiException {
        ApiResponse<MailboxDetail> localVarResp = getMailboxWithHttpInfo(mailboxName, mailboxName2);
        return localVarResp.getData();
    }

    /**
     * Get a specific mailbox
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @return ApiResponse&lt;MailboxDetail&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<MailboxDetail> getMailboxWithHttpInfo(String mailboxName, String mailboxName2) throws ApiException {
        okhttp3.Call localVarCall = getMailboxValidateBeforeCall(mailboxName, mailboxName2, null);
        Type localVarReturnType = new TypeToken<MailboxDetail>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get a specific mailbox (asynchronously)
     * 
     * @param mailboxName Mailbox name. (required)
     * @param mailboxName2 Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMailboxAsync(String mailboxName, String mailboxName2, final ApiCallback<MailboxDetail> _callback) throws ApiException {

        okhttp3.Call localVarCall = getMailboxValidateBeforeCall(mailboxName, mailboxName2, _callback);
        Type localVarReturnType = new TypeToken<MailboxDetail>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getMailboxes
     * @param domainName Obligated domain name for getting mailboxes. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMailboxesCall(String domainName, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/mailboxes";

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
    private okhttp3.Call getMailboxesValidateBeforeCall(String domainName, final ApiCallback _callback) throws ApiException {
        return getMailboxesCall(domainName, _callback);

    }

    /**
     * Gets your mailboxes.
     * Currently only supports getting the mailboxes filtered by domain name.
     * @param domainName Obligated domain name for getting mailboxes. (optional)
     * @return List&lt;Mailbox&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public List<Mailbox> getMailboxes(String domainName) throws ApiException {
        ApiResponse<List<Mailbox>> localVarResp = getMailboxesWithHttpInfo(domainName);
        return localVarResp.getData();
    }

    /**
     * Gets your mailboxes.
     * Currently only supports getting the mailboxes filtered by domain name.
     * @param domainName Obligated domain name for getting mailboxes. (optional)
     * @return ApiResponse&lt;List&lt;Mailbox&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Mailbox>> getMailboxesWithHttpInfo(String domainName) throws ApiException {
        okhttp3.Call localVarCall = getMailboxesValidateBeforeCall(domainName, null);
        Type localVarReturnType = new TypeToken<List<Mailbox>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Gets your mailboxes. (asynchronously)
     * Currently only supports getting the mailboxes filtered by domain name.
     * @param domainName Obligated domain name for getting mailboxes. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getMailboxesAsync(String domainName, final ApiCallback<List<Mailbox>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getMailboxesValidateBeforeCall(domainName, _callback);
        Type localVarReturnType = new TypeToken<List<Mailbox>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
