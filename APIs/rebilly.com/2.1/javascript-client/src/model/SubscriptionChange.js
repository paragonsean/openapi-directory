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
import SubscriptionChangeItemsInner from './SubscriptionChangeItemsInner';

/**
 * The SubscriptionChange model module.
 * @module model/SubscriptionChange
 * @version 2.1
 */
class SubscriptionChange {
    /**
     * Constructs a new <code>SubscriptionChange</code>.
     * @alias module:model/SubscriptionChange
     * @param items {Array.<module:model/SubscriptionChangeItemsInner>} 
     * @param prorated {Boolean} Whether or not to give a pro rata credit for the amount of time remaining between the `effectiveTime` and the end of the current period. In addition, if the `renewalTime` is retained (by setting the `renewalPolicy` to `retain`), then a pro rata debit will occur as well, for the amount between the `effectiveTime` and the `renewalTime` as a percentage of the normal period size. 
     * @param renewalPolicy {module:model/SubscriptionChange.RenewalPolicyEnum} The value determines whether the subscription retains its current `renewalTime` or resets it to a newly calculated `renewalTime`.
     */
    constructor(items, prorated, renewalPolicy) { 
        
        SubscriptionChange.initialize(this, items, prorated, renewalPolicy);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, items, prorated, renewalPolicy) { 
        obj['items'] = items;
        obj['keepTrial'] = false;
        obj['preview'] = false;
        obj['prorated'] = prorated;
        obj['renewalPolicy'] = renewalPolicy;
    }

    /**
     * Constructs a <code>SubscriptionChange</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SubscriptionChange} obj Optional instance to populate.
     * @return {module:model/SubscriptionChange} The populated <code>SubscriptionChange</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SubscriptionChange();

            if (data.hasOwnProperty('effectiveTime')) {
                obj['effectiveTime'] = ApiClient.convertToType(data['effectiveTime'], 'Date');
            }
            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [SubscriptionChangeItemsInner]);
            }
            if (data.hasOwnProperty('keepTrial')) {
                obj['keepTrial'] = ApiClient.convertToType(data['keepTrial'], 'Boolean');
            }
            if (data.hasOwnProperty('preview')) {
                obj['preview'] = ApiClient.convertToType(data['preview'], 'Boolean');
            }
            if (data.hasOwnProperty('prorated')) {
                obj['prorated'] = ApiClient.convertToType(data['prorated'], 'Boolean');
            }
            if (data.hasOwnProperty('renewalPolicy')) {
                obj['renewalPolicy'] = ApiClient.convertToType(data['renewalPolicy'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SubscriptionChange</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SubscriptionChange</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SubscriptionChange.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                SubscriptionChangeItemsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['renewalPolicy'] && !(typeof data['renewalPolicy'] === 'string' || data['renewalPolicy'] instanceof String)) {
            throw new Error("Expected the field `renewalPolicy` to be a primitive type in the JSON string but got " + data['renewalPolicy']);
        }

        return true;
    }


}

SubscriptionChange.RequiredProperties = ["items", "prorated", "renewalPolicy"];

/**
 * The date from which the renewal time (for `reset` operations) and proration calculations are made.  If omitted, it will default to the current time.
 * @member {Date} effectiveTime
 */
SubscriptionChange.prototype['effectiveTime'] = undefined;

/**
 * @member {Array.<module:model/SubscriptionChangeItemsInner>} items
 */
SubscriptionChange.prototype['items'] = undefined;

/**
 * If set to true and the subscription order has an active trial, it will use that trial further. Works with 'retain' renewalPolicy only.
 * @member {Boolean} keepTrial
 * @default false
 */
SubscriptionChange.prototype['keepTrial'] = false;

/**
 * If set to true, it will not change the subscription.  It allows for a way to preview the changes that would be made to a subscription.
 * @member {Boolean} preview
 * @default false
 */
SubscriptionChange.prototype['preview'] = false;

/**
 * Whether or not to give a pro rata credit for the amount of time remaining between the `effectiveTime` and the end of the current period. In addition, if the `renewalTime` is retained (by setting the `renewalPolicy` to `retain`), then a pro rata debit will occur as well, for the amount between the `effectiveTime` and the `renewalTime` as a percentage of the normal period size. 
 * @member {Boolean} prorated
 */
SubscriptionChange.prototype['prorated'] = undefined;

/**
 * The value determines whether the subscription retains its current `renewalTime` or resets it to a newly calculated `renewalTime`.
 * @member {module:model/SubscriptionChange.RenewalPolicyEnum} renewalPolicy
 */
SubscriptionChange.prototype['renewalPolicy'] = undefined;





/**
 * Allowed values for the <code>renewalPolicy</code> property.
 * @enum {String}
 * @readonly
 */
SubscriptionChange['RenewalPolicyEnum'] = {

    /**
     * value: "reset"
     * @const
     */
    "reset": "reset",

    /**
     * value: "retain"
     * @const
     */
    "retain": "retain"
};



export default SubscriptionChange;

