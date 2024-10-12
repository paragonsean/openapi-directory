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


import org.openapitools.client.model.ListResultPaymentLink;
import org.openapitools.client.model.PaymentLink;
import org.openapitools.client.model.PaymentLinkUriApiModel;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PaymentLinkApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public PaymentLinkApi() {
        this(Configuration.getDefaultApiClient());
    }

    public PaymentLinkApi(ApiClient apiClient) {
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
     * Build call for paymentLinkApiAll
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param queryOptionsPage  (optional)
     * @param queryOptionsPageSize  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentLinkApiAllCall(String xAuthKey, String xAuthSecret, Integer queryOptionsPage, Integer queryOptionsPageSize, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/paymentlink/all";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (queryOptionsPage != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("queryOptions.page", queryOptionsPage));
        }

        if (queryOptionsPageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("queryOptions.pageSize", queryOptionsPageSize));
        }

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
    private okhttp3.Call paymentLinkApiAllValidateBeforeCall(String xAuthKey, String xAuthSecret, Integer queryOptionsPage, Integer queryOptionsPageSize, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAuthKey' is set
        if (xAuthKey == null) {
            throw new ApiException("Missing the required parameter 'xAuthKey' when calling paymentLinkApiAll(Async)");
        }

        // verify the required parameter 'xAuthSecret' is set
        if (xAuthSecret == null) {
            throw new ApiException("Missing the required parameter 'xAuthSecret' when calling paymentLinkApiAll(Async)");
        }

        return paymentLinkApiAllCall(xAuthKey, xAuthSecret, queryOptionsPage, queryOptionsPageSize, _callback);

    }

    /**
     * Create a payment link
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param queryOptionsPage  (optional)
     * @param queryOptionsPageSize  (optional)
     * @return ListResultPaymentLink
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ListResultPaymentLink paymentLinkApiAll(String xAuthKey, String xAuthSecret, Integer queryOptionsPage, Integer queryOptionsPageSize) throws ApiException {
        ApiResponse<ListResultPaymentLink> localVarResp = paymentLinkApiAllWithHttpInfo(xAuthKey, xAuthSecret, queryOptionsPage, queryOptionsPageSize);
        return localVarResp.getData();
    }

    /**
     * Create a payment link
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param queryOptionsPage  (optional)
     * @param queryOptionsPageSize  (optional)
     * @return ApiResponse&lt;ListResultPaymentLink&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListResultPaymentLink> paymentLinkApiAllWithHttpInfo(String xAuthKey, String xAuthSecret, Integer queryOptionsPage, Integer queryOptionsPageSize) throws ApiException {
        okhttp3.Call localVarCall = paymentLinkApiAllValidateBeforeCall(xAuthKey, xAuthSecret, queryOptionsPage, queryOptionsPageSize, null);
        Type localVarReturnType = new TypeToken<ListResultPaymentLink>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a payment link (asynchronously)
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param queryOptionsPage  (optional)
     * @param queryOptionsPageSize  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentLinkApiAllAsync(String xAuthKey, String xAuthSecret, Integer queryOptionsPage, Integer queryOptionsPageSize, final ApiCallback<ListResultPaymentLink> _callback) throws ApiException {

        okhttp3.Call localVarCall = paymentLinkApiAllValidateBeforeCall(xAuthKey, xAuthSecret, queryOptionsPage, queryOptionsPageSize, _callback);
        Type localVarReturnType = new TypeToken<ListResultPaymentLink>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for paymentLinkApiDelete
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param paymentLink  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentLinkApiDeleteCall(String xAuthKey, String xAuthSecret, PaymentLink paymentLink, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = paymentLink;

        // create path and map variables
        String localVarPath = "/api/paymentlink/delete";

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
    private okhttp3.Call paymentLinkApiDeleteValidateBeforeCall(String xAuthKey, String xAuthSecret, PaymentLink paymentLink, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAuthKey' is set
        if (xAuthKey == null) {
            throw new ApiException("Missing the required parameter 'xAuthKey' when calling paymentLinkApiDelete(Async)");
        }

        // verify the required parameter 'xAuthSecret' is set
        if (xAuthSecret == null) {
            throw new ApiException("Missing the required parameter 'xAuthSecret' when calling paymentLinkApiDelete(Async)");
        }

        // verify the required parameter 'paymentLink' is set
        if (paymentLink == null) {
            throw new ApiException("Missing the required parameter 'paymentLink' when calling paymentLinkApiDelete(Async)");
        }

        return paymentLinkApiDeleteCall(xAuthKey, xAuthSecret, paymentLink, _callback);

    }

    /**
     * Delete an existing payment link
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param paymentLink  (required)
     * @return Integer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Integer paymentLinkApiDelete(String xAuthKey, String xAuthSecret, PaymentLink paymentLink) throws ApiException {
        ApiResponse<Integer> localVarResp = paymentLinkApiDeleteWithHttpInfo(xAuthKey, xAuthSecret, paymentLink);
        return localVarResp.getData();
    }

    /**
     * Delete an existing payment link
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param paymentLink  (required)
     * @return ApiResponse&lt;Integer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Integer> paymentLinkApiDeleteWithHttpInfo(String xAuthKey, String xAuthSecret, PaymentLink paymentLink) throws ApiException {
        okhttp3.Call localVarCall = paymentLinkApiDeleteValidateBeforeCall(xAuthKey, xAuthSecret, paymentLink, null);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete an existing payment link (asynchronously)
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param paymentLink  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentLinkApiDeleteAsync(String xAuthKey, String xAuthSecret, PaymentLink paymentLink, final ApiCallback<Integer> _callback) throws ApiException {

        okhttp3.Call localVarCall = paymentLinkApiDeleteValidateBeforeCall(xAuthKey, xAuthSecret, paymentLink, _callback);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for paymentLinkApiNew
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param paymentLink  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentLinkApiNewCall(String xAuthKey, String xAuthSecret, PaymentLink paymentLink, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = paymentLink;

        // create path and map variables
        String localVarPath = "/api/paymentlink/new";

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
    private okhttp3.Call paymentLinkApiNewValidateBeforeCall(String xAuthKey, String xAuthSecret, PaymentLink paymentLink, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'xAuthKey' is set
        if (xAuthKey == null) {
            throw new ApiException("Missing the required parameter 'xAuthKey' when calling paymentLinkApiNew(Async)");
        }

        // verify the required parameter 'xAuthSecret' is set
        if (xAuthSecret == null) {
            throw new ApiException("Missing the required parameter 'xAuthSecret' when calling paymentLinkApiNew(Async)");
        }

        // verify the required parameter 'paymentLink' is set
        if (paymentLink == null) {
            throw new ApiException("Missing the required parameter 'paymentLink' when calling paymentLinkApiNew(Async)");
        }

        return paymentLinkApiNewCall(xAuthKey, xAuthSecret, paymentLink, _callback);

    }

    /**
     * Create a payment link
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param paymentLink  (required)
     * @return Integer
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Integer paymentLinkApiNew(String xAuthKey, String xAuthSecret, PaymentLink paymentLink) throws ApiException {
        ApiResponse<Integer> localVarResp = paymentLinkApiNewWithHttpInfo(xAuthKey, xAuthSecret, paymentLink);
        return localVarResp.getData();
    }

    /**
     * Create a payment link
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param paymentLink  (required)
     * @return ApiResponse&lt;Integer&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Integer> paymentLinkApiNewWithHttpInfo(String xAuthKey, String xAuthSecret, PaymentLink paymentLink) throws ApiException {
        okhttp3.Call localVarCall = paymentLinkApiNewValidateBeforeCall(xAuthKey, xAuthSecret, paymentLink, null);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Create a payment link (asynchronously)
     * 
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @param paymentLink  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call paymentLinkApiNewAsync(String xAuthKey, String xAuthSecret, PaymentLink paymentLink, final ApiCallback<Integer> _callback) throws ApiException {

        okhttp3.Call localVarCall = paymentLinkApiNewValidateBeforeCall(xAuthKey, xAuthSecret, paymentLink, _callback);
        Type localVarReturnType = new TypeToken<Integer>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for paymentLinkApiUri
     * @param id  (required)
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
    public okhttp3.Call paymentLinkApiUriCall(Integer id, String xAuthKey, String xAuthSecret, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/paymentlink/uri";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (id != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("id", id));
        }

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
    private okhttp3.Call paymentLinkApiUriValidateBeforeCall(Integer id, String xAuthKey, String xAuthSecret, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling paymentLinkApiUri(Async)");
        }

        // verify the required parameter 'xAuthKey' is set
        if (xAuthKey == null) {
            throw new ApiException("Missing the required parameter 'xAuthKey' when calling paymentLinkApiUri(Async)");
        }

        // verify the required parameter 'xAuthSecret' is set
        if (xAuthSecret == null) {
            throw new ApiException("Missing the required parameter 'xAuthSecret' when calling paymentLinkApiUri(Async)");
        }

        return paymentLinkApiUriCall(id, xAuthKey, xAuthSecret, _callback);

    }

    /**
     * Return the unique url to the client&#39;s payment link
     * 
     * @param id  (required)
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @return PaymentLinkUriApiModel
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public PaymentLinkUriApiModel paymentLinkApiUri(Integer id, String xAuthKey, String xAuthSecret) throws ApiException {
        ApiResponse<PaymentLinkUriApiModel> localVarResp = paymentLinkApiUriWithHttpInfo(id, xAuthKey, xAuthSecret);
        return localVarResp.getData();
    }

    /**
     * Return the unique url to the client&#39;s payment link
     * 
     * @param id  (required)
     * @param xAuthKey  (required)
     * @param xAuthSecret  (required)
     * @return ApiResponse&lt;PaymentLinkUriApiModel&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PaymentLinkUriApiModel> paymentLinkApiUriWithHttpInfo(Integer id, String xAuthKey, String xAuthSecret) throws ApiException {
        okhttp3.Call localVarCall = paymentLinkApiUriValidateBeforeCall(id, xAuthKey, xAuthSecret, null);
        Type localVarReturnType = new TypeToken<PaymentLinkUriApiModel>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Return the unique url to the client&#39;s payment link (asynchronously)
     * 
     * @param id  (required)
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
    public okhttp3.Call paymentLinkApiUriAsync(Integer id, String xAuthKey, String xAuthSecret, final ApiCallback<PaymentLinkUriApiModel> _callback) throws ApiException {

        okhttp3.Call localVarCall = paymentLinkApiUriValidateBeforeCall(id, xAuthKey, xAuthSecret, _callback);
        Type localVarReturnType = new TypeToken<PaymentLinkUriApiModel>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
