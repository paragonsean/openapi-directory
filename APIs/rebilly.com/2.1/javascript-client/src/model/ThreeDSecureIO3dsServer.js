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
import EMS3dsServers from './EMS3dsServers';
import TestProcessor3dsServers from './TestProcessor3dsServers';
import ThreeDSecureServerName from './ThreeDSecureServerName';
import WorldlineAtosFrankfurt3dsServers from './WorldlineAtosFrankfurt3dsServers';

/**
 * The ThreeDSecureIO3dsServer model module.
 * @module model/ThreeDSecureIO3dsServer
 * @version 2.1
 */
class ThreeDSecureIO3dsServer {
    /**
     * Constructs a new <code>ThreeDSecureIO3dsServer</code>.
     * ThreeDSecureIO3dsServer.
     * @alias module:model/ThreeDSecureIO3dsServer
     * @extends module:model/WorldlineAtosFrankfurt3dsServers
     * @implements module:model/WorldlineAtosFrankfurt3dsServers
     * @implements module:model/TestProcessor3dsServers
     * @implements module:model/EMS3dsServers
     * @param name {module:model/ThreeDSecureServerName} 
     * @param merchantAcquirerBinMastercard {String} Mastercard Acquirer BIN.
     * @param merchantAcquirerBinVisa {String} Visa Acquirer BIN.
     * @param merchantCountry {String} Merchant Country ISO Alpha-2 Code.
     * @param merchantId {String} Merchant Id.
     * @param merchantName {String} Merchant Name.
     * @param merchantUrl {String} Merchant URL.
     */
    constructor(name, merchantAcquirerBinMastercard, merchantAcquirerBinVisa, merchantCountry, merchantId, merchantName, merchantUrl) { 
        WorldlineAtosFrankfurt3dsServers.initialize(this, name);TestProcessor3dsServers.initialize(this, name);EMS3dsServers.initialize(this, name);
        ThreeDSecureIO3dsServer.initialize(this, name, merchantAcquirerBinMastercard, merchantAcquirerBinVisa, merchantCountry, merchantId, merchantName, merchantUrl);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name, merchantAcquirerBinMastercard, merchantAcquirerBinVisa, merchantCountry, merchantId, merchantName, merchantUrl) { 
        obj['name'] = name;
        obj['merchantAcquirerBinMastercard'] = merchantAcquirerBinMastercard;
        obj['merchantAcquirerBinVisa'] = merchantAcquirerBinVisa;
        obj['merchantCountry'] = merchantCountry;
        obj['merchantId'] = merchantId;
        obj['merchantName'] = merchantName;
        obj['merchantUrl'] = merchantUrl;
    }

