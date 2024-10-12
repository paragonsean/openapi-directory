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


import org.openapitools.client.model.Error;
import org.openapitools.client.model.InvalidError;
import org.openapitools.client.model.Invoice;
import org.openapitools.client.model.InvoiceIssue;
import org.openapitools.client.model.InvoiceItem;
import org.openapitools.client.model.InvoiceReissue;
import org.openapitools.client.model.InvoiceTimeline;
import org.openapitools.client.model.InvoiceTransaction;
import org.openapitools.client.model.InvoiceTransactionAllocation;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class InvoicesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public InvoicesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public InvoicesApi(ApiClient apiClient) {
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
     * Build call for deleteInvoiceTimeline
     * @param id The resource identifier string. (required)
     * @param messageId The Invoice Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Invoice Timeline message was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteInvoiceTimelineCall(String id, String messageId, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/invoices/{id}/timeline/{messageId}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "messageId" + "}", localVarApiClient.escapeString(messageId.toString()));

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
    private okhttp3.Call deleteInvoiceTimelineValidateBeforeCall(String id, String messageId, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling deleteInvoiceTimeline(Async)");
        }

        // verify the required parameter 'messageId' is set
        if (messageId == null) {
            throw new ApiException("Missing the required parameter 'messageId' when calling deleteInvoiceTimeline(Async)");
        }

        return deleteInvoiceTimelineCall(id, messageId, organizationId, _callback);

    }

    /**
     * Delete an Invoice Timeline message
     * Delete an Invoice Timeline message with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param messageId The Invoice Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Invoice Timeline message was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public void deleteInvoiceTimeline(String id, String messageId, String organizationId) throws ApiException {
        deleteInvoiceTimelineWithHttpInfo(id, messageId, organizationId);
    }

    /**
     * Delete an Invoice Timeline message
     * Delete an Invoice Timeline message with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param messageId The Invoice Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Invoice Timeline message was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteInvoiceTimelineWithHttpInfo(String id, String messageId, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = deleteInvoiceTimelineValidateBeforeCall(id, messageId, organizationId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete an Invoice Timeline message (asynchronously)
     * Delete an Invoice Timeline message with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param messageId The Invoice Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Invoice Timeline message was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteInvoiceTimelineAsync(String id, String messageId, String organizationId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteInvoiceTimelineValidateBeforeCall(id, messageId, organizationId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getCustomerUpcomingInvoiceCollection
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Upcoming invoices are retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCustomerUpcomingInvoiceCollectionCall(String id, String organizationId, String expand, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/customers/{id}/upcoming-invoices"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (expand != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("expand", expand));
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
    private okhttp3.Call getCustomerUpcomingInvoiceCollectionValidateBeforeCall(String id, String organizationId, String expand, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getCustomerUpcomingInvoiceCollection(Async)");
        }

        return getCustomerUpcomingInvoiceCollectionCall(id, organizationId, expand, _callback);

    }

    /**
     * Retrieve customer&#39;s upcoming invoices
     * Retrieve a list of upcoming invoices from the subscriptions which belong to. the given customer. The endpoint is temporary before upcoming invoices get a complete integration. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return List&lt;Invoice&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Upcoming invoices are retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public List<Invoice> getCustomerUpcomingInvoiceCollection(String id, String organizationId, String expand) throws ApiException {
        ApiResponse<List<Invoice>> localVarResp = getCustomerUpcomingInvoiceCollectionWithHttpInfo(id, organizationId, expand);
        return localVarResp.getData();
    }

    /**
     * Retrieve customer&#39;s upcoming invoices
     * Retrieve a list of upcoming invoices from the subscriptions which belong to. the given customer. The endpoint is temporary before upcoming invoices get a complete integration. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return ApiResponse&lt;List&lt;Invoice&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Upcoming invoices are retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Invoice>> getCustomerUpcomingInvoiceCollectionWithHttpInfo(String id, String organizationId, String expand) throws ApiException {
        okhttp3.Call localVarCall = getCustomerUpcomingInvoiceCollectionValidateBeforeCall(id, organizationId, expand, null);
        Type localVarReturnType = new TypeToken<List<Invoice>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve customer&#39;s upcoming invoices (asynchronously)
     * Retrieve a list of upcoming invoices from the subscriptions which belong to. the given customer. The endpoint is temporary before upcoming invoices get a complete integration. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Upcoming invoices are retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getCustomerUpcomingInvoiceCollectionAsync(String id, String organizationId, String expand, final ApiCallback<List<Invoice>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getCustomerUpcomingInvoiceCollectionValidateBeforeCall(id, organizationId, expand, _callback);
        Type localVarReturnType = new TypeToken<List<Invoice>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getInvoice
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param accept The response media type. (optional, default to application/json)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceCall(String id, String organizationId, String accept, String expand, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/invoices/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (expand != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("expand", expand));
        }

        if (organizationId != null) {
            localVarHeaderParams.put("Organization-Id", localVarApiClient.parameterToString(organizationId));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        final String[] localVarAccepts = {
            "application/json",
            "application/pdf"
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
    private okhttp3.Call getInvoiceValidateBeforeCall(String id, String organizationId, String accept, String expand, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getInvoice(Async)");
        }

        return getInvoiceCall(id, organizationId, accept, expand, _callback);

    }

    /**
     * Retrieve an invoice
     * Retrieve an invoice with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param accept The response media type. (optional, default to application/json)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return Invoice
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public Invoice getInvoice(String id, String organizationId, String accept, String expand) throws ApiException {
        ApiResponse<Invoice> localVarResp = getInvoiceWithHttpInfo(id, organizationId, accept, expand);
        return localVarResp.getData();
    }

    /**
     * Retrieve an invoice
     * Retrieve an invoice with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param accept The response media type. (optional, default to application/json)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return ApiResponse&lt;Invoice&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Invoice> getInvoiceWithHttpInfo(String id, String organizationId, String accept, String expand) throws ApiException {
        okhttp3.Call localVarCall = getInvoiceValidateBeforeCall(id, organizationId, accept, expand, null);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve an invoice (asynchronously)
     * Retrieve an invoice with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param accept The response media type. (optional, default to application/json)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceAsync(String id, String organizationId, String accept, String expand, final ApiCallback<Invoice> _callback) throws ApiException {

        okhttp3.Call localVarCall = getInvoiceValidateBeforeCall(id, organizationId, accept, expand, _callback);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getInvoiceCollection
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of invoices was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceCollectionCall(String organizationId, String filter, List<String> sort, Integer limit, Integer offset, String q, String expand, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/invoices";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter", filter));
        }

        if (sort != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("csv", "sort", sort));
        }

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
        }

        if (q != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("q", q));
        }

        if (expand != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("expand", expand));
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
    private okhttp3.Call getInvoiceCollectionValidateBeforeCall(String organizationId, String filter, List<String> sort, Integer limit, Integer offset, String q, String expand, final ApiCallback _callback) throws ApiException {
        return getInvoiceCollectionCall(organizationId, filter, sort, limit, offset, q, expand, _callback);

    }

    /**
     * Retrieve a list of invoices
     * Retrieve a list of invoices. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return List&lt;Invoice&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of invoices was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public List<Invoice> getInvoiceCollection(String organizationId, String filter, List<String> sort, Integer limit, Integer offset, String q, String expand) throws ApiException {
        ApiResponse<List<Invoice>> localVarResp = getInvoiceCollectionWithHttpInfo(organizationId, filter, sort, limit, offset, q, expand);
        return localVarResp.getData();
    }

    /**
     * Retrieve a list of invoices
     * Retrieve a list of invoices. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return ApiResponse&lt;List&lt;Invoice&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of invoices was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Invoice>> getInvoiceCollectionWithHttpInfo(String organizationId, String filter, List<String> sort, Integer limit, Integer offset, String q, String expand) throws ApiException {
        okhttp3.Call localVarCall = getInvoiceCollectionValidateBeforeCall(organizationId, filter, sort, limit, offset, q, expand, null);
        Type localVarReturnType = new TypeToken<List<Invoice>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a list of invoices (asynchronously)
     * Retrieve a list of invoices. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of invoices was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceCollectionAsync(String organizationId, String filter, List<String> sort, Integer limit, Integer offset, String q, String expand, final ApiCallback<List<Invoice>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getInvoiceCollectionValidateBeforeCall(organizationId, filter, sort, limit, offset, q, expand, _callback);
        Type localVarReturnType = new TypeToken<List<Invoice>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getInvoiceItemCollection
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice items were retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceItemCollectionCall(String id, String organizationId, Integer limit, Integer offset, String expand, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/invoices/{id}/items"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        if (expand != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("expand", expand));
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
    private okhttp3.Call getInvoiceItemCollectionValidateBeforeCall(String id, String organizationId, Integer limit, Integer offset, String expand, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getInvoiceItemCollection(Async)");
        }

        return getInvoiceItemCollectionCall(id, organizationId, limit, offset, expand, _callback);

    }

    /**
     * Retrieve invoice items
     * Retrieve an invoice items with specified invoice identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return List&lt;InvoiceItem&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice items were retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public List<InvoiceItem> getInvoiceItemCollection(String id, String organizationId, Integer limit, Integer offset, String expand) throws ApiException {
        ApiResponse<List<InvoiceItem>> localVarResp = getInvoiceItemCollectionWithHttpInfo(id, organizationId, limit, offset, expand);
        return localVarResp.getData();
    }

    /**
     * Retrieve invoice items
     * Retrieve an invoice items with specified invoice identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return ApiResponse&lt;List&lt;InvoiceItem&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice items were retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<InvoiceItem>> getInvoiceItemCollectionWithHttpInfo(String id, String organizationId, Integer limit, Integer offset, String expand) throws ApiException {
        okhttp3.Call localVarCall = getInvoiceItemCollectionValidateBeforeCall(id, organizationId, limit, offset, expand, null);
        Type localVarReturnType = new TypeToken<List<InvoiceItem>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve invoice items (asynchronously)
     * Retrieve an invoice items with specified invoice identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice items were retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceItemCollectionAsync(String id, String organizationId, Integer limit, Integer offset, String expand, final ApiCallback<List<InvoiceItem>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getInvoiceItemCollectionValidateBeforeCall(id, organizationId, limit, offset, expand, _callback);
        Type localVarReturnType = new TypeToken<List<InvoiceItem>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getInvoiceTimeline
     * @param id The resource identifier string. (required)
     * @param messageId The Invoice Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice message was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceTimelineCall(String id, String messageId, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/invoices/{id}/timeline/{messageId}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "messageId" + "}", localVarApiClient.escapeString(messageId.toString()));

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
    private okhttp3.Call getInvoiceTimelineValidateBeforeCall(String id, String messageId, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getInvoiceTimeline(Async)");
        }

        // verify the required parameter 'messageId' is set
        if (messageId == null) {
            throw new ApiException("Missing the required parameter 'messageId' when calling getInvoiceTimeline(Async)");
        }

        return getInvoiceTimelineCall(id, messageId, organizationId, _callback);

    }

    /**
     * Retrieve an Invoice Timeline message
     * Retrieve a invoice message with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param messageId The Invoice Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return InvoiceTimeline
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice message was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public InvoiceTimeline getInvoiceTimeline(String id, String messageId, String organizationId) throws ApiException {
        ApiResponse<InvoiceTimeline> localVarResp = getInvoiceTimelineWithHttpInfo(id, messageId, organizationId);
        return localVarResp.getData();
    }

    /**
     * Retrieve an Invoice Timeline message
     * Retrieve a invoice message with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param messageId The Invoice Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;InvoiceTimeline&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice message was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<InvoiceTimeline> getInvoiceTimelineWithHttpInfo(String id, String messageId, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = getInvoiceTimelineValidateBeforeCall(id, messageId, organizationId, null);
        Type localVarReturnType = new TypeToken<InvoiceTimeline>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve an Invoice Timeline message (asynchronously)
     * Retrieve a invoice message with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param messageId The Invoice Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice message was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceTimelineAsync(String id, String messageId, String organizationId, final ApiCallback<InvoiceTimeline> _callback) throws ApiException {

        okhttp3.Call localVarCall = getInvoiceTimelineValidateBeforeCall(id, messageId, organizationId, _callback);
        Type localVarReturnType = new TypeToken<InvoiceTimeline>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getInvoiceTimelineCollection
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param q The partial search of the text fields. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of invoice timeline messages was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceTimelineCollectionCall(String id, String organizationId, Integer limit, Integer offset, String filter, List<String> sort, String q, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/invoices/{id}/timeline"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter", filter));
        }

        if (sort != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("csv", "sort", sort));
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
    private okhttp3.Call getInvoiceTimelineCollectionValidateBeforeCall(String id, String organizationId, Integer limit, Integer offset, String filter, List<String> sort, String q, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getInvoiceTimelineCollection(Async)");
        }

        return getInvoiceTimelineCollectionCall(id, organizationId, limit, offset, filter, sort, q, _callback);

    }

    /**
     * Retrieve a list of invoice timeline messages
     * Retrieve a list of invoice timeline messages. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param q The partial search of the text fields. (optional)
     * @return List&lt;InvoiceTimeline&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of invoice timeline messages was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public List<InvoiceTimeline> getInvoiceTimelineCollection(String id, String organizationId, Integer limit, Integer offset, String filter, List<String> sort, String q) throws ApiException {
        ApiResponse<List<InvoiceTimeline>> localVarResp = getInvoiceTimelineCollectionWithHttpInfo(id, organizationId, limit, offset, filter, sort, q);
        return localVarResp.getData();
    }

    /**
     * Retrieve a list of invoice timeline messages
     * Retrieve a list of invoice timeline messages. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param q The partial search of the text fields. (optional)
     * @return ApiResponse&lt;List&lt;InvoiceTimeline&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of invoice timeline messages was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<InvoiceTimeline>> getInvoiceTimelineCollectionWithHttpInfo(String id, String organizationId, Integer limit, Integer offset, String filter, List<String> sort, String q) throws ApiException {
        okhttp3.Call localVarCall = getInvoiceTimelineCollectionValidateBeforeCall(id, organizationId, limit, offset, filter, sort, q, null);
        Type localVarReturnType = new TypeToken<List<InvoiceTimeline>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a list of invoice timeline messages (asynchronously)
     * Retrieve a list of invoice timeline messages. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param q The partial search of the text fields. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of invoice timeline messages was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceTimelineCollectionAsync(String id, String organizationId, Integer limit, Integer offset, String filter, List<String> sort, String q, final ApiCallback<List<InvoiceTimeline>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getInvoiceTimelineCollectionValidateBeforeCall(id, organizationId, limit, offset, filter, sort, q, _callback);
        Type localVarReturnType = new TypeToken<List<InvoiceTimeline>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getInvoiceTransactionAllocationCollection
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of allocations was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceTransactionAllocationCollectionCall(String id, String organizationId, Integer limit, Integer offset, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/invoices/{id}/transaction-allocations"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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
    private okhttp3.Call getInvoiceTransactionAllocationCollectionValidateBeforeCall(String id, String organizationId, Integer limit, Integer offset, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getInvoiceTransactionAllocationCollection(Async)");
        }

        return getInvoiceTransactionAllocationCollectionCall(id, organizationId, limit, offset, _callback);

    }

    /**
     * Get transaction amounts allocated to an invoice
     * Get the precise amounts from a transaction allocated as invoice payments.
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @return List&lt;InvoiceTransactionAllocation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of allocations was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public List<InvoiceTransactionAllocation> getInvoiceTransactionAllocationCollection(String id, String organizationId, Integer limit, Integer offset) throws ApiException {
        ApiResponse<List<InvoiceTransactionAllocation>> localVarResp = getInvoiceTransactionAllocationCollectionWithHttpInfo(id, organizationId, limit, offset);
        return localVarResp.getData();
    }

    /**
     * Get transaction amounts allocated to an invoice
     * Get the precise amounts from a transaction allocated as invoice payments.
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @return ApiResponse&lt;List&lt;InvoiceTransactionAllocation&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of allocations was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<InvoiceTransactionAllocation>> getInvoiceTransactionAllocationCollectionWithHttpInfo(String id, String organizationId, Integer limit, Integer offset) throws ApiException {
        okhttp3.Call localVarCall = getInvoiceTransactionAllocationCollectionValidateBeforeCall(id, organizationId, limit, offset, null);
        Type localVarReturnType = new TypeToken<List<InvoiceTransactionAllocation>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get transaction amounts allocated to an invoice (asynchronously)
     * Get the precise amounts from a transaction allocated as invoice payments.
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of allocations was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getInvoiceTransactionAllocationCollectionAsync(String id, String organizationId, Integer limit, Integer offset, final ApiCallback<List<InvoiceTransactionAllocation>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getInvoiceTransactionAllocationCollectionValidateBeforeCall(id, organizationId, limit, offset, _callback);
        Type localVarReturnType = new TypeToken<List<InvoiceTransactionAllocation>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postInvoice
     * @param invoice Invoice resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceCall(Invoice invoice, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = invoice;

        // create path and map variables
        String localVarPath = "/invoices";

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
    private okhttp3.Call postInvoiceValidateBeforeCall(Invoice invoice, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'invoice' is set
        if (invoice == null) {
            throw new ApiException("Missing the required parameter 'invoice' when calling postInvoice(Async)");
        }

        return postInvoiceCall(invoice, organizationId, _callback);

    }

    /**
     * Create an invoice
     * Create an invoice. 
     * @param invoice Invoice resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Invoice
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public Invoice postInvoice(Invoice invoice, String organizationId) throws ApiException {
        ApiResponse<Invoice> localVarResp = postInvoiceWithHttpInfo(invoice, organizationId);
        return localVarResp.getData();
    }

    /**
     * Create an invoice
     * Create an invoice. 
     * @param invoice Invoice resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Invoice&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Invoice> postInvoiceWithHttpInfo(Invoice invoice, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postInvoiceValidateBeforeCall(invoice, organizationId, null);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create an invoice (asynchronously)
     * Create an invoice. 
     * @param invoice Invoice resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceAsync(Invoice invoice, String organizationId, final ApiCallback<Invoice> _callback) throws ApiException {

        okhttp3.Call localVarCall = postInvoiceValidateBeforeCall(invoice, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postInvoiceAbandonment
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was abandoned successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceAbandonmentCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/invoices/{id}/abandon"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postInvoiceAbandonmentValidateBeforeCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling postInvoiceAbandonment(Async)");
        }

        return postInvoiceAbandonmentCall(id, organizationId, _callback);

    }

    /**
     * Abandon an invoice
     * Abandon an invoice with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Invoice
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was abandoned successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public Invoice postInvoiceAbandonment(String id, String organizationId) throws ApiException {
        ApiResponse<Invoice> localVarResp = postInvoiceAbandonmentWithHttpInfo(id, organizationId);
        return localVarResp.getData();
    }

    /**
     * Abandon an invoice
     * Abandon an invoice with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Invoice&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was abandoned successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Invoice> postInvoiceAbandonmentWithHttpInfo(String id, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postInvoiceAbandonmentValidateBeforeCall(id, organizationId, null);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Abandon an invoice (asynchronously)
     * Abandon an invoice with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was abandoned successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceAbandonmentAsync(String id, String organizationId, final ApiCallback<Invoice> _callback) throws ApiException {

        okhttp3.Call localVarCall = postInvoiceAbandonmentValidateBeforeCall(id, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postInvoiceIssuance
     * @param id The resource identifier string. (required)
     * @param invoiceIssue InvoiceIssue resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was issued successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceIssuanceCall(String id, InvoiceIssue invoiceIssue, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = invoiceIssue;

        // create path and map variables
        String localVarPath = "/invoices/{id}/issue"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postInvoiceIssuanceValidateBeforeCall(String id, InvoiceIssue invoiceIssue, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling postInvoiceIssuance(Async)");
        }

        // verify the required parameter 'invoiceIssue' is set
        if (invoiceIssue == null) {
            throw new ApiException("Missing the required parameter 'invoiceIssue' when calling postInvoiceIssuance(Async)");
        }

        return postInvoiceIssuanceCall(id, invoiceIssue, organizationId, _callback);

    }

    /**
     * Issue an invoice
     * Issue an invoice with specified identifier string. It must be in &#x60;draft&#x60; status. 
     * @param id The resource identifier string. (required)
     * @param invoiceIssue InvoiceIssue resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Invoice
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was issued successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public Invoice postInvoiceIssuance(String id, InvoiceIssue invoiceIssue, String organizationId) throws ApiException {
        ApiResponse<Invoice> localVarResp = postInvoiceIssuanceWithHttpInfo(id, invoiceIssue, organizationId);
        return localVarResp.getData();
    }

    /**
     * Issue an invoice
     * Issue an invoice with specified identifier string. It must be in &#x60;draft&#x60; status. 
     * @param id The resource identifier string. (required)
     * @param invoiceIssue InvoiceIssue resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Invoice&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was issued successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Invoice> postInvoiceIssuanceWithHttpInfo(String id, InvoiceIssue invoiceIssue, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postInvoiceIssuanceValidateBeforeCall(id, invoiceIssue, organizationId, null);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Issue an invoice (asynchronously)
     * Issue an invoice with specified identifier string. It must be in &#x60;draft&#x60; status. 
     * @param id The resource identifier string. (required)
     * @param invoiceIssue InvoiceIssue resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was issued successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceIssuanceAsync(String id, InvoiceIssue invoiceIssue, String organizationId, final ApiCallback<Invoice> _callback) throws ApiException {

        okhttp3.Call localVarCall = postInvoiceIssuanceValidateBeforeCall(id, invoiceIssue, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postInvoiceItem
     * @param id The resource identifier string. (required)
     * @param invoiceItem InvoiceItem resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> InvoiceItem was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceItemCall(String id, InvoiceItem invoiceItem, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = invoiceItem;

        // create path and map variables
        String localVarPath = "/invoices/{id}/items"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postInvoiceItemValidateBeforeCall(String id, InvoiceItem invoiceItem, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling postInvoiceItem(Async)");
        }

        // verify the required parameter 'invoiceItem' is set
        if (invoiceItem == null) {
            throw new ApiException("Missing the required parameter 'invoiceItem' when calling postInvoiceItem(Async)");
        }

        return postInvoiceItemCall(id, invoiceItem, organizationId, _callback);

    }

    /**
     * Create an invoice item
     * Create an invoice item. 
     * @param id The resource identifier string. (required)
     * @param invoiceItem InvoiceItem resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return InvoiceItem
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> InvoiceItem was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public InvoiceItem postInvoiceItem(String id, InvoiceItem invoiceItem, String organizationId) throws ApiException {
        ApiResponse<InvoiceItem> localVarResp = postInvoiceItemWithHttpInfo(id, invoiceItem, organizationId);
        return localVarResp.getData();
    }

    /**
     * Create an invoice item
     * Create an invoice item. 
     * @param id The resource identifier string. (required)
     * @param invoiceItem InvoiceItem resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;InvoiceItem&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> InvoiceItem was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<InvoiceItem> postInvoiceItemWithHttpInfo(String id, InvoiceItem invoiceItem, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postInvoiceItemValidateBeforeCall(id, invoiceItem, organizationId, null);
        Type localVarReturnType = new TypeToken<InvoiceItem>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create an invoice item (asynchronously)
     * Create an invoice item. 
     * @param id The resource identifier string. (required)
     * @param invoiceItem InvoiceItem resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> InvoiceItem was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceItemAsync(String id, InvoiceItem invoiceItem, String organizationId, final ApiCallback<InvoiceItem> _callback) throws ApiException {

        okhttp3.Call localVarCall = postInvoiceItemValidateBeforeCall(id, invoiceItem, organizationId, _callback);
        Type localVarReturnType = new TypeToken<InvoiceItem>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postInvoiceRecalculation
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was recalculated successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceRecalculationCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/invoices/{id}/recalculate"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postInvoiceRecalculationValidateBeforeCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling postInvoiceRecalculation(Async)");
        }

        return postInvoiceRecalculationCall(id, organizationId, _callback);

    }

    /**
     * Recalculate an invoice
     * Recalculate an invoice with specified identifier string. It will recalculate shipping rates, taxes, discounts. It is useful when coupon was revoked or customer redeemed coupon after invoice was issued and you want to apply it to this invoice. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Invoice
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was recalculated successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public Invoice postInvoiceRecalculation(String id, String organizationId) throws ApiException {
        ApiResponse<Invoice> localVarResp = postInvoiceRecalculationWithHttpInfo(id, organizationId);
        return localVarResp.getData();
    }

    /**
     * Recalculate an invoice
     * Recalculate an invoice with specified identifier string. It will recalculate shipping rates, taxes, discounts. It is useful when coupon was revoked or customer redeemed coupon after invoice was issued and you want to apply it to this invoice. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Invoice&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was recalculated successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Invoice> postInvoiceRecalculationWithHttpInfo(String id, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postInvoiceRecalculationValidateBeforeCall(id, organizationId, null);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Recalculate an invoice (asynchronously)
     * Recalculate an invoice with specified identifier string. It will recalculate shipping rates, taxes, discounts. It is useful when coupon was revoked or customer redeemed coupon after invoice was issued and you want to apply it to this invoice. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was recalculated successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceRecalculationAsync(String id, String organizationId, final ApiCallback<Invoice> _callback) throws ApiException {

        okhttp3.Call localVarCall = postInvoiceRecalculationValidateBeforeCall(id, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postInvoiceReissuance
     * @param id The resource identifier string. (required)
     * @param invoiceReissue InvoiceReissue resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was reissued successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceReissuanceCall(String id, InvoiceReissue invoiceReissue, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = invoiceReissue;

        // create path and map variables
        String localVarPath = "/invoices/{id}/reissue"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postInvoiceReissuanceValidateBeforeCall(String id, InvoiceReissue invoiceReissue, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling postInvoiceReissuance(Async)");
        }

        // verify the required parameter 'invoiceReissue' is set
        if (invoiceReissue == null) {
            throw new ApiException("Missing the required parameter 'invoiceReissue' when calling postInvoiceReissuance(Async)");
        }

        return postInvoiceReissuanceCall(id, invoiceReissue, organizationId, _callback);

    }

    /**
     * Reissue an invoice
     * Reissue an invoice with specified identifier string. It must be issued. (status must be &#x60;unpaid&#x60; or &#x60;past-due&#x60;). 
     * @param id The resource identifier string. (required)
     * @param invoiceReissue InvoiceReissue resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Invoice
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was reissued successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public Invoice postInvoiceReissuance(String id, InvoiceReissue invoiceReissue, String organizationId) throws ApiException {
        ApiResponse<Invoice> localVarResp = postInvoiceReissuanceWithHttpInfo(id, invoiceReissue, organizationId);
        return localVarResp.getData();
    }

    /**
     * Reissue an invoice
     * Reissue an invoice with specified identifier string. It must be issued. (status must be &#x60;unpaid&#x60; or &#x60;past-due&#x60;). 
     * @param id The resource identifier string. (required)
     * @param invoiceReissue InvoiceReissue resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Invoice&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was reissued successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Invoice> postInvoiceReissuanceWithHttpInfo(String id, InvoiceReissue invoiceReissue, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postInvoiceReissuanceValidateBeforeCall(id, invoiceReissue, organizationId, null);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Reissue an invoice (asynchronously)
     * Reissue an invoice with specified identifier string. It must be issued. (status must be &#x60;unpaid&#x60; or &#x60;past-due&#x60;). 
     * @param id The resource identifier string. (required)
     * @param invoiceReissue InvoiceReissue resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was reissued successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceReissuanceAsync(String id, InvoiceReissue invoiceReissue, String organizationId, final ApiCallback<Invoice> _callback) throws ApiException {

        okhttp3.Call localVarCall = postInvoiceReissuanceValidateBeforeCall(id, invoiceReissue, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postInvoiceTimeline
     * @param id The resource identifier string. (required)
     * @param invoiceTimeline Invoice Timeline resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice Timeline comment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceTimelineCall(String id, InvoiceTimeline invoiceTimeline, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = invoiceTimeline;

        // create path and map variables
        String localVarPath = "/invoices/{id}/timeline"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postInvoiceTimelineValidateBeforeCall(String id, InvoiceTimeline invoiceTimeline, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling postInvoiceTimeline(Async)");
        }

        // verify the required parameter 'invoiceTimeline' is set
        if (invoiceTimeline == null) {
            throw new ApiException("Missing the required parameter 'invoiceTimeline' when calling postInvoiceTimeline(Async)");
        }

        return postInvoiceTimelineCall(id, invoiceTimeline, organizationId, _callback);

    }

    /**
     * Create an invoice Timeline comment
     * Create an invoice Timeline comment. 
     * @param id The resource identifier string. (required)
     * @param invoiceTimeline Invoice Timeline resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return InvoiceTimeline
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice Timeline comment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public InvoiceTimeline postInvoiceTimeline(String id, InvoiceTimeline invoiceTimeline, String organizationId) throws ApiException {
        ApiResponse<InvoiceTimeline> localVarResp = postInvoiceTimelineWithHttpInfo(id, invoiceTimeline, organizationId);
        return localVarResp.getData();
    }

    /**
     * Create an invoice Timeline comment
     * Create an invoice Timeline comment. 
     * @param id The resource identifier string. (required)
     * @param invoiceTimeline Invoice Timeline resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;InvoiceTimeline&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice Timeline comment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<InvoiceTimeline> postInvoiceTimelineWithHttpInfo(String id, InvoiceTimeline invoiceTimeline, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postInvoiceTimelineValidateBeforeCall(id, invoiceTimeline, organizationId, null);
        Type localVarReturnType = new TypeToken<InvoiceTimeline>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create an invoice Timeline comment (asynchronously)
     * Create an invoice Timeline comment. 
     * @param id The resource identifier string. (required)
     * @param invoiceTimeline Invoice Timeline resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice Timeline comment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceTimelineAsync(String id, InvoiceTimeline invoiceTimeline, String organizationId, final ApiCallback<InvoiceTimeline> _callback) throws ApiException {

        okhttp3.Call localVarCall = postInvoiceTimelineValidateBeforeCall(id, invoiceTimeline, organizationId, _callback);
        Type localVarReturnType = new TypeToken<InvoiceTimeline>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postInvoiceTransaction
     * @param id The resource identifier string. (required)
     * @param invoiceTransaction InvoiceTransaction resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Transaction was applied to invoice successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceTransactionCall(String id, InvoiceTransaction invoiceTransaction, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = invoiceTransaction;

        // create path and map variables
        String localVarPath = "/invoices/{id}/transaction"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postInvoiceTransactionValidateBeforeCall(String id, InvoiceTransaction invoiceTransaction, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling postInvoiceTransaction(Async)");
        }

        // verify the required parameter 'invoiceTransaction' is set
        if (invoiceTransaction == null) {
            throw new ApiException("Missing the required parameter 'invoiceTransaction' when calling postInvoiceTransaction(Async)");
        }

        return postInvoiceTransactionCall(id, invoiceTransaction, organizationId, _callback);

    }

    /**
     * Apply a transaction to an invoice
     * Apply a transaction to an invoice. The invoice must be unpaid. The transaction must have a non-zero unused amount (not fully applied to other invoices). 
     * @param id The resource identifier string. (required)
     * @param invoiceTransaction InvoiceTransaction resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Invoice
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Transaction was applied to invoice successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public Invoice postInvoiceTransaction(String id, InvoiceTransaction invoiceTransaction, String organizationId) throws ApiException {
        ApiResponse<Invoice> localVarResp = postInvoiceTransactionWithHttpInfo(id, invoiceTransaction, organizationId);
        return localVarResp.getData();
    }

    /**
     * Apply a transaction to an invoice
     * Apply a transaction to an invoice. The invoice must be unpaid. The transaction must have a non-zero unused amount (not fully applied to other invoices). 
     * @param id The resource identifier string. (required)
     * @param invoiceTransaction InvoiceTransaction resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Invoice&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Transaction was applied to invoice successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Invoice> postInvoiceTransactionWithHttpInfo(String id, InvoiceTransaction invoiceTransaction, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postInvoiceTransactionValidateBeforeCall(id, invoiceTransaction, organizationId, null);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Apply a transaction to an invoice (asynchronously)
     * Apply a transaction to an invoice. The invoice must be unpaid. The transaction must have a non-zero unused amount (not fully applied to other invoices). 
     * @param id The resource identifier string. (required)
     * @param invoiceTransaction InvoiceTransaction resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Transaction was applied to invoice successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceTransactionAsync(String id, InvoiceTransaction invoiceTransaction, String organizationId, final ApiCallback<Invoice> _callback) throws ApiException {

        okhttp3.Call localVarCall = postInvoiceTransactionValidateBeforeCall(id, invoiceTransaction, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postInvoiceVoid
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was voided successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceVoidCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/invoices/{id}/void"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postInvoiceVoidValidateBeforeCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling postInvoiceVoid(Async)");
        }

        return postInvoiceVoidCall(id, organizationId, _callback);

    }

    /**
     * Void an invoice
     * Void an invoice with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Invoice
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was voided successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public Invoice postInvoiceVoid(String id, String organizationId) throws ApiException {
        ApiResponse<Invoice> localVarResp = postInvoiceVoidWithHttpInfo(id, organizationId);
        return localVarResp.getData();
    }

    /**
     * Void an invoice
     * Void an invoice with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Invoice&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was voided successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Invoice> postInvoiceVoidWithHttpInfo(String id, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postInvoiceVoidValidateBeforeCall(id, organizationId, null);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Void an invoice (asynchronously)
     * Void an invoice with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Invoice was voided successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postInvoiceVoidAsync(String id, String organizationId, final ApiCallback<Invoice> _callback) throws ApiException {

        okhttp3.Call localVarCall = postInvoiceVoidValidateBeforeCall(id, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putInvoice
     * @param id The resource identifier string. (required)
     * @param invoice Invoice resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Invoice was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putInvoiceCall(String id, Invoice invoice, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = invoice;

        // create path and map variables
        String localVarPath = "/invoices/{id}"
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
    private okhttp3.Call putInvoiceValidateBeforeCall(String id, Invoice invoice, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling putInvoice(Async)");
        }

        // verify the required parameter 'invoice' is set
        if (invoice == null) {
            throw new ApiException("Missing the required parameter 'invoice' when calling putInvoice(Async)");
        }

        return putInvoiceCall(id, invoice, organizationId, _callback);

    }

    /**
     * Create or update an invoice with predefined ID
     * Create or update an invoice with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param invoice Invoice resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Invoice
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Invoice was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public Invoice putInvoice(String id, Invoice invoice, String organizationId) throws ApiException {
        ApiResponse<Invoice> localVarResp = putInvoiceWithHttpInfo(id, invoice, organizationId);
        return localVarResp.getData();
    }

    /**
     * Create or update an invoice with predefined ID
     * Create or update an invoice with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param invoice Invoice resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Invoice&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Invoice was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Invoice> putInvoiceWithHttpInfo(String id, Invoice invoice, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = putInvoiceValidateBeforeCall(id, invoice, organizationId, null);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create or update an invoice with predefined ID (asynchronously)
     * Create or update an invoice with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param invoice Invoice resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Invoice was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Invoice was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putInvoiceAsync(String id, Invoice invoice, String organizationId, final ApiCallback<Invoice> _callback) throws ApiException {

        okhttp3.Call localVarCall = putInvoiceValidateBeforeCall(id, invoice, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
