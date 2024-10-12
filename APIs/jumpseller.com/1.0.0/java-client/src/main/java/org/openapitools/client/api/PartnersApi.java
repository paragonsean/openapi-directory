/*
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
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


import org.openapitools.client.model.PartnerError;
import org.openapitools.client.model.PartnerStoreCode;
import org.openapitools.client.model.PartnerStoreCreate;
import org.openapitools.client.model.StoreCheckStatusJsonGet200Response;
import org.openapitools.client.model.Type;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PartnersApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public PartnersApi() {
        this(Configuration.getDefaultApiClient());
    }

    public PartnersApi(ApiClient apiClient) {
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
     * Build call for partnersStoresJsonGet
     * @param partnerCode Partner code. (required)
     * @param authToken Partner authentication token. (required)
     * @param from Statistics start date. Should be in format &#39;Y-m-d&#39;. (required)
     * @param to Statistics end date. Should be in format &#39;Y-m-d&#39;. (required)
     * @param page List page (optional, default to 1)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Array of partner stores statistics. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call partnersStoresJsonGetCall(String partnerCode, String authToken, String from, String to, Integer page, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/partners/stores.json";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (partnerCode != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("partner_code", partnerCode));
        }

        if (authToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("auth_token", authToken));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (from != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("from", from));
        }

        if (to != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("to", to));
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
    private okhttp3.Call partnersStoresJsonGetValidateBeforeCall(String partnerCode, String authToken, String from, String to, Integer page, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'partnerCode' is set
        if (partnerCode == null) {
            throw new ApiException("Missing the required parameter 'partnerCode' when calling partnersStoresJsonGet(Async)");
        }

        // verify the required parameter 'authToken' is set
        if (authToken == null) {
            throw new ApiException("Missing the required parameter 'authToken' when calling partnersStoresJsonGet(Async)");
        }

        // verify the required parameter 'from' is set
        if (from == null) {
            throw new ApiException("Missing the required parameter 'from' when calling partnersStoresJsonGet(Async)");
        }

        // verify the required parameter 'to' is set
        if (to == null) {
            throw new ApiException("Missing the required parameter 'to' when calling partnersStoresJsonGet(Async)");
        }

        return partnersStoresJsonGetCall(partnerCode, authToken, from, to, page, _callback);

    }

    /**
     * Retrieve statistics.
     * 
     * @param partnerCode Partner code. (required)
     * @param authToken Partner authentication token. (required)
     * @param from Statistics start date. Should be in format &#39;Y-m-d&#39;. (required)
     * @param to Statistics end date. Should be in format &#39;Y-m-d&#39;. (required)
     * @param page List page (optional, default to 1)
     * @return List&lt;Type&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Array of partner stores statistics. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. </td><td>  -  </td></tr>
     </table>
     */
    public List<Type> partnersStoresJsonGet(String partnerCode, String authToken, String from, String to, Integer page) throws ApiException {
        ApiResponse<List<Type>> localVarResp = partnersStoresJsonGetWithHttpInfo(partnerCode, authToken, from, to, page);
        return localVarResp.getData();
    }

    /**
     * Retrieve statistics.
     * 
     * @param partnerCode Partner code. (required)
     * @param authToken Partner authentication token. (required)
     * @param from Statistics start date. Should be in format &#39;Y-m-d&#39;. (required)
     * @param to Statistics end date. Should be in format &#39;Y-m-d&#39;. (required)
     * @param page List page (optional, default to 1)
     * @return ApiResponse&lt;List&lt;Type&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Array of partner stores statistics. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Type>> partnersStoresJsonGetWithHttpInfo(String partnerCode, String authToken, String from, String to, Integer page) throws ApiException {
        okhttp3.Call localVarCall = partnersStoresJsonGetValidateBeforeCall(partnerCode, authToken, from, to, page, null);
        Type localVarReturnType = new TypeToken<List<Type>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve statistics. (asynchronously)
     * 
     * @param partnerCode Partner code. (required)
     * @param authToken Partner authentication token. (required)
     * @param from Statistics start date. Should be in format &#39;Y-m-d&#39;. (required)
     * @param to Statistics end date. Should be in format &#39;Y-m-d&#39;. (required)
     * @param page List page (optional, default to 1)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Array of partner stores statistics. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call partnersStoresJsonGetAsync(String partnerCode, String authToken, String from, String to, Integer page, final ApiCallback<List<Type>> _callback) throws ApiException {

        okhttp3.Call localVarCall = partnersStoresJsonGetValidateBeforeCall(partnerCode, authToken, from, to, page, _callback);
        Type localVarReturnType = new TypeToken<List<Type>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for storeCheckStatusJsonGet
     * @param partnerCode Partner code. (required)
     * @param authToken Partner authentication token. (required)
     * @param storeCode Store Code (required)
     * @param locale ISO 3166-2 code of the language used in the response messages. (optional, default to en)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Store status object if creation is still in progress. A new Partner Store object when creation is done. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call storeCheckStatusJsonGetCall(String partnerCode, String authToken, String storeCode, String locale, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/store/check_status.json";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (partnerCode != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("partner_code", partnerCode));
        }

        if (authToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("auth_token", authToken));
        }

        if (storeCode != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("store_code", storeCode));
        }

        if (locale != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("locale", locale));
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
    private okhttp3.Call storeCheckStatusJsonGetValidateBeforeCall(String partnerCode, String authToken, String storeCode, String locale, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'partnerCode' is set
        if (partnerCode == null) {
            throw new ApiException("Missing the required parameter 'partnerCode' when calling storeCheckStatusJsonGet(Async)");
        }

        // verify the required parameter 'authToken' is set
        if (authToken == null) {
            throw new ApiException("Missing the required parameter 'authToken' when calling storeCheckStatusJsonGet(Async)");
        }

        // verify the required parameter 'storeCode' is set
        if (storeCode == null) {
            throw new ApiException("Missing the required parameter 'storeCode' when calling storeCheckStatusJsonGet(Async)");
        }

        return storeCheckStatusJsonGetCall(partnerCode, authToken, storeCode, locale, _callback);

    }

    /**
     * Retrive store creation status.
     * 
     * @param partnerCode Partner code. (required)
     * @param authToken Partner authentication token. (required)
     * @param storeCode Store Code (required)
     * @param locale ISO 3166-2 code of the language used in the response messages. (optional, default to en)
     * @return StoreCheckStatusJsonGet200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Store status object if creation is still in progress. A new Partner Store object when creation is done. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. </td><td>  -  </td></tr>
     </table>
     */
    public StoreCheckStatusJsonGet200Response storeCheckStatusJsonGet(String partnerCode, String authToken, String storeCode, String locale) throws ApiException {
        ApiResponse<StoreCheckStatusJsonGet200Response> localVarResp = storeCheckStatusJsonGetWithHttpInfo(partnerCode, authToken, storeCode, locale);
        return localVarResp.getData();
    }

    /**
     * Retrive store creation status.
     * 
     * @param partnerCode Partner code. (required)
     * @param authToken Partner authentication token. (required)
     * @param storeCode Store Code (required)
     * @param locale ISO 3166-2 code of the language used in the response messages. (optional, default to en)
     * @return ApiResponse&lt;StoreCheckStatusJsonGet200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Store status object if creation is still in progress. A new Partner Store object when creation is done. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<StoreCheckStatusJsonGet200Response> storeCheckStatusJsonGetWithHttpInfo(String partnerCode, String authToken, String storeCode, String locale) throws ApiException {
        okhttp3.Call localVarCall = storeCheckStatusJsonGetValidateBeforeCall(partnerCode, authToken, storeCode, locale, null);
        Type localVarReturnType = new TypeToken<StoreCheckStatusJsonGet200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrive store creation status. (asynchronously)
     * 
     * @param partnerCode Partner code. (required)
     * @param authToken Partner authentication token. (required)
     * @param storeCode Store Code (required)
     * @param locale ISO 3166-2 code of the language used in the response messages. (optional, default to en)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Store status object if creation is still in progress. A new Partner Store object when creation is done. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call storeCheckStatusJsonGetAsync(String partnerCode, String authToken, String storeCode, String locale, final ApiCallback<StoreCheckStatusJsonGet200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = storeCheckStatusJsonGetValidateBeforeCall(partnerCode, authToken, storeCode, locale, _callback);
        Type localVarReturnType = new TypeToken<StoreCheckStatusJsonGet200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for storeCreateJsonPost
     * @param partnerCode Partner code. (required)
     * @param authToken Partner authentication token. (required)
     * @param partnerStoreCreate New partnered Store parameters. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Partner Store object. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call storeCreateJsonPostCall(String partnerCode, String authToken, PartnerStoreCreate partnerStoreCreate, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = partnerStoreCreate;

        // create path and map variables
        String localVarPath = "/store/create.json";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (partnerCode != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("partner_code", partnerCode));
        }

        if (authToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("auth_token", authToken));
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

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call storeCreateJsonPostValidateBeforeCall(String partnerCode, String authToken, PartnerStoreCreate partnerStoreCreate, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'partnerCode' is set
        if (partnerCode == null) {
            throw new ApiException("Missing the required parameter 'partnerCode' when calling storeCreateJsonPost(Async)");
        }

        // verify the required parameter 'authToken' is set
        if (authToken == null) {
            throw new ApiException("Missing the required parameter 'authToken' when calling storeCreateJsonPost(Async)");
        }

        // verify the required parameter 'partnerStoreCreate' is set
        if (partnerStoreCreate == null) {
            throw new ApiException("Missing the required parameter 'partnerStoreCreate' when calling storeCreateJsonPost(Async)");
        }

        return storeCreateJsonPostCall(partnerCode, authToken, partnerStoreCreate, _callback);

    }

    /**
     * Create a Partnered Store
     * 
     * @param partnerCode Partner code. (required)
     * @param authToken Partner authentication token. (required)
     * @param partnerStoreCreate New partnered Store parameters. (required)
     * @return PartnerStoreCode
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Partner Store object. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. </td><td>  -  </td></tr>
     </table>
     */
    public PartnerStoreCode storeCreateJsonPost(String partnerCode, String authToken, PartnerStoreCreate partnerStoreCreate) throws ApiException {
        ApiResponse<PartnerStoreCode> localVarResp = storeCreateJsonPostWithHttpInfo(partnerCode, authToken, partnerStoreCreate);
        return localVarResp.getData();
    }

    /**
     * Create a Partnered Store
     * 
     * @param partnerCode Partner code. (required)
     * @param authToken Partner authentication token. (required)
     * @param partnerStoreCreate New partnered Store parameters. (required)
     * @return ApiResponse&lt;PartnerStoreCode&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Partner Store object. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PartnerStoreCode> storeCreateJsonPostWithHttpInfo(String partnerCode, String authToken, PartnerStoreCreate partnerStoreCreate) throws ApiException {
        okhttp3.Call localVarCall = storeCreateJsonPostValidateBeforeCall(partnerCode, authToken, partnerStoreCreate, null);
        Type localVarReturnType = new TypeToken<PartnerStoreCode>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a Partnered Store (asynchronously)
     * 
     * @param partnerCode Partner code. (required)
     * @param authToken Partner authentication token. (required)
     * @param partnerStoreCreate New partnered Store parameters. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> A Partner Store object. </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call storeCreateJsonPostAsync(String partnerCode, String authToken, PartnerStoreCreate partnerStoreCreate, final ApiCallback<PartnerStoreCode> _callback) throws ApiException {

        okhttp3.Call localVarCall = storeCreateJsonPostValidateBeforeCall(partnerCode, authToken, partnerStoreCreate, _callback);
        Type localVarReturnType = new TypeToken<PartnerStoreCode>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
