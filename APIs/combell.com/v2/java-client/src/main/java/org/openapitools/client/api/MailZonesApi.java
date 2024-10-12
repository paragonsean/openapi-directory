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
import org.openapitools.client.model.CreateAliasRequest;
import org.openapitools.client.model.CreateCatchAllRequest;
import org.openapitools.client.model.CreateSmtpDomainRequest;
import org.openapitools.client.model.MailZone;
import org.openapitools.client.model.UpdateAliasRequest;
import org.openapitools.client.model.UpdateAntiSpamRequest;
import org.openapitools.client.model.UpdateSmtpDomainRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MailZonesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public MailZonesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public MailZonesApi(ApiClient apiClient) {
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
     * Build call for configureAlias
     * @param domainName Mail zone domain name. (required)
     * @param emailAddress Alias e-mail address. (required)
     * @param domainName2 Automatically added (required)
     * @param emailAddress2 Automatically added (required)
     * @param updateAliasRequest Contains the alias information. (optional)
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
    public okhttp3.Call configureAliasCall(String domainName, String emailAddress, String domainName2, String emailAddress2, UpdateAliasRequest updateAliasRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateAliasRequest;

        // create path and map variables
        String localVarPath = "/mailzones/{domainName}/aliases/{emailAddress}"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()))
            .replace("{" + "emailAddress" + "}", localVarApiClient.escapeString(emailAddress2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
        }

        if (emailAddress != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("email_address", emailAddress));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call configureAliasValidateBeforeCall(String domainName, String emailAddress, String domainName2, String emailAddress2, UpdateAliasRequest updateAliasRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling configureAlias(Async)");
        }

        // verify the required parameter 'emailAddress' is set
        if (emailAddress == null) {
            throw new ApiException("Missing the required parameter 'emailAddress' when calling configureAlias(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling configureAlias(Async)");
        }

        // verify the required parameter 'emailAddress2' is set
        if (emailAddress2 == null) {
            throw new ApiException("Missing the required parameter 'emailAddress2' when calling configureAlias(Async)");
        }

        return configureAliasCall(domainName, emailAddress, domainName2, emailAddress2, updateAliasRequest, _callback);

    }

    /**
     * Configure a alias
     * 
     * @param domainName Mail zone domain name. (required)
     * @param emailAddress Alias e-mail address. (required)
     * @param domainName2 Automatically added (required)
     * @param emailAddress2 Automatically added (required)
     * @param updateAliasRequest Contains the alias information. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void configureAlias(String domainName, String emailAddress, String domainName2, String emailAddress2, UpdateAliasRequest updateAliasRequest) throws ApiException {
        configureAliasWithHttpInfo(domainName, emailAddress, domainName2, emailAddress2, updateAliasRequest);
    }

    /**
     * Configure a alias
     * 
     * @param domainName Mail zone domain name. (required)
     * @param emailAddress Alias e-mail address. (required)
     * @param domainName2 Automatically added (required)
     * @param emailAddress2 Automatically added (required)
     * @param updateAliasRequest Contains the alias information. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> configureAliasWithHttpInfo(String domainName, String emailAddress, String domainName2, String emailAddress2, UpdateAliasRequest updateAliasRequest) throws ApiException {
        okhttp3.Call localVarCall = configureAliasValidateBeforeCall(domainName, emailAddress, domainName2, emailAddress2, updateAliasRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure a alias (asynchronously)
     * 
     * @param domainName Mail zone domain name. (required)
     * @param emailAddress Alias e-mail address. (required)
     * @param domainName2 Automatically added (required)
     * @param emailAddress2 Automatically added (required)
     * @param updateAliasRequest Contains the alias information. (optional)
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
    public okhttp3.Call configureAliasAsync(String domainName, String emailAddress, String domainName2, String emailAddress2, UpdateAliasRequest updateAliasRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = configureAliasValidateBeforeCall(domainName, emailAddress, domainName2, emailAddress2, updateAliasRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for configureAntiSpam
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param updateAntiSpamRequest Contains the anti-spam information. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call configureAntiSpamCall(String domainName, String domainName2, UpdateAntiSpamRequest updateAntiSpamRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateAntiSpamRequest;

        // create path and map variables
        String localVarPath = "/mailzones/{domainName}/antispam"
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
    private okhttp3.Call configureAntiSpamValidateBeforeCall(String domainName, String domainName2, UpdateAntiSpamRequest updateAntiSpamRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling configureAntiSpam(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling configureAntiSpam(Async)");
        }

        return configureAntiSpamCall(domainName, domainName2, updateAntiSpamRequest, _callback);

    }

    /**
     * Configure anti-spam for mail zone
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param updateAntiSpamRequest Contains the anti-spam information. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void configureAntiSpam(String domainName, String domainName2, UpdateAntiSpamRequest updateAntiSpamRequest) throws ApiException {
        configureAntiSpamWithHttpInfo(domainName, domainName2, updateAntiSpamRequest);
    }

    /**
     * Configure anti-spam for mail zone
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param updateAntiSpamRequest Contains the anti-spam information. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> configureAntiSpamWithHttpInfo(String domainName, String domainName2, UpdateAntiSpamRequest updateAntiSpamRequest) throws ApiException {
        okhttp3.Call localVarCall = configureAntiSpamValidateBeforeCall(domainName, domainName2, updateAntiSpamRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure anti-spam for mail zone (asynchronously)
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param updateAntiSpamRequest Contains the anti-spam information. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call configureAntiSpamAsync(String domainName, String domainName2, UpdateAntiSpamRequest updateAntiSpamRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = configureAntiSpamValidateBeforeCall(domainName, domainName2, updateAntiSpamRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for configureSmtpDomain
     * @param domainName Mail zone domain name. (required)
     * @param hostname Smtp domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param updateSmtpDomainRequest Contains the smtp domain information. (optional)
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
    public okhttp3.Call configureSmtpDomainCall(String domainName, String hostname, String domainName2, UpdateSmtpDomainRequest updateSmtpDomainRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateSmtpDomainRequest;

        // create path and map variables
        String localVarPath = "/mailzones/{domainName}/smtpdomains/{hostname}"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call configureSmtpDomainValidateBeforeCall(String domainName, String hostname, String domainName2, UpdateSmtpDomainRequest updateSmtpDomainRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling configureSmtpDomain(Async)");
        }

        // verify the required parameter 'hostname' is set
        if (hostname == null) {
            throw new ApiException("Missing the required parameter 'hostname' when calling configureSmtpDomain(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling configureSmtpDomain(Async)");
        }

        return configureSmtpDomainCall(domainName, hostname, domainName2, updateSmtpDomainRequest, _callback);

    }

    /**
     * Configure an extra smtp domain
     * 
     * @param domainName Mail zone domain name. (required)
     * @param hostname Smtp domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param updateSmtpDomainRequest Contains the smtp domain information. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void configureSmtpDomain(String domainName, String hostname, String domainName2, UpdateSmtpDomainRequest updateSmtpDomainRequest) throws ApiException {
        configureSmtpDomainWithHttpInfo(domainName, hostname, domainName2, updateSmtpDomainRequest);
    }

    /**
     * Configure an extra smtp domain
     * 
     * @param domainName Mail zone domain name. (required)
     * @param hostname Smtp domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param updateSmtpDomainRequest Contains the smtp domain information. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> configureSmtpDomainWithHttpInfo(String domainName, String hostname, String domainName2, UpdateSmtpDomainRequest updateSmtpDomainRequest) throws ApiException {
        okhttp3.Call localVarCall = configureSmtpDomainValidateBeforeCall(domainName, hostname, domainName2, updateSmtpDomainRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure an extra smtp domain (asynchronously)
     * 
     * @param domainName Mail zone domain name. (required)
     * @param hostname Smtp domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param updateSmtpDomainRequest Contains the smtp domain information. (optional)
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
    public okhttp3.Call configureSmtpDomainAsync(String domainName, String hostname, String domainName2, UpdateSmtpDomainRequest updateSmtpDomainRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = configureSmtpDomainValidateBeforeCall(domainName, hostname, domainName2, updateSmtpDomainRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for createAlias
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param createAliasRequest Contains the alias information. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createAliasCall(String domainName, String domainName2, CreateAliasRequest createAliasRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createAliasRequest;

        // create path and map variables
        String localVarPath = "/mailzones/{domainName}/aliases"
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
    private okhttp3.Call createAliasValidateBeforeCall(String domainName, String domainName2, CreateAliasRequest createAliasRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling createAlias(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling createAlias(Async)");
        }

        return createAliasCall(domainName, domainName2, createAliasRequest, _callback);

    }

    /**
     * Create a new alias
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param createAliasRequest Contains the alias information. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void createAlias(String domainName, String domainName2, CreateAliasRequest createAliasRequest) throws ApiException {
        createAliasWithHttpInfo(domainName, domainName2, createAliasRequest);
    }

    /**
     * Create a new alias
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param createAliasRequest Contains the alias information. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> createAliasWithHttpInfo(String domainName, String domainName2, CreateAliasRequest createAliasRequest) throws ApiException {
        okhttp3.Call localVarCall = createAliasValidateBeforeCall(domainName, domainName2, createAliasRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Create a new alias (asynchronously)
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param createAliasRequest Contains the alias information. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createAliasAsync(String domainName, String domainName2, CreateAliasRequest createAliasRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = createAliasValidateBeforeCall(domainName, domainName2, createAliasRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for createCatchAll
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param createCatchAllRequest Contains the catch-all information. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call createCatchAllCall(String domainName, String domainName2, CreateCatchAllRequest createCatchAllRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createCatchAllRequest;

        // create path and map variables
        String localVarPath = "/mailzones/{domainName}/catchall"
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
    private okhttp3.Call createCatchAllValidateBeforeCall(String domainName, String domainName2, CreateCatchAllRequest createCatchAllRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling createCatchAll(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling createCatchAll(Async)");
        }

        return createCatchAllCall(domainName, domainName2, createCatchAllRequest, _callback);

    }

    /**
     * Create a catch-all on the mail zone
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param createCatchAllRequest Contains the catch-all information. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public void createCatchAll(String domainName, String domainName2, CreateCatchAllRequest createCatchAllRequest) throws ApiException {
        createCatchAllWithHttpInfo(domainName, domainName2, createCatchAllRequest);
    }

    /**
     * Create a catch-all on the mail zone
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param createCatchAllRequest Contains the catch-all information. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Void> createCatchAllWithHttpInfo(String domainName, String domainName2, CreateCatchAllRequest createCatchAllRequest) throws ApiException {
        okhttp3.Call localVarCall = createCatchAllValidateBeforeCall(domainName, domainName2, createCatchAllRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Create a catch-all on the mail zone (asynchronously)
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param createCatchAllRequest Contains the catch-all information. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call createCatchAllAsync(String domainName, String domainName2, CreateCatchAllRequest createCatchAllRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = createCatchAllValidateBeforeCall(domainName, domainName2, createCatchAllRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for createSmtpDomain
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param createSmtpDomainRequest Contains the smtp domain information. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createSmtpDomainCall(String domainName, String domainName2, CreateSmtpDomainRequest createSmtpDomainRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createSmtpDomainRequest;

        // create path and map variables
        String localVarPath = "/mailzones/{domainName}/smtpdomains"
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
    private okhttp3.Call createSmtpDomainValidateBeforeCall(String domainName, String domainName2, CreateSmtpDomainRequest createSmtpDomainRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling createSmtpDomain(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling createSmtpDomain(Async)");
        }

        return createSmtpDomainCall(domainName, domainName2, createSmtpDomainRequest, _callback);

    }

    /**
     * Create an extra smtp domain
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param createSmtpDomainRequest Contains the smtp domain information. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void createSmtpDomain(String domainName, String domainName2, CreateSmtpDomainRequest createSmtpDomainRequest) throws ApiException {
        createSmtpDomainWithHttpInfo(domainName, domainName2, createSmtpDomainRequest);
    }

    /**
     * Create an extra smtp domain
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param createSmtpDomainRequest Contains the smtp domain information. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> createSmtpDomainWithHttpInfo(String domainName, String domainName2, CreateSmtpDomainRequest createSmtpDomainRequest) throws ApiException {
        okhttp3.Call localVarCall = createSmtpDomainValidateBeforeCall(domainName, domainName2, createSmtpDomainRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Create an extra smtp domain (asynchronously)
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param createSmtpDomainRequest Contains the smtp domain information. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createSmtpDomainAsync(String domainName, String domainName2, CreateSmtpDomainRequest createSmtpDomainRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = createSmtpDomainValidateBeforeCall(domainName, domainName2, createSmtpDomainRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteAlias
     * @param domainName Mail zone domain name. (required)
     * @param emailAddress Alias e-mail address. (required)
     * @param domainName2 Automatically added (required)
     * @param emailAddress2 Automatically added (required)
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
    public okhttp3.Call deleteAliasCall(String domainName, String emailAddress, String domainName2, String emailAddress2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/mailzones/{domainName}/aliases/{emailAddress}"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()))
            .replace("{" + "emailAddress" + "}", localVarApiClient.escapeString(emailAddress2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
        }

        if (emailAddress != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("email_address", emailAddress));
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
    private okhttp3.Call deleteAliasValidateBeforeCall(String domainName, String emailAddress, String domainName2, String emailAddress2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling deleteAlias(Async)");
        }

        // verify the required parameter 'emailAddress' is set
        if (emailAddress == null) {
            throw new ApiException("Missing the required parameter 'emailAddress' when calling deleteAlias(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling deleteAlias(Async)");
        }

        // verify the required parameter 'emailAddress2' is set
        if (emailAddress2 == null) {
            throw new ApiException("Missing the required parameter 'emailAddress2' when calling deleteAlias(Async)");
        }

        return deleteAliasCall(domainName, emailAddress, domainName2, emailAddress2, _callback);

    }

    /**
     * Delete a alias
     * 
     * @param domainName Mail zone domain name. (required)
     * @param emailAddress Alias e-mail address. (required)
     * @param domainName2 Automatically added (required)
     * @param emailAddress2 Automatically added (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void deleteAlias(String domainName, String emailAddress, String domainName2, String emailAddress2) throws ApiException {
        deleteAliasWithHttpInfo(domainName, emailAddress, domainName2, emailAddress2);
    }

    /**
     * Delete a alias
     * 
     * @param domainName Mail zone domain name. (required)
     * @param emailAddress Alias e-mail address. (required)
     * @param domainName2 Automatically added (required)
     * @param emailAddress2 Automatically added (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteAliasWithHttpInfo(String domainName, String emailAddress, String domainName2, String emailAddress2) throws ApiException {
        okhttp3.Call localVarCall = deleteAliasValidateBeforeCall(domainName, emailAddress, domainName2, emailAddress2, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a alias (asynchronously)
     * 
     * @param domainName Mail zone domain name. (required)
     * @param emailAddress Alias e-mail address. (required)
     * @param domainName2 Automatically added (required)
     * @param emailAddress2 Automatically added (required)
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
    public okhttp3.Call deleteAliasAsync(String domainName, String emailAddress, String domainName2, String emailAddress2, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteAliasValidateBeforeCall(domainName, emailAddress, domainName2, emailAddress2, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteCatchAll
     * @param domainName Mail zone domain name. (required)
     * @param emailAddress E-mail address to which all e-mails are sent to inexistent mailboxes or aliases. (required)
     * @param domainName2 Automatically added (required)
     * @param emailAddress2 Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteCatchAllCall(String domainName, String emailAddress, String domainName2, String emailAddress2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/mailzones/{domainName}/catchall/{emailAddress}"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()))
            .replace("{" + "emailAddress" + "}", localVarApiClient.escapeString(emailAddress2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
        }

        if (emailAddress != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("email_address", emailAddress));
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
    private okhttp3.Call deleteCatchAllValidateBeforeCall(String domainName, String emailAddress, String domainName2, String emailAddress2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling deleteCatchAll(Async)");
        }

        // verify the required parameter 'emailAddress' is set
        if (emailAddress == null) {
            throw new ApiException("Missing the required parameter 'emailAddress' when calling deleteCatchAll(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling deleteCatchAll(Async)");
        }

        // verify the required parameter 'emailAddress2' is set
        if (emailAddress2 == null) {
            throw new ApiException("Missing the required parameter 'emailAddress2' when calling deleteCatchAll(Async)");
        }

        return deleteCatchAllCall(domainName, emailAddress, domainName2, emailAddress2, _callback);

    }

    /**
     * Delete a catch-all on the mail zone
     * 
     * @param domainName Mail zone domain name. (required)
     * @param emailAddress E-mail address to which all e-mails are sent to inexistent mailboxes or aliases. (required)
     * @param domainName2 Automatically added (required)
     * @param emailAddress2 Automatically added (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void deleteCatchAll(String domainName, String emailAddress, String domainName2, String emailAddress2) throws ApiException {
        deleteCatchAllWithHttpInfo(domainName, emailAddress, domainName2, emailAddress2);
    }

    /**
     * Delete a catch-all on the mail zone
     * 
     * @param domainName Mail zone domain name. (required)
     * @param emailAddress E-mail address to which all e-mails are sent to inexistent mailboxes or aliases. (required)
     * @param domainName2 Automatically added (required)
     * @param emailAddress2 Automatically added (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteCatchAllWithHttpInfo(String domainName, String emailAddress, String domainName2, String emailAddress2) throws ApiException {
        okhttp3.Call localVarCall = deleteCatchAllValidateBeforeCall(domainName, emailAddress, domainName2, emailAddress2, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a catch-all on the mail zone (asynchronously)
     * 
     * @param domainName Mail zone domain name. (required)
     * @param emailAddress E-mail address to which all e-mails are sent to inexistent mailboxes or aliases. (required)
     * @param domainName2 Automatically added (required)
     * @param emailAddress2 Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteCatchAllAsync(String domainName, String emailAddress, String domainName2, String emailAddress2, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteCatchAllValidateBeforeCall(domainName, emailAddress, domainName2, emailAddress2, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteSmtpDomain
     * @param domainName Mail zone domain name. (required)
     * @param hostname Smtp domain name. (required)
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
    public okhttp3.Call deleteSmtpDomainCall(String domainName, String hostname, String domainName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/mailzones/{domainName}/smtpdomains/{hostname}"
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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteSmtpDomainValidateBeforeCall(String domainName, String hostname, String domainName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling deleteSmtpDomain(Async)");
        }

        // verify the required parameter 'hostname' is set
        if (hostname == null) {
            throw new ApiException("Missing the required parameter 'hostname' when calling deleteSmtpDomain(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling deleteSmtpDomain(Async)");
        }

        return deleteSmtpDomainCall(domainName, hostname, domainName2, _callback);

    }

    /**
     * Delete an extra smtp domain
     * 
     * @param domainName Mail zone domain name. (required)
     * @param hostname Smtp domain name. (required)
     * @param domainName2 Automatically added (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
     </table>
     */
    public void deleteSmtpDomain(String domainName, String hostname, String domainName2) throws ApiException {
        deleteSmtpDomainWithHttpInfo(domainName, hostname, domainName2);
    }

    /**
     * Delete an extra smtp domain
     * 
     * @param domainName Mail zone domain name. (required)
     * @param hostname Smtp domain name. (required)
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
    public ApiResponse<Void> deleteSmtpDomainWithHttpInfo(String domainName, String hostname, String domainName2) throws ApiException {
        okhttp3.Call localVarCall = deleteSmtpDomainValidateBeforeCall(domainName, hostname, domainName2, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete an extra smtp domain (asynchronously)
     * 
     * @param domainName Mail zone domain name. (required)
     * @param hostname Smtp domain name. (required)
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
    public okhttp3.Call deleteSmtpDomainAsync(String domainName, String hostname, String domainName2, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteSmtpDomainValidateBeforeCall(domainName, hostname, domainName2, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getMailZone
     * @param domainName Mail zone domain name. (required)
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
    public okhttp3.Call getMailZoneCall(String domainName, String domainName2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/mailzones/{domainName}"
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
    private okhttp3.Call getMailZoneValidateBeforeCall(String domainName, String domainName2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling getMailZone(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling getMailZone(Async)");
        }

        return getMailZoneCall(domainName, domainName2, _callback);

    }

    /**
     * Get the mail zone.
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @return MailZone
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public MailZone getMailZone(String domainName, String domainName2) throws ApiException {
        ApiResponse<MailZone> localVarResp = getMailZoneWithHttpInfo(domainName, domainName2);
        return localVarResp.getData();
    }

    /**
     * Get the mail zone.
     * 
     * @param domainName Mail zone domain name. (required)
     * @param domainName2 Automatically added (required)
     * @return ApiResponse&lt;MailZone&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<MailZone> getMailZoneWithHttpInfo(String domainName, String domainName2) throws ApiException {
        okhttp3.Call localVarCall = getMailZoneValidateBeforeCall(domainName, domainName2, null);
        Type localVarReturnType = new TypeToken<MailZone>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get the mail zone. (asynchronously)
     * 
     * @param domainName Mail zone domain name. (required)
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
    public okhttp3.Call getMailZoneAsync(String domainName, String domainName2, final ApiCallback<MailZone> _callback) throws ApiException {

        okhttp3.Call localVarCall = getMailZoneValidateBeforeCall(domainName, domainName2, _callback);
        Type localVarReturnType = new TypeToken<MailZone>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
