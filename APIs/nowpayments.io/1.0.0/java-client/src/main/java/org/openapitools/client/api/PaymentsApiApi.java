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


import org.openapitools.client.model.GetEstimatedPrice200Response;
import org.openapitools.client.model.GetListOfPayments200Response;
import org.openapitools.client.model.GetPaymentStatus200Response;
import org.openapitools.client.model.GetTheMinimumPaymentAmount200Response;
import org.openapitools.client.model.GetUpdatePaymentEstimate200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PaymentsApiApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public PaymentsApiApi() {
        this(Configuration.getDefaultApiClient());
    }

    public PaymentsApiApi(ApiClient apiClient) {
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
     * Build call for getEstimatedPrice
     * @param amount  (optional)
     * @param currencyFrom  (optional)
     * @param currencyTo  (optional)
     * @param xApiKey  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getEstimatedPriceCall(String amount, String currencyFrom, String currencyTo, String xApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/estimate";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (amount != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("amount", amount));
        }

        if (currencyFrom != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("currency_from", currencyFrom));
        }

        if (currencyTo != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("currency_to", currencyTo));
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
    private okhttp3.Call getEstimatedPriceValidateBeforeCall(String amount, String currencyFrom, String currencyTo, String xApiKey, final ApiCallback _callback) throws ApiException {
        return getEstimatedPriceCall(amount, currencyFrom, currencyTo, xApiKey, _callback);

    }

    /**
     * Get estimated price
     * This is a method for calculating the approximate price in cryptocurrency for a given value in Fiat currency. You will need to provide the initial cost in the Fiat currency (amount, currency_from) and the necessary cryptocurrency (currency_to) Currently following fiat currencies are available: usd, eur, nzd, brl, gbp.
     * @param amount  (optional)
     * @param currencyFrom  (optional)
     * @param currencyTo  (optional)
     * @param xApiKey  (optional)
     * @return GetEstimatedPrice200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public GetEstimatedPrice200Response getEstimatedPrice(String amount, String currencyFrom, String currencyTo, String xApiKey) throws ApiException {
        ApiResponse<GetEstimatedPrice200Response> localVarResp = getEstimatedPriceWithHttpInfo(amount, currencyFrom, currencyTo, xApiKey);
        return localVarResp.getData();
    }

    /**
     * Get estimated price
     * This is a method for calculating the approximate price in cryptocurrency for a given value in Fiat currency. You will need to provide the initial cost in the Fiat currency (amount, currency_from) and the necessary cryptocurrency (currency_to) Currently following fiat currencies are available: usd, eur, nzd, brl, gbp.
     * @param amount  (optional)
     * @param currencyFrom  (optional)
     * @param currencyTo  (optional)
     * @param xApiKey  (optional)
     * @return ApiResponse&lt;GetEstimatedPrice200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<GetEstimatedPrice200Response> getEstimatedPriceWithHttpInfo(String amount, String currencyFrom, String currencyTo, String xApiKey) throws ApiException {
        okhttp3.Call localVarCall = getEstimatedPriceValidateBeforeCall(amount, currencyFrom, currencyTo, xApiKey, null);
        Type localVarReturnType = new TypeToken<GetEstimatedPrice200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get estimated price (asynchronously)
     * This is a method for calculating the approximate price in cryptocurrency for a given value in Fiat currency. You will need to provide the initial cost in the Fiat currency (amount, currency_from) and the necessary cryptocurrency (currency_to) Currently following fiat currencies are available: usd, eur, nzd, brl, gbp.
     * @param amount  (optional)
     * @param currencyFrom  (optional)
     * @param currencyTo  (optional)
     * @param xApiKey  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getEstimatedPriceAsync(String amount, String currencyFrom, String currencyTo, String xApiKey, final ApiCallback<GetEstimatedPrice200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getEstimatedPriceValidateBeforeCall(amount, currencyFrom, currencyTo, xApiKey, _callback);
        Type localVarReturnType = new TypeToken<GetEstimatedPrice200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getListOfPayments
     * @param limit  (optional)
     * @param page  (optional)
     * @param sortBy  (optional)
     * @param orderBy  (optional)
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param xApiKey  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getListOfPaymentsCall(String limit, String page, String sortBy, String orderBy, String dateFrom, String dateTo, String xApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/payment/";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (limit != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("limit", limit));
        }

        if (page != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page", page));
        }

        if (sortBy != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("sortBy", sortBy));
        }

        if (orderBy != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("orderBy", orderBy));
        }

        if (dateFrom != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("dateFrom", dateFrom));
        }

        if (dateTo != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("dateTo", dateTo));
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
    private okhttp3.Call getListOfPaymentsValidateBeforeCall(String limit, String page, String sortBy, String orderBy, String dateFrom, String dateTo, String xApiKey, final ApiCallback _callback) throws ApiException {
        return getListOfPaymentsCall(limit, page, sortBy, orderBy, dateFrom, dateTo, xApiKey, _callback);

    }

    /**
     * Get list of payments
     * Returns the entire list of all transactions, created with certain API key. The list of optional parameters: - limit - number of records in one page. (possible values: from 1 to 500) - page - the page number you want to get (possible values: from 0 to **page count - 1**) - sortBy - sort the received list by a paramenter. Set to **created_at** by default (possible values: payment_id, payment_status, pay_address, price_amount, price_currency, pay_amount, actually_paid, pay_currency, order_id, order_description, purchase_id, outcome_amount, outcome_currency) - orderBy - display the list in ascending or descending order. Set to **asc** by default (possible values: asc, desc) - dateFrom - select the displayed period start date (date format: YYYY-MM-DD or yy-MM-ddTHH:mm:ss.SSSZ). - dateTo - select the displayed period end date (date format: YYYY-MM-DD or yy-MM-ddTHH:mm:ss.SSSZ).
     * @param limit  (optional)
     * @param page  (optional)
     * @param sortBy  (optional)
     * @param orderBy  (optional)
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param xApiKey  (optional)
     * @return GetListOfPayments200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public GetListOfPayments200Response getListOfPayments(String limit, String page, String sortBy, String orderBy, String dateFrom, String dateTo, String xApiKey) throws ApiException {
        ApiResponse<GetListOfPayments200Response> localVarResp = getListOfPaymentsWithHttpInfo(limit, page, sortBy, orderBy, dateFrom, dateTo, xApiKey);
        return localVarResp.getData();
    }

    /**
     * Get list of payments
     * Returns the entire list of all transactions, created with certain API key. The list of optional parameters: - limit - number of records in one page. (possible values: from 1 to 500) - page - the page number you want to get (possible values: from 0 to **page count - 1**) - sortBy - sort the received list by a paramenter. Set to **created_at** by default (possible values: payment_id, payment_status, pay_address, price_amount, price_currency, pay_amount, actually_paid, pay_currency, order_id, order_description, purchase_id, outcome_amount, outcome_currency) - orderBy - display the list in ascending or descending order. Set to **asc** by default (possible values: asc, desc) - dateFrom - select the displayed period start date (date format: YYYY-MM-DD or yy-MM-ddTHH:mm:ss.SSSZ). - dateTo - select the displayed period end date (date format: YYYY-MM-DD or yy-MM-ddTHH:mm:ss.SSSZ).
     * @param limit  (optional)
     * @param page  (optional)
     * @param sortBy  (optional)
     * @param orderBy  (optional)
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param xApiKey  (optional)
     * @return ApiResponse&lt;GetListOfPayments200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<GetListOfPayments200Response> getListOfPaymentsWithHttpInfo(String limit, String page, String sortBy, String orderBy, String dateFrom, String dateTo, String xApiKey) throws ApiException {
        okhttp3.Call localVarCall = getListOfPaymentsValidateBeforeCall(limit, page, sortBy, orderBy, dateFrom, dateTo, xApiKey, null);
        Type localVarReturnType = new TypeToken<GetListOfPayments200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get list of payments (asynchronously)
     * Returns the entire list of all transactions, created with certain API key. The list of optional parameters: - limit - number of records in one page. (possible values: from 1 to 500) - page - the page number you want to get (possible values: from 0 to **page count - 1**) - sortBy - sort the received list by a paramenter. Set to **created_at** by default (possible values: payment_id, payment_status, pay_address, price_amount, price_currency, pay_amount, actually_paid, pay_currency, order_id, order_description, purchase_id, outcome_amount, outcome_currency) - orderBy - display the list in ascending or descending order. Set to **asc** by default (possible values: asc, desc) - dateFrom - select the displayed period start date (date format: YYYY-MM-DD or yy-MM-ddTHH:mm:ss.SSSZ). - dateTo - select the displayed period end date (date format: YYYY-MM-DD or yy-MM-ddTHH:mm:ss.SSSZ).
     * @param limit  (optional)
     * @param page  (optional)
     * @param sortBy  (optional)
     * @param orderBy  (optional)
     * @param dateFrom  (optional)
     * @param dateTo  (optional)
     * @param xApiKey  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getListOfPaymentsAsync(String limit, String page, String sortBy, String orderBy, String dateFrom, String dateTo, String xApiKey, final ApiCallback<GetListOfPayments200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getListOfPaymentsValidateBeforeCall(limit, page, sortBy, orderBy, dateFrom, dateTo, xApiKey, _callback);
        Type localVarReturnType = new TypeToken<GetListOfPayments200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getPaymentStatus
     * @param paymentId  (required)
     * @param xApiKey  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getPaymentStatusCall(String paymentId, String xApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/payment/{payment_id}"
            .replace("{" + "payment_id" + "}", localVarApiClient.escapeString(paymentId.toString()));

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
    private okhttp3.Call getPaymentStatusValidateBeforeCall(String paymentId, String xApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'paymentId' is set
        if (paymentId == null) {
            throw new ApiException("Missing the required parameter 'paymentId' when calling getPaymentStatus(Async)");
        }

        return getPaymentStatusCall(paymentId, xApiKey, _callback);

    }

    /**
     * Get payment status
     * Get the actual information about the payment. You need to provide the ID of the payment in the request.  NOTE! You should make the get payment status request with the same API key that you used in the create payment request. Here is the list of avalable statuses: - waiting - waiting for the customer to send the payment. The initial status of each payment. - confirming - the transaction is being processed on the blockchain. Appears when NOWPayments detect the funds from the user on the blockchain. - confirmed -  the process is confirmed by the blockchain. Customer’s funds have accumulated enough confirmations. - sending - the funds are being sent to your personal wallet. We are in the process of sending the funds to you. - partially_paid -  it shows that the customer sent the less than the actual price. Appears when the funds have arrived in your wallet. - finished - the funds have reached your personal address and the payment is finished. - failed -  the payment wasn&#39;t completed due to the error of some kind. - refunded -  the funds were refunded back to the user. - expired - the user didn&#39;t send the funds to the specified address in the 24 hour time window.  Additional info: - outcome_amount - this parameter shows the amount that will be (or is already) received on your Outcome Wallet once the transaction is settled. - outcome_currency - this parameter shows the currency in which the transaction will be settled. - invoice_id - this parameter shows invoice ID from which the payment was created
     * @param paymentId  (required)
     * @param xApiKey  (optional)
     * @return GetPaymentStatus200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public GetPaymentStatus200Response getPaymentStatus(String paymentId, String xApiKey) throws ApiException {
        ApiResponse<GetPaymentStatus200Response> localVarResp = getPaymentStatusWithHttpInfo(paymentId, xApiKey);
        return localVarResp.getData();
    }

    /**
     * Get payment status
     * Get the actual information about the payment. You need to provide the ID of the payment in the request.  NOTE! You should make the get payment status request with the same API key that you used in the create payment request. Here is the list of avalable statuses: - waiting - waiting for the customer to send the payment. The initial status of each payment. - confirming - the transaction is being processed on the blockchain. Appears when NOWPayments detect the funds from the user on the blockchain. - confirmed -  the process is confirmed by the blockchain. Customer’s funds have accumulated enough confirmations. - sending - the funds are being sent to your personal wallet. We are in the process of sending the funds to you. - partially_paid -  it shows that the customer sent the less than the actual price. Appears when the funds have arrived in your wallet. - finished - the funds have reached your personal address and the payment is finished. - failed -  the payment wasn&#39;t completed due to the error of some kind. - refunded -  the funds were refunded back to the user. - expired - the user didn&#39;t send the funds to the specified address in the 24 hour time window.  Additional info: - outcome_amount - this parameter shows the amount that will be (or is already) received on your Outcome Wallet once the transaction is settled. - outcome_currency - this parameter shows the currency in which the transaction will be settled. - invoice_id - this parameter shows invoice ID from which the payment was created
     * @param paymentId  (required)
     * @param xApiKey  (optional)
     * @return ApiResponse&lt;GetPaymentStatus200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<GetPaymentStatus200Response> getPaymentStatusWithHttpInfo(String paymentId, String xApiKey) throws ApiException {
        okhttp3.Call localVarCall = getPaymentStatusValidateBeforeCall(paymentId, xApiKey, null);
        Type localVarReturnType = new TypeToken<GetPaymentStatus200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get payment status (asynchronously)
     * Get the actual information about the payment. You need to provide the ID of the payment in the request.  NOTE! You should make the get payment status request with the same API key that you used in the create payment request. Here is the list of avalable statuses: - waiting - waiting for the customer to send the payment. The initial status of each payment. - confirming - the transaction is being processed on the blockchain. Appears when NOWPayments detect the funds from the user on the blockchain. - confirmed -  the process is confirmed by the blockchain. Customer’s funds have accumulated enough confirmations. - sending - the funds are being sent to your personal wallet. We are in the process of sending the funds to you. - partially_paid -  it shows that the customer sent the less than the actual price. Appears when the funds have arrived in your wallet. - finished - the funds have reached your personal address and the payment is finished. - failed -  the payment wasn&#39;t completed due to the error of some kind. - refunded -  the funds were refunded back to the user. - expired - the user didn&#39;t send the funds to the specified address in the 24 hour time window.  Additional info: - outcome_amount - this parameter shows the amount that will be (or is already) received on your Outcome Wallet once the transaction is settled. - outcome_currency - this parameter shows the currency in which the transaction will be settled. - invoice_id - this parameter shows invoice ID from which the payment was created
     * @param paymentId  (required)
     * @param xApiKey  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getPaymentStatusAsync(String paymentId, String xApiKey, final ApiCallback<GetPaymentStatus200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getPaymentStatusValidateBeforeCall(paymentId, xApiKey, _callback);
        Type localVarReturnType = new TypeToken<GetPaymentStatus200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getTheMinimumPaymentAmount
     * @param currencyFrom  (optional)
     * @param currencyTo  (optional)
     * @param xApiKey  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getTheMinimumPaymentAmountCall(String currencyFrom, String currencyTo, String xApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/min-amount";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (currencyFrom != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("currency_from", currencyFrom));
        }

        if (currencyTo != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("currency_to", currencyTo));
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
    private okhttp3.Call getTheMinimumPaymentAmountValidateBeforeCall(String currencyFrom, String currencyTo, String xApiKey, final ApiCallback _callback) throws ApiException {
        return getTheMinimumPaymentAmountCall(currencyFrom, currencyTo, xApiKey, _callback);

    }

    /**
     * Get the minimum payment amount
     * Get the minimum payment amount for a specific pair.  You can provide both currencies in the pair or just currency\\_from, and we will calculate the minimum payment amount for currency\\_from and currency which you have specified as the outcome in the Store Settings.  You can also specify one of the fiat currencies in the currency\\_from. In this case, the minimum payment will be calculated in this fiat currency.  You can also add field fiat\\_equivalent (optional field) to get the fiat equivalent of the minimum amount.  In the case of several outcome wallets we will calculate the minimum amount in the same way we route your payment to a specific wallet.
     * @param currencyFrom  (optional)
     * @param currencyTo  (optional)
     * @param xApiKey  (optional)
     * @return GetTheMinimumPaymentAmount200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public GetTheMinimumPaymentAmount200Response getTheMinimumPaymentAmount(String currencyFrom, String currencyTo, String xApiKey) throws ApiException {
        ApiResponse<GetTheMinimumPaymentAmount200Response> localVarResp = getTheMinimumPaymentAmountWithHttpInfo(currencyFrom, currencyTo, xApiKey);
        return localVarResp.getData();
    }

    /**
     * Get the minimum payment amount
     * Get the minimum payment amount for a specific pair.  You can provide both currencies in the pair or just currency\\_from, and we will calculate the minimum payment amount for currency\\_from and currency which you have specified as the outcome in the Store Settings.  You can also specify one of the fiat currencies in the currency\\_from. In this case, the minimum payment will be calculated in this fiat currency.  You can also add field fiat\\_equivalent (optional field) to get the fiat equivalent of the minimum amount.  In the case of several outcome wallets we will calculate the minimum amount in the same way we route your payment to a specific wallet.
     * @param currencyFrom  (optional)
     * @param currencyTo  (optional)
     * @param xApiKey  (optional)
     * @return ApiResponse&lt;GetTheMinimumPaymentAmount200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<GetTheMinimumPaymentAmount200Response> getTheMinimumPaymentAmountWithHttpInfo(String currencyFrom, String currencyTo, String xApiKey) throws ApiException {
        okhttp3.Call localVarCall = getTheMinimumPaymentAmountValidateBeforeCall(currencyFrom, currencyTo, xApiKey, null);
        Type localVarReturnType = new TypeToken<GetTheMinimumPaymentAmount200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get the minimum payment amount (asynchronously)
     * Get the minimum payment amount for a specific pair.  You can provide both currencies in the pair or just currency\\_from, and we will calculate the minimum payment amount for currency\\_from and currency which you have specified as the outcome in the Store Settings.  You can also specify one of the fiat currencies in the currency\\_from. In this case, the minimum payment will be calculated in this fiat currency.  You can also add field fiat\\_equivalent (optional field) to get the fiat equivalent of the minimum amount.  In the case of several outcome wallets we will calculate the minimum amount in the same way we route your payment to a specific wallet.
     * @param currencyFrom  (optional)
     * @param currencyTo  (optional)
     * @param xApiKey  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getTheMinimumPaymentAmountAsync(String currencyFrom, String currencyTo, String xApiKey, final ApiCallback<GetTheMinimumPaymentAmount200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getTheMinimumPaymentAmountValidateBeforeCall(currencyFrom, currencyTo, xApiKey, _callback);
        Type localVarReturnType = new TypeToken<GetTheMinimumPaymentAmount200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getUpdatePaymentEstimate
     * @param id payment ID, for which you want to get the estimate (required)
     * @param xApiKey  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * alt-svc -  <br>  * strict-transport-security -  <br>  * vary -  <br>  * x-content-type-options -  <br>  * x-dns-prefetch-control -  <br>  * x-download-options -  <br>  * x-frame-options -  <br>  * x-xss-protection -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getUpdatePaymentEstimateCall(String id, String xApiKey, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/v1/payment/{id}/update-merchant-estimate"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

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
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getUpdatePaymentEstimateValidateBeforeCall(String id, String xApiKey, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling getUpdatePaymentEstimate(Async)");
        }

        return getUpdatePaymentEstimateCall(id, xApiKey, _callback);

    }

    /**
     * Get/Update payment estimate
     * This endpoint is required to get the current estimate on the payment, and update the current estimate.   Please note! Calling this estimate before &#x60;expiration_estimate_date&#x60; will return the current estimate, it won’t be updated.  &#x60;:id&#x60; \\- payment ID, for which you want to get the estimate  Response:   &#x60;id&#x60; \\- payment ID   &#x60;token_id&#x60; - id of api key used to create this payment (please discard this parameter)   &#x60;pay_amount&#x60; - payment estimate, the exact amount the user will have to send to complete the payment   &#x60;expiration_estimate_date&#x60; - expiration date of this estimate
     * @param id payment ID, for which you want to get the estimate (required)
     * @param xApiKey  (optional)
     * @return GetUpdatePaymentEstimate200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * alt-svc -  <br>  * strict-transport-security -  <br>  * vary -  <br>  * x-content-type-options -  <br>  * x-dns-prefetch-control -  <br>  * x-download-options -  <br>  * x-frame-options -  <br>  * x-xss-protection -  <br>  </td></tr>
     </table>
     */
    public GetUpdatePaymentEstimate200Response getUpdatePaymentEstimate(String id, String xApiKey) throws ApiException {
        ApiResponse<GetUpdatePaymentEstimate200Response> localVarResp = getUpdatePaymentEstimateWithHttpInfo(id, xApiKey);
        return localVarResp.getData();
    }

    /**
     * Get/Update payment estimate
     * This endpoint is required to get the current estimate on the payment, and update the current estimate.   Please note! Calling this estimate before &#x60;expiration_estimate_date&#x60; will return the current estimate, it won’t be updated.  &#x60;:id&#x60; \\- payment ID, for which you want to get the estimate  Response:   &#x60;id&#x60; \\- payment ID   &#x60;token_id&#x60; - id of api key used to create this payment (please discard this parameter)   &#x60;pay_amount&#x60; - payment estimate, the exact amount the user will have to send to complete the payment   &#x60;expiration_estimate_date&#x60; - expiration date of this estimate
     * @param id payment ID, for which you want to get the estimate (required)
     * @param xApiKey  (optional)
     * @return ApiResponse&lt;GetUpdatePaymentEstimate200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * alt-svc -  <br>  * strict-transport-security -  <br>  * vary -  <br>  * x-content-type-options -  <br>  * x-dns-prefetch-control -  <br>  * x-download-options -  <br>  * x-frame-options -  <br>  * x-xss-protection -  <br>  </td></tr>
     </table>
     */
    public ApiResponse<GetUpdatePaymentEstimate200Response> getUpdatePaymentEstimateWithHttpInfo(String id, String xApiKey) throws ApiException {
        okhttp3.Call localVarCall = getUpdatePaymentEstimateValidateBeforeCall(id, xApiKey, null);
        Type localVarReturnType = new TypeToken<GetUpdatePaymentEstimate200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get/Update payment estimate (asynchronously)
     * This endpoint is required to get the current estimate on the payment, and update the current estimate.   Please note! Calling this estimate before &#x60;expiration_estimate_date&#x60; will return the current estimate, it won’t be updated.  &#x60;:id&#x60; \\- payment ID, for which you want to get the estimate  Response:   &#x60;id&#x60; \\- payment ID   &#x60;token_id&#x60; - id of api key used to create this payment (please discard this parameter)   &#x60;pay_amount&#x60; - payment estimate, the exact amount the user will have to send to complete the payment   &#x60;expiration_estimate_date&#x60; - expiration date of this estimate
     * @param id payment ID, for which you want to get the estimate (required)
     * @param xApiKey  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> 200 </td><td>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * alt-svc -  <br>  * strict-transport-security -  <br>  * vary -  <br>  * x-content-type-options -  <br>  * x-dns-prefetch-control -  <br>  * x-download-options -  <br>  * x-frame-options -  <br>  * x-xss-protection -  <br>  </td></tr>
     </table>
     */
    public okhttp3.Call getUpdatePaymentEstimateAsync(String id, String xApiKey, final ApiCallback<GetUpdatePaymentEstimate200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = getUpdatePaymentEstimateValidateBeforeCall(id, xApiKey, _callback);
        Type localVarReturnType = new TypeToken<GetUpdatePaymentEstimate200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
