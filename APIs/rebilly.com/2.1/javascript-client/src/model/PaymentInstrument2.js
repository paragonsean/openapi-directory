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
import AlternativePaymentInstrument2 from './AlternativePaymentInstrument2';
import AlternativePaymentInstrument2EmbeddedInner from './AlternativePaymentInstrument2EmbeddedInner';
import AlternativePaymentInstrument2LinksInner from './AlternativePaymentInstrument2LinksInner';
import AlternativePaymentMethods from './AlternativePaymentMethods';
import BankAccount from './BankAccount';
import ContactObject from './ContactObject';
import KhelocardCard from './KhelocardCard';
import PayPalAccount from './PayPalAccount';
import PaymentCard from './PaymentCard';
import PaymentCardBrand from './PaymentCardBrand';
import RiskMetadata from './RiskMetadata';

/**
 * The PaymentInstrument2 model module.
 * @module model/PaymentInstrument2
 * @version 2.1
 */
class PaymentInstrument2 {
    /**
     * Constructs a new <code>PaymentInstrument2</code>.
     * @alias module:model/PaymentInstrument2
     * @param {(module:model/AlternativePaymentInstrument2|module:model/BankAccount|module:model/KhelocardCard|module:model/PayPalAccount|module:model/PaymentCard)} instance The actual instance to initialize PaymentInstrument2.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "PaymentCard") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                PaymentCard.validateJSON(instance); // throw an exception if no match
                // create PaymentCard from JS object
                this.actualInstance = PaymentCard.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into PaymentCard
            errorMessages.push("Failed to construct PaymentCard: " + err)
        }

        try {
            if (typeof instance === "BankAccount") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                BankAccount.validateJSON(instance); // throw an exception if no match
                // create BankAccount from JS object
                this.actualInstance = BankAccount.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into BankAccount
            errorMessages.push("Failed to construct BankAccount: " + err)
        }

        try {
            if (typeof instance === "PayPalAccount") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                PayPalAccount.validateJSON(instance); // throw an exception if no match
                // create PayPalAccount from JS object
                this.actualInstance = PayPalAccount.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into PayPalAccount
            errorMessages.push("Failed to construct PayPalAccount: " + err)
        }

        try {
            if (typeof instance === "KhelocardCard") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                KhelocardCard.validateJSON(instance); // throw an exception if no match
                // create KhelocardCard from JS object
                this.actualInstance = KhelocardCard.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into KhelocardCard
            errorMessages.push("Failed to construct KhelocardCard: " + err)
        }

        try {
            if (typeof instance === "AlternativePaymentInstrument2") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                AlternativePaymentInstrument2.validateJSON(instance); // throw an exception if no match
                // create AlternativePaymentInstrument2 from JS object
                this.actualInstance = AlternativePaymentInstrument2.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into AlternativePaymentInstrument2
            errorMessages.push("Failed to construct AlternativePaymentInstrument2: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `PaymentInstrument2` with oneOf schemas AlternativePaymentInstrument2, BankAccount, KhelocardCard, PayPalAccount, PaymentCard. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `PaymentInstrument2` with oneOf schemas AlternativePaymentInstrument2, BankAccount, KhelocardCard, PayPalAccount, PaymentCard. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>PaymentInstrument2</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PaymentInstrument2} obj Optional instance to populate.
     * @return {module:model/PaymentInstrument2} The populated <code>PaymentInstrument2</code> instance.
     */
    static constructFromObject(data, obj) {
        return new PaymentInstrument2(data);
    }

