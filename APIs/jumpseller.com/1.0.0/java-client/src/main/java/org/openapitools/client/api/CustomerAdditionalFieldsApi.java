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


import org.openapitools.client.model.BadParams;
import org.openapitools.client.model.CustomerAdditionalField;
import org.openapitools.client.model.CustomerAdditionalFieldEdit;
import org.openapitools.client.model.NotFound;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CustomerAdditionalFieldsApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public CustomerAdditionalFieldsApi() {
        this(Configuration.getDefaultApiClient());
    }

    public CustomerAdditionalFieldsApi(ApiClient apiClient) {
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
     * Build call for customersIdFieldsFieldIdDelete
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param fieldId Id of the Customer Additional Field (required)
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
    public okhttp3.Call customersIdFieldsFieldIdDeleteCall(String login, String authtoken, Integer id, Integer fieldId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/customers/{id}/fields/{field_id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
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
    private okhttp3.Call customersIdFieldsFieldIdDeleteValidateBeforeCall(String login, String authtoken, Integer id, Integer fieldId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling customersIdFieldsFieldIdDelete(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling customersIdFieldsFieldIdDelete(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling customersIdFieldsFieldIdDelete(Async)");
        }

        // verify the required parameter 'fieldId' is set
        if (fieldId == null) {
            throw new ApiException("Missing the required parameter 'fieldId' when calling customersIdFieldsFieldIdDelete(Async)");
        }

        return customersIdFieldsFieldIdDeleteCall(login, authtoken, id, fieldId, _callback);

    }

    /**
     * Delete a Customer Additional Field.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param fieldId Id of the Customer Additional Field (required)
     * @return String
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public String customersIdFieldsFieldIdDelete(String login, String authtoken, Integer id, Integer fieldId) throws ApiException {
        ApiResponse<String> localVarResp = customersIdFieldsFieldIdDeleteWithHttpInfo(login, authtoken, id, fieldId);
        return localVarResp.getData();
    }

    /**
     * Delete a Customer Additional Field.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param fieldId Id of the Customer Additional Field (required)
     * @return ApiResponse&lt;String&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<String> customersIdFieldsFieldIdDeleteWithHttpInfo(String login, String authtoken, Integer id, Integer fieldId) throws ApiException {
        okhttp3.Call localVarCall = customersIdFieldsFieldIdDeleteValidateBeforeCall(login, authtoken, id, fieldId, null);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete a Customer Additional Field. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param fieldId Id of the Customer Additional Field (required)
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
    public okhttp3.Call customersIdFieldsFieldIdDeleteAsync(String login, String authtoken, Integer id, Integer fieldId, final ApiCallback<String> _callback) throws ApiException {

        okhttp3.Call localVarCall = customersIdFieldsFieldIdDeleteValidateBeforeCall(login, authtoken, id, fieldId, _callback);
        Type localVarReturnType = new TypeToken<String>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for customersIdFieldsFieldIdGet
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param fieldId Id of the Customer Additional Field (required)
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
    public okhttp3.Call customersIdFieldsFieldIdGetCall(String login, String authtoken, Integer id, Integer fieldId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/customers/{id}/fields/{field_id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
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
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call customersIdFieldsFieldIdGetValidateBeforeCall(String login, String authtoken, Integer id, Integer fieldId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling customersIdFieldsFieldIdGet(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling customersIdFieldsFieldIdGet(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling customersIdFieldsFieldIdGet(Async)");
        }

        // verify the required parameter 'fieldId' is set
        if (fieldId == null) {
            throw new ApiException("Missing the required parameter 'fieldId' when calling customersIdFieldsFieldIdGet(Async)");
        }

        return customersIdFieldsFieldIdGetCall(login, authtoken, id, fieldId, _callback);

    }

    /**
     * Retrieve a single Customer Additional Field.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param fieldId Id of the Customer Additional Field (required)
     * @return CustomerAdditionalField
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public CustomerAdditionalField customersIdFieldsFieldIdGet(String login, String authtoken, Integer id, Integer fieldId) throws ApiException {
        ApiResponse<CustomerAdditionalField> localVarResp = customersIdFieldsFieldIdGetWithHttpInfo(login, authtoken, id, fieldId);
        return localVarResp.getData();
    }

    /**
     * Retrieve a single Customer Additional Field.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param fieldId Id of the Customer Additional Field (required)
     * @return ApiResponse&lt;CustomerAdditionalField&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CustomerAdditionalField> customersIdFieldsFieldIdGetWithHttpInfo(String login, String authtoken, Integer id, Integer fieldId) throws ApiException {
        okhttp3.Call localVarCall = customersIdFieldsFieldIdGetValidateBeforeCall(login, authtoken, id, fieldId, null);
        Type localVarReturnType = new TypeToken<CustomerAdditionalField>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieve a single Customer Additional Field. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param fieldId Id of the Customer Additional Field (required)
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
    public okhttp3.Call customersIdFieldsFieldIdGetAsync(String login, String authtoken, Integer id, Integer fieldId, final ApiCallback<CustomerAdditionalField> _callback) throws ApiException {

        okhttp3.Call localVarCall = customersIdFieldsFieldIdGetValidateBeforeCall(login, authtoken, id, fieldId, _callback);
        Type localVarReturnType = new TypeToken<CustomerAdditionalField>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for customersIdFieldsFieldIdPut
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param fieldId Id of the Customer Additional Field (required)
     * @param customerAdditionalFieldEdit Customer Additional Field parameters. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Customer Additional Field Bad Parameters. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Additional Field Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersIdFieldsFieldIdPutCall(String login, String authtoken, Integer id, Integer fieldId, CustomerAdditionalFieldEdit customerAdditionalFieldEdit, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = customerAdditionalFieldEdit;

        // create path and map variables
        String localVarPath = "/customers/{id}/fields/{field_id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()))
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
    private okhttp3.Call customersIdFieldsFieldIdPutValidateBeforeCall(String login, String authtoken, Integer id, Integer fieldId, CustomerAdditionalFieldEdit customerAdditionalFieldEdit, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling customersIdFieldsFieldIdPut(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling customersIdFieldsFieldIdPut(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling customersIdFieldsFieldIdPut(Async)");
        }

        // verify the required parameter 'fieldId' is set
        if (fieldId == null) {
            throw new ApiException("Missing the required parameter 'fieldId' when calling customersIdFieldsFieldIdPut(Async)");
        }

        // verify the required parameter 'customerAdditionalFieldEdit' is set
        if (customerAdditionalFieldEdit == null) {
            throw new ApiException("Missing the required parameter 'customerAdditionalFieldEdit' when calling customersIdFieldsFieldIdPut(Async)");
        }

        return customersIdFieldsFieldIdPutCall(login, authtoken, id, fieldId, customerAdditionalFieldEdit, _callback);

    }

    /**
     * Update a Customer Additional Field.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param fieldId Id of the Customer Additional Field (required)
     * @param customerAdditionalFieldEdit Customer Additional Field parameters. (required)
     * @return CustomerAdditionalField
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Customer Additional Field Bad Parameters. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Additional Field Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public CustomerAdditionalField customersIdFieldsFieldIdPut(String login, String authtoken, Integer id, Integer fieldId, CustomerAdditionalFieldEdit customerAdditionalFieldEdit) throws ApiException {
        ApiResponse<CustomerAdditionalField> localVarResp = customersIdFieldsFieldIdPutWithHttpInfo(login, authtoken, id, fieldId, customerAdditionalFieldEdit);
        return localVarResp.getData();
    }

    /**
     * Update a Customer Additional Field.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param fieldId Id of the Customer Additional Field (required)
     * @param customerAdditionalFieldEdit Customer Additional Field parameters. (required)
     * @return ApiResponse&lt;CustomerAdditionalField&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Customer Additional Field Bad Parameters. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Additional Field Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CustomerAdditionalField> customersIdFieldsFieldIdPutWithHttpInfo(String login, String authtoken, Integer id, Integer fieldId, CustomerAdditionalFieldEdit customerAdditionalFieldEdit) throws ApiException {
        okhttp3.Call localVarCall = customersIdFieldsFieldIdPutValidateBeforeCall(login, authtoken, id, fieldId, customerAdditionalFieldEdit, null);
        Type localVarReturnType = new TypeToken<CustomerAdditionalField>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Update a Customer Additional Field. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param fieldId Id of the Customer Additional Field (required)
     * @param customerAdditionalFieldEdit Customer Additional Field parameters. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Customer Additional Field Bad Parameters. </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Additional Field Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersIdFieldsFieldIdPutAsync(String login, String authtoken, Integer id, Integer fieldId, CustomerAdditionalFieldEdit customerAdditionalFieldEdit, final ApiCallback<CustomerAdditionalField> _callback) throws ApiException {

        okhttp3.Call localVarCall = customersIdFieldsFieldIdPutValidateBeforeCall(login, authtoken, id, fieldId, customerAdditionalFieldEdit, _callback);
        Type localVarReturnType = new TypeToken<CustomerAdditionalField>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for customersIdFieldsGet
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
    public okhttp3.Call customersIdFieldsGetCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/customers/{id}/fields"
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
    private okhttp3.Call customersIdFieldsGetValidateBeforeCall(String login, String authtoken, Integer id, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling customersIdFieldsGet(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling customersIdFieldsGet(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling customersIdFieldsGet(Async)");
        }

        return customersIdFieldsGetCall(login, authtoken, id, _callback);

    }

    /**
     * Retrieves the Customer Additional Field of a Customer.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @return List&lt;CustomerAdditionalField&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public List<CustomerAdditionalField> customersIdFieldsGet(String login, String authtoken, Integer id) throws ApiException {
        ApiResponse<List<CustomerAdditionalField>> localVarResp = customersIdFieldsGetWithHttpInfo(login, authtoken, id);
        return localVarResp.getData();
    }

    /**
     * Retrieves the Customer Additional Field of a Customer.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @return ApiResponse&lt;List&lt;CustomerAdditionalField&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<CustomerAdditionalField>> customersIdFieldsGetWithHttpInfo(String login, String authtoken, Integer id) throws ApiException {
        okhttp3.Call localVarCall = customersIdFieldsGetValidateBeforeCall(login, authtoken, id, null);
        Type localVarReturnType = new TypeToken<List<CustomerAdditionalField>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Retrieves the Customer Additional Field of a Customer. (asynchronously)
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
    public okhttp3.Call customersIdFieldsGetAsync(String login, String authtoken, Integer id, final ApiCallback<List<CustomerAdditionalField>> _callback) throws ApiException {

        okhttp3.Call localVarCall = customersIdFieldsGetValidateBeforeCall(login, authtoken, id, _callback);
        Type localVarReturnType = new TypeToken<List<CustomerAdditionalField>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for customersIdFieldsPost
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param customerAdditionalFieldEdit Customer Additional Field parameters. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Additional Field Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersIdFieldsPostCall(String login, String authtoken, Integer id, CustomerAdditionalFieldEdit customerAdditionalFieldEdit, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = customerAdditionalFieldEdit;

        // create path and map variables
        String localVarPath = "/customers/{id}/fields"
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
    private okhttp3.Call customersIdFieldsPostValidateBeforeCall(String login, String authtoken, Integer id, CustomerAdditionalFieldEdit customerAdditionalFieldEdit, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'login' is set
        if (login == null) {
            throw new ApiException("Missing the required parameter 'login' when calling customersIdFieldsPost(Async)");
        }

        // verify the required parameter 'authtoken' is set
        if (authtoken == null) {
            throw new ApiException("Missing the required parameter 'authtoken' when calling customersIdFieldsPost(Async)");
        }

        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling customersIdFieldsPost(Async)");
        }

        // verify the required parameter 'customerAdditionalFieldEdit' is set
        if (customerAdditionalFieldEdit == null) {
            throw new ApiException("Missing the required parameter 'customerAdditionalFieldEdit' when calling customersIdFieldsPost(Async)");
        }

        return customersIdFieldsPostCall(login, authtoken, id, customerAdditionalFieldEdit, _callback);

    }

    /**
     * Adds Customer Additional Fields to a Customer.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param customerAdditionalFieldEdit Customer Additional Field parameters. (required)
     * @return CustomerAdditionalField
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Additional Field Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public CustomerAdditionalField customersIdFieldsPost(String login, String authtoken, Integer id, CustomerAdditionalFieldEdit customerAdditionalFieldEdit) throws ApiException {
        ApiResponse<CustomerAdditionalField> localVarResp = customersIdFieldsPostWithHttpInfo(login, authtoken, id, customerAdditionalFieldEdit);
        return localVarResp.getData();
    }

    /**
     * Adds Customer Additional Fields to a Customer.
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param customerAdditionalFieldEdit Customer Additional Field parameters. (required)
     * @return ApiResponse&lt;CustomerAdditionalField&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Additional Field Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CustomerAdditionalField> customersIdFieldsPostWithHttpInfo(String login, String authtoken, Integer id, CustomerAdditionalFieldEdit customerAdditionalFieldEdit) throws ApiException {
        okhttp3.Call localVarCall = customersIdFieldsPostValidateBeforeCall(login, authtoken, id, customerAdditionalFieldEdit, null);
        Type localVarReturnType = new TypeToken<CustomerAdditionalField>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Adds Customer Additional Fields to a Customer. (asynchronously)
     * 
     * @param login API OAuth login. (required)
     * @param authtoken API OAuth token. (required)
     * @param id Id of the Customer (required)
     * @param customerAdditionalFieldEdit Customer Additional Field parameters. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Customer Additional Field Not Found. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customersIdFieldsPostAsync(String login, String authtoken, Integer id, CustomerAdditionalFieldEdit customerAdditionalFieldEdit, final ApiCallback<CustomerAdditionalField> _callback) throws ApiException {

        okhttp3.Call localVarCall = customersIdFieldsPostValidateBeforeCall(login, authtoken, id, customerAdditionalFieldEdit, _callback);
        Type localVarReturnType = new TypeToken<CustomerAdditionalField>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
