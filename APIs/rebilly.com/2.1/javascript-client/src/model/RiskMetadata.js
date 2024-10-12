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
import BrowserData from './BrowserData';

/**
 * The RiskMetadata model module.
 * @module model/RiskMetadata
 * @version 2.1
 */
class RiskMetadata {
    /**
     * Constructs a new <code>RiskMetadata</code>.
     * Risk metadata used for 3DS and risk scoring.
     * @alias module:model/RiskMetadata
     */
    constructor() { 
        
        RiskMetadata.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RiskMetadata</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RiskMetadata} obj Optional instance to populate.
     * @return {module:model/RiskMetadata} The populated <code>RiskMetadata</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RiskMetadata();

            if (data.hasOwnProperty('accuracyRadius')) {
                obj['accuracyRadius'] = ApiClient.convertToType(data['accuracyRadius'], 'Number');
            }
            if (data.hasOwnProperty('browserData')) {
                obj['browserData'] = BrowserData.constructFromObject(data['browserData']);
            }
            if (data.hasOwnProperty('city')) {
                obj['city'] = ApiClient.convertToType(data['city'], 'String');
            }
            if (data.hasOwnProperty('country')) {
                obj['country'] = ApiClient.convertToType(data['country'], 'String');
            }
            if (data.hasOwnProperty('deviceVelocity')) {
                obj['deviceVelocity'] = ApiClient.convertToType(data['deviceVelocity'], 'Number');
            }
            if (data.hasOwnProperty('distance')) {
                obj['distance'] = ApiClient.convertToType(data['distance'], 'Number');
            }
            if (data.hasOwnProperty('fingerprint')) {
                obj['fingerprint'] = ApiClient.convertToType(data['fingerprint'], 'String');
            }
            if (data.hasOwnProperty('hasMismatchedBankCountry')) {
                obj['hasMismatchedBankCountry'] = ApiClient.convertToType(data['hasMismatchedBankCountry'], 'Boolean');
            }
            if (data.hasOwnProperty('hasMismatchedBillingAddressCountry')) {
                obj['hasMismatchedBillingAddressCountry'] = ApiClient.convertToType(data['hasMismatchedBillingAddressCountry'], 'Boolean');
            }
            if (data.hasOwnProperty('hasMismatchedHolderName')) {
                obj['hasMismatchedHolderName'] = ApiClient.convertToType(data['hasMismatchedHolderName'], 'Boolean');
            }
            if (data.hasOwnProperty('hasMismatchedTimeZone')) {
                obj['hasMismatchedTimeZone'] = ApiClient.convertToType(data['hasMismatchedTimeZone'], 'Boolean');
            }
            if (data.hasOwnProperty('httpHeaders')) {
                obj['httpHeaders'] = ApiClient.convertToType(data['httpHeaders'], {'String': 'String'});
            }
            if (data.hasOwnProperty('ipAddress')) {
                obj['ipAddress'] = ApiClient.convertToType(data['ipAddress'], 'String');
            }
            if (data.hasOwnProperty('isHosting')) {
                obj['isHosting'] = ApiClient.convertToType(data['isHosting'], 'Boolean');
            }
            if (data.hasOwnProperty('isProxy')) {
                obj['isProxy'] = ApiClient.convertToType(data['isProxy'], 'Boolean');
            }
            if (data.hasOwnProperty('isTor')) {
                obj['isTor'] = ApiClient.convertToType(data['isTor'], 'Boolean');
            }
            if (data.hasOwnProperty('isVpn')) {
                obj['isVpn'] = ApiClient.convertToType(data['isVpn'], 'Boolean');
            }
            if (data.hasOwnProperty('isp')) {
                obj['isp'] = ApiClient.convertToType(data['isp'], 'String');
            }
            if (data.hasOwnProperty('latitude')) {
                obj['latitude'] = ApiClient.convertToType(data['latitude'], 'Number');
            }
            if (data.hasOwnProperty('longitude')) {
                obj['longitude'] = ApiClient.convertToType(data['longitude'], 'Number');
            }
            if (data.hasOwnProperty('paymentInstrumentVelocity')) {
                obj['paymentInstrumentVelocity'] = ApiClient.convertToType(data['paymentInstrumentVelocity'], 'Number');
            }
            if (data.hasOwnProperty('postalCode')) {
                obj['postalCode'] = ApiClient.convertToType(data['postalCode'], 'String');
            }
            if (data.hasOwnProperty('region')) {
                obj['region'] = ApiClient.convertToType(data['region'], 'String');
            }
            if (data.hasOwnProperty('score')) {
                obj['score'] = ApiClient.convertToType(data['score'], 'Number');
            }
            if (data.hasOwnProperty('timeZone')) {
                obj['timeZone'] = ApiClient.convertToType(data['timeZone'], 'String');
            }
            if (data.hasOwnProperty('vpnServiceName')) {
                obj['vpnServiceName'] = ApiClient.convertToType(data['vpnServiceName'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RiskMetadata</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RiskMetadata</code>.
     */
    static validateJSON(data) {
        // validate the optional field `browserData`
        if (data['browserData']) { // data not null
          BrowserData.validateJSON(data['browserData']);
        }
        // ensure the json data is a string
        if (data['city'] && !(typeof data['city'] === 'string' || data['city'] instanceof String)) {
            throw new Error("Expected the field `city` to be a primitive type in the JSON string but got " + data['city']);
        }
        // ensure the json data is a string
        if (data['country'] && !(typeof data['country'] === 'string' || data['country'] instanceof String)) {
            throw new Error("Expected the field `country` to be a primitive type in the JSON string but got " + data['country']);
        }
        // ensure the json data is a string
        if (data['fingerprint'] && !(typeof data['fingerprint'] === 'string' || data['fingerprint'] instanceof String)) {
            throw new Error("Expected the field `fingerprint` to be a primitive type in the JSON string but got " + data['fingerprint']);
        }
        // ensure the json data is a string
        if (data['ipAddress'] && !(typeof data['ipAddress'] === 'string' || data['ipAddress'] instanceof String)) {
            throw new Error("Expected the field `ipAddress` to be a primitive type in the JSON string but got " + data['ipAddress']);
        }
        // ensure the json data is a string
        if (data['isp'] && !(typeof data['isp'] === 'string' || data['isp'] instanceof String)) {
            throw new Error("Expected the field `isp` to be a primitive type in the JSON string but got " + data['isp']);
        }
        // ensure the json data is a string
        if (data['postalCode'] && !(typeof data['postalCode'] === 'string' || data['postalCode'] instanceof String)) {
            throw new Error("Expected the field `postalCode` to be a primitive type in the JSON string but got " + data['postalCode']);
        }
        // ensure the json data is a string
        if (data['region'] && !(typeof data['region'] === 'string' || data['region'] instanceof String)) {
            throw new Error("Expected the field `region` to be a primitive type in the JSON string but got " + data['region']);
        }
        // ensure the json data is a string
        if (data['timeZone'] && !(typeof data['timeZone'] === 'string' || data['timeZone'] instanceof String)) {
            throw new Error("Expected the field `timeZone` to be a primitive type in the JSON string but got " + data['timeZone']);
        }
        // ensure the json data is a string
        if (data['vpnServiceName'] && !(typeof data['vpnServiceName'] === 'string' || data['vpnServiceName'] instanceof String)) {
            throw new Error("Expected the field `vpnServiceName` to be a primitive type in the JSON string but got " + data['vpnServiceName']);
        }

        return true;
    }


}



/**
 * Accuracy radius for specified ipAddress (kilometers).
 * @member {Number} accuracyRadius
 */
RiskMetadata.prototype['accuracyRadius'] = undefined;

/**
 * @member {module:model/BrowserData} browserData
 */
RiskMetadata.prototype['browserData'] = undefined;

/**
 * City for specified ipAddress.
 * @member {String} city
 */
RiskMetadata.prototype['city'] = undefined;

/**
 * Country ISO Alpha-2 code for specified ipAddress.
 * @member {String} country
 */
RiskMetadata.prototype['country'] = undefined;

/**
 * Number of transactions for this device (based on fingerprint) in the last 24 hours.
 * @member {Number} deviceVelocity
 */
RiskMetadata.prototype['deviceVelocity'] = undefined;

/**
 * Distance between IP Address and Billing Address geolocation (kilometers).
 * @member {Number} distance
 */
RiskMetadata.prototype['distance'] = undefined;

/**
 * The fingerprint.
 * @member {String} fingerprint
 */
RiskMetadata.prototype['fingerprint'] = undefined;

/**
 * True if the bank country and geo-IP address are not the same.
 * @member {Boolean} hasMismatchedBankCountry
 */
RiskMetadata.prototype['hasMismatchedBankCountry'] = undefined;

/**
 * True if the billing address country and geo-IP address are not the same.
 * @member {Boolean} hasMismatchedBillingAddressCountry
 */
RiskMetadata.prototype['hasMismatchedBillingAddressCountry'] = undefined;

/**
 * True if the customer's name from billing address and from customer's primary address are not the same.
 * @member {Boolean} hasMismatchedHolderName
 */
RiskMetadata.prototype['hasMismatchedHolderName'] = undefined;

/**
 * True if the browser time zone and IP address associated time zone are not the same.
 * @member {Boolean} hasMismatchedTimeZone
 */
RiskMetadata.prototype['hasMismatchedTimeZone'] = undefined;

/**
 * The HTTP headers.
 * @member {Object.<String, String>} httpHeaders
 */
RiskMetadata.prototype['httpHeaders'] = undefined;

/**
 * The customer's IP.
 * @member {String} ipAddress
 */
RiskMetadata.prototype['ipAddress'] = undefined;

/**
 * True if customer's ip address is related to hosting.
 * @member {Boolean} isHosting
 */
RiskMetadata.prototype['isHosting'] = undefined;

/**
 * True if customer's ip address is related to proxy.
 * @member {Boolean} isProxy
 */
RiskMetadata.prototype['isProxy'] = undefined;

/**
 * True if customer's ip address is related to TOR.
 * @member {Boolean} isTor
 */
RiskMetadata.prototype['isTor'] = undefined;

/**
 * True if customer's ip address is related to VPN.
 * @member {Boolean} isVpn
 */
RiskMetadata.prototype['isVpn'] = undefined;

/**
 * Internet Service Provider name, if available.
 * @member {String} isp
 */
RiskMetadata.prototype['isp'] = undefined;

/**
 * Latitude for specified ipAddress.
 * @member {Number} latitude
 */
RiskMetadata.prototype['latitude'] = undefined;

/**
 * Longitude for specified ipAddress.
 * @member {Number} longitude
 */
RiskMetadata.prototype['longitude'] = undefined;

/**
 * Number of transactions for this payment instrument (based on fingerprint) in the last 24 hours.
 * @member {Number} paymentInstrumentVelocity
 */
RiskMetadata.prototype['paymentInstrumentVelocity'] = undefined;

/**
 * Postal code for specified ipAddress.
 * @member {String} postalCode
 */
RiskMetadata.prototype['postalCode'] = undefined;

/**
 * Region for specified ipAddress.
 * @member {String} region
 */
RiskMetadata.prototype['region'] = undefined;

/**
 * Risk score computed per all the factors.
 * @member {Number} score
 */
RiskMetadata.prototype['score'] = undefined;

/**
 * Time zone for specified ipAddress.
 * @member {String} timeZone
 */
RiskMetadata.prototype['timeZone'] = undefined;

/**
 * VPN service name, if available.
 * @member {String} vpnServiceName
 */
RiskMetadata.prototype['vpnServiceName'] = undefined;






export default RiskMetadata;