    /**
     * Constructs a <code>ThreeDSecureIO3dsServer</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ThreeDSecureIO3dsServer} obj Optional instance to populate.
     * @return {module:model/ThreeDSecureIO3dsServer} The populated <code>ThreeDSecureIO3dsServer</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ThreeDSecureIO3dsServer();
            WorldlineAtosFrankfurt3dsServers.constructFromObject(data, obj);
            WorldlineAtosFrankfurt3dsServers.constructFromObject(data, obj);
            TestProcessor3dsServers.constructFromObject(data, obj);
            EMS3dsServers.constructFromObject(data, obj);

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], ThreeDSecureServerName);
            }
            if (data.hasOwnProperty('merchantAcquirerBinMastercard')) {
                obj['merchantAcquirerBinMastercard'] = ApiClient.convertToType(data['merchantAcquirerBinMastercard'], 'String');
            }
            if (data.hasOwnProperty('merchantAcquirerBinVisa')) {
                obj['merchantAcquirerBinVisa'] = ApiClient.convertToType(data['merchantAcquirerBinVisa'], 'String');
            }
            if (data.hasOwnProperty('merchantCountry')) {
                obj['merchantCountry'] = ApiClient.convertToType(data['merchantCountry'], 'String');
            }
            if (data.hasOwnProperty('merchantId')) {
                obj['merchantId'] = ApiClient.convertToType(data['merchantId'], 'String');
            }
            if (data.hasOwnProperty('merchantName')) {
                obj['merchantName'] = ApiClient.convertToType(data['merchantName'], 'String');
            }
            if (data.hasOwnProperty('merchantUrl')) {
                obj['merchantUrl'] = ApiClient.convertToType(data['merchantUrl'], 'String');
            }
            if (data.hasOwnProperty('transactionType')) {
                obj['transactionType'] = ApiClient.convertToType(data['transactionType'], 'String');
            }
            if (data.hasOwnProperty('v1')) {
                obj['v1'] = ApiClient.convertToType(data['v1'], 'Boolean');
            }
            if (data.hasOwnProperty('v2')) {
                obj['v2'] = ApiClient.convertToType(data['v2'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ThreeDSecureIO3dsServer</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ThreeDSecureIO3dsServer</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ThreeDSecureIO3dsServer.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['merchantAcquirerBinMastercard'] && !(typeof data['merchantAcquirerBinMastercard'] === 'string' || data['merchantAcquirerBinMastercard'] instanceof String)) {
            throw new Error("Expected the field `merchantAcquirerBinMastercard` to be a primitive type in the JSON string but got " + data['merchantAcquirerBinMastercard']);
        }
        // ensure the json data is a string
        if (data['merchantAcquirerBinVisa'] && !(typeof data['merchantAcquirerBinVisa'] === 'string' || data['merchantAcquirerBinVisa'] instanceof String)) {
            throw new Error("Expected the field `merchantAcquirerBinVisa` to be a primitive type in the JSON string but got " + data['merchantAcquirerBinVisa']);
        }
        // ensure the json data is a string
        if (data['merchantCountry'] && !(typeof data['merchantCountry'] === 'string' || data['merchantCountry'] instanceof String)) {
            throw new Error("Expected the field `merchantCountry` to be a primitive type in the JSON string but got " + data['merchantCountry']);
        }
        // ensure the json data is a string
        if (data['merchantId'] && !(typeof data['merchantId'] === 'string' || data['merchantId'] instanceof String)) {
            throw new Error("Expected the field `merchantId` to be a primitive type in the JSON string but got " + data['merchantId']);
        }
        // ensure the json data is a string
        if (data['merchantName'] && !(typeof data['merchantName'] === 'string' || data['merchantName'] instanceof String)) {
            throw new Error("Expected the field `merchantName` to be a primitive type in the JSON string but got " + data['merchantName']);
        }
        // ensure the json data is a string
        if (data['merchantUrl'] && !(typeof data['merchantUrl'] === 'string' || data['merchantUrl'] instanceof String)) {
            throw new Error("Expected the field `merchantUrl` to be a primitive type in the JSON string but got " + data['merchantUrl']);
        }
        // ensure the json data is a string
        if (data['transactionType'] && !(typeof data['transactionType'] === 'string' || data['transactionType'] instanceof String)) {
            throw new Error("Expected the field `transactionType` to be a primitive type in the JSON string but got " + data['transactionType']);
        }

        return true;
    }


}

ThreeDSecureIO3dsServer.RequiredProperties = ["name", "merchantAcquirerBinMastercard", "merchantAcquirerBinVisa", "merchantCountry", "merchantId", "merchantName", "merchantUrl"];

/**
 * @member {module:model/ThreeDSecureServerName} name
 */
ThreeDSecureIO3dsServer.prototype['name'] = undefined;

/**
 * Mastercard Acquirer BIN.
 * @member {String} merchantAcquirerBinMastercard
 */
ThreeDSecureIO3dsServer.prototype['merchantAcquirerBinMastercard'] = undefined;

/**
 * Visa Acquirer BIN.
 * @member {String} merchantAcquirerBinVisa
 */
ThreeDSecureIO3dsServer.prototype['merchantAcquirerBinVisa'] = undefined;

/**
 * Merchant Country ISO Alpha-2 Code.
 * @member {String} merchantCountry
 */
ThreeDSecureIO3dsServer.prototype['merchantCountry'] = undefined;

/**
 * Merchant Id.
 * @member {String} merchantId
 */
ThreeDSecureIO3dsServer.prototype['merchantId'] = undefined;

/**
 * Merchant Name.
 * @member {String} merchantName
 */
ThreeDSecureIO3dsServer.prototype['merchantName'] = undefined;

/**
 * Merchant URL.
 * @member {String} merchantUrl
 */
ThreeDSecureIO3dsServer.prototype['merchantUrl'] = undefined;

/**
 * 01 - Goods/Service Purchase 03 - Check Acceptance 10 - Account Funding 11 - Quasi-Cash Transaction 28 - Prepaid Activation and Load  Identifies the type of transaction being authenticated. 
 * @member {module:model/ThreeDSecureIO3dsServer.TransactionTypeEnum} transactionType
 */
ThreeDSecureIO3dsServer.prototype['transactionType'] = undefined;

/**
 * Value determines if requests can use version 1 of 3DS. In case both v1 and v2 are enabled it will prefer v2. If v2 is not supported for the issuer, it will coalesce to v1. 
 * @member {Boolean} v1
 */
ThreeDSecureIO3dsServer.prototype['v1'] = undefined;

/**
 * Value determines if requests will attempt version 2 of 3DS. In case both v1 and v2 are enabled it will prefer v2. If v2 is not supported for the issuer, it will coalesce to v1. 
 * @member {Boolean} v2
 */
ThreeDSecureIO3dsServer.prototype['v2'] = undefined;


// Implement WorldlineAtosFrankfurt3dsServers interface:
/**
 * @member {module:model/ThreeDSecureServerName} name
 */
WorldlineAtosFrankfurt3dsServers.prototype['name'] = undefined;
// Implement TestProcessor3dsServers interface:
/**
 * @member {module:model/ThreeDSecureServerName} name
 */
TestProcessor3dsServers.prototype['name'] = undefined;
// Implement EMS3dsServers interface:
/**
 * @member {module:model/ThreeDSecureServerName} name
 */
EMS3dsServers.prototype['name'] = undefined;



/**
 * Allowed values for the <code>transactionType</code> property.
 * @enum {String}
 * @readonly
 */
ThreeDSecureIO3dsServer['TransactionTypeEnum'] = {

    /**
     * value: "01"
     * @const
     */
    "01": "01",

    /**
     * value: "03"
     * @const
     */
    "03": "03",

    /**
     * value: "10"
     * @const
     */
    "10": "10",

    /**
     * value: "11"
     * @const
     */
    "11": "11",

    /**
     * value: "28"
     * @const
     */
    "28": "28"
};



export default ThreeDSecureIO3dsServer;

