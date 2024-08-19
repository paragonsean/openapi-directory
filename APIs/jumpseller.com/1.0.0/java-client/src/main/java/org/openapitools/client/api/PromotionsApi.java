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


import org.openapitools.client.model.NotFound;
import org.openapitools.client.model.Promotion;
import org.openapitools.client.model.PromotionEdit;

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
     * Build call for promotionsIdJsonDelete
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Promotion (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call promotionsIdJsonDeleteCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/promotions/{id}.json"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (login != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("login", login));
        }

        if (authtoken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("authtoken", authtoken));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call promotionsIdJsonDeleteValidateBeforeCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling promotionsIdJsonDelete(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling promotionsIdJsonDelete(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling promotionsIdJsonDelete(Async)");
        }

        return promotionsIdJsonDeleteCall(login, authtoken, id, _callback);

    }

    /**
     * Delete an existing Promotion.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Promotion (required)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public String promotionsIdJsonDelete(String login, String authtoken, Integer id) throws ApiException {
        ApiResponse<String> localVarResp = promotionsIdJsonDeleteWithHttpInfo(login, authtoken, id);
        return localVarResp.getData();
    }

    /**
     * Delete an existing Promotion.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Promotion (required)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> promotionsIdJsonDeleteWithHttpInfo(String login, String authtoken, Integer id) throws ApiException {
        okhttp3.Call localVarCall = promotionsIdJsonDeleteValidateBeforeCall(login, authtoken, id, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete an existing Promotion. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Promotion (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call promotionsIdJsonDeleteAsync(String login, String authtoken, Integer id, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = promotionsIdJsonDeleteValidateBeforeCall(login, authtoken, id, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for promotionsIdJsonGet
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Promotion (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call promotionsIdJsonGetCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/promotions/{id}.json"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (login != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("login", login));
        }

        if (authtoken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("authtoken", authtoken));
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
    private okhttp3.Call promotionsIdJsonGetValidateBeforeCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling promotionsIdJsonGet(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling promotionsIdJsonGet(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling promotionsIdJsonGet(Async)");
        }

        return promotionsIdJsonGetCall(login, authtoken, id, _callback);

    }

    /**
     * Retrieve a single Promotion.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Promotion (required)
     * @return Promotion
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public Promotion promotionsIdJsonGet(String login, String authtoken, Integer id) throws ApiException {
        ApiResponse<Promotion> localVarResp = promotionsIdJsonGetWithHttpInfo(login, authtoken, id);
        return localVarResp.getData();
    }

    /**
     * Retrieve a single Promotion.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Promotion (required)
     * @return ApiResponse&lt;Promotion&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Promotion> promotionsIdJsonGetWithHttpInfo(String login, String authtoken, Integer id) throws ApiException {
        okhttp3.Call localVarCall = promotionsIdJsonGetValidateBeforeCall(login, authtoken, id, null);
        Type localVarReturnType = new TypeToken<Promotion>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a single Promotion. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Promotion (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call promotionsIdJsonGetAsync(String login, String authtoken, Integer id, final ApiCallback<Promotion> _callback) throws ApiException {

        okhttp3.Call localVarCall = promotionsIdJsonGetValidateBeforeCall(login, authtoken, id, _callback);
        Type localVarReturnType = new TypeToken<Promotion>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for promotionsIdJsonPut
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Promotion (required)
     * @param promotionEdit Promotion parameters. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call promotionsIdJsonPutCall(String login, String authtoken, Integer id, PromotionEdit promotionEdit, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = promotionEdit;

        // create path and map variables
        String localVarPath = "/promotions/{id}.json"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (login != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("login", login));
        }

        if (authtoken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("authtoken", authtoken));
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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call promotionsIdJsonPutValidateBeforeCall(String login, String authtoken, Integer id, PromotionEdit promotionEdit, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling promotionsIdJsonPut(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling promotionsIdJsonPut(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling promotionsIdJsonPut(Async)");
        }

        // verify the required parameter 'promotionEdit' is set
        if (promotionEdit == null) {
            throw new ApiException("Missing the required parameter 'promotionEdit' when calling promotionsIdJsonPut(Async)");
        }

        return promotionsIdJsonPutCall(login, authtoken, id, promotionEdit, _callback);

    }

    /**
     * Update a Promotion.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Promotion (required)
     * @param promotionEdit Promotion parameters. (required)
     * @return Promotion
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public Promotion promotionsIdJsonPut(String login, String authtoken, Integer id, PromotionEdit promotionEdit) throws ApiException {
        ApiResponse<Promotion> localVarResp = promotionsIdJsonPutWithHttpInfo(login, authtoken, id, promotionEdit);
        return localVarResp.getData();
    }

    /**
     * Update a Promotion.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Promotion (required)
     * @param promotionEdit Promotion parameters. (required)
     * @return ApiResponse&lt;Promotion&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Promotion> promotionsIdJsonPutWithHttpInfo(String login, String authtoken, Integer id, PromotionEdit promotionEdit) throws ApiException {
        okhttp3.Call localVarCall = promotionsIdJsonPutValidateBeforeCall(login, authtoken, id, promotionEdit, null);
        Type localVarReturnType = new TypeToken<Promotion>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update a Promotion. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Promotion (required)
     * @param promotionEdit Promotion parameters. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call promotionsIdJsonPutAsync(String login, String authtoken, Integer id, PromotionEdit promotionEdit, final ApiCallback<Promotion> _callback) throws ApiException {

        okhttp3.Call localVarCall = promotionsIdJsonPutValidateBeforeCall(login, authtoken, id, promotionEdit, _callback);
        Type localVarReturnType = new TypeToken<Promotion>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for promotionsJsonGet
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param limit Promotions&#39; list restriction (default: 50 | max: 200). (optional)
     * @param page Promotions&#39; list page (default: 1). (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array of Promotions </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call promotionsJsonGetCall(String login, String authtoken, Integer limit, Integer page, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/promotions.json";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (login != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("login", login));
        }

        if (authtoken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("authtoken", authtoken));
        }

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
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
    private okhttp3.Call promotionsJsonGetValidateBeforeCall(String login, String authtoken, Integer limit, Integer page, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling promotionsJsonGet(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling promotionsJsonGet(Async)");
        }

        return promotionsJsonGetCall(login, authtoken, limit, page, _callback);

    }

    /**
     * Retrieve all Promotions.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param limit Promotions&#39; list restriction (default: 50 | max: 200). (optional)
     * @param page Promotions&#39; list page (default: 1). (optional)
     * @return List&lt;Promotion&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array of Promotions </td><td>  -  </td></tr>
     </table>
     */
    public List<Promotion> promotionsJsonGet(String login, String authtoken, Integer limit, Integer page) throws ApiException {
        ApiResponse<List<Promotion>> localVarResp = promotionsJsonGetWithHttpInfo(login, authtoken, limit, page);
        return localVarResp.getData();
    }

    /**
     * Retrieve all Promotions.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param limit Promotions&#39; list restriction (default: 50 | max: 200). (optional)
     * @param page Promotions&#39; list page (default: 1). (optional)
     * @return ApiResponse&lt;List&lt;Promotion&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array of Promotions </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Promotion>> promotionsJsonGetWithHttpInfo(String login, String authtoken, Integer limit, Integer page) throws ApiException {
        okhttp3.Call localVarCall = promotionsJsonGetValidateBeforeCall(login, authtoken, limit, page, null);
        Type localVarReturnType = new TypeToken<List<Promotion>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve all Promotions. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param limit Promotions&#39; list restriction (default: 50 | max: 200). (optional)
     * @param page Promotions&#39; list page (default: 1). (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array of Promotions </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call promotionsJsonGetAsync(String login, String authtoken, Integer limit, Integer page, final ApiCallback<List<Promotion>> _callback) throws ApiException {

        okhttp3.Call localVarCall = promotionsJsonGetValidateBeforeCall(login, authtoken, limit, page, _callback);
        Type localVarReturnType = new TypeToken<List<Promotion>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for promotionsJsonPost
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param promotionEdit Promotion parameters. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call promotionsJsonPostCall(String login, String authtoken, PromotionEdit promotionEdit, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = promotionEdit;

        // create path and map variables
        String localVarPath = "/promotions.json";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (login != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("login", login));
        }

        if (authtoken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("authtoken", authtoken));
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
    private okhttp3.Call promotionsJsonPostValidateBeforeCall(String login, String authtoken, PromotionEdit promotionEdit, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling promotionsJsonPost(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling promotionsJsonPost(Async)");
        }

        // verify the required parameter 'promotionEdit' is set
        if (promotionEdit == null) {
            throw new ApiException("Missing the required parameter 'promotionEdit' when calling promotionsJsonPost(Async)");
        }

        return promotionsJsonPostCall(login, authtoken, promotionEdit, _callback);

    }

    /**
     * Create a new Promotion.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param promotionEdit Promotion parameters. (required)
     * @return Promotion
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public Promotion promotionsJsonPost(String login, String authtoken, PromotionEdit promotionEdit) throws ApiException {
        ApiResponse<Promotion> localVarResp = promotionsJsonPostWithHttpInfo(login, authtoken, promotionEdit);
        return localVarResp.getData();
    }

    /**
     * Create a new Promotion.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param promotionEdit Promotion parameters. (required)
     * @return ApiResponse&lt;Promotion&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Promotion> promotionsJsonPostWithHttpInfo(String login, String authtoken, PromotionEdit promotionEdit) throws ApiException {
        okhttp3.Call localVarCall = promotionsJsonPostValidateBeforeCall(login, authtoken, promotionEdit, null);
        Type localVarReturnType = new TypeToken<Promotion>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a new Promotion. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param promotionEdit Promotion parameters. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Promotion Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call promotionsJsonPostAsync(String login, String authtoken, PromotionEdit promotionEdit, final ApiCallback<Promotion> _callback) throws ApiException {

        okhttp3.Call localVarCall = promotionsJsonPostValidateBeforeCall(login, authtoken, promotionEdit, _callback);
        Type localVarReturnType = new TypeToken<Promotion>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
