/**
 * NOWPayments API
 * NOWPayments is a non-custodial cryptocurrency payment processing platform. Accept payments in a wide range of cryptos and get them instantly converted into a coin of your choice and sent to your wallet. Keeping it simple – no excess.  # Sandbox  Before production usage, you can test our API using the Sandbox. Details can be found [here](https://documenter.getpostman.com/view/7907941/T1LSCRHC)  # Authentication  To use the NOWPayments API you should do the following:  *   Sign up at [nowpayments.io](https://nowpayments.io) *   Specify your outcome wallet *   Generate an API key       # Standard e-commerce flow for NOWPayments API:  1.  API - Check API availability with the [\"GET API status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#9998079f-dcc8-4e07-9ac7-3d52f0fd733a) method. If required, check the list of available payment currencies with the [\"GET available currencies\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#1c268f89-4fe7-471e-81b4-5a3153577b73) method. 2.  UI - Ask a customer to select item/items for purchase to determine the total sum; 3.  UI - Ask a customer to select payment currency 4.  API - Get the minimum payment amount for the selected currency pair (payment currency to your Outcome Wallet currency) with the [\"GET Minimum payment amount\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#41b02221-2d58-4fcf-9529-59d3763d6434) method; 5.  API - Get the estimate of the total amount in crypto with [\"GET Estimated price\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#7025cacf-7040-4c7b-a83f-f9ff0a22a822) and check that it is larger than the minimum payment amount from step 4; 6.  API - Call the [\"POST Create payment\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#5e37f3ad-0fa1-4292-af51-5c7f95730486) method to create a payment and get the deposit address (in our example, the generated BTC wallet address is returned from this method); 7.  UI - Ask a customer to send the payment to the generated deposit address (in our example, user has to send BTC coins); 8.  UI - A customer sends coins, NOWPayments processes and exchanges them (if required), and settles the payment to your Outcome Wallet (in our example, to your ETH address); 9.  API - You can get the payment status either via our IPN callbacks or manually, using [\"GET Payment Status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) and display it to a customer so that they know when their payment has been processed. 10.  API - you call the list of payments made to your account via the [\"GET List of payments\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#c8399c0e-d798-4f01-83ae-ddaa6905c2da) method. Additionally, you can see all of this information in your [Account](https://account.nowpayments.io/payments) on NOWPayments website.       ## Alternative flow  1.  API - Check API availability with the [\"GET API status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#9998079f-dcc8-4e07-9ac7-3d52f0fd733a) method. If required, check the list of available payment currencies with the [\"GET available currencies\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#1c268f89-4fe7-471e-81b4-5a3153577b73) method. 2.  UI - Ask a customer to select item/items for purchase to determine the total sum; 3.  UI - Ask a customer to select payment currency 4.  API - Get the minimum payment amount for the selected currency pair (payment currency to your Outcome Wallet currency) with the [\"GET Minimum payment amount\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#41b02221-2d58-4fcf-9529-59d3763d6434) method; 5.  API - Get the estimate of the total amount in crypto with [\"GET Estimated price\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#7025cacf-7040-4c7b-a83f-f9ff0a22a822) and check that it is larger than the minimum payment amount from step 4; 6.  API - Call the [\"POST Create Invoice](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#3e3ce25e-f43f-4636-bbd9-11560e46048b) method to create an invoice. Set \"success_url\" - parameter so that the user will be redirected to your website after successful payment. 7.  UI - display the invoice url or redirect the user to the generated link. 8.  NOWPayments - the customer completes the payment and is redirected back to your website (only if \"success_url\" parameter is configured correctly!). 9.  API - You can get the payment status either via our IPN callbacks or manually, using [\"GET Payment Status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) and display it to a customer so that they know when their payment has been processed. 10.  API - you call the list of payments made to your account via the [\"GET List of payments\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#c8399c0e-d798-4f01-83ae-ddaa6905c2da) method. Additionally, you can see all of this information in your [Account](https://account.nowpayments.io/invoices) on NOWPayments website.       # API Documentation  ## Instant Payments Notifications  IPN (Instant payment notifications, or callbacks) are used to notify you when transaction status is changed.   To use them, you should complete the following steps:  1.  Generate and save the IPN Secret key in Store Settings tab at the Dashboard. 2.  Insert your URL address where you want to get callbacks in create_payment request. The parameter name is ipn_callback_url. You will receive payment updates (statuses) to this URL address. 3.  You will receive all the parameters at the URL address you specified in (2) by POST request.       The POST request will contain the *x-nowpayments-sig* parameter in the header.       The body of the request is similiar to a [get payment status](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) response body.       Example:       {\"payment_id\":5077125051,\"payment_status\":\"waiting\",\"pay_address\":\"0xd1cDE08A07cD25adEbEd35c3867a59228C09B606\",\"price_amount\":170,\"price_currency\":\"usd\",\"pay_amount\":155.38559757,\"actually_paid\":0,\"pay_currency\":\"mana\",\"order_id\":\"2\",\"order_description\":\"Apple Macbook Pro 2019 x 1\",\"purchase_id\":\"6084744717\",\"created_at\":\"2021-04-12T14:22:54.942Z\",\"updated_at\":\"2021-04-12T14:23:06.244Z\",\"outcome_amount\":1131.7812095,\"outcome_currency\":\"trx\"} 4.  Sort all the parameters from the POST request in alphabetical order. 5.  Convert them to string using       [JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) (params, Object.keys(params).sort()) or the same function. 6.  Sign a string with an IPN-secret key with HMAC and sha-512 key 7.  Compare the signed string from the previous step with the x-nowpayments-sig , which is stored in the header of the callback request.       If these strings are similar it is a success.       Otherwise, contact us on [support@nowpayments.io](mailto:support@nowpayments.io) to solve the problem.       Example of creating a signed string at Node.JS  ``` const hmac = crypto.createHmac('sha512', notificationsKey); hmac.update(JSON.stringify(params, Object.keys(params).sort())); const signature = hmac.digest('hex');  ```  Example of comparing signed strings in PHP  ``` function check_ipn_request_is_valid()     {         $error_msg = \"Unknown error\";         $auth_ok = false;         $request_data = null;         if (isset($_SERVER['HTTP_X_NOWPAYMENTS_SIG']) && !empty($_SERVER['HTTP_X_NOWPAYMENTS_SIG'])) {             $recived_hmac = $_SERVER['HTTP_X_NOWPAYMENTS_SIG'];             $request_json = file_get_contents('php://input');             $request_data = json_decode($request_json, true);             ksort($request_data);             $sorted_request_json = json_encode($request_data, JSON_UNESCAPED_SLASHES);             if ($request_json !== false && !empty($request_json)) {                 $hmac = hash_hmac(\"sha512\", $sorted_request_json, trim($this->ipn_secret));                 if ($hmac == $recived_hmac) {                     $auth_ok = true;                 } else {                     $error_msg = 'HMAC signature does not match';                 }             } else {                 $error_msg = 'Error reading POST data';             }         } else {             $error_msg = 'No HMAC signature sent.';         }     }  ```  ## Recurrent payment notifications  If an error is detected, the payment is flagged and will receive additional recurrent notifications (number of recurrent notifications can be changed in your Store Settings-> Instant Payment Notifications).  If an error is received again during processing of the payment, recurrent notifications will be initiated again.  Example: \"Timeout\" is set to 1 minute and \"Number of recurrent notifications\" is set to 3.  Once an error is detected, you will receive 3 notifications at 1 minute intervals.  ## Several payments for one order  If you want to create several payments for one Order you should do the following:  *   Create a payment for the full order amount. *   Save \"purchase_id\" which will be in \"create_payment\" response *   Create next payment or payments with this \"purchase_id\" in \"create_payment\" request. *   **Only works for partially_paid payments**       It may be useful if you want to give your customers opportunity to pay a full order with several payments, for example, one part in BTC and one part in ETH. Also, if your customer accidentally paid you only part of a full amount, you can automatically ask them to make another payment.  ## Packages  Please find our out-of-the box packages for easy integration below:  [JavaScript package](https://www.npmjs.com/package/@nowpaymentsio/nowpayments-api-js)  \\[PHP package\\]   ([https://packagist.org/packages/nowpayments/nowpayments-api-php](https://packagist.org/packages/nowpayments/nowpayments-api-php))  More coming soon!  ## Payments
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import DeleteRecurringPayment200Response from './model/DeleteRecurringPayment200Response';
import GetAllTransfers200Response from './model/GetAllTransfers200Response';
import GetAllTransfers200ResponseResultInner from './model/GetAllTransfers200ResponseResultInner';
import GetEstimatedPrice200Response from './model/GetEstimatedPrice200Response';
import GetListOfPayments200Response from './model/GetListOfPayments200Response';
import GetListOfPayments200ResponseDataInner from './model/GetListOfPayments200ResponseDataInner';
import GetManyPlans200Response from './model/GetManyPlans200Response';
import GetManyPlans200ResponseResultInner from './model/GetManyPlans200ResponseResultInner';
import GetManyRecurringPayments200Response from './model/GetManyRecurringPayments200Response';
import GetManyRecurringPayments200ResponseResultInner from './model/GetManyRecurringPayments200ResponseResultInner';
import GetManyRecurringPayments200ResponseResultInnerSubscriber from './model/GetManyRecurringPayments200ResponseResultInnerSubscriber';
import GetOnePlan200Response from './model/GetOnePlan200Response';
import GetOnePlan200ResponseResult from './model/GetOnePlan200ResponseResult';
import GetOnePlan404Response from './model/GetOnePlan404Response';
import GetOneRecurringPayment200Response from './model/GetOneRecurringPayment200Response';
import GetOneRecurringPayment200ResponseResult from './model/GetOneRecurringPayment200ResponseResult';
import GetOneRecurringPayment200ResponseResultSubscriber from './model/GetOneRecurringPayment200ResponseResultSubscriber';
import GetOneRecurringPayment404Response from './model/GetOneRecurringPayment404Response';
import GetPaymentStatus200Response from './model/GetPaymentStatus200Response';
import GetSubPartnerBalance200Response from './model/GetSubPartnerBalance200Response';
import GetSubPartnerBalance200ResponseResult from './model/GetSubPartnerBalance200ResponseResult';
import GetSubPartnerBalance200ResponseResultBalances from './model/GetSubPartnerBalance200ResponseResultBalances';
import GetSubPartnerBalance200ResponseResultBalancesUsddtrc20 from './model/GetSubPartnerBalance200ResponseResultBalancesUsddtrc20';
import GetSubPartnerBalance200ResponseResultBalancesUsdtbsc from './model/GetSubPartnerBalance200ResponseResultBalancesUsdtbsc';
import GetTheMinimumPaymentAmount200Response from './model/GetTheMinimumPaymentAmount200Response';
import GetTransfer200Response from './model/GetTransfer200Response';
import GetTransfer200ResponseResult from './model/GetTransfer200ResponseResult';
import GetUpdatePaymentEstimate200Response from './model/GetUpdatePaymentEstimate200Response';
import UpdatePlanRequest from './model/UpdatePlanRequest';
import VerifyPayoutRequest from './model/VerifyPayoutRequest';
import BillingSubPartnerAPIApi from './api/BillingSubPartnerAPIApi';
import PaymentsAPIApi from './api/PaymentsAPIApi';
import PayoutsAPIApi from './api/PayoutsAPIApi';
import RecurringPaymentsAPIEmailSubscriptionsFeatureApi from './api/RecurringPaymentsAPIEmailSubscriptionsFeatureApi';


/**
* NOWPayments is a non-custodial cryptocurrency payment processing platform. Accept payments in a wide range of cryptos and get them instantly converted into a coin of your choice and sent to your wallet. Keeping it simple – no excess.  # Sandbox  Before production usage, you can test our API using the Sandbox. Details can be found [here](https://documenter.getpostman.com/view/7907941/T1LSCRHC)  # Authentication  To use the NOWPayments API you should do the following:  *   Sign up at [nowpayments.io](https://nowpayments.io) *   Specify your outcome wallet *   Generate an API key       # Standard e-commerce flow for NOWPayments API:  1.  API - Check API availability with the [\&quot;GET API status\&quot;](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#9998079f-dcc8-4e07-9ac7-3d52f0fd733a) method. If required, check the list of available payment currencies with the [\&quot;GET available currencies\&quot;](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#1c268f89-4fe7-471e-81b4-5a3153577b73) method. 2.  UI - Ask a customer to select item/items for purchase to determine the total sum; 3.  UI - Ask a customer to select payment currency 4.  API - Get the minimum payment amount for the selected currency pair (payment currency to your Outcome Wallet currency) with the [\&quot;GET Minimum payment amount\&quot;](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#41b02221-2d58-4fcf-9529-59d3763d6434) method; 5.  API - Get the estimate of the total amount in crypto with [\&quot;GET Estimated price\&quot;](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#7025cacf-7040-4c7b-a83f-f9ff0a22a822) and check that it is larger than the minimum payment amount from step 4; 6.  API - Call the [\&quot;POST Create payment\&quot;](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#5e37f3ad-0fa1-4292-af51-5c7f95730486) method to create a payment and get the deposit address (in our example, the generated BTC wallet address is returned from this method); 7.  UI - Ask a customer to send the payment to the generated deposit address (in our example, user has to send BTC coins); 8.  UI - A customer sends coins, NOWPayments processes and exchanges them (if required), and settles the payment to your Outcome Wallet (in our example, to your ETH address); 9.  API - You can get the payment status either via our IPN callbacks or manually, using [\&quot;GET Payment Status\&quot;](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#0b77a8e3-2344-4760-a0bd-247da067db6d) and display it to a customer so that they know when their payment has been processed. 10.  API - you call the list of payments made to your account via the [\&quot;GET List of payments\&quot;](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#c8399c0e-d798-4f01-83ae-ddaa6905c2da) method. Additionally, you can see all of this information in your [Account](https://account.nowpayments.io/payments) on NOWPayments website.       ## Alternative flow  1.  API - Check API availability with the [\&quot;GET API status\&quot;](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#9998079f-dcc8-4e07-9ac7-3d52f0fd733a) method. If required, check the list of available payment currencies with the [\&quot;GET available currencies\&quot;](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#1c268f89-4fe7-471e-81b4-5a3153577b73) method. 2.  UI - Ask a customer to select item/items for purchase to determine the total sum; 3.  UI - Ask a customer to select payment currency 4.  API - Get the minimum payment amount for the selected currency pair (payment currency to your Outcome Wallet currency) with the [\&quot;GET Minimum payment amount\&quot;](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#41b02221-2d58-4fcf-9529-59d3763d6434) method; 5.  API - Get the estimate of the total amount in crypto with [\&quot;GET Estimated price\&quot;](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#7025cacf-7040-4c7b-a83f-f9ff0a22a822) and check that it is larger than the minimum payment amount from step 4; 6.  API - Call the [\&quot;POST Create Invoice](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#3e3ce25e-f43f-4636-bbd9-11560e46048b) method to create an invoice. Set \&quot;success_url\&quot; - parameter so that the user will be redirected to your website after successful payment. 7.  UI - display the invoice url or redirect the user to the generated link. 8.  NOWPayments - the customer completes the payment and is redirected back to your website (only if \&quot;success_url\&quot; parameter is configured correctly!). 9.  API - You can get the payment status either via our IPN callbacks or manually, using [\&quot;GET Payment Status\&quot;](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#0b77a8e3-2344-4760-a0bd-247da067db6d) and display it to a customer so that they know when their payment has been processed. 10.  API - you call the list of payments made to your account via the [\&quot;GET List of payments\&quot;](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#c8399c0e-d798-4f01-83ae-ddaa6905c2da) method. Additionally, you can see all of this information in your [Account](https://account.nowpayments.io/invoices) on NOWPayments website.       # API Documentation  ## Instant Payments Notifications  IPN (Instant payment notifications, or callbacks) are used to notify you when transaction status is changed.   To use them, you should complete the following steps:  1.  Generate and save the IPN Secret key in Store Settings tab at the Dashboard. 2.  Insert your URL address where you want to get callbacks in create_payment request. The parameter name is ipn_callback_url. You will receive payment updates (statuses) to this URL address. 3.  You will receive all the parameters at the URL address you specified in (2) by POST request.       The POST request will contain the *x-nowpayments-sig* parameter in the header.       The body of the request is similiar to a [get payment status](https://documenter.getpostman.com/view/7907941/S1a32n38?version&#x3D;latest#0b77a8e3-2344-4760-a0bd-247da067db6d) response body.       Example:       {\&quot;payment_id\&quot;:5077125051,\&quot;payment_status\&quot;:\&quot;waiting\&quot;,\&quot;pay_address\&quot;:\&quot;0xd1cDE08A07cD25adEbEd35c3867a59228C09B606\&quot;,\&quot;price_amount\&quot;:170,\&quot;price_currency\&quot;:\&quot;usd\&quot;,\&quot;pay_amount\&quot;:155.38559757,\&quot;actually_paid\&quot;:0,\&quot;pay_currency\&quot;:\&quot;mana\&quot;,\&quot;order_id\&quot;:\&quot;2\&quot;,\&quot;order_description\&quot;:\&quot;Apple Macbook Pro 2019 x 1\&quot;,\&quot;purchase_id\&quot;:\&quot;6084744717\&quot;,\&quot;created_at\&quot;:\&quot;2021-04-12T14:22:54.942Z\&quot;,\&quot;updated_at\&quot;:\&quot;2021-04-12T14:23:06.244Z\&quot;,\&quot;outcome_amount\&quot;:1131.7812095,\&quot;outcome_currency\&quot;:\&quot;trx\&quot;} 4.  Sort all the parameters from the POST request in alphabetical order. 5.  Convert them to string using       [JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) (params, Object.keys(params).sort()) or the same function. 6.  Sign a string with an IPN-secret key with HMAC and sha-512 key 7.  Compare the signed string from the previous step with the x-nowpayments-sig , which is stored in the header of the callback request.       If these strings are similar it is a success.       Otherwise, contact us on [support@nowpayments.io](mailto:support@nowpayments.io) to solve the problem.       Example of creating a signed string at Node.JS  &#x60;&#x60;&#x60; const hmac &#x3D; crypto.createHmac(&#39;sha512&#39;, notificationsKey); hmac.update(JSON.stringify(params, Object.keys(params).sort())); const signature &#x3D; hmac.digest(&#39;hex&#39;);  &#x60;&#x60;&#x60;  Example of comparing signed strings in PHP  &#x60;&#x60;&#x60; function check_ipn_request_is_valid()     {         $error_msg &#x3D; \&quot;Unknown error\&quot;;         $auth_ok &#x3D; false;         $request_data &#x3D; null;         if (isset($_SERVER[&#39;HTTP_X_NOWPAYMENTS_SIG&#39;]) &amp;&amp; !empty($_SERVER[&#39;HTTP_X_NOWPAYMENTS_SIG&#39;])) {             $recived_hmac &#x3D; $_SERVER[&#39;HTTP_X_NOWPAYMENTS_SIG&#39;];             $request_json &#x3D; file_get_contents(&#39;php://input&#39;);             $request_data &#x3D; json_decode($request_json, true);             ksort($request_data);             $sorted_request_json &#x3D; json_encode($request_data, JSON_UNESCAPED_SLASHES);             if ($request_json !&#x3D;&#x3D; false &amp;&amp; !empty($request_json)) {                 $hmac &#x3D; hash_hmac(\&quot;sha512\&quot;, $sorted_request_json, trim($this-&gt;ipn_secret));                 if ($hmac &#x3D;&#x3D; $recived_hmac) {                     $auth_ok &#x3D; true;                 } else {                     $error_msg &#x3D; &#39;HMAC signature does not match&#39;;                 }             } else {                 $error_msg &#x3D; &#39;Error reading POST data&#39;;             }         } else {             $error_msg &#x3D; &#39;No HMAC signature sent.&#39;;         }     }  &#x60;&#x60;&#x60;  ## Recurrent payment notifications  If an error is detected, the payment is flagged and will receive additional recurrent notifications (number of recurrent notifications can be changed in your Store Settings-&gt; Instant Payment Notifications).  If an error is received again during processing of the payment, recurrent notifications will be initiated again.  Example: \&quot;Timeout\&quot; is set to 1 minute and \&quot;Number of recurrent notifications\&quot; is set to 3.  Once an error is detected, you will receive 3 notifications at 1 minute intervals.  ## Several payments for one order  If you want to create several payments for one Order you should do the following:  *   Create a payment for the full order amount. *   Save \&quot;purchase_id\&quot; which will be in \&quot;create_payment\&quot; response *   Create next payment or payments with this \&quot;purchase_id\&quot; in \&quot;create_payment\&quot; request. *   **Only works for partially_paid payments**       It may be useful if you want to give your customers opportunity to pay a full order with several payments, for example, one part in BTC and one part in ETH. Also, if your customer accidentally paid you only part of a full amount, you can automatically ask them to make another payment.  ## Packages  Please find our out-of-the box packages for easy integration below:  [JavaScript package](https://www.npmjs.com/package/@nowpaymentsio/nowpayments-api-js)  \\[PHP package\\]   ([https://packagist.org/packages/nowpayments/nowpayments-api-php](https://packagist.org/packages/nowpayments/nowpayments-api-php))  More coming soon!  ## Payments.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var NowPaymentsApi = require('index'); // See note below*.
* var xxxSvc = new NowPaymentsApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new NowPaymentsApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new NowPaymentsApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new NowPaymentsApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The DeleteRecurringPayment200Response model constructor.
     * @property {module:model/DeleteRecurringPayment200Response}
     */
    DeleteRecurringPayment200Response,

    /**
     * The GetAllTransfers200Response model constructor.
     * @property {module:model/GetAllTransfers200Response}
     */
    GetAllTransfers200Response,

    /**
     * The GetAllTransfers200ResponseResultInner model constructor.
     * @property {module:model/GetAllTransfers200ResponseResultInner}
     */
    GetAllTransfers200ResponseResultInner,

    /**
     * The GetEstimatedPrice200Response model constructor.
     * @property {module:model/GetEstimatedPrice200Response}
     */
    GetEstimatedPrice200Response,

    /**
     * The GetListOfPayments200Response model constructor.
     * @property {module:model/GetListOfPayments200Response}
     */
    GetListOfPayments200Response,

    /**
     * The GetListOfPayments200ResponseDataInner model constructor.
     * @property {module:model/GetListOfPayments200ResponseDataInner}
     */
    GetListOfPayments200ResponseDataInner,

    /**
     * The GetManyPlans200Response model constructor.
     * @property {module:model/GetManyPlans200Response}
     */
    GetManyPlans200Response,

    /**
     * The GetManyPlans200ResponseResultInner model constructor.
     * @property {module:model/GetManyPlans200ResponseResultInner}
     */
    GetManyPlans200ResponseResultInner,

    /**
     * The GetManyRecurringPayments200Response model constructor.
     * @property {module:model/GetManyRecurringPayments200Response}
     */
    GetManyRecurringPayments200Response,

    /**
     * The GetManyRecurringPayments200ResponseResultInner model constructor.
     * @property {module:model/GetManyRecurringPayments200ResponseResultInner}
     */
    GetManyRecurringPayments200ResponseResultInner,

    /**
     * The GetManyRecurringPayments200ResponseResultInnerSubscriber model constructor.
     * @property {module:model/GetManyRecurringPayments200ResponseResultInnerSubscriber}
     */
    GetManyRecurringPayments200ResponseResultInnerSubscriber,

    /**
     * The GetOnePlan200Response model constructor.
     * @property {module:model/GetOnePlan200Response}
     */
    GetOnePlan200Response,

    /**
     * The GetOnePlan200ResponseResult model constructor.
     * @property {module:model/GetOnePlan200ResponseResult}
     */
    GetOnePlan200ResponseResult,

    /**
     * The GetOnePlan404Response model constructor.
     * @property {module:model/GetOnePlan404Response}
     */
    GetOnePlan404Response,

    /**
     * The GetOneRecurringPayment200Response model constructor.
     * @property {module:model/GetOneRecurringPayment200Response}
     */
    GetOneRecurringPayment200Response,

    /**
     * The GetOneRecurringPayment200ResponseResult model constructor.
     * @property {module:model/GetOneRecurringPayment200ResponseResult}
     */
    GetOneRecurringPayment200ResponseResult,

    /**
     * The GetOneRecurringPayment200ResponseResultSubscriber model constructor.
     * @property {module:model/GetOneRecurringPayment200ResponseResultSubscriber}
     */
    GetOneRecurringPayment200ResponseResultSubscriber,

    /**
     * The GetOneRecurringPayment404Response model constructor.
     * @property {module:model/GetOneRecurringPayment404Response}
     */
    GetOneRecurringPayment404Response,

    /**
     * The GetPaymentStatus200Response model constructor.
     * @property {module:model/GetPaymentStatus200Response}
     */
    GetPaymentStatus200Response,

    /**
     * The GetSubPartnerBalance200Response model constructor.
     * @property {module:model/GetSubPartnerBalance200Response}
     */
    GetSubPartnerBalance200Response,

    /**
     * The GetSubPartnerBalance200ResponseResult model constructor.
     * @property {module:model/GetSubPartnerBalance200ResponseResult}
     */
    GetSubPartnerBalance200ResponseResult,

    /**
     * The GetSubPartnerBalance200ResponseResultBalances model constructor.
     * @property {module:model/GetSubPartnerBalance200ResponseResultBalances}
     */
    GetSubPartnerBalance200ResponseResultBalances,

    /**
     * The GetSubPartnerBalance200ResponseResultBalancesUsddtrc20 model constructor.
     * @property {module:model/GetSubPartnerBalance200ResponseResultBalancesUsddtrc20}
     */
    GetSubPartnerBalance200ResponseResultBalancesUsddtrc20,

    /**
     * The GetSubPartnerBalance200ResponseResultBalancesUsdtbsc model constructor.
     * @property {module:model/GetSubPartnerBalance200ResponseResultBalancesUsdtbsc}
     */
    GetSubPartnerBalance200ResponseResultBalancesUsdtbsc,

    /**
     * The GetTheMinimumPaymentAmount200Response model constructor.
     * @property {module:model/GetTheMinimumPaymentAmount200Response}
     */
    GetTheMinimumPaymentAmount200Response,

    /**
     * The GetTransfer200Response model constructor.
     * @property {module:model/GetTransfer200Response}
     */
    GetTransfer200Response,

    /**
     * The GetTransfer200ResponseResult model constructor.
     * @property {module:model/GetTransfer200ResponseResult}
     */
    GetTransfer200ResponseResult,

    /**
     * The GetUpdatePaymentEstimate200Response model constructor.
     * @property {module:model/GetUpdatePaymentEstimate200Response}
     */
    GetUpdatePaymentEstimate200Response,

    /**
     * The UpdatePlanRequest model constructor.
     * @property {module:model/UpdatePlanRequest}
     */
    UpdatePlanRequest,

    /**
     * The VerifyPayoutRequest model constructor.
     * @property {module:model/VerifyPayoutRequest}
     */
    VerifyPayoutRequest,

    /**
    * The BillingSubPartnerAPIApi service constructor.
    * @property {module:api/BillingSubPartnerAPIApi}
    */
    BillingSubPartnerAPIApi,

    /**
    * The PaymentsAPIApi service constructor.
    * @property {module:api/PaymentsAPIApi}
    */
    PaymentsAPIApi,

    /**
    * The PayoutsAPIApi service constructor.
    * @property {module:api/PayoutsAPIApi}
    */
    PayoutsAPIApi,

    /**
    * The RecurringPaymentsAPIEmailSubscriptionsFeatureApi service constructor.
    * @property {module:api/RecurringPaymentsAPIEmailSubscriptionsFeatureApi}
    */
    RecurringPaymentsAPIEmailSubscriptionsFeatureApi
};
