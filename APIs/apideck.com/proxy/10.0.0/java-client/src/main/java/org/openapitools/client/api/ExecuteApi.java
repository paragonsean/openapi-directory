/*
 * Proxy API
 * Welcome to the Proxy API.  You can use this API to access all Proxy API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                               | Type   | Required | Description | | ---------------------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | | Authorization                      | String | Yes      | Bearer API KEY | | x-apideck-app-id                   | String | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys. | | x-apideck-consumer-id              | String | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app.                       | | x-apideck-downstream-url           | String | Yes      | Downstream URL to forward the request too | | x-apideck-downstream-authorization | String | No       | Downstream authorization header. This will skip the Vault token injection. | | x-apideck-downstream-method        | String | No       | Downstream method. If not provided the upstream method will be inherited, depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. | | x-apideck-service-id               | String | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.                                   |  ## Authorization  You can interact with the API through the authorization methods below.  ### apiKey  To use API you have to sign up and get your own API key. Unify API accounts have sandbox mode and live mode API keys. To change modes just use the appropriate key to get a live or test object. You can find your API keys on the unify settings of your Apideck app. Your Apideck application_id can also be found on the same page.  Authenticate your API requests by including your test or live secret API key in the request header.  - Bearer authorization header: Authorization: Bearer <your-apideck-api-key> - Application id header: x-apideck-app-id: <your-apideck-app-id>   You should use the public keys on the SDKs and the secret keys to authenticate API requests.  **Do not share or include your secret API keys on client side code.** Your API keys carry significant privileges. Please ensure to keep them 100% secure and be sure to not share your secret API keys in areas that are publicly accessible like GitHub.  Learn how to set the Authorization header inside Postman https://learning.postman.com/docs/postman/sending-api-requests/authorization/#api-key  Go to Unify to grab your API KEY https://app.apideck.com/unify/api-keys  | Security Scheme Type      | HTTP   | | ------------------------- | ------ | | HTTP Authorization Scheme | bearer |  ### applicationId  The ID of your Unify application  | Security Scheme Type  | API Key          | | --------------------- | ---------------- | | Header parameter name | x-apideck-app-id |  ## Static IP  Some of the APIs you want to use can require a static IP. Apideck's static IP feature allows you to the Proxy API with a fixed IP avoiding the need for you to set up your own infrastructure. This feature is currently available to all Apideck customers. To use this feature, the API Vendor will need to whitelist the associated static IP addresses. The provided static IP addresses are fixed to their specified region and shared by all customers who use this feature.  - EU Central 1: **18.197.244.247** - Other: upcoming    More info about our data security can be found at [https://compliance.apideck.com/](https://compliance.apideck.com/)  ## Limitations  ### Timeout  The request timeout is set at 30 seconds.  ### Response Size  The Proxy API has no response size limit. For responses larger than 2MB, the Proxy API will redirect to a temporary URL. In this case the usual Apideck response headers will be returned in the redirect response. Most HTTP clients will handle this redirect automatically.  ``` GET /proxy < 301 Moved Permanently < x-apideck-request-id: {{requestId}} < Location: {{temporaryUrl}}  GET {{temporaryUrl}} < {{responseBody}} ```  ## SDKs and API Clients  Upcoming. [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created. | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body. | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource. | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue. | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request. | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource. | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later. | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue. |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
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


import org.openapitools.client.model.GetProxy401Response;
import org.openapitools.client.model.PostProxyRequest;
import org.openapitools.client.model.PutProxyRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ExecuteApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ExecuteApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ExecuteApi(ApiClient apiClient) {
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
     * Build call for deleteProxy
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call deleteProxyCall(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/proxy";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xApideckConsumerId != null) {
            localVarHeaderParams.put("x-apideck-consumer-id", localVarApiClient.parameterToString(xApideckConsumerId));
        }

        if (xApideckAppId != null) {
            localVarHeaderParams.put("x-apideck-app-id", localVarApiClient.parameterToString(xApideckAppId));
        }

        if (xApideckServiceId != null) {
            localVarHeaderParams.put("x-apideck-service-id", localVarApiClient.parameterToString(xApideckServiceId));
        }

        if (xApideckDownstreamUrl != null) {
            localVarHeaderParams.put("x-apideck-downstream-url", localVarApiClient.parameterToString(xApideckDownstreamUrl));
        }

        if (xApideckDownstreamAuthorization != null) {
            localVarHeaderParams.put("x-apideck-downstream-authorization", localVarApiClient.parameterToString(xApideckDownstreamAuthorization));
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
    private okhttp3.Call deleteProxyValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling deleteProxy(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling deleteProxy(Async)");
        }

        // verify the required parameter 'xApideckServiceId' is set
        if (xApideckServiceId == null) {
            throw new ApiException("Missing the required parameter 'xApideckServiceId' when calling deleteProxy(Async)");
        }

        // verify the required parameter 'xApideckDownstreamUrl' is set
        if (xApideckDownstreamUrl == null) {
            throw new ApiException("Missing the required parameter 'xApideckDownstreamUrl' when calling deleteProxy(Async)");
        }

        return deleteProxyCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, _callback);

    }

    /**
     * DELETE
     * Proxies a downstream DELETE request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public Object deleteProxy(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization) throws ApiException {
        ApiResponse<Object> localVarResp = deleteProxyWithHttpInfo(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization);
        return localVarResp.getData();
    }

    /**
     * DELETE
     * Proxies a downstream DELETE request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<Object> deleteProxyWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization) throws ApiException {
        okhttp3.Call localVarCall = deleteProxyValidateBeforeCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * DELETE (asynchronously)
     * Proxies a downstream DELETE request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call deleteProxyAsync(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteProxyValidateBeforeCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getProxy
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getProxyCall(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/proxy";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xApideckConsumerId != null) {
            localVarHeaderParams.put("x-apideck-consumer-id", localVarApiClient.parameterToString(xApideckConsumerId));
        }

        if (xApideckAppId != null) {
            localVarHeaderParams.put("x-apideck-app-id", localVarApiClient.parameterToString(xApideckAppId));
        }

        if (xApideckServiceId != null) {
            localVarHeaderParams.put("x-apideck-service-id", localVarApiClient.parameterToString(xApideckServiceId));
        }

        if (xApideckDownstreamUrl != null) {
            localVarHeaderParams.put("x-apideck-downstream-url", localVarApiClient.parameterToString(xApideckDownstreamUrl));
        }

        if (xApideckDownstreamAuthorization != null) {
            localVarHeaderParams.put("x-apideck-downstream-authorization", localVarApiClient.parameterToString(xApideckDownstreamAuthorization));
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
    private okhttp3.Call getProxyValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling getProxy(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling getProxy(Async)");
        }

        // verify the required parameter 'xApideckServiceId' is set
        if (xApideckServiceId == null) {
            throw new ApiException("Missing the required parameter 'xApideckServiceId' when calling getProxy(Async)");
        }

        // verify the required parameter 'xApideckDownstreamUrl' is set
        if (xApideckDownstreamUrl == null) {
            throw new ApiException("Missing the required parameter 'xApideckDownstreamUrl' when calling getProxy(Async)");
        }

        return getProxyCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, _callback);

    }

    /**
     * GET
     * Proxies a downstream GET request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public Object getProxy(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization) throws ApiException {
        ApiResponse<Object> localVarResp = getProxyWithHttpInfo(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization);
        return localVarResp.getData();
    }

    /**
     * GET
     * Proxies a downstream GET request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<Object> getProxyWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization) throws ApiException {
        okhttp3.Call localVarCall = getProxyValidateBeforeCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * GET (asynchronously)
     * Proxies a downstream GET request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getProxyAsync(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = getProxyValidateBeforeCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for optionsProxy
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call optionsProxyCall(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/proxy";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xApideckConsumerId != null) {
            localVarHeaderParams.put("x-apideck-consumer-id", localVarApiClient.parameterToString(xApideckConsumerId));
        }

        if (xApideckAppId != null) {
            localVarHeaderParams.put("x-apideck-app-id", localVarApiClient.parameterToString(xApideckAppId));
        }

        if (xApideckServiceId != null) {
            localVarHeaderParams.put("x-apideck-service-id", localVarApiClient.parameterToString(xApideckServiceId));
        }

        if (xApideckDownstreamUrl != null) {
            localVarHeaderParams.put("x-apideck-downstream-url", localVarApiClient.parameterToString(xApideckDownstreamUrl));
        }

        if (xApideckDownstreamAuthorization != null) {
            localVarHeaderParams.put("x-apideck-downstream-authorization", localVarApiClient.parameterToString(xApideckDownstreamAuthorization));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "OPTIONS", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call optionsProxyValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling optionsProxy(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling optionsProxy(Async)");
        }

        // verify the required parameter 'xApideckServiceId' is set
        if (xApideckServiceId == null) {
            throw new ApiException("Missing the required parameter 'xApideckServiceId' when calling optionsProxy(Async)");
        }

        // verify the required parameter 'xApideckDownstreamUrl' is set
        if (xApideckDownstreamUrl == null) {
            throw new ApiException("Missing the required parameter 'xApideckDownstreamUrl' when calling optionsProxy(Async)");
        }

        return optionsProxyCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, _callback);

    }

    /**
     * OPTIONS
     * Proxies a downstream OPTION request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public Object optionsProxy(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization) throws ApiException {
        ApiResponse<Object> localVarResp = optionsProxyWithHttpInfo(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization);
        return localVarResp.getData();
    }

    /**
     * OPTIONS
     * Proxies a downstream OPTION request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<Object> optionsProxyWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization) throws ApiException {
        okhttp3.Call localVarCall = optionsProxyValidateBeforeCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * OPTIONS (asynchronously)
     * Proxies a downstream OPTION request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call optionsProxyAsync(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = optionsProxyValidateBeforeCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for patchProxy
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param postProxyRequest Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call patchProxyCall(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PostProxyRequest postProxyRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = postProxyRequest;

        // create path and map variables
        String localVarPath = "/proxy";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xApideckConsumerId != null) {
            localVarHeaderParams.put("x-apideck-consumer-id", localVarApiClient.parameterToString(xApideckConsumerId));
        }

        if (xApideckAppId != null) {
            localVarHeaderParams.put("x-apideck-app-id", localVarApiClient.parameterToString(xApideckAppId));
        }

        if (xApideckServiceId != null) {
            localVarHeaderParams.put("x-apideck-service-id", localVarApiClient.parameterToString(xApideckServiceId));
        }

        if (xApideckDownstreamUrl != null) {
            localVarHeaderParams.put("x-apideck-downstream-url", localVarApiClient.parameterToString(xApideckDownstreamUrl));
        }

        if (xApideckDownstreamAuthorization != null) {
            localVarHeaderParams.put("x-apideck-downstream-authorization", localVarApiClient.parameterToString(xApideckDownstreamAuthorization));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "PATCH", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call patchProxyValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PostProxyRequest postProxyRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling patchProxy(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling patchProxy(Async)");
        }

        // verify the required parameter 'xApideckServiceId' is set
        if (xApideckServiceId == null) {
            throw new ApiException("Missing the required parameter 'xApideckServiceId' when calling patchProxy(Async)");
        }

        // verify the required parameter 'xApideckDownstreamUrl' is set
        if (xApideckDownstreamUrl == null) {
            throw new ApiException("Missing the required parameter 'xApideckDownstreamUrl' when calling patchProxy(Async)");
        }

        return patchProxyCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, postProxyRequest, _callback);

    }

    /**
     * PATCH
     * Proxies a downstream PATCH request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param postProxyRequest Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public Object patchProxy(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PostProxyRequest postProxyRequest) throws ApiException {
        ApiResponse<Object> localVarResp = patchProxyWithHttpInfo(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, postProxyRequest);
        return localVarResp.getData();
    }

    /**
     * PATCH
     * Proxies a downstream PATCH request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param postProxyRequest Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<Object> patchProxyWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PostProxyRequest postProxyRequest) throws ApiException {
        okhttp3.Call localVarCall = patchProxyValidateBeforeCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, postProxyRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * PATCH (asynchronously)
     * Proxies a downstream PATCH request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param postProxyRequest Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call patchProxyAsync(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PostProxyRequest postProxyRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = patchProxyValidateBeforeCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, postProxyRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for postProxy
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param postProxyRequest Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call postProxyCall(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PostProxyRequest postProxyRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = postProxyRequest;

        // create path and map variables
        String localVarPath = "/proxy";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xApideckConsumerId != null) {
            localVarHeaderParams.put("x-apideck-consumer-id", localVarApiClient.parameterToString(xApideckConsumerId));
        }

        if (xApideckAppId != null) {
            localVarHeaderParams.put("x-apideck-app-id", localVarApiClient.parameterToString(xApideckAppId));
        }

        if (xApideckServiceId != null) {
            localVarHeaderParams.put("x-apideck-service-id", localVarApiClient.parameterToString(xApideckServiceId));
        }

        if (xApideckDownstreamUrl != null) {
            localVarHeaderParams.put("x-apideck-downstream-url", localVarApiClient.parameterToString(xApideckDownstreamUrl));
        }

        if (xApideckDownstreamAuthorization != null) {
            localVarHeaderParams.put("x-apideck-downstream-authorization", localVarApiClient.parameterToString(xApideckDownstreamAuthorization));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call postProxyValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PostProxyRequest postProxyRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling postProxy(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling postProxy(Async)");
        }

        // verify the required parameter 'xApideckServiceId' is set
        if (xApideckServiceId == null) {
            throw new ApiException("Missing the required parameter 'xApideckServiceId' when calling postProxy(Async)");
        }

        // verify the required parameter 'xApideckDownstreamUrl' is set
        if (xApideckDownstreamUrl == null) {
            throw new ApiException("Missing the required parameter 'xApideckDownstreamUrl' when calling postProxy(Async)");
        }

        return postProxyCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, postProxyRequest, _callback);

    }

    /**
     * POST
     * Proxies a downstream POST request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param postProxyRequest Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public Object postProxy(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PostProxyRequest postProxyRequest) throws ApiException {
        ApiResponse<Object> localVarResp = postProxyWithHttpInfo(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, postProxyRequest);
        return localVarResp.getData();
    }

    /**
     * POST
     * Proxies a downstream POST request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param postProxyRequest Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<Object> postProxyWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PostProxyRequest postProxyRequest) throws ApiException {
        okhttp3.Call localVarCall = postProxyValidateBeforeCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, postProxyRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * POST (asynchronously)
     * Proxies a downstream POST request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param postProxyRequest Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call postProxyAsync(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PostProxyRequest postProxyRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = postProxyValidateBeforeCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, postProxyRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putProxy
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param putProxyRequest Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call putProxyCall(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PutProxyRequest putProxyRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = putProxyRequest;

        // create path and map variables
        String localVarPath = "/proxy";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xApideckConsumerId != null) {
            localVarHeaderParams.put("x-apideck-consumer-id", localVarApiClient.parameterToString(xApideckConsumerId));
        }

        if (xApideckAppId != null) {
            localVarHeaderParams.put("x-apideck-app-id", localVarApiClient.parameterToString(xApideckAppId));
        }

        if (xApideckServiceId != null) {
            localVarHeaderParams.put("x-apideck-service-id", localVarApiClient.parameterToString(xApideckServiceId));
        }

        if (xApideckDownstreamUrl != null) {
            localVarHeaderParams.put("x-apideck-downstream-url", localVarApiClient.parameterToString(xApideckDownstreamUrl));
        }

        if (xApideckDownstreamAuthorization != null) {
            localVarHeaderParams.put("x-apideck-downstream-authorization", localVarApiClient.parameterToString(xApideckDownstreamAuthorization));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putProxyValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PutProxyRequest putProxyRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling putProxy(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling putProxy(Async)");
        }

        // verify the required parameter 'xApideckServiceId' is set
        if (xApideckServiceId == null) {
            throw new ApiException("Missing the required parameter 'xApideckServiceId' when calling putProxy(Async)");
        }

        // verify the required parameter 'xApideckDownstreamUrl' is set
        if (xApideckDownstreamUrl == null) {
            throw new ApiException("Missing the required parameter 'xApideckDownstreamUrl' when calling putProxy(Async)");
        }

        return putProxyCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, putProxyRequest, _callback);

    }

    /**
     * PUT
     * Proxies a downstream PUT request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param putProxyRequest Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public Object putProxy(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PutProxyRequest putProxyRequest) throws ApiException {
        ApiResponse<Object> localVarResp = putProxyWithHttpInfo(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, putProxyRequest);
        return localVarResp.getData();
    }

    /**
     * PUT
     * Proxies a downstream PUT request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param putProxyRequest Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<Object> putProxyWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PutProxyRequest putProxyRequest) throws ApiException {
        okhttp3.Call localVarCall = putProxyValidateBeforeCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, putProxyRequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * PUT (asynchronously)
     * Proxies a downstream PUT request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param xApideckServiceId Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. (required)
     * @param xApideckDownstreamUrl Downstream URL (required)
     * @param xApideckDownstreamAuthorization Downstream authorization header. This will skip the Vault token injection. (optional)
     * @param putProxyRequest Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Ok </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Proxy error </td><td>  * x-apideck-downstream-error -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call putProxyAsync(String xApideckConsumerId, String xApideckAppId, String xApideckServiceId, String xApideckDownstreamUrl, String xApideckDownstreamAuthorization, PutProxyRequest putProxyRequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = putProxyValidateBeforeCall(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, putProxyRequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
