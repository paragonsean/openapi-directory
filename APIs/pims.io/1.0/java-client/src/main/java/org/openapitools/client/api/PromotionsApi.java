/*
 * Pims
 *  Hereafter is the documentation of the private API of [Pims: Pointages Intelligents pour le Monde du Spectacle](https://pims.io). This API is designed for 3rd-party softwares, editors and partners. Its main purpose is to give access the core data of a Pims customer (i.e. events, ticket counts and promotions).  ## Authentication The API uses [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), meaning you will need a username and password to get authorized.  As each customer in Pims has its own domain (e.g. caramba.pims.io, gdp.pims.io...), each credentials will be valid for one domain/customer only. If you need dedicated credentials for one domain, please contact us. (In any case, we will need an explicit agreement from the customer before we create these credentials.)  <div class=\"info\"> To make your life easy, you can try all endpoints with the public credentials below, pointing to our [demo domain](https://demo.pims.io):   <ul>     <li>Base path: `https://demo.pims.io/api`</li>     <li>Username: `demo`</li>     <li>Password: `q83792db2GCvgYVdKpU3yG3R`</li>   </ul> </div>  ## Response format The API returns JSON and matches the [HAL specification](http://stateless.co/hal_specification.html). The `Content-Type` of each response will be `application/hal+json`, unless an error occurs.  Please note that this documentation describes all responses “as if” they were plain JSON. The specificities of HAL are ignored on purpose, in order to remain compact and avoid repetition. <div style=\"-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;\">  <div style=\"display: inline-block; width:100%;\">   <strong>So when you read in the doc:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property1\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"object\"</span>: {   <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,   <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>  } }</code></pre>  </div>  <div style=\"display: inline-block; width:100%;\">   <strong>... you'll get in the Real World®:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property2\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"_embedded\"</span>: {   <span class=\"token string\">\"object\"</span>: {    <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,    <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>,    <span class=\"token string\">\"_links\"</span>: {     <span class=\"token string\">\"self\"</span>: {      <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/other-item/456\"</span>     }    }   }  }  <span class=\"token string\">\"_links\"</span>: {   <span class=\"token string\">\"self\"</span>: {    <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/item/123\"</span>   }  } }</code></pre>  </div> </div>  ### Errors Errors return JSON too and tries to match the [Problem Details for HTTP APIs specification](https://tools.ietf.org/html/rfc7807). If it does not match this spec, that's either a bug or a compatibility issue. Please contact us to solve the problem.  The `Content-Type` of errors will be `application/problem+json`. The content will match the following JSON: ```json {  \"type\": \"https://tools.ietf.org/html/rfc2616#section-10\",     \"title\": \"Not Found\",  \"status\": 404,     \"detail\": \"Entity not found\" } ```  ## Versioning The API is fully versionned, using an URL-versioning scheme: `https://demo.pims.io/api/v1/events`, `https://demo.pims.io/api/v2/events`,...  The version part of the URL is optional, and will be completed with the last stable version if omitted.  ## Pagination All responses corresponding to a collection of resources (e.g. `/venues` or `/series/:id/events`) are paginated. When so, you will only get the first 25 resources you asked for.  If you need to get more resources in one call, you can use the `page_size` query parameter. E.g. `/venues?page_size=50` to get the 50 first venues.  Also note that with HAL, the navigation in paginated responses is a piece of cake, as you can see below: ```json {  \"_links\": {   \"self\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=1\"   },   \"first\": {    \"href\": \"https://demo.pims.io/api/v1/events\"   },   \"last\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=14\"   },   \"next\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=2\"   }  },  \"_embedded\": {    ... // data content goes here  },  \"page_count\": 14,  \"page_size\": 25,  \"total_items\": 331,  \"page\": 1 } ```  ## Filtering and sorting Every textual filter (e.g. `/events?label=U2`) and/or sort (e.g. `/events?sort=label`) performed with the API uses UTF8_UNICODE_CI collation, meaning it is: - Case insensitive: “Chloé” will be considered the same as “CHLOÉ”; - Diacritic insensitive: “Chloé” will be considered the same as “Chloe”.  When performing a sort, it will always be *ascending* by default. To make it *descending*, just use a minus sign (`-`) in front of the parameter value (e.g. `/events?sort=-label`).  ## I18n In responses, some labels can be translated (e.g. promotion types, event input types, etc.). These translatable labels are clearly indicated in the documentation below.  By default, they will be displayed in English, but you can change this behaviour via the `Accept-Language` header. E.g., use `fr` as a value for French.  ## PHP SDK We provide a simple yet convenient SDK for the PHP language, see [the Github page of the project](https://github.com/pimssas/pims-api-client-php).  ## And now? Generaly, you will start by [fetching one or more events](#tag/Events). An <span class=\"definition\">event</span> can be anything that occurs in one venue at one given date and time: a concert, a play, a match, a conference, etc. Additionnally, you can explore the [series](#tag/Series): a <span class=\"definition\">series</span> is just a group of events (e.g. a tour or a festival).  Once you retrieved the events you were interested in, you can look for the sales (<span class=\"definition\">ticket counts</span>): - Get a quick overview with [`/events/:id/ticket-counts`](#operation/fetchAllTicketCounts) - Or get a full insight by calling these endpoints:     1. [`/events/:id/categories`](#operation/fetchAllEventsCategories)     2. [`/events/:id/channels`](#operation/fetchAllEventsChannels)     3. [`/events/:id/ticket-counts/detailed`](#operation/fetchAllDetailedTicketCounts)  Eventually, you may also want to fetch the [promotions](#tag/Promotions). A <span class=\"definition\">promotion</span> can be anything meant to leverage the sales: ads, marketing campaigns, buzz or news around the event, etc. A promotion can be linked to any combination of events and/or series.
 *
 * The version of the OpenAPI document: 1.0
 * Contact: support@pims.io
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


import org.openapitools.client.model.Error401;
import org.openapitools.client.model.Error403;
import org.openapitools.client.model.Error404;
import org.openapitools.client.model.Error422;
import org.openapitools.client.model.Error500;
import java.time.LocalDate;
import org.openapitools.client.model.PromotionsEntity;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PromotionsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public PromotionsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public PromotionsApi(ApiClient apiClient) {
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
     * Build call for fetchAllEventsPromotions
     * @param eventId ID of the targeted event. (required)
     * @param label Find only the promotions whose label contains this value. (optional)
     * @param fromDate Find only the promotions starting after this date. (optional)
     * @param toDate Find only the promotions ending before this date. (optional)
     * @param type Find only the promotions whose type is equal to this value. (optional)
     * @param family Find only the promotions whose family is equal to this value. (optional)
     * @param sort Sort the promotions in the corresponding order. (optional, default to date)
     * @param pageSize Pagination size, i.e. maximum number of items to be displayed in the response. (optional, default to 25)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives an array of promotions </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call fetchAllEventsPromotionsCall(Integer eventId, String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/events/{event_id}/promotions"
            .replace("{" + "event_id" + "}", localVarApiClient.escapeString(eventId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (label != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("label", label));
        }

        if (fromDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("from_date", fromDate));
        }

        if (toDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("to_date", toDate));
        }

        if (type != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("type", type));
        }

        if (family != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("family", family));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (acceptLanguage != null) {
            localVarHeaderParams.put("Accept-Language", localVarApiClient.parameterToString(acceptLanguage));
        }

        final String[] localVarAccepts = {
            "application/hal+json"
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

        String[] localVarAuthNames = new String[] { "Basic Auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call fetchAllEventsPromotionsValidateBeforeCall(Integer eventId, String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'eventId' is set
        if (eventId == null) {
            throw new ApiException("Missing the required parameter 'eventId' when calling fetchAllEventsPromotions(Async)");
        }

        return fetchAllEventsPromotionsCall(eventId, label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage, _callback);

    }

    /**
     * Find all promotions for one event
     * 
     * @param eventId ID of the targeted event. (required)
     * @param label Find only the promotions whose label contains this value. (optional)
     * @param fromDate Find only the promotions starting after this date. (optional)
     * @param toDate Find only the promotions ending before this date. (optional)
     * @param type Find only the promotions whose type is equal to this value. (optional)
     * @param family Find only the promotions whose family is equal to this value. (optional)
     * @param sort Sort the promotions in the corresponding order. (optional, default to date)
     * @param pageSize Pagination size, i.e. maximum number of items to be displayed in the response. (optional, default to 25)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @return List&lt;PromotionsEntity&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives an array of promotions </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public List<PromotionsEntity> fetchAllEventsPromotions(Integer eventId, String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage) throws ApiException {
        ApiResponse<List<PromotionsEntity>> localVarResp = fetchAllEventsPromotionsWithHttpInfo(eventId, label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage);
        return localVarResp.getData();
    }

    /**
     * Find all promotions for one event
     * 
     * @param eventId ID of the targeted event. (required)
     * @param label Find only the promotions whose label contains this value. (optional)
     * @param fromDate Find only the promotions starting after this date. (optional)
     * @param toDate Find only the promotions ending before this date. (optional)
     * @param type Find only the promotions whose type is equal to this value. (optional)
     * @param family Find only the promotions whose family is equal to this value. (optional)
     * @param sort Sort the promotions in the corresponding order. (optional, default to date)
     * @param pageSize Pagination size, i.e. maximum number of items to be displayed in the response. (optional, default to 25)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @return ApiResponse&lt;List&lt;PromotionsEntity&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives an array of promotions </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<PromotionsEntity>> fetchAllEventsPromotionsWithHttpInfo(Integer eventId, String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage) throws ApiException {
        okhttp3.Call localVarCall = fetchAllEventsPromotionsValidateBeforeCall(eventId, label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage, null);
        Type localVarReturnType = new TypeToken<List<PromotionsEntity>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Find all promotions for one event (asynchronously)
     * 
     * @param eventId ID of the targeted event. (required)
     * @param label Find only the promotions whose label contains this value. (optional)
     * @param fromDate Find only the promotions starting after this date. (optional)
     * @param toDate Find only the promotions ending before this date. (optional)
     * @param type Find only the promotions whose type is equal to this value. (optional)
     * @param family Find only the promotions whose family is equal to this value. (optional)
     * @param sort Sort the promotions in the corresponding order. (optional, default to date)
     * @param pageSize Pagination size, i.e. maximum number of items to be displayed in the response. (optional, default to 25)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives an array of promotions </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call fetchAllEventsPromotionsAsync(Integer eventId, String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage, final ApiCallback<List<PromotionsEntity>> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchAllEventsPromotionsValidateBeforeCall(eventId, label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage, _callback);
        Type localVarReturnType = new TypeToken<List<PromotionsEntity>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for fetchAllPromotions
     * @param label Find only the promotions whose label contains this value. (optional)
     * @param fromDate Find only the promotions starting after this date. (optional)
     * @param toDate Find only the promotions ending before this date. (optional)
     * @param type Find only the promotions whose type is equal to this value. (optional)
     * @param family Find only the promotions whose family is equal to this value. (optional)
     * @param sort Sort the promotions in the corresponding order. (optional, default to date)
     * @param pageSize Pagination size, i.e. maximum number of items to be displayed in the response. (optional, default to 25)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives an array of promotions </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call fetchAllPromotionsCall(String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/promotions";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (label != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("label", label));
        }

        if (fromDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("from_date", fromDate));
        }

        if (toDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("to_date", toDate));
        }

        if (type != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("type", type));
        }

        if (family != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("family", family));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (acceptLanguage != null) {
            localVarHeaderParams.put("Accept-Language", localVarApiClient.parameterToString(acceptLanguage));
        }

        final String[] localVarAccepts = {
            "application/hal+json"
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

        String[] localVarAuthNames = new String[] { "Basic Auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call fetchAllPromotionsValidateBeforeCall(String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage, final ApiCallback _callback) throws ApiException {
        return fetchAllPromotionsCall(label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage, _callback);

    }

    /**
     * Find all promotions
     * 
     * @param label Find only the promotions whose label contains this value. (optional)
     * @param fromDate Find only the promotions starting after this date. (optional)
     * @param toDate Find only the promotions ending before this date. (optional)
     * @param type Find only the promotions whose type is equal to this value. (optional)
     * @param family Find only the promotions whose family is equal to this value. (optional)
     * @param sort Sort the promotions in the corresponding order. (optional, default to date)
     * @param pageSize Pagination size, i.e. maximum number of items to be displayed in the response. (optional, default to 25)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @return List&lt;PromotionsEntity&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives an array of promotions </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public List<PromotionsEntity> fetchAllPromotions(String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage) throws ApiException {
        ApiResponse<List<PromotionsEntity>> localVarResp = fetchAllPromotionsWithHttpInfo(label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage);
        return localVarResp.getData();
    }

    /**
     * Find all promotions
     * 
     * @param label Find only the promotions whose label contains this value. (optional)
     * @param fromDate Find only the promotions starting after this date. (optional)
     * @param toDate Find only the promotions ending before this date. (optional)
     * @param type Find only the promotions whose type is equal to this value. (optional)
     * @param family Find only the promotions whose family is equal to this value. (optional)
     * @param sort Sort the promotions in the corresponding order. (optional, default to date)
     * @param pageSize Pagination size, i.e. maximum number of items to be displayed in the response. (optional, default to 25)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @return ApiResponse&lt;List&lt;PromotionsEntity&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives an array of promotions </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<PromotionsEntity>> fetchAllPromotionsWithHttpInfo(String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage) throws ApiException {
        okhttp3.Call localVarCall = fetchAllPromotionsValidateBeforeCall(label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage, null);
        Type localVarReturnType = new TypeToken<List<PromotionsEntity>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Find all promotions (asynchronously)
     * 
     * @param label Find only the promotions whose label contains this value. (optional)
     * @param fromDate Find only the promotions starting after this date. (optional)
     * @param toDate Find only the promotions ending before this date. (optional)
     * @param type Find only the promotions whose type is equal to this value. (optional)
     * @param family Find only the promotions whose family is equal to this value. (optional)
     * @param sort Sort the promotions in the corresponding order. (optional, default to date)
     * @param pageSize Pagination size, i.e. maximum number of items to be displayed in the response. (optional, default to 25)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives an array of promotions </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call fetchAllPromotionsAsync(String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage, final ApiCallback<List<PromotionsEntity>> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchAllPromotionsValidateBeforeCall(label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage, _callback);
        Type localVarReturnType = new TypeToken<List<PromotionsEntity>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for fetchAllSeriesPromotions
     * @param seriesId ID of the targeted series. (required)
     * @param label Find only the promotions whose label contains this value. (optional)
     * @param fromDate Find only the promotions starting after this date. (optional)
     * @param toDate Find only the promotions ending before this date. (optional)
     * @param type Find only the promotions whose type is equal to this value. (optional)
     * @param family Find only the promotions whose family is equal to this value. (optional)
     * @param sort Sort the promotions in the corresponding order. (optional, default to date)
     * @param pageSize Pagination size, i.e. maximum number of items to be displayed in the response. (optional, default to 25)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives an array of promotions </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call fetchAllSeriesPromotionsCall(Integer seriesId, String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/series/{series_id}/promotions"
            .replace("{" + "series_id" + "}", localVarApiClient.escapeString(seriesId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (label != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("label", label));
        }

        if (fromDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("from_date", fromDate));
        }

        if (toDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("to_date", toDate));
        }

        if (type != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("type", type));
        }

        if (family != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("family", family));
        }

        if (sort != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sort", sort));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (acceptLanguage != null) {
            localVarHeaderParams.put("Accept-Language", localVarApiClient.parameterToString(acceptLanguage));
        }

        final String[] localVarAccepts = {
            "application/hal+json"
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

        String[] localVarAuthNames = new String[] { "Basic Auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call fetchAllSeriesPromotionsValidateBeforeCall(Integer seriesId, String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'seriesId' is set
        if (seriesId == null) {
            throw new ApiException("Missing the required parameter 'seriesId' when calling fetchAllSeriesPromotions(Async)");
        }

        return fetchAllSeriesPromotionsCall(seriesId, label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage, _callback);

    }

    /**
     * Find all promotions for one series
     * 
     * @param seriesId ID of the targeted series. (required)
     * @param label Find only the promotions whose label contains this value. (optional)
     * @param fromDate Find only the promotions starting after this date. (optional)
     * @param toDate Find only the promotions ending before this date. (optional)
     * @param type Find only the promotions whose type is equal to this value. (optional)
     * @param family Find only the promotions whose family is equal to this value. (optional)
     * @param sort Sort the promotions in the corresponding order. (optional, default to date)
     * @param pageSize Pagination size, i.e. maximum number of items to be displayed in the response. (optional, default to 25)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @return List&lt;PromotionsEntity&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives an array of promotions </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public List<PromotionsEntity> fetchAllSeriesPromotions(Integer seriesId, String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage) throws ApiException {
        ApiResponse<List<PromotionsEntity>> localVarResp = fetchAllSeriesPromotionsWithHttpInfo(seriesId, label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage);
        return localVarResp.getData();
    }

    /**
     * Find all promotions for one series
     * 
     * @param seriesId ID of the targeted series. (required)
     * @param label Find only the promotions whose label contains this value. (optional)
     * @param fromDate Find only the promotions starting after this date. (optional)
     * @param toDate Find only the promotions ending before this date. (optional)
     * @param type Find only the promotions whose type is equal to this value. (optional)
     * @param family Find only the promotions whose family is equal to this value. (optional)
     * @param sort Sort the promotions in the corresponding order. (optional, default to date)
     * @param pageSize Pagination size, i.e. maximum number of items to be displayed in the response. (optional, default to 25)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @return ApiResponse&lt;List&lt;PromotionsEntity&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives an array of promotions </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<PromotionsEntity>> fetchAllSeriesPromotionsWithHttpInfo(Integer seriesId, String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage) throws ApiException {
        okhttp3.Call localVarCall = fetchAllSeriesPromotionsValidateBeforeCall(seriesId, label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage, null);
        Type localVarReturnType = new TypeToken<List<PromotionsEntity>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Find all promotions for one series (asynchronously)
     * 
     * @param seriesId ID of the targeted series. (required)
     * @param label Find only the promotions whose label contains this value. (optional)
     * @param fromDate Find only the promotions starting after this date. (optional)
     * @param toDate Find only the promotions ending before this date. (optional)
     * @param type Find only the promotions whose type is equal to this value. (optional)
     * @param family Find only the promotions whose family is equal to this value. (optional)
     * @param sort Sort the promotions in the corresponding order. (optional, default to date)
     * @param pageSize Pagination size, i.e. maximum number of items to be displayed in the response. (optional, default to 25)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives an array of promotions </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 422 </td><td> Unprocessable Entity </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call fetchAllSeriesPromotionsAsync(Integer seriesId, String label, LocalDate fromDate, LocalDate toDate, String type, String family, String sort, Integer pageSize, String acceptLanguage, final ApiCallback<List<PromotionsEntity>> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchAllSeriesPromotionsValidateBeforeCall(seriesId, label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage, _callback);
        Type localVarReturnType = new TypeToken<List<PromotionsEntity>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for fetchOnePromotion
     * @param promotionId ID of the targeted promotion. (required)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives one promotion </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call fetchOnePromotionCall(Integer promotionId, String acceptLanguage, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/promotions/{promotion_id}"
            .replace("{" + "promotion_id" + "}", localVarApiClient.escapeString(promotionId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (acceptLanguage != null) {
            localVarHeaderParams.put("Accept-Language", localVarApiClient.parameterToString(acceptLanguage));
        }

        final String[] localVarAccepts = {
            "application/hal+json"
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

        String[] localVarAuthNames = new String[] { "Basic Auth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call fetchOnePromotionValidateBeforeCall(Integer promotionId, String acceptLanguage, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'promotionId' is set
        if (promotionId == null) {
            throw new ApiException("Missing the required parameter 'promotionId' when calling fetchOnePromotion(Async)");
        }

        return fetchOnePromotionCall(promotionId, acceptLanguage, _callback);

    }

    /**
     * Get one promotion by ID
     * 
     * @param promotionId ID of the targeted promotion. (required)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @return PromotionsEntity
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives one promotion </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public PromotionsEntity fetchOnePromotion(Integer promotionId, String acceptLanguage) throws ApiException {
        ApiResponse<PromotionsEntity> localVarResp = fetchOnePromotionWithHttpInfo(promotionId, acceptLanguage);
        return localVarResp.getData();
    }

    /**
     * Get one promotion by ID
     * 
     * @param promotionId ID of the targeted promotion. (required)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @return ApiResponse&lt;PromotionsEntity&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives one promotion </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PromotionsEntity> fetchOnePromotionWithHttpInfo(Integer promotionId, String acceptLanguage) throws ApiException {
        okhttp3.Call localVarCall = fetchOnePromotionValidateBeforeCall(promotionId, acceptLanguage, null);
        Type localVarReturnType = new TypeToken<PromotionsEntity>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get one promotion by ID (asynchronously)
     * 
     * @param promotionId ID of the targeted promotion. (required)
     * @param acceptLanguage Language used for the translatable labels. (optional, default to en)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Successful operation, gives one promotion </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized, no authentication was made </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Forbidden, the authentication is wrong </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Unexpected error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call fetchOnePromotionAsync(Integer promotionId, String acceptLanguage, final ApiCallback<PromotionsEntity> _callback) throws ApiException {

        okhttp3.Call localVarCall = fetchOnePromotionValidateBeforeCall(promotionId, acceptLanguage, _callback);
        Type localVarReturnType = new TypeToken<PromotionsEntity>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
