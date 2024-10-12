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


import org.openapitools.client.model.DnsRecord;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DnsRecordsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DnsRecordsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DnsRecordsApi(ApiClient apiClient) {
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
     * Build call for dnsDomainNameRecordsGet
     * @param domainName The domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param skip The number of items to skip in the resultset. (optional)
     * @param take The number of items to return in the resultset. The returned count can be equal or less than this number. (optional)
     * @param type Filters records matching the type. Most other filters only apply when this filter is specified. (optional)
     * @param recordName Filters records matching the record name. This filter only applies to lookups of A, CNAME, TXT, CAA, ALIAS and TLSA records. (optional)
     * @param service Filters records for the service. This filter only applies to lookups of SRV records. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call dnsDomainNameRecordsGetCall(String domainName, String domainName2, Integer skip, Integer take, String type, String recordName, String service, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/dns/{domainName}/records"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
        }

        if (skip != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("skip", skip));
        }

        if (take != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("take", take));
        }

        if (type != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("type", type));
        }

        if (recordName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("record_name", recordName));
        }

        if (service != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("service", service));
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
    private okhttp3.Call dnsDomainNameRecordsGetValidateBeforeCall(String domainName, String domainName2, Integer skip, Integer take, String type, String recordName, String service, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling dnsDomainNameRecordsGet(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling dnsDomainNameRecordsGet(Async)");
        }

        return dnsDomainNameRecordsGetCall(domainName, domainName2, skip, take, type, recordName, service, _callback);

    }

    /**
     * Get records
     * 
     * @param domainName The domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param skip The number of items to skip in the resultset. (optional)
     * @param take The number of items to return in the resultset. The returned count can be equal or less than this number. (optional)
     * @param type Filters records matching the type. Most other filters only apply when this filter is specified. (optional)
     * @param recordName Filters records matching the record name. This filter only applies to lookups of A, CNAME, TXT, CAA, ALIAS and TLSA records. (optional)
     * @param service Filters records for the service. This filter only applies to lookups of SRV records. (optional)
     * @return List&lt;DnsRecord&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  </td></tr>
     </table>
     */
    public List<DnsRecord> dnsDomainNameRecordsGet(String domainName, String domainName2, Integer skip, Integer take, String type, String recordName, String service) throws ApiException {
        ApiResponse<List<DnsRecord>> localVarResp = dnsDomainNameRecordsGetWithHttpInfo(domainName, domainName2, skip, take, type, recordName, service);
        return localVarResp.getData();
    }

    /**
     * Get records
     * 
     * @param domainName The domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param skip The number of items to skip in the resultset. (optional)
     * @param take The number of items to return in the resultset. The returned count can be equal or less than this number. (optional)
     * @param type Filters records matching the type. Most other filters only apply when this filter is specified. (optional)
     * @param recordName Filters records matching the record name. This filter only applies to lookups of A, CNAME, TXT, CAA, ALIAS and TLSA records. (optional)
     * @param service Filters records for the service. This filter only applies to lookups of SRV records. (optional)
     * @return ApiResponse&lt;List&lt;DnsRecord&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  </td></tr>
     </table>
     */
    public ApiResponse<List<DnsRecord>> dnsDomainNameRecordsGetWithHttpInfo(String domainName, String domainName2, Integer skip, Integer take, String type, String recordName, String service) throws ApiException {
        okhttp3.Call localVarCall = dnsDomainNameRecordsGetValidateBeforeCall(domainName, domainName2, skip, take, type, recordName, service, null);
        Type localVarReturnType = new TypeToken<List<DnsRecord>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get records (asynchronously)
     * 
     * @param domainName The domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param skip The number of items to skip in the resultset. (optional)
     * @param take The number of items to return in the resultset. The returned count can be equal or less than this number. (optional)
     * @param type Filters records matching the type. Most other filters only apply when this filter is specified. (optional)
     * @param recordName Filters records matching the record name. This filter only applies to lookups of A, CNAME, TXT, CAA, ALIAS and TLSA records. (optional)
     * @param service Filters records for the service. This filter only applies to lookups of SRV records. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call dnsDomainNameRecordsGetAsync(String domainName, String domainName2, Integer skip, Integer take, String type, String recordName, String service, final ApiCallback<List<DnsRecord>> _callback) throws ApiException {

        okhttp3.Call localVarCall = dnsDomainNameRecordsGetValidateBeforeCall(domainName, domainName2, skip, take, type, recordName, service, _callback);
        Type localVarReturnType = new TypeToken<List<DnsRecord>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for dnsDomainNameRecordsPost
     * @param domainName The domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param dnsRecord The record to create (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call dnsDomainNameRecordsPostCall(String domainName, String domainName2, DnsRecord dnsRecord, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = dnsRecord;

        // create path and map variables
        String localVarPath = "/dns/{domainName}/records"
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
    private okhttp3.Call dnsDomainNameRecordsPostValidateBeforeCall(String domainName, String domainName2, DnsRecord dnsRecord, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling dnsDomainNameRecordsPost(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling dnsDomainNameRecordsPost(Async)");
        }

        return dnsDomainNameRecordsPostCall(domainName, domainName2, dnsRecord, _callback);

    }

    /**
     * Create a record
     * 
     * @param domainName The domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param dnsRecord The record to create (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public void dnsDomainNameRecordsPost(String domainName, String domainName2, DnsRecord dnsRecord) throws ApiException {
        dnsDomainNameRecordsPostWithHttpInfo(domainName, domainName2, dnsRecord);
    }

    /**
     * Create a record
     * 
     * @param domainName The domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param dnsRecord The record to create (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public ApiResponse<Void> dnsDomainNameRecordsPostWithHttpInfo(String domainName, String domainName2, DnsRecord dnsRecord) throws ApiException {
        okhttp3.Call localVarCall = dnsDomainNameRecordsPostValidateBeforeCall(domainName, domainName2, dnsRecord, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Create a record (asynchronously)
     * 
     * @param domainName The domain name. (required)
     * @param domainName2 Automatically added (required)
     * @param dnsRecord The record to create (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Success </td><td>  * Location - The location referring to a resource that replaced the original resource. <br>  </td></tr>
     </table>
     */
    public okhttp3.Call dnsDomainNameRecordsPostAsync(String domainName, String domainName2, DnsRecord dnsRecord, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = dnsDomainNameRecordsPostValidateBeforeCall(domainName, domainName2, dnsRecord, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for dnsDomainNameRecordsRecordIdDelete
     * @param domainName The domain name. (required)
     * @param recordId The id of the record. (required)
     * @param domainName2 Automatically added (required)
     * @param recordId2 Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call dnsDomainNameRecordsRecordIdDeleteCall(String domainName, String recordId, String domainName2, String recordId2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/dns/{domainName}/records/{recordId}"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()))
            .replace("{" + "recordId" + "}", localVarApiClient.escapeString(recordId2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
        }

        if (recordId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("record_id", recordId));
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
    private okhttp3.Call dnsDomainNameRecordsRecordIdDeleteValidateBeforeCall(String domainName, String recordId, String domainName2, String recordId2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling dnsDomainNameRecordsRecordIdDelete(Async)");
        }

        // verify the required parameter 'recordId' is set
        if (recordId == null) {
            throw new ApiException("Missing the required parameter 'recordId' when calling dnsDomainNameRecordsRecordIdDelete(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling dnsDomainNameRecordsRecordIdDelete(Async)");
        }

        // verify the required parameter 'recordId2' is set
        if (recordId2 == null) {
            throw new ApiException("Missing the required parameter 'recordId2' when calling dnsDomainNameRecordsRecordIdDelete(Async)");
        }

        return dnsDomainNameRecordsRecordIdDeleteCall(domainName, recordId, domainName2, recordId2, _callback);

    }

    /**
     * Delete a record
     * 
     * @param domainName The domain name. (required)
     * @param recordId The id of the record. (required)
     * @param domainName2 Automatically added (required)
     * @param recordId2 Automatically added (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void dnsDomainNameRecordsRecordIdDelete(String domainName, String recordId, String domainName2, String recordId2) throws ApiException {
        dnsDomainNameRecordsRecordIdDeleteWithHttpInfo(domainName, recordId, domainName2, recordId2);
    }

    /**
     * Delete a record
     * 
     * @param domainName The domain name. (required)
     * @param recordId The id of the record. (required)
     * @param domainName2 Automatically added (required)
     * @param recordId2 Automatically added (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> dnsDomainNameRecordsRecordIdDeleteWithHttpInfo(String domainName, String recordId, String domainName2, String recordId2) throws ApiException {
        okhttp3.Call localVarCall = dnsDomainNameRecordsRecordIdDeleteValidateBeforeCall(domainName, recordId, domainName2, recordId2, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a record (asynchronously)
     * 
     * @param domainName The domain name. (required)
     * @param recordId The id of the record. (required)
     * @param domainName2 Automatically added (required)
     * @param recordId2 Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call dnsDomainNameRecordsRecordIdDeleteAsync(String domainName, String recordId, String domainName2, String recordId2, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = dnsDomainNameRecordsRecordIdDeleteValidateBeforeCall(domainName, recordId, domainName2, recordId2, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for dnsDomainNameRecordsRecordIdGet
     * @param domainName The domain name. (required)
     * @param recordId The id of the record. (required)
     * @param domainName2 Automatically added (required)
     * @param recordId2 Automatically added (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call dnsDomainNameRecordsRecordIdGetCall(String domainName, String recordId, String domainName2, String recordId2, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/dns/{domainName}/records/{recordId}"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()))
            .replace("{" + "recordId" + "}", localVarApiClient.escapeString(recordId2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
        }

        if (recordId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("record_id", recordId));
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
    private okhttp3.Call dnsDomainNameRecordsRecordIdGetValidateBeforeCall(String domainName, String recordId, String domainName2, String recordId2, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling dnsDomainNameRecordsRecordIdGet(Async)");
        }

        // verify the required parameter 'recordId' is set
        if (recordId == null) {
            throw new ApiException("Missing the required parameter 'recordId' when calling dnsDomainNameRecordsRecordIdGet(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling dnsDomainNameRecordsRecordIdGet(Async)");
        }

        // verify the required parameter 'recordId2' is set
        if (recordId2 == null) {
            throw new ApiException("Missing the required parameter 'recordId2' when calling dnsDomainNameRecordsRecordIdGet(Async)");
        }

        return dnsDomainNameRecordsRecordIdGetCall(domainName, recordId, domainName2, recordId2, _callback);

    }

    /**
     * Get specific record
     * 
     * @param domainName The domain name. (required)
     * @param recordId The id of the record. (required)
     * @param domainName2 Automatically added (required)
     * @param recordId2 Automatically added (required)
     * @return DnsRecord
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public DnsRecord dnsDomainNameRecordsRecordIdGet(String domainName, String recordId, String domainName2, String recordId2) throws ApiException {
        ApiResponse<DnsRecord> localVarResp = dnsDomainNameRecordsRecordIdGetWithHttpInfo(domainName, recordId, domainName2, recordId2);
        return localVarResp.getData();
    }

    /**
     * Get specific record
     * 
     * @param domainName The domain name. (required)
     * @param recordId The id of the record. (required)
     * @param domainName2 Automatically added (required)
     * @param recordId2 Automatically added (required)
     * @return ApiResponse&lt;DnsRecord&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DnsRecord> dnsDomainNameRecordsRecordIdGetWithHttpInfo(String domainName, String recordId, String domainName2, String recordId2) throws ApiException {
        okhttp3.Call localVarCall = dnsDomainNameRecordsRecordIdGetValidateBeforeCall(domainName, recordId, domainName2, recordId2, null);
        Type localVarReturnType = new TypeToken<DnsRecord>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get specific record (asynchronously)
     * 
     * @param domainName The domain name. (required)
     * @param recordId The id of the record. (required)
     * @param domainName2 Automatically added (required)
     * @param recordId2 Automatically added (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call dnsDomainNameRecordsRecordIdGetAsync(String domainName, String recordId, String domainName2, String recordId2, final ApiCallback<DnsRecord> _callback) throws ApiException {

        okhttp3.Call localVarCall = dnsDomainNameRecordsRecordIdGetValidateBeforeCall(domainName, recordId, domainName2, recordId2, _callback);
        Type localVarReturnType = new TypeToken<DnsRecord>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for dnsDomainNameRecordsRecordIdPut
     * @param domainName The domain name. (required)
     * @param recordId The id of the record. (required)
     * @param domainName2 Automatically added (required)
     * @param recordId2 Automatically added (required)
     * @param dnsRecord The record with updated values. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call dnsDomainNameRecordsRecordIdPutCall(String domainName, String recordId, String domainName2, String recordId2, DnsRecord dnsRecord, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = dnsRecord;

        // create path and map variables
        String localVarPath = "/dns/{domainName}/records/{recordId}"
            .replace("{" + "domainName" + "}", localVarApiClient.escapeString(domainName2.toString()))
            .replace("{" + "recordId" + "}", localVarApiClient.escapeString(recordId2.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (domainName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("domain_name", domainName));
        }

        if (recordId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("record_id", recordId));
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
    private okhttp3.Call dnsDomainNameRecordsRecordIdPutValidateBeforeCall(String domainName, String recordId, String domainName2, String recordId2, DnsRecord dnsRecord, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'domainName' is set
        if (domainName == null) {
            throw new ApiException("Missing the required parameter 'domainName' when calling dnsDomainNameRecordsRecordIdPut(Async)");
        }

        // verify the required parameter 'recordId' is set
        if (recordId == null) {
            throw new ApiException("Missing the required parameter 'recordId' when calling dnsDomainNameRecordsRecordIdPut(Async)");
        }

        // verify the required parameter 'domainName2' is set
        if (domainName2 == null) {
            throw new ApiException("Missing the required parameter 'domainName2' when calling dnsDomainNameRecordsRecordIdPut(Async)");
        }

        // verify the required parameter 'recordId2' is set
        if (recordId2 == null) {
            throw new ApiException("Missing the required parameter 'recordId2' when calling dnsDomainNameRecordsRecordIdPut(Async)");
        }

        return dnsDomainNameRecordsRecordIdPutCall(domainName, recordId, domainName2, recordId2, dnsRecord, _callback);

    }

    /**
     * Edit a record
     * 
     * @param domainName The domain name. (required)
     * @param recordId The id of the record. (required)
     * @param domainName2 Automatically added (required)
     * @param recordId2 Automatically added (required)
     * @param dnsRecord The record with updated values. (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public void dnsDomainNameRecordsRecordIdPut(String domainName, String recordId, String domainName2, String recordId2, DnsRecord dnsRecord) throws ApiException {
        dnsDomainNameRecordsRecordIdPutWithHttpInfo(domainName, recordId, domainName2, recordId2, dnsRecord);
    }

    /**
     * Edit a record
     * 
     * @param domainName The domain name. (required)
     * @param recordId The id of the record. (required)
     * @param domainName2 Automatically added (required)
     * @param recordId2 Automatically added (required)
     * @param dnsRecord The record with updated values. (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> dnsDomainNameRecordsRecordIdPutWithHttpInfo(String domainName, String recordId, String domainName2, String recordId2, DnsRecord dnsRecord) throws ApiException {
        okhttp3.Call localVarCall = dnsDomainNameRecordsRecordIdPutValidateBeforeCall(domainName, recordId, domainName2, recordId2, dnsRecord, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Edit a record (asynchronously)
     * 
     * @param domainName The domain name. (required)
     * @param recordId The id of the record. (required)
     * @param domainName2 Automatically added (required)
     * @param recordId2 Automatically added (required)
     * @param dnsRecord The record with updated values. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call dnsDomainNameRecordsRecordIdPutAsync(String domainName, String recordId, String domainName2, String recordId2, DnsRecord dnsRecord, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = dnsDomainNameRecordsRecordIdPutValidateBeforeCall(domainName, recordId, domainName2, recordId2, dnsRecord, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
