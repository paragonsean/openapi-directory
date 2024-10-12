/*
 * Vault API
 * Welcome to the Vault API 👋  When you're looking to connect to an API, the first step is authentication.  Vault helps you handle OAuth flows, store API keys, and refresh access tokens from users (called consumers in Apideck).  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Get Started  To use the Apideck APIs, you need to sign up for free at [https://app.apideck.com/signup](). Follow the steps below to get started.  - [Create a free account.](https://app.apideck.com/signup) - Go to the [Dashboard](https://app.apideck.com/unify/unified-apis/dashboard). - Get your API key and the application ID. - Select and configure the integrations you want to make available to your users. Through the Unify dashboard, you can configure which connectors you want to support as integrations. - Retrieve the client_id and client_secret for the integration you want to activate (Only needed for OAuth integrations). - Soon, you can skip the previous step and use the Apideck sandbox credentials to get you started instead (upcoming) - Register the redirect URI for the example app (https://unify.apideck.com/vault/callback) in the list of redirect URIs under your app's settings - Use the [publishing guides](/app-listing-requirements) to get your integration listed across app marketplaces.  ### Hosted Vault  Hosted Vault (vault.apideck.com) is a no-code solution, so you don't need to build your own UI to handle the integration settings and authentication.  ![Hosted Vault - Integrations portal](https://github.com/apideck-samples/integration-settings/raw/master/public/img/vault.png)  Behind the scenes, Hosted Vault implements the Vault API endpoints and handles the following features for your customers:  - Add a connection - Handle the OAuth flow - Configure connection settings per integration - Manage connections - Discover and propose integration options - Search for integrations (upcoming) - Give integration suggestions based on provided metadata (email or website) when creating the session (upcoming)  To use Hosted Vault, you will need to first [**create a session**](https://developers.apideck.com/apis/vault/reference#operation/sessionsCreate). This can be achieved by making a POST request to the Vault API to create a valid session for a user, hereafter referred to as the consumer ID.  Example using curl:  ``` curl -X POST https://unify.apideck.com/vault/sessions     -H \"Content-Type: application/json\"     -H \"Authorization: Bearer <your-api-key>\"     -H \"X-APIDECK-CONSUMER-ID: <consumer-id>\"     -H \"X-APIDECK-APP-ID: <application-id>\"     -d '{\"consumer_metadata\": { \"account_name\" : \"Sample\", \"user_name\": \"Sand Box\", \"email\": \"sand@box.com\", \"image\": \"https://unavatar.now.sh/jake\" }, \"theme\": { \"vault_name\": \"Intercom\", \"primary_color\": \"#286efa\", \"sidepanel_background_color\": \"#286efa\",\"sidepanel_text_color\": \"#FFFFFF\", \"favicon\": \"https://res.cloudinary.com/apideck/icons/intercom\" }}' ```  ### Vault API  _Beware, this is strategy takes more time to implement in comparison to Hosted Vault._  If you are building your integration settings UI manually, you can call the Vault API directly.  The Vault API is for those who want to completely white label the in-app integrations overview and authentication experience. All the available endpoints are listed below.  Through the API, your customers authenticate directly in your app, where Vault will still take care of redirecting to the auth provider and back to your app.  If you're already storing access tokens, we will help you migrate through our Vault Migration API (upcoming).  ## Domain model  At its core, a domain model creates a web of interconnected entities.  Our domain model contains five main entity types: Consumer (user, account, team, machine), Application, Connector, Integration, and Connection.  ## Connection state  The connection state is computed based on the connection flow below.  ![](https://developers.apideck.com/api-references/vault/connection-flow.png)  More information about the connection state can be found in the [Connection state](https://developers.apideck.com/guides/connection-states) guide.  ## Unify and Proxy integration  The only thing you need to use the Unify APIs and Proxy is the consumer id; thereafter, Vault will do the look-up in the background to handle the token injection before performing the API call(s).  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-app-id      | String  | Yes      | The id of your Unify application. Available at https://app.apideck.com/api-keys. | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes. |  ## Guides  - [Get started with Apideck](https://developers.apideck.com/getting-started) - [Get started with Vault](https://developers.apideck.com/guides/vault) - [Authorize connection via Vault](https://developers.apideck.com/guides/authorize-connections) - [Vault connection status](https://developers.apideck.com/guides/connection-states) - [How to build an integrations UI with Vault](https://github.com/apideck-samples/integration-settings)   ## FAQ  **What purpose does Vault serve? Can I just handle the authentication and access token myself?** You can store everything yourself, but that defeats the purpose of using Apideck Unify. Handling tokens for multiple providers can quickly become very complex.  ### Is my data secure?  Vault employs data minimization, therefore only requesting the minimum amount of scopes needed to perform an API request.  ### How do I migrate existing data?  Using our migration API, you can migrate the access tokens and accounts to Apideck Vault.  ### Can I use Vault in combination with existing integrations?  Yes, you can. The flexibility of Unify allows you to quickly the use cases you need while keeping a gradual migration path based on your timeline and requirements.  ### How does Vault work for Apideck Ecosystem customers?  Once logged in, pick your ecosystem; on the left-hand side of the screen, you'll have the option to create an application underneath the Unify section.  ### How to integrate Apideck Vault  This section covers everything you need to know to authenticate your customers through Vault. Vault provides **three auth strategies** to use API tokens from your customers:  - Vault API - Hosted Vault - Vault Widget (JS, React, Vue)  You can also opt to bypass Vault and still take care of authentication flows yourself. Make sure to put the right safeguards in place to protect your customers' tokens and other sensitive data.  ### What auth types does Vault support?  We support all the common authentication types, including: API keys, OAuth, Basic auth, and more.  #### API keys  For Services supporting the API key strategy, you can use Hosted Vault will need to provide an in-app form where users can configure their API keys provided by the integration service.  #### OAuth 2.0  ##### Authorization Code Grant Type Flow  Vault handles the complete Authorization Code Grant Type Flow for you. This flow only supports browser-based (passive) authentication because most identity providers don't allow entering a username and password to be entered into applications that they don't own.  Certain connectors require an OAuth redirect authentication flow, where the end-user is redirected to the provider's website or mobile app to authenticate.  This is being handled by the `/authorize` endpoint.  #### Basic auth  Basic authentication is a simple authentication scheme built into the HTTP protocol. The required fields to complete basic auth are handled by Hosted Vault or by updating the connection through the Vault API below.  
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
import org.openapitools.client.model.Connection;
import org.openapitools.client.model.ConnectionImportData;
import org.openapitools.client.model.CreateConnectionResponse;
import org.openapitools.client.model.GetConnectionResponse;
import org.openapitools.client.model.GetConnectionsResponse;
import org.openapitools.client.model.GetCustomFieldsResponse;
import org.openapitools.client.model.NotFoundResponse;
import org.openapitools.client.model.PaymentRequiredResponse;
import org.openapitools.client.model.UnauthorizedResponse;
import org.openapitools.client.model.UnexpectedErrorResponse;
import org.openapitools.client.model.UnprocessableResponse;
import org.openapitools.client.model.UpdateConnectionResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ConnectionsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ConnectionsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ConnectionsApi(ApiClient apiClient) {
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
     * Build call for connectionSettingsAll
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param unifiedApi Unified API (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param resource Name of the resource (plural) (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionSettingsAllCall(String xApideckConsumerId, String xApideckAppId, String unifiedApi, String serviceId, String resource, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vault/connections/{unified_api}/{service_id}/{resource}/config"
            .replace("{" + "unified_api" + "}", localVarApiClient.escapeString(unifiedApi.toString()))
            .replace("{" + "service_id" + "}", localVarApiClient.escapeString(serviceId.toString()))
            .replace("{" + "resource" + "}", localVarApiClient.escapeString(resource.toString()));

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
    private okhttp3.Call connectionSettingsAllValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String unifiedApi, String serviceId, String resource, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling connectionSettingsAll(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling connectionSettingsAll(Async)");
        }

        // verify the required parameter 'unifiedApi' is set
        if (unifiedApi == null) {
            throw new ApiException("Missing the required parameter 'unifiedApi' when calling connectionSettingsAll(Async)");
        }

        // verify the required parameter 'serviceId' is set
        if (serviceId == null) {
            throw new ApiException("Missing the required parameter 'serviceId' when calling connectionSettingsAll(Async)");
        }

        // verify the required parameter 'resource' is set
        if (resource == null) {
            throw new ApiException("Missing the required parameter 'resource' when calling connectionSettingsAll(Async)");
        }

        return connectionSettingsAllCall(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource, _callback);

    }

    /**
     * Get resource settings
     * This endpoint returns custom settings and their defaults required by connection for a given resource. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param unifiedApi Unified API (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param resource Name of the resource (plural) (required)
     * @return GetConnectionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public GetConnectionResponse connectionSettingsAll(String xApideckConsumerId, String xApideckAppId, String unifiedApi, String serviceId, String resource) throws ApiException {
        ApiResponse<GetConnectionResponse> localVarResp = connectionSettingsAllWithHttpInfo(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource);
        return localVarResp.getData();
    }

    /**
     * Get resource settings
     * This endpoint returns custom settings and their defaults required by connection for a given resource. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param unifiedApi Unified API (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param resource Name of the resource (plural) (required)
     * @return ApiResponse&lt;GetConnectionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetConnectionResponse> connectionSettingsAllWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String unifiedApi, String serviceId, String resource) throws ApiException {
        okhttp3.Call localVarCall = connectionSettingsAllValidateBeforeCall(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource, null);
        Type localVarReturnType = new TypeToken<GetConnectionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get resource settings (asynchronously)
     * This endpoint returns custom settings and their defaults required by connection for a given resource. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param unifiedApi Unified API (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param resource Name of the resource (plural) (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionSettingsAllAsync(String xApideckConsumerId, String xApideckAppId, String unifiedApi, String serviceId, String resource, final ApiCallback<GetConnectionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = connectionSettingsAllValidateBeforeCall(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource, _callback);
        Type localVarReturnType = new TypeToken<GetConnectionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for connectionSettingsUpdate
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param resource Name of the resource (plural) (required)
     * @param connection Fields that need to be updated on the resource (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection updated </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionSettingsUpdateCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, String resource, Connection connection, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = connection;

        // create path and map variables
        String localVarPath = "/vault/connections/{unified_api}/{service_id}/{resource}/config"
            .replace("{" + "service_id" + "}", localVarApiClient.escapeString(serviceId.toString()))
            .replace("{" + "unified_api" + "}", localVarApiClient.escapeString(unifiedApi.toString()))
            .replace("{" + "resource" + "}", localVarApiClient.escapeString(resource.toString()));

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
    private okhttp3.Call connectionSettingsUpdateValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, String resource, Connection connection, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling connectionSettingsUpdate(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling connectionSettingsUpdate(Async)");
        }

        // verify the required parameter 'serviceId' is set
        if (serviceId == null) {
            throw new ApiException("Missing the required parameter 'serviceId' when calling connectionSettingsUpdate(Async)");
        }

        // verify the required parameter 'unifiedApi' is set
        if (unifiedApi == null) {
            throw new ApiException("Missing the required parameter 'unifiedApi' when calling connectionSettingsUpdate(Async)");
        }

        // verify the required parameter 'resource' is set
        if (resource == null) {
            throw new ApiException("Missing the required parameter 'resource' when calling connectionSettingsUpdate(Async)");
        }

        // verify the required parameter 'connection' is set
        if (connection == null) {
            throw new ApiException("Missing the required parameter 'connection' when calling connectionSettingsUpdate(Async)");
        }

        return connectionSettingsUpdateCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, resource, connection, _callback);

    }

    /**
     * Update settings
     * Update default values for a connection&#39;s resource settings
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param resource Name of the resource (plural) (required)
     * @param connection Fields that need to be updated on the resource (required)
     * @return UpdateConnectionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection updated </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public UpdateConnectionResponse connectionSettingsUpdate(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, String resource, Connection connection) throws ApiException {
        ApiResponse<UpdateConnectionResponse> localVarResp = connectionSettingsUpdateWithHttpInfo(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, resource, connection);
        return localVarResp.getData();
    }

    /**
     * Update settings
     * Update default values for a connection&#39;s resource settings
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param resource Name of the resource (plural) (required)
     * @param connection Fields that need to be updated on the resource (required)
     * @return ApiResponse&lt;UpdateConnectionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection updated </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateConnectionResponse> connectionSettingsUpdateWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, String resource, Connection connection) throws ApiException {
        okhttp3.Call localVarCall = connectionSettingsUpdateValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, resource, connection, null);
        Type localVarReturnType = new TypeToken<UpdateConnectionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update settings (asynchronously)
     * Update default values for a connection&#39;s resource settings
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param resource Name of the resource (plural) (required)
     * @param connection Fields that need to be updated on the resource (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection updated </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionSettingsUpdateAsync(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, String resource, Connection connection, final ApiCallback<UpdateConnectionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = connectionSettingsUpdateValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, resource, connection, _callback);
        Type localVarReturnType = new TypeToken<UpdateConnectionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for connectionsAdd
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param connection Fields that need to be persisted on the resource (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsAddCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Connection connection, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = connection;

        // create path and map variables
        String localVarPath = "/vault/connections/{unified_api}/{service_id}"
            .replace("{" + "service_id" + "}", localVarApiClient.escapeString(serviceId.toString()))
            .replace("{" + "unified_api" + "}", localVarApiClient.escapeString(unifiedApi.toString()));

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
    private okhttp3.Call connectionsAddValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Connection connection, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling connectionsAdd(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling connectionsAdd(Async)");
        }

        // verify the required parameter 'serviceId' is set
        if (serviceId == null) {
            throw new ApiException("Missing the required parameter 'serviceId' when calling connectionsAdd(Async)");
        }

        // verify the required parameter 'unifiedApi' is set
        if (unifiedApi == null) {
            throw new ApiException("Missing the required parameter 'unifiedApi' when calling connectionsAdd(Async)");
        }

        // verify the required parameter 'connection' is set
        if (connection == null) {
            throw new ApiException("Missing the required parameter 'connection' when calling connectionsAdd(Async)");
        }

        return connectionsAddCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection, _callback);

    }

    /**
     * Create connection
     * Create an authorized connection 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param connection Fields that need to be persisted on the resource (required)
     * @return CreateConnectionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public CreateConnectionResponse connectionsAdd(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Connection connection) throws ApiException {
        ApiResponse<CreateConnectionResponse> localVarResp = connectionsAddWithHttpInfo(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection);
        return localVarResp.getData();
    }

    /**
     * Create connection
     * Create an authorized connection 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param connection Fields that need to be persisted on the resource (required)
     * @return ApiResponse&lt;CreateConnectionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateConnectionResponse> connectionsAddWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Connection connection) throws ApiException {
        okhttp3.Call localVarCall = connectionsAddValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection, null);
        Type localVarReturnType = new TypeToken<CreateConnectionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create connection (asynchronously)
     * Create an authorized connection 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param connection Fields that need to be persisted on the resource (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsAddAsync(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Connection connection, final ApiCallback<CreateConnectionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = connectionsAddValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection, _callback);
        Type localVarReturnType = new TypeToken<CreateConnectionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for connectionsAll
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param api Scope results to Unified API (optional)
     * @param configured Scopes results to connections that have been configured or not (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connections </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsAllCall(String xApideckConsumerId, String xApideckAppId, String api, Boolean configured, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vault/connections";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (api != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("api", api));
        }

        if (configured != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("configured", configured));
        }

        if (xApideckConsumerId != null) {
            localVarHeaderParams.put("x-apideck-consumer-id", localVarApiClient.parameterToString(xApideckConsumerId));
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
    private okhttp3.Call connectionsAllValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String api, Boolean configured, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling connectionsAll(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling connectionsAll(Async)");
        }

        return connectionsAllCall(xApideckConsumerId, xApideckAppId, api, configured, _callback);

    }

    /**
     * Get all connections
     * This endpoint includes all the configured integrations and contains the required assets to build an integrations page where your users can install integrations. OAuth2 supported integrations will contain authorize and revoke links to handle the authentication flows. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param api Scope results to Unified API (optional)
     * @param configured Scopes results to connections that have been configured or not (optional)
     * @return GetConnectionsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connections </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public GetConnectionsResponse connectionsAll(String xApideckConsumerId, String xApideckAppId, String api, Boolean configured) throws ApiException {
        ApiResponse<GetConnectionsResponse> localVarResp = connectionsAllWithHttpInfo(xApideckConsumerId, xApideckAppId, api, configured);
        return localVarResp.getData();
    }

    /**
     * Get all connections
     * This endpoint includes all the configured integrations and contains the required assets to build an integrations page where your users can install integrations. OAuth2 supported integrations will contain authorize and revoke links to handle the authentication flows. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param api Scope results to Unified API (optional)
     * @param configured Scopes results to connections that have been configured or not (optional)
     * @return ApiResponse&lt;GetConnectionsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connections </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetConnectionsResponse> connectionsAllWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String api, Boolean configured) throws ApiException {
        okhttp3.Call localVarCall = connectionsAllValidateBeforeCall(xApideckConsumerId, xApideckAppId, api, configured, null);
        Type localVarReturnType = new TypeToken<GetConnectionsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get all connections (asynchronously)
     * This endpoint includes all the configured integrations and contains the required assets to build an integrations page where your users can install integrations. OAuth2 supported integrations will contain authorize and revoke links to handle the authentication flows. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param api Scope results to Unified API (optional)
     * @param configured Scopes results to connections that have been configured or not (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connections </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsAllAsync(String xApideckConsumerId, String xApideckAppId, String api, Boolean configured, final ApiCallback<GetConnectionsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = connectionsAllValidateBeforeCall(xApideckConsumerId, xApideckAppId, api, configured, _callback);
        Type localVarReturnType = new TypeToken<GetConnectionsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for connectionsAuthorize
     * @param serviceId Service ID of the resource to return (required)
     * @param applicationId Application ID of the resource to return (required)
     * @param state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. (required)
     * @param redirectUri URL to redirect back to after authorization. When left empty the default configured redirect uri will be used. (required)
     * @param scope One or more OAuth scopes to request from the connector. OAuth scopes control the set of resources and operations that are allowed after authorization. Refer to the connector&#39;s documentation for the available scopes. (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 301 </td><td> redirect </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsAuthorizeCall(String serviceId, String applicationId, String state, String redirectUri, List<String> scope, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vault/authorize/{service_id}/{application_id}"
            .replace("{" + "service_id" + "}", localVarApiClient.escapeString(serviceId.toString()))
            .replace("{" + "application_id" + "}", localVarApiClient.escapeString(applicationId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (state != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("state", state));
        }

        if (redirectUri != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("redirect_uri", redirectUri));
        }

        if (scope != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("ssv", "scope", scope));
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
    private okhttp3.Call connectionsAuthorizeValidateBeforeCall(String serviceId, String applicationId, String state, String redirectUri, List<String> scope, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'serviceId' is set
        if (serviceId == null) {
            throw new ApiException("Missing the required parameter 'serviceId' when calling connectionsAuthorize(Async)");
        }

        // verify the required parameter 'applicationId' is set
        if (applicationId == null) {
            throw new ApiException("Missing the required parameter 'applicationId' when calling connectionsAuthorize(Async)");
        }

        // verify the required parameter 'state' is set
        if (state == null) {
            throw new ApiException("Missing the required parameter 'state' when calling connectionsAuthorize(Async)");
        }

        // verify the required parameter 'redirectUri' is set
        if (redirectUri == null) {
            throw new ApiException("Missing the required parameter 'redirectUri' when calling connectionsAuthorize(Async)");
        }

        return connectionsAuthorizeCall(serviceId, applicationId, state, redirectUri, scope, _callback);

    }

    /**
     * Authorize
     * __In most cases the authorize link is provided in the &#x60;&#x60;/connections&#x60;&#x60; endpoint. Normally you don&#39;t need to manually generate these links.__  Use this endpoint to authenticate a user with a connector. It will return a 301 redirect to the downstream connector endpoints.  Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.  Vault handles the complete Authorization Code Grant Type Flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application. 
     * @param serviceId Service ID of the resource to return (required)
     * @param applicationId Application ID of the resource to return (required)
     * @param state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. (required)
     * @param redirectUri URL to redirect back to after authorization. When left empty the default configured redirect uri will be used. (required)
     * @param scope One or more OAuth scopes to request from the connector. OAuth scopes control the set of resources and operations that are allowed after authorization. Refer to the connector&#39;s documentation for the available scopes. (optional)
     * @return UnexpectedErrorResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 301 </td><td> redirect </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public UnexpectedErrorResponse connectionsAuthorize(String serviceId, String applicationId, String state, String redirectUri, List<String> scope) throws ApiException {
        ApiResponse<UnexpectedErrorResponse> localVarResp = connectionsAuthorizeWithHttpInfo(serviceId, applicationId, state, redirectUri, scope);
        return localVarResp.getData();
    }

    /**
     * Authorize
     * __In most cases the authorize link is provided in the &#x60;&#x60;/connections&#x60;&#x60; endpoint. Normally you don&#39;t need to manually generate these links.__  Use this endpoint to authenticate a user with a connector. It will return a 301 redirect to the downstream connector endpoints.  Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.  Vault handles the complete Authorization Code Grant Type Flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application. 
     * @param serviceId Service ID of the resource to return (required)
     * @param applicationId Application ID of the resource to return (required)
     * @param state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. (required)
     * @param redirectUri URL to redirect back to after authorization. When left empty the default configured redirect uri will be used. (required)
     * @param scope One or more OAuth scopes to request from the connector. OAuth scopes control the set of resources and operations that are allowed after authorization. Refer to the connector&#39;s documentation for the available scopes. (optional)
     * @return ApiResponse&lt;UnexpectedErrorResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 301 </td><td> redirect </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UnexpectedErrorResponse> connectionsAuthorizeWithHttpInfo(String serviceId, String applicationId, String state, String redirectUri, List<String> scope) throws ApiException {
        okhttp3.Call localVarCall = connectionsAuthorizeValidateBeforeCall(serviceId, applicationId, state, redirectUri, scope, null);
        Type localVarReturnType = new TypeToken<UnexpectedErrorResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Authorize (asynchronously)
     * __In most cases the authorize link is provided in the &#x60;&#x60;/connections&#x60;&#x60; endpoint. Normally you don&#39;t need to manually generate these links.__  Use this endpoint to authenticate a user with a connector. It will return a 301 redirect to the downstream connector endpoints.  Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.  Vault handles the complete Authorization Code Grant Type Flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application. 
     * @param serviceId Service ID of the resource to return (required)
     * @param applicationId Application ID of the resource to return (required)
     * @param state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. (required)
     * @param redirectUri URL to redirect back to after authorization. When left empty the default configured redirect uri will be used. (required)
     * @param scope One or more OAuth scopes to request from the connector. OAuth scopes control the set of resources and operations that are allowed after authorization. Refer to the connector&#39;s documentation for the available scopes. (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 301 </td><td> redirect </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsAuthorizeAsync(String serviceId, String applicationId, String state, String redirectUri, List<String> scope, final ApiCallback<UnexpectedErrorResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = connectionsAuthorizeValidateBeforeCall(serviceId, applicationId, state, redirectUri, scope, _callback);
        Type localVarReturnType = new TypeToken<UnexpectedErrorResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for connectionsCallback
     * @param state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. (required)
     * @param code An authorization code from the connector which Apideck Vault will later exchange for an access token. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 301 </td><td> callback </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsCallbackCall(String state, String code, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vault/callback";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (state != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("state", state));
        }

        if (code != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("code", code));
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
    private okhttp3.Call connectionsCallbackValidateBeforeCall(String state, String code, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'state' is set
        if (state == null) {
            throw new ApiException("Missing the required parameter 'state' when calling connectionsCallback(Async)");
        }

        // verify the required parameter 'code' is set
        if (code == null) {
            throw new ApiException("Missing the required parameter 'code' when calling connectionsCallback(Async)");
        }

        return connectionsCallbackCall(state, code, _callback);

    }

    /**
     * Callback
     * This endpoint gets called after the triggering the authorize flow.  Callback links need a state and code parameter to verify the validity of the request. 
     * @param state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. (required)
     * @param code An authorization code from the connector which Apideck Vault will later exchange for an access token. (required)
     * @return UnexpectedErrorResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 301 </td><td> callback </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public UnexpectedErrorResponse connectionsCallback(String state, String code) throws ApiException {
        ApiResponse<UnexpectedErrorResponse> localVarResp = connectionsCallbackWithHttpInfo(state, code);
        return localVarResp.getData();
    }

    /**
     * Callback
     * This endpoint gets called after the triggering the authorize flow.  Callback links need a state and code parameter to verify the validity of the request. 
     * @param state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. (required)
     * @param code An authorization code from the connector which Apideck Vault will later exchange for an access token. (required)
     * @return ApiResponse&lt;UnexpectedErrorResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 301 </td><td> callback </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UnexpectedErrorResponse> connectionsCallbackWithHttpInfo(String state, String code) throws ApiException {
        okhttp3.Call localVarCall = connectionsCallbackValidateBeforeCall(state, code, null);
        Type localVarReturnType = new TypeToken<UnexpectedErrorResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Callback (asynchronously)
     * This endpoint gets called after the triggering the authorize flow.  Callback links need a state and code parameter to verify the validity of the request. 
     * @param state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. (required)
     * @param code An authorization code from the connector which Apideck Vault will later exchange for an access token. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 301 </td><td> callback </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsCallbackAsync(String state, String code, final ApiCallback<UnexpectedErrorResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = connectionsCallbackValidateBeforeCall(state, code, _callback);
        Type localVarReturnType = new TypeToken<UnexpectedErrorResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for connectionsDelete
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Resource deleted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsDeleteCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vault/connections/{unified_api}/{service_id}"
            .replace("{" + "service_id" + "}", localVarApiClient.escapeString(serviceId.toString()))
            .replace("{" + "unified_api" + "}", localVarApiClient.escapeString(unifiedApi.toString()));

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
    private okhttp3.Call connectionsDeleteValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling connectionsDelete(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling connectionsDelete(Async)");
        }

        // verify the required parameter 'serviceId' is set
        if (serviceId == null) {
            throw new ApiException("Missing the required parameter 'serviceId' when calling connectionsDelete(Async)");
        }

        // verify the required parameter 'unifiedApi' is set
        if (unifiedApi == null) {
            throw new ApiException("Missing the required parameter 'unifiedApi' when calling connectionsDelete(Async)");
        }

        return connectionsDeleteCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, _callback);

    }

    /**
     * Deletes a connection
     * Deletes a connection
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Resource deleted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public void connectionsDelete(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi) throws ApiException {
        connectionsDeleteWithHttpInfo(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi);
    }

    /**
     * Deletes a connection
     * Deletes a connection
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Resource deleted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> connectionsDeleteWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi) throws ApiException {
        okhttp3.Call localVarCall = connectionsDeleteValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Deletes a connection (asynchronously)
     * Deletes a connection
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Resource deleted </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsDeleteAsync(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = connectionsDeleteValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for connectionsImport
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param connectionImportData Fields that need to be persisted on the resource (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsImportCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, ConnectionImportData connectionImportData, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = connectionImportData;

        // create path and map variables
        String localVarPath = "/vault/connections/{unified_api}/{service_id}/import"
            .replace("{" + "service_id" + "}", localVarApiClient.escapeString(serviceId.toString()))
            .replace("{" + "unified_api" + "}", localVarApiClient.escapeString(unifiedApi.toString()));

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
    private okhttp3.Call connectionsImportValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, ConnectionImportData connectionImportData, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling connectionsImport(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling connectionsImport(Async)");
        }

        // verify the required parameter 'serviceId' is set
        if (serviceId == null) {
            throw new ApiException("Missing the required parameter 'serviceId' when calling connectionsImport(Async)");
        }

        // verify the required parameter 'unifiedApi' is set
        if (unifiedApi == null) {
            throw new ApiException("Missing the required parameter 'unifiedApi' when calling connectionsImport(Async)");
        }

        // verify the required parameter 'connectionImportData' is set
        if (connectionImportData == null) {
            throw new ApiException("Missing the required parameter 'connectionImportData' when calling connectionsImport(Async)");
        }

        return connectionsImportCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connectionImportData, _callback);

    }

    /**
     * Import connection
     * Import an authorized connection. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param connectionImportData Fields that need to be persisted on the resource (required)
     * @return CreateConnectionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public CreateConnectionResponse connectionsImport(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, ConnectionImportData connectionImportData) throws ApiException {
        ApiResponse<CreateConnectionResponse> localVarResp = connectionsImportWithHttpInfo(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connectionImportData);
        return localVarResp.getData();
    }

    /**
     * Import connection
     * Import an authorized connection. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param connectionImportData Fields that need to be persisted on the resource (required)
     * @return ApiResponse&lt;CreateConnectionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateConnectionResponse> connectionsImportWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, ConnectionImportData connectionImportData) throws ApiException {
        okhttp3.Call localVarCall = connectionsImportValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connectionImportData, null);
        Type localVarReturnType = new TypeToken<CreateConnectionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Import connection (asynchronously)
     * Import an authorized connection. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param connectionImportData Fields that need to be persisted on the resource (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsImportAsync(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, ConnectionImportData connectionImportData, final ApiCallback<CreateConnectionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = connectionsImportValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connectionImportData, _callback);
        Type localVarReturnType = new TypeToken<CreateConnectionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for connectionsOne
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsOneCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vault/connections/{unified_api}/{service_id}"
            .replace("{" + "service_id" + "}", localVarApiClient.escapeString(serviceId.toString()))
            .replace("{" + "unified_api" + "}", localVarApiClient.escapeString(unifiedApi.toString()));

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
    private okhttp3.Call connectionsOneValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling connectionsOne(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling connectionsOne(Async)");
        }

        // verify the required parameter 'serviceId' is set
        if (serviceId == null) {
            throw new ApiException("Missing the required parameter 'serviceId' when calling connectionsOne(Async)");
        }

        // verify the required parameter 'unifiedApi' is set
        if (unifiedApi == null) {
            throw new ApiException("Missing the required parameter 'unifiedApi' when calling connectionsOne(Async)");
        }

        return connectionsOneCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, _callback);

    }

    /**
     * Get connection
     * Get a connection
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @return GetConnectionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public GetConnectionResponse connectionsOne(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi) throws ApiException {
        ApiResponse<GetConnectionResponse> localVarResp = connectionsOneWithHttpInfo(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi);
        return localVarResp.getData();
    }

    /**
     * Get connection
     * Get a connection
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @return ApiResponse&lt;GetConnectionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetConnectionResponse> connectionsOneWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi) throws ApiException {
        okhttp3.Call localVarCall = connectionsOneValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, null);
        Type localVarReturnType = new TypeToken<GetConnectionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get connection (asynchronously)
     * Get a connection
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsOneAsync(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, final ApiCallback<GetConnectionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = connectionsOneValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, _callback);
        Type localVarReturnType = new TypeToken<GetConnectionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for connectionsRevoke
     * @param serviceId Service ID of the resource to return (required)
     * @param applicationId Application ID of the resource to return (required)
     * @param state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. (required)
     * @param redirectUri URL to redirect back to after authorization. When left empty the default configured redirect uri will be used. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 301 </td><td> redirect </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsRevokeCall(String serviceId, String applicationId, String state, String redirectUri, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vault/revoke/{service_id}/{application_id}"
            .replace("{" + "service_id" + "}", localVarApiClient.escapeString(serviceId.toString()))
            .replace("{" + "application_id" + "}", localVarApiClient.escapeString(applicationId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (state != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("state", state));
        }

        if (redirectUri != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("redirect_uri", redirectUri));
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
    private okhttp3.Call connectionsRevokeValidateBeforeCall(String serviceId, String applicationId, String state, String redirectUri, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'serviceId' is set
        if (serviceId == null) {
            throw new ApiException("Missing the required parameter 'serviceId' when calling connectionsRevoke(Async)");
        }

        // verify the required parameter 'applicationId' is set
        if (applicationId == null) {
            throw new ApiException("Missing the required parameter 'applicationId' when calling connectionsRevoke(Async)");
        }

        // verify the required parameter 'state' is set
        if (state == null) {
            throw new ApiException("Missing the required parameter 'state' when calling connectionsRevoke(Async)");
        }

        // verify the required parameter 'redirectUri' is set
        if (redirectUri == null) {
            throw new ApiException("Missing the required parameter 'redirectUri' when calling connectionsRevoke(Async)");
        }

        return connectionsRevokeCall(serviceId, applicationId, state, redirectUri, _callback);

    }

    /**
     * Revoke connection
     * __In most cases the authorize link is provided in the &#x60;&#x60;/connections&#x60;&#x60; endpoint. Normally you don&#39;t need to manually generate these links.__  Use this endpoint to revoke an existing OAuth connector.  Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.  Vault handles the complete revoke flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application. 
     * @param serviceId Service ID of the resource to return (required)
     * @param applicationId Application ID of the resource to return (required)
     * @param state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. (required)
     * @param redirectUri URL to redirect back to after authorization. When left empty the default configured redirect uri will be used. (required)
     * @return UnexpectedErrorResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 301 </td><td> redirect </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public UnexpectedErrorResponse connectionsRevoke(String serviceId, String applicationId, String state, String redirectUri) throws ApiException {
        ApiResponse<UnexpectedErrorResponse> localVarResp = connectionsRevokeWithHttpInfo(serviceId, applicationId, state, redirectUri);
        return localVarResp.getData();
    }

    /**
     * Revoke connection
     * __In most cases the authorize link is provided in the &#x60;&#x60;/connections&#x60;&#x60; endpoint. Normally you don&#39;t need to manually generate these links.__  Use this endpoint to revoke an existing OAuth connector.  Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.  Vault handles the complete revoke flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application. 
     * @param serviceId Service ID of the resource to return (required)
     * @param applicationId Application ID of the resource to return (required)
     * @param state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. (required)
     * @param redirectUri URL to redirect back to after authorization. When left empty the default configured redirect uri will be used. (required)
     * @return ApiResponse&lt;UnexpectedErrorResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 301 </td><td> redirect </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UnexpectedErrorResponse> connectionsRevokeWithHttpInfo(String serviceId, String applicationId, String state, String redirectUri) throws ApiException {
        okhttp3.Call localVarCall = connectionsRevokeValidateBeforeCall(serviceId, applicationId, state, redirectUri, null);
        Type localVarReturnType = new TypeToken<UnexpectedErrorResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Revoke connection (asynchronously)
     * __In most cases the authorize link is provided in the &#x60;&#x60;/connections&#x60;&#x60; endpoint. Normally you don&#39;t need to manually generate these links.__  Use this endpoint to revoke an existing OAuth connector.  Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.  Vault handles the complete revoke flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application. 
     * @param serviceId Service ID of the resource to return (required)
     * @param applicationId Application ID of the resource to return (required)
     * @param state An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. (required)
     * @param redirectUri URL to redirect back to after authorization. When left empty the default configured redirect uri will be used. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 301 </td><td> redirect </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsRevokeAsync(String serviceId, String applicationId, String state, String redirectUri, final ApiCallback<UnexpectedErrorResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = connectionsRevokeValidateBeforeCall(serviceId, applicationId, state, redirectUri, _callback);
        Type localVarReturnType = new TypeToken<UnexpectedErrorResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for connectionsToken
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param body  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsTokenCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Object body, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = body;

        // create path and map variables
        String localVarPath = "/vault/connections/{unified_api}/{service_id}/token"
            .replace("{" + "service_id" + "}", localVarApiClient.escapeString(serviceId.toString()))
            .replace("{" + "unified_api" + "}", localVarApiClient.escapeString(unifiedApi.toString()));

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
    private okhttp3.Call connectionsTokenValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Object body, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling connectionsToken(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling connectionsToken(Async)");
        }

        // verify the required parameter 'serviceId' is set
        if (serviceId == null) {
            throw new ApiException("Missing the required parameter 'serviceId' when calling connectionsToken(Async)");
        }

        // verify the required parameter 'unifiedApi' is set
        if (unifiedApi == null) {
            throw new ApiException("Missing the required parameter 'unifiedApi' when calling connectionsToken(Async)");
        }

        return connectionsTokenCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, body, _callback);

    }

    /**
     * Get Access Token
     * Get an access token for a connection and store it in Vault. Currently only supported for connections with the client_credentials OAuth grant type.  Note that the access token will not be returned in the response. A 200 response code indicates a valid access token was stored on the connection. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param body  (optional)
     * @return GetConnectionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public GetConnectionResponse connectionsToken(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Object body) throws ApiException {
        ApiResponse<GetConnectionResponse> localVarResp = connectionsTokenWithHttpInfo(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, body);
        return localVarResp.getData();
    }

    /**
     * Get Access Token
     * Get an access token for a connection and store it in Vault. Currently only supported for connections with the client_credentials OAuth grant type.  Note that the access token will not be returned in the response. A 200 response code indicates a valid access token was stored on the connection. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param body  (optional)
     * @return ApiResponse&lt;GetConnectionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetConnectionResponse> connectionsTokenWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Object body) throws ApiException {
        okhttp3.Call localVarCall = connectionsTokenValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, body, null);
        Type localVarReturnType = new TypeToken<GetConnectionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Access Token (asynchronously)
     * Get an access token for a connection and store it in Vault. Currently only supported for connections with the client_credentials OAuth grant type.  Note that the access token will not be returned in the response. A 200 response code indicates a valid access token was stored on the connection. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param body  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsTokenAsync(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Object body, final ApiCallback<GetConnectionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = connectionsTokenValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, body, _callback);
        Type localVarReturnType = new TypeToken<GetConnectionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for connectionsUpdate
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param connection Fields that need to be updated on the resource (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection updated </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsUpdateCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Connection connection, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = connection;

        // create path and map variables
        String localVarPath = "/vault/connections/{unified_api}/{service_id}"
            .replace("{" + "service_id" + "}", localVarApiClient.escapeString(serviceId.toString()))
            .replace("{" + "unified_api" + "}", localVarApiClient.escapeString(unifiedApi.toString()));

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
    private okhttp3.Call connectionsUpdateValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Connection connection, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling connectionsUpdate(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling connectionsUpdate(Async)");
        }

        // verify the required parameter 'serviceId' is set
        if (serviceId == null) {
            throw new ApiException("Missing the required parameter 'serviceId' when calling connectionsUpdate(Async)");
        }

        // verify the required parameter 'unifiedApi' is set
        if (unifiedApi == null) {
            throw new ApiException("Missing the required parameter 'unifiedApi' when calling connectionsUpdate(Async)");
        }

        // verify the required parameter 'connection' is set
        if (connection == null) {
            throw new ApiException("Missing the required parameter 'connection' when calling connectionsUpdate(Async)");
        }

        return connectionsUpdateCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection, _callback);

    }

    /**
     * Update connection
     * Update a connection
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param connection Fields that need to be updated on the resource (required)
     * @return UpdateConnectionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection updated </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public UpdateConnectionResponse connectionsUpdate(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Connection connection) throws ApiException {
        ApiResponse<UpdateConnectionResponse> localVarResp = connectionsUpdateWithHttpInfo(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection);
        return localVarResp.getData();
    }

    /**
     * Update connection
     * Update a connection
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param connection Fields that need to be updated on the resource (required)
     * @return ApiResponse&lt;UpdateConnectionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection updated </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateConnectionResponse> connectionsUpdateWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Connection connection) throws ApiException {
        okhttp3.Call localVarCall = connectionsUpdateValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection, null);
        Type localVarReturnType = new TypeToken<UpdateConnectionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update connection (asynchronously)
     * Update a connection
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param unifiedApi Unified API (required)
     * @param connection Fields that need to be updated on the resource (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Connection updated </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call connectionsUpdateAsync(String xApideckConsumerId, String xApideckAppId, String serviceId, String unifiedApi, Connection connection, final ApiCallback<UpdateConnectionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = connectionsUpdateValidateBeforeCall(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection, _callback);
        Type localVarReturnType = new TypeToken<UpdateConnectionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for customFieldsAll
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param unifiedApi Unified API (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param resource Name of the resource (plural) (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Custom mapping </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customFieldsAllCall(String xApideckConsumerId, String xApideckAppId, String unifiedApi, String serviceId, String resource, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/vault/connections/{unified_api}/{service_id}/{resource}/custom-fields"
            .replace("{" + "unified_api" + "}", localVarApiClient.escapeString(unifiedApi.toString()))
            .replace("{" + "service_id" + "}", localVarApiClient.escapeString(serviceId.toString()))
            .replace("{" + "resource" + "}", localVarApiClient.escapeString(resource.toString()));

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
    private okhttp3.Call customFieldsAllValidateBeforeCall(String xApideckConsumerId, String xApideckAppId, String unifiedApi, String serviceId, String resource, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xApideckConsumerId' is set
        if (xApideckConsumerId == null) {
            throw new ApiException("Missing the required parameter 'xApideckConsumerId' when calling customFieldsAll(Async)");
        }

        // verify the required parameter 'xApideckAppId' is set
        if (xApideckAppId == null) {
            throw new ApiException("Missing the required parameter 'xApideckAppId' when calling customFieldsAll(Async)");
        }

        // verify the required parameter 'unifiedApi' is set
        if (unifiedApi == null) {
            throw new ApiException("Missing the required parameter 'unifiedApi' when calling customFieldsAll(Async)");
        }

        // verify the required parameter 'serviceId' is set
        if (serviceId == null) {
            throw new ApiException("Missing the required parameter 'serviceId' when calling customFieldsAll(Async)");
        }

        // verify the required parameter 'resource' is set
        if (resource == null) {
            throw new ApiException("Missing the required parameter 'resource' when calling customFieldsAll(Async)");
        }

        return customFieldsAllCall(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource, _callback);

    }

    /**
     * Get resource custom fields
     * This endpoint returns an custom fields on a connection resource. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param unifiedApi Unified API (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param resource Name of the resource (plural) (required)
     * @return GetCustomFieldsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Custom mapping </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public GetCustomFieldsResponse customFieldsAll(String xApideckConsumerId, String xApideckAppId, String unifiedApi, String serviceId, String resource) throws ApiException {
        ApiResponse<GetCustomFieldsResponse> localVarResp = customFieldsAllWithHttpInfo(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource);
        return localVarResp.getData();
    }

    /**
     * Get resource custom fields
     * This endpoint returns an custom fields on a connection resource. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param unifiedApi Unified API (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param resource Name of the resource (plural) (required)
     * @return ApiResponse&lt;GetCustomFieldsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Custom mapping </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetCustomFieldsResponse> customFieldsAllWithHttpInfo(String xApideckConsumerId, String xApideckAppId, String unifiedApi, String serviceId, String resource) throws ApiException {
        okhttp3.Call localVarCall = customFieldsAllValidateBeforeCall(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource, null);
        Type localVarReturnType = new TypeToken<GetCustomFieldsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get resource custom fields (asynchronously)
     * This endpoint returns an custom fields on a connection resource. 
     * @param xApideckConsumerId ID of the consumer which you want to get or push data from (required)
     * @param xApideckAppId The ID of your Unify application (required)
     * @param unifiedApi Unified API (required)
     * @param serviceId Service ID of the resource to return (required)
     * @param resource Name of the resource (plural) (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Custom mapping </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 402 </td><td> Payment Required </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> The specified resource was not found </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable </td><td>  -  </td></tr>
        <tr><td> 0 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customFieldsAllAsync(String xApideckConsumerId, String xApideckAppId, String unifiedApi, String serviceId, String resource, final ApiCallback<GetCustomFieldsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = customFieldsAllValidateBeforeCall(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource, _callback);
        Type localVarReturnType = new TypeToken<GetCustomFieldsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
