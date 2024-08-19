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
import org.openapitools.client.model.Customer;
import org.openapitools.client.model.CustomerWithPasswordNoID;
import org.openapitools.client.model.NotFound;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CustomersApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CustomersApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CustomersApi(ApiClient apiClient) {
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
     * Build call for customersCountJsonGet
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersCountJsonGetCall(String login, String authtoken, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/customers/count.json";

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
    private okhttp3.Call customersCountJsonGetValidateBeforeCall(String login, String authtoken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling customersCountJsonGet(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling customersCountJsonGet(Async)");
        }

        return customersCountJsonGetCall(login, authtoken, _callback);

    }

    /**
     * Count all Customers.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @return Count
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Count customersCountJsonGet(String login, String authtoken) throws ApiException {
        ApiResponse<Count> localVarResp = customersCountJsonGetWithHttpInfo(login, authtoken);
        return localVarResp.getData();
    }

    /**
     * Count all Customers.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @return ApiResponse&lt;Count&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Count> customersCountJsonGetWithHttpInfo(String login, String authtoken) throws ApiException {
        okhttp3.Call localVarCall = customersCountJsonGetValidateBeforeCall(login, authtoken, null);
        Type localVarReturnType = new TypeToken<Count>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Count all Customers. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersCountJsonGetAsync(String login, String authtoken, final ApiCallback<Count> _callback) throws ApiException {

        okhttp3.Call localVarCall = customersCountJsonGetValidateBeforeCall(login, authtoken, _callback);
        Type localVarReturnType = new TypeToken<Count>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for customersEmailEmailJsonGet
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param email Email of the Customer (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersEmailEmailJsonGetCall(String login, String authtoken, String email, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/customers/email/{email}.json"
            .replace("{" + "email" + "}", localVarApiClient.escapeString(email.toString()));

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
    private okhttp3.Call customersEmailEmailJsonGetValidateBeforeCall(String login, String authtoken, String email, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling customersEmailEmailJsonGet(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling customersEmailEmailJsonGet(Async)");
        }

        // verify the required parameter 'email' is set
        if (email == null) {
            throw new ApiException("Missing the required parameter 'email' when calling customersEmailEmailJsonGet(Async)");
        }

        return customersEmailEmailJsonGetCall(login, authtoken, email, _callback);

    }

    /**
     * Retrieve a single Customer by email.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param email Email of the Customer (required)
     * @return Customer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public Customer customersEmailEmailJsonGet(String login, String authtoken, String email) throws ApiException {
        ApiResponse<Customer> localVarResp = customersEmailEmailJsonGetWithHttpInfo(login, authtoken, email);
        return localVarResp.getData();
    }

    /**
     * Retrieve a single Customer by email.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param email Email of the Customer (required)
     * @return ApiResponse&lt;Customer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Customer> customersEmailEmailJsonGetWithHttpInfo(String login, String authtoken, String email) throws ApiException {
        okhttp3.Call localVarCall = customersEmailEmailJsonGetValidateBeforeCall(login, authtoken, email, null);
        Type localVarReturnType = new TypeToken<Customer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a single Customer by email. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param email Email of the Customer (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersEmailEmailJsonGetAsync(String login, String authtoken, String email, final ApiCallback<Customer> _callback) throws ApiException {

        okhttp3.Call localVarCall = customersEmailEmailJsonGetValidateBeforeCall(login, authtoken, email, _callback);
        Type localVarReturnType = new TypeToken<Customer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for customersIdJsonDelete
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersIdJsonDeleteCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/customers/{id}.json"
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
    private okhttp3.Call customersIdJsonDeleteValidateBeforeCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling customersIdJsonDelete(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling customersIdJsonDelete(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling customersIdJsonDelete(Async)");
        }

        return customersIdJsonDeleteCall(login, authtoken, id, _callback);

    }

    /**
     * Delete an existing Customer.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public String customersIdJsonDelete(String login, String authtoken, Integer id) throws ApiException {
        ApiResponse<String> localVarResp = customersIdJsonDeleteWithHttpInfo(login, authtoken, id);
        return localVarResp.getData();
    }

    /**
     * Delete an existing Customer.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> customersIdJsonDeleteWithHttpInfo(String login, String authtoken, Integer id) throws ApiException {
        okhttp3.Call localVarCall = customersIdJsonDeleteValidateBeforeCall(login, authtoken, id, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete an existing Customer. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersIdJsonDeleteAsync(String login, String authtoken, Integer id, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = customersIdJsonDeleteValidateBeforeCall(login, authtoken, id, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for customersIdJsonGet
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersIdJsonGetCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/customers/{id}.json"
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
    private okhttp3.Call customersIdJsonGetValidateBeforeCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling customersIdJsonGet(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling customersIdJsonGet(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling customersIdJsonGet(Async)");
        }

        return customersIdJsonGetCall(login, authtoken, id, _callback);

    }

    /**
     * Retrieve a single Customer by id.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @return Customer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public Customer customersIdJsonGet(String login, String authtoken, Integer id) throws ApiException {
        ApiResponse<Customer> localVarResp = customersIdJsonGetWithHttpInfo(login, authtoken, id);
        return localVarResp.getData();
    }

    /**
     * Retrieve a single Customer by id.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @return ApiResponse&lt;Customer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Customer> customersIdJsonGetWithHttpInfo(String login, String authtoken, Integer id) throws ApiException {
        okhttp3.Call localVarCall = customersIdJsonGetValidateBeforeCall(login, authtoken, id, null);
        Type localVarReturnType = new TypeToken<Customer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a single Customer by id. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersIdJsonGetAsync(String login, String authtoken, Integer id, final ApiCallback<Customer> _callback) throws ApiException {

        okhttp3.Call localVarCall = customersIdJsonGetValidateBeforeCall(login, authtoken, id, _callback);
        Type localVarReturnType = new TypeToken<Customer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for customersIdJsonPut
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param customerWithPasswordNoID Customer parameters. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersIdJsonPutCall(String login, String authtoken, Integer id, CustomerWithPasswordNoID customerWithPasswordNoID, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = customerWithPasswordNoID;

        // create path and map variables
        String localVarPath = "/customers/{id}.json"
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
    private okhttp3.Call customersIdJsonPutValidateBeforeCall(String login, String authtoken, Integer id, CustomerWithPasswordNoID customerWithPasswordNoID, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling customersIdJsonPut(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling customersIdJsonPut(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling customersIdJsonPut(Async)");
        }

        // verify the required parameter 'customerWithPasswordNoID' is set
        if (customerWithPasswordNoID == null) {
            throw new ApiException("Missing the required parameter 'customerWithPasswordNoID' when calling customersIdJsonPut(Async)");
        }

        return customersIdJsonPutCall(login, authtoken, id, customerWithPasswordNoID, _callback);

    }

    /**
     * Update a new Customer.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param customerWithPasswordNoID Customer parameters. (required)
     * @return Customer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public Customer customersIdJsonPut(String login, String authtoken, Integer id, CustomerWithPasswordNoID customerWithPasswordNoID) throws ApiException {
        ApiResponse<Customer> localVarResp = customersIdJsonPutWithHttpInfo(login, authtoken, id, customerWithPasswordNoID);
        return localVarResp.getData();
    }

    /**
     * Update a new Customer.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param customerWithPasswordNoID Customer parameters. (required)
     * @return ApiResponse&lt;Customer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Customer> customersIdJsonPutWithHttpInfo(String login, String authtoken, Integer id, CustomerWithPasswordNoID customerWithPasswordNoID) throws ApiException {
        okhttp3.Call localVarCall = customersIdJsonPutValidateBeforeCall(login, authtoken, id, customerWithPasswordNoID, null);
        Type localVarReturnType = new TypeToken<Customer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update a new Customer. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param customerWithPasswordNoID Customer parameters. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersIdJsonPutAsync(String login, String authtoken, Integer id, CustomerWithPasswordNoID customerWithPasswordNoID, final ApiCallback<Customer> _callback) throws ApiException {

        okhttp3.Call localVarCall = customersIdJsonPutValidateBeforeCall(login, authtoken, id, customerWithPasswordNoID, _callback);
        Type localVarReturnType = new TypeToken<Customer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for customersJsonGet
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param limit List restriction (optional, default to 50)
     * @param page List page (optional, default to 1)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array of Orders </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersJsonGetCall(String login, String authtoken, Integer limit, Integer page, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/customers.json";

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
    private okhttp3.Call customersJsonGetValidateBeforeCall(String login, String authtoken, Integer limit, Integer page, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling customersJsonGet(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling customersJsonGet(Async)");
        }

        return customersJsonGetCall(login, authtoken, limit, page, _callback);

    }

    /**
     * Retrieve all Customers.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param limit List restriction (optional, default to 50)
     * @param page List page (optional, default to 1)
     * @return List&lt;Customer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array of Orders </td><td>  -  </td></tr>
     </table>
     */
    public List<Customer> customersJsonGet(String login, String authtoken, Integer limit, Integer page) throws ApiException {
        ApiResponse<List<Customer>> localVarResp = customersJsonGetWithHttpInfo(login, authtoken, limit, page);
        return localVarResp.getData();
    }

    /**
     * Retrieve all Customers.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param limit List restriction (optional, default to 50)
     * @param page List page (optional, default to 1)
     * @return ApiResponse&lt;List&lt;Customer&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array of Orders </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<Customer>> customersJsonGetWithHttpInfo(String login, String authtoken, Integer limit, Integer page) throws ApiException {
        okhttp3.Call localVarCall = customersJsonGetValidateBeforeCall(login, authtoken, limit, page, null);
        Type localVarReturnType = new TypeToken<List<Customer>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve all Customers. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param limit List restriction (optional, default to 50)
     * @param page List page (optional, default to 1)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> An array of Orders </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersJsonGetAsync(String login, String authtoken, Integer limit, Integer page, final ApiCallback<List<Customer>> _callback) throws ApiException {

        okhttp3.Call localVarCall = customersJsonGetValidateBeforeCall(login, authtoken, limit, page, _callback);
        Type localVarReturnType = new TypeToken<List<Customer>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for customersJsonPost
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param customerWithPasswordNoID Customer parameters. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersJsonPostCall(String login, String authtoken, CustomerWithPasswordNoID customerWithPasswordNoID, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = customerWithPasswordNoID;

        // create path and map variables
        String localVarPath = "/customers.json";

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
    private okhttp3.Call customersJsonPostValidateBeforeCall(String login, String authtoken, CustomerWithPasswordNoID customerWithPasswordNoID, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling customersJsonPost(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling customersJsonPost(Async)");
        }

        // verify the required parameter 'customerWithPasswordNoID' is set
        if (customerWithPasswordNoID == null) {
            throw new ApiException("Missing the required parameter 'customerWithPasswordNoID' when calling customersJsonPost(Async)");
        }

        return customersJsonPostCall(login, authtoken, customerWithPasswordNoID, _callback);

    }

    /**
     * Create a new Customer.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param customerWithPasswordNoID Customer parameters. (required)
     * @return Customer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public Customer customersJsonPost(String login, String authtoken, CustomerWithPasswordNoID customerWithPasswordNoID) throws ApiException {
        ApiResponse<Customer> localVarResp = customersJsonPostWithHttpInfo(login, authtoken, customerWithPasswordNoID);
        return localVarResp.getData();
    }

    /**
     * Create a new Customer.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param customerWithPasswordNoID Customer parameters. (required)
     * @return ApiResponse&lt;Customer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Customer> customersJsonPostWithHttpInfo(String login, String authtoken, CustomerWithPasswordNoID customerWithPasswordNoID) throws ApiException {
        okhttp3.Call localVarCall = customersJsonPostValidateBeforeCall(login, authtoken, customerWithPasswordNoID, null);
        Type localVarReturnType = new TypeToken<Customer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a new Customer. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param customerWithPasswordNoID Customer parameters. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersJsonPostAsync(String login, String authtoken, CustomerWithPasswordNoID customerWithPasswordNoID, final ApiCallback<Customer> _callback) throws ApiException {

        okhttp3.Call localVarCall = customersJsonPostValidateBeforeCall(login, authtoken, customerWithPasswordNoID, _callback);
        Type localVarReturnType = new TypeToken<Customer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
