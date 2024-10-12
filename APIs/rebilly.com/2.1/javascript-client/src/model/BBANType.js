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
import RiskMetadata from './RiskMetadata';

/**
 * The BBANType model module.
 * @module model/BBANType
 * @version 2.1
 */
class BBANType {
    /**
     * Constructs a new <code>BBANType</code>.
     * BBAN type object.
     * @alias module:model/BBANType
     * @param accountNumber {String} Bank's account number.
     * @param accountNumberType {module:model/BBANType.AccountNumberTypeEnum} Bank's Account Number type. A valid value is basic bank account number (BBAN) or international bank account number (IBAN). This is the object for the BBAN.
     * @param accountType {module:model/BBANType.AccountTypeEnum} Bank's account type.
     * @param billingAddress {module:model/ContactObject} The billing address.
     * @param customerId {String} Customer's ID.
     * @param method {module:model/BBANType.MethodEnum} The method of payment instrument.
     * @param routingNumber {String} Bank's routing number.
     */
    constructor(accountNumber, accountNumberType, accountType, billingAddress, customerId, method, routingNumber) { 
        
        BBANType.initialize(this, accountNumber, accountNumberType, accountType, billingAddress, customerId, method, routingNumber);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, accountNumber, accountNumberType, accountType, billingAddress, customerId, method, routingNumber) { 
        obj['accountNumber'] = accountNumber;
        obj['accountNumberType'] = accountNumberType || 'BBAN';
        obj['accountType'] = accountType;
        obj['billingAddress'] = billingAddress;
        obj['customerId'] = customerId;
        obj['method'] = method;
        obj['routingNumber'] = routingNumber;
    }

