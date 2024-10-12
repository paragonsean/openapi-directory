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
import PaymentInstrument3 from './PaymentInstrument3';
import PaymentMethod from './PaymentMethod';
import PaymentMethods from './PaymentMethods';
import PaymentToken from './PaymentToken';

/**
 * The PaymentInstruction model module.
 * @module model/PaymentInstruction
 * @version 2.1
 */
class PaymentInstruction {
    /**
     * Constructs a new <code>PaymentInstruction</code>.
     * @alias module:model/PaymentInstruction
     * @param {(module:model/PaymentInstrument3|module:model/PaymentMethods|module:model/PaymentToken)} instance The actual instance to initialize PaymentInstruction.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "PaymentToken") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                PaymentToken.validateJSON(instance); // throw an exception if no match
                // create PaymentToken from JS object
                this.actualInstance = PaymentToken.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into PaymentToken
            errorMessages.push("Failed to construct PaymentToken: " + err)
        }

        try {
            if (typeof instance === "PaymentInstrument3") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                PaymentInstrument3.validateJSON(instance); // throw an exception if no match
                // create PaymentInstrument3 from JS object
                this.actualInstance = PaymentInstrument3.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into PaymentInstrument3
            errorMessages.push("Failed to construct PaymentInstrument3: " + err)
        }

        try {
            if (typeof instance === "PaymentMethods") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                PaymentMethods.validateJSON(instance); // throw an exception if no match
                // create PaymentMethods from JS object
                this.actualInstance = PaymentMethods.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into PaymentMethods
            errorMessages.push("Failed to construct PaymentMethods: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `PaymentInstruction` with oneOf schemas PaymentInstrument3, PaymentMethods, PaymentToken. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `PaymentInstruction` with oneOf schemas PaymentInstrument3, PaymentMethods, PaymentToken. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>PaymentInstruction</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PaymentInstruction} obj Optional instance to populate.
     * @return {module:model/PaymentInstruction} The populated <code>PaymentInstruction</code> instance.
     */
    static constructFromObject(data, obj) {
        return new PaymentInstruction(data);
    }

    /**
     * Gets the actual instance, which can be <code>PaymentInstrument3</code>, <code>PaymentMethods</code>, <code>PaymentToken</code>.
     * @return {(module:model/PaymentInstrument3|module:model/PaymentMethods|module:model/PaymentToken)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>PaymentInstrument3</code>, <code>PaymentMethods</code>, <code>PaymentToken</code>.
     * @param {(module:model/PaymentInstrument3|module:model/PaymentMethods|module:model/PaymentToken)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = PaymentInstruction.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of PaymentInstruction from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/PaymentInstruction} An instance of PaymentInstruction.
     */
    static fromJSON = function(json_string){
        return PaymentInstruction.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * Payment Token ID.
 * @member {String} token
 */
PaymentInstruction.prototype['token'] = undefined;

/**
 * The Payment Instrument identifier string.
 * @member {String} paymentInstrumentId
 */
PaymentInstruction.prototype['paymentInstrumentId'] = undefined;

/**
 * The list of available payment methods. Only payment methods with at least one active gateway account are allowed.  If not specified all available payment methods will be displayed.  Customer can choose any of those as well as the payment instrument for them. Additional steps will occur via a redirect to `approvalUrl`. 
 * @member {Array.<module:model/PaymentMethod>} methods
 */
PaymentInstruction.prototype['methods'] = undefined;


PaymentInstruction.OneOf = ["PaymentInstrument3", "PaymentMethods", "PaymentToken"];

export default PaymentInstruction;

