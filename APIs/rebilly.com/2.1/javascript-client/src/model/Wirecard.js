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
import GatewayAccount from './GatewayAccount';
import GatewayAccountLinksInner from './GatewayAccountLinksInner';
import GatewayName from './GatewayName';
import PaymentCardBrand from './PaymentCardBrand';
import PaymentMethod from './PaymentMethod';
import Wirecard3dsServers from './Wirecard3dsServers';
import WirecardAllOfCredentials from './WirecardAllOfCredentials';

/**
 * The Wirecard model module.
 * @module model/Wirecard
 * @version 2.1
 */
class Wirecard {
    /**
     * Constructs a new <code>Wirecard</code>.
     * Wirecard Gateway config.
     * @alias module:model/Wirecard
     * @extends module:model/GatewayAccount
     * @implements module:model/GatewayAccount
     * @param acceptedCurrencies {Array.<String>} Accepted currencies (array of the currency three letter codes).
     * @param gatewayName {module:model/GatewayName} 
     * @param method {module:model/PaymentMethod} 
     * @param credentials {module:model/WirecardAllOfCredentials} 
     */
    constructor(acceptedCurrencies, gatewayName, method, credentials) { 
        GatewayAccount.initialize(this, acceptedCurrencies, gatewayName, method);
        Wirecard.initialize(this, acceptedCurrencies, gatewayName, method, credentials);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, acceptedCurrencies, gatewayName, method, credentials) { 
        obj['credentials'] = credentials;
    }

    /**
     * Constructs a <code>Wirecard</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Wirecard} obj Optional instance to populate.
     * @return {module:model/Wirecard} The populated <code>Wirecard</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Wirecard();
            GatewayAccount.constructFromObject(data, obj);
            GatewayAccount.constructFromObject(data, obj);

            if (data.hasOwnProperty('credentials')) {
                obj['credentials'] = WirecardAllOfCredentials.constructFromObject(data['credentials']);
            }
            if (data.hasOwnProperty('threeDSecureServer')) {
                obj['threeDSecureServer'] = Wirecard3dsServers.constructFromObject(data['threeDSecureServer']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Wirecard</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Wirecard</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Wirecard.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `credentials`
        if (data['credentials']) { // data not null
          WirecardAllOfCredentials.validateJSON(data['credentials']);
        }
        // validate the optional field `threeDSecureServer`
        if (data['threeDSecureServer']) { // data not null
          Wirecard3dsServers.validateJSON(data['threeDSecureServer']);
        }

        return true;
    }


}

Wirecard.RequiredProperties = ["credentials", "acceptedCurrencies", "gatewayName", "method"];

/**
 * @member {module:model/WirecardAllOfCredentials} credentials
 */
Wirecard.prototype['credentials'] = undefined;

/**
 * @member {module:model/Wirecard3dsServers} threeDSecureServer
 */
Wirecard.prototype['threeDSecureServer'] = undefined;


// Implement GatewayAccount interface:
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




export default Wirecard;

