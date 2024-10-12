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
import org.openapitools.client.model.OrderTimeline;
import org.openapitools.client.model.Subscription;
import org.openapitools.client.model.SubscriptionCancellation;
import org.openapitools.client.model.SubscriptionChange;
import org.openapitools.client.model.SubscriptionInvoice;
import org.openapitools.client.model.SubscriptionReactivation;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class OrdersApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public OrdersApi() {
        this(Configuration.getDefaultApiClient());
    }

    public OrdersApi(ApiClient apiClient) {
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
     * Build call for deleteSubscriptionCancellation
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Cancellaton was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteSubscriptionCancellationCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscription-cancellations/{id}"
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
    private okhttp3.Call deleteSubscriptionCancellationValidateBeforeCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling deleteSubscriptionCancellation(Async)");
        }

        return deleteSubscriptionCancellationCall(id, organizationId, _callback);

    }

    /**
     * Delete a cancellation
     * Delete an order&#39;s cancellation. Only draft can be deleted.
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Cancellaton was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public void deleteSubscriptionCancellation(String id, String organizationId) throws ApiException {
        deleteSubscriptionCancellationWithHttpInfo(id, organizationId);
    }

    /**
     * Delete a cancellation
     * Delete an order&#39;s cancellation. Only draft can be deleted.
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Cancellaton was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteSubscriptionCancellationWithHttpInfo(String id, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = deleteSubscriptionCancellationValidateBeforeCall(id, organizationId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete a cancellation (asynchronously)
     * Delete an order&#39;s cancellation. Only draft can be deleted.
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Cancellaton was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteSubscriptionCancellationAsync(String id, String organizationId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteSubscriptionCancellationValidateBeforeCall(id, organizationId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteSubscriptionTimeline
     * @param id The resource identifier string. (required)
     * @param messageId The Order Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Order Timeline message was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteSubscriptionTimelineCall(String id, String messageId, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{id}/timeline/{messageId}"
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
    private okhttp3.Call deleteSubscriptionTimelineValidateBeforeCall(String id, String messageId, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling deleteSubscriptionTimeline(Async)");
        }

        // verify the required parameter 'messageId' is set
        if (messageId == null) {
            throw new ApiException("Missing the required parameter 'messageId' when calling deleteSubscriptionTimeline(Async)");
        }

        return deleteSubscriptionTimelineCall(id, messageId, organizationId, _callback);

    }

    /**
     * Delete an Order Timeline message
     * Delete an Order Timeline message with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param messageId The Order Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Order Timeline message was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public void deleteSubscriptionTimeline(String id, String messageId, String organizationId) throws ApiException {
        deleteSubscriptionTimelineWithHttpInfo(id, messageId, organizationId);
    }

    /**
     * Delete an Order Timeline message
     * Delete an Order Timeline message with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param messageId The Order Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Order Timeline message was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteSubscriptionTimelineWithHttpInfo(String id, String messageId, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = deleteSubscriptionTimelineValidateBeforeCall(id, messageId, organizationId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Delete an Order Timeline message (asynchronously)
     * Delete an Order Timeline message with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param messageId The Order Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Order Timeline message was deleted. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteSubscriptionTimelineAsync(String id, String messageId, String organizationId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteSubscriptionTimelineValidateBeforeCall(id, messageId, organizationId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSubscription
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Order was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionCall(String id, String organizationId, String expand, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{id}"
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
    private okhttp3.Call getSubscriptionValidateBeforeCall(String id, String organizationId, String expand, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getSubscription(Async)");
        }

        return getSubscriptionCall(id, organizationId, expand, _callback);

    }

    /**
     * Retrieve an order
     * Retrieve an order with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return Subscription
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Order was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public Subscription getSubscription(String id, String organizationId, String expand) throws ApiException {
        ApiResponse<Subscription> localVarResp = getSubscriptionWithHttpInfo(id, organizationId, expand);
        return localVarResp.getData();
    }

    /**
     * Retrieve an order
     * Retrieve an order with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return ApiResponse&lt;Subscription&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Order was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Subscription> getSubscriptionWithHttpInfo(String id, String organizationId, String expand) throws ApiException {
        okhttp3.Call localVarCall = getSubscriptionValidateBeforeCall(id, organizationId, expand, null);
        Type localVarReturnType = new TypeToken<Subscription>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve an order (asynchronously)
     * Retrieve an order with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Order was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionAsync(String id, String organizationId, String expand, final ApiCallback<Subscription> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSubscriptionValidateBeforeCall(id, organizationId, expand, _callback);
        Type localVarReturnType = new TypeToken<Subscription>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSubscriptionCancellation
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Cancellation was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionCancellationCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscription-cancellations/{id}"
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
    private okhttp3.Call getSubscriptionCancellationValidateBeforeCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getSubscriptionCancellation(Async)");
        }

        return getSubscriptionCancellationCall(id, organizationId, _callback);

    }

    /**
     * Retrieve an order сancellation
     * Retrieve an order сancellation with specified identifier string.
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return SubscriptionCancellation
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Cancellation was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public SubscriptionCancellation getSubscriptionCancellation(String id, String organizationId) throws ApiException {
        ApiResponse<SubscriptionCancellation> localVarResp = getSubscriptionCancellationWithHttpInfo(id, organizationId);
        return localVarResp.getData();
    }

    /**
     * Retrieve an order сancellation
     * Retrieve an order сancellation with specified identifier string.
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;SubscriptionCancellation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Cancellation was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SubscriptionCancellation> getSubscriptionCancellationWithHttpInfo(String id, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = getSubscriptionCancellationValidateBeforeCall(id, organizationId, null);
        Type localVarReturnType = new TypeToken<SubscriptionCancellation>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve an order сancellation (asynchronously)
     * Retrieve an order сancellation with specified identifier string.
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Cancellation was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionCancellationAsync(String id, String organizationId, final ApiCallback<SubscriptionCancellation> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSubscriptionCancellationValidateBeforeCall(id, organizationId, _callback);
        Type localVarReturnType = new TypeToken<SubscriptionCancellation>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSubscriptionCancellationCollection
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of cancellations was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionCancellationCollectionCall(String organizationId, Integer limit, Integer offset, String filter, List<String> sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscription-cancellations";

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
    private okhttp3.Call getSubscriptionCancellationCollectionValidateBeforeCall(String organizationId, Integer limit, Integer offset, String filter, List<String> sort, final ApiCallback _callback) throws ApiException {
        return getSubscriptionCancellationCollectionCall(organizationId, limit, offset, filter, sort, _callback);

    }

    /**
     * Retrieve a list of cancellations
     * Retrieve a list of cancellations for all subscriptions.
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @return List&lt;SubscriptionCancellation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of cancellations was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public List<SubscriptionCancellation> getSubscriptionCancellationCollection(String organizationId, Integer limit, Integer offset, String filter, List<String> sort) throws ApiException {
        ApiResponse<List<SubscriptionCancellation>> localVarResp = getSubscriptionCancellationCollectionWithHttpInfo(organizationId, limit, offset, filter, sort);
        return localVarResp.getData();
    }

    /**
     * Retrieve a list of cancellations
     * Retrieve a list of cancellations for all subscriptions.
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @return ApiResponse&lt;List&lt;SubscriptionCancellation&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of cancellations was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<SubscriptionCancellation>> getSubscriptionCancellationCollectionWithHttpInfo(String organizationId, Integer limit, Integer offset, String filter, List<String> sort) throws ApiException {
        okhttp3.Call localVarCall = getSubscriptionCancellationCollectionValidateBeforeCall(organizationId, limit, offset, filter, sort, null);
        Type localVarReturnType = new TypeToken<List<SubscriptionCancellation>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a list of cancellations (asynchronously)
     * Retrieve a list of cancellations for all subscriptions.
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of cancellations was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionCancellationCollectionAsync(String organizationId, Integer limit, Integer offset, String filter, List<String> sort, final ApiCallback<List<SubscriptionCancellation>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSubscriptionCancellationCollectionValidateBeforeCall(organizationId, limit, offset, filter, sort, _callback);
        Type localVarReturnType = new TypeToken<List<SubscriptionCancellation>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSubscriptionCollection
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of subscriptions was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionCollectionCall(String organizationId, String filter, List<String> sort, Integer limit, Integer offset, String q, String expand, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions";

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
    private okhttp3.Call getSubscriptionCollectionValidateBeforeCall(String organizationId, String filter, List<String> sort, Integer limit, Integer offset, String q, String expand, final ApiCallback _callback) throws ApiException {
        return getSubscriptionCollectionCall(organizationId, filter, sort, limit, offset, q, expand, _callback);

    }

    /**
     * Retrieve a list of orders
     * Retrieve a list of orders. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return List&lt;Subscription&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of subscriptions was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public List<Subscription> getSubscriptionCollection(String organizationId, String filter, List<String> sort, Integer limit, Integer offset, String q, String expand) throws ApiException {
        ApiResponse<List<Subscription>> localVarResp = getSubscriptionCollectionWithHttpInfo(organizationId, filter, sort, limit, offset, q, expand);
        return localVarResp.getData();
    }

    /**
     * Retrieve a list of orders
     * Retrieve a list of orders. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return ApiResponse&lt;List&lt;Subscription&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of subscriptions was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Subscription>> getSubscriptionCollectionWithHttpInfo(String organizationId, String filter, List<String> sort, Integer limit, Integer offset, String q, String expand) throws ApiException {
        okhttp3.Call localVarCall = getSubscriptionCollectionValidateBeforeCall(organizationId, filter, sort, limit, offset, q, expand, null);
        Type localVarReturnType = new TypeToken<List<Subscription>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a list of orders (asynchronously)
     * Retrieve a list of orders. 
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param q The partial search of the text fields. (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of subscriptions was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionCollectionAsync(String organizationId, String filter, List<String> sort, Integer limit, Integer offset, String q, String expand, final ApiCallback<List<Subscription>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSubscriptionCollectionValidateBeforeCall(organizationId, filter, sort, limit, offset, q, expand, _callback);
        Type localVarReturnType = new TypeToken<List<Subscription>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSubscriptionReactivation
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Reactivation was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionReactivationCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscription-reactivations/{id}"
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
    private okhttp3.Call getSubscriptionReactivationValidateBeforeCall(String id, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getSubscriptionReactivation(Async)");
        }

        return getSubscriptionReactivationCall(id, organizationId, _callback);

    }

    /**
     * Retrieve an order reactivation
     * Retrieve an order reactivation with specified identifier string.
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return SubscriptionReactivation
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Reactivation was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public SubscriptionReactivation getSubscriptionReactivation(String id, String organizationId) throws ApiException {
        ApiResponse<SubscriptionReactivation> localVarResp = getSubscriptionReactivationWithHttpInfo(id, organizationId);
        return localVarResp.getData();
    }

    /**
     * Retrieve an order reactivation
     * Retrieve an order reactivation with specified identifier string.
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;SubscriptionReactivation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Reactivation was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SubscriptionReactivation> getSubscriptionReactivationWithHttpInfo(String id, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = getSubscriptionReactivationValidateBeforeCall(id, organizationId, null);
        Type localVarReturnType = new TypeToken<SubscriptionReactivation>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve an order reactivation (asynchronously)
     * Retrieve an order reactivation with specified identifier string.
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Reactivation was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionReactivationAsync(String id, String organizationId, final ApiCallback<SubscriptionReactivation> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSubscriptionReactivationValidateBeforeCall(id, organizationId, _callback);
        Type localVarReturnType = new TypeToken<SubscriptionReactivation>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSubscriptionReactivationCollection
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of reactivations was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionReactivationCollectionCall(String organizationId, Integer limit, Integer offset, String filter, List<String> sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscription-reactivations";

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
    private okhttp3.Call getSubscriptionReactivationCollectionValidateBeforeCall(String organizationId, Integer limit, Integer offset, String filter, List<String> sort, final ApiCallback _callback) throws ApiException {
        return getSubscriptionReactivationCollectionCall(organizationId, limit, offset, filter, sort, _callback);

    }

    /**
     * Retrieve a list of reactivations
     * Retrieve a list of reactivations for all subscriptions.
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @return List&lt;SubscriptionReactivation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of reactivations was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public List<SubscriptionReactivation> getSubscriptionReactivationCollection(String organizationId, Integer limit, Integer offset, String filter, List<String> sort) throws ApiException {
        ApiResponse<List<SubscriptionReactivation>> localVarResp = getSubscriptionReactivationCollectionWithHttpInfo(organizationId, limit, offset, filter, sort);
        return localVarResp.getData();
    }

    /**
     * Retrieve a list of reactivations
     * Retrieve a list of reactivations for all subscriptions.
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @return ApiResponse&lt;List&lt;SubscriptionReactivation&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of reactivations was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<SubscriptionReactivation>> getSubscriptionReactivationCollectionWithHttpInfo(String organizationId, Integer limit, Integer offset, String filter, List<String> sort) throws ApiException {
        okhttp3.Call localVarCall = getSubscriptionReactivationCollectionValidateBeforeCall(organizationId, limit, offset, filter, sort, null);
        Type localVarReturnType = new TypeToken<List<SubscriptionReactivation>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a list of reactivations (asynchronously)
     * Retrieve a list of reactivations for all subscriptions.
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of reactivations was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionReactivationCollectionAsync(String organizationId, Integer limit, Integer offset, String filter, List<String> sort, final ApiCallback<List<SubscriptionReactivation>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSubscriptionReactivationCollectionValidateBeforeCall(organizationId, limit, offset, filter, sort, _callback);
        Type localVarReturnType = new TypeToken<List<SubscriptionReactivation>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSubscriptionTimeline
     * @param id The resource identifier string. (required)
     * @param messageId The Order Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Order message was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionTimelineCall(String id, String messageId, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{id}/timeline/{messageId}"
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
    private okhttp3.Call getSubscriptionTimelineValidateBeforeCall(String id, String messageId, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getSubscriptionTimeline(Async)");
        }

        // verify the required parameter 'messageId' is set
        if (messageId == null) {
            throw new ApiException("Missing the required parameter 'messageId' when calling getSubscriptionTimeline(Async)");
        }

        return getSubscriptionTimelineCall(id, messageId, organizationId, _callback);

    }

    /**
     * Retrieve an Order Timeline message
     * Retrieve a order message with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param messageId The Order Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return OrderTimeline
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Order message was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public OrderTimeline getSubscriptionTimeline(String id, String messageId, String organizationId) throws ApiException {
        ApiResponse<OrderTimeline> localVarResp = getSubscriptionTimelineWithHttpInfo(id, messageId, organizationId);
        return localVarResp.getData();
    }

    /**
     * Retrieve an Order Timeline message
     * Retrieve a order message with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param messageId The Order Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;OrderTimeline&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Order message was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<OrderTimeline> getSubscriptionTimelineWithHttpInfo(String id, String messageId, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = getSubscriptionTimelineValidateBeforeCall(id, messageId, organizationId, null);
        Type localVarReturnType = new TypeToken<OrderTimeline>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve an Order Timeline message (asynchronously)
     * Retrieve a order message with specified identifier string. 
     * @param id The resource identifier string. (required)
     * @param messageId The Order Timeline message ID. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Order message was retrieved successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionTimelineAsync(String id, String messageId, String organizationId, final ApiCallback<OrderTimeline> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSubscriptionTimelineValidateBeforeCall(id, messageId, organizationId, _callback);
        Type localVarReturnType = new TypeToken<OrderTimeline>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSubscriptionTimelineCollection
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
        <tr><td> 200 </td><td> A list of order timeline messages was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionTimelineCollectionCall(String id, String organizationId, Integer limit, Integer offset, String filter, List<String> sort, String q, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{id}/timeline"
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
    private okhttp3.Call getSubscriptionTimelineCollectionValidateBeforeCall(String id, String organizationId, Integer limit, Integer offset, String filter, List<String> sort, String q, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getSubscriptionTimelineCollection(Async)");
        }

        return getSubscriptionTimelineCollectionCall(id, organizationId, limit, offset, filter, sort, q, _callback);

    }

    /**
     * Retrieve a list of order timeline messages
     * Retrieve a list of order timeline messages. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param q The partial search of the text fields. (optional)
     * @return List&lt;OrderTimeline&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of order timeline messages was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
     </table>
     */
    public List<OrderTimeline> getSubscriptionTimelineCollection(String id, String organizationId, Integer limit, Integer offset, String filter, List<String> sort, String q) throws ApiException {
        ApiResponse<List<OrderTimeline>> localVarResp = getSubscriptionTimelineCollectionWithHttpInfo(id, organizationId, limit, offset, filter, sort, q);
        return localVarResp.getData();
    }

    /**
     * Retrieve a list of order timeline messages
     * Retrieve a list of order timeline messages. 
     * @param id The resource identifier string. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param limit The collection items limit. (optional)
     * @param offset The collection items offset. (optional)
     * @param filter The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  (optional)
     * @param sort The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). (optional)
     * @param q The partial search of the text fields. (optional)
     * @return ApiResponse&lt;List&lt;OrderTimeline&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A list of order timeline messages was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<OrderTimeline>> getSubscriptionTimelineCollectionWithHttpInfo(String id, String organizationId, Integer limit, Integer offset, String filter, List<String> sort, String q) throws ApiException {
        okhttp3.Call localVarCall = getSubscriptionTimelineCollectionValidateBeforeCall(id, organizationId, limit, offset, filter, sort, q, null);
        Type localVarReturnType = new TypeToken<List<OrderTimeline>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a list of order timeline messages (asynchronously)
     * Retrieve a list of order timeline messages. 
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
        <tr><td> 200 </td><td> A list of order timeline messages was retrieved successfully. </td><td>  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getSubscriptionTimelineCollectionAsync(String id, String organizationId, Integer limit, Integer offset, String filter, List<String> sort, String q, final ApiCallback<List<OrderTimeline>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSubscriptionTimelineCollectionValidateBeforeCall(id, organizationId, limit, offset, filter, sort, q, _callback);
        Type localVarReturnType = new TypeToken<List<OrderTimeline>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getSubscriptionUpcomingInvoiceCollection
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
    public okhttp3.Call getSubscriptionUpcomingInvoiceCollectionCall(String id, String organizationId, String expand, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{id}/upcoming-invoices"
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
    private okhttp3.Call getSubscriptionUpcomingInvoiceCollectionValidateBeforeCall(String id, String organizationId, String expand, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getSubscriptionUpcomingInvoiceCollection(Async)");
        }

        return getSubscriptionUpcomingInvoiceCollectionCall(id, organizationId, expand, _callback);

    }

    /**
     * Retrieve subscription order&#39;s upcoming invoice
     * Retrieve an upcoming invoice from the specified subscription order. The endpoint is temporary before upcoming invoices get a complete integration. 
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
    public List<Invoice> getSubscriptionUpcomingInvoiceCollection(String id, String organizationId, String expand) throws ApiException {
        ApiResponse<List<Invoice>> localVarResp = getSubscriptionUpcomingInvoiceCollectionWithHttpInfo(id, organizationId, expand);
        return localVarResp.getData();
    }

    /**
     * Retrieve subscription order&#39;s upcoming invoice
     * Retrieve an upcoming invoice from the specified subscription order. The endpoint is temporary before upcoming invoices get a complete integration. 
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
    public ApiResponse<List<Invoice>> getSubscriptionUpcomingInvoiceCollectionWithHttpInfo(String id, String organizationId, String expand) throws ApiException {
        okhttp3.Call localVarCall = getSubscriptionUpcomingInvoiceCollectionValidateBeforeCall(id, organizationId, expand, null);
        Type localVarReturnType = new TypeToken<List<Invoice>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve subscription order&#39;s upcoming invoice (asynchronously)
     * Retrieve an upcoming invoice from the specified subscription order. The endpoint is temporary before upcoming invoices get a complete integration. 
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
    public okhttp3.Call getSubscriptionUpcomingInvoiceCollectionAsync(String id, String organizationId, String expand, final ApiCallback<List<Invoice>> _callback) throws ApiException {

        okhttp3.Call localVarCall = getSubscriptionUpcomingInvoiceCollectionValidateBeforeCall(id, organizationId, expand, _callback);
        Type localVarReturnType = new TypeToken<List<Invoice>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postSubscription
     * @param subscription Order resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Order was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postSubscriptionCall(Subscription subscription, String organizationId, String expand, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = subscription;

        // create path and map variables
        String localVarPath = "/subscriptions";

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
    private okhttp3.Call postSubscriptionValidateBeforeCall(Subscription subscription, String organizationId, String expand, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'subscription' is set
        if (subscription == null) {
            throw new ApiException("Missing the required parameter 'subscription' when calling postSubscription(Async)");
        }

        return postSubscriptionCall(subscription, organizationId, expand, _callback);

    }

    /**
     * Create an order
     * Create an order. Consider using the upsert. operation to accomplish this task. 
     * @param subscription Order resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return Subscription
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Order was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public Subscription postSubscription(Subscription subscription, String organizationId, String expand) throws ApiException {
        ApiResponse<Subscription> localVarResp = postSubscriptionWithHttpInfo(subscription, organizationId, expand);
        return localVarResp.getData();
    }

    /**
     * Create an order
     * Create an order. Consider using the upsert. operation to accomplish this task. 
     * @param subscription Order resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return ApiResponse&lt;Subscription&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Order was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Subscription> postSubscriptionWithHttpInfo(Subscription subscription, String organizationId, String expand) throws ApiException {
        okhttp3.Call localVarCall = postSubscriptionValidateBeforeCall(subscription, organizationId, expand, null);
        Type localVarReturnType = new TypeToken<Subscription>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create an order (asynchronously)
     * Create an order. Consider using the upsert. operation to accomplish this task. 
     * @param subscription Order resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Order was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postSubscriptionAsync(Subscription subscription, String organizationId, String expand, final ApiCallback<Subscription> _callback) throws ApiException {

        okhttp3.Call localVarCall = postSubscriptionValidateBeforeCall(subscription, organizationId, expand, _callback);
        Type localVarReturnType = new TypeToken<Subscription>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postSubscriptionCancellation
     * @param subscriptionCancellation Cancellation resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Cancellation was created, the order is or will be deactivated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postSubscriptionCancellationCall(SubscriptionCancellation subscriptionCancellation, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = subscriptionCancellation;

        // create path and map variables
        String localVarPath = "/subscription-cancellations";

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
    private okhttp3.Call postSubscriptionCancellationValidateBeforeCall(SubscriptionCancellation subscriptionCancellation, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'subscriptionCancellation' is set
        if (subscriptionCancellation == null) {
            throw new ApiException("Missing the required parameter 'subscriptionCancellation' when calling postSubscriptionCancellation(Async)");
        }

        return postSubscriptionCancellationCall(subscriptionCancellation, organizationId, _callback);

    }

    /**
     * Cancel an order
     * Cancel an order or preview the cancellation parameters before that.
     * @param subscriptionCancellation Cancellation resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return SubscriptionCancellation
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Cancellation was created, the order is or will be deactivated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public SubscriptionCancellation postSubscriptionCancellation(SubscriptionCancellation subscriptionCancellation, String organizationId) throws ApiException {
        ApiResponse<SubscriptionCancellation> localVarResp = postSubscriptionCancellationWithHttpInfo(subscriptionCancellation, organizationId);
        return localVarResp.getData();
    }

    /**
     * Cancel an order
     * Cancel an order or preview the cancellation parameters before that.
     * @param subscriptionCancellation Cancellation resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;SubscriptionCancellation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Cancellation was created, the order is or will be deactivated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SubscriptionCancellation> postSubscriptionCancellationWithHttpInfo(SubscriptionCancellation subscriptionCancellation, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postSubscriptionCancellationValidateBeforeCall(subscriptionCancellation, organizationId, null);
        Type localVarReturnType = new TypeToken<SubscriptionCancellation>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Cancel an order (asynchronously)
     * Cancel an order or preview the cancellation parameters before that.
     * @param subscriptionCancellation Cancellation resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Cancellation was created, the order is or will be deactivated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postSubscriptionCancellationAsync(SubscriptionCancellation subscriptionCancellation, String organizationId, final ApiCallback<SubscriptionCancellation> _callback) throws ApiException {

        okhttp3.Call localVarCall = postSubscriptionCancellationValidateBeforeCall(subscriptionCancellation, organizationId, _callback);
        Type localVarReturnType = new TypeToken<SubscriptionCancellation>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postSubscriptionInterimInvoice
     * @param id The resource identifier string. (required)
     * @param subscriptionInvoice Issue an interim invoice. (required)
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
    public okhttp3.Call postSubscriptionInterimInvoiceCall(String id, SubscriptionInvoice subscriptionInvoice, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = subscriptionInvoice;

        // create path and map variables
        String localVarPath = "/subscriptions/{id}/interim-invoice"
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
    private okhttp3.Call postSubscriptionInterimInvoiceValidateBeforeCall(String id, SubscriptionInvoice subscriptionInvoice, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling postSubscriptionInterimInvoice(Async)");
        }

        // verify the required parameter 'subscriptionInvoice' is set
        if (subscriptionInvoice == null) {
            throw new ApiException("Missing the required parameter 'subscriptionInvoice' when calling postSubscriptionInterimInvoice(Async)");
        }

        return postSubscriptionInterimInvoiceCall(id, subscriptionInvoice, organizationId, _callback);

    }

    /**
     * Issue an interim invoice for a subscription order
     * Issue an interim invoice for a subscription, typically used in conjunction. with plan changes and pro rata adjustments. This process creates an invoice, adds the subscription&#39;s line items to the invoice, and issues the invoice, and applies payment to it if a transaction id is supplied. 
     * @param id The resource identifier string. (required)
     * @param subscriptionInvoice Issue an interim invoice. (required)
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
    public Invoice postSubscriptionInterimInvoice(String id, SubscriptionInvoice subscriptionInvoice, String organizationId) throws ApiException {
        ApiResponse<Invoice> localVarResp = postSubscriptionInterimInvoiceWithHttpInfo(id, subscriptionInvoice, organizationId);
        return localVarResp.getData();
    }

    /**
     * Issue an interim invoice for a subscription order
     * Issue an interim invoice for a subscription, typically used in conjunction. with plan changes and pro rata adjustments. This process creates an invoice, adds the subscription&#39;s line items to the invoice, and issues the invoice, and applies payment to it if a transaction id is supplied. 
     * @param id The resource identifier string. (required)
     * @param subscriptionInvoice Issue an interim invoice. (required)
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
    public ApiResponse<Invoice> postSubscriptionInterimInvoiceWithHttpInfo(String id, SubscriptionInvoice subscriptionInvoice, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postSubscriptionInterimInvoiceValidateBeforeCall(id, subscriptionInvoice, organizationId, null);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Issue an interim invoice for a subscription order (asynchronously)
     * Issue an interim invoice for a subscription, typically used in conjunction. with plan changes and pro rata adjustments. This process creates an invoice, adds the subscription&#39;s line items to the invoice, and issues the invoice, and applies payment to it if a transaction id is supplied. 
     * @param id The resource identifier string. (required)
     * @param subscriptionInvoice Issue an interim invoice. (required)
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
    public okhttp3.Call postSubscriptionInterimInvoiceAsync(String id, SubscriptionInvoice subscriptionInvoice, String organizationId, final ApiCallback<Invoice> _callback) throws ApiException {

        okhttp3.Call localVarCall = postSubscriptionInterimInvoiceValidateBeforeCall(id, subscriptionInvoice, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postSubscriptionItemsChange
     * @param id The resource identifier string. (required)
     * @param subscriptionChange Change items request. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Order was changed. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postSubscriptionItemsChangeCall(String id, SubscriptionChange subscriptionChange, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = subscriptionChange;

        // create path and map variables
        String localVarPath = "/subscriptions/{id}/change-items"
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
    private okhttp3.Call postSubscriptionItemsChangeValidateBeforeCall(String id, SubscriptionChange subscriptionChange, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling postSubscriptionItemsChange(Async)");
        }

        // verify the required parameter 'subscriptionChange' is set
        if (subscriptionChange == null) {
            throw new ApiException("Missing the required parameter 'subscriptionChange' when calling postSubscriptionItemsChange(Async)");
        }

        return postSubscriptionItemsChangeCall(id, subscriptionChange, organizationId, _callback);

    }

    /**
     * Change an order&#39;s items
     * Change an order&#39;s items or quantities and designate when and if there should be pro-rata credits given. 
     * @param id The resource identifier string. (required)
     * @param subscriptionChange Change items request. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Subscription
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Order was changed. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public Subscription postSubscriptionItemsChange(String id, SubscriptionChange subscriptionChange, String organizationId) throws ApiException {
        ApiResponse<Subscription> localVarResp = postSubscriptionItemsChangeWithHttpInfo(id, subscriptionChange, organizationId);
        return localVarResp.getData();
    }

    /**
     * Change an order&#39;s items
     * Change an order&#39;s items or quantities and designate when and if there should be pro-rata credits given. 
     * @param id The resource identifier string. (required)
     * @param subscriptionChange Change items request. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Subscription&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Order was changed. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Subscription> postSubscriptionItemsChangeWithHttpInfo(String id, SubscriptionChange subscriptionChange, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postSubscriptionItemsChangeValidateBeforeCall(id, subscriptionChange, organizationId, null);
        Type localVarReturnType = new TypeToken<Subscription>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Change an order&#39;s items (asynchronously)
     * Change an order&#39;s items or quantities and designate when and if there should be pro-rata credits given. 
     * @param id The resource identifier string. (required)
     * @param subscriptionChange Change items request. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Order was changed. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postSubscriptionItemsChangeAsync(String id, SubscriptionChange subscriptionChange, String organizationId, final ApiCallback<Subscription> _callback) throws ApiException {

        okhttp3.Call localVarCall = postSubscriptionItemsChangeValidateBeforeCall(id, subscriptionChange, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Subscription>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postSubscriptionReactivation
     * @param subscriptionReactivation Reactivation resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Reactivation was created, the order is active and won&#39;t be. deactivated. If there was a cancellation with status \&quot;confirmed\&quot;, it is revoked.  </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postSubscriptionReactivationCall(SubscriptionReactivation subscriptionReactivation, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = subscriptionReactivation;

        // create path and map variables
        String localVarPath = "/subscription-reactivations";

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
    private okhttp3.Call postSubscriptionReactivationValidateBeforeCall(SubscriptionReactivation subscriptionReactivation, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'subscriptionReactivation' is set
        if (subscriptionReactivation == null) {
            throw new ApiException("Missing the required parameter 'subscriptionReactivation' when calling postSubscriptionReactivation(Async)");
        }

        return postSubscriptionReactivationCall(subscriptionReactivation, organizationId, _callback);

    }

    /**
     * Reactivate an order
     * Reactivate a subscription.
     * @param subscriptionReactivation Reactivation resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return SubscriptionReactivation
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Reactivation was created, the order is active and won&#39;t be. deactivated. If there was a cancellation with status \&quot;confirmed\&quot;, it is revoked.  </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public SubscriptionReactivation postSubscriptionReactivation(SubscriptionReactivation subscriptionReactivation, String organizationId) throws ApiException {
        ApiResponse<SubscriptionReactivation> localVarResp = postSubscriptionReactivationWithHttpInfo(subscriptionReactivation, organizationId);
        return localVarResp.getData();
    }

    /**
     * Reactivate an order
     * Reactivate a subscription.
     * @param subscriptionReactivation Reactivation resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;SubscriptionReactivation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Reactivation was created, the order is active and won&#39;t be. deactivated. If there was a cancellation with status \&quot;confirmed\&quot;, it is revoked.  </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SubscriptionReactivation> postSubscriptionReactivationWithHttpInfo(SubscriptionReactivation subscriptionReactivation, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postSubscriptionReactivationValidateBeforeCall(subscriptionReactivation, organizationId, null);
        Type localVarReturnType = new TypeToken<SubscriptionReactivation>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Reactivate an order (asynchronously)
     * Reactivate a subscription.
     * @param subscriptionReactivation Reactivation resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Reactivation was created, the order is active and won&#39;t be. deactivated. If there was a cancellation with status \&quot;confirmed\&quot;, it is revoked.  </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postSubscriptionReactivationAsync(SubscriptionReactivation subscriptionReactivation, String organizationId, final ApiCallback<SubscriptionReactivation> _callback) throws ApiException {

        okhttp3.Call localVarCall = postSubscriptionReactivationValidateBeforeCall(subscriptionReactivation, organizationId, _callback);
        Type localVarReturnType = new TypeToken<SubscriptionReactivation>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postSubscriptionTimeline
     * @param id The resource identifier string. (required)
     * @param orderTimeline Order Timeline resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Order Timeline comment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postSubscriptionTimelineCall(String id, OrderTimeline orderTimeline, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = orderTimeline;

        // create path and map variables
        String localVarPath = "/subscriptions/{id}/timeline"
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
    private okhttp3.Call postSubscriptionTimelineValidateBeforeCall(String id, OrderTimeline orderTimeline, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling postSubscriptionTimeline(Async)");
        }

        // verify the required parameter 'orderTimeline' is set
        if (orderTimeline == null) {
            throw new ApiException("Missing the required parameter 'orderTimeline' when calling postSubscriptionTimeline(Async)");
        }

        return postSubscriptionTimelineCall(id, orderTimeline, organizationId, _callback);

    }

    /**
     * Create an order Timeline comment
     * Create an order Timeline comment. 
     * @param id The resource identifier string. (required)
     * @param orderTimeline Order Timeline resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return OrderTimeline
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Order Timeline comment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public OrderTimeline postSubscriptionTimeline(String id, OrderTimeline orderTimeline, String organizationId) throws ApiException {
        ApiResponse<OrderTimeline> localVarResp = postSubscriptionTimelineWithHttpInfo(id, orderTimeline, organizationId);
        return localVarResp.getData();
    }

    /**
     * Create an order Timeline comment
     * Create an order Timeline comment. 
     * @param id The resource identifier string. (required)
     * @param orderTimeline Order Timeline resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;OrderTimeline&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Order Timeline comment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<OrderTimeline> postSubscriptionTimelineWithHttpInfo(String id, OrderTimeline orderTimeline, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postSubscriptionTimelineValidateBeforeCall(id, orderTimeline, organizationId, null);
        Type localVarReturnType = new TypeToken<OrderTimeline>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create an order Timeline comment (asynchronously)
     * Create an order Timeline comment. 
     * @param id The resource identifier string. (required)
     * @param orderTimeline Order Timeline resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Order Timeline comment was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postSubscriptionTimelineAsync(String id, OrderTimeline orderTimeline, String organizationId, final ApiCallback<OrderTimeline> _callback) throws ApiException {

        okhttp3.Call localVarCall = postSubscriptionTimelineValidateBeforeCall(id, orderTimeline, organizationId, _callback);
        Type localVarReturnType = new TypeToken<OrderTimeline>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postUpcomingInvoiceIssuance
     * @param id The resource identifier string. (required)
     * @param invoiceId The Upcoming Invoice ID. (required)
     * @param invoiceIssue InvoiceIssue resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Upcoming Invoice was issued successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postUpcomingInvoiceIssuanceCall(String id, String invoiceId, InvoiceIssue invoiceIssue, String organizationId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/subscriptions/{id}/upcoming-invoices/{invoiceId}/issue"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "invoiceId" + "}", localVarApiClient.escapeString(invoiceId.toString()));

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
    private okhttp3.Call postUpcomingInvoiceIssuanceValidateBeforeCall(String id, String invoiceId, InvoiceIssue invoiceIssue, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling postUpcomingInvoiceIssuance(Async)");
        }

        // verify the required parameter 'invoiceId' is set
        if (invoiceId == null) {
            throw new ApiException("Missing the required parameter 'invoiceId' when calling postUpcomingInvoiceIssuance(Async)");
        }

        // verify the required parameter 'invoiceIssue' is set
        if (invoiceIssue == null) {
            throw new ApiException("Missing the required parameter 'invoiceIssue' when calling postUpcomingInvoiceIssuance(Async)");
        }

        return postUpcomingInvoiceIssuanceCall(id, invoiceId, invoiceIssue, organizationId, _callback);

    }

    /**
     * Issue an upcoming invoice for early pay
     * Issue an upcoming invoice with specified identifier string for early pay. 
     * @param id The resource identifier string. (required)
     * @param invoiceId The Upcoming Invoice ID. (required)
     * @param invoiceIssue InvoiceIssue resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return Invoice
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Upcoming Invoice was issued successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public Invoice postUpcomingInvoiceIssuance(String id, String invoiceId, InvoiceIssue invoiceIssue, String organizationId) throws ApiException {
        ApiResponse<Invoice> localVarResp = postUpcomingInvoiceIssuanceWithHttpInfo(id, invoiceId, invoiceIssue, organizationId);
        return localVarResp.getData();
    }

    /**
     * Issue an upcoming invoice for early pay
     * Issue an upcoming invoice with specified identifier string for early pay. 
     * @param id The resource identifier string. (required)
     * @param invoiceId The Upcoming Invoice ID. (required)
     * @param invoiceIssue InvoiceIssue resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;Invoice&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Upcoming Invoice was issued successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Invoice> postUpcomingInvoiceIssuanceWithHttpInfo(String id, String invoiceId, InvoiceIssue invoiceIssue, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = postUpcomingInvoiceIssuanceValidateBeforeCall(id, invoiceId, invoiceIssue, organizationId, null);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Issue an upcoming invoice for early pay (asynchronously)
     * Issue an upcoming invoice with specified identifier string for early pay. 
     * @param id The resource identifier string. (required)
     * @param invoiceId The Upcoming Invoice ID. (required)
     * @param invoiceIssue InvoiceIssue resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Upcoming Invoice was issued successfully. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 409 </td><td> Conflict. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call postUpcomingInvoiceIssuanceAsync(String id, String invoiceId, InvoiceIssue invoiceIssue, String organizationId, final ApiCallback<Invoice> _callback) throws ApiException {

        okhttp3.Call localVarCall = postUpcomingInvoiceIssuanceValidateBeforeCall(id, invoiceId, invoiceIssue, organizationId, _callback);
        Type localVarReturnType = new TypeToken<Invoice>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putSubscription
     * @param id The resource identifier string. (required)
     * @param subscription Order resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Order was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Order was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putSubscriptionCall(String id, Subscription subscription, String organizationId, String expand, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = subscription;

        // create path and map variables
        String localVarPath = "/subscriptions/{id}"
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
    private okhttp3.Call putSubscriptionValidateBeforeCall(String id, Subscription subscription, String organizationId, String expand, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling putSubscription(Async)");
        }

        // verify the required parameter 'subscription' is set
        if (subscription == null) {
            throw new ApiException("Missing the required parameter 'subscription' when calling putSubscription(Async)");
        }

        return putSubscriptionCall(id, subscription, organizationId, expand, _callback);

    }

    /**
     * Upsert an order with predefined ID
     * Create or update an order with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param subscription Order resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return Subscription
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Order was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Order was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public Subscription putSubscription(String id, Subscription subscription, String organizationId, String expand) throws ApiException {
        ApiResponse<Subscription> localVarResp = putSubscriptionWithHttpInfo(id, subscription, organizationId, expand);
        return localVarResp.getData();
    }

    /**
     * Upsert an order with predefined ID
     * Create or update an order with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param subscription Order resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @return ApiResponse&lt;Subscription&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Order was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Order was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Subscription> putSubscriptionWithHttpInfo(String id, Subscription subscription, String organizationId, String expand) throws ApiException {
        okhttp3.Call localVarCall = putSubscriptionValidateBeforeCall(id, subscription, organizationId, expand, null);
        Type localVarReturnType = new TypeToken<Subscription>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Upsert an order with predefined ID (asynchronously)
     * Create or update an order with predefined identifier string. 
     * @param id The resource identifier string. (required)
     * @param subscription Order resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param expand Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. To expand multiple objects, it accepts a comma-separated list of objects (example: &#x60;expand&#x3D;recentInvoice,initialInvoice&#x60;). Available arguments are:   - recentInvoice   - initialInvoice   - customer   - website  See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Order was updated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Order was created. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Resource was not found. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putSubscriptionAsync(String id, Subscription subscription, String organizationId, String expand, final ApiCallback<Subscription> _callback) throws ApiException {

        okhttp3.Call localVarCall = putSubscriptionValidateBeforeCall(id, subscription, organizationId, expand, _callback);
        Type localVarReturnType = new TypeToken<Subscription>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putSubscriptionCancellation
     * @param id The resource identifier string. (required)
     * @param subscriptionCancellation Cancellation resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Cancellation was updated, the order is or will be deactivated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Cancellation was created, the order is or will be deactivated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putSubscriptionCancellationCall(String id, SubscriptionCancellation subscriptionCancellation, String organizationId, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = subscriptionCancellation;

        // create path and map variables
        String localVarPath = "/subscription-cancellations/{id}"
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
    private okhttp3.Call putSubscriptionCancellationValidateBeforeCall(String id, SubscriptionCancellation subscriptionCancellation, String organizationId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling putSubscriptionCancellation(Async)");
        }

        // verify the required parameter 'subscriptionCancellation' is set
        if (subscriptionCancellation == null) {
            throw new ApiException("Missing the required parameter 'subscriptionCancellation' when calling putSubscriptionCancellation(Async)");
        }

        return putSubscriptionCancellationCall(id, subscriptionCancellation, organizationId, _callback);

    }

    /**
     * Cancel an order
     * Cancel a subscription.
     * @param id The resource identifier string. (required)
     * @param subscriptionCancellation Cancellation resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return SubscriptionCancellation
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Cancellation was updated, the order is or will be deactivated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Cancellation was created, the order is or will be deactivated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public SubscriptionCancellation putSubscriptionCancellation(String id, SubscriptionCancellation subscriptionCancellation, String organizationId) throws ApiException {
        ApiResponse<SubscriptionCancellation> localVarResp = putSubscriptionCancellationWithHttpInfo(id, subscriptionCancellation, organizationId);
        return localVarResp.getData();
    }

    /**
     * Cancel an order
     * Cancel a subscription.
     * @param id The resource identifier string. (required)
     * @param subscriptionCancellation Cancellation resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @return ApiResponse&lt;SubscriptionCancellation&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Cancellation was updated, the order is or will be deactivated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Cancellation was created, the order is or will be deactivated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SubscriptionCancellation> putSubscriptionCancellationWithHttpInfo(String id, SubscriptionCancellation subscriptionCancellation, String organizationId) throws ApiException {
        okhttp3.Call localVarCall = putSubscriptionCancellationValidateBeforeCall(id, subscriptionCancellation, organizationId, null);
        Type localVarReturnType = new TypeToken<SubscriptionCancellation>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Cancel an order (asynchronously)
     * Cancel a subscription.
     * @param id The resource identifier string. (required)
     * @param subscriptionCancellation Cancellation resource. (required)
     * @param organizationId Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Cancellation was updated, the order is or will be deactivated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 201 </td><td> Cancellation was created, the order is or will be deactivated. </td><td>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  </td></tr>
        <tr><td> 401 </td><td> Unauthorized access, invalid credentials was used. </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Access forbidden. </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Invalid data was sent. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putSubscriptionCancellationAsync(String id, SubscriptionCancellation subscriptionCancellation, String organizationId, final ApiCallback<SubscriptionCancellation> _callback) throws ApiException {

        okhttp3.Call localVarCall = putSubscriptionCancellationValidateBeforeCall(id, subscriptionCancellation, organizationId, _callback);
        Type localVarReturnType = new TypeToken<SubscriptionCancellation>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
