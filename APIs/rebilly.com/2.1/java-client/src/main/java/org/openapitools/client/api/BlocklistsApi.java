/*
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
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


import org.openapitools.client.model.Blocklist;
import org.openapitools.client.model.Error;
import org.openapitools.client.model.InvalidError;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BlocklistsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public BlocklistsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public BlocklistsApi(ApiClient apiClient) {
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
     * Build call for deleteBlocklist
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Blocklist was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteBlocklistCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/blocklists/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteBlocklistValidateBeforeCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling deleteBlocklist(Async)");
        }

        return deleteBlocklistCall(id, organizationId, _callback);

    }

    /**
     * Delete a blocklist
     * Delete a blocklist with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Blocklist was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public void deleteBlocklist(String id, String organizationId) throws ApiException {
        deleteBlocklistWithHttpInfo(id, organizationId);
    }

    /**
     * Delete a blocklist
     * Delete a blocklist with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Blocklist was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteBlocklistWithHttpInfo(String id, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = deleteBlocklistValidateBeforeCall(id, organizationId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a blocklist (asynchronously)
     * Delete a blocklist with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Blocklist was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteBlocklistAsync(String id, String organizationId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteBlocklistValidateBeforeCall(id, organizationId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getBlocklist
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Blocklist was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBlocklistCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/blocklists/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getBlocklistValidateBeforeCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getBlocklist(Async)");
        }

        return getBlocklistCall(id, organizationId, _callback);

    }

    /**
     * Retrieve a blocklist
     * Retrieve a blocklist with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Blocklist
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Blocklist was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public Blocklist getBlocklist(String id, String organizationId) throws ApiException {
        ApiResponse<Blocklist> localVarResp = getBlocklistWithHttpInfo(id, organizationId);
        return localVarResp.getData();
    }

    /**
     * Retrieve a blocklist
     * Retrieve a blocklist with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Blocklist&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Blocklist was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Blocklist> getBlocklistWithHttpInfo(String id, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = getBlocklistValidateBeforeCall(id, organizationId, null);
        Type localVarReturnType = new TypeToken<Blocklist>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a blocklist (asynchronously)
     * Retrieve a blocklist with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Blocklist was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBlocklistAsync(String id, String organizationId, final ApiCallback<Blocklist> _callback) throws ApiException {

        okhttp3.Call localVarCall = getBlocklistValidateBeforeCall(id, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Blocklist>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getBlocklistCollection
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param q The partial search of the text fields. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Blocklists was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBlocklistCollectionCall(String organizationId, Integer limit, Integer offset, List<String> sort, String filter, String q, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/blocklists";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
        }

        if (sort != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("csv", "sort", sort));
        }

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter", filter));
        }

        if (q != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("q", q));
        }

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getBlocklistCollectionValidateBeforeCall(String organizationId, Integer limit, Integer offset, List<String> sort, String filter, String q, final ApiCallback _callback) throws ApiException {
        return getBlocklistCollectionCall(organizationId, limit, offset, sort, filter, q, _callback);

    }

    /**
     * Retrieve a list of blocklists
     * Retrieve a list of blocklists. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param q The partial search of the text fields. (optional)
     * @return List&lt;Blocklist&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Blocklists was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public List<Blocklist> getBlocklistCollection(String organizationId, Integer limit, Integer offset, List<String> sort, String filter, String q) throws ApiException {
        ApiResponse<List<Blocklist>> localVarResp = getBlocklistCollectionWithHttpInfo(organizationId, limit, offset, sort, filter, q);
        return localVarResp.getData();
    }

    /**
     * Retrieve a list of blocklists
     * Retrieve a list of blocklists. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param q The partial search of the text fields. (optional)
     * @return ApiResponse&lt;List&lt;Blocklist&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Blocklists was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Blocklist>> getBlocklistCollectionWithHttpInfo(String organizationId, Integer limit, Integer offset, List<String> sort, String filter, String q) throws ApiException {
        okhttp3.Call localVarCall = getBlocklistCollectionValidateBeforeCall(organizationId, limit, offset, sort, filter, q, null);
        Type localVarReturnType = new TypeToken<List<Blocklist>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a list of blocklists (asynchronously)
     * Retrieve a list of blocklists. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param q The partial search of the text fields. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of Blocklists was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getBlocklistCollectionAsync(String organizationId, Integer limit, Integer offset, List<String> sort, String filter, String q, final ApiCallback<List<Blocklist>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getBlocklistCollectionValidateBeforeCall(organizationId, limit, offset, sort, filter, q, _callback);
        Type localVarReturnType = new TypeToken<List<Blocklist>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postBlocklist
     * @param blocklist Blocklist resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Blocklist was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postBlocklistCall(Blocklist blocklist, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = blocklist;

        // create path and map variables
        String localVarPath = "/blocklists";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postBlocklistValidateBeforeCall(Blocklist blocklist, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'blocklist' is set
        if (blocklist == null) {
            throw new ApiException("Missing the required parameter 'blocklist' when calling postBlocklist(Async)");
        }

        return postBlocklistCall(blocklist, organizationId, _callback);

    }

    /**
     * Create a blocklist
     * Create a blocklist. 
     * @param blocklist Blocklist resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Blocklist
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Blocklist was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public Blocklist postBlocklist(Blocklist blocklist, String organizationId) throws ApiException {
        ApiResponse<Blocklist> localVarResp = postBlocklistWithHttpInfo(blocklist, organizationId);
        return localVarResp.getData();
    }

    /**
     * Create a blocklist
     * Create a blocklist. 
     * @param blocklist Blocklist resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Blocklist&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Blocklist was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Blocklist> postBlocklistWithHttpInfo(Blocklist blocklist, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postBlocklistValidateBeforeCall(blocklist, organizationId, null);
        Type localVarReturnType = new TypeToken<Blocklist>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a blocklist (asynchronously)
     * Create a blocklist. 
     * @param blocklist Blocklist resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Blocklist was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postBlocklistAsync(Blocklist blocklist, String organizationId, final ApiCallback<Blocklist> _callback) throws ApiException {

        okhttp3.Call localVarCall = postBlocklistValidateBeforeCall(blocklist, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Blocklist>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putBlocklist
     * @param id The resource identifier string. (required)
     * @param blocklist Blocklist resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Blocklist was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Blocklist exist and cannot be updated. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putBlocklistCall(String id, Blocklist blocklist, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = blocklist;

        // create path and map variables
        String localVarPath = "/blocklists/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
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

        String[] localVarAuthNames = new String[] { "SecretApiKey", "JWT" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putBlocklistValidateBeforeCall(String id, Blocklist blocklist, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling putBlocklist(Async)");
        }

        // verify the required parameter 'blocklist' is set
        if (blocklist == null) {
            throw new ApiException("Missing the required parameter 'blocklist' when calling putBlocklist(Async)");
        }

        return putBlocklistCall(id, blocklist, organizationId, _callback);

    }

    /**
     * Create a blocklist with predefined ID
     * Create a blocklist with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param blocklist Blocklist resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Blocklist
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Blocklist was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Blocklist exist and cannot be updated. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public Blocklist putBlocklist(String id, Blocklist blocklist, String organizationId) throws ApiException {
        ApiResponse<Blocklist> localVarResp = putBlocklistWithHttpInfo(id, blocklist, organizationId);
        return localVarResp.getData();
    }

    /**
     * Create a blocklist with predefined ID
     * Create a blocklist with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param blocklist Blocklist resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Blocklist&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Blocklist was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Blocklist exist and cannot be updated. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Blocklist> putBlocklistWithHttpInfo(String id, Blocklist blocklist, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = putBlocklistValidateBeforeCall(id, blocklist, organizationId, null);
        Type localVarReturnType = new TypeToken<Blocklist>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a blocklist with predefined ID (asynchronously)
     * Create a blocklist with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param blocklist Blocklist resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Blocklist was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Blocklist exist and cannot be updated. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putBlocklistAsync(String id, Blocklist blocklist, String organizationId, final ApiCallback<Blocklist> _callback) throws ApiException {

        okhttp3.Call localVarCall = putBlocklistValidateBeforeCall(id, blocklist, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Blocklist>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
