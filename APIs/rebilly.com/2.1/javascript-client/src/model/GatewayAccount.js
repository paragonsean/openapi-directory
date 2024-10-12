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
import AcquirerName from './AcquirerName';
import DigitalWallets from './DigitalWallets';
import GatewayAccountLinksInner from './GatewayAccountLinksInner';
import GatewayName from './GatewayName';
import PaymentCardBrand from './PaymentCardBrand';
import PaymentMethod from './PaymentMethod';

/**
 * The GatewayAccount model module.
 * @module model/GatewayAccount
 * @version 2.1
 */
class GatewayAccount {
    /**
     * Constructs a new <code>GatewayAccount</code>.
     * @alias module:model/GatewayAccount
     * @param acceptedCurrencies {Array.<String>} Accepted currencies (array of the currency three letter codes).
     * @param gatewayName {module:model/GatewayName} 
     * @param method {module:model/PaymentMethod} 
     */
    constructor(acceptedCurrencies, gatewayName, method) { 
        
        GatewayAccount.initialize(this, acceptedCurrencies, gatewayName, method);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, acceptedCurrencies, gatewayName, method) { 
        obj['acceptedCurrencies'] = acceptedCurrencies;
        obj['approvalWindowTtl'] = 3600;
        obj['dynamicDescriptor'] = false;
        obj['gatewayName'] = gatewayName;
        obj['merchantCategoryCode'] = '0000';
        obj['method'] = method;
        obj['reconciliationWindowEnabled'] = false;
        obj['sticky'] = true;
        obj['threeDSecure'] = false;
    }

