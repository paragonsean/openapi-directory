/*
 * OpenFinTech.io
 * # Introduction [OpenFinTech.io](https://openfintech.io) is an open database that comprises of standardized primary data for FinTech industry.<br> It contains such information as geolocation data (countries, cities, regions), organizations, currencies (national, digital, virtual, crypto), banks, digital exchangers, payment providers (PSP), payment methods, etc.<br> It is created for communication of cross-integrated micro-services on \"one language\". This is achieved through standardization of entity identifiers that are used to exchange information among different services.<br>  ### UML UML Domain Model diagram you can find [here](https://api.openfintech.io/public_domain_model.png).<br>  ### Persistence Entities are updated not more than 1 time per day.<br>  ### Terms and Conditions This *OpenFinTech.io* is made available under the [Open Database License](http://opendatacommons.org/licenses/odbl/1.0/).<br> Any rights in individual contents of the database are licensed under the [Database Contents License](http://opendatacommons.org/licenses/dbcl/1.0/).<br>  ### Contacts For any questions, please email - info@openfintech.io<br> Or you can contact us at <a href=\"https://gitter.im/paymaxicom/openfintech.io\">Gitter</a><br>  Powered by [Paymaxi](https://www.paymaxi.com)  # Get Started  If you use [POSTMAN](https://www.getpostman.com) or similar program which can operate with swagger`s files - just [download](https://docs.openfintech.io) our spec and [import it](https://www.getpostman.com/docs/importing_swagger). Also you can try live [API demo](https://api.openfintech.io).  ## Overview  The OpenFinTech API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors.<br> API is based on [JSON API](http://jsonapi.org) standard. JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.<br> JSON API requires use of the JSON API media type (`application/vnd.api+json`) for exchanging data.<br> ### Additional Request Headers #### ACCEPT HEADER Your requests should always include the header: ```curl Accept: application/vnd.api+json ```  ## Authentication  To use OpenFinTech API no needed authorization.  ## Versioning  When we make changes to the API, we release new, dated versions. The current version is **2017-08-24**. Read our [API upgrades guide]() to see our API changelog and to learn more about backwards compatibility.  ## Pagination  OpenFinTech APIs to retrieve lists of banks, currencies and other resources - paginated to **100** items by default. The pagination information will be included in the list API response under the node name `meta` - contains information about listed objects [`total` - contains information about total count of listed objects, `pages` - count of pages], `links` - contain links to navigate between pages [`first` - link to first page, `prev` - link to previous page, `next` - link to next page, `last` - link to last page].<br> By default first page will be listed. For navigating through pages, use the page parameter (e.g. `page[number]`, `page[size]`).<br> The `page[size]` parameter can be used to set the number of records that you want to receive in the response.<br> The `page[number]` parameter can be used to set needed page number.<br> Example of response: ```json {   \"meta\": {     \"total\": 419,     \"pages\": 42   },   \"links\": {     \"first\": \"/v1/{path}?page[number]=1&page[size]=10\",     \"prev\": \"/v1/{path}?page[number]=39&page[size]=10\",     \"next\": \"/v1/{path}?page[number]=41&page[size]=10\",     \"last\": \"/v1/{path}?page[number]=42&page[size]=10\"   } ```  ### Sorting  OpenFinTech\\`s API supported query parameter to sort result collection [e.g. `?sort=code`]. Information about available parameters may be found in the endpoint description. Positive parameter [e.g. `?sort=code`] points to ascending sorting, negative  [e.g. `?sort=-code`] - to descending sorting. Also, supported multiple sorting parameters [e.g. `?sort=code, -name, id`, etc.] ```curl https://api.openfintech.io/v1/countries?sort=name,-area ```  ### Filtering  Filtering provided by unique query key `filter[*filtering_condition*]`. Information about available parameters may be found in the endpoint description. ```curl https://api.openfintech.io/v1/countries?filter[region]=europe ```  ## Images  OpenFinTech provides two types of images: icons and logos. To get one of those types you should to use next url pattern: ``` curl https://api.openfintech.io/v1/{path}/{id}/{icon/logo} ``` Also, images can be resized by adding next parameters: `h={height}&w={width}`. For example, you want to get organization icon with width equals to 20 pixels: ``` curl https://api.openfintech.io/v1/organizations/{id}/icon?w=20&h=20 ``` If argument height or width is missing API returns original image with real sizes.  ## Errors  API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.), and codes in the `5xx` range indicate an error with OpenFinTech's servers (these are rare).  | Code | Description | |------|-------------| | 200 - OK | Everything worked as expected. | | 400 - Bad Request | The request was unacceptable, often due to missing a required parameter. | | 401 - Unauthorized | No valid API key provided. | | 402 - Request Failed | The parameters were valid but the request failed. | | 404 - Not Found | The requested resource doesn't exist. | | 409 - Conflict | The request conflicts with another request (perhaps due to using the same idempotent key). | | 429 - Too Many Requests | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. | | 500, 502, 503, 504 - Server Errors | Something went wrong on OpenFinTech's end. (These are rare.) | 
 *
 * The version of the OpenAPI document: 2017-08-24
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


import org.openapitools.client.model.CurrenciesResponse;
import org.openapitools.client.model.CurrencyResponse;
import java.util.Set;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CurrenciesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CurrenciesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CurrenciesApi(ApiClient apiClient) {
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
     * Build call for currenciesGet
     * @param pageNumber Current page number. (optional)
     * @param pageSize Page size.&lt;br&gt;*Default value: 100*  (optional)
     * @param filterSearch Full text search with name, code, type, code_iso_alpha3, code_jsons_alpha, code_estandards_alpha, category. (optional)
     * @param filterCodeIsoAlpha3 Filtering by ISO code. (optional)
     * @param filterCodeIsoNumeric3 Filtering by ISO number. (optional)
     * @param filterCodeEstandardsAlpha Filtering by estandards code. (optional)
     * @param filterCurrencyType Filtration by currency type. (optional)
     * @param filterCategory Filtration by category. (optional)
     * @param sort Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | type | -type | | category | -category | | code | -code | | code_iso_alpha3 | -code_iso_alpha3 | | code_iso_numeric3 | -code_iso_numeric3 | | code_estandards_alpha | -code_estandards_alpha |  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of currencies. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call currenciesGetCall(Integer pageNumber, Integer pageSize, String filterSearch, String filterCodeIsoAlpha3, Integer filterCodeIsoNumeric3, String filterCodeEstandardsAlpha, Set<String> filterCurrencyType, Set<String> filterCategory, Set<String> sort, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/currencies";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (pageNumber != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page[number]", pageNumber));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page[size]", pageSize));
        }

        if (filterSearch != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter[search]", filterSearch));
        }

        if (filterCodeIsoAlpha3 != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter[code_iso_alpha3]", filterCodeIsoAlpha3));
        }

        if (filterCodeIsoNumeric3 != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter[code_iso_numeric3]", filterCodeIsoNumeric3));
        }

        if (filterCodeEstandardsAlpha != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("filter[code_estandards_alpha]", filterCodeEstandardsAlpha));
        }

        if (filterCurrencyType != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("csv", "filter[currency_type]", filterCurrencyType));
        }

        if (filterCategory != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("csv", "filter[category]", filterCategory));
        }

        if (sort != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("csv", "sort", sort));
        }

        final String[] localVarAccepts = {
            "application/vnd.api+json"
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
    private okhttp3.Call currenciesGetValidateBeforeCall(Integer pageNumber, Integer pageSize, String filterSearch, String filterCodeIsoAlpha3, Integer filterCodeIsoNumeric3, String filterCodeEstandardsAlpha, Set<String> filterCurrencyType, Set<String> filterCategory, Set<String> sort, final ApiCallback _callback) throws ApiException {
        return currenciesGetCall(pageNumber, pageSize, filterSearch, filterCodeIsoAlpha3, filterCodeIsoNumeric3, filterCodeEstandardsAlpha, filterCurrencyType, filterCategory, sort, _callback);

    }

    /**
     * List of currencies
     * Returns all available currencies. 
     * @param pageNumber Current page number. (optional)
     * @param pageSize Page size.&lt;br&gt;*Default value: 100*  (optional)
     * @param filterSearch Full text search with name, code, type, code_iso_alpha3, code_jsons_alpha, code_estandards_alpha, category. (optional)
     * @param filterCodeIsoAlpha3 Filtering by ISO code. (optional)
     * @param filterCodeIsoNumeric3 Filtering by ISO number. (optional)
     * @param filterCodeEstandardsAlpha Filtering by estandards code. (optional)
     * @param filterCurrencyType Filtration by currency type. (optional)
     * @param filterCategory Filtration by category. (optional)
     * @param sort Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | type | -type | | category | -category | | code | -code | | code_iso_alpha3 | -code_iso_alpha3 | | code_iso_numeric3 | -code_iso_numeric3 | | code_estandards_alpha | -code_estandards_alpha |  (optional)
     * @return CurrenciesResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of currencies. </td><td>  -  </td></tr>
     </table>
     */
    public CurrenciesResponse currenciesGet(Integer pageNumber, Integer pageSize, String filterSearch, String filterCodeIsoAlpha3, Integer filterCodeIsoNumeric3, String filterCodeEstandardsAlpha, Set<String> filterCurrencyType, Set<String> filterCategory, Set<String> sort) throws ApiException {
        ApiResponse<CurrenciesResponse> localVarResp = currenciesGetWithHttpInfo(pageNumber, pageSize, filterSearch, filterCodeIsoAlpha3, filterCodeIsoNumeric3, filterCodeEstandardsAlpha, filterCurrencyType, filterCategory, sort);
        return localVarResp.getData();
    }

    /**
     * List of currencies
     * Returns all available currencies. 
     * @param pageNumber Current page number. (optional)
     * @param pageSize Page size.&lt;br&gt;*Default value: 100*  (optional)
     * @param filterSearch Full text search with name, code, type, code_iso_alpha3, code_jsons_alpha, code_estandards_alpha, category. (optional)
     * @param filterCodeIsoAlpha3 Filtering by ISO code. (optional)
     * @param filterCodeIsoNumeric3 Filtering by ISO number. (optional)
     * @param filterCodeEstandardsAlpha Filtering by estandards code. (optional)
     * @param filterCurrencyType Filtration by currency type. (optional)
     * @param filterCategory Filtration by category. (optional)
     * @param sort Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | type | -type | | category | -category | | code | -code | | code_iso_alpha3 | -code_iso_alpha3 | | code_iso_numeric3 | -code_iso_numeric3 | | code_estandards_alpha | -code_estandards_alpha |  (optional)
     * @return ApiResponse&lt;CurrenciesResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of currencies. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CurrenciesResponse> currenciesGetWithHttpInfo(Integer pageNumber, Integer pageSize, String filterSearch, String filterCodeIsoAlpha3, Integer filterCodeIsoNumeric3, String filterCodeEstandardsAlpha, Set<String> filterCurrencyType, Set<String> filterCategory, Set<String> sort) throws ApiException {
        okhttp3.Call localVarCall = currenciesGetValidateBeforeCall(pageNumber, pageSize, filterSearch, filterCodeIsoAlpha3, filterCodeIsoNumeric3, filterCodeEstandardsAlpha, filterCurrencyType, filterCategory, sort, null);
        Type localVarReturnType = new TypeToken<CurrenciesResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * List of currencies (asynchronously)
     * Returns all available currencies. 
     * @param pageNumber Current page number. (optional)
     * @param pageSize Page size.&lt;br&gt;*Default value: 100*  (optional)
     * @param filterSearch Full text search with name, code, type, code_iso_alpha3, code_jsons_alpha, code_estandards_alpha, category. (optional)
     * @param filterCodeIsoAlpha3 Filtering by ISO code. (optional)
     * @param filterCodeIsoNumeric3 Filtering by ISO number. (optional)
     * @param filterCodeEstandardsAlpha Filtering by estandards code. (optional)
     * @param filterCurrencyType Filtration by currency type. (optional)
     * @param filterCategory Filtration by category. (optional)
     * @param sort Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | type | -type | | category | -category | | code | -code | | code_iso_alpha3 | -code_iso_alpha3 | | code_iso_numeric3 | -code_iso_numeric3 | | code_estandards_alpha | -code_estandards_alpha |  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> List of currencies. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call currenciesGetAsync(Integer pageNumber, Integer pageSize, String filterSearch, String filterCodeIsoAlpha3, Integer filterCodeIsoNumeric3, String filterCodeEstandardsAlpha, Set<String> filterCurrencyType, Set<String> filterCategory, Set<String> sort, final ApiCallback<CurrenciesResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = currenciesGetValidateBeforeCall(pageNumber, pageSize, filterSearch, filterCodeIsoAlpha3, filterCodeIsoNumeric3, filterCodeEstandardsAlpha, filterCurrencyType, filterCategory, sort, _callback);
        Type localVarReturnType = new TypeToken<CurrenciesResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for currenciesIdGet
     * @param id Unique ID. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Currency information. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Currency ID is not valid. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call currenciesIdGetCall(String id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/currencies/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/vnd.api+json"
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
    private okhttp3.Call currenciesIdGetValidateBeforeCall(String id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling currenciesIdGet(Async)");
        }

        return currenciesIdGetCall(id, _callback);

    }

    /**
     * Currency by ID
     * Returns currency with specific ID. 
     * @param id Unique ID. (required)
     * @return CurrencyResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Currency information. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Currency ID is not valid. </td><td>  -  </td></tr>
     </table>
     */
    public CurrencyResponse currenciesIdGet(String id) throws ApiException {
        ApiResponse<CurrencyResponse> localVarResp = currenciesIdGetWithHttpInfo(id);
        return localVarResp.getData();
    }

    /**
     * Currency by ID
     * Returns currency with specific ID. 
     * @param id Unique ID. (required)
     * @return ApiResponse&lt;CurrencyResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Currency information. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Currency ID is not valid. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CurrencyResponse> currenciesIdGetWithHttpInfo(String id) throws ApiException {
        okhttp3.Call localVarCall = currenciesIdGetValidateBeforeCall(id, null);
        Type localVarReturnType = new TypeToken<CurrencyResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Currency by ID (asynchronously)
     * Returns currency with specific ID. 
     * @param id Unique ID. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Currency information. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Currency ID is not valid. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call currenciesIdGetAsync(String id, final ApiCallback<CurrencyResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = currenciesIdGetValidateBeforeCall(id, _callback);
        Type localVarReturnType = new TypeToken<CurrencyResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
