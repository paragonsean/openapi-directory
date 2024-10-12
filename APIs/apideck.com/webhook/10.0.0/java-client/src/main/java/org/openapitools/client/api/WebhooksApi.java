/*
 * Webhook API
 * Welcome to the Webhook API.  You can use this API to access all Webhook API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
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
import org.openapitools.client.model.CreateWebhookRequest;
import org.openapitools.client.model.CreateWebhookResponse;
import org.openapitools.client.model.DeleteWebhookResponse;
import org.openapitools.client.model.GetWebhookEventLogsResponse;
import org.openapitools.client.model.GetWebhookResponse;
import org.openapitools.client.model.GetWebhooksResponse;
import org.openapitools.client.model.NotFoundResponse;
import org.openapitools.client.model.PaymentRequiredResponse;
import org.openapitools.client.model.UnauthorizedResponse;
import org.openapitools.client.model.UnexpectedErrorResponse;
import org.openapitools.client.model.UnprocessableResponse;
import org.openapitools.client.model.UpdateWebhookRequest;
import org.openapitools.client.model.UpdateWebhookResponse;
import org.openapitools.client.model.WebhookEventLogsFilter;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class WebhooksApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public WebhooksApi() {
        this(Configuration.getDefaultApiClient());
    }

    public WebhooksApi(ApiClient apiClient) {
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
     * Build call for eventLogsAll
     * @param xApideckAppId The ID of your Unify application (required)
     * @param cursor Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
     * @param limit Number of results to return. Minimum 1, Maximum 200, Default 20 (optional, default to 20)
     * @param filter Filter results (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> EventLogs </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call eventLogsAllCall(String xApideckAppId, String cursor, Integer limit, WebhookEventLogsFilter filter, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/webhook/logs";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (cursor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("cursor", cursor));
        }

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (filter != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter", filter));
        }

        if (xApideckAppId != null) {
            localVarHeaderParams.put("x-apideck-app-id", localVarApiClient.parameterToString(xApideckAppId));
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

        String[] localVarAuthNames = new String[] { "apiKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call eventLogsAllValidateBeforeCall(String xApideckAppId, String cursor, Integer limit, WebhookEventLogsFilter filter, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling eventLogsAll(Async)");
        }

        return eventLogsAllCall(xApideckAppId, cursor, limit, filter, _callback);

    }

    /**
     * List event logs
     * List event logs
     * @param xApideckAppId The ID of your Unify application (required)
     * @param cursor Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
     * @param limit Number of results to return. Minimum 1, Maximum 200, Default 20 (optional, default to 20)
     * @param filter Filter results (optional)
     * @return GetWebhookEventLogsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> EventLogs </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public GetWebhookEventLogsResponse eventLogsAll(String xApideckAppId, String cursor, Integer limit, WebhookEventLogsFilter filter) throws ApiException {
        ApiResponse<GetWebhookEventLogsResponse> localVarResp = eventLogsAllWithHttpInfo(xApideckAppId, cursor, limit, filter);
        return localVarResp.getData();
    }

    /**
     * List event logs
     * List event logs
     * @param xApideckAppId The ID of your Unify application (required)
     * @param cursor Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
     * @param limit Number of results to return. Minimum 1, Maximum 200, Default 20 (optional, default to 20)
     * @param filter Filter results (optional)
     * @return ApiResponse&lt;GetWebhookEventLogsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> EventLogs </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetWebhookEventLogsResponse> eventLogsAllWithHttpInfo(String xApideckAppId, String cursor, Integer limit, WebhookEventLogsFilter filter) throws ApiException {
        okhttp3.Call localVarCall = eventLogsAllValidateBeforeCall(xApideckAppId, cursor, limit, filter, null);
        Type localVarReturnType = new TypeToken<GetWebhookEventLogsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List event logs (asynchronously)
     * List event logs
     * @param xApideckAppId The ID of your Unify application (required)
     * @param cursor Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
     * @param limit Number of results to return. Minimum 1, Maximum 200, Default 20 (optional, default to 20)
     * @param filter Filter results (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> EventLogs </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call eventLogsAllAsync(String xApideckAppId, String cursor, Integer limit, WebhookEventLogsFilter filter, final ApiCallback<GetWebhookEventLogsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = eventLogsAllValidateBeforeCall(xApideckAppId, cursor, limit, filter, _callback);
        Type localVarReturnType = new TypeToken<GetWebhookEventLogsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for webhooksAdd
     * @param xApideckAppId The ID of your Unify application (required)
     * @param createWebhookRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksAddCall(String xApideckAppId, CreateWebhookRequest createWebhookRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createWebhookRequest;

        // create path and map variables
        String localVarPath = "/webhook/webhooks";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xApideckAppId != null) {
            localVarHeaderParams.put("x-apideck-app-id", localVarApiClient.parameterToString(xApideckAppId));
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

        String[] localVarAuthNames = new String[] { "apiKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call webhooksAddValidateBeforeCall(String xApideckAppId, CreateWebhookRequest createWebhookRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling webhooksAdd(Async)");
        }

        // verify the required parameter 'createWebhookRequest' is set
        if (createWebhookRequest == null) {
            throw new ApiException("Missing the required parameter 'createWebhookRequest' when calling webhooksAdd(Async)");
        }

        return webhooksAddCall(xApideckAppId, createWebhookRequest, _callback);

    }

    /**
     * Create webhook subscription
     * Create a webhook subscription to receive events
     * @param xApideckAppId The ID of your Unify application (required)
     * @param createWebhookRequest  (required)
     * @return CreateWebhookResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public CreateWebhookResponse webhooksAdd(String xApideckAppId, CreateWebhookRequest createWebhookRequest) throws ApiException {
        ApiResponse<CreateWebhookResponse> localVarResp = webhooksAddWithHttpInfo(xApideckAppId, createWebhookRequest);
        return localVarResp.getData();
    }

    /**
     * Create webhook subscription
     * Create a webhook subscription to receive events
     * @param xApideckAppId The ID of your Unify application (required)
     * @param createWebhookRequest  (required)
     * @return ApiResponse&lt;CreateWebhookResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateWebhookResponse> webhooksAddWithHttpInfo(String xApideckAppId, CreateWebhookRequest createWebhookRequest) throws ApiException {
        okhttp3.Call localVarCall = webhooksAddValidateBeforeCall(xApideckAppId, createWebhookRequest, null);
        Type localVarReturnType = new TypeToken<CreateWebhookResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create webhook subscription (asynchronously)
     * Create a webhook subscription to receive events
     * @param xApideckAppId The ID of your Unify application (required)
     * @param createWebhookRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksAddAsync(String xApideckAppId, CreateWebhookRequest createWebhookRequest, final ApiCallback<CreateWebhookResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = webhooksAddValidateBeforeCall(xApideckAppId, createWebhookRequest, _callback);
        Type localVarReturnType = new TypeToken<CreateWebhookResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for webhooksAll
     * @param xApideckAppId The ID of your Unify application (required)
     * @param cursor Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
     * @param limit Number of results to return. Minimum 1, Maximum 200, Default 20 (optional, default to 20)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksAllCall(String xApideckAppId, String cursor, Integer limit, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/webhook/webhooks";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (cursor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("cursor", cursor));
        }

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (xApideckAppId != null) {
            localVarHeaderParams.put("x-apideck-app-id", localVarApiClient.parameterToString(xApideckAppId));
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

        String[] localVarAuthNames = new String[] { "apiKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call webhooksAllValidateBeforeCall(String xApideckAppId, String cursor, Integer limit, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling webhooksAll(Async)");
        }

        return webhooksAllCall(xApideckAppId, cursor, limit, _callback);

    }

    /**
     * List webhook subscriptions
     * List all webhook subscriptions
     * @param xApideckAppId The ID of your Unify application (required)
     * @param cursor Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
     * @param limit Number of results to return. Minimum 1, Maximum 200, Default 20 (optional, default to 20)
     * @return GetWebhooksResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public GetWebhooksResponse webhooksAll(String xApideckAppId, String cursor, Integer limit) throws ApiException {
        ApiResponse<GetWebhooksResponse> localVarResp = webhooksAllWithHttpInfo(xApideckAppId, cursor, limit);
        return localVarResp.getData();
    }

    /**
     * List webhook subscriptions
     * List all webhook subscriptions
     * @param xApideckAppId The ID of your Unify application (required)
     * @param cursor Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
     * @param limit Number of results to return. Minimum 1, Maximum 200, Default 20 (optional, default to 20)
     * @return ApiResponse&lt;GetWebhooksResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetWebhooksResponse> webhooksAllWithHttpInfo(String xApideckAppId, String cursor, Integer limit) throws ApiException {
        okhttp3.Call localVarCall = webhooksAllValidateBeforeCall(xApideckAppId, cursor, limit, null);
        Type localVarReturnType = new TypeToken<GetWebhooksResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List webhook subscriptions (asynchronously)
     * List all webhook subscriptions
     * @param xApideckAppId The ID of your Unify application (required)
     * @param cursor Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. (optional)
     * @param limit Number of results to return. Minimum 1, Maximum 200, Default 20 (optional, default to 20)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksAllAsync(String xApideckAppId, String cursor, Integer limit, final ApiCallback<GetWebhooksResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = webhooksAllValidateBeforeCall(xApideckAppId, cursor, limit, _callback);
        Type localVarReturnType = new TypeToken<GetWebhooksResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for webhooksDelete
     * @param id JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksDeleteCall(String id, String xApideckAppId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/webhook/webhooks/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xApideckAppId != null) {
            localVarHeaderParams.put("x-apideck-app-id", localVarApiClient.parameterToString(xApideckAppId));
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

        String[] localVarAuthNames = new String[] { "apiKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call webhooksDeleteValidateBeforeCall(String id, String xApideckAppId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling webhooksDelete(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling webhooksDelete(Async)");
        }

        return webhooksDeleteCall(id, xApideckAppId, _callback);

    }

    /**
     * Delete webhook subscription
     * Delete a webhook subscription
     * @param id JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @return DeleteWebhookResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public DeleteWebhookResponse webhooksDelete(String id, String xApideckAppId) throws ApiException {
        ApiResponse<DeleteWebhookResponse> localVarResp = webhooksDeleteWithHttpInfo(id, xApideckAppId);
        return localVarResp.getData();
    }

    /**
     * Delete webhook subscription
     * Delete a webhook subscription
     * @param id JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @return ApiResponse&lt;DeleteWebhookResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteWebhookResponse> webhooksDeleteWithHttpInfo(String id, String xApideckAppId) throws ApiException {
        okhttp3.Call localVarCall = webhooksDeleteValidateBeforeCall(id, xApideckAppId, null);
        Type localVarReturnType = new TypeToken<DeleteWebhookResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete webhook subscription (asynchronously)
     * Delete a webhook subscription
     * @param id JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksDeleteAsync(String id, String xApideckAppId, final ApiCallback<DeleteWebhookResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = webhooksDeleteValidateBeforeCall(id, xApideckAppId, _callback);
        Type localVarReturnType = new TypeToken<DeleteWebhookResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for webhooksOne
     * @param id JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksOneCall(String id, String xApideckAppId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/webhook/webhooks/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xApideckAppId != null) {
            localVarHeaderParams.put("x-apideck-app-id", localVarApiClient.parameterToString(xApideckAppId));
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

        String[] localVarAuthNames = new String[] { "apiKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call webhooksOneValidateBeforeCall(String id, String xApideckAppId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling webhooksOne(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling webhooksOne(Async)");
        }

        return webhooksOneCall(id, xApideckAppId, _callback);

    }

    /**
     * Get webhook subscription
     * Get the webhook subscription details
     * @param id JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @return GetWebhookResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public GetWebhookResponse webhooksOne(String id, String xApideckAppId) throws ApiException {
        ApiResponse<GetWebhookResponse> localVarResp = webhooksOneWithHttpInfo(id, xApideckAppId);
        return localVarResp.getData();
    }

    /**
     * Get webhook subscription
     * Get the webhook subscription details
     * @param id JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @return ApiResponse&lt;GetWebhookResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetWebhookResponse> webhooksOneWithHttpInfo(String id, String xApideckAppId) throws ApiException {
        okhttp3.Call localVarCall = webhooksOneValidateBeforeCall(id, xApideckAppId, null);
        Type localVarReturnType = new TypeToken<GetWebhookResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get webhook subscription (asynchronously)
     * Get the webhook subscription details
     * @param id JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksOneAsync(String id, String xApideckAppId, final ApiCallback<GetWebhookResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = webhooksOneValidateBeforeCall(id, xApideckAppId, _callback);
        Type localVarReturnType = new TypeToken<GetWebhookResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for webhooksUpdate
     * @param id JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param updateWebhookRequest  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksUpdateCall(String id, String xApideckAppId, UpdateWebhookRequest updateWebhookRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateWebhookRequest;

        // create path and map variables
        String localVarPath = "/webhook/webhooks/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xApideckAppId != null) {
            localVarHeaderParams.put("x-apideck-app-id", localVarApiClient.parameterToString(xApideckAppId));
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

        String[] localVarAuthNames = new String[] { "apiKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PATCH", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call webhooksUpdateValidateBeforeCall(String id, String xApideckAppId, UpdateWebhookRequest updateWebhookRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling webhooksUpdate(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling webhooksUpdate(Async)");
        }

        // verify the required parameter 'updateWebhookRequest' is set
        if (updateWebhookRequest == null) {
            throw new ApiException("Missing the required parameter 'updateWebhookRequest' when calling webhooksUpdate(Async)");
        }

        return webhooksUpdateCall(id, xApideckAppId, updateWebhookRequest, _callback);

    }

    /**
     * Update webhook subscription
     * Update a webhook subscription
     * @param id JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param updateWebhookRequest  (required)
     * @return UpdateWebhookResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public UpdateWebhookResponse webhooksUpdate(String id, String xApideckAppId, UpdateWebhookRequest updateWebhookRequest) throws ApiException {
        ApiResponse<UpdateWebhookResponse> localVarResp = webhooksUpdateWithHttpInfo(id, xApideckAppId, updateWebhookRequest);
        return localVarResp.getData();
    }

    /**
     * Update webhook subscription
     * Update a webhook subscription
     * @param id JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param updateWebhookRequest  (required)
     * @return ApiResponse&lt;UpdateWebhookResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateWebhookResponse> webhooksUpdateWithHttpInfo(String id, String xApideckAppId, UpdateWebhookRequest updateWebhookRequest) throws ApiException {
        okhttp3.Call localVarCall = webhooksUpdateValidateBeforeCall(id, xApideckAppId, updateWebhookRequest, null);
        Type localVarReturnType = new TypeToken<UpdateWebhookResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update webhook subscription (asynchronously)
     * Update a webhook subscription
     * @param id JWT Webhook token that represents the unifiedApi and applicationId associated to the event source. (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param updateWebhookRequest  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Webhooks </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call webhooksUpdateAsync(String id, String xApideckAppId, UpdateWebhookRequest updateWebhookRequest, final ApiCallback<UpdateWebhookResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = webhooksUpdateValidateBeforeCall(id, xApideckAppId, updateWebhookRequest, _callback);
        Type localVarReturnType = new TypeToken<UpdateWebhookResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