    /**
     * Constructs a <code>GatewayAccount</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GatewayAccount} obj Optional instance to populate.
     * @return {module:model/GatewayAccount} The populated <code>GatewayAccount</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GatewayAccount();

            if (data.hasOwnProperty('_links')) {
                obj['_links'] = ApiClient.convertToType(data['_links'], [GatewayAccountLinksInner]);
            }
            if (data.hasOwnProperty('acceptedCurrencies')) {
                obj['acceptedCurrencies'] = ApiClient.convertToType(data['acceptedCurrencies'], ['String']);
            }
            if (data.hasOwnProperty('acquirerName')) {
                obj['acquirerName'] = ApiClient.convertToType(data['acquirerName'], AcquirerName);
            }
            if (data.hasOwnProperty('additionalFilters')) {
                obj['additionalFilters'] = ApiClient.convertToType(data['additionalFilters'], 'String');
            }
            if (data.hasOwnProperty('approvalWindowTtl')) {
                obj['approvalWindowTtl'] = ApiClient.convertToType(data['approvalWindowTtl'], 'Number');
            }
            if (data.hasOwnProperty('cityField')) {
                obj['cityField'] = ApiClient.convertToType(data['cityField'], 'String');
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('dccForceCurrency')) {
                obj['dccForceCurrency'] = ApiClient.convertToType(data['dccForceCurrency'], 'String');
            }
            if (data.hasOwnProperty('dccMarkup')) {
                obj['dccMarkup'] = ApiClient.convertToType(data['dccMarkup'], 'Number');
            }
            if (data.hasOwnProperty('descriptor')) {
                obj['descriptor'] = ApiClient.convertToType(data['descriptor'], 'String');
            }
            if (data.hasOwnProperty('digitalWallets')) {
                obj['digitalWallets'] = DigitalWallets.constructFromObject(data['digitalWallets']);
            }
            if (data.hasOwnProperty('dynamicDescriptor')) {
                obj['dynamicDescriptor'] = ApiClient.convertToType(data['dynamicDescriptor'], 'Boolean');
            }
            if (data.hasOwnProperty('excludedDccQuoteCurrencies')) {
                obj['excludedDccQuoteCurrencies'] = ApiClient.convertToType(data['excludedDccQuoteCurrencies'], ['String']);
            }
            if (data.hasOwnProperty('gatewayName')) {
                obj['gatewayName'] = GatewayName.constructFromObject(data['gatewayName']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('isDown')) {
                obj['isDown'] = ApiClient.convertToType(data['isDown'], 'Boolean');
            }
            if (data.hasOwnProperty('merchantCategoryCode')) {
                obj['merchantCategoryCode'] = ApiClient.convertToType(data['merchantCategoryCode'], 'String');
            }
            if (data.hasOwnProperty('method')) {
                obj['method'] = PaymentMethod.constructFromObject(data['method']);
            }
            if (data.hasOwnProperty('monthlyLimit')) {
                obj['monthlyLimit'] = ApiClient.convertToType(data['monthlyLimit'], 'Number');
            }
            if (data.hasOwnProperty('organizationId')) {
                obj['organizationId'] = ApiClient.convertToType(data['organizationId'], 'String');
            }
            if (data.hasOwnProperty('paymentCardSchemes')) {
                obj['paymentCardSchemes'] = ApiClient.convertToType(data['paymentCardSchemes'], [PaymentCardBrand]);
            }
            if (data.hasOwnProperty('reconciliationWindowEnabled')) {
                obj['reconciliationWindowEnabled'] = ApiClient.convertToType(data['reconciliationWindowEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('reconciliationWindowTtl')) {
                obj['reconciliationWindowTtl'] = ApiClient.convertToType(data['reconciliationWindowTtl'], 'Number');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('sticky')) {
                obj['sticky'] = ApiClient.convertToType(data['sticky'], 'Boolean');
            }
            if (data.hasOwnProperty('threeDSecure')) {
                obj['threeDSecure'] = ApiClient.convertToType(data['threeDSecure'], 'Boolean');
            }
            if (data.hasOwnProperty('timeout')) {
                obj['timeout'] = ApiClient.convertToType(data['timeout'], 'Number');
            }
            if (data.hasOwnProperty('token')) {
                obj['token'] = ApiClient.convertToType(data['token'], 'String');
            }
            if (data.hasOwnProperty('updatedTime')) {
                obj['updatedTime'] = ApiClient.convertToType(data['updatedTime'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GatewayAccount</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GatewayAccount</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GatewayAccount.RequiredProperties) {
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
                GatewayAccountLinksInner.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['acceptedCurrencies'])) {
            throw new Error("Expected the field `acceptedCurrencies` to be an array in the JSON data but got " + data['acceptedCurrencies']);
        }
        // ensure the json data is a string
        if (data['additionalFilters'] && !(typeof data['additionalFilters'] === 'string' || data['additionalFilters'] instanceof String)) {
            throw new Error("Expected the field `additionalFilters` to be a primitive type in the JSON string but got " + data['additionalFilters']);
        }
        // ensure the json data is a string
        if (data['cityField'] && !(typeof data['cityField'] === 'string' || data['cityField'] instanceof String)) {
            throw new Error("Expected the field `cityField` to be a primitive type in the JSON string but got " + data['cityField']);
        }
        // ensure the json data is a string
        if (data['dccForceCurrency'] && !(typeof data['dccForceCurrency'] === 'string' || data['dccForceCurrency'] instanceof String)) {
            throw new Error("Expected the field `dccForceCurrency` to be a primitive type in the JSON string but got " + data['dccForceCurrency']);
        }
        // ensure the json data is a string
        if (data['descriptor'] && !(typeof data['descriptor'] === 'string' || data['descriptor'] instanceof String)) {
            throw new Error("Expected the field `descriptor` to be a primitive type in the JSON string but got " + data['descriptor']);
        }
        // validate the optional field `digitalWallets`
        if (data['digitalWallets']) { // data not null
          DigitalWallets.validateJSON(data['digitalWallets']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['excludedDccQuoteCurrencies'])) {
            throw new Error("Expected the field `excludedDccQuoteCurrencies` to be an array in the JSON data but got " + data['excludedDccQuoteCurrencies']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['merchantCategoryCode'] && !(typeof data['merchantCategoryCode'] === 'string' || data['merchantCategoryCode'] instanceof String)) {
            throw new Error("Expected the field `merchantCategoryCode` to be a primitive type in the JSON string but got " + data['merchantCategoryCode']);
        }
        // ensure the json data is a string
        if (data['organizationId'] && !(typeof data['organizationId'] === 'string' || data['organizationId'] instanceof String)) {
            throw new Error("Expected the field `organizationId` to be a primitive type in the JSON string but got " + data['organizationId']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['paymentCardSchemes'])) {
            throw new Error("Expected the field `paymentCardSchemes` to be an array in the JSON data but got " + data['paymentCardSchemes']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['token'] && !(typeof data['token'] === 'string' || data['token'] instanceof String)) {
            throw new Error("Expected the field `token` to be a primitive type in the JSON string but got " + data['token']);
        }

        return true;
    }


}

GatewayAccount.RequiredProperties = ["acceptedCurrencies", "gatewayName", "method"];

/**
 * The links related to resource.
 * @member {Array.<module:model/GatewayAccountLinksInner>} _links
 */
GatewayAccount.prototype['_links'] = undefined;

/**
 * Accepted currencies (array of the currency three letter codes).
 * @member {Array.<String>} acceptedCurrencies
 */
GatewayAccount.prototype['acceptedCurrencies'] = undefined;

/**
 * @member {module:model/AcquirerName} acquirerName
 */
GatewayAccount.prototype['acquirerName'] = undefined;

/**
 * The additional filters are used to determine whether the gateway account can be selected for the transaction to be processed. For example, the filter may put a maximum amount value. If the transaction is above that amount, this gateway account wouldn't be used. This follows our standard filter format. 
 * @member {String} additionalFilters
 */
GatewayAccount.prototype['additionalFilters'] = undefined;

/**
 * The time window (in seconds) allotted for approving an offsite transaction before it is automatically `abandoned`.
 * @member {Number} approvalWindowTtl
 * @default 3600
 */
GatewayAccount.prototype['approvalWindowTtl'] = 3600;

/**
 * The gateway account's city field (also known as line 2 descriptor).
 * @member {String} cityField
 */
GatewayAccount.prototype['cityField'] = undefined;

/**
 * Gateway Account created time.
 * @member {Date} createdTime
 */
GatewayAccount.prototype['createdTime'] = undefined;

/**
 * Force dynamic currency conversion to the specified currency on each sale. Leave it empty to disable force DCC. 
 * @member {String} dccForceCurrency
 */
GatewayAccount.prototype['dccForceCurrency'] = undefined;

/**
 * Dynamic currency conversion markup in basis points.
 * @member {Number} dccMarkup
 */
GatewayAccount.prototype['dccMarkup'] = undefined;

/**
 * The gateway account's descriptor.
 * @member {String} descriptor
 */
GatewayAccount.prototype['descriptor'] = undefined;

/**
 * @member {module:model/DigitalWallets} digitalWallets
 */
GatewayAccount.prototype['digitalWallets'] = undefined;

/**
 * True, if Gateway Account allows dynamic descriptor.
 * @member {Boolean} dynamicDescriptor
 * @default false
 */
GatewayAccount.prototype['dynamicDescriptor'] = false;

/**
 * Excluded Dynamic Currency Conversion Quote Currencies.
 * @member {Array.<String>} excludedDccQuoteCurrencies
 */
GatewayAccount.prototype['excludedDccQuoteCurrencies'] = undefined;

/**
 * @member {module:model/GatewayName} gatewayName
 */
GatewayAccount.prototype['gatewayName'] = undefined;

/**
 * The gateway identifier string.
 * @member {String} id
 */
GatewayAccount.prototype['id'] = undefined;

/**
 * True if gateway is currently in downtime period.
 * @member {Boolean} isDown
 */
GatewayAccount.prototype['isDown'] = undefined;

/**
 * The gateway account's merchant category code.
 * @member {String} merchantCategoryCode
 * @default '0000'
 */
GatewayAccount.prototype['merchantCategoryCode'] = '0000';

/**
 * @member {module:model/PaymentMethod} method
 */
GatewayAccount.prototype['method'] = undefined;

/**
 * Monthly Limit.
 * @member {Number} monthlyLimit
 */
GatewayAccount.prototype['monthlyLimit'] = undefined;

/**
 * Organization ID.
 * @member {String} organizationId
 */
GatewayAccount.prototype['organizationId'] = undefined;

/**
 * Accepted payment card brands.
 * @member {Array.<module:model/PaymentCardBrand>} paymentCardSchemes
 */
GatewayAccount.prototype['paymentCardSchemes'] = undefined;

/**
 * If a transaction is not reconciled within the `reconciliationWindowTtl` time, then the transaction is marked as `abandoned`.
 * @member {Boolean} reconciliationWindowEnabled
 * @default false
 */
GatewayAccount.prototype['reconciliationWindowEnabled'] = false;

/**
 * The time window (in seconds) allotted for a reconciliation to occur. If it is not reconciled in that time, then the transaction is marked as `abandoned`.
 * @member {Number} reconciliationWindowTtl
 */
GatewayAccount.prototype['reconciliationWindowTtl'] = undefined;

/**
 * The gateway account's status.
 * @member {module:model/GatewayAccount.StatusEnum} status
 */
GatewayAccount.prototype['status'] = undefined;

/**
 * Customer's payment instrument will \"stick\" to the gateway account for future transactions when enabled.
 * @member {Boolean} sticky
 * @default true
 */
GatewayAccount.prototype['sticky'] = true;

/**
 * True, if Gateway Account allows 3DSecure.
 * @member {Boolean} threeDSecure
 * @default false
 */
GatewayAccount.prototype['threeDSecure'] = false;

/**
 * Gateway Account request timeout in seconds.
 * @member {Number} timeout
 */
GatewayAccount.prototype['timeout'] = undefined;

/**
 * Gateway Account token.
 * @member {String} token
 */
GatewayAccount.prototype['token'] = undefined;

/**
 * Gateway Account updated time.
 * @member {Date} updatedTime
 */
GatewayAccount.prototype['updatedTime'] = undefined;





/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
GatewayAccount['StatusEnum'] = {

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
     * value: "pending"
     * @const
     */
    "pending": "pending",

    /**
     * value: "closed"
     * @const
     */
    "closed": "closed"
};



export default GatewayAccount;

