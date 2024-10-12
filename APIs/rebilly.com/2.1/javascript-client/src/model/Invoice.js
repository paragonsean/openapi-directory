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
import CommonInvoice from './CommonInvoice';
import ContactObject from './ContactObject';
import InvoiceAllOfEmbedded from './InvoiceAllOfEmbedded';
import InvoiceAllOfLinks from './InvoiceAllOfLinks';
import InvoiceAllOfRetryInstruction from './InvoiceAllOfRetryInstruction';
import InvoiceDiscount from './InvoiceDiscount';
import InvoiceItem from './InvoiceItem';
import InvoiceShipping from './InvoiceShipping';
import InvoiceTax from './InvoiceTax';
import Transaction from './Transaction';

/**
 * The Invoice model module.
 * @module model/Invoice
 * @version 2.1
 */
class Invoice {
    /**
     * Constructs a new <code>Invoice</code>.
     * @alias module:model/Invoice
     * @implements module:model/CommonInvoice
     * @param currency {String} ISO 4217 alphabetic currency code.
     * @param websiteId {String} The website ID.
     * @param customerId {String} The сustomer's ID.
     */
    constructor(currency, websiteId, customerId) { 
        CommonInvoice.initialize(this, currency, websiteId);
        Invoice.initialize(this, currency, websiteId, customerId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, currency, websiteId, customerId) { 
        obj['autopayRetryNumber'] = 0;
        obj['currency'] = currency;
        obj['websiteId'] = websiteId;
        obj['customerId'] = customerId;
    }

    /**
     * Constructs a <code>Invoice</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Invoice} obj Optional instance to populate.
     * @return {module:model/Invoice} The populated <code>Invoice</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Invoice();
            CommonInvoice.constructFromObject(data, obj);

            if (data.hasOwnProperty('abandonedTime')) {
                obj['abandonedTime'] = ApiClient.convertToType(data['abandonedTime'], 'Date');
            }
            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'Number');
            }
            if (data.hasOwnProperty('amountDue')) {
                obj['amountDue'] = ApiClient.convertToType(data['amountDue'], 'Number');
            }
            if (data.hasOwnProperty('autopayRetryNumber')) {
                obj['autopayRetryNumber'] = ApiClient.convertToType(data['autopayRetryNumber'], 'Number');
            }
            if (data.hasOwnProperty('autopayScheduledTime')) {
                obj['autopayScheduledTime'] = ApiClient.convertToType(data['autopayScheduledTime'], 'Date');
            }
            if (data.hasOwnProperty('billingAddress')) {
                obj['billingAddress'] = ApiClient.convertToType(data['billingAddress'], ContactObject);
            }
            if (data.hasOwnProperty('collectionPeriod')) {
                obj['collectionPeriod'] = ApiClient.convertToType(data['collectionPeriod'], 'Number');
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('delinquentCollectionPeriod')) {
                obj['delinquentCollectionPeriod'] = ApiClient.convertToType(data['delinquentCollectionPeriod'], 'Number');
            }
            if (data.hasOwnProperty('deliveryAddress')) {
                obj['deliveryAddress'] = ApiClient.convertToType(data['deliveryAddress'], ContactObject);
            }
            if (data.hasOwnProperty('discountAmount')) {
                obj['discountAmount'] = ApiClient.convertToType(data['discountAmount'], 'Number');
            }
            if (data.hasOwnProperty('discounts')) {
                obj['discounts'] = ApiClient.convertToType(data['discounts'], [InvoiceDiscount]);
            }
            if (data.hasOwnProperty('dueTime')) {
                obj['dueTime'] = ApiClient.convertToType(data['dueTime'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('invoiceNumber')) {
                obj['invoiceNumber'] = ApiClient.convertToType(data['invoiceNumber'], 'Number');
            }
            if (data.hasOwnProperty('issuedTime')) {
                obj['issuedTime'] = ApiClient.convertToType(data['issuedTime'], 'Date');
            }
            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [InvoiceItem]);
            }
            if (data.hasOwnProperty('notes')) {
                obj['notes'] = ApiClient.convertToType(data['notes'], 'String');
            }
            if (data.hasOwnProperty('paidTime')) {
                obj['paidTime'] = ApiClient.convertToType(data['paidTime'], 'Date');
            }
            if (data.hasOwnProperty('paymentFormUrl')) {
                obj['paymentFormUrl'] = ApiClient.convertToType(data['paymentFormUrl'], 'String');
            }
            if (data.hasOwnProperty('poNumber')) {
                obj['poNumber'] = ApiClient.convertToType(data['poNumber'], 'String');
            }
            if (data.hasOwnProperty('shipping')) {
                obj['shipping'] = InvoiceShipping.constructFromObject(data['shipping']);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('subscriptionId')) {
                obj['subscriptionId'] = ApiClient.convertToType(data['subscriptionId'], 'String');
            }
            if (data.hasOwnProperty('subtotalAmount')) {
                obj['subtotalAmount'] = ApiClient.convertToType(data['subtotalAmount'], 'Number');
            }
            if (data.hasOwnProperty('tax')) {
                obj['tax'] = InvoiceTax.constructFromObject(data['tax']);
            }
            if (data.hasOwnProperty('updatedTime')) {
                obj['updatedTime'] = ApiClient.convertToType(data['updatedTime'], 'Date');
            }
            if (data.hasOwnProperty('voidedTime')) {
                obj['voidedTime'] = ApiClient.convertToType(data['voidedTime'], 'Date');
            }
            if (data.hasOwnProperty('websiteId')) {
                obj['websiteId'] = ApiClient.convertToType(data['websiteId'], 'String');
            }
            if (data.hasOwnProperty('_embedded')) {
                obj['_embedded'] = ApiClient.convertToType(data['_embedded'], [InvoiceAllOfEmbedded]);
            }
            if (data.hasOwnProperty('_links')) {
                obj['_links'] = ApiClient.convertToType(data['_links'], [InvoiceAllOfLinks]);
            }
            if (data.hasOwnProperty('customerId')) {
                obj['customerId'] = ApiClient.convertToType(data['customerId'], 'String');
            }
            if (data.hasOwnProperty('dueReminderNumber')) {
                obj['dueReminderNumber'] = ApiClient.convertToType(data['dueReminderNumber'], 'Number');
            }
            if (data.hasOwnProperty('dueReminderTime')) {
                obj['dueReminderTime'] = ApiClient.convertToType(data['dueReminderTime'], 'Date');
            }
            if (data.hasOwnProperty('retryInstruction')) {
                obj['retryInstruction'] = InvoiceAllOfRetryInstruction.constructFromObject(data['retryInstruction']);
            }
            if (data.hasOwnProperty('revision')) {
                obj['revision'] = ApiClient.convertToType(data['revision'], 'Number');
            }
            if (data.hasOwnProperty('transactions')) {
                obj['transactions'] = ApiClient.convertToType(data['transactions'], [Transaction]);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Invoice</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Invoice</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Invoice.RequiredProperties) {
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
        // validate the optional field `deliveryAddress`
        if (data['deliveryAddress']) { // data not null
          ContactObject.validateJSON(data['deliveryAddress']);
        }
        if (data['discounts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['discounts'])) {
                throw new Error("Expected the field `discounts` to be an array in the JSON data but got " + data['discounts']);
            }
            // validate the optional field `discounts` (array)
            for (const item of data['discounts']) {
                InvoiceDiscount.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                InvoiceItem.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['notes'] && !(typeof data['notes'] === 'string' || data['notes'] instanceof String)) {
            throw new Error("Expected the field `notes` to be a primitive type in the JSON string but got " + data['notes']);
        }
        // ensure the json data is a string
        if (data['paymentFormUrl'] && !(typeof data['paymentFormUrl'] === 'string' || data['paymentFormUrl'] instanceof String)) {
            throw new Error("Expected the field `paymentFormUrl` to be a primitive type in the JSON string but got " + data['paymentFormUrl']);
        }
        // ensure the json data is a string
        if (data['poNumber'] && !(typeof data['poNumber'] === 'string' || data['poNumber'] instanceof String)) {
            throw new Error("Expected the field `poNumber` to be a primitive type in the JSON string but got " + data['poNumber']);
        }
        // validate the optional field `shipping`
        if (data['shipping']) { // data not null
          InvoiceShipping.validateJSON(data['shipping']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['subscriptionId'] && !(typeof data['subscriptionId'] === 'string' || data['subscriptionId'] instanceof String)) {
            throw new Error("Expected the field `subscriptionId` to be a primitive type in the JSON string but got " + data['subscriptionId']);
        }
        // validate the optional field `tax`
        if (data['tax']) { // data not null
          InvoiceTax.validateJSON(data['tax']);
        }
        // ensure the json data is a string
        if (data['websiteId'] && !(typeof data['websiteId'] === 'string' || data['websiteId'] instanceof String)) {
            throw new Error("Expected the field `websiteId` to be a primitive type in the JSON string but got " + data['websiteId']);
        }
        if (data['_embedded']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_embedded'])) {
                throw new Error("Expected the field `_embedded` to be an array in the JSON data but got " + data['_embedded']);
            }
            // validate the optional field `_embedded` (array)
            for (const item of data['_embedded']) {
                InvoiceAllOfEmbedded.validateJSON(item);
            };
        }
        if (data['_links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_links'])) {
                throw new Error("Expected the field `_links` to be an array in the JSON data but got " + data['_links']);
            }
            // validate the optional field `_links` (array)
            for (const item of data['_links']) {
                InvoiceAllOfLinks.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['customerId'] && !(typeof data['customerId'] === 'string' || data['customerId'] instanceof String)) {
            throw new Error("Expected the field `customerId` to be a primitive type in the JSON string but got " + data['customerId']);
        }
        // validate the optional field `retryInstruction`
        if (data['retryInstruction']) { // data not null
          InvoiceAllOfRetryInstruction.validateJSON(data['retryInstruction']);
        }
        if (data['transactions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['transactions'])) {
                throw new Error("Expected the field `transactions` to be an array in the JSON data but got " + data['transactions']);
            }
            // validate the optional field `transactions` (array)
            for (const item of data['transactions']) {
                Transaction.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

Invoice.RequiredProperties = ["currency", "websiteId", "customerId"];

/**
 * Invoice abandoned time.
 * @member {Date} abandonedTime
 */
Invoice.prototype['abandonedTime'] = undefined;

/**
 * The invoice's amount.
 * @member {Number} amount
 */
Invoice.prototype['amount'] = undefined;

/**
 * The invoice's due amount.
 * @member {Number} amountDue
 */
Invoice.prototype['amountDue'] = undefined;

/**
 * Invoice autopay retry number.
 * @member {Number} autopayRetryNumber
 * @default 0
 */
Invoice.prototype['autopayRetryNumber'] = 0;

/**
 * Invoice autopay scheduled time.
 * @member {Date} autopayScheduledTime
 */
Invoice.prototype['autopayScheduledTime'] = undefined;

/**
 * Invoice's billing address.
 * @member {module:model/ContactObject} billingAddress
 */
Invoice.prototype['billingAddress'] = undefined;

/**
 * Collection period - difference between paidTime and issuedTime in days.
 * @member {Number} collectionPeriod
 */
Invoice.prototype['collectionPeriod'] = undefined;

/**
 * Invoice created time.
 * @member {Date} createdTime
 */
Invoice.prototype['createdTime'] = undefined;

/**
 * ISO 4217 alphabetic currency code.
 * @member {String} currency
 */
Invoice.prototype['currency'] = undefined;

/**
 * Delinquent collection period - difference between paidTime and dueTime in days.
 * @member {Number} delinquentCollectionPeriod
 */
Invoice.prototype['delinquentCollectionPeriod'] = undefined;

/**
 * Invoice's delivery address.
 * @member {module:model/ContactObject} deliveryAddress
 */
Invoice.prototype['deliveryAddress'] = undefined;

/**
 * The invoice's discounts amount.
 * @member {Number} discountAmount
 */
Invoice.prototype['discountAmount'] = undefined;

/**
 * Discounts applied.
 * @member {Array.<module:model/InvoiceDiscount>} discounts
 */
Invoice.prototype['discounts'] = undefined;

/**
 * Invoice due time.
 * @member {Date} dueTime
 */
Invoice.prototype['dueTime'] = undefined;

/**
 * The invoice ID.
 * @member {String} id
 */
Invoice.prototype['id'] = undefined;

/**
 * An auto-incrementing number based on the sequence of invoices for any particular customer.
 * @member {Number} invoiceNumber
 */
Invoice.prototype['invoiceNumber'] = undefined;

/**
 * Invoice issued time.
 * @member {Date} issuedTime
 */
Invoice.prototype['issuedTime'] = undefined;

/**
 * Invoice items array.
 * @member {Array.<module:model/InvoiceItem>} items
 */
Invoice.prototype['items'] = undefined;

/**
 * Notes for the customer which will be displayed on the invoice.
 * @member {String} notes
 */
Invoice.prototype['notes'] = undefined;

/**
 * Invoice paid time.
 * @member {Date} paidTime
 */
Invoice.prototype['paidTime'] = undefined;

/**
 * URL where the customer can be redirected to pay for the invoice with one of the methods which are available for this customer. It's an alternative to creating a new transaction with empty `methods`. 
 * @member {String} paymentFormUrl
 */
Invoice.prototype['paymentFormUrl'] = undefined;

/**
 * Purchase order number which will be displayed on the invoice.
 * @member {String} poNumber
 */
Invoice.prototype['poNumber'] = undefined;

/**
 * @member {module:model/InvoiceShipping} shipping
 */
Invoice.prototype['shipping'] = undefined;

/**
 * Invoice status.
 * @member {module:model/Invoice.StatusEnum} status
 */
Invoice.prototype['status'] = undefined;

/**
 * The related order's ID if available, otherwise null.
 * @member {String} subscriptionId
 */
Invoice.prototype['subscriptionId'] = undefined;

/**
 * The invoice's subtotal amount.
 * @member {Number} subtotalAmount
 */
Invoice.prototype['subtotalAmount'] = undefined;

/**
 * @member {module:model/InvoiceTax} tax
 */
Invoice.prototype['tax'] = undefined;

/**
 * Invoice updated time.
 * @member {Date} updatedTime
 */
Invoice.prototype['updatedTime'] = undefined;

/**
 * Invoice voided time.
 * @member {Date} voidedTime
 */
Invoice.prototype['voidedTime'] = undefined;

/**
 * The website ID.
 * @member {String} websiteId
 */
Invoice.prototype['websiteId'] = undefined;

/**
 * Any embedded objects available that are requested by the `expand` querystring parameter.
 * @member {Array.<module:model/InvoiceAllOfEmbedded>} _embedded
 */
Invoice.prototype['_embedded'] = undefined;

/**
 * The links related to resource.
 * @member {Array.<module:model/InvoiceAllOfLinks>} _links
 */
Invoice.prototype['_links'] = undefined;

/**
 * The сustomer's ID.
 * @member {String} customerId
 */
Invoice.prototype['customerId'] = undefined;

/**
 * Number of past due reminder events triggered.
 * @member {Number} dueReminderNumber
 */
Invoice.prototype['dueReminderNumber'] = undefined;

/**
 * Time past due reminder event will be triggered.
 * @member {Date} dueReminderTime
 */
Invoice.prototype['dueReminderTime'] = undefined;

/**
 * @member {module:model/InvoiceAllOfRetryInstruction} retryInstruction
 */
Invoice.prototype['retryInstruction'] = undefined;

/**
 * The number of times the invoice data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation. 
 * @member {Number} revision
 */
Invoice.prototype['revision'] = undefined;

/**
 * Invoice transactions array.
 * @member {Array.<module:model/Transaction>} transactions
 */
Invoice.prototype['transactions'] = undefined;

/**
 * Invoice type.
 * @member {module:model/Invoice.TypeEnum} type
 */
Invoice.prototype['type'] = undefined;


// Implement CommonInvoice interface:
/**
 * Invoice abandoned time.
 * @member {Date} abandonedTime
 */
CommonInvoice.prototype['abandonedTime'] = undefined;
/**
 * The invoice's amount.
 * @member {Number} amount
 */
CommonInvoice.prototype['amount'] = undefined;
/**
 * The invoice's due amount.
 * @member {Number} amountDue
 */
CommonInvoice.prototype['amountDue'] = undefined;
/**
 * Invoice autopay retry number.
 * @member {Number} autopayRetryNumber
 * @default 0
 */
CommonInvoice.prototype['autopayRetryNumber'] = 0;
/**
 * Invoice autopay scheduled time.
 * @member {Date} autopayScheduledTime
 */
CommonInvoice.prototype['autopayScheduledTime'] = undefined;
/**
 * Invoice's billing address.
 * @member {module:model/ContactObject} billingAddress
 */
CommonInvoice.prototype['billingAddress'] = undefined;
/**
 * Collection period - difference between paidTime and issuedTime in days.
 * @member {Number} collectionPeriod
 */
CommonInvoice.prototype['collectionPeriod'] = undefined;
/**
 * Invoice created time.
 * @member {Date} createdTime
 */
CommonInvoice.prototype['createdTime'] = undefined;
/**
 * ISO 4217 alphabetic currency code.
 * @member {String} currency
 */
CommonInvoice.prototype['currency'] = undefined;
/**
 * Delinquent collection period - difference between paidTime and dueTime in days.
 * @member {Number} delinquentCollectionPeriod
 */
CommonInvoice.prototype['delinquentCollectionPeriod'] = undefined;
/**
 * Invoice's delivery address.
 * @member {module:model/ContactObject} deliveryAddress
 */
CommonInvoice.prototype['deliveryAddress'] = undefined;
/**
 * The invoice's discounts amount.
 * @member {Number} discountAmount
 */
CommonInvoice.prototype['discountAmount'] = undefined;
/**
 * Discounts applied.
 * @member {Array.<module:model/InvoiceDiscount>} discounts
 */
CommonInvoice.prototype['discounts'] = undefined;
/**
 * Invoice due time.
 * @member {Date} dueTime
 */
CommonInvoice.prototype['dueTime'] = undefined;
/**
 * The invoice ID.
 * @member {String} id
 */
CommonInvoice.prototype['id'] = undefined;
/**
 * An auto-incrementing number based on the sequence of invoices for any particular customer.
 * @member {Number} invoiceNumber
 */
CommonInvoice.prototype['invoiceNumber'] = undefined;
/**
 * Invoice issued time.
 * @member {Date} issuedTime
 */
CommonInvoice.prototype['issuedTime'] = undefined;
/**
 * Invoice items array.
 * @member {Array.<module:model/InvoiceItem>} items
 */
CommonInvoice.prototype['items'] = undefined;
/**
 * Notes for the customer which will be displayed on the invoice.
 * @member {String} notes
 */
CommonInvoice.prototype['notes'] = undefined;
/**
 * Invoice paid time.
 * @member {Date} paidTime
 */
CommonInvoice.prototype['paidTime'] = undefined;
/**
 * URL where the customer can be redirected to pay for the invoice with one of the methods which are available for this customer. It's an alternative to creating a new transaction with empty `methods`. 
 * @member {String} paymentFormUrl
 */
CommonInvoice.prototype['paymentFormUrl'] = undefined;
/**
 * Purchase order number which will be displayed on the invoice.
 * @member {String} poNumber
 */
CommonInvoice.prototype['poNumber'] = undefined;
/**
 * @member {module:model/InvoiceShipping} shipping
 */
CommonInvoice.prototype['shipping'] = undefined;
/**
 * Invoice status.
 * @member {module:model/CommonInvoice.StatusEnum} status
 */
CommonInvoice.prototype['status'] = undefined;
/**
 * The related order's ID if available, otherwise null.
 * @member {String} subscriptionId
 */
CommonInvoice.prototype['subscriptionId'] = undefined;
/**
 * The invoice's subtotal amount.
 * @member {Number} subtotalAmount
 */
CommonInvoice.prototype['subtotalAmount'] = undefined;
/**
 * @member {module:model/InvoiceTax} tax
 */
CommonInvoice.prototype['tax'] = undefined;
/**
 * Invoice updated time.
 * @member {Date} updatedTime
 */
CommonInvoice.prototype['updatedTime'] = undefined;
/**
 * Invoice voided time.
 * @member {Date} voidedTime
 */
CommonInvoice.prototype['voidedTime'] = undefined;
/**
 * The website ID.
 * @member {String} websiteId
 */
CommonInvoice.prototype['websiteId'] = undefined;



/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
Invoice['StatusEnum'] = {

    /**
     * value: "draft"
     * @const
     */
    "draft": "draft",

    /**
     * value: "unpaid"
     * @const
     */
    "unpaid": "unpaid",

    /**
     * value: "paid"
     * @const
     */
    "paid": "paid",

    /**
     * value: "past-due"
     * @const
     */
    "past-due": "past-due",

    /**
     * value: "delinquent"
     * @const
     */
    "delinquent": "delinquent",

    /**
     * value: "abandoned"
     * @const
     */
    "abandoned": "abandoned",

    /**
     * value: "voided"
     * @const
     */
    "voided": "voided",

    /**
     * value: "partially-refunded"
     * @const
     */
    "partially-refunded": "partially-refunded",

    /**
     * value: "refunded"
     * @const
     */
    "refunded": "refunded",

    /**
     * value: "disputed"
     * @const
     */
    "disputed": "disputed"
};


/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
Invoice['TypeEnum'] = {

    /**
     * value: "initial"
     * @const
     */
    "initial": "initial",

    /**
     * value: "renewal"
     * @const
     */
    "renewal": "renewal",

    /**
     * value: "interim"
     * @const
     */
    "interim": "interim",

    /**
     * value: "cancellation"
     * @const
     */
    "cancellation": "cancellation",

    /**
     * value: "one-time"
     * @const
     */
    "one-time": "one-time",

    /**
     * value: "refund"
     * @const
     */
    "refund": "refund",

    /**
     * value: "charge"
     * @const
     */
    "charge": "charge"
};



export default Invoice;

