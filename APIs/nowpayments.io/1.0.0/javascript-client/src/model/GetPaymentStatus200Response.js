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

import ApiClient from '../ApiClient';

/**
 * The GetPaymentStatus200Response model module.
 * @module model/GetPaymentStatus200Response
 * @version 1.0.0
 */
class GetPaymentStatus200Response {
    /**
     * Constructs a new <code>GetPaymentStatus200Response</code>.
     * @alias module:model/GetPaymentStatus200Response
     */
    constructor() { 
        
        GetPaymentStatus200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetPaymentStatus200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetPaymentStatus200Response} obj Optional instance to populate.
     * @return {module:model/GetPaymentStatus200Response} The populated <code>GetPaymentStatus200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetPaymentStatus200Response();

            if (data.hasOwnProperty('actually_paid')) {
                obj['actually_paid'] = ApiClient.convertToType(data['actually_paid'], 'Number');
            }
            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'String');
            }
            if (data.hasOwnProperty('order_description')) {
                obj['order_description'] = ApiClient.convertToType(data['order_description'], 'String');
            }
            if (data.hasOwnProperty('order_id')) {
                obj['order_id'] = ApiClient.convertToType(data['order_id'], 'String');
            }
            if (data.hasOwnProperty('outcome_amount')) {
                obj['outcome_amount'] = ApiClient.convertToType(data['outcome_amount'], 'Number');
            }
            if (data.hasOwnProperty('outcome_currency')) {
                obj['outcome_currency'] = ApiClient.convertToType(data['outcome_currency'], 'String');
            }
            if (data.hasOwnProperty('pay_address')) {
                obj['pay_address'] = ApiClient.convertToType(data['pay_address'], 'String');
            }
            if (data.hasOwnProperty('pay_amount')) {
                obj['pay_amount'] = ApiClient.convertToType(data['pay_amount'], 'Number');
            }
            if (data.hasOwnProperty('pay_currency')) {
                obj['pay_currency'] = ApiClient.convertToType(data['pay_currency'], 'String');
            }
            if (data.hasOwnProperty('payment_id')) {
                obj['payment_id'] = ApiClient.convertToType(data['payment_id'], 'Number');
            }
            if (data.hasOwnProperty('payment_status')) {
                obj['payment_status'] = ApiClient.convertToType(data['payment_status'], 'String');
            }
            if (data.hasOwnProperty('price_amount')) {
                obj['price_amount'] = ApiClient.convertToType(data['price_amount'], 'Number');
            }
            if (data.hasOwnProperty('price_currency')) {
                obj['price_currency'] = ApiClient.convertToType(data['price_currency'], 'String');
            }
            if (data.hasOwnProperty('purchase_id')) {
                obj['purchase_id'] = ApiClient.convertToType(data['purchase_id'], 'String');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetPaymentStatus200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetPaymentStatus200Response</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['created_at'] && !(typeof data['created_at'] === 'string' || data['created_at'] instanceof String)) {
            throw new Error("Expected the field `created_at` to be a primitive type in the JSON string but got " + data['created_at']);
        }
        // ensure the json data is a string
        if (data['order_description'] && !(typeof data['order_description'] === 'string' || data['order_description'] instanceof String)) {
            throw new Error("Expected the field `order_description` to be a primitive type in the JSON string but got " + data['order_description']);
        }
        // ensure the json data is a string
        if (data['order_id'] && !(typeof data['order_id'] === 'string' || data['order_id'] instanceof String)) {
            throw new Error("Expected the field `order_id` to be a primitive type in the JSON string but got " + data['order_id']);
        }
        // ensure the json data is a string
        if (data['outcome_currency'] && !(typeof data['outcome_currency'] === 'string' || data['outcome_currency'] instanceof String)) {
            throw new Error("Expected the field `outcome_currency` to be a primitive type in the JSON string but got " + data['outcome_currency']);
        }
        // ensure the json data is a string
        if (data['pay_address'] && !(typeof data['pay_address'] === 'string' || data['pay_address'] instanceof String)) {
            throw new Error("Expected the field `pay_address` to be a primitive type in the JSON string but got " + data['pay_address']);
        }
        // ensure the json data is a string
        if (data['pay_currency'] && !(typeof data['pay_currency'] === 'string' || data['pay_currency'] instanceof String)) {
            throw new Error("Expected the field `pay_currency` to be a primitive type in the JSON string but got " + data['pay_currency']);
        }
        // ensure the json data is a string
        if (data['payment_status'] && !(typeof data['payment_status'] === 'string' || data['payment_status'] instanceof String)) {
            throw new Error("Expected the field `payment_status` to be a primitive type in the JSON string but got " + data['payment_status']);
        }
        // ensure the json data is a string
        if (data['price_currency'] && !(typeof data['price_currency'] === 'string' || data['price_currency'] instanceof String)) {
            throw new Error("Expected the field `price_currency` to be a primitive type in the JSON string but got " + data['price_currency']);
        }
        // ensure the json data is a string
        if (data['purchase_id'] && !(typeof data['purchase_id'] === 'string' || data['purchase_id'] instanceof String)) {
            throw new Error("Expected the field `purchase_id` to be a primitive type in the JSON string but got " + data['purchase_id']);
        }
        // ensure the json data is a string
        if (data['updated_at'] && !(typeof data['updated_at'] === 'string' || data['updated_at'] instanceof String)) {
            throw new Error("Expected the field `updated_at` to be a primitive type in the JSON string but got " + data['updated_at']);
        }

        return true;
    }


}



/**
 * @member {Number} actually_paid
 */
GetPaymentStatus200Response.prototype['actually_paid'] = undefined;

/**
 * @member {String} created_at
 */
GetPaymentStatus200Response.prototype['created_at'] = undefined;

/**
 * @member {String} order_description
 */
GetPaymentStatus200Response.prototype['order_description'] = undefined;

/**
 * @member {String} order_id
 */
GetPaymentStatus200Response.prototype['order_id'] = undefined;

/**
 * @member {Number} outcome_amount
 */
GetPaymentStatus200Response.prototype['outcome_amount'] = undefined;

/**
 * @member {String} outcome_currency
 */
GetPaymentStatus200Response.prototype['outcome_currency'] = undefined;

/**
 * @member {String} pay_address
 */
GetPaymentStatus200Response.prototype['pay_address'] = undefined;

/**
 * @member {Number} pay_amount
 */
GetPaymentStatus200Response.prototype['pay_amount'] = undefined;

/**
 * @member {String} pay_currency
 */
GetPaymentStatus200Response.prototype['pay_currency'] = undefined;

/**
 * @member {Number} payment_id
 */
GetPaymentStatus200Response.prototype['payment_id'] = undefined;

/**
 * @member {String} payment_status
 */
GetPaymentStatus200Response.prototype['payment_status'] = undefined;

/**
 * @member {Number} price_amount
 */
GetPaymentStatus200Response.prototype['price_amount'] = undefined;

/**
 * @member {String} price_currency
 */
GetPaymentStatus200Response.prototype['price_currency'] = undefined;

/**
 * @member {String} purchase_id
 */
GetPaymentStatus200Response.prototype['purchase_id'] = undefined;

/**
 * @member {String} updated_at
 */
GetPaymentStatus200Response.prototype['updated_at'] = undefined;






export default GetPaymentStatus200Response;

