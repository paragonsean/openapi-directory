/*
 * Braze Endpoints
 * # Braze API Overview  Braze provides a high performance REST API to allow you to track users, send messages, export data, and more.  A REST API is a way to programmatically transfer information over the web using a predefined schema. Braze has created many different endpoints with specific requirements that will perform various actions and/or return various data. API access is done using HTTPS web requests to your company's REST API endpoint (this will correspond to your Dashboard URL as shown in the table below).  Customers using Braze's EU database should use `https://rest.fra-01.braze.eu/`. For more information on REST API endpoints for customers using Braze's EU database see our [EU/US Implementation Differences documentation](https://www.braze.com/docs/developer_guide/eu01_us3_sdk_implementation_differences/overview/).  ## Braze Instances  Instance    | Dashboard URL   | REST Endpoint ----------- |---------------- | -------------------- US-01 | `https://dashboard.braze.com` or<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` US-02 | `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` US-03 | `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` US-04 | `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` US-06 | `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` EU-01 | `https://dashboard.braze.eu` or<br> `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu`   # Using Braze's Postman Collection   If you have a Postman account (MacOS, Windows, and Linux versions can be downloaded from their website located [here](https://www.getpostman.com)), you can go to our Postman documentation and click the orange `Run in Postman` button in the top, right corner. This will allow you to [create an environment](#setting-up-your-postman-environment), as well as edit the available `POST` and `GET` requests to suit your own needs.  ## Setting Up Your Postman Environment  The Braze Postman Collection uses a templating variable, `{{instance_url}}`, to substitute the REST API URL of your Braze instance into the pre-built requests. Rather than having to manually edit all requests in the Collection, you can set up this variable in your Postman environment. To do so, please follow the steps below:  1. Click on the gear icon in the top right corner of the Postman app.  2. Select \"Manage Environments\" to open a modal window which displays your active environments. 3. In the bottom right corner of the modal window, click \"Add\" to create a new environment. 4. Give this environment a name (e.g. \"Braze API Requests\") and add keys for `instance_url` and `api_key` with values corresponding to [your Braze instance](https://www.braze.com/docs/api/basics/#endpoints) and [Braze REST API Key](https://www.braze.com/docs/api/basics/#app-group-rest-api-keys), as pictured below.   As of April, 2020 Braze has changed how we read App Group API keys. Instead of passing them in the request body or through url parameters, we now read the App Group Rest`api_key` through the HTTP Authorization header. API keys not passed through the HTTP Authorization Header will coninue to work until they have been sunset.   ## Using the Pre-Built Requests from the Collection  Once you have configured your environment. You can use any of the pre-built requests in the collection as a template for building new API requests. To start using one of the pre-built requests, simply click on it within the 'Collections' menu on the left side of Postman. This will open the request as a new tab in the main window of the Postman app.  In general, there are two types of requests that Braze's API endpoints accept - `GET` and `POST`. Depending on which `HTTP` method the endpoint uses, you'll need to edit the pre-built request differently.  ### Edit a POST Request  When editing a `POST` request, you'll need to open the request and navigate to the `Body` section in the request editor. For readability, select the `raw` radio button to format the `JSON` request body.  ### Edit a GET Request  When editing a `GET` request, you will need to edit the parameters passed in the request URL. To edit these easily, select the `Params` button next to the URL bar and edit the key-value pairs in the fields that will appear below the URL bar.  ## Send Your Request  Once your API request is ready to send, click on the 'Send' button next to the URL bar. The request will be sent and the response data will be populated in a section underneath the request editor. From here, you can view the raw data returned from Braze's API, see the HTTP response code, see how long the request took to process, and view header information.
 *
 * The version of the OpenAPI document: 1.0.0
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



import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CustomEventsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CustomEventsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CustomEventsApi(ApiClient apiClient) {
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
     * Build call for customEventsAnalytics_0
     * @param event (Required) String  The name of the custom event for which to return analytics  (optional)
     * @param length (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive (optional)
     * @param unit (Optional) String  Unit of time between data points - can be \&quot;day\&quot; or \&quot;hour\&quot; (defaults to \&quot;day\&quot;) (optional)
     * @param endingAt (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request (optional)
     * @param appId (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app (optional)
     * @param segmentId (Optional) String  Segment API identifier indicating the analytics enabled segment for which event analytics should be returned (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customEventsAnalytics_0Call(String event, String length, String unit, String endingAt, String appId, String segmentId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/events/data_series";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (event != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("event", event));
        }

        if (length != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("length", length));
        }

        if (unit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("unit", unit));
        }

        if (endingAt != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("ending_at", endingAt));
        }

        if (appId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("app_id", appId));
        }

        if (segmentId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("segment_id", segmentId));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call customEventsAnalytics_0ValidateBeforeCall(String event, String length, String unit, String endingAt, String appId, String segmentId, final ApiCallback _callback) throws ApiException {
        return customEventsAnalytics_0Call(event, length, unit, endingAt, appId, segmentId, _callback);

    }

    /**
     * Custom Events Analytics
     * This endpoint allows you to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.  ### Components Used -[Segment Identifier](https://www.braze.com/docs/api/identifier_types/)   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) point in time - as ISO 8601 extended when unit is \&quot;hour\&quot; and as ISO 8601 date when unit is \&quot;day\&quot;,             \&quot;count\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;  ### Fatal Error Response Codes The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |
     * @param event (Required) String  The name of the custom event for which to return analytics  (optional)
     * @param length (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive (optional)
     * @param unit (Optional) String  Unit of time between data points - can be \&quot;day\&quot; or \&quot;hour\&quot; (defaults to \&quot;day\&quot;) (optional)
     * @param endingAt (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request (optional)
     * @param appId (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app (optional)
     * @param segmentId (Optional) String  Segment API identifier indicating the analytics enabled segment for which event analytics should be returned (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void customEventsAnalytics_0(String event, String length, String unit, String endingAt, String appId, String segmentId) throws ApiException {
        customEventsAnalytics_0WithHttpInfo(event, length, unit, endingAt, appId, segmentId);
    }

    /**
     * Custom Events Analytics
     * This endpoint allows you to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.  ### Components Used -[Segment Identifier](https://www.braze.com/docs/api/identifier_types/)   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) point in time - as ISO 8601 extended when unit is \&quot;hour\&quot; and as ISO 8601 date when unit is \&quot;day\&quot;,             \&quot;count\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;  ### Fatal Error Response Codes The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |
     * @param event (Required) String  The name of the custom event for which to return analytics  (optional)
     * @param length (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive (optional)
     * @param unit (Optional) String  Unit of time between data points - can be \&quot;day\&quot; or \&quot;hour\&quot; (defaults to \&quot;day\&quot;) (optional)
     * @param endingAt (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request (optional)
     * @param appId (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app (optional)
     * @param segmentId (Optional) String  Segment API identifier indicating the analytics enabled segment for which event analytics should be returned (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> customEventsAnalytics_0WithHttpInfo(String event, String length, String unit, String endingAt, String appId, String segmentId) throws ApiException {
        okhttp3.Call localVarCall = customEventsAnalytics_0ValidateBeforeCall(event, length, unit, endingAt, appId, segmentId, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Custom Events Analytics (asynchronously)
     * This endpoint allows you to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.  ### Components Used -[Segment Identifier](https://www.braze.com/docs/api/identifier_types/)   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) point in time - as ISO 8601 extended when unit is \&quot;hour\&quot; and as ISO 8601 date when unit is \&quot;day\&quot;,             \&quot;count\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;  ### Fatal Error Response Codes The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |
     * @param event (Required) String  The name of the custom event for which to return analytics  (optional)
     * @param length (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive (optional)
     * @param unit (Optional) String  Unit of time between data points - can be \&quot;day\&quot; or \&quot;hour\&quot; (defaults to \&quot;day\&quot;) (optional)
     * @param endingAt (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request (optional)
     * @param appId (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app (optional)
     * @param segmentId (Optional) String  Segment API identifier indicating the analytics enabled segment for which event analytics should be returned (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customEventsAnalytics_0Async(String event, String length, String unit, String endingAt, String appId, String segmentId, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = customEventsAnalytics_0ValidateBeforeCall(event, length, unit, endingAt, appId, segmentId, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for customEventsList_0
     * @param page (Optional) Integer  The page of event names to return, defaults to 0 (returns the first set of up to 250) (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customEventsList_0Call(String page, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/events/list";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call customEventsList_0ValidateBeforeCall(String page, final ApiCallback _callback) throws ApiException {
        return customEventsList_0Call(page, _callback);

    }

    /**
     * Custom Events List
     * This endpoint allows you to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;events\&quot; : [         \&quot;Event A\&quot;,         \&quot;Event B\&quot;,         \&quot;Event C\&quot;,         ...     ] } &#x60;&#x60;&#x60;  ### Fatal Error Response Codes  The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |
     * @param page (Optional) Integer  The page of event names to return, defaults to 0 (returns the first set of up to 250) (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void customEventsList_0(String page) throws ApiException {
        customEventsList_0WithHttpInfo(page);
    }

    /**
     * Custom Events List
     * This endpoint allows you to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;events\&quot; : [         \&quot;Event A\&quot;,         \&quot;Event B\&quot;,         \&quot;Event C\&quot;,         ...     ] } &#x60;&#x60;&#x60;  ### Fatal Error Response Codes  The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |
     * @param page (Optional) Integer  The page of event names to return, defaults to 0 (returns the first set of up to 250) (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> customEventsList_0WithHttpInfo(String page) throws ApiException {
        okhttp3.Call localVarCall = customEventsList_0ValidateBeforeCall(page, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Custom Events List (asynchronously)
     * This endpoint allows you to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;events\&quot; : [         \&quot;Event A\&quot;,         \&quot;Event B\&quot;,         \&quot;Event C\&quot;,         ...     ] } &#x60;&#x60;&#x60;  ### Fatal Error Response Codes  The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |
     * @param page (Optional) Integer  The page of event names to return, defaults to 0 (returns the first set of up to 250) (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customEventsList_0Async(String page, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = customEventsList_0ValidateBeforeCall(page, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
