/*
 * API v1.0.0
 * [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/80638214aa04722c9203)  <span style='margin-left: 0.5em;'>or</span>  <a href='https://documenter.getpostman.com/view/3559821/TVeqcn2L' class='openapi-button' _ngcontent-c6>View Postman docs</a>    # Quickstart    Visit [github](https://github.com/EmitKnowledge/Envoice) to view the quickstart tutorial.    <div class='postman-tutorial'>    # Tutorial for running the API in postman    Click on \"\"Run in Postman\"\" button  <br /><br />  ![postman - tutorial - 1](/Assets/images/api/postman-tutorial/postman-tutorial-1.png)     ---     A new page will open.  Click the \"\"Postman for windows\"\" to run postman as a desktop app.  Make sure you have already [installed](https://www.getpostman.com/docs/postman/launching_postman/installation_and_updates) Postman.  <br /><br />  ![postman - tutorial - 2](/Assets/images/api/postman-tutorial/postman-tutorial-2.png)     ---     In chrome an alert might show up to set a default app for opening postman links. Click on \"\"Open Postman\"\".  <br /><br />  ![postman - tutorial - 3](/Assets/images/api/postman-tutorial/postman-tutorial-3.png)     ---     The OpenAPI specification will be imported in Postman as a new collection named \"\"Envoice api\"\"  <br /><br />  ![postman - tutorial - 4](/Assets/images/api/postman-tutorial/postman-tutorial-4.png)     ---     When testing be sure to check and modify the environment variables to suit your api key and secret. The domain is set to envoice's endpoint so you don't really need to change that.    <sub>\\*Eye button in top right corner </sub>  <br /><br />   ![postman - tutorial - 5](/Assets/images/api/postman-tutorial/postman-tutorial-5.png)  <br /><br />   ![postman - tutorial - 6](/Assets/images/api/postman-tutorial/postman-tutorial-6.png)     ---     You don't need to change the values of the header parameters, because they will be replaced automatically when you send a request with real values from the environment configured in the previous step.  <br /><br />  ![postman - tutorial - 7](/Assets/images/api/postman-tutorial/postman-tutorial-7.png)     ---     Modify the example data to suit your needs and send a request.  <br /><br />  ![postman - tutorial - 8](/Assets/images/api/postman-tutorial/postman-tutorial-8.png)  </div>    # Webhooks    Webhooks allow you to build or set up Envoice Apps which subscribe to invoice activities.   When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL.   Webhooks can be used to update an external invoice data storage.    In order to use webhooks visit [this link](/account/settings#api-tab) and add upto 10 webhook urls that will return status `200` in order to signal that the webhook is working.  All nonworking webhooks will be ignored after a certain period of time and several retry attempts.  If after several attempts the webhook starts to work, we will send you all activities, both past and present, in chronological order.    The payload of the webhook is in format:  ```  {      Signature: \"\"sha256 string\"\",      Timestamp: \"\"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"\",      Activity: {          Message: \"string\",          Link: \"share url\",          Type: int,                  InvoiceNumber: \"string\",          InvoiceId: int,                  OrderNumber: \"string\",          OrderId: int,          Id: int,          CreatedOn: \"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"      }  }  ```            
 *
 * The version of the OpenAPI document: v1
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


import org.openapitools.client.model.TaxCreateApiModel;
import org.openapitools.client.model.TaxDeleteApiModel;
import org.openapitools.client.model.TaxDetailsApiModel;
import org.openapitools.client.model.TaxUpdateApiModel;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TaxApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public TaxApi() {
        this(Configuration.getDefaultApiClient());
    }

    public TaxApi(ApiClient apiClient) {
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
     * Build call for taxApiAll
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call taxApiAllCall(String xAuthKey, String xAuthSecret, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/tax/all";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAuthKey != null) {
            localVarHeaderParams.put("x-auth-key", localVarApiClient.parameterToString(xAuthKey));
        }

        if (xAuthSecret != null) {
            localVarHeaderParams.put("x-auth-secret", localVarApiClient.parameterToString(xAuthSecret));
        }

        final String[] localVarAccepts = {
            "application/json",
            "application/xml",
            "text/html",
            "text/json",
            "text/xml"
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
    private okhttp3.Call taxApiAllValidateBeforeCall(String xAuthKey, String xAuthSecret, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAuthKey' is set
        if (xAuthKey == null) {
            throw new ApiException("Missing the required parameter 'xAuthKey' when calling taxApiAll(Async)");
        }

        // verify the required parameter 'xAuthSecret' is set
        if (xAuthSecret == null) {
            throw new ApiException("Missing the required parameter 'xAuthSecret' when calling taxApiAll(Async)");
        }

        return taxApiAllCall(xAuthKey, xAuthSecret, _callback);

    }

    /**
     * Return all taxes for the account
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @return List&lt;TaxDetailsApiModel&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public List<TaxDetailsApiModel> taxApiAll(String xAuthKey, String xAuthSecret) throws ApiException {
        ApiResponse<List<TaxDetailsApiModel>> localVarResp = taxApiAllWithHttpInfo(xAuthKey, xAuthSecret);
        return localVarResp.getData();
    }

    /**
     * Return all taxes for the account
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @return ApiResponse&lt;List&lt;TaxDetailsApiModel&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<List<TaxDetailsApiModel>> taxApiAllWithHttpInfo(String xAuthKey, String xAuthSecret) throws ApiException {
        okhttp3.Call localVarCall = taxApiAllValidateBeforeCall(xAuthKey, xAuthSecret, null);
        Type localVarReturnType = new TypeToken<List<TaxDetailsApiModel>>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return all taxes for the account (asynchronously)
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call taxApiAllAsync(String xAuthKey, String xAuthSecret, final ApiCallback<List<TaxDetailsApiModel>> _callback) throws ApiException {

        okhttp3.Call localVarCall = taxApiAllValidateBeforeCall(xAuthKey, xAuthSecret, _callback);
        Type localVarReturnType = new TypeToken<List<TaxDetailsApiModel>>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for taxApiDelete
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param taxDeleteApiModel  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call taxApiDeleteCall(String xAuthKey, String xAuthSecret, TaxDeleteApiModel taxDeleteApiModel, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = taxDeleteApiModel;

        // create path and map variables
        String localVarPath = "/api/tax/delete";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAuthKey != null) {
            localVarHeaderParams.put("x-auth-key", localVarApiClient.parameterToString(xAuthKey));
        }

        if (xAuthSecret != null) {
            localVarHeaderParams.put("x-auth-secret", localVarApiClient.parameterToString(xAuthSecret));
        }

        final String[] localVarAccepts = {
            "application/json",
            "application/xml",
            "text/html",
            "text/json",
            "text/xml"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json",
            "application/x-www-form-urlencoded",
            "application/xml",
            "text/html",
            "text/json",
            "text/xml"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call taxApiDeleteValidateBeforeCall(String xAuthKey, String xAuthSecret, TaxDeleteApiModel taxDeleteApiModel, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAuthKey' is set
        if (xAuthKey == null) {
            throw new ApiException("Missing the required parameter 'xAuthKey' when calling taxApiDelete(Async)");
        }

        // verify the required parameter 'xAuthSecret' is set
        if (xAuthSecret == null) {
            throw new ApiException("Missing the required parameter 'xAuthSecret' when calling taxApiDelete(Async)");
        }

        // verify the required parameter 'taxDeleteApiModel' is set
        if (taxDeleteApiModel == null) {
            throw new ApiException("Missing the required parameter 'taxDeleteApiModel' when calling taxApiDelete(Async)");
        }

        return taxApiDeleteCall(xAuthKey, xAuthSecret, taxDeleteApiModel, _callback);

    }

    /**
     * Delete an existing tax
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param taxDeleteApiModel  (required)
     * @return Integer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Integer taxApiDelete(String xAuthKey, String xAuthSecret, TaxDeleteApiModel taxDeleteApiModel) throws ApiException {
        ApiResponse<Integer> localVarResp = taxApiDeleteWithHttpInfo(xAuthKey, xAuthSecret, taxDeleteApiModel);
        return localVarResp.getData();
    }

    /**
     * Delete an existing tax
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param taxDeleteApiModel  (required)
     * @return ApiResponse&lt;Integer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Integer> taxApiDeleteWithHttpInfo(String xAuthKey, String xAuthSecret, TaxDeleteApiModel taxDeleteApiModel) throws ApiException {
        okhttp3.Call localVarCall = taxApiDeleteValidateBeforeCall(xAuthKey, xAuthSecret, taxDeleteApiModel, null);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete an existing tax (asynchronously)
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param taxDeleteApiModel  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call taxApiDeleteAsync(String xAuthKey, String xAuthSecret, TaxDeleteApiModel taxDeleteApiModel, final ApiCallback<Integer> _callback) throws ApiException {

        okhttp3.Call localVarCall = taxApiDeleteValidateBeforeCall(xAuthKey, xAuthSecret, taxDeleteApiModel, _callback);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for taxApiNew
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param taxCreateApiModel  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call taxApiNewCall(String xAuthKey, String xAuthSecret, TaxCreateApiModel taxCreateApiModel, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = taxCreateApiModel;

        // create path and map variables
        String localVarPath = "/api/tax/new";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAuthKey != null) {
            localVarHeaderParams.put("x-auth-key", localVarApiClient.parameterToString(xAuthKey));
        }

        if (xAuthSecret != null) {
            localVarHeaderParams.put("x-auth-secret", localVarApiClient.parameterToString(xAuthSecret));
        }

        final String[] localVarAccepts = {
            "application/json",
            "application/xml",
            "text/html",
            "text/json",
            "text/xml"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json",
            "application/x-www-form-urlencoded",
            "application/xml",
            "text/html",
            "text/json",
            "text/xml"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call taxApiNewValidateBeforeCall(String xAuthKey, String xAuthSecret, TaxCreateApiModel taxCreateApiModel, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAuthKey' is set
        if (xAuthKey == null) {
            throw new ApiException("Missing the required parameter 'xAuthKey' when calling taxApiNew(Async)");
        }

        // verify the required parameter 'xAuthSecret' is set
        if (xAuthSecret == null) {
            throw new ApiException("Missing the required parameter 'xAuthSecret' when calling taxApiNew(Async)");
        }

        // verify the required parameter 'taxCreateApiModel' is set
        if (taxCreateApiModel == null) {
            throw new ApiException("Missing the required parameter 'taxCreateApiModel' when calling taxApiNew(Async)");
        }

        return taxApiNewCall(xAuthKey, xAuthSecret, taxCreateApiModel, _callback);

    }

    /**
     * Create a tax
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param taxCreateApiModel  (required)
     * @return Integer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Integer taxApiNew(String xAuthKey, String xAuthSecret, TaxCreateApiModel taxCreateApiModel) throws ApiException {
        ApiResponse<Integer> localVarResp = taxApiNewWithHttpInfo(xAuthKey, xAuthSecret, taxCreateApiModel);
        return localVarResp.getData();
    }

    /**
     * Create a tax
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param taxCreateApiModel  (required)
     * @return ApiResponse&lt;Integer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Integer> taxApiNewWithHttpInfo(String xAuthKey, String xAuthSecret, TaxCreateApiModel taxCreateApiModel) throws ApiException {
        okhttp3.Call localVarCall = taxApiNewValidateBeforeCall(xAuthKey, xAuthSecret, taxCreateApiModel, null);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a tax (asynchronously)
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param taxCreateApiModel  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call taxApiNewAsync(String xAuthKey, String xAuthSecret, TaxCreateApiModel taxCreateApiModel, final ApiCallback<Integer> _callback) throws ApiException {

        okhttp3.Call localVarCall = taxApiNewValidateBeforeCall(xAuthKey, xAuthSecret, taxCreateApiModel, _callback);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for taxApiUpdate
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param taxUpdateApiModel  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call taxApiUpdateCall(String xAuthKey, String xAuthSecret, TaxUpdateApiModel taxUpdateApiModel, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = taxUpdateApiModel;

        // create path and map variables
        String localVarPath = "/api/tax/update";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAuthKey != null) {
            localVarHeaderParams.put("x-auth-key", localVarApiClient.parameterToString(xAuthKey));
        }

        if (xAuthSecret != null) {
            localVarHeaderParams.put("x-auth-secret", localVarApiClient.parameterToString(xAuthSecret));
        }

        final String[] localVarAccepts = {
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json",
            "application/x-www-form-urlencoded",
            "application/xml",
            "text/html",
            "text/json",
            "text/xml"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call taxApiUpdateValidateBeforeCall(String xAuthKey, String xAuthSecret, TaxUpdateApiModel taxUpdateApiModel, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAuthKey' is set
        if (xAuthKey == null) {
            throw new ApiException("Missing the required parameter 'xAuthKey' when calling taxApiUpdate(Async)");
        }

        // verify the required parameter 'xAuthSecret' is set
        if (xAuthSecret == null) {
            throw new ApiException("Missing the required parameter 'xAuthSecret' when calling taxApiUpdate(Async)");
        }

        // verify the required parameter 'taxUpdateApiModel' is set
        if (taxUpdateApiModel == null) {
            throw new ApiException("Missing the required parameter 'taxUpdateApiModel' when calling taxApiUpdate(Async)");
        }

        return taxApiUpdateCall(xAuthKey, xAuthSecret, taxUpdateApiModel, _callback);

    }

    /**
     * Update an existing tax
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param taxUpdateApiModel  (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public void taxApiUpdate(String xAuthKey, String xAuthSecret, TaxUpdateApiModel taxUpdateApiModel) throws ApiException {
        taxApiUpdateWithHttpInfo(xAuthKey, xAuthSecret, taxUpdateApiModel);
    }

    /**
     * Update an existing tax
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param taxUpdateApiModel  (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> taxApiUpdateWithHttpInfo(String xAuthKey, String xAuthSecret, TaxUpdateApiModel taxUpdateApiModel) throws ApiException {
        okhttp3.Call localVarCall = taxApiUpdateValidateBeforeCall(xAuthKey, xAuthSecret, taxUpdateApiModel, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update an existing tax (asynchronously)
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param taxUpdateApiModel  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call taxApiUpdateAsync(String xAuthKey, String xAuthSecret, TaxUpdateApiModel taxUpdateApiModel, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = taxApiUpdateValidateBeforeCall(xAuthKey, xAuthSecret, taxUpdateApiModel, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