    /**
     * Constructs a <code>BBANType</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BBANType} obj Optional instance to populate.
     * @return {module:model/BBANType} The populated <code>BBANType</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BBANType();

            if (data.hasOwnProperty('accountNumber')) {
                obj['accountNumber'] = ApiClient.convertToType(data['accountNumber'], 'String');
            }
            if (data.hasOwnProperty('accountNumberType')) {
                obj['accountNumberType'] = ApiClient.convertToType(data['accountNumberType'], 'String');
            }
            if (data.hasOwnProperty('accountType')) {
                obj['accountType'] = ApiClient.convertToType(data['accountType'], 'String');
            }
            if (data.hasOwnProperty('bankName')) {
                obj['bankName'] = ApiClient.convertToType(data['bankName'], 'String');
            }
            if (data.hasOwnProperty('bic')) {
                obj['bic'] = ApiClient.convertToType(data['bic'], 'String');
            }
            if (data.hasOwnProperty('billingAddress')) {
                obj['billingAddress'] = ApiClient.convertToType(data['billingAddress'], ContactObject);
            }
            if (data.hasOwnProperty('customFields')) {
                obj['customFields'] = ApiClient.convertToType(data['customFields'], Object);
            }
            if (data.hasOwnProperty('customerId')) {
                obj['customerId'] = ApiClient.convertToType(data['customerId'], 'String');
            }
            if (data.hasOwnProperty('method')) {
                obj['method'] = ApiClient.convertToType(data['method'], 'String');
            }
            if (data.hasOwnProperty('riskMetadata')) {
                obj['riskMetadata'] = RiskMetadata.constructFromObject(data['riskMetadata']);
            }
            if (data.hasOwnProperty('routingNumber')) {
                obj['routingNumber'] = ApiClient.convertToType(data['routingNumber'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BBANType</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BBANType</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BBANType.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['accountNumber'] && !(typeof data['accountNumber'] === 'string' || data['accountNumber'] instanceof String)) {
            throw new Error("Expected the field `accountNumber` to be a primitive type in the JSON string but got " + data['accountNumber']);
        }
        // ensure the json data is a string
        if (data['accountNumberType'] && !(typeof data['accountNumberType'] === 'string' || data['accountNumberType'] instanceof String)) {
            throw new Error("Expected the field `accountNumberType` to be a primitive type in the JSON string but got " + data['accountNumberType']);
        }
        // ensure the json data is a string
        if (data['accountType'] && !(typeof data['accountType'] === 'string' || data['accountType'] instanceof String)) {
            throw new Error("Expected the field `accountType` to be a primitive type in the JSON string but got " + data['accountType']);
        }
        // ensure the json data is a string
        if (data['bankName'] && !(typeof data['bankName'] === 'string' || data['bankName'] instanceof String)) {
            throw new Error("Expected the field `bankName` to be a primitive type in the JSON string but got " + data['bankName']);
        }
        // ensure the json data is a string
        if (data['bic'] && !(typeof data['bic'] === 'string' || data['bic'] instanceof String)) {
            throw new Error("Expected the field `bic` to be a primitive type in the JSON string but got " + data['bic']);
        }
        // validate the optional field `billingAddress`
        if (data['billingAddress']) { // data not null
          ContactObject.validateJSON(data['billingAddress']);
        }
        // ensure the json data is a string
        if (data['customerId'] && !(typeof data['customerId'] === 'string' || data['customerId'] instanceof String)) {
            throw new Error("Expected the field `customerId` to be a primitive type in the JSON string but got " + data['customerId']);
        }
        // ensure the json data is a string
        if (data['method'] && !(typeof data['method'] === 'string' || data['method'] instanceof String)) {
            throw new Error("Expected the field `method` to be a primitive type in the JSON string but got " + data['method']);
        }
        // validate the optional field `riskMetadata`
        if (data['riskMetadata']) { // data not null
          RiskMetadata.validateJSON(data['riskMetadata']);
        }
        // ensure the json data is a string
        if (data['routingNumber'] && !(typeof data['routingNumber'] === 'string' || data['routingNumber'] instanceof String)) {
            throw new Error("Expected the field `routingNumber` to be a primitive type in the JSON string but got " + data['routingNumber']);
        }

        return true;
    }


}

BBANType.RequiredProperties = ["accountNumber", "accountNumberType", "accountType", "billingAddress", "customerId", "method", "routingNumber"];

/**
 * Bank's account number.
 * @member {String} accountNumber
 */
BBANType.prototype['accountNumber'] = undefined;

/**
 * Bank's Account Number type. A valid value is basic bank account number (BBAN) or international bank account number (IBAN). This is the object for the BBAN.
 * @member {module:model/BBANType.AccountNumberTypeEnum} accountNumberType
 * @default 'BBAN'
 */
BBANType.prototype['accountNumberType'] = 'BBAN';

/**
 * Bank's account type.
 * @member {module:model/BBANType.AccountTypeEnum} accountType
 */
BBANType.prototype['accountType'] = undefined;

/**
 * Bank's name.
 * @member {String} bankName
 */
BBANType.prototype['bankName'] = undefined;

/**
 * Bank Identifier Code.
 * @member {String} bic
 */
BBANType.prototype['bic'] = undefined;

/**
 * The billing address.
 * @member {module:model/ContactObject} billingAddress
 */
BBANType.prototype['billingAddress'] = undefined;

/**
 * Custom Fields list as a map `{\"custom field name\": \"custom field value\", ...}`. The format must follow the saved format (see Custom Fields section for the formats). 
 * @member {Object} customFields
 */
BBANType.prototype['customFields'] = undefined;

/**
 * Customer's ID.
 * @member {String} customerId
 */
BBANType.prototype['customerId'] = undefined;

/**
 * The method of payment instrument.
 * @member {module:model/BBANType.MethodEnum} method
 */
BBANType.prototype['method'] = undefined;

/**
 * @member {module:model/RiskMetadata} riskMetadata
 */
BBANType.prototype['riskMetadata'] = undefined;

/**
 * Bank's routing number.
 * @member {String} routingNumber
 */
BBANType.prototype['routingNumber'] = undefined;





/**
 * Allowed values for the <code>accountNumberType</code> property.
 * @enum {String}
 * @readonly
 */
BBANType['AccountNumberTypeEnum'] = {

    /**
     * value: "IBAN"
     * @const
     */
    "IBAN": "IBAN",

    /**
     * value: "BBAN"
     * @const
     */
    "BBAN": "BBAN"
};


/**
 * Allowed values for the <code>accountType</code> property.
 * @enum {String}
 * @readonly
 */
BBANType['AccountTypeEnum'] = {

    /**
     * value: "checking"
     * @const
     */
    "checking": "checking",

    /**
     * value: "savings"
     * @const
     */
    "savings": "savings",

    /**
     * value: "other"
     * @const
     */
    "other": "other"
};


/**
 * Allowed values for the <code>method</code> property.
 * @enum {String}
 * @readonly
 */
BBANType['MethodEnum'] = {

    /**
     * value: "ach"
     * @const
     */
    "ach": "ach"
};



export default BBANType;

