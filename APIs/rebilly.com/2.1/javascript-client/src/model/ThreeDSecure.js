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
import SelfLink from './SelfLink';

/**
 * The ThreeDSecure model module.
 * @module model/ThreeDSecure
 * @version 2.1
 */
class ThreeDSecure {
    /**
     * Constructs a new <code>ThreeDSecure</code>.
     * @alias module:model/ThreeDSecure
     * @param amount {Number} Transaction amount.
     * @param currency {String} ISO 4217 alphabetic currency code.
     * @param customerId {String} Related customer ID.
     * @param enrolled {module:model/ThreeDSecure.EnrolledEnum} Is the cardholder enrolled in 3DSecure.
     * @param enrollmentEci {String} The 3D Secure entry enrollment eci.
     * @param gatewayAccountId {String} Related gateway account ID.
     * @param paymentCardId {String} Related payment card ID.
     * @param websiteId {String} Related Website ID.
     */
    constructor(amount, currency, customerId, enrolled, enrollmentEci, gatewayAccountId, paymentCardId, websiteId) { 
        
        ThreeDSecure.initialize(this, amount, currency, customerId, enrolled, enrollmentEci, gatewayAccountId, paymentCardId, websiteId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, amount, currency, customerId, enrolled, enrollmentEci, gatewayAccountId, paymentCardId, websiteId) { 
        obj['amount'] = amount;
        obj['currency'] = currency;
        obj['customerId'] = customerId;
        obj['enrolled'] = enrolled;
        obj['enrollmentEci'] = enrollmentEci;
        obj['gatewayAccountId'] = gatewayAccountId;
        obj['paymentCardId'] = paymentCardId;
        obj['websiteId'] = websiteId;
    }

    /**
     * Constructs a <code>ThreeDSecure</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ThreeDSecure} obj Optional instance to populate.
     * @return {module:model/ThreeDSecure} The populated <code>ThreeDSecure</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ThreeDSecure();

            if (data.hasOwnProperty('_links')) {
                obj['_links'] = ApiClient.convertToType(data['_links'], [SelfLink]);
            }
            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'Number');
            }
            if (data.hasOwnProperty('cavv')) {
                obj['cavv'] = ApiClient.convertToType(data['cavv'], 'String');
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
            if (data.hasOwnProperty('eci')) {
                obj['eci'] = ApiClient.convertToType(data['eci'], 'Number');
            }
            if (data.hasOwnProperty('enrolled')) {
                obj['enrolled'] = ApiClient.convertToType(data['enrolled'], 'String');
            }
            if (data.hasOwnProperty('enrollmentEci')) {
                obj['enrollmentEci'] = ApiClient.convertToType(data['enrollmentEci'], 'String');
            }
            if (data.hasOwnProperty('gatewayAccountId')) {
                obj['gatewayAccountId'] = ApiClient.convertToType(data['gatewayAccountId'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('payerAuthResponseStatus')) {
                obj['payerAuthResponseStatus'] = ApiClient.convertToType(data['payerAuthResponseStatus'], 'String');
            }
            if (data.hasOwnProperty('paymentCardId')) {
                obj['paymentCardId'] = ApiClient.convertToType(data['paymentCardId'], 'String');
            }
            if (data.hasOwnProperty('signatureVerification')) {
                obj['signatureVerification'] = ApiClient.convertToType(data['signatureVerification'], 'String');
            }
            if (data.hasOwnProperty('websiteId')) {
                obj['websiteId'] = ApiClient.convertToType(data['websiteId'], 'String');
            }
            if (data.hasOwnProperty('xid')) {
                obj['xid'] = ApiClient.convertToType(data['xid'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ThreeDSecure</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ThreeDSecure</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ThreeDSecure.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['_links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_links'])) {
                throw new Error("Expected the field `_links` to be an array in the JSON data but got " + data['_links']);
            }
            // validate the optional field `_links` (array)
            for (const item of data['_links']) {
                SelfLink.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['cavv'] && !(typeof data['cavv'] === 'string' || data['cavv'] instanceof String)) {
            throw new Error("Expected the field `cavv` to be a primitive type in the JSON string but got " + data['cavv']);
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
        if (data['enrolled'] && !(typeof data['enrolled'] === 'string' || data['enrolled'] instanceof String)) {
            throw new Error("Expected the field `enrolled` to be a primitive type in the JSON string but got " + data['enrolled']);
        }
        // ensure the json data is a string
        if (data['enrollmentEci'] && !(typeof data['enrollmentEci'] === 'string' || data['enrollmentEci'] instanceof String)) {
            throw new Error("Expected the field `enrollmentEci` to be a primitive type in the JSON string but got " + data['enrollmentEci']);
        }
        // ensure the json data is a string
        if (data['gatewayAccountId'] && !(typeof data['gatewayAccountId'] === 'string' || data['gatewayAccountId'] instanceof String)) {
            throw new Error("Expected the field `gatewayAccountId` to be a primitive type in the JSON string but got " + data['gatewayAccountId']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['payerAuthResponseStatus'] && !(typeof data['payerAuthResponseStatus'] === 'string' || data['payerAuthResponseStatus'] instanceof String)) {
            throw new Error("Expected the field `payerAuthResponseStatus` to be a primitive type in the JSON string but got " + data['payerAuthResponseStatus']);
        }
        // ensure the json data is a string
        if (data['paymentCardId'] && !(typeof data['paymentCardId'] === 'string' || data['paymentCardId'] instanceof String)) {
            throw new Error("Expected the field `paymentCardId` to be a primitive type in the JSON string but got " + data['paymentCardId']);
        }
        // ensure the json data is a string
        if (data['signatureVerification'] && !(typeof data['signatureVerification'] === 'string' || data['signatureVerification'] instanceof String)) {
            throw new Error("Expected the field `signatureVerification` to be a primitive type in the JSON string but got " + data['signatureVerification']);
        }
        // ensure the json data is a string
        if (data['websiteId'] && !(typeof data['websiteId'] === 'string' || data['websiteId'] instanceof String)) {
            throw new Error("Expected the field `websiteId` to be a primitive type in the JSON string but got " + data['websiteId']);
        }
        // ensure the json data is a string
        if (data['xid'] && !(typeof data['xid'] === 'string' || data['xid'] instanceof String)) {
            throw new Error("Expected the field `xid` to be a primitive type in the JSON string but got " + data['xid']);
        }

        return true;
    }


}

ThreeDSecure.RequiredProperties = ["amount", "currency", "customerId", "enrolled", "enrollmentEci", "gatewayAccountId", "paymentCardId", "websiteId"];

/**
 * The links related to resource.
 * @member {Array.<module:model/SelfLink>} _links
 */
ThreeDSecure.prototype['_links'] = undefined;

/**
 * Transaction amount.
 * @member {Number} amount
 */
ThreeDSecure.prototype['amount'] = undefined;

/**
 * The 3D Secure entry cardholder authentication verification value.
 * @member {String} cavv
 */
ThreeDSecure.prototype['cavv'] = undefined;

/**
 * The 3D Secure entry created time.
 * @member {Date} createdTime
 */
ThreeDSecure.prototype['createdTime'] = undefined;

/**
 * ISO 4217 alphabetic currency code.
 * @member {String} currency
 */
ThreeDSecure.prototype['currency'] = undefined;

/**
 * Related customer ID.
 * @member {String} customerId
 */
ThreeDSecure.prototype['customerId'] = undefined;

/**
 * The 3D Secure entry electronic commerce indicator.
 * @member {Number} eci
 */
ThreeDSecure.prototype['eci'] = undefined;

/**
 * Is the cardholder enrolled in 3DSecure.
 * @member {module:model/ThreeDSecure.EnrolledEnum} enrolled
 */
ThreeDSecure.prototype['enrolled'] = undefined;

/**
 * The 3D Secure entry enrollment eci.
 * @member {String} enrollmentEci
 */
ThreeDSecure.prototype['enrollmentEci'] = undefined;

/**
 * Related gateway account ID.
 * @member {String} gatewayAccountId
 */
ThreeDSecure.prototype['gatewayAccountId'] = undefined;

/**
 * The 3D Secure entry identifier string.
 * @member {String} id
 */
ThreeDSecure.prototype['id'] = undefined;

/**
 * The 3D Secure entry Auth Response Status.
 * @member {module:model/ThreeDSecure.PayerAuthResponseStatusEnum} payerAuthResponseStatus
 */
ThreeDSecure.prototype['payerAuthResponseStatus'] = undefined;

/**
 * Related payment card ID.
 * @member {String} paymentCardId
 */
ThreeDSecure.prototype['paymentCardId'] = undefined;

/**
 * If signature was verified.
 * @member {module:model/ThreeDSecure.SignatureVerificationEnum} signatureVerification
 */
ThreeDSecure.prototype['signatureVerification'] = undefined;

/**
 * Related Website ID.
 * @member {String} websiteId
 */
ThreeDSecure.prototype['websiteId'] = undefined;

/**
 * The 3D Secure entry transaction Id.
 * @member {String} xid
 */
ThreeDSecure.prototype['xid'] = undefined;





/**
 * Allowed values for the <code>enrolled</code> property.
 * @enum {String}
 * @readonly
 */
ThreeDSecure['EnrolledEnum'] = {

    /**
     * value: "Y"
     * @const
     */
    "Y": "Y",

    /**
     * value: "N"
     * @const
     */
    "N": "N",

    /**
     * value: "U"
     * @const
     */
    "U": "U"
};


/**
 * Allowed values for the <code>payerAuthResponseStatus</code> property.
 * @enum {String}
 * @readonly
 */
ThreeDSecure['PayerAuthResponseStatusEnum'] = {

    /**
     * value: "Y"
     * @const
     */
    "Y": "Y",

    /**
     * value: "N"
     * @const
     */
    "N": "N",

    /**
     * value: "U"
     * @const
     */
    "U": "U",

    /**
     * value: "A"
     * @const
     */
    "A": "A"
};


/**
 * Allowed values for the <code>signatureVerification</code> property.
 * @enum {String}
 * @readonly
 */
ThreeDSecure['SignatureVerificationEnum'] = {

    /**
     * value: "Y"
     * @const
     */
    "Y": "Y",

    /**
     * value: "N"
     * @const
     */
    "N": "N"
};



export default ThreeDSecure;

