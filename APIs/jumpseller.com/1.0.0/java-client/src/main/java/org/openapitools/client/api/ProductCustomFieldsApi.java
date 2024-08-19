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


import org.openapitools.client.model.AddProductCustomField;
import org.openapitools.client.model.Count;
import org.openapitools.client.model.MessageObject;
import org.openapitools.client.model.NotFound;
import org.openapitools.client.model.Product;
import org.openapitools.client.model.ProductCustomField;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProductCustomFieldsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public ProductCustomFieldsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public ProductCustomFieldsApi(ApiClient apiClient) {
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
     * Build call for productsIdFieldsCountJsonGet
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id ID of the Product (required)
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
    public okhttp3.Call productsIdFieldsCountJsonGetCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/products/{id}/fields/count.json"
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
    private okhttp3.Call productsIdFieldsCountJsonGetValidateBeforeCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling productsIdFieldsCountJsonGet(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling productsIdFieldsCountJsonGet(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling productsIdFieldsCountJsonGet(Async)");
        }

        return productsIdFieldsCountJsonGetCall(login, authtoken, id, _callback);

    }

    /**
     * Count all Product Custom Fields.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id ID of the Product (required)
     * @return Count
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public Count productsIdFieldsCountJsonGet(String login, String authtoken, Integer id) throws ApiException {
        ApiResponse<Count> localVarResp = productsIdFieldsCountJsonGetWithHttpInfo(login, authtoken, id);
        return localVarResp.getData();
    }

    /**
     * Count all Product Custom Fields.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id ID of the Product (required)
     * @return ApiResponse&lt;Count&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Count> productsIdFieldsCountJsonGetWithHttpInfo(String login, String authtoken, Integer id) throws ApiException {
        okhttp3.Call localVarCall = productsIdFieldsCountJsonGetValidateBeforeCall(login, authtoken, id, null);
        Type localVarReturnType = new TypeToken<Count>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Count all Product Custom Fields. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id ID of the Product (required)
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
    public okhttp3.Call productsIdFieldsCountJsonGetAsync(String login, String authtoken, Integer id, final ApiCallback<Count> _callback) throws ApiException {

        okhttp3.Call localVarCall = productsIdFieldsCountJsonGetValidateBeforeCall(login, authtoken, id, _callback);
        Type localVarReturnType = new TypeToken<Count>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for productsIdFieldsJsonGet
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
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
    public okhttp3.Call productsIdFieldsJsonGetCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/products/{id}/fields.json"
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
    private okhttp3.Call productsIdFieldsJsonGetValidateBeforeCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling productsIdFieldsJsonGet(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling productsIdFieldsJsonGet(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling productsIdFieldsJsonGet(Async)");
        }

        return productsIdFieldsJsonGetCall(login, authtoken, id, _callback);

    }

    /**
     * Retrieve all Product Custom Fields
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @return List&lt;ProductCustomField&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public List<ProductCustomField> productsIdFieldsJsonGet(String login, String authtoken, Integer id) throws ApiException {
        ApiResponse<List<ProductCustomField>> localVarResp = productsIdFieldsJsonGetWithHttpInfo(login, authtoken, id);
        return localVarResp.getData();
    }

    /**
     * Retrieve all Product Custom Fields
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @return ApiResponse&lt;List&lt;ProductCustomField&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<ProductCustomField>> productsIdFieldsJsonGetWithHttpInfo(String login, String authtoken, Integer id) throws ApiException {
        okhttp3.Call localVarCall = productsIdFieldsJsonGetValidateBeforeCall(login, authtoken, id, null);
        Type localVarReturnType = new TypeToken<List<ProductCustomField>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve all Product Custom Fields (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
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
    public okhttp3.Call productsIdFieldsJsonGetAsync(String login, String authtoken, Integer id, final ApiCallback<List<ProductCustomField>> _callback) throws ApiException {

        okhttp3.Call localVarCall = productsIdFieldsJsonGetValidateBeforeCall(login, authtoken, id, _callback);
        Type localVarReturnType = new TypeToken<List<ProductCustomField>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for productsIdFieldsJsonPost
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param addProductCustomField Product Custom Field parameters. (required)
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
    public okhttp3.Call productsIdFieldsJsonPostCall(String login, String authtoken, Integer id, AddProductCustomField addProductCustomField, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = addProductCustomField;

        // create path and map variables
        String localVarPath = "/products/{id}/fields.json"
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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call productsIdFieldsJsonPostValidateBeforeCall(String login, String authtoken, Integer id, AddProductCustomField addProductCustomField, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling productsIdFieldsJsonPost(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling productsIdFieldsJsonPost(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling productsIdFieldsJsonPost(Async)");
        }

        // verify the required parameter 'addProductCustomField' is set
        if (addProductCustomField == null) {
            throw new ApiException("Missing the required parameter 'addProductCustomField' when calling productsIdFieldsJsonPost(Async)");
        }

        return productsIdFieldsJsonPostCall(login, authtoken, id, addProductCustomField, _callback);

    }

    /**
     * Add an existing Custom Field to a Product.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param addProductCustomField Product Custom Field parameters. (required)
     * @return Product
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public Product productsIdFieldsJsonPost(String login, String authtoken, Integer id, AddProductCustomField addProductCustomField) throws ApiException {
        ApiResponse<Product> localVarResp = productsIdFieldsJsonPostWithHttpInfo(login, authtoken, id, addProductCustomField);
        return localVarResp.getData();
    }

    /**
     * Add an existing Custom Field to a Product.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param addProductCustomField Product Custom Field parameters. (required)
     * @return ApiResponse&lt;Product&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Product> productsIdFieldsJsonPostWithHttpInfo(String login, String authtoken, Integer id, AddProductCustomField addProductCustomField) throws ApiException {
        okhttp3.Call localVarCall = productsIdFieldsJsonPostValidateBeforeCall(login, authtoken, id, addProductCustomField, null);
        Type localVarReturnType = new TypeToken<Product>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Add an existing Custom Field to a Product. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Product (required)
     * @param addProductCustomField Product Custom Field parameters. (required)
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
    public okhttp3.Call productsIdFieldsJsonPostAsync(String login, String authtoken, Integer id, AddProductCustomField addProductCustomField, final ApiCallback<Product> _callback) throws ApiException {

        okhttp3.Call localVarCall = productsIdFieldsJsonPostValidateBeforeCall(login, authtoken, id, addProductCustomField, _callback);
        Type localVarReturnType = new TypeToken<Product>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for productsProductIdFieldsFieldIdJsonDelete
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param productId Id of the Product. (required)
     * @param fieldId Id of the Custom Field Value. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product or Custom Field Value Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsProductIdFieldsFieldIdJsonDeleteCall(String login, String authtoken, Integer productId, Integer fieldId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/products/{product_id}/fields/{field_id}.json"
            .replace("{" + "product_id" + "}", localVarApiClient.escapeString(productId.toString()))
            .replace("{" + "field_id" + "}", localVarApiClient.escapeString(fieldId.toString()));

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
    private okhttp3.Call productsProductIdFieldsFieldIdJsonDeleteValidateBeforeCall(String login, String authtoken, Integer productId, Integer fieldId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling productsProductIdFieldsFieldIdJsonDelete(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling productsProductIdFieldsFieldIdJsonDelete(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling productsProductIdFieldsFieldIdJsonDelete(Async)");
        }

        // verify the required parameter 'fieldId' is set
        if (fieldId == null) {
            throw new ApiException("Missing the required parameter 'fieldId' when calling productsProductIdFieldsFieldIdJsonDelete(Async)");
        }

        return productsProductIdFieldsFieldIdJsonDeleteCall(login, authtoken, productId, fieldId, _callback);

    }

    /**
     * Delete value of Product Custom Field
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param productId Id of the Product. (required)
     * @param fieldId Id of the Custom Field Value. (required)
     * @return MessageObject
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product or Custom Field Value Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public MessageObject productsProductIdFieldsFieldIdJsonDelete(String login, String authtoken, Integer productId, Integer fieldId) throws ApiException {
        ApiResponse<MessageObject> localVarResp = productsProductIdFieldsFieldIdJsonDeleteWithHttpInfo(login, authtoken, productId, fieldId);
        return localVarResp.getData();
    }

    /**
     * Delete value of Product Custom Field
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param productId Id of the Product. (required)
     * @param fieldId Id of the Custom Field Value. (required)
     * @return ApiResponse&lt;MessageObject&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product or Custom Field Value Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<MessageObject> productsProductIdFieldsFieldIdJsonDeleteWithHttpInfo(String login, String authtoken, Integer productId, Integer fieldId) throws ApiException {
        okhttp3.Call localVarCall = productsProductIdFieldsFieldIdJsonDeleteValidateBeforeCall(login, authtoken, productId, fieldId, null);
        Type localVarReturnType = new TypeToken<MessageObject>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete value of Product Custom Field (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param productId Id of the Product. (required)
     * @param fieldId Id of the Custom Field Value. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product or Custom Field Value Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsProductIdFieldsFieldIdJsonDeleteAsync(String login, String authtoken, Integer productId, Integer fieldId, final ApiCallback<MessageObject> _callback) throws ApiException {

        okhttp3.Call localVarCall = productsProductIdFieldsFieldIdJsonDeleteValidateBeforeCall(login, authtoken, productId, fieldId, _callback);
        Type localVarReturnType = new TypeToken<MessageObject>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for productsProductIdFieldsFieldIdJsonPut
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param productId Id of the Product. (required)
     * @param fieldId Id of the Custom Field Value. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product or Custom Field Value Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsProductIdFieldsFieldIdJsonPutCall(String login, String authtoken, Integer productId, Integer fieldId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/products/{product_id}/fields/{field_id}.json"
            .replace("{" + "product_id" + "}", localVarApiClient.escapeString(productId.toString()))
            .replace("{" + "field_id" + "}", localVarApiClient.escapeString(fieldId.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call productsProductIdFieldsFieldIdJsonPutValidateBeforeCall(String login, String authtoken, Integer productId, Integer fieldId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling productsProductIdFieldsFieldIdJsonPut(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling productsProductIdFieldsFieldIdJsonPut(Async)");
        }

        // verify the required parameter 'productId' is set
        if (productId == null) {
            throw new ApiException("Missing the required parameter 'productId' when calling productsProductIdFieldsFieldIdJsonPut(Async)");
        }

        // verify the required parameter 'fieldId' is set
        if (fieldId == null) {
            throw new ApiException("Missing the required parameter 'fieldId' when calling productsProductIdFieldsFieldIdJsonPut(Async)");
        }

        return productsProductIdFieldsFieldIdJsonPutCall(login, authtoken, productId, fieldId, _callback);

    }

    /**
     * Update value of Product Custom Field
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param productId Id of the Product. (required)
     * @param fieldId Id of the Custom Field Value. (required)
     * @return ProductCustomField
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product or Custom Field Value Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ProductCustomField productsProductIdFieldsFieldIdJsonPut(String login, String authtoken, Integer productId, Integer fieldId) throws ApiException {
        ApiResponse<ProductCustomField> localVarResp = productsProductIdFieldsFieldIdJsonPutWithHttpInfo(login, authtoken, productId, fieldId);
        return localVarResp.getData();
    }

    /**
     * Update value of Product Custom Field
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param productId Id of the Product. (required)
     * @param fieldId Id of the Custom Field Value. (required)
     * @return ApiResponse&lt;ProductCustomField&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product or Custom Field Value Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ProductCustomField> productsProductIdFieldsFieldIdJsonPutWithHttpInfo(String login, String authtoken, Integer productId, Integer fieldId) throws ApiException {
        okhttp3.Call localVarCall = productsProductIdFieldsFieldIdJsonPutValidateBeforeCall(login, authtoken, productId, fieldId, null);
        Type localVarReturnType = new TypeToken<ProductCustomField>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update value of Product Custom Field (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param productId Id of the Product. (required)
     * @param fieldId Id of the Custom Field Value. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Product or Custom Field Value Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call productsProductIdFieldsFieldIdJsonPutAsync(String login, String authtoken, Integer productId, Integer fieldId, final ApiCallback<ProductCustomField> _callback) throws ApiException {

        okhttp3.Call localVarCall = productsProductIdFieldsFieldIdJsonPutValidateBeforeCall(login, authtoken, productId, fieldId, _callback);
        Type localVarReturnType = new TypeToken<ProductCustomField>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
