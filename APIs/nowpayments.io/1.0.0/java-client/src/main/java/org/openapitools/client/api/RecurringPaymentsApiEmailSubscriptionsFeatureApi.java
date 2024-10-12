/*
 * NOWPayments API
 * NOWPayments is a non-custodial cryptocurrency payment processing platform. Accept payments in a wide range of cryptos and get them instantly converted into a coin of your choice and sent to your wallet. Keeping it simple – no excess.  # Sandbox  Before production usage, you can test our API using the Sandbox. Details can be found [here](https://documenter.getpostman.com/view/7907941/T1LSCRHC)  # Authentication  To use the NOWPayments API you should do the following:  *   Sign up at [nowpayments.io](https://nowpayments.io) *   Specify your outcome wallet *   Generate an API key       # Standard e-commerce flow for NOWPayments API:  1.  API - Check API availability with the [\"GET API status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#9998079f-dcc8-4e07-9ac7-3d52f0fd733a) method. If required, check the list of available payment currencies with the [\"GET available currencies\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#1c268f89-4fe7-471e-81b4-5a3153577b73) method. 2.  UI - Ask a customer to select item/items for purchase to determine the total sum; 3.  UI - Ask a customer to select payment currency 4.  API - Get the minimum payment amount for the selected currency pair (payment currency to your Outcome Wallet currency) with the [\"GET Minimum payment amount\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#41b02221-2d58-4fcf-9529-59d3763d6434) method; 5.  API - Get the estimate of the total amount in crypto with [\"GET Estimated price\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#7025cacf-7040-4c7b-a83f-f9ff0a22a822) and check that it is larger than the minimum payment amount from step 4; 6.  API - Call the [\"POST Create payment\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#5e37f3ad-0fa1-4292-af51-5c7f95730486) method to create a payment and get the deposit address (in our example, the generated BTC wallet address is returned from this method); 7.  UI - Ask a customer to send the payment to the generated deposit address (in our example, user has to send BTC coins); 8.  UI - A customer sends coins, NOWPayments processes and exchanges them (if required), and settles the payment to your Outcome Wallet (in our example, to your ETH address); 9.  API - You can get the payment status either via our IPN callbacks or manually, using [\"GET Payment Status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) and display it to a customer so that they know when their payment has been processed. 10.  API - you call the list of payments made to your account via the [\"GET List of payments\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#c8399c0e-d798-4f01-83ae-ddaa6905c2da) method. Additionally, you can see all of this information in your [Account](https://account.nowpayments.io/payments) on NOWPayments website.       ## Alternative flow  1.  API - Check API availability with the [\"GET API status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#9998079f-dcc8-4e07-9ac7-3d52f0fd733a) method. If required, check the list of available payment currencies with the [\"GET available currencies\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#1c268f89-4fe7-471e-81b4-5a3153577b73) method. 2.  UI - Ask a customer to select item/items for purchase to determine the total sum; 3.  UI - Ask a customer to select payment currency 4.  API - Get the minimum payment amount for the selected currency pair (payment currency to your Outcome Wallet currency) with the [\"GET Minimum payment amount\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#41b02221-2d58-4fcf-9529-59d3763d6434) method; 5.  API - Get the estimate of the total amount in crypto with [\"GET Estimated price\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#7025cacf-7040-4c7b-a83f-f9ff0a22a822) and check that it is larger than the minimum payment amount from step 4; 6.  API - Call the [\"POST Create Invoice](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#3e3ce25e-f43f-4636-bbd9-11560e46048b) method to create an invoice. Set \"success_url\" - parameter so that the user will be redirected to your website after successful payment. 7.  UI - display the invoice url or redirect the user to the generated link. 8.  NOWPayments - the customer completes the payment and is redirected back to your website (only if \"success_url\" parameter is configured correctly!). 9.  API - You can get the payment status either via our IPN callbacks or manually, using [\"GET Payment Status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) and display it to a customer so that they know when their payment has been processed. 10.  API - you call the list of payments made to your account via the [\"GET List of payments\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#c8399c0e-d798-4f01-83ae-ddaa6905c2da) method. Additionally, you can see all of this information in your [Account](https://account.nowpayments.io/invoices) on NOWPayments website.       # API Documentation  ## Instant Payments Notifications  IPN (Instant payment notifications, or callbacks) are used to notify you when transaction status is changed.   To use them, you should complete the following steps:  1.  Generate and save the IPN Secret key in Store Settings tab at the Dashboard. 2.  Insert your URL address where you want to get callbacks in create_payment request. The parameter name is ipn_callback_url. You will receive payment updates (statuses) to this URL address. 3.  You will receive all the parameters at the URL address you specified in (2) by POST request.       The POST request will contain the *x-nowpayments-sig* parameter in the header.       The body of the request is similiar to a [get payment status](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) response body.       Example:       {\"payment_id\":5077125051,\"payment_status\":\"waiting\",\"pay_address\":\"0xd1cDE08A07cD25adEbEd35c3867a59228C09B606\",\"price_amount\":170,\"price_currency\":\"usd\",\"pay_amount\":155.38559757,\"actually_paid\":0,\"pay_currency\":\"mana\",\"order_id\":\"2\",\"order_description\":\"Apple Macbook Pro 2019 x 1\",\"purchase_id\":\"6084744717\",\"created_at\":\"2021-04-12T14:22:54.942Z\",\"updated_at\":\"2021-04-12T14:23:06.244Z\",\"outcome_amount\":1131.7812095,\"outcome_currency\":\"trx\"} 4.  Sort all the parameters from the POST request in alphabetical order. 5.  Convert them to string using       [JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) (params, Object.keys(params).sort()) or the same function. 6.  Sign a string with an IPN-secret key with HMAC and sha-512 key 7.  Compare the signed string from the previous step with the x-nowpayments-sig , which is stored in the header of the callback request.       If these strings are similar it is a success.       Otherwise, contact us on [support@nowpayments.io](mailto:support@nowpayments.io) to solve the problem.       Example of creating a signed string at Node.JS  ``` const hmac = crypto.createHmac('sha512', notificationsKey); hmac.update(JSON.stringify(params, Object.keys(params).sort())); const signature = hmac.digest('hex');  ```  Example of comparing signed strings in PHP  ``` function check_ipn_request_is_valid()     {         $error_msg = \"Unknown error\";         $auth_ok = false;         $request_data = null;         if (isset($_SERVER['HTTP_X_NOWPAYMENTS_SIG']) && !empty($_SERVER['HTTP_X_NOWPAYMENTS_SIG'])) {             $recived_hmac = $_SERVER['HTTP_X_NOWPAYMENTS_SIG'];             $request_json = file_get_contents('php://input');             $request_data = json_decode($request_json, true);             ksort($request_data);             $sorted_request_json = json_encode($request_data, JSON_UNESCAPED_SLASHES);             if ($request_json !== false && !empty($request_json)) {                 $hmac = hash_hmac(\"sha512\", $sorted_request_json, trim($this->ipn_secret));                 if ($hmac == $recived_hmac) {                     $auth_ok = true;                 } else {                     $error_msg = 'HMAC signature does not match';                 }             } else {                 $error_msg = 'Error reading POST data';             }         } else {             $error_msg = 'No HMAC signature sent.';         }     }  ```  ## Recurrent payment notifications  If an error is detected, the payment is flagged and will receive additional recurrent notifications (number of recurrent notifications can be changed in your Store Settings-> Instant Payment Notifications).  If an error is received again during processing of the payment, recurrent notifications will be initiated again.  Example: \"Timeout\" is set to 1 minute and \"Number of recurrent notifications\" is set to 3.  Once an error is detected, you will receive 3 notifications at 1 minute intervals.  ## Several payments for one order  If you want to create several payments for one Order you should do the following:  *   Create a payment for the full order amount. *   Save \"purchase_id\" which will be in \"create_payment\" response *   Create next payment or payments with this \"purchase_id\" in \"create_payment\" request. *   **Only works for partially_paid payments**       It may be useful if you want to give your customers opportunity to pay a full order with several payments, for example, one part in BTC and one part in ETH. Also, if your customer accidentally paid you only part of a full amount, you can automatically ask them to make another payment.  ## Packages  Please find our out-of-the box packages for easy integration below:  [JavaScript package](https://www.npmjs.com/package/@nowpaymentsio/nowpayments-api-js)  \\[PHP package\\]   ([https://packagist.org/packages/nowpayments/nowpayments-api-php](https://packagist.org/packages/nowpayments/nowpayments-api-php))  More coming soon!  ## Payments
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


import org.openapitools.client.model.DeleteRecurringPayment200Response;
import org.openapitools.client.model.GetManyPlans200Response;
import org.openapitools.client.model.GetManyRecurringPayments200Response;
import org.openapitools.client.model.GetOnePlan200Response;
import org.openapitools.client.model.GetOnePlan404Response;
import org.openapitools.client.model.GetOneRecurringPayment200Response;
import org.openapitools.client.model.GetOneRecurringPayment404Response;
import org.openapitools.client.model.UpdatePlanRequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class RecurringPaymentsApiEmailSubscriptionsFeatureApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public RecurringPaymentsApiEmailSubscriptionsFeatureApi() {
        this(Configuration.getDefaultApiClient());
    }

    public RecurringPaymentsApiEmailSubscriptionsFeatureApi(ApiClient apiClient) {
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
     * Build call for deleteRecurringPayment
     * @param subId  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> 404 </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRecurringPaymentCall(String subId, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/subscriptions/{sub_id}"
            .replace("{" + "sub_id" + "}", localVarApiClient.escapeString(subId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "text/plain"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteRecurringPaymentValidateBeforeCall(String subId, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'subId' is set
        if (subId == null) {
            throw new ApiException("Missing the required parameter 'subId' when calling deleteRecurringPayment(Async)");
        }

        return deleteRecurringPaymentCall(subId, _callback);

    }

    /**
     * Delete recurring payment
     * Completely removes a particular payment from the recurring payment plan.   You need to specify the payment plan id in the request.
     * @param subId  (required)
     * @return DeleteRecurringPayment200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> 404 </td><td>  -  </td></tr>
     </table>
     */
    public DeleteRecurringPayment200Response deleteRecurringPayment(String subId) throws ApiException {
        ApiResponse<DeleteRecurringPayment200Response> localVarResp = deleteRecurringPaymentWithHttpInfo(subId);
        return localVarResp.getData();
    }

    /**
     * Delete recurring payment
     * Completely removes a particular payment from the recurring payment plan.   You need to specify the payment plan id in the request.
     * @param subId  (required)
     * @return ApiResponse&lt;DeleteRecurringPayment200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> 404 </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteRecurringPayment200Response> deleteRecurringPaymentWithHttpInfo(String subId) throws ApiException {
        okhttp3.Call localVarCall = deleteRecurringPaymentValidateBeforeCall(subId, null);
        Type localVarReturnType = new TypeToken<DeleteRecurringPayment200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Delete recurring payment (asynchronously)
     * Completely removes a particular payment from the recurring payment plan.   You need to specify the payment plan id in the request.
     * @param subId  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> 404 </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRecurringPaymentAsync(String subId, final ApiCallback<DeleteRecurringPayment200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteRecurringPaymentValidateBeforeCall(subId, _callback);
        Type localVarReturnType = new TypeToken<DeleteRecurringPayment200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getManyPlans
     * @param limit Number (optional)
     * @param offset Number (optional)
     * @param xApiKey  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getManyPlansCall(String limit, String offset, String xApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/subscriptions/plans";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
        }

        if (xApiKey != null) {
            localVarHeaderParams.put("x-api-key", localVarApiClient.parameterToString(xApiKey));
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
    private okhttp3.Call getManyPlansValidateBeforeCall(String limit, String offset, String xApiKey, final ApiCallback _callback) throws ApiException {
        return getManyPlansCall(limit, offset, xApiKey, _callback);

    }

    /**
     * Get many plans
     * This method allows you to obtain information about all the payment plans you’ve created.
     * @param limit Number (optional)
     * @param offset Number (optional)
     * @param xApiKey  (optional)
     * @return GetManyPlans200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
     </table>
     */
    public GetManyPlans200Response getManyPlans(String limit, String offset, String xApiKey) throws ApiException {
        ApiResponse<GetManyPlans200Response> localVarResp = getManyPlansWithHttpInfo(limit, offset, xApiKey);
        return localVarResp.getData();
    }

    /**
     * Get many plans
     * This method allows you to obtain information about all the payment plans you’ve created.
     * @param limit Number (optional)
     * @param offset Number (optional)
     * @param xApiKey  (optional)
     * @return ApiResponse&lt;GetManyPlans200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetManyPlans200Response> getManyPlansWithHttpInfo(String limit, String offset, String xApiKey) throws ApiException {
        okhttp3.Call localVarCall = getManyPlansValidateBeforeCall(limit, offset, xApiKey, null);
        Type localVarReturnType = new TypeToken<GetManyPlans200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get many plans (asynchronously)
     * This method allows you to obtain information about all the payment plans you’ve created.
     * @param limit Number (optional)
     * @param offset Number (optional)
     * @param xApiKey  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getManyPlansAsync(String limit, String offset, String xApiKey, final ApiCallback<GetManyPlans200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getManyPlansValidateBeforeCall(limit, offset, xApiKey, _callback);
        Type localVarReturnType = new TypeToken<GetManyPlans200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getManyRecurringPayments
     * @param status \&quot;WAITING_PAY\&quot; / \&quot;PAID\&quot; /  \&quot;PARTIALLY_PAID\&quot; / \&quot;EXPIRED\&quot; (optional)
     * @param subscriptionPlanId  (optional)
     * @param isActive true / false (optional)
     * @param limit  (optional)
     * @param offset  (optional)
     * @param xApiKey  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getManyRecurringPaymentsCall(String status, String subscriptionPlanId, String isActive, String limit, String offset, String xApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/subscriptions";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (status != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("status", status));
        }

        if (subscriptionPlanId != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("subscription_plan_id", subscriptionPlanId));
        }

        if (isActive != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("is_active", isActive));
        }

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (offset != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("offset", offset));
        }

        if (xApiKey != null) {
            localVarHeaderParams.put("x-api-key", localVarApiClient.parameterToString(xApiKey));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "text/plain"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getManyRecurringPaymentsValidateBeforeCall(String status, String subscriptionPlanId, String isActive, String limit, String offset, String xApiKey, final ApiCallback _callback) throws ApiException {
        return getManyRecurringPaymentsCall(status, subscriptionPlanId, isActive, limit, offset, xApiKey, _callback);

    }

    /**
     * Get many recurring payments
     * The method allows you to view the entire list of recurring payments filtered by payment status and/or payment plan id
     * @param status \&quot;WAITING_PAY\&quot; / \&quot;PAID\&quot; /  \&quot;PARTIALLY_PAID\&quot; / \&quot;EXPIRED\&quot; (optional)
     * @param subscriptionPlanId  (optional)
     * @param isActive true / false (optional)
     * @param limit  (optional)
     * @param offset  (optional)
     * @param xApiKey  (optional)
     * @return GetManyRecurringPayments200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
     </table>
     */
    public GetManyRecurringPayments200Response getManyRecurringPayments(String status, String subscriptionPlanId, String isActive, String limit, String offset, String xApiKey) throws ApiException {
        ApiResponse<GetManyRecurringPayments200Response> localVarResp = getManyRecurringPaymentsWithHttpInfo(status, subscriptionPlanId, isActive, limit, offset, xApiKey);
        return localVarResp.getData();
    }

    /**
     * Get many recurring payments
     * The method allows you to view the entire list of recurring payments filtered by payment status and/or payment plan id
     * @param status \&quot;WAITING_PAY\&quot; / \&quot;PAID\&quot; /  \&quot;PARTIALLY_PAID\&quot; / \&quot;EXPIRED\&quot; (optional)
     * @param subscriptionPlanId  (optional)
     * @param isActive true / false (optional)
     * @param limit  (optional)
     * @param offset  (optional)
     * @param xApiKey  (optional)
     * @return ApiResponse&lt;GetManyRecurringPayments200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetManyRecurringPayments200Response> getManyRecurringPaymentsWithHttpInfo(String status, String subscriptionPlanId, String isActive, String limit, String offset, String xApiKey) throws ApiException {
        okhttp3.Call localVarCall = getManyRecurringPaymentsValidateBeforeCall(status, subscriptionPlanId, isActive, limit, offset, xApiKey, null);
        Type localVarReturnType = new TypeToken<GetManyRecurringPayments200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get many recurring payments (asynchronously)
     * The method allows you to view the entire list of recurring payments filtered by payment status and/or payment plan id
     * @param status \&quot;WAITING_PAY\&quot; / \&quot;PAID\&quot; /  \&quot;PARTIALLY_PAID\&quot; / \&quot;EXPIRED\&quot; (optional)
     * @param subscriptionPlanId  (optional)
     * @param isActive true / false (optional)
     * @param limit  (optional)
     * @param offset  (optional)
     * @param xApiKey  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getManyRecurringPaymentsAsync(String status, String subscriptionPlanId, String isActive, String limit, String offset, String xApiKey, final ApiCallback<GetManyRecurringPayments200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getManyRecurringPaymentsValidateBeforeCall(status, subscriptionPlanId, isActive, limit, offset, xApiKey, _callback);
        Type localVarReturnType = new TypeToken<GetManyRecurringPayments200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getOnePlan
     * @param planId  (required)
     * @param xApiKey  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> 404 </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getOnePlanCall(String planId, String xApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/subscriptions/plans/{plan-id}"
            .replace("{" + "plan-id" + "}", localVarApiClient.escapeString(planId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xApiKey != null) {
            localVarHeaderParams.put("x-api-key", localVarApiClient.parameterToString(xApiKey));
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
    private okhttp3.Call getOnePlanValidateBeforeCall(String planId, String xApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'planId' is set
        if (planId == null) {
            throw new ApiException("Missing the required parameter 'planId' when calling getOnePlan(Async)");
        }

        return getOnePlanCall(planId, xApiKey, _callback);

    }

    /**
     * Get one plan
     * This method allows you to obtain information about your payment plan.   (you need to specify your payment plan id in the request).
     * @param planId  (required)
     * @param xApiKey  (optional)
     * @return GetOnePlan200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> 404 </td><td>  -  </td></tr>
     </table>
     */
    public GetOnePlan200Response getOnePlan(String planId, String xApiKey) throws ApiException {
        ApiResponse<GetOnePlan200Response> localVarResp = getOnePlanWithHttpInfo(planId, xApiKey);
        return localVarResp.getData();
    }

    /**
     * Get one plan
     * This method allows you to obtain information about your payment plan.   (you need to specify your payment plan id in the request).
     * @param planId  (required)
     * @param xApiKey  (optional)
     * @return ApiResponse&lt;GetOnePlan200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> 404 </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetOnePlan200Response> getOnePlanWithHttpInfo(String planId, String xApiKey) throws ApiException {
        okhttp3.Call localVarCall = getOnePlanValidateBeforeCall(planId, xApiKey, null);
        Type localVarReturnType = new TypeToken<GetOnePlan200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get one plan (asynchronously)
     * This method allows you to obtain information about your payment plan.   (you need to specify your payment plan id in the request).
     * @param planId  (required)
     * @param xApiKey  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> 404 </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getOnePlanAsync(String planId, String xApiKey, final ApiCallback<GetOnePlan200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getOnePlanValidateBeforeCall(planId, xApiKey, _callback);
        Type localVarReturnType = new TypeToken<GetOnePlan200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getOneRecurringPayment
     * @param subId  (required)
     * @param xApiKey  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> 404 </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getOneRecurringPaymentCall(String subId, String xApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/subscriptions/{sub_id}"
            .replace("{" + "sub_id" + "}", localVarApiClient.escapeString(subId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xApiKey != null) {
            localVarHeaderParams.put("x-api-key", localVarApiClient.parameterToString(xApiKey));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "text/plain"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getOneRecurringPaymentValidateBeforeCall(String subId, String xApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'subId' is set
        if (subId == null) {
            throw new ApiException("Missing the required parameter 'subId' when calling getOneRecurringPayment(Async)");
        }

        return getOneRecurringPaymentCall(subId, xApiKey, _callback);

    }

    /**
     * Get one recurring payment
     * Get information about a particular recurring payment via its ID.  Here’s the list of available statuses:   \\- WAITING_PAY   \\- PAID   \\- PARTIALLY_PAID   \\- EXPIRED
     * @param subId  (required)
     * @param xApiKey  (optional)
     * @return GetOneRecurringPayment200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> 404 </td><td>  -  </td></tr>
     </table>
     */
    public GetOneRecurringPayment200Response getOneRecurringPayment(String subId, String xApiKey) throws ApiException {
        ApiResponse<GetOneRecurringPayment200Response> localVarResp = getOneRecurringPaymentWithHttpInfo(subId, xApiKey);
        return localVarResp.getData();
    }

    /**
     * Get one recurring payment
     * Get information about a particular recurring payment via its ID.  Here’s the list of available statuses:   \\- WAITING_PAY   \\- PAID   \\- PARTIALLY_PAID   \\- EXPIRED
     * @param subId  (required)
     * @param xApiKey  (optional)
     * @return ApiResponse&lt;GetOneRecurringPayment200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> 404 </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetOneRecurringPayment200Response> getOneRecurringPaymentWithHttpInfo(String subId, String xApiKey) throws ApiException {
        okhttp3.Call localVarCall = getOneRecurringPaymentValidateBeforeCall(subId, xApiKey, null);
        Type localVarReturnType = new TypeToken<GetOneRecurringPayment200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get one recurring payment (asynchronously)
     * Get information about a particular recurring payment via its ID.  Here’s the list of available statuses:   \\- WAITING_PAY   \\- PAID   \\- PARTIALLY_PAID   \\- EXPIRED
     * @param subId  (required)
     * @param xApiKey  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> 404 </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getOneRecurringPaymentAsync(String subId, String xApiKey, final ApiCallback<GetOneRecurringPayment200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getOneRecurringPaymentValidateBeforeCall(subId, xApiKey, _callback);
        Type localVarReturnType = new TypeToken<GetOneRecurringPayment200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updatePlan
     * @param planId  (required)
     * @param updatePlanRequest  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updatePlanCall(String planId, UpdatePlanRequest updatePlanRequest, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updatePlanRequest;

        // create path and map variables
        String localVarPath = "/v1/subscriptions/plans/{plan-id}"
            .replace("{" + "plan-id" + "}", localVarApiClient.escapeString(planId.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
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
        return localVarApiClient.buildCall(basePath, localVarPath, "PATCH", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updatePlanValidateBeforeCall(String planId, UpdatePlanRequest updatePlanRequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'planId' is set
        if (planId == null) {
            throw new ApiException("Missing the required parameter 'planId' when calling updatePlan(Async)");
        }

        return updatePlanCall(planId, updatePlanRequest, _callback);

    }

    /**
     * Update plan
     * This method allows you to add necessary changes to a created plan. They won’t affect users who have already paid; however, the changes will take effect when a new payment is to be made.
     * @param planId  (required)
     * @param updatePlanRequest  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public void updatePlan(String planId, UpdatePlanRequest updatePlanRequest) throws ApiException {
        updatePlanWithHttpInfo(planId, updatePlanRequest);
    }

    /**
     * Update plan
     * This method allows you to add necessary changes to a created plan. They won’t affect users who have already paid; however, the changes will take effect when a new payment is to be made.
     * @param planId  (required)
     * @param updatePlanRequest  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> updatePlanWithHttpInfo(String planId, UpdatePlanRequest updatePlanRequest) throws ApiException {
        okhttp3.Call localVarCall = updatePlanValidateBeforeCall(planId, updatePlanRequest, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Update plan (asynchronously)
     * This method allows you to add necessary changes to a created plan. They won’t affect users who have already paid; however, the changes will take effect when a new payment is to be made.
     * @param planId  (required)
     * @param updatePlanRequest  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td>  </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updatePlanAsync(String planId, UpdatePlanRequest updatePlanRequest, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = updatePlanValidateBeforeCall(planId, updatePlanRequest, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
