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
import CommonPaymentToken from './CommonPaymentToken';
import ContactObject from './ContactObject';
import LeadSource from './LeadSource';
import RiskMetadata from './RiskMetadata';
import SelfLink from './SelfLink';

/**
 * The KhelocardCardToken model module.
 * @module model/KhelocardCardToken
 * @version 2.1
 */
class KhelocardCardToken {
    /**
     * Constructs a new <code>KhelocardCardToken</code>.
     * @alias module:model/KhelocardCardToken
     * @implements module:model/CommonPaymentToken
     * @param method {String} 
     */
    constructor(method) { 
        CommonPaymentToken.initialize(this, method);
        KhelocardCardToken.initialize(this, method);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, method) { 
        obj['billingAddress'] = billingAddress;
        obj['method'] = method;
        obj['paymentInstrument'] = paymentInstrument;
        obj['isUsed'] = false;
    }

    /**
     * Constructs a <code>KhelocardCardToken</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/KhelocardCardToken} obj Optional instance to populate.
     * @return {module:model/KhelocardCardToken} The populated <code>KhelocardCardToken</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new KhelocardCardToken();
            CommonPaymentToken.constructFromObject(data, obj);

            if (data.hasOwnProperty('billingAddress')) {
                obj['billingAddress'] = ApiClient.convertToType(data['billingAddress'], ContactObject);
            }
            if (data.hasOwnProperty('method')) {
                obj['method'] = ApiClient.convertToType(data['method'], 'String');
            }
            if (data.hasOwnProperty('paymentInstrument')) {
                obj['paymentInstrument'] = ApiClient.convertToType(data['paymentInstrument'], Object);
            }
            if (data.hasOwnProperty('_links')) {
                obj['_links'] = ApiClient.convertToType(data['_links'], [SelfLink]);
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('expirationTime')) {
                obj['expirationTime'] = ApiClient.convertToType(data['expirationTime'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('isUsed')) {
                obj['isUsed'] = ApiClient.convertToType(data['isUsed'], 'Boolean');
            }
            if (data.hasOwnProperty('leadSource')) {
                obj['leadSource'] = ApiClient.convertToType(data['leadSource'], LeadSource);
            }
            if (data.hasOwnProperty('riskMetadata')) {
                obj['riskMetadata'] = ApiClient.convertToType(data['riskMetadata'], RiskMetadata);
            }
            if (data.hasOwnProperty('updatedTime')) {
                obj['updatedTime'] = ApiClient.convertToType(data['updatedTime'], 'Date');
            }
            if (data.hasOwnProperty('usageTime')) {
                obj['usageTime'] = ApiClient.convertToType(data['usageTime'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>KhelocardCardToken</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>KhelocardCardToken</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of KhelocardCardToken.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `billingAddress`
        if (data['billingAddress']) { // data not null
          ContactObject.validateJSON(data['billingAddress']);
        }
        // ensure the json data is a string
        if (data['method'] && !(typeof data['method'] === 'string' || data['method'] instanceof String)) {
            throw new Error("Expected the field `method` to be a primitive type in the JSON string but got " + data['method']);
        }
        // validate the optional field `paymentInstrument`
        if (data['paymentInstrument']) { // data not null
          Object.validateJSON(data['paymentInstrument']);
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
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `leadSource`
        if (data['leadSource']) { // data not null
          LeadSource.validateJSON(data['leadSource']);
        }
        // validate the optional field `riskMetadata`
        if (data['riskMetadata']) { // data not null
          RiskMetadata.validateJSON(data['riskMetadata']);
        }

        return true;
    }


}

KhelocardCardToken.RequiredProperties = ["billingAddress", "method", "paymentInstrument"];

/**
 * The billing address object.
 * @member {module:model/ContactObject} billingAddress
 */
KhelocardCardToken.prototype['billingAddress'] = undefined;

/**
 * The token method.
 * @member {module:model/KhelocardCardToken.MethodEnum} method
 */
KhelocardCardToken.prototype['method'] = undefined;

/**
 * The token instrument details.
 * @member {Object} paymentInstrument
 */
KhelocardCardToken.prototype['paymentInstrument'] = undefined;

/**
 * The links related to resource.
 * @member {Array.<module:model/SelfLink>} _links
 */
KhelocardCardToken.prototype['_links'] = undefined;

/**
 * Token created time.
 * @member {Date} createdTime
 */
KhelocardCardToken.prototype['createdTime'] = undefined;

/**
 * Token expiration time.
 * @member {Date} expirationTime
 */
KhelocardCardToken.prototype['expirationTime'] = undefined;

/**
 * The token identifier string.
 * @member {String} id
 */
KhelocardCardToken.prototype['id'] = undefined;

/**
 * Whether the token was already used.
 * @member {Boolean} isUsed
 * @default false
 */
KhelocardCardToken.prototype['isUsed'] = false;

/**
 * @member {module:model/LeadSource} leadSource
 */
KhelocardCardToken.prototype['leadSource'] = undefined;

/**
 * @member {module:model/RiskMetadata} riskMetadata
 */
KhelocardCardToken.prototype['riskMetadata'] = undefined;

/**
 * Token updated time.
 * @member {Date} updatedTime
 */
KhelocardCardToken.prototype['updatedTime'] = undefined;

/**
 * Token usage time.
 * @member {Date} usageTime
 */
KhelocardCardToken.prototype['usageTime'] = undefined;


// Implement CommonPaymentToken interface:
/**
 * The links related to resource.
 * @member {Array.<module:model/SelfLink>} _links
 */
CommonPaymentToken.prototype['_links'] = undefined;
/**
 * Token created time.
 * @member {Date} createdTime
 */
CommonPaymentToken.prototype['createdTime'] = undefined;
/**
 * Token expiration time.
 * @member {Date} expirationTime
 */
CommonPaymentToken.prototype['expirationTime'] = undefined;
/**
 * The token identifier string.
 * @member {String} id
 */
CommonPaymentToken.prototype['id'] = undefined;
/**
 * Whether the token was already used.
 * @member {Boolean} isUsed
 * @default false
 */
CommonPaymentToken.prototype['isUsed'] = false;
/**
 * @member {module:model/LeadSource} leadSource
 */
CommonPaymentToken.prototype['leadSource'] = undefined;
/**
 * @member {String} method
 */
CommonPaymentToken.prototype['method'] = undefined;
/**
 * @member {module:model/RiskMetadata} riskMetadata
 */
CommonPaymentToken.prototype['riskMetadata'] = undefined;
/**
 * Token updated time.
 * @member {Date} updatedTime
 */
CommonPaymentToken.prototype['updatedTime'] = undefined;
/**
 * Token usage time.
 * @member {Date} usageTime
 */
CommonPaymentToken.prototype['usageTime'] = undefined;



/**
 * Allowed values for the <code>method</code> property.
 * @enum {String}
 * @readonly
 */
KhelocardCardToken['MethodEnum'] = {

    /**
     * value: "Khelocard"
     * @const
     */
    "Khelocard": "Khelocard"
};



export default KhelocardCardToken;

