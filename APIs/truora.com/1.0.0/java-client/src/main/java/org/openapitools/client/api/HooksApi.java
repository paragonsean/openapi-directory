/*
 * Checks API
 * **NOTE:** This is a preview of the API and it is not considered stable since refinements are still being made.  # Introduction  Welcome to the  **Truora Check** [**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) reference. You may also want to check out our [**Validations API docs**](https://docs.validations.truora.com/) or our [**Signals API docs**](https://docs.signals.truora.com/).  Truora Check API allows performing full background checks on people, vehicles and companies. There are three main types of background checks:  - **Personal background check**: Verifies national IDs in multiple databases of public and legal entities in the LATAM region. For every national ID, returns information on: personal identity, criminal records, international background check, and professional background.  - **Vehicle background check**: Verifies the vehicle documents and the owner identity in multiple databases of public and legal entities in the LATAM region. For every vehicle and owner type, returns information on: personal identity, driving records, criminal records, and vehicle information.    - **Company background check**: Verifies the tax ID or a company name in multiple databases of public and legal entities in the LATAM region. For every company, returns the associated: business status, legal and criminal records, and media reports.  # API Key V1 is live!  API key version 1 is now live. Users with version 0 API keys are not immediately required to upgrade to V1 but should plan to do so at their earliest convenience. The changes for integration with API keys v1 are as follows:  - The field ``user_authorized`` is now required to perform person checks. This field indicates the API user has authorization to perform the check in compliance with data protection law. - The field ``homonym_scores`` is no longer included in our person check response as its results are already included in the body of the check and keeping them duplicated is generating unnecessary confusion.   # API composition  ## Endpoints  - **Check endpoints**: Provide an easy way to create and search for a background check. They also allow inserting groups of checks into reports. Each check contains scores, datasets and databases.   ```plain https://api.truora.com/v1/checks ```  - **Report endpoints**: Support batch uploads and grouping multiple checks together. Excel and .csv files are supported for batch uploads.   ```plain https://api.truora.com/v1/reports ```  - **Configuration endpoints**: Allows personalizing data sets and scores for customized background checks.  ```plain https://api.truora.com/v1/config ```  - **Continuous check endpoints**: Allows creating recurring checks and get notified whenever a change in the check score occurs.  ```plain https://api.truora.com/v1/continuous_checks ```  - **Behavior endpoints**: Allows sharing anonymous feedback about a person behavior when interacting with the company.  ```plain https://api.truora.com/v1/behaviour ```  - **Hooks endpoints**: Allows sending notifications via requests to your service or another third-party service whenever certain events occur.  ```plain https://api.truora.com/v1/hooks ```  ## Datasets  Categories that group the resulting information for background checks from databases are called datasets. Datasets are divided in:  - **Personal identity**: Corroborates the existence and validates personal identity documents.   - **Criminal record**: Checks for crimes according to each country penal code or criminal code. Keep in mind that data aged less than 10 years is usually more consistent.  - **Legal background**: Checks for lawsuits filed. Keep in mind that data aged less than 10 years is usually more consistent.  - **International background**: Checks international lists for crimes related to identity theft, money laundering, terrorist financing, and high crimes.  - **Professional background**: Checks professional regulatory entities for relevant information.  - **Affiliations and insurances**: Checks the history and status of social security affiliations.  - **Alert in media**: Checks major media agencies for relevant news related to violent actions.      - **Vehicle information**: Checks for the physical characteristics of the vehicle, technical status, insurance history, and other relevant information.  - **Traffic fines**: Checks for outstanding traffic fines.  - **Driving licenses**: Shows information relevant to the driver. Such as license status and driver certificates.  - **Business background**: Checks for business status, legal and criminal history, and other relevant information.  - **Taxes and Finances**: Checks for the information related to personal finances, liabilities, and taxes.  ## Requests Format  The POST requests receive a body that must be encoded in `www-x-form-urlencoded`, for instance:  ```plain type=person&national_id=123456&country=CO ```  The responses are always encoded in `JSON` format.  ## Errors  Whenever there is an error, a JSON with the following format is returned:  ```json {     \"code\": <Truora error code>,     \"http_code\": <The HTTP status of the response>,     \"message\": <The error message> } ```  for instance:  ```json {     \"code\": 10404,     \"http_code\": 404,     \"message\": \"The Check was not found\" } ```  ## SDKs  If your favorite language was not on the next list, You can use our [OpenAPI 3 spec](https://docs.truora.com/openapi.json) to generate it using the [Open API Generator](https://openapi-generator.tech/docs/installation).  To download the SDK click on the desired programming language:  - [C# .Net Core](https://truora-sdk.s3.amazonaws.com/checks/checks_csharp-netcore_latest.zip)  - [Elixir](https://truora-sdk.s3.amazonaws.com/checks/checks_elixir_latest.zip)  - [Go](https://truora-sdk.s3.amazonaws.com/checks/checks_go_latest.zip)  - [Java](https://truora-sdk.s3.amazonaws.com/checks/checks_java_latest.zip)  - [JavaScript](https://truora-sdk.s3.amazonaws.com/checks/checks_javascript_latest.zip)  - [Objc](https://truora-sdk.s3.amazonaws.com/checks/checks_objc_latest.zip)  - [Php](https://truora-sdk.s3.amazonaws.com/checks/checks_php_latest.zip)  - [Python](https://truora-sdk.s3.amazonaws.com/checks/checks_python_latest.zip)  - [Ruby](https://truora-sdk.s3.amazonaws.com/checks/checks_ruby_latest.zip)  You can see the full list of supported platforms here:  https://openapi-generator.tech/docs/generators   
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: api@truora.com
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
import org.openapitools.client.model.Hook;
import org.openapitools.client.model.HookOutput;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HooksApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public HooksApi() {
        this(Configuration.getDefaultApiClient());
    }

    public HooksApi(ApiClient apiClient) {
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
     * Build call for createHook
     * @param eventType The entity events the client wants to subscribe (required)
     * @param subscriberType A platform with an endpoint ready to process the information (required)
     * @param actions Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three (optional)
     * @param status indicates whether the hook is active or not. enabled by default (optional)
     * @param subscriberAddress Email address where the notification is to be sent. Required if subscriber_type was set to email (optional)
     * @param subscriberLanguage Language for the notification to be sent (optional)
     * @param subscriberName Name of the person to be notified (optional)
     * @param subscriberUrl URL where the notification is to be sent. Required only if subscriber_type is set to web (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error, at least one of the parameters was invalid. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createHookCall(String eventType, String subscriberType, List<String> actions, String status, String subscriberAddress, String subscriberLanguage, String subscriberName, String subscriberUrl, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/hooks";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (actions != null) {
            localVarFormParams.put("actions", actions);
        }

        if (eventType != null) {
            localVarFormParams.put("event_type", eventType);
        }

        if (status != null) {
            localVarFormParams.put("status", status);
        }

        if (subscriberAddress != null) {
            localVarFormParams.put("subscriber_address", subscriberAddress);
        }

        if (subscriberLanguage != null) {
            localVarFormParams.put("subscriber_language", subscriberLanguage);
        }

        if (subscriberName != null) {
            localVarFormParams.put("subscriber_name", subscriberName);
        }

        if (subscriberType != null) {
            localVarFormParams.put("subscriber_type", subscriberType);
        }

        if (subscriberUrl != null) {
            localVarFormParams.put("subscriber_url", subscriberUrl);
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/x-www-form-urlencoded"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createHookValidateBeforeCall(String eventType, String subscriberType, List<String> actions, String status, String subscriberAddress, String subscriberLanguage, String subscriberName, String subscriberUrl, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'eventType' is set
        if (eventType == null) {
            throw new ApiException("Missing the required parameter 'eventType' when calling createHook(Async)");
        }

        // verify the required parameter 'subscriberType' is set
        if (subscriberType == null) {
            throw new ApiException("Missing the required parameter 'subscriberType' when calling createHook(Async)");
        }

        return createHookCall(eventType, subscriberType, actions, status, subscriberAddress, subscriberLanguage, subscriberName, subscriberUrl, _callback);

    }

    /**
     * Creates a hook subscription
     * Creates a hook subscription to notify events in Truora plataform. Subscriptions broadcast data as events occur and additional subscription instances are not required in order to refresh the information. Events are received in an array as a JWT and are decoded using the signing key returned by this endpoint. Their structure is as follows:  &#x60;&#x60;&#x60; {     \&quot;events\&quot;: [         {             \&quot;event_action\&quot;: \&quot;created\&quot;,             \&quot;event_type\&quot;: \&quot;check\&quot;,             \&quot;id\&quot;: \&quot;HKEdd28c569cf5eb74e45f0f4c092096e62c1c95ba2\&quot;,             \&quot;object\&quot;: {                 \&quot;check_id\&quot;: \&quot;CHK9c39003424c521aec8566ce59e1ddc86\&quot;,                 \&quot;country\&quot;: \&quot;CO\&quot;,                 \&quot;creation_date\&quot;: \&quot;2020-04-01T23:00:30.581232281Z\&quot;,                 \&quot;homonym_score\&quot;: 0,                 \&quot;id_score\&quot;: 0,                 \&quot;national_id\&quot;: \&quot;1151959906\&quot;,                 \&quot;previous_check\&quot;: \&quot;CHK4ec814fecd147eaae41027081d7d5caf\&quot;,                 \&quot;score\&quot;: -1,                 \&quot;status\&quot;: \&quot;not_started\&quot;,                 \&quot;type\&quot;: \&quot;person\&quot;,                 \&quot;update_date\&quot;: \&quot;2020-04-01T23:00:30.680937413Z\&quot;             },             \&quot;timestamp\&quot;: \&quot;2020-04-01T23:00:30Z\&quot;,             \&quot;version\&quot;: \&quot;1.0\&quot;         }     ],     \&quot;iat\&quot;: 1585782031,     \&quot;iss\&quot;: \&quot;Truora\&quot; } &#x60;&#x60;&#x60;  Keep in mind that the object attribute varies depending on the event_type.
     * @param eventType The entity events the client wants to subscribe (required)
     * @param subscriberType A platform with an endpoint ready to process the information (required)
     * @param actions Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three (optional)
     * @param status indicates whether the hook is active or not. enabled by default (optional)
     * @param subscriberAddress Email address where the notification is to be sent. Required if subscriber_type was set to email (optional)
     * @param subscriberLanguage Language for the notification to be sent (optional)
     * @param subscriberName Name of the person to be notified (optional)
     * @param subscriberUrl URL where the notification is to be sent. Required only if subscriber_type is set to web (optional)
     * @return Hook
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error, at least one of the parameters was invalid. </td><td>  -  </td></tr>
     </table>
     */
    public Hook createHook(String eventType, String subscriberType, List<String> actions, String status, String subscriberAddress, String subscriberLanguage, String subscriberName, String subscriberUrl) throws ApiException {
        ApiResponse<Hook> localVarResp = createHookWithHttpInfo(eventType, subscriberType, actions, status, subscriberAddress, subscriberLanguage, subscriberName, subscriberUrl);
        return localVarResp.getData();
    }

    /**
     * Creates a hook subscription
     * Creates a hook subscription to notify events in Truora plataform. Subscriptions broadcast data as events occur and additional subscription instances are not required in order to refresh the information. Events are received in an array as a JWT and are decoded using the signing key returned by this endpoint. Their structure is as follows:  &#x60;&#x60;&#x60; {     \&quot;events\&quot;: [         {             \&quot;event_action\&quot;: \&quot;created\&quot;,             \&quot;event_type\&quot;: \&quot;check\&quot;,             \&quot;id\&quot;: \&quot;HKEdd28c569cf5eb74e45f0f4c092096e62c1c95ba2\&quot;,             \&quot;object\&quot;: {                 \&quot;check_id\&quot;: \&quot;CHK9c39003424c521aec8566ce59e1ddc86\&quot;,                 \&quot;country\&quot;: \&quot;CO\&quot;,                 \&quot;creation_date\&quot;: \&quot;2020-04-01T23:00:30.581232281Z\&quot;,                 \&quot;homonym_score\&quot;: 0,                 \&quot;id_score\&quot;: 0,                 \&quot;national_id\&quot;: \&quot;1151959906\&quot;,                 \&quot;previous_check\&quot;: \&quot;CHK4ec814fecd147eaae41027081d7d5caf\&quot;,                 \&quot;score\&quot;: -1,                 \&quot;status\&quot;: \&quot;not_started\&quot;,                 \&quot;type\&quot;: \&quot;person\&quot;,                 \&quot;update_date\&quot;: \&quot;2020-04-01T23:00:30.680937413Z\&quot;             },             \&quot;timestamp\&quot;: \&quot;2020-04-01T23:00:30Z\&quot;,             \&quot;version\&quot;: \&quot;1.0\&quot;         }     ],     \&quot;iat\&quot;: 1585782031,     \&quot;iss\&quot;: \&quot;Truora\&quot; } &#x60;&#x60;&#x60;  Keep in mind that the object attribute varies depending on the event_type.
     * @param eventType The entity events the client wants to subscribe (required)
     * @param subscriberType A platform with an endpoint ready to process the information (required)
     * @param actions Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three (optional)
     * @param status indicates whether the hook is active or not. enabled by default (optional)
     * @param subscriberAddress Email address where the notification is to be sent. Required if subscriber_type was set to email (optional)
     * @param subscriberLanguage Language for the notification to be sent (optional)
     * @param subscriberName Name of the person to be notified (optional)
     * @param subscriberUrl URL where the notification is to be sent. Required only if subscriber_type is set to web (optional)
     * @return ApiResponse&lt;Hook&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error, at least one of the parameters was invalid. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Hook> createHookWithHttpInfo(String eventType, String subscriberType, List<String> actions, String status, String subscriberAddress, String subscriberLanguage, String subscriberName, String subscriberUrl) throws ApiException {
        okhttp3.Call localVarCall = createHookValidateBeforeCall(eventType, subscriberType, actions, status, subscriberAddress, subscriberLanguage, subscriberName, subscriberUrl, null);
        Type localVarReturnType = new TypeToken<Hook>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Creates a hook subscription (asynchronously)
     * Creates a hook subscription to notify events in Truora plataform. Subscriptions broadcast data as events occur and additional subscription instances are not required in order to refresh the information. Events are received in an array as a JWT and are decoded using the signing key returned by this endpoint. Their structure is as follows:  &#x60;&#x60;&#x60; {     \&quot;events\&quot;: [         {             \&quot;event_action\&quot;: \&quot;created\&quot;,             \&quot;event_type\&quot;: \&quot;check\&quot;,             \&quot;id\&quot;: \&quot;HKEdd28c569cf5eb74e45f0f4c092096e62c1c95ba2\&quot;,             \&quot;object\&quot;: {                 \&quot;check_id\&quot;: \&quot;CHK9c39003424c521aec8566ce59e1ddc86\&quot;,                 \&quot;country\&quot;: \&quot;CO\&quot;,                 \&quot;creation_date\&quot;: \&quot;2020-04-01T23:00:30.581232281Z\&quot;,                 \&quot;homonym_score\&quot;: 0,                 \&quot;id_score\&quot;: 0,                 \&quot;national_id\&quot;: \&quot;1151959906\&quot;,                 \&quot;previous_check\&quot;: \&quot;CHK4ec814fecd147eaae41027081d7d5caf\&quot;,                 \&quot;score\&quot;: -1,                 \&quot;status\&quot;: \&quot;not_started\&quot;,                 \&quot;type\&quot;: \&quot;person\&quot;,                 \&quot;update_date\&quot;: \&quot;2020-04-01T23:00:30.680937413Z\&quot;             },             \&quot;timestamp\&quot;: \&quot;2020-04-01T23:00:30Z\&quot;,             \&quot;version\&quot;: \&quot;1.0\&quot;         }     ],     \&quot;iat\&quot;: 1585782031,     \&quot;iss\&quot;: \&quot;Truora\&quot; } &#x60;&#x60;&#x60;  Keep in mind that the object attribute varies depending on the event_type.
     * @param eventType The entity events the client wants to subscribe (required)
     * @param subscriberType A platform with an endpoint ready to process the information (required)
     * @param actions Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three (optional)
     * @param status indicates whether the hook is active or not. enabled by default (optional)
     * @param subscriberAddress Email address where the notification is to be sent. Required if subscriber_type was set to email (optional)
     * @param subscriberLanguage Language for the notification to be sent (optional)
     * @param subscriberName Name of the person to be notified (optional)
     * @param subscriberUrl URL where the notification is to be sent. Required only if subscriber_type is set to web (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error, at least one of the parameters was invalid. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createHookAsync(String eventType, String subscriberType, List<String> actions, String status, String subscriberAddress, String subscriberLanguage, String subscriberName, String subscriberUrl, final ApiCallback<Hook> _callback) throws ApiException {

        okhttp3.Call localVarCall = createHookValidateBeforeCall(eventType, subscriberType, actions, status, subscriberAddress, subscriberLanguage, subscriberName, subscriberUrl, _callback);
        Type localVarReturnType = new TypeToken<Hook>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deletHook
     * @param hookId Hook ID (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deletHookCall(String hookId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/hooks/{hook_id}"
            .replace("{" + "hook_id" + "}", localVarApiClient.escapeString(hookId.toString()));

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

        String[] localVarAuthNames = new String[] { "api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deletHookValidateBeforeCall(String hookId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'hookId' is set
        if (hookId == null) {
            throw new ApiException("Missing the required parameter 'hookId' when calling deletHook(Async)");
        }

        return deletHookCall(hookId, _callback);

    }

    /**
     * Deletes hook
     * Deletes hook configuration.
     * @param hookId Hook ID (required)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public String deletHook(String hookId) throws ApiException {
        ApiResponse<String> localVarResp = deletHookWithHttpInfo(hookId);
        return localVarResp.getData();
    }

    /**
     * Deletes hook
     * Deletes hook configuration.
     * @param hookId Hook ID (required)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> deletHookWithHttpInfo(String hookId) throws ApiException {
        okhttp3.Call localVarCall = deletHookValidateBeforeCall(hookId, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Deletes hook (asynchronously)
     * Deletes hook configuration.
     * @param hookId Hook ID (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deletHookAsync(String hookId, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = deletHookValidateBeforeCall(hookId, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listHook
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listHookCall(final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/hooks";

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

        String[] localVarAuthNames = new String[] { "api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listHookValidateBeforeCall(final ApiCallback _callback) throws ApiException {
        return listHookCall(_callback);

    }

    /**
     * Lists all hooks
     * Lists all the configured hooks in your account.
     * @return HookOutput
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public HookOutput listHook() throws ApiException {
        ApiResponse<HookOutput> localVarResp = listHookWithHttpInfo();
        return localVarResp.getData();
    }

    /**
     * Lists all hooks
     * Lists all the configured hooks in your account.
     * @return ApiResponse&lt;HookOutput&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<HookOutput> listHookWithHttpInfo() throws ApiException {
        okhttp3.Call localVarCall = listHookValidateBeforeCall(null);
        Type localVarReturnType = new TypeToken<HookOutput>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Lists all hooks (asynchronously)
     * Lists all the configured hooks in your account.
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listHookAsync(final ApiCallback<HookOutput> _callback) throws ApiException {

        okhttp3.Call localVarCall = listHookValidateBeforeCall(_callback);
        Type localVarReturnType = new TypeToken<HookOutput>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateHook
     * @param hookId Hook ID (required)
     * @param eventType The entity events the client wants to subscribe (required)
     * @param subscriberType A platform with an endpoint ready to process the information (required)
     * @param actions Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three (optional)
     * @param status indicates whether the hook is active or not. enabled by default (optional)
     * @param subscriberAddress Email address where the notification is to be sent. Required if subscriber_type was set to email (optional)
     * @param subscriberLanguage Language for the notification to be sent (optional)
     * @param subscriberName Name of the person to be notified (optional)
     * @param subscriberUrl URL where the notification is to be sent. Required only if subscriber_type is set to web (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error, at least one of the parameters was invalid. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateHookCall(String hookId, String eventType, String subscriberType, List<String> actions, String status, String subscriberAddress, String subscriberLanguage, String subscriberName, String subscriberUrl, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/hooks/{hook_id}"
            .replace("{" + "hook_id" + "}", localVarApiClient.escapeString(hookId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (actions != null) {
            localVarFormParams.put("actions", actions);
        }

        if (eventType != null) {
            localVarFormParams.put("event_type", eventType);
        }

        if (status != null) {
            localVarFormParams.put("status", status);
        }

        if (subscriberAddress != null) {
            localVarFormParams.put("subscriber_address", subscriberAddress);
        }

        if (subscriberLanguage != null) {
            localVarFormParams.put("subscriber_language", subscriberLanguage);
        }

        if (subscriberName != null) {
            localVarFormParams.put("subscriber_name", subscriberName);
        }

        if (subscriberType != null) {
            localVarFormParams.put("subscriber_type", subscriberType);
        }

        if (subscriberUrl != null) {
            localVarFormParams.put("subscriber_url", subscriberUrl);
        }

        final String[] localVarAccepts = {
            "application/x-www-form-urlencoded",
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/x-www-form-urlencoded"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "api-key" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateHookValidateBeforeCall(String hookId, String eventType, String subscriberType, List<String> actions, String status, String subscriberAddress, String subscriberLanguage, String subscriberName, String subscriberUrl, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'hookId' is set
        if (hookId == null) {
            throw new ApiException("Missing the required parameter 'hookId' when calling updateHook(Async)");
        }

        // verify the required parameter 'eventType' is set
        if (eventType == null) {
            throw new ApiException("Missing the required parameter 'eventType' when calling updateHook(Async)");
        }

        // verify the required parameter 'subscriberType' is set
        if (subscriberType == null) {
            throw new ApiException("Missing the required parameter 'subscriberType' when calling updateHook(Async)");
        }

        return updateHookCall(hookId, eventType, subscriberType, actions, status, subscriberAddress, subscriberLanguage, subscriberName, subscriberUrl, _callback);

    }

    /**
     * Updates hook
     * Updates a hook configuration.
     * @param hookId Hook ID (required)
     * @param eventType The entity events the client wants to subscribe (required)
     * @param subscriberType A platform with an endpoint ready to process the information (required)
     * @param actions Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three (optional)
     * @param status indicates whether the hook is active or not. enabled by default (optional)
     * @param subscriberAddress Email address where the notification is to be sent. Required if subscriber_type was set to email (optional)
     * @param subscriberLanguage Language for the notification to be sent (optional)
     * @param subscriberName Name of the person to be notified (optional)
     * @param subscriberUrl URL where the notification is to be sent. Required only if subscriber_type is set to web (optional)
     * @return Hook
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error, at least one of the parameters was invalid. </td><td>  -  </td></tr>
     </table>
     */
    public Hook updateHook(String hookId, String eventType, String subscriberType, List<String> actions, String status, String subscriberAddress, String subscriberLanguage, String subscriberName, String subscriberUrl) throws ApiException {
        ApiResponse<Hook> localVarResp = updateHookWithHttpInfo(hookId, eventType, subscriberType, actions, status, subscriberAddress, subscriberLanguage, subscriberName, subscriberUrl);
        return localVarResp.getData();
    }

    /**
     * Updates hook
     * Updates a hook configuration.
     * @param hookId Hook ID (required)
     * @param eventType The entity events the client wants to subscribe (required)
     * @param subscriberType A platform with an endpoint ready to process the information (required)
     * @param actions Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three (optional)
     * @param status indicates whether the hook is active or not. enabled by default (optional)
     * @param subscriberAddress Email address where the notification is to be sent. Required if subscriber_type was set to email (optional)
     * @param subscriberLanguage Language for the notification to be sent (optional)
     * @param subscriberName Name of the person to be notified (optional)
     * @param subscriberUrl URL where the notification is to be sent. Required only if subscriber_type is set to web (optional)
     * @return ApiResponse&lt;Hook&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error, at least one of the parameters was invalid. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Hook> updateHookWithHttpInfo(String hookId, String eventType, String subscriberType, List<String> actions, String status, String subscriberAddress, String subscriberLanguage, String subscriberName, String subscriberUrl) throws ApiException {
        okhttp3.Call localVarCall = updateHookValidateBeforeCall(hookId, eventType, subscriberType, actions, status, subscriberAddress, subscriberLanguage, subscriberName, subscriberUrl, null);
        Type localVarReturnType = new TypeToken<Hook>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Updates hook (asynchronously)
     * Updates a hook configuration.
     * @param hookId Hook ID (required)
     * @param eventType The entity events the client wants to subscribe (required)
     * @param subscriberType A platform with an endpoint ready to process the information (required)
     * @param actions Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three (optional)
     * @param status indicates whether the hook is active or not. enabled by default (optional)
     * @param subscriberAddress Email address where the notification is to be sent. Required if subscriber_type was set to email (optional)
     * @param subscriberLanguage Language for the notification to be sent (optional)
     * @param subscriberName Name of the person to be notified (optional)
     * @param subscriberUrl URL where the notification is to be sent. Required only if subscriber_type is set to web (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Validation error, at least one of the parameters was invalid. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateHookAsync(String hookId, String eventType, String subscriberType, List<String> actions, String status, String subscriberAddress, String subscriberLanguage, String subscriberName, String subscriberUrl, final ApiCallback<Hook> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateHookValidateBeforeCall(hookId, eventType, subscriberType, actions, status, subscriberAddress, subscriberLanguage, subscriberName, subscriberUrl, _callback);
        Type localVarReturnType = new TypeToken<Hook>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
