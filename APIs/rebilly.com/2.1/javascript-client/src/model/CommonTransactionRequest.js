/**
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ContactObject from './ContactObject';
import PaymentInstruction from './PaymentInstruction';
import PaymentInstrument from './PaymentInstrument';
import RiskMetadata from './RiskMetadata';

/**
 * The CommonTransactionRequest model module.
 * @module model/CommonTransactionRequest
 * @version 2.1
 */
class CommonTransactionRequest {
    /**
     * Constructs a new <code>CommonTransactionRequest</code>.
     * @alias module:model/CommonTransactionRequest
     * @param amount {Number} The transaction amount.
     * @param currency {String} ISO 4217 alphabetic currency code.
     * @param customerId {String} The customer identifier string.
     * @param websiteId {String} The website identifier string.
     */
    constructor(amount, currency, customerId, websiteId) { 
        
        CommonTransactionRequest.initialize(this, amount, currency, customerId, websiteId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, amount, currency, customerId, websiteId) { 
        obj['amount'] = amount;
        obj['currency'] = currency;
        obj['customerId'] = customerId;
        obj['isMerchantInitiated'] = false;
        obj['isProcessedOutside'] = false;
        obj['websiteId'] = websiteId;
    }

    /**
     * Constructs a <code>CommonTransactionRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CommonTransactionRequest} obj Optional instance to populate.
     * @return {module:model/CommonTransactionRequest} The populated <code>CommonTransactionRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CommonTransactionRequest();

            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'Number');
            }
            if (data.hasOwnProperty('billingAddress')) {
                obj['billingAddress'] = ApiClient.convertToType(data['billingAddress'], ContactObject);
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('customFields')) {
                obj['customFields'] = ApiClient.convertToType(data['customFields'], Object);
            }
            if (data.hasOwnProperty('customerId')) {
                obj['customerId'] = ApiClient.convertToType(data['customerId'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('gatewayAccountId')) {
                obj['gatewayAccountId'] = ApiClient.convertToType(data['gatewayAccountId'], 'String');
            }
            if (data.hasOwnProperty('invoiceIds')) {
                obj['invoiceIds'] = ApiClient.convertToType(data['invoiceIds'], ['String']);
            }
            if (data.hasOwnProperty('isMerchantInitiated')) {
                obj['isMerchantInitiated'] = ApiClient.convertToType(data['isMerchantInitiated'], 'Boolean');
            }
            if (data.hasOwnProperty('isProcessedOutside')) {
                obj['isProcessedOutside'] = ApiClient.convertToType(data['isProcessedOutside'], 'Boolean');
            }
            if (data.hasOwnProperty('notificationUrl')) {
                obj['notificationUrl'] = ApiClient.convertToType(data['notificationUrl'], 'String');
            }
            if (data.hasOwnProperty('paymentInstruction')) {
                obj['paymentInstruction'] = ApiClient.convertToType(data['paymentInstruction'], PaymentInstruction);
            }
            if (data.hasOwnProperty('paymentInstrument')) {
                obj['paymentInstrument'] = ApiClient.convertToType(data['paymentInstrument'], PaymentInstrument);
            }
            if (data.hasOwnProperty('processedTime')) {
                obj['processedTime'] = ApiClient.convertToType(data['processedTime'], 'Date');
            }
            if (data.hasOwnProperty('redirectUrl')) {
                obj['redirectUrl'] = ApiClient.convertToType(data['redirectUrl'], 'String');
            }
            if (data.hasOwnProperty('requestId')) {
                obj['requestId'] = ApiClient.convertToType(data['requestId'], 'String');
            }
            if (data.hasOwnProperty('riskMetadata')) {
                obj['riskMetadata'] = RiskMetadata.constructFromObject(data['riskMetadata']);
            }
            if (data.hasOwnProperty('websiteId')) {
                obj['websiteId'] = ApiClient.convertToType(data['websiteId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CommonTransactionRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CommonTransactionRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CommonTransactionRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `billingAddress`
        if (data['billingAddress']) { // data not null
          ContactObject.validateJSON(data['billingAddress']);
        }
        // ensure the json data is a string
        if (data['currency'] && !(typeof data['currency'] === 'string' || data['currency'] instanceof String)) {
            throw new Error("Expected the field `currency` to be a primitive type in the JSON string but got " + data['currency']);
        }
        // ensure the json data is a string
        if (data['customerId'] && !(typeof data['customerId'] === 'string' || data['customerId'] instanceof String)) {
            throw new Error("Expected the field `customerId` to be a primitive type in the JSON string but got " + data['customerId']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['gatewayAccountId'] && !(typeof data['gatewayAccountId'] === 'string' || data['gatewayAccountId'] instanceof String)) {
            throw new Error("Expected the field `gatewayAccountId` to be a primitive type in the JSON string but got " + data['gatewayAccountId']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['invoiceIds'])) {
            throw new Error("Expected the field `invoiceIds` to be an array in the JSON data but got " + data['invoiceIds']);
        }
        // ensure the json data is a string
        if (data['notificationUrl'] && !(typeof data['notificationUrl'] === 'string' || data['notificationUrl'] instanceof String)) {
            throw new Error("Expected the field `notificationUrl` to be a primitive type in the JSON string but got " + data['notificationUrl']);
        }
        // validate the optional field `paymentInstruction`
        if (data['paymentInstruction']) { // data not null
          PaymentInstruction.validateJSON(data['paymentInstruction']);
        }
        // validate the optional field `paymentInstrument`
        if (data['paymentInstrument']) { // data not null
          PaymentInstrument.validateJSON(data['paymentInstrument']);
        }
        // ensure the json data is a string
        if (data['redirectUrl'] && !(typeof data['redirectUrl'] === 'string' || data['redirectUrl'] instanceof String)) {
            throw new Error("Expected the field `redirectUrl` to be a primitive type in the JSON string but got " + data['redirectUrl']);
        }
        // ensure the json data is a string
        if (data['requestId'] && !(typeof data['requestId'] === 'string' || data['requestId'] instanceof String)) {
            throw new Error("Expected the field `requestId` to be a primitive type in the JSON string but got " + data['requestId']);
        }
        // validate the optional field `riskMetadata`
        if (data['riskMetadata']) { // data not null
          RiskMetadata.validateJSON(data['riskMetadata']);
        }
        // ensure the json data is a string
        if (data['websiteId'] && !(typeof data['websiteId'] === 'string' || data['websiteId'] instanceof String)) {
            throw new Error("Expected the field `websiteId` to be a primitive type in the JSON string but got " + data['websiteId']);
        }

        return true;
    }


}

CommonTransactionRequest.RequiredProperties = ["amount", "currency", "customerId", "websiteId"];

/**
 * The transaction amount.
 * @member {Number} amount
 */
CommonTransactionRequest.prototype['amount'] = undefined;

/**
 * Billing address. If not supplied, we use the billing address associated with the payment instrument, and then customer.
 * @member {module:model/ContactObject} billingAddress
 */
CommonTransactionRequest.prototype['billingAddress'] = undefined;

/**
 * ISO 4217 alphabetic currency code.
 * @member {String} currency
 */
CommonTransactionRequest.prototype['currency'] = undefined;

/**
 * Custom Fields list as a map `{\"custom field name\": \"custom field value\", ...}`. The format must follow the saved format (see Custom Fields section for the formats). 
 * @member {Object} customFields
 */
CommonTransactionRequest.prototype['customFields'] = undefined;

/**
 * The customer identifier string.
 * @member {String} customerId
 */
CommonTransactionRequest.prototype['customerId'] = undefined;

/**
 * The payment description.
 * @member {String} description
 */
CommonTransactionRequest.prototype['description'] = undefined;

/**
 * Rebilly will select the appropriate payment gateway account for the transaction based on the properties of the transaction and the `gateway-account-requested` event rules configurations. If you wish to prevent Rebilly from making the gateway account selection, you may supply a gateway account id here, and it will be used instead. Only use this field if you intend to override the settings.
 * @member {String} gatewayAccountId
 */
CommonTransactionRequest.prototype['gatewayAccountId'] = undefined;

/**
 * The array of invoice identifiers.
 * @member {Array.<String>} invoiceIds
 */
CommonTransactionRequest.prototype['invoiceIds'] = undefined;

/**
 * True if the transaction was initiated by the merchant.
 * @member {Boolean} isMerchantInitiated
 * @default false
 */
CommonTransactionRequest.prototype['isMerchantInitiated'] = false;

/**
 * True if transaction was processed outside Rebilly.
 * @member {Boolean} isProcessedOutside
 * @default false
 */
CommonTransactionRequest.prototype['isProcessedOutside'] = false;

/**
 * The URL where a server-to-server notification request type `POST` with a transaction payload will be sent when the transaction's result is finalized. Do not trust the notification; follow with a `GET` request to confirm the result of the transaction. Please respond with a `2xx` HTTP status code, or we will reattempt the request again. You may use `{id}` or `{result}` as placeholders in the URL and we will replace them with the transaction's id and result accordingly. 
 * @member {String} notificationUrl
 */
CommonTransactionRequest.prototype['notificationUrl'] = undefined;

/**
 * Payment instruction. If not supplied, customer's default payment instrument will be used.
 * @member {module:model/PaymentInstruction} paymentInstruction
 */
CommonTransactionRequest.prototype['paymentInstruction'] = undefined;

/**
 * @member {module:model/PaymentInstrument} paymentInstrument
 */
CommonTransactionRequest.prototype['paymentInstrument'] = undefined;

/**
 * The time the transaction was processed. Can be specified only if transaction was processed outside Rebilly.
 * @member {Date} processedTime
 */
CommonTransactionRequest.prototype['processedTime'] = undefined;

/**
 * The URL to redirect the end-user when an offsite transaction is completed. Defaults to the website's configured URL. You may use `{id}` or `{result}` as placeholders in the URL and we will replace them with the transaction's id and result accordingly.
 * @member {String} redirectUrl
 */
CommonTransactionRequest.prototype['redirectUrl'] = undefined;

/**
 * The request id is **recommended**. It prevents duplicate transaction requests within a short period of time. If a duplicate request is sent with the same `requestId` it will be ignored to prevent double-billing anyone.  It must be unique within a 24-hour period.  We recommend generating a UUID v4 as its value.
 * @member {String} requestId
 */
CommonTransactionRequest.prototype['requestId'] = undefined;

/**
 * @member {module:model/RiskMetadata} riskMetadata
 */
CommonTransactionRequest.prototype['riskMetadata'] = undefined;

/**
 * The website identifier string.
 * @member {String} websiteId
 */
CommonTransactionRequest.prototype['websiteId'] = undefined;






export default CommonTransactionRequest;

