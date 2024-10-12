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


import org.openapitools.client.model.CreateSslCertificateRequest;
import org.openapitools.client.model.SslCertificateRequest;
import org.openapitools.client.model.SslCertificateRequestDetail;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SslCertificateRequestsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SslCertificateRequestsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SslCertificateRequestsApi(ApiClient apiClient) {
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
     * Build call for addSslCertificateRequest
     * @param createSslCertificateRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call addSslCertificateRequestCall(CreateSslCertificateRequest createSslCertificateRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createSslCertificateRequest;

        // create path and map variables
        String localVarPath = "/sslcertificaterequests";

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
    private okhttp3.Call addSslCertificateRequestValidateBeforeCall(CreateSslCertificateRequest createSslCertificateRequest, final ApiCallback _callback) throws ApiException {
        return addSslCertificateRequestCall(createSslCertificateRequest, _callback);

    }

    /**
     * Add a SSL certificate request
     * Executing this method causes the purchase of a paying product.&lt;br /&gt;  Log on to our website to see your current (renewal) prices or contact our Sales department.&lt;br /&gt;  Please note that promotional pricing does not apply for purchases made through our API.
     * @param createSslCertificateRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public void addSslCertificateRequest(CreateSslCertificateRequest createSslCertificateRequest) throws ApiException {
        addSslCertificateRequestWithHttpInfo(createSslCertificateRequest);
    }

    /**
     * Add a SSL certificate request
     * Executing this method causes the purchase of a paying product.&lt;br /&gt;  Log on to our website to see your current (renewal) prices or contact our Sales department.&lt;br /&gt;  Please note that promotional pricing does not apply for purchases made through our API.
     * @param createSslCertificateRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Void> addSslCertificateRequestWithHttpInfo(CreateSslCertificateRequest createSslCertificateRequest) throws ApiException {
        okhttp3.Call localVarCall = addSslCertificateRequestValidateBeforeCall(createSslCertificateRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Add a SSL certificate request (asynchronously)
     * Executing this method causes the purchase of a paying product.&lt;br /&gt;  Log on to our website to see your current (renewal) prices or contact our Sales department.&lt;br /&gt;  Please note that promotional pricing does not apply for purchases made through our API.
     * @param createSslCertificateRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call addSslCertificateRequestAsync(CreateSslCertificateRequest createSslCertificateRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = addSslCertificateRequestValidateBeforeCall(createSslCertificateRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSslCertificateRequest
     * @param id The id of the certificate request. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 303 </td><td> Redirect </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 410 </td><td> The resource existed in the past, but is no longer available. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSslCertificateRequestCall(Integer id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/sslcertificaterequests/{id}"
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
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getSslCertificateRequestValidateBeforeCall(Integer id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getSslCertificateRequest(Async)");
        }

        return getSslCertificateRequestCall(id, _callback);

    }

    /**
     * Detail of a SSL certificate request
     * 
     * @param id The id of the certificate request. (required)
     * @return SslCertificateRequestDetail
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 303 </td><td> Redirect </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 410 </td><td> The resource existed in the past, but is no longer available. </td><td>  -  </td></tr>
     </table>
     */
    public SslCertificateRequestDetail getSslCertificateRequest(Integer id) throws ApiException {
        ApiResponse<SslCertificateRequestDetail> localVarResp = getSslCertificateRequestWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Detail of a SSL certificate request
     * 
     * @param id The id of the certificate request. (required)
     * @return ApiResponse&lt;SslCertificateRequestDetail&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 303 </td><td> Redirect </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 410 </td><td> The resource existed in the past, but is no longer available. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SslCertificateRequestDetail> getSslCertificateRequestWithHttpInfo(Integer id) throws ApiException {
        okhttp3.Call localVarCall = getSslCertificateRequestValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<SslCertificateRequestDetail>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Detail of a SSL certificate request (asynchronously)
     * 
     * @param id The id of the certificate request. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 303 </td><td> Redirect </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 410 </td><td> The resource existed in the past, but is no longer available. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSslCertificateRequestAsync(Integer id, final ApiCallback<SslCertificateRequestDetail> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSslCertificateRequestValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<SslCertificateRequestDetail>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSslCertificateRequests
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
    public okhttp3.Call getSslCertificateRequestsCall(Integer skip, Integer take, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/sslcertificaterequests";

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
    private okhttp3.Call getSslCertificateRequestsValidateBeforeCall(Integer skip, Integer take, final ApiCallback _callback) throws ApiException {
        return getSslCertificateRequestsCall(skip, take, _callback);

    }

    /**
     * Overview of SSL certificate requests
     * 
     * @param skip The number of items to skip in the resultset. (optional)
     * @param take The number of items to return in the resultset. The returned count can be equal or less than this number. (optional)
     * @return List&lt;SslCertificateRequest&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  </td></tr>
     </table>
     */
    public List<SslCertificateRequest> getSslCertificateRequests(Integer skip, Integer take) throws ApiException {
        ApiResponse<List<SslCertificateRequest>> localVarResp = getSslCertificateRequestsWithHttpInfo(skip, take);
        return localVarResp.getData();
    }

    /**
     * Overview of SSL certificate requests
     * 
     * @param skip The number of items to skip in the resultset. (optional)
     * @param take The number of items to return in the resultset. The returned count can be equal or less than this number. (optional)
     * @return ApiResponse&lt;List&lt;SslCertificateRequest&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  </td></tr>
     </table>
     */
    public ApiResponse<List<SslCertificateRequest>> getSslCertificateRequestsWithHttpInfo(Integer skip, Integer take) throws ApiException {
        okhttp3.Call localVarCall = getSslCertificateRequestsValidateBeforeCall(skip, take, null);
        Type localVarReturnType = new TypeToken<List<SslCertificateRequest>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Overview of SSL certificate requests (asynchronously)
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
    public okhttp3.Call getSslCertificateRequestsAsync(Integer skip, Integer take, final ApiCallback<List<SslCertificateRequest>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSslCertificateRequestsValidateBeforeCall(skip, take, _callback);
        Type localVarReturnType = new TypeToken<List<SslCertificateRequest>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for verifySslCertificateRequestDomainValidations
     * @param id The id of the certificate request. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 303 </td><td> Redirect </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 410 </td><td> The resource existed in the past, but is no longer available. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call verifySslCertificateRequestDomainValidationsCall(Integer id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/sslcertificaterequests/{id}"
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call verifySslCertificateRequestDomainValidationsValidateBeforeCall(Integer id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling verifySslCertificateRequestDomainValidations(Async)");
        }

        return verifySslCertificateRequestDomainValidationsCall(id, _callback);

    }

    /**
     * Verify the SSL certificate request domain validations
     * 
     * @param id The id of the certificate request. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 303 </td><td> Redirect </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 410 </td><td> The resource existed in the past, but is no longer available. </td><td>  -  </td></tr>
     </table>
     */
    public void verifySslCertificateRequestDomainValidations(Integer id) throws ApiException {
        verifySslCertificateRequestDomainValidationsWithHttpInfo(id);
    }

    /**
     * Verify the SSL certificate request domain validations
     * 
     * @param id The id of the certificate request. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 303 </td><td> Redirect </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 410 </td><td> The resource existed in the past, but is no longer available. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> verifySslCertificateRequestDomainValidationsWithHttpInfo(Integer id) throws ApiException {
        okhttp3.Call localVarCall = verifySslCertificateRequestDomainValidationsValidateBeforeCall(id, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Verify the SSL certificate request domain validations (asynchronously)
     * 
     * @param id The id of the certificate request. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 202 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 303 </td><td> Redirect </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
        <tr><td> 410 </td><td> The resource existed in the past, but is no longer available. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call verifySslCertificateRequestDomainValidationsAsync(Integer id, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = verifySslCertificateRequestDomainValidationsValidateBeforeCall(id, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
