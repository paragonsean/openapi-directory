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
import GatewayName from './GatewayName';
import InstrumentReference from './InstrumentReference';
import ThreeDSecureResult from './ThreeDSecureResult';

/**
 * The CommonTransaction model module.
 * @module model/CommonTransaction
 * @version 2.1
 */
class CommonTransaction {
    /**
     * Constructs a new <code>CommonTransaction</code>.
     * @alias module:model/CommonTransaction
     */
    constructor() { 
        
        CommonTransaction.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CommonTransaction</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CommonTransaction} obj Optional instance to populate.
     * @return {module:model/CommonTransaction} The populated <code>CommonTransaction</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CommonTransaction();

            if (data.hasOwnProperty('3ds')) {
                obj['3ds'] = ApiClient.convertToType(data['3ds'], ThreeDSecureResult);
            }
            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'Number');
            }
            if (data.hasOwnProperty('billingAddress')) {
                obj['billingAddress'] = ApiClient.convertToType(data['billingAddress'], ContactObject);
            }
            if (data.hasOwnProperty('billingDescriptor')) {
                obj['billingDescriptor'] = ApiClient.convertToType(data['billingDescriptor'], 'String');
            }
            if (data.hasOwnProperty('childTransactions')) {
                obj['childTransactions'] = ApiClient.convertToType(data['childTransactions'], ['String']);
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
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
            if (data.hasOwnProperty('gatewayName')) {
                obj['gatewayName'] = ApiClient.convertToType(data['gatewayName'], GatewayName);
            }
            if (data.hasOwnProperty('has3ds')) {
                obj['has3ds'] = ApiClient.convertToType(data['has3ds'], 'Boolean');
            }
            if (data.hasOwnProperty('hasAmountAdjustment')) {
                obj['hasAmountAdjustment'] = ApiClient.convertToType(data['hasAmountAdjustment'], 'Boolean');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('invoiceIds')) {
                obj['invoiceIds'] = ApiClient.convertToType(data['invoiceIds'], ['String']);
            }
            if (data.hasOwnProperty('isRebill')) {
                obj['isRebill'] = ApiClient.convertToType(data['isRebill'], 'Boolean');
            }
            if (data.hasOwnProperty('isRetry')) {
                obj['isRetry'] = ApiClient.convertToType(data['isRetry'], 'Boolean');
            }
            if (data.hasOwnProperty('parentTransactionId')) {
                obj['parentTransactionId'] = ApiClient.convertToType(data['parentTransactionId'], 'String');
            }
            if (data.hasOwnProperty('paymentInstrument')) {
                obj['paymentInstrument'] = InstrumentReference.constructFromObject(data['paymentInstrument']);
            }
            if (data.hasOwnProperty('planIds')) {
                obj['planIds'] = ApiClient.convertToType(data['planIds'], ['String']);
            }
            if (data.hasOwnProperty('processedTime')) {
                obj['processedTime'] = ApiClient.convertToType(data['processedTime'], 'Date');
            }
            if (data.hasOwnProperty('purchaseAmount')) {
                obj['purchaseAmount'] = ApiClient.convertToType(data['purchaseAmount'], 'Number');
            }
            if (data.hasOwnProperty('purchaseCurrency')) {
                obj['purchaseCurrency'] = ApiClient.convertToType(data['purchaseCurrency'], 'String');
            }
            if (data.hasOwnProperty('rebillNumber')) {
                obj['rebillNumber'] = ApiClient.convertToType(data['rebillNumber'], 'Number');
            }
            if (data.hasOwnProperty('redirectUrl')) {
                obj['redirectUrl'] = ApiClient.convertToType(data['redirectUrl'], 'String');
            }
            if (data.hasOwnProperty('requestAmount')) {
                obj['requestAmount'] = ApiClient.convertToType(data['requestAmount'], 'Number');
            }
            if (data.hasOwnProperty('requestCurrency')) {
                obj['requestCurrency'] = ApiClient.convertToType(data['requestCurrency'], 'String');
            }
            if (data.hasOwnProperty('requestId')) {
                obj['requestId'] = ApiClient.convertToType(data['requestId'], 'String');
            }
            if (data.hasOwnProperty('result')) {
                obj['result'] = ApiClient.convertToType(data['result'], 'String');
            }
            if (data.hasOwnProperty('retryNumber')) {
                obj['retryNumber'] = ApiClient.convertToType(data['retryNumber'], 'Number');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('subscriptionIds')) {
                obj['subscriptionIds'] = ApiClient.convertToType(data['subscriptionIds'], ['String']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('updatedTime')) {
                obj['updatedTime'] = ApiClient.convertToType(data['updatedTime'], 'Date');
            }
            if (data.hasOwnProperty('websiteId')) {
                obj['websiteId'] = ApiClient.convertToType(data['websiteId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CommonTransaction</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CommonTransaction</code>.
     */
    static validateJSON(data) {
        // validate the optional field `3ds`
        if (data['3ds']) { // data not null
          ThreeDSecureResult.validateJSON(data['3ds']);
        }
        // validate the optional field `billingAddress`
        if (data['billingAddress']) { // data not null
          ContactObject.validateJSON(data['billingAddress']);
        }
        // ensure the json data is a string
        if (data['billingDescriptor'] && !(typeof data['billingDescriptor'] === 'string' || data['billingDescriptor'] instanceof String)) {
            throw new Error("Expected the field `billingDescriptor` to be a primitive type in the JSON string but got " + data['billingDescriptor']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['childTransactions'])) {
            throw new Error("Expected the field `childTransactions` to be an array in the JSON data but got " + data['childTransactions']);
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
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['invoiceIds'])) {
            throw new Error("Expected the field `invoiceIds` to be an array in the JSON data but got " + data['invoiceIds']);
        }
        // ensure the json data is a string
        if (data['parentTransactionId'] && !(typeof data['parentTransactionId'] === 'string' || data['parentTransactionId'] instanceof String)) {
            throw new Error("Expected the field `parentTransactionId` to be a primitive type in the JSON string but got " + data['parentTransactionId']);
        }
        // validate the optional field `paymentInstrument`
        if (data['paymentInstrument']) { // data not null
          InstrumentReference.validateJSON(data['paymentInstrument']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['planIds'])) {
            throw new Error("Expected the field `planIds` to be an array in the JSON data but got " + data['planIds']);
        }
        // ensure the json data is a string
        if (data['purchaseCurrency'] && !(typeof data['purchaseCurrency'] === 'string' || data['purchaseCurrency'] instanceof String)) {
            throw new Error("Expected the field `purchaseCurrency` to be a primitive type in the JSON string but got " + data['purchaseCurrency']);
        }
        // ensure the json data is a string
        if (data['redirectUrl'] && !(typeof data['redirectUrl'] === 'string' || data['redirectUrl'] instanceof String)) {
            throw new Error("Expected the field `redirectUrl` to be a primitive type in the JSON string but got " + data['redirectUrl']);
        }
        // ensure the json data is a string
        if (data['requestCurrency'] && !(typeof data['requestCurrency'] === 'string' || data['requestCurrency'] instanceof String)) {
            throw new Error("Expected the field `requestCurrency` to be a primitive type in the JSON string but got " + data['requestCurrency']);
        }
        // ensure the json data is a string
        if (data['requestId'] && !(typeof data['requestId'] === 'string' || data['requestId'] instanceof String)) {
            throw new Error("Expected the field `requestId` to be a primitive type in the JSON string but got " + data['requestId']);
        }
        // ensure the json data is a string
        if (data['result'] && !(typeof data['result'] === 'string' || data['result'] instanceof String)) {
            throw new Error("Expected the field `result` to be a primitive type in the JSON string but got " + data['result']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['subscriptionIds'])) {
            throw new Error("Expected the field `subscriptionIds` to be an array in the JSON data but got " + data['subscriptionIds']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // ensure the json data is a string
        if (data['websiteId'] && !(typeof data['websiteId'] === 'string' || data['websiteId'] instanceof String)) {
            throw new Error("Expected the field `websiteId` to be a primitive type in the JSON string but got " + data['websiteId']);
        }

        return true;
    }


}



/**
 * @member {module:model/ThreeDSecureResult} 3ds
 */
CommonTransaction.prototype['3ds'] = undefined;

/**
 * The transaction's amount.
 * @member {Number} amount
 */
CommonTransaction.prototype['amount'] = undefined;

/**
 * Billing address.
 * @member {module:model/ContactObject} billingAddress
 */
CommonTransaction.prototype['billingAddress'] = undefined;

/**
 * The billing descriptor that appears on the periodic billing statement. Commonly 12 or fewer characters for a credit card statement. 
 * @member {String} billingDescriptor
 */
CommonTransaction.prototype['billingDescriptor'] = undefined;

/**
 * The child transaction IDs.
 * @member {Array.<String>} childTransactions
 */
CommonTransaction.prototype['childTransactions'] = undefined;

/**
 * Transaction created time.
 * @member {Date} createdTime
 */
CommonTransaction.prototype['createdTime'] = undefined;

/**
 * ISO 4217 alphabetic currency code.
 * @member {String} currency
 */
CommonTransaction.prototype['currency'] = undefined;

/**
 * Custom Fields list as a map `{\"custom field name\": \"custom field value\", ...}`. The format must follow the saved format (see Custom Fields section for the formats). 
 * @member {Object} customFields
 */
CommonTransaction.prototype['customFields'] = undefined;

/**
 * The сustomer's ID.
 * @member {String} customerId
 */
CommonTransaction.prototype['customerId'] = undefined;

/**
 * The payment description.
 * @member {String} description
 */
CommonTransaction.prototype['description'] = undefined;

/**
 * Payment Gateway name, available only after the gateway is selected for the transaction. 
 * @member {module:model/GatewayName} gatewayName
 */
CommonTransaction.prototype['gatewayName'] = undefined;

/**
 * @member {Boolean} has3ds
 */
CommonTransaction.prototype['has3ds'] = undefined;

/**
 * True if transaction has amount adjustment.
 * @member {Boolean} hasAmountAdjustment
 */
CommonTransaction.prototype['hasAmountAdjustment'] = undefined;

/**
 * The transaction ID.
 * @member {String} id
 */
CommonTransaction.prototype['id'] = undefined;

/**
 * The invoice IDs related to transaction.
 * @member {Array.<String>} invoiceIds
 */
CommonTransaction.prototype['invoiceIds'] = undefined;

/**
 * @member {Boolean} isRebill
 */
CommonTransaction.prototype['isRebill'] = undefined;

/**
 * True if this transaction is retry.
 * @member {Boolean} isRetry
 */
CommonTransaction.prototype['isRetry'] = undefined;

/**
 * The parent's transaction ID.
 * @member {String} parentTransactionId
 */
CommonTransaction.prototype['parentTransactionId'] = undefined;

/**
 * @member {module:model/InstrumentReference} paymentInstrument
 */
CommonTransaction.prototype['paymentInstrument'] = undefined;

/**
 * The plan IDs related to transaction's order(s).
 * @member {Array.<String>} planIds
 */
CommonTransaction.prototype['planIds'] = undefined;

/**
 * Transaction processed time.
 * @member {Date} processedTime
 */
CommonTransaction.prototype['processedTime'] = undefined;

/**
 * The amount actually purchased which may have differed from the originally requested amount in case of an adjustment.
 * @member {Number} purchaseAmount
 */
CommonTransaction.prototype['purchaseAmount'] = undefined;

/**
 * ISO 4217 alphabetic currency code.
 * @member {String} purchaseCurrency
 */
CommonTransaction.prototype['purchaseCurrency'] = undefined;

/**
 * The transaction's rebill number.
 * @member {Number} rebillNumber
 */
CommonTransaction.prototype['rebillNumber'] = undefined;

/**
 * The URL to redirect the end-user when an offsite transaction is completed. Defaults to the website's configured URL.
 * @member {String} redirectUrl
 */
CommonTransaction.prototype['redirectUrl'] = undefined;

/**
 * The amount in the payment request. If adjusted, the purchase amount and billing amount may vary from it.
 * @member {Number} requestAmount
 */
CommonTransaction.prototype['requestAmount'] = undefined;

/**
 * ISO 4217 alphabetic currency code.
 * @member {String} requestCurrency
 */
CommonTransaction.prototype['requestCurrency'] = undefined;

/**
 * The transaction's request ID.  This ID must be unique within a 24 hour period. Use this field to prevent duplicated transactions.
 * @member {String} requestId
 */
CommonTransaction.prototype['requestId'] = undefined;

/**
 * Transaction result.
 * @member {module:model/CommonTransaction.ResultEnum} result
 */
CommonTransaction.prototype['result'] = undefined;

/**
 * The position in the sequence of retries.
 * @member {Number} retryNumber
 */
CommonTransaction.prototype['retryNumber'] = undefined;

/**
 * Transaction status.
 * @member {module:model/CommonTransaction.StatusEnum} status
 */
CommonTransaction.prototype['status'] = undefined;

/**
 * The orders IDs related to transaction's invoice(s).
 * @member {Array.<String>} subscriptionIds
 */
CommonTransaction.prototype['subscriptionIds'] = undefined;

/**
 * Transaction type.
 * @member {module:model/CommonTransaction.TypeEnum} type
 */
CommonTransaction.prototype['type'] = undefined;

/**
 * Transaction updated time.
 * @member {Date} updatedTime
 */
CommonTransaction.prototype['updatedTime'] = undefined;

/**
 * The website ID.
 * @member {String} websiteId
 */
CommonTransaction.prototype['websiteId'] = undefined;





/**
 * Allowed values for the <code>result</code> property.
 * @enum {String}
 * @readonly
 */
CommonTransaction['ResultEnum'] = {

    /**
     * value: "abandoned"
     * @const
     */
    "abandoned": "abandoned",

    /**
     * value: "approved"
     * @const
     */
    "approved": "approved",

    /**
     * value: "canceled"
     * @const
     */
    "canceled": "canceled",

    /**
     * value: "declined"
     * @const
     */
    "declined": "declined",

    /**
     * value: "unknown"
     * @const
     */
    "unknown": "unknown"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
CommonTransaction['StatusEnum'] = {

    /**
     * value: "completed"
     * @const
     */
    "completed": "completed",

    /**
     * value: "conn-error"
     * @const
     */
    "conn-error": "conn-error",

    /**
     * value: "disputed"
     * @const
     */
    "disputed": "disputed",

    /**
     * value: "never-sent"
     * @const
     */
    "never-sent": "never-sent",

    /**
     * value: "offsite"
     * @const
     */
    "offsite": "offsite",

    /**
     * value: "partially-refunded"
     * @const
     */
    "partially-refunded": "partially-refunded",

    /**
     * value: "pending"
     * @const
     */
    "pending": "pending",

    /**
     * value: "refunded"
     * @const
     */
    "refunded": "refunded",

    /**
     * value: "sending"
     * @const
     */
    "sending": "sending",

    /**
     * value: "suspended"
     * @const
     */
    "suspended": "suspended",

    /**
     * value: "timeout"
     * @const
     */
    "timeout": "timeout",

    /**
     * value: "voided"
     * @const
     */
    "voided": "voided",

    /**
     * value: "waiting-approval"
     * @const
     */
    "waiting-approval": "waiting-approval",

    /**
     * value: "waiting-capture"
     * @const
     */
    "waiting-capture": "waiting-capture",

    /**
     * value: "waiting-gateway"
     * @const
     */
    "waiting-gateway": "waiting-gateway",

    /**
     * value: "waiting-refund"
     * @const
     */
    "waiting-refund": "waiting-refund"
};


/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
CommonTransaction['TypeEnum'] = {

    /**
     * value: "3ds-authentication"
     * @const
     */
    "3ds-authentication": "3ds-authentication",

    /**
     * value: "authorize"
     * @const
     */
    "authorize": "authorize",

    /**
     * value: "capture"
     * @const
     */
    "capture": "capture",

    /**
     * value: "credit"
     * @const
     */
    "credit": "credit",

    /**
     * value: "refund"
     * @const
     */
    "refund": "refund",

    /**
     * value: "sale"
     * @const
     */
    "sale": "sale",

    /**
     * value: "void"
     * @const
     */
    "void": "void"
};



export default CommonTransaction;

