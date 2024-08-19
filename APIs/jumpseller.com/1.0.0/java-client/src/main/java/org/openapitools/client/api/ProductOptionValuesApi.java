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


import org.openapitools.client.model.Count;
import org.openapitools.client.model.NotFound;
import org.openapitools.client.model.ProductOptionValue;
import org.openapitools.client.model.ProductOptionValueEdit;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProductOptionValuesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProductOptionValuesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProductOptionValuesApi(ApiClient apiClient) {
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
     * Build call for productsIdOptionsOptionIdValuesCountJsonGet
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id ID of the Product (required)
     * @param optionId ID of the Product Option (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsIdOptionsOptionIdValuesCountJsonGetCall(String login, String authtoken, Integer id, Integer optionId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/products/{id}/options/{option_id}/values/count.json"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "option_id" + "}", localVarApiClient.escapeString(optionId.toString()));

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
    private okhttp3.Call productsIdOptionsOptionIdValuesCountJsonGetValidateBeforeCall(String login, String authtoken, Integer id, Integer optionId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling productsIdOptionsOptionIdValuesCountJsonGet(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling productsIdOptionsOptionIdValuesCountJsonGet(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling productsIdOptionsOptionIdValuesCountJsonGet(Async)");
        }

        // verify the required parameter 'optionId' is set
        if (optionId == null) {
            throw new ApiException("Missing the required parameter 'optionId' when calling productsIdOptionsOptionIdValuesCountJsonGet(Async)");
        }

        return productsIdOptionsOptionIdValuesCountJsonGetCall(login, authtoken, id, optionId, _callback);

    }

    /**
     * Count all Product Option Values.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id ID of the Product (required)
     * @param optionId ID of the Product Option (required)
     * @return Count
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public Count productsIdOptionsOptionIdValuesCountJsonGet(String login, String authtoken, Integer id, Integer optionId) throws ApiException {
        ApiResponse<Count> localVarResp = productsIdOptionsOptionIdValuesCountJsonGetWithHttpInfo(login, authtoken, id, optionId);
        return localVarResp.getData();
    }

    /**
     * Count all Product Option Values.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id ID of the Product (required)
     * @param optionId ID of the Product Option (required)
     * @return ApiResponse&lt;Count&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Count> productsIdOptionsOptionIdValuesCountJsonGetWithHttpInfo(String login, String authtoken, Integer id, Integer optionId) throws ApiException {
        okhttp3.Call localVarCall = productsIdOptionsOptionIdValuesCountJsonGetValidateBeforeCall(login, authtoken, id, optionId, null);
        Type localVarReturnType = new TypeToken<Count>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Count all Product Option Values. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id ID of the Product (required)
     * @param optionId ID of the Product Option (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsIdOptionsOptionIdValuesCountJsonGetAsync(String login, String authtoken, Integer id, Integer optionId, final ApiCallback<Count> _callback) throws ApiException {

        okhttp3.Call localVarCall = productsIdOptionsOptionIdValuesCountJsonGetValidateBeforeCall(login, authtoken, id, optionId, _callback);
        Type localVarReturnType = new TypeToken<Count>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for productsIdOptionsOptionIdValuesJsonGet
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id ID of the Product (required)
     * @param optionId ID of the Product Option (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsIdOptionsOptionIdValuesJsonGetCall(String login, String authtoken, Integer id, Integer optionId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/products/{id}/options/{option_id}/values.json"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "option_id" + "}", localVarApiClient.escapeString(optionId.toString()));

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
    private okhttp3.Call productsIdOptionsOptionIdValuesJsonGetValidateBeforeCall(String login, String authtoken, Integer id, Integer optionId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling productsIdOptionsOptionIdValuesJsonGet(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling productsIdOptionsOptionIdValuesJsonGet(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling productsIdOptionsOptionIdValuesJsonGet(Async)");
        }

        // verify the required parameter 'optionId' is set
        if (optionId == null) {
            throw new ApiException("Missing the required parameter 'optionId' when calling productsIdOptionsOptionIdValuesJsonGet(Async)");
        }

        return productsIdOptionsOptionIdValuesJsonGetCall(login, authtoken, id, optionId, _callback);

    }

    /**
     * Retrieve all Product Option Values.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id ID of the Product (required)
     * @param optionId ID of the Product Option (required)
     * @return List&lt;ProductOptionValue&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public List<ProductOptionValue> productsIdOptionsOptionIdValuesJsonGet(String login, String authtoken, Integer id, Integer optionId) throws ApiException {
        ApiResponse<List<ProductOptionValue>> localVarResp = productsIdOptionsOptionIdValuesJsonGetWithHttpInfo(login, authtoken, id, optionId);
        return localVarResp.getData();
    }

    /**
     * Retrieve all Product Option Values.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id ID of the Product (required)
     * @param optionId ID of the Product Option (required)
     * @return ApiResponse&lt;List&lt;ProductOptionValue&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ProductOptionValue>> productsIdOptionsOptionIdValuesJsonGetWithHttpInfo(String login, String authtoken, Integer id, Integer optionId) throws ApiException {
        okhttp3.Call localVarCall = productsIdOptionsOptionIdValuesJsonGetValidateBeforeCall(login, authtoken, id, optionId, null);
        Type localVarReturnType = new TypeToken<List<ProductOptionValue>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve all Product Option Values. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id ID of the Product (required)
     * @param optionId ID of the Product Option (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsIdOptionsOptionIdValuesJsonGetAsync(String login, String authtoken, Integer id, Integer optionId, final ApiCallback<List<ProductOptionValue>> _callback) throws ApiException {

        okhttp3.Call localVarCall = productsIdOptionsOptionIdValuesJsonGetValidateBeforeCall(login, authtoken, id, optionId, _callback);
        Type localVarReturnType = new TypeToken<List<ProductOptionValue>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for productsIdOptionsOptionIdValuesJsonPost
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param productOptionValueEdit Product Option Value parameters. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsIdOptionsOptionIdValuesJsonPostCall(String login, String authtoken, Integer id, Integer optionId, ProductOptionValueEdit productOptionValueEdit, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = productOptionValueEdit;

        // create path and map variables
        String localVarPath = "/products/{id}/options/{option_id}/values.json"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "option_id" + "}", localVarApiClient.escapeString(optionId.toString()));

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
    private okhttp3.Call productsIdOptionsOptionIdValuesJsonPostValidateBeforeCall(String login, String authtoken, Integer id, Integer optionId, ProductOptionValueEdit productOptionValueEdit, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling productsIdOptionsOptionIdValuesJsonPost(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling productsIdOptionsOptionIdValuesJsonPost(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling productsIdOptionsOptionIdValuesJsonPost(Async)");
        }

        // verify the required parameter 'optionId' is set
        if (optionId == null) {
            throw new ApiException("Missing the required parameter 'optionId' when calling productsIdOptionsOptionIdValuesJsonPost(Async)");
        }

        // verify the required parameter 'productOptionValueEdit' is set
        if (productOptionValueEdit == null) {
            throw new ApiException("Missing the required parameter 'productOptionValueEdit' when calling productsIdOptionsOptionIdValuesJsonPost(Async)");
        }

        return productsIdOptionsOptionIdValuesJsonPostCall(login, authtoken, id, optionId, productOptionValueEdit, _callback);

    }

    /**
     * Create a new Product Option Value.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param productOptionValueEdit Product Option Value parameters. (required)
     * @return ProductOptionValue
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ProductOptionValue productsIdOptionsOptionIdValuesJsonPost(String login, String authtoken, Integer id, Integer optionId, ProductOptionValueEdit productOptionValueEdit) throws ApiException {
        ApiResponse<ProductOptionValue> localVarResp = productsIdOptionsOptionIdValuesJsonPostWithHttpInfo(login, authtoken, id, optionId, productOptionValueEdit);
        return localVarResp.getData();
    }

    /**
     * Create a new Product Option Value.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param productOptionValueEdit Product Option Value parameters. (required)
     * @return ApiResponse&lt;ProductOptionValue&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProductOptionValue> productsIdOptionsOptionIdValuesJsonPostWithHttpInfo(String login, String authtoken, Integer id, Integer optionId, ProductOptionValueEdit productOptionValueEdit) throws ApiException {
        okhttp3.Call localVarCall = productsIdOptionsOptionIdValuesJsonPostValidateBeforeCall(login, authtoken, id, optionId, productOptionValueEdit, null);
        Type localVarReturnType = new TypeToken<ProductOptionValue>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a new Product Option Value. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param productOptionValueEdit Product Option Value parameters. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsIdOptionsOptionIdValuesJsonPostAsync(String login, String authtoken, Integer id, Integer optionId, ProductOptionValueEdit productOptionValueEdit, final ApiCallback<ProductOptionValue> _callback) throws ApiException {

        okhttp3.Call localVarCall = productsIdOptionsOptionIdValuesJsonPostValidateBeforeCall(login, authtoken, id, optionId, productOptionValueEdit, _callback);
        Type localVarReturnType = new TypeToken<ProductOptionValue>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for productsIdOptionsOptionIdValuesValueIdJsonDelete
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param valueId ID of the Product Option Value (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsIdOptionsOptionIdValuesValueIdJsonDeleteCall(String login, String authtoken, Integer id, Integer optionId, Integer valueId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/products/{id}/options/{option_id}/values/{value_id}.json"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "option_id" + "}", localVarApiClient.escapeString(optionId.toString()))
            .replace("{" + "value_id" + "}", localVarApiClient.escapeString(valueId.toString()));

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
    private okhttp3.Call productsIdOptionsOptionIdValuesValueIdJsonDeleteValidateBeforeCall(String login, String authtoken, Integer id, Integer optionId, Integer valueId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling productsIdOptionsOptionIdValuesValueIdJsonDelete(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling productsIdOptionsOptionIdValuesValueIdJsonDelete(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling productsIdOptionsOptionIdValuesValueIdJsonDelete(Async)");
        }

        // verify the required parameter 'optionId' is set
        if (optionId == null) {
            throw new ApiException("Missing the required parameter 'optionId' when calling productsIdOptionsOptionIdValuesValueIdJsonDelete(Async)");
        }

        // verify the required parameter 'valueId' is set
        if (valueId == null) {
            throw new ApiException("Missing the required parameter 'valueId' when calling productsIdOptionsOptionIdValuesValueIdJsonDelete(Async)");
        }

        return productsIdOptionsOptionIdValuesValueIdJsonDeleteCall(login, authtoken, id, optionId, valueId, _callback);

    }

    /**
     * Delete a Product Option Value.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param valueId ID of the Product Option Value (required)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public String productsIdOptionsOptionIdValuesValueIdJsonDelete(String login, String authtoken, Integer id, Integer optionId, Integer valueId) throws ApiException {
        ApiResponse<String> localVarResp = productsIdOptionsOptionIdValuesValueIdJsonDeleteWithHttpInfo(login, authtoken, id, optionId, valueId);
        return localVarResp.getData();
    }

    /**
     * Delete a Product Option Value.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param valueId ID of the Product Option Value (required)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> productsIdOptionsOptionIdValuesValueIdJsonDeleteWithHttpInfo(String login, String authtoken, Integer id, Integer optionId, Integer valueId) throws ApiException {
        okhttp3.Call localVarCall = productsIdOptionsOptionIdValuesValueIdJsonDeleteValidateBeforeCall(login, authtoken, id, optionId, valueId, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete a Product Option Value. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param valueId ID of the Product Option Value (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsIdOptionsOptionIdValuesValueIdJsonDeleteAsync(String login, String authtoken, Integer id, Integer optionId, Integer valueId, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = productsIdOptionsOptionIdValuesValueIdJsonDeleteValidateBeforeCall(login, authtoken, id, optionId, valueId, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for productsIdOptionsOptionIdValuesValueIdJsonGet
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param valueId ID of the Product Option Value (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsIdOptionsOptionIdValuesValueIdJsonGetCall(String login, String authtoken, Integer id, Integer optionId, Integer valueId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/products/{id}/options/{option_id}/values/{value_id}.json"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "option_id" + "}", localVarApiClient.escapeString(optionId.toString()))
            .replace("{" + "value_id" + "}", localVarApiClient.escapeString(valueId.toString()));

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
    private okhttp3.Call productsIdOptionsOptionIdValuesValueIdJsonGetValidateBeforeCall(String login, String authtoken, Integer id, Integer optionId, Integer valueId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling productsIdOptionsOptionIdValuesValueIdJsonGet(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling productsIdOptionsOptionIdValuesValueIdJsonGet(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling productsIdOptionsOptionIdValuesValueIdJsonGet(Async)");
        }

        // verify the required parameter 'optionId' is set
        if (optionId == null) {
            throw new ApiException("Missing the required parameter 'optionId' when calling productsIdOptionsOptionIdValuesValueIdJsonGet(Async)");
        }

        // verify the required parameter 'valueId' is set
        if (valueId == null) {
            throw new ApiException("Missing the required parameter 'valueId' when calling productsIdOptionsOptionIdValuesValueIdJsonGet(Async)");
        }

        return productsIdOptionsOptionIdValuesValueIdJsonGetCall(login, authtoken, id, optionId, valueId, _callback);

    }

    /**
     * Retrieve a single Product Option Value.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param valueId ID of the Product Option Value (required)
     * @return ProductOptionValue
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ProductOptionValue productsIdOptionsOptionIdValuesValueIdJsonGet(String login, String authtoken, Integer id, Integer optionId, Integer valueId) throws ApiException {
        ApiResponse<ProductOptionValue> localVarResp = productsIdOptionsOptionIdValuesValueIdJsonGetWithHttpInfo(login, authtoken, id, optionId, valueId);
        return localVarResp.getData();
    }

    /**
     * Retrieve a single Product Option Value.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param valueId ID of the Product Option Value (required)
     * @return ApiResponse&lt;ProductOptionValue&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProductOptionValue> productsIdOptionsOptionIdValuesValueIdJsonGetWithHttpInfo(String login, String authtoken, Integer id, Integer optionId, Integer valueId) throws ApiException {
        okhttp3.Call localVarCall = productsIdOptionsOptionIdValuesValueIdJsonGetValidateBeforeCall(login, authtoken, id, optionId, valueId, null);
        Type localVarReturnType = new TypeToken<ProductOptionValue>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a single Product Option Value. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param valueId ID of the Product Option Value (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsIdOptionsOptionIdValuesValueIdJsonGetAsync(String login, String authtoken, Integer id, Integer optionId, Integer valueId, final ApiCallback<ProductOptionValue> _callback) throws ApiException {

        okhttp3.Call localVarCall = productsIdOptionsOptionIdValuesValueIdJsonGetValidateBeforeCall(login, authtoken, id, optionId, valueId, _callback);
        Type localVarReturnType = new TypeToken<ProductOptionValue>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for productsIdOptionsOptionIdValuesValueIdJsonPut
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param valueId Id of the Product Option Value (required)
     * @param productOptionValueEdit Product option value parameters to change (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsIdOptionsOptionIdValuesValueIdJsonPutCall(String login, String authtoken, Integer id, Integer optionId, Integer valueId, ProductOptionValueEdit productOptionValueEdit, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = productOptionValueEdit;

        // create path and map variables
        String localVarPath = "/products/{id}/options/{option_id}/values/{value_id}.json"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
            .replace("{" + "option_id" + "}", localVarApiClient.escapeString(optionId.toString()))
            .replace("{" + "value_id" + "}", localVarApiClient.escapeString(valueId.toString()));

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
    private okhttp3.Call productsIdOptionsOptionIdValuesValueIdJsonPutValidateBeforeCall(String login, String authtoken, Integer id, Integer optionId, Integer valueId, ProductOptionValueEdit productOptionValueEdit, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling productsIdOptionsOptionIdValuesValueIdJsonPut(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling productsIdOptionsOptionIdValuesValueIdJsonPut(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling productsIdOptionsOptionIdValuesValueIdJsonPut(Async)");
        }

        // verify the required parameter 'optionId' is set
        if (optionId == null) {
            throw new ApiException("Missing the required parameter 'optionId' when calling productsIdOptionsOptionIdValuesValueIdJsonPut(Async)");
        }

        // verify the required parameter 'valueId' is set
        if (valueId == null) {
            throw new ApiException("Missing the required parameter 'valueId' when calling productsIdOptionsOptionIdValuesValueIdJsonPut(Async)");
        }

        // verify the required parameter 'productOptionValueEdit' is set
        if (productOptionValueEdit == null) {
            throw new ApiException("Missing the required parameter 'productOptionValueEdit' when calling productsIdOptionsOptionIdValuesValueIdJsonPut(Async)");
        }

        return productsIdOptionsOptionIdValuesValueIdJsonPutCall(login, authtoken, id, optionId, valueId, productOptionValueEdit, _callback);

    }

    /**
     * Modify an existing Product Option Value.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param valueId Id of the Product Option Value (required)
     * @param productOptionValueEdit Product option value parameters to change (required)
     * @return ProductOptionValue
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ProductOptionValue productsIdOptionsOptionIdValuesValueIdJsonPut(String login, String authtoken, Integer id, Integer optionId, Integer valueId, ProductOptionValueEdit productOptionValueEdit) throws ApiException {
        ApiResponse<ProductOptionValue> localVarResp = productsIdOptionsOptionIdValuesValueIdJsonPutWithHttpInfo(login, authtoken, id, optionId, valueId, productOptionValueEdit);
        return localVarResp.getData();
    }

    /**
     * Modify an existing Product Option Value.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param valueId Id of the Product Option Value (required)
     * @param productOptionValueEdit Product option value parameters to change (required)
     * @return ApiResponse&lt;ProductOptionValue&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProductOptionValue> productsIdOptionsOptionIdValuesValueIdJsonPutWithHttpInfo(String login, String authtoken, Integer id, Integer optionId, Integer valueId, ProductOptionValueEdit productOptionValueEdit) throws ApiException {
        okhttp3.Call localVarCall = productsIdOptionsOptionIdValuesValueIdJsonPutValidateBeforeCall(login, authtoken, id, optionId, valueId, productOptionValueEdit, null);
        Type localVarReturnType = new TypeToken<ProductOptionValue>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Modify an existing Product Option Value. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param optionId Id of the Product Option (required)
     * @param valueId Id of the Product Option Value (required)
     * @param productOptionValueEdit Product option value parameters to change (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsIdOptionsOptionIdValuesValueIdJsonPutAsync(String login, String authtoken, Integer id, Integer optionId, Integer valueId, ProductOptionValueEdit productOptionValueEdit, final ApiCallback<ProductOptionValue> _callback) throws ApiException {

        okhttp3.Call localVarCall = productsIdOptionsOptionIdValuesValueIdJsonPutValidateBeforeCall(login, authtoken, id, optionId, valueId, productOptionValueEdit, _callback);
        Type localVarReturnType = new TypeToken<ProductOptionValue>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