    /**
     * Gets the actual instance, which can be <code>AlternativePaymentInstrument2</code>, <code>BankAccount</code>, <code>KhelocardCard</code>, <code>PayPalAccount</code>, <code>PaymentCard</code>.
     * @return {(module:model/AlternativePaymentInstrument2|module:model/BankAccount|module:model/KhelocardCard|module:model/PayPalAccount|module:model/PaymentCard)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>AlternativePaymentInstrument2</code>, <code>BankAccount</code>, <code>KhelocardCard</code>, <code>PayPalAccount</code>, <code>PaymentCard</code>.
     * @param {(module:model/AlternativePaymentInstrument2|module:model/BankAccount|module:model/KhelocardCard|module:model/PayPalAccount|module:model/PaymentCard)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = PaymentInstrument2.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of PaymentInstrument2 from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/PaymentInstrument2} An instance of PaymentInstrument2.
     */
    static fromJSON = function(json_string){
        return PaymentInstrument2.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * Payment instrument bank country.
 * @member {String} bankCountry
 */
PaymentInstrument2.prototype['bankCountry'] = undefined;

/**
 * Bank's name.
 * @member {String} bankName
 */
PaymentInstrument2.prototype['bankName'] = undefined;

/**
 * The billing address.
 * @member {module:model/ContactObject} billingAddress
 */
PaymentInstrument2.prototype['billingAddress'] = undefined;

/**
 * The card's bin (the PAN's first 6 digits).
 * @member {String} bin
 */
PaymentInstrument2.prototype['bin'] = undefined;

/**
 * @member {module:model/PaymentCardBrand} brand
 */
PaymentInstrument2.prototype['brand'] = undefined;

/**
 * The payment instrument created time.
 * @member {Date} createdTime
 */
PaymentInstrument2.prototype['createdTime'] = undefined;

/**
 * Custom Fields list as a map `{\"custom field name\": \"custom field value\", ...}`. The format must follow the saved format (see Custom Fields section for the formats). 
 * @member {Object} customFields
 */
PaymentInstrument2.prototype['customFields'] = undefined;

/**
 * Customer's ID.
 * @member {String} customerId
 */
PaymentInstrument2.prototype['customerId'] = undefined;

/**
 * Card's cvv (card verification value).
 * @member {String} cvv
 */
PaymentInstrument2.prototype['cvv'] = undefined;

/**
 * Khelocard card's expiration month.
 * @member {Number} expMonth
 */
PaymentInstrument2.prototype['expMonth'] = undefined;

/**
 * Khelocard card's expiration year.
 * @member {Number} expYear
 */
PaymentInstrument2.prototype['expYear'] = undefined;

/**
 * A unique value to identify the payment instrument regardless of variable values. It contains alphanumeric values.
 * @member {String} fingerprint
 */
PaymentInstrument2.prototype['fingerprint'] = undefined;

/**
 * The payment instrument ID.
 * @member {String} id
 */
PaymentInstrument2.prototype['id'] = undefined;

/**
 * The number's last 4 digits.
 * @member {String} last4
 */
PaymentInstrument2.prototype['last4'] = undefined;

/**
 * The method of payment instrument.
 * @member {module:model/AlternativePaymentMethods} method
 */
PaymentInstrument2.prototype['method'] = undefined;

/**
 * The card PAN (primary account number).
 * @member {String} pan
 */
PaymentInstrument2.prototype['pan'] = undefined;

/**
 * @member {module:model/RiskMetadata} riskMetadata
 */
PaymentInstrument2.prototype['riskMetadata'] = undefined;

/**
 * The payment instrument status.
 * @member {module:model/PaymentInstrument2.StatusEnum} status
 */
PaymentInstrument2.prototype['status'] = undefined;

/**
 * The payment instrument updated time.
 * @member {Date} updatedTime
 */
PaymentInstrument2.prototype['updatedTime'] = undefined;

/**
 * Any embedded objects available that are requested by the `expand` querystring parameter.
 * @member {Array.<module:model/AlternativePaymentInstrument2EmbeddedInner>} _embedded
 */
PaymentInstrument2.prototype['_embedded'] = undefined;

/**
 * Links related to the resource.
 * @member {Array.<module:model/AlternativePaymentInstrument2LinksInner>} _links
 */
PaymentInstrument2.prototype['_links'] = undefined;

/**
 * Number of expiration reminder events triggered.
 * @member {Number} expirationReminderNumber
 */
PaymentInstrument2.prototype['expirationReminderNumber'] = undefined;

/**
 * Time expiration reminder event will be triggered.
 * @member {Date} expirationReminderTime
 */
PaymentInstrument2.prototype['expirationReminderTime'] = undefined;

/**
 * Default gateway account ID used for transactions.
 * @member {String} stickyGatewayAccountId
 */
PaymentInstrument2.prototype['stickyGatewayAccountId'] = undefined;

/**
 * Bank's account number type. A valid value is basic bank account number (BBAN) or international bank account number (IBAN).
 * @member {module:model/PaymentInstrument2.AccountNumberTypeEnum} accountNumberType
 * @default 'BBAN'
 */
PaymentInstrument2.prototype['accountNumberType'] = 'BBAN';

/**
 * Bank's account type.
 * @member {module:model/PaymentInstrument2.AccountTypeEnum} accountType
 */
PaymentInstrument2.prototype['accountType'] = undefined;

/**
 * Bank Identifier Code.
 * @member {String} bic
 */
PaymentInstrument2.prototype['bic'] = undefined;

/**
 * Bank's routing number.
 * @member {String} routingNumber
 */
PaymentInstrument2.prototype['routingNumber'] = undefined;

/**
 * PayPal username.
 * @member {String} username
 */
PaymentInstrument2.prototype['username'] = undefined;

/**
 * Khelocard card's masked number.
 * @member {String} number
 */
PaymentInstrument2.prototype['number'] = undefined;


PaymentInstrument2.OneOf = ["AlternativePaymentInstrument2", "BankAccount", "KhelocardCard", "PayPalAccount", "PaymentCard"];

export default PaymentInstrument2;

