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
import DisputeEmbeddedInner from './DisputeEmbeddedInner';
import DisputeLinksInner from './DisputeLinksInner';

/**
 * The Dispute model module.
 * @module model/Dispute
 * @version 2.1
 */
class Dispute {
    /**
     * Constructs a new <code>Dispute</code>.
     * @alias module:model/Dispute
     * @param amount {Number} The dispute amount.
     * @param currency {String} ISO 4217 alphabetic currency code.
     * @param postedTime {Date} Dispute posted time.
     * @param reasonCode {module:model/Dispute.ReasonCodeEnum} The dispute's reason code.
     * @param status {module:model/Dispute.StatusEnum} The dispute's status.
     * @param transactionId {String} The dispute's transaction ID.
     * @param type {module:model/Dispute.TypeEnum} The dispute's type.
     */
    constructor(amount, currency, postedTime, reasonCode, status, transactionId, type) { 
        
        Dispute.initialize(this, amount, currency, postedTime, reasonCode, status, transactionId, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, amount, currency, postedTime, reasonCode, status, transactionId, type) { 
        obj['amount'] = amount;
        obj['currency'] = currency;
        obj['postedTime'] = postedTime;
        obj['reasonCode'] = reasonCode;
        obj['status'] = status;
        obj['transactionId'] = transactionId;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>Dispute</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Dispute} obj Optional instance to populate.
     * @return {module:model/Dispute} The populated <code>Dispute</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Dispute();

            if (data.hasOwnProperty('_embedded')) {
                obj['_embedded'] = ApiClient.convertToType(data['_embedded'], [DisputeEmbeddedInner]);
            }
            if (data.hasOwnProperty('_links')) {
                obj['_links'] = ApiClient.convertToType(data['_links'], [DisputeLinksInner]);
            }
            if (data.hasOwnProperty('acquirerReferenceNumber')) {
                obj['acquirerReferenceNumber'] = ApiClient.convertToType(data['acquirerReferenceNumber'], 'String');
            }
            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'Number');
            }
            if (data.hasOwnProperty('caseId')) {
                obj['caseId'] = ApiClient.convertToType(data['caseId'], 'String');
            }
            if (data.hasOwnProperty('category')) {
                obj['category'] = ApiClient.convertToType(data['category'], 'String');
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('customerId')) {
                obj['customerId'] = ApiClient.convertToType(data['customerId'], 'String');
            }
            if (data.hasOwnProperty('deadlineTime')) {
                obj['deadlineTime'] = ApiClient.convertToType(data['deadlineTime'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('postedTime')) {
                obj['postedTime'] = ApiClient.convertToType(data['postedTime'], 'Date');
            }
            if (data.hasOwnProperty('rawResponse')) {
                obj['rawResponse'] = ApiClient.convertToType(data['rawResponse'], 'String');
            }
            if (data.hasOwnProperty('reasonCode')) {
                obj['reasonCode'] = ApiClient.convertToType(data['reasonCode'], 'String');
            }
            if (data.hasOwnProperty('resolvedTime')) {
                obj['resolvedTime'] = ApiClient.convertToType(data['resolvedTime'], 'Date');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('transactionId')) {
                obj['transactionId'] = ApiClient.convertToType(data['transactionId'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('updatedTime')) {
                obj['updatedTime'] = ApiClient.convertToType(data['updatedTime'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Dispute</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Dispute</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Dispute.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['_embedded']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_embedded'])) {
                throw new Error("Expected the field `_embedded` to be an array in the JSON data but got " + data['_embedded']);
            }
            // validate the optional field `_embedded` (array)
            for (const item of data['_embedded']) {
                DisputeEmbeddedInner.validateJSON(item);
            };
        }
        if (data['_links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_links'])) {
                throw new Error("Expected the field `_links` to be an array in the JSON data but got " + data['_links']);
            }
            // validate the optional field `_links` (array)
            for (const item of data['_links']) {
                DisputeLinksInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['acquirerReferenceNumber'] && !(typeof data['acquirerReferenceNumber'] === 'string' || data['acquirerReferenceNumber'] instanceof String)) {
            throw new Error("Expected the field `acquirerReferenceNumber` to be a primitive type in the JSON string but got " + data['acquirerReferenceNumber']);
        }
        // ensure the json data is a string
        if (data['caseId'] && !(typeof data['caseId'] === 'string' || data['caseId'] instanceof String)) {
            throw new Error("Expected the field `caseId` to be a primitive type in the JSON string but got " + data['caseId']);
        }
        // ensure the json data is a string
        if (data['category'] && !(typeof data['category'] === 'string' || data['category'] instanceof String)) {
            throw new Error("Expected the field `category` to be a primitive type in the JSON string but got " + data['category']);
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
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['rawResponse'] && !(typeof data['rawResponse'] === 'string' || data['rawResponse'] instanceof String)) {
            throw new Error("Expected the field `rawResponse` to be a primitive type in the JSON string but got " + data['rawResponse']);
        }
        // ensure the json data is a string
        if (data['reasonCode'] && !(typeof data['reasonCode'] === 'string' || data['reasonCode'] instanceof String)) {
            throw new Error("Expected the field `reasonCode` to be a primitive type in the JSON string but got " + data['reasonCode']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['transactionId'] && !(typeof data['transactionId'] === 'string' || data['transactionId'] instanceof String)) {
            throw new Error("Expected the field `transactionId` to be a primitive type in the JSON string but got " + data['transactionId']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

Dispute.RequiredProperties = ["amount", "currency", "postedTime", "reasonCode", "status", "transactionId", "type"];

/**
 * Any embedded objects available that are requested by the `expand` querystring parameter.
 * @member {Array.<module:model/DisputeEmbeddedInner>} _embedded
 */
Dispute.prototype['_embedded'] = undefined;

/**
 * The links related to resource.
 * @member {Array.<module:model/DisputeLinksInner>} _links
 */
Dispute.prototype['_links'] = undefined;

/**
 * The dispute's acquirer reference number.
 * @member {String} acquirerReferenceNumber
 */
Dispute.prototype['acquirerReferenceNumber'] = undefined;

/**
 * The dispute amount.
 * @member {Number} amount
 */
Dispute.prototype['amount'] = undefined;

/**
 * The case ID for the dispute.
 * @member {String} caseId
 */
Dispute.prototype['caseId'] = undefined;

/**
 * The dispute's category.
 * @member {module:model/Dispute.CategoryEnum} category
 */
Dispute.prototype['category'] = undefined;

/**
 * Dispute created time.
 * @member {Date} createdTime
 */
Dispute.prototype['createdTime'] = undefined;

/**
 * ISO 4217 alphabetic currency code.
 * @member {String} currency
 */
Dispute.prototype['currency'] = undefined;

/**
 * The dispute's customer ID.
 * @member {String} customerId
 */
Dispute.prototype['customerId'] = undefined;

/**
 * Dispute deadline time.
 * @member {Date} deadlineTime
 */
Dispute.prototype['deadlineTime'] = undefined;

/**
 * The dispute identifier string.
 * @member {String} id
 */
Dispute.prototype['id'] = undefined;

/**
 * Dispute posted time.
 * @member {Date} postedTime
 */
Dispute.prototype['postedTime'] = undefined;

/**
 * Dispute raw response from gateway.
 * @member {String} rawResponse
 */
Dispute.prototype['rawResponse'] = undefined;

/**
 * The dispute's reason code.
 * @member {module:model/Dispute.ReasonCodeEnum} reasonCode
 */
Dispute.prototype['reasonCode'] = undefined;

/**
 * Dispute resolved time.
 * @member {Date} resolvedTime
 */
Dispute.prototype['resolvedTime'] = undefined;

/**
 * The dispute's status.
 * @member {module:model/Dispute.StatusEnum} status
 */
Dispute.prototype['status'] = undefined;

/**
 * The dispute's transaction ID.
 * @member {String} transactionId
 */
Dispute.prototype['transactionId'] = undefined;

/**
 * The dispute's type.
 * @member {module:model/Dispute.TypeEnum} type
 */
Dispute.prototype['type'] = undefined;

/**
 * Dispute updated time.
 * @member {Date} updatedTime
 */
Dispute.prototype['updatedTime'] = undefined;





/**
 * Allowed values for the <code>category</code> property.
 * @enum {String}
 * @readonly
 */
Dispute['CategoryEnum'] = {

    /**
     * value: "fraud"
     * @const
     */
    "fraud": "fraud",

    /**
     * value: "unrecognized"
     * @const
     */
    "unrecognized": "unrecognized",

    /**
     * value: "product-not-received"
     * @const
     */
    "product-not-received": "product-not-received",

    /**
     * value: "product-unacceptable"
     * @const
     */
    "product-unacceptable": "product-unacceptable",

    /**
     * value: "product-not-refunded"
     * @const
     */
    "product-not-refunded": "product-not-refunded",

    /**
     * value: "duplicate"
     * @const
     */
    "duplicate": "duplicate",

    /**
     * value: "subscription-canceled"
     * @const
     */
    "subscription-canceled": "subscription-canceled",

    /**
     * value: "uncategorized"
     * @const
     */
    "uncategorized": "uncategorized"
};


/**
 * Allowed values for the <code>reasonCode</code> property.
 * @enum {String}
 * @readonly
 */
Dispute['ReasonCodeEnum'] = {

    /**
     * value: "1000"
     * @const
     */
    "1000": "1000",

    /**
     * value: "10.1"
     * @const
     */
    "10.1": "10.1",

    /**
     * value: "10.2"
     * @const
     */
    "10.2": "10.2",

    /**
     * value: "10.3"
     * @const
     */
    "10.3": "10.3",

    /**
     * value: "10.4"
     * @const
     */
    "10.4": "10.4",

    /**
     * value: "10.5"
     * @const
     */
    "10.5": "10.5",

    /**
     * value: "11.1"
     * @const
     */
    "11.1": "11.1",

    /**
     * value: "11.2"
     * @const
     */
    "11.2": "11.2",

    /**
     * value: "11.3"
     * @const
     */
    "11.3": "11.3",

    /**
     * value: "12"
     * @const
     */
    "12": "12",

    /**
     * value: "12.1"
     * @const
     */
    "12.1": "12.1",

    /**
     * value: "12.2"
     * @const
     */
    "12.2": "12.2",

    /**
     * value: "12.3"
     * @const
     */
    "12.3": "12.3",

    /**
     * value: "12.4"
     * @const
     */
    "12.4": "12.4",

    /**
     * value: "12.5"
     * @const
     */
    "12.5": "12.5",

    /**
     * value: "12.6"
     * @const
     */
    "12.6": "12.6",

    /**
     * value: "12.7"
     * @const
     */
    "12.7": "12.7",

    /**
     * value: "13.1"
     * @const
     */
    "13.1": "13.1",

    /**
     * value: "13.2"
     * @const
     */
    "13.2": "13.2",

    /**
     * value: "13.3"
     * @const
     */
    "13.3": "13.3",

    /**
     * value: "13.4"
     * @const
     */
    "13.4": "13.4",

    /**
     * value: "13.5"
     * @const
     */
    "13.5": "13.5",

    /**
     * value: "13.6"
     * @const
     */
    "13.6": "13.6",

    /**
     * value: "13.7"
     * @const
     */
    "13.7": "13.7",

    /**
     * value: "13.8"
     * @const
     */
    "13.8": "13.8",

    /**
     * value: "13.9"
     * @const
     */
    "13.9": "13.9",

    /**
     * value: "2"
     * @const
     */
    "2": "2",

    /**
     * value: "30"
     * @const
     */
    "30": "30",

    /**
     * value: "31"
     * @const
     */
    "31": "31",

    /**
     * value: "35"
     * @const
     */
    "35": "35",

    /**
     * value: "37"
     * @const
     */
    "37": "37",

    /**
     * value: "40"
     * @const
     */
    "40": "40",

    /**
     * value: "41"
     * @const
     */
    "41": "41",

    /**
     * value: "42"
     * @const
     */
    "42": "42",

    /**
     * value: "46"
     * @const
     */
    "46": "46",

    /**
     * value: "47"
     * @const
     */
    "47": "47",

    /**
     * value: "49"
     * @const
     */
    "49": "49",

    /**
     * value: "50"
     * @const
     */
    "50": "50",

    /**
     * value: "53"
     * @const
     */
    "53": "53",

    /**
     * value: "54"
     * @const
     */
    "54": "54",

    /**
     * value: "55"
     * @const
     */
    "55": "55",

    /**
     * value: "57"
     * @const
     */
    "57": "57",

    /**
     * value: "59"
     * @const
     */
    "59": "59",

    /**
     * value: "60"
     * @const
     */
    "60": "60",

    /**
     * value: "62"
     * @const
     */
    "62": "62",

    /**
     * value: "7"
     * @const
     */
    "7": "7",

    /**
     * value: "70"
     * @const
     */
    "70": "70",

    /**
     * value: "71"
     * @const
     */
    "71": "71",

    /**
     * value: "72"
     * @const
     */
    "722": "72",

    /**
     * value: "73"
     * @const
     */
    "73": "73",

    /**
     * value: "74"
     * @const
     */
    "74": "74",

    /**
     * value: "75"
     * @const
     */
    "75": "75",

    /**
     * value: "76"
     * @const
     */
    "76": "76",

    /**
     * value: "77"
     * @const
     */
    "77": "77",

    /**
     * value: "79"
     * @const
     */
    "79": "79",

    /**
     * value: "8"
     * @const
     */
    "8": "8",

    /**
     * value: "80"
     * @const
     */
    "80": "80",

    /**
     * value: "81"
     * @const
     */
    "81": "81",

    /**
     * value: "82"
     * @const
     */
    "82": "82",

    /**
     * value: "83"
     * @const
     */
    "83": "83",

    /**
     * value: "85"
     * @const
     */
    "85": "85",

    /**
     * value: "86"
     * @const
     */
    "86": "86",

    /**
     * value: "93"
     * @const
     */
    "93": "93",

    /**
     * value: "00"
     * @const
     */
    "00": "00",

    /**
     * value: "63"
     * @const
     */
    "63": "63",

    /**
     * value: "A01"
     * @const
     */
    "A01": "A01",

    /**
     * value: "A02"
     * @const
     */
    "A02": "A02",

    /**
     * value: "A08"
     * @const
     */
    "A08": "A08",

    /**
     * value: "F10"
     * @const
     */
    "F10": "F10",

    /**
     * value: "F14"
     * @const
     */
    "F14": "F14",

    /**
     * value: "F22"
     * @const
     */
    "F22": "F22",

    /**
     * value: "F24"
     * @const
     */
    "F24": "F24",

    /**
     * value: "F29"
     * @const
     */
    "F29": "F29",

    /**
     * value: "C02"
     * @const
     */
    "C02": "C02",

    /**
     * value: "C04"
     * @const
     */
    "C04": "C04",

    /**
     * value: "C05"
     * @const
     */
    "C05": "C05",

    /**
     * value: "C08"
     * @const
     */
    "C08": "C08",

    /**
     * value: "C14"
     * @const
     */
    "C14": "C14",

    /**
     * value: "C18"
     * @const
     */
    "C18": "C18",

    /**
     * value: "C28"
     * @const
     */
    "C28": "C28",

    /**
     * value: "C31"
     * @const
     */
    "C31": "C31",

    /**
     * value: "C32"
     * @const
     */
    "C32": "C32",

    /**
     * value: "M10"
     * @const
     */
    "M10": "M10",

    /**
     * value: "M49"
     * @const
     */
    "M49": "M49",

    /**
     * value: "P01"
     * @const
     */
    "P01": "P01",

    /**
     * value: "P03"
     * @const
     */
    "P03": "P03",

    /**
     * value: "P04"
     * @const
     */
    "P04": "P04",

    /**
     * value: "P05"
     * @const
     */
    "P05": "P05",

    /**
     * value: "P07"
     * @const
     */
    "P07": "P07",

    /**
     * value: "P08"
     * @const
     */
    "P08": "P08",

    /**
     * value: "P22"
     * @const
     */
    "P22": "P22",

    /**
     * value: "P23"
     * @const
     */
    "P23": "P23",

    /**
     * value: "R03"
     * @const
     */
    "R03": "R03",

    /**
     * value: "R13"
     * @const
     */
    "R13": "R13",

    /**
     * value: "M01"
     * @const
     */
    "M01": "M01",

    /**
     * value: "FR1"
     * @const
     */
    "FR1": "FR1",

    /**
     * value: "FR4"
     * @const
     */
    "FR4": "FR4",

    /**
     * value: "FR6"
     * @const
     */
    "FR6": "FR6",

    /**
     * value: "AL"
     * @const
     */
    "AL": "AL",

    /**
     * value: "AP"
     * @const
     */
    "AP": "AP",

    /**
     * value: "AW"
     * @const
     */
    "AW": "AW",

    /**
     * value: "CA"
     * @const
     */
    "CA": "CA",

    /**
     * value: "CD"
     * @const
     */
    "CD": "CD",

    /**
     * value: "CR"
     * @const
     */
    "CR": "CR",

    /**
     * value: "DA"
     * @const
     */
    "DA": "DA",

    /**
     * value: "DP"
     * @const
     */
    "DP": "DP",

    /**
     * value: "DP1"
     * @const
     */
    "DP1": "DP1",

    /**
     * value: "EX"
     * @const
     */
    "EX": "EX",

    /**
     * value: "IC"
     * @const
     */
    "IC": "IC",

    /**
     * value: "IN"
     * @const
     */
    "IN": "IN",

    /**
     * value: "IS"
     * @const
     */
    "IS": "IS",

    /**
     * value: "LP"
     * @const
     */
    "LP": "LP",

    /**
     * value: "N"
     * @const
     */
    "N": "N",

    /**
     * value: "NA"
     * @const
     */
    "NA": "NA",

    /**
     * value: "NC"
     * @const
     */
    "NC": "NC",

    /**
     * value: "P"
     * @const
     */
    "P": "P",

    /**
     * value: "RG"
     * @const
     */
    "RG": "RG",

    /**
     * value: "RM"
     * @const
     */
    "RM": "RM",

    /**
     * value: "RN1"
     * @const
     */
    "RN1": "RN1",

    /**
     * value: "RN2"
     * @const
     */
    "RN2": "RN2",

    /**
     * value: "SV"
     * @const
     */
    "SV": "SV",

    /**
     * value: "TF"
     * @const
     */
    "TF": "TF",

    /**
     * value: "TNM"
     * @const
     */
    "TNM": "TNM",

    /**
     * value: "UA01"
     * @const
     */
    "UA01": "UA01",

    /**
     * value: "UA02"
     * @const
     */
    "UA02": "UA02",

    /**
     * value: "UA32"
     * @const
     */
    "UA32": "UA32",

    /**
     * value: "UA99"
     * @const
     */
    "UA99": "UA99",

    /**
     * value: "UA03"
     * @const
     */
    "UA03": "UA03",

    /**
     * value: "UA10"
     * @const
     */
    "UA10": "UA10",

    /**
     * value: "UA11"
     * @const
     */
    "UA11": "UA11",

    /**
     * value: "UA12"
     * @const
     */
    "UA12": "UA12",

    /**
     * value: "UA18"
     * @const
     */
    "UA18": "UA18",

    /**
     * value: "UA20"
     * @const
     */
    "UA20": "UA20",

    /**
     * value: "UA21"
     * @const
     */
    "UA21": "UA21",

    /**
     * value: "UA22"
     * @const
     */
    "UA22": "UA22",

    /**
     * value: "UA23"
     * @const
     */
    "UA23": "UA23",

    /**
     * value: "UA28"
     * @const
     */
    "UA28": "UA28",

    /**
     * value: "UA30"
     * @const
     */
    "UA30": "UA30",

    /**
     * value: "UA31"
     * @const
     */
    "UA31": "UA31",

    /**
     * value: "UA38"
     * @const
     */
    "UA38": "UA38",

    /**
     * value: "duplicate"
     * @const
     */
    "duplicate": "duplicate",

    /**
     * value: "fraudulent"
     * @const
     */
    "fraudulent": "fraudulent",

    /**
     * value: "subscription_canceled"
     * @const
     */
    "subscription_canceled": "subscription_canceled",

    /**
     * value: "product_unacceptable"
     * @const
     */
    "product_unacceptable": "product_unacceptable",

    /**
     * value: "product_not_received"
     * @const
     */
    "product_not_received": "product_not_received",

    /**
     * value: "unrecognized"
     * @const
     */
    "unrecognized": "unrecognized",

    /**
     * value: "credit_not_processed"
     * @const
     */
    "credit_not_processed": "credit_not_processed",

    /**
     * value: "customer_initiated"
     * @const
     */
    "customer_initiated": "customer_initiated",

    /**
     * value: "incorrect_account_details"
     * @const
     */
    "incorrect_account_details": "incorrect_account_details",

    /**
     * value: "insufficient_funds"
     * @const
     */
    "insufficient_funds": "insufficient_funds",

    /**
     * value: "bank_cannot_process"
     * @const
     */
    "bank_cannot_process": "bank_cannot_process",

    /**
     * value: "debit_not_authorized"
     * @const
     */
    "debit_not_authorized": "debit_not_authorized",

    /**
     * value: "general"
     * @const
     */
    "general": "general",

    /**
     * value: "pre-chargeback-alert"
     * @const
     */
    "pre-chargeback-alert": "pre-chargeback-alert",

    /**
     * value: "0"
     * @const
     */
    "0": "0",

    /**
     * value: "1"
     * @const
     */
    "1": "1",

    /**
     * value: "2"
     * @const
     */
    "22": "2",

    /**
     * value: "3"
     * @const
     */
    "3": "3",

    /**
     * value: "4"
     * @const
     */
    "4": "4",

    /**
     * value: "5"
     * @const
     */
    "5": "5",

    /**
     * value: "6"
     * @const
     */
    "6": "6",

    /**
     * value: "7"
     * @const
     */
    "72": "7",

    /**
     * value: "9"
     * @const
     */
    "9": "9",

    /**
     * value: "51"
     * @const
     */
    "51": "51",

    /**
     * value: "A"
     * @const
     */
    "A": "A",

    /**
     * value: "B"
     * @const
     */
    "B": "B"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
Dispute['StatusEnum'] = {

    /**
     * value: "response-needed"
     * @const
     */
    "response-needed": "response-needed",

    /**
     * value: "under-review"
     * @const
     */
    "under-review": "under-review",

    /**
     * value: "forfeited"
     * @const
     */
    "forfeited": "forfeited",

    /**
     * value: "won"
     * @const
     */
    "won": "won",

    /**
     * value: "lost"
     * @const
     */
    "lost": "lost",

    /**
     * value: "unknown"
     * @const
     */
    "unknown": "unknown"
};


/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
Dispute['TypeEnum'] = {

    /**
     * value: "information-request"
     * @const
     */
    "information-request": "information-request",

    /**
     * value: "first-chargeback"
     * @const
     */
    "first-chargeback": "first-chargeback",

    /**
     * value: "second-chargeback"
     * @const
     */
    "second-chargeback": "second-chargeback",

    /**
     * value: "arbitration"
     * @const
     */
    "arbitration": "arbitration",

    /**
     * value: "fraud"
     * @const
     */
    "fraud": "fraud",

    /**
     * value: "ethoca-alert"
     * @const
     */
    "ethoca-alert": "ethoca-alert",

    /**
     * value: "verifi-alert"
     * @const
     */
    "verifi-alert": "verifi-alert"
};



export default Dispute;

