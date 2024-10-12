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
import PaymentCardBrand from './PaymentCardBrand';
import RiskMetadata from './RiskMetadata';

/**
 * The CommonPaymentCard model module.
 * @module model/CommonPaymentCard
 * @version 2.1
 */
class CommonPaymentCard {
    /**
     * Constructs a new <code>CommonPaymentCard</code>.
     * @alias module:model/CommonPaymentCard
     */
    constructor() { 
        
        CommonPaymentCard.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CommonPaymentCard</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CommonPaymentCard} obj Optional instance to populate.
     * @return {module:model/CommonPaymentCard} The populated <code>CommonPaymentCard</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CommonPaymentCard();

            if (data.hasOwnProperty('bankCountry')) {
                obj['bankCountry'] = ApiClient.convertToType(data['bankCountry'], 'String');
            }
            if (data.hasOwnProperty('bankName')) {
                obj['bankName'] = ApiClient.convertToType(data['bankName'], 'String');
            }
            if (data.hasOwnProperty('billingAddress')) {
                obj['billingAddress'] = ApiClient.convertToType(data['billingAddress'], ContactObject);
            }
            if (data.hasOwnProperty('bin')) {
                obj['bin'] = ApiClient.convertToType(data['bin'], 'String');
            }
            if (data.hasOwnProperty('brand')) {
                obj['brand'] = ApiClient.convertToType(data['brand'], PaymentCardBrand);
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('customFields')) {
                obj['customFields'] = ApiClient.convertToType(data['customFields'], Object);
            }
            if (data.hasOwnProperty('customerId')) {
                obj['customerId'] = ApiClient.convertToType(data['customerId'], 'String');
            }
            if (data.hasOwnProperty('cvv')) {
                obj['cvv'] = ApiClient.convertToType(data['cvv'], 'String');
            }
            if (data.hasOwnProperty('expMonth')) {
                obj['expMonth'] = ApiClient.convertToType(data['expMonth'], 'Number');
            }
            if (data.hasOwnProperty('expYear')) {
                obj['expYear'] = ApiClient.convertToType(data['expYear'], 'Number');
            }
            if (data.hasOwnProperty('fingerprint')) {
                obj['fingerprint'] = ApiClient.convertToType(data['fingerprint'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('last4')) {
                obj['last4'] = ApiClient.convertToType(data['last4'], 'String');
            }
            if (data.hasOwnProperty('method')) {
                obj['method'] = ApiClient.convertToType(data['method'], 'String');
            }
            if (data.hasOwnProperty('pan')) {
                obj['pan'] = ApiClient.convertToType(data['pan'], 'String');
            }
            if (data.hasOwnProperty('riskMetadata')) {
                obj['riskMetadata'] = RiskMetadata.constructFromObject(data['riskMetadata']);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('updatedTime')) {
                obj['updatedTime'] = ApiClient.convertToType(data['updatedTime'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CommonPaymentCard</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CommonPaymentCard</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['bankCountry'] && !(typeof data['bankCountry'] === 'string' || data['bankCountry'] instanceof String)) {
            throw new Error("Expected the field `bankCountry` to be a primitive type in the JSON string but got " + data['bankCountry']);
        }
        // ensure the json data is a string
        if (data['bankName'] && !(typeof data['bankName'] === 'string' || data['bankName'] instanceof String)) {
            throw new Error("Expected the field `bankName` to be a primitive type in the JSON string but got " + data['bankName']);
        }
        // validate the optional field `billingAddress`
        if (data['billingAddress']) { // data not null
          ContactObject.validateJSON(data['billingAddress']);
        }
        // ensure the json data is a string
        if (data['bin'] && !(typeof data['bin'] === 'string' || data['bin'] instanceof String)) {
            throw new Error("Expected the field `bin` to be a primitive type in the JSON string but got " + data['bin']);
        }
        // ensure the json data is a string
        if (data['customerId'] && !(typeof data['customerId'] === 'string' || data['customerId'] instanceof String)) {
            throw new Error("Expected the field `customerId` to be a primitive type in the JSON string but got " + data['customerId']);
        }
        // ensure the json data is a string
        if (data['cvv'] && !(typeof data['cvv'] === 'string' || data['cvv'] instanceof String)) {
            throw new Error("Expected the field `cvv` to be a primitive type in the JSON string but got " + data['cvv']);
        }
        // ensure the json data is a string
        if (data['fingerprint'] && !(typeof data['fingerprint'] === 'string' || data['fingerprint'] instanceof String)) {
            throw new Error("Expected the field `fingerprint` to be a primitive type in the JSON string but got " + data['fingerprint']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['last4'] && !(typeof data['last4'] === 'string' || data['last4'] instanceof String)) {
            throw new Error("Expected the field `last4` to be a primitive type in the JSON string but got " + data['last4']);
        }
        // ensure the json data is a string
        if (data['method'] && !(typeof data['method'] === 'string' || data['method'] instanceof String)) {
            throw new Error("Expected the field `method` to be a primitive type in the JSON string but got " + data['method']);
        }
        // ensure the json data is a string
        if (data['pan'] && !(typeof data['pan'] === 'string' || data['pan'] instanceof String)) {
            throw new Error("Expected the field `pan` to be a primitive type in the JSON string but got " + data['pan']);
        }
        // validate the optional field `riskMetadata`
        if (data['riskMetadata']) { // data not null
          RiskMetadata.validateJSON(data['riskMetadata']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * Payment instrument bank country.
 * @member {String} bankCountry
 */
CommonPaymentCard.prototype['bankCountry'] = undefined;

/**
 * Payment instrument bank name.
 * @member {String} bankName
 */
CommonPaymentCard.prototype['bankName'] = undefined;

/**
 * The billing address.
 * @member {module:model/ContactObject} billingAddress
 */
CommonPaymentCard.prototype['billingAddress'] = undefined;

/**
 * The card's bin (the PAN's first 6 digits).
 * @member {String} bin
 */
CommonPaymentCard.prototype['bin'] = undefined;

/**
 * @member {module:model/PaymentCardBrand} brand
 */
CommonPaymentCard.prototype['brand'] = undefined;

/**
 * Payment instrument created time.
 * @member {Date} createdTime
 */
CommonPaymentCard.prototype['createdTime'] = undefined;

/**
 * Custom Fields list as a map `{\"custom field name\": \"custom field value\", ...}`. The format must follow the saved format (see Custom Fields section for the formats). 
 * @member {Object} customFields
 */
CommonPaymentCard.prototype['customFields'] = undefined;

/**
 * The сustomer's ID.
 * @member {String} customerId
 */
CommonPaymentCard.prototype['customerId'] = undefined;

/**
 * Card's cvv (card verification value).
 * @member {String} cvv
 */
CommonPaymentCard.prototype['cvv'] = undefined;

/**
 * Card's expiration month.
 * @member {Number} expMonth
 */
CommonPaymentCard.prototype['expMonth'] = undefined;

/**
 * Card's expiration year.
 * @member {Number} expYear
 */
CommonPaymentCard.prototype['expYear'] = undefined;

/**
 * A unique value to identify the payment instrument regardless of variable values. It contains alphanumeric values.
 * @member {String} fingerprint
 */
CommonPaymentCard.prototype['fingerprint'] = undefined;

/**
 * The payment instrument ID.
 * @member {String} id
 */
CommonPaymentCard.prototype['id'] = undefined;

/**
 * The PAN's last 4 digits.
 * @member {String} last4
 */
CommonPaymentCard.prototype['last4'] = undefined;

/**
 * The method of payment instrument.
 * @member {module:model/CommonPaymentCard.MethodEnum} method
 */
CommonPaymentCard.prototype['method'] = undefined;

/**
 * The card PAN (primary account number).
 * @member {String} pan
 */
CommonPaymentCard.prototype['pan'] = undefined;

/**
 * @member {module:model/RiskMetadata} riskMetadata
 */
CommonPaymentCard.prototype['riskMetadata'] = undefined;

/**
 * Payment instrument status. When an instrument is `active` it means it has been used at least once for an approved transaction. To remove an instrument from being in use, set it as `deactivated` (see the deactivation endpoint). 
 * @member {module:model/CommonPaymentCard.StatusEnum} status
 */
CommonPaymentCard.prototype['status'] = undefined;

/**
 * Payment instrument updated time.
 * @member {Date} updatedTime
 */
CommonPaymentCard.prototype['updatedTime'] = undefined;





/**
 * Allowed values for the <code>method</code> property.
 * @enum {String}
 * @readonly
 */
CommonPaymentCard['MethodEnum'] = {

    /**
     * value: "payment-card"
     * @const
     */
    "payment-card": "payment-card"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
CommonPaymentCard['StatusEnum'] = {

    /**
     * value: "active"
     * @const
     */
    "active": "active",

    /**
     * value: "inactive"
     * @const
     */
    "inactive": "inactive",

    /**
     * value: "expired"
     * @const
     */
    "expired": "expired",

    /**
     * value: "deactivated"
     * @const
     */
    "deactivated": "deactivated",

    /**
     * value: "verification-needed"
     * @const
     */
    "verification-needed": "verification-needed"
};



export default CommonPaymentCard;

