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
import CommonPlan from './CommonPlan';
import CommonPlanRecurringInterval from './CommonPlanRecurringInterval';
import CommonPlanSetup from './CommonPlanSetup';
import CommonPlanTrial from './CommonPlanTrial';
import PlanPriceFormula from './PlanPriceFormula';

/**
 * The FlexiblePlan model module.
 * @module model/FlexiblePlan
 * @version 2.1
 */
class FlexiblePlan {
    /**
     * Constructs a new <code>FlexiblePlan</code>.
     * @alias module:model/FlexiblePlan
     * @implements module:model/CommonPlan
     * @param currency {String} ISO 4217 alphabetic currency code.
     * @param id {String} The plan ID.
     * @param name {String} The plan name, displayed on invoices and receipts.
     * @param pricing {module:model/PlanPriceFormula} 
     * @param productId {String} The related product ID.
     */
    constructor(currency, id, name, pricing, productId) { 
        CommonPlan.initialize(this, currency, name, pricing, productId);
        FlexiblePlan.initialize(this, currency, id, name, pricing, productId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, currency, id, name, pricing, productId) { 
        obj['id'] = id;
        obj['currency'] = currency;
        obj['name'] = name;
        obj['pricing'] = pricing;
        obj['productId'] = productId;
    }

    /**
     * Constructs a <code>FlexiblePlan</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FlexiblePlan} obj Optional instance to populate.
     * @return {module:model/FlexiblePlan} The populated <code>FlexiblePlan</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FlexiblePlan();
            CommonPlan.constructFromObject(data, obj);

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('currencySign')) {
                obj['currencySign'] = ApiClient.convertToType(data['currencySign'], 'String');
            }
            if (data.hasOwnProperty('customFields')) {
                obj['customFields'] = ApiClient.convertToType(data['customFields'], Object);
            }
            if (data.hasOwnProperty('isTrialOnly')) {
                obj['isTrialOnly'] = ApiClient.convertToType(data['isTrialOnly'], 'Boolean');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('pricing')) {
                obj['pricing'] = PlanPriceFormula.constructFromObject(data['pricing']);
            }
            if (data.hasOwnProperty('productId')) {
                obj['productId'] = ApiClient.convertToType(data['productId'], 'String');
            }
            if (data.hasOwnProperty('productOptions')) {
                obj['productOptions'] = ApiClient.convertToType(data['productOptions'], {'String': 'String'});
            }
            if (data.hasOwnProperty('recurringInterval')) {
                obj['recurringInterval'] = CommonPlanRecurringInterval.constructFromObject(data['recurringInterval']);
            }
            if (data.hasOwnProperty('revision')) {
                obj['revision'] = ApiClient.convertToType(data['revision'], 'Number');
            }
            if (data.hasOwnProperty('setup')) {
                obj['setup'] = CommonPlanSetup.constructFromObject(data['setup']);
            }
            if (data.hasOwnProperty('trial')) {
                obj['trial'] = CommonPlanTrial.constructFromObject(data['trial']);
            }
            if (data.hasOwnProperty('updatedTime')) {
                obj['updatedTime'] = ApiClient.convertToType(data['updatedTime'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FlexiblePlan</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FlexiblePlan</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of FlexiblePlan.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['currency'] && !(typeof data['currency'] === 'string' || data['currency'] instanceof String)) {
            throw new Error("Expected the field `currency` to be a primitive type in the JSON string but got " + data['currency']);
        }
        // ensure the json data is a string
        if (data['currencySign'] && !(typeof data['currencySign'] === 'string' || data['currencySign'] instanceof String)) {
            throw new Error("Expected the field `currencySign` to be a primitive type in the JSON string but got " + data['currencySign']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `pricing`
        if (data['pricing']) { // data not null
          PlanPriceFormula.validateJSON(data['pricing']);
        }
        // ensure the json data is a string
        if (data['productId'] && !(typeof data['productId'] === 'string' || data['productId'] instanceof String)) {
            throw new Error("Expected the field `productId` to be a primitive type in the JSON string but got " + data['productId']);
        }
        // validate the optional field `recurringInterval`
        if (data['recurringInterval']) { // data not null
          CommonPlanRecurringInterval.validateJSON(data['recurringInterval']);
        }
        // validate the optional field `setup`
        if (data['setup']) { // data not null
          CommonPlanSetup.validateJSON(data['setup']);
        }
        // validate the optional field `trial`
        if (data['trial']) { // data not null
          CommonPlanTrial.validateJSON(data['trial']);
        }

        return true;
    }


}

FlexiblePlan.RequiredProperties = ["id", "currency", "name", "pricing", "productId"];

/**
 * The Plan identifier.
 * @member {String} id
 */
FlexiblePlan.prototype['id'] = undefined;

/**
 * Plan created time.
 * @member {Date} createdTime
 */
FlexiblePlan.prototype['createdTime'] = undefined;

/**
 * ISO 4217 alphabetic currency code.
 * @member {String} currency
 */
FlexiblePlan.prototype['currency'] = undefined;

/**
 * Currency sign.
 * @member {String} currencySign
 */
FlexiblePlan.prototype['currencySign'] = undefined;

/**
 * Custom Fields list as a map `{\"custom field name\": \"custom field value\", ...}`. The format must follow the saved format (see Custom Fields section for the formats). 
 * @member {Object} customFields
 */
FlexiblePlan.prototype['customFields'] = undefined;

/**
 * Whether a plan has a trial without recurring instructions.
 * @member {Boolean} isTrialOnly
 */
FlexiblePlan.prototype['isTrialOnly'] = undefined;

/**
 * The plan name, displayed on invoices and receipts.
 * @member {String} name
 */
FlexiblePlan.prototype['name'] = undefined;

/**
 * @member {module:model/PlanPriceFormula} pricing
 */
FlexiblePlan.prototype['pricing'] = undefined;

/**
 * The related product ID.
 * @member {String} productId
 */
FlexiblePlan.prototype['productId'] = undefined;

/**
 * Name-value pairs to specify the product options.
 * @member {Object.<String, String>} productOptions
 */
FlexiblePlan.prototype['productOptions'] = undefined;

/**
 * @member {module:model/CommonPlanRecurringInterval} recurringInterval
 */
FlexiblePlan.prototype['recurringInterval'] = undefined;

/**
 * Increments when the plan is modified.  Compare to materialized subscription items revision. 
 * @member {Number} revision
 */
FlexiblePlan.prototype['revision'] = undefined;

/**
 * @member {module:model/CommonPlanSetup} setup
 */
FlexiblePlan.prototype['setup'] = undefined;

/**
 * @member {module:model/CommonPlanTrial} trial
 */
FlexiblePlan.prototype['trial'] = undefined;

/**
 * Plan updated time.
 * @member {Date} updatedTime
 */
FlexiblePlan.prototype['updatedTime'] = undefined;


// Implement CommonPlan interface:
/**
 * Plan created time.
 * @member {Date} createdTime
 */
CommonPlan.prototype['createdTime'] = undefined;
/**
 * ISO 4217 alphabetic currency code.
 * @member {String} currency
 */
CommonPlan.prototype['currency'] = undefined;
/**
 * Currency sign.
 * @member {String} currencySign
 */
CommonPlan.prototype['currencySign'] = undefined;
/**
 * Custom Fields list as a map `{\"custom field name\": \"custom field value\", ...}`. The format must follow the saved format (see Custom Fields section for the formats). 
 * @member {Object} customFields
 */
CommonPlan.prototype['customFields'] = undefined;
/**
 * The plan ID.
 * @member {String} id
 */
CommonPlan.prototype['id'] = undefined;
/**
 * Whether a plan has a trial without recurring instructions.
 * @member {Boolean} isTrialOnly
 */
CommonPlan.prototype['isTrialOnly'] = undefined;
/**
 * The plan name, displayed on invoices and receipts.
 * @member {String} name
 */
CommonPlan.prototype['name'] = undefined;
/**
 * @member {module:model/PlanPriceFormula} pricing
 */
CommonPlan.prototype['pricing'] = undefined;
/**
 * The related product ID.
 * @member {String} productId
 */
CommonPlan.prototype['productId'] = undefined;
/**
 * Name-value pairs to specify the product options.
 * @member {Object.<String, String>} productOptions
 */
CommonPlan.prototype['productOptions'] = undefined;
/**
 * @member {module:model/CommonPlanRecurringInterval} recurringInterval
 */
CommonPlan.prototype['recurringInterval'] = undefined;
/**
 * Increments when the plan is modified.  Compare to materialized subscription items revision. 
 * @member {Number} revision
 */
CommonPlan.prototype['revision'] = undefined;
/**
 * @member {module:model/CommonPlanSetup} setup
 */
CommonPlan.prototype['setup'] = undefined;
/**
 * @member {module:model/CommonPlanTrial} trial
 */
CommonPlan.prototype['trial'] = undefined;
/**
 * Plan updated time.
 * @member {Date} updatedTime
 */
CommonPlan.prototype['updatedTime'] = undefined;




export default FlexiblePlan;

