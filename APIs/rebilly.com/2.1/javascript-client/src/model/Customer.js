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
import CustomerAverageValue from './CustomerAverageValue';
import CustomerEmbeddedInner from './CustomerEmbeddedInner';
import CustomerLifetimeRevenue from './CustomerLifetimeRevenue';
import CustomerLinksInner from './CustomerLinksInner';
import PaymentInstrument from './PaymentInstrument';
import Tag from './Tag';

/**
 * The Customer model module.
 * @module model/Customer
 * @version 2.1
 */
class Customer {
    /**
     * Constructs a new <code>Customer</code>.
     * @alias module:model/Customer
     */
    constructor() { 
        
        Customer.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Customer</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Customer} obj Optional instance to populate.
     * @return {module:model/Customer} The populated <code>Customer</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Customer();

            if (data.hasOwnProperty('_embedded')) {
                obj['_embedded'] = ApiClient.convertToType(data['_embedded'], [CustomerEmbeddedInner]);
            }
            if (data.hasOwnProperty('_links')) {
                obj['_links'] = ApiClient.convertToType(data['_links'], [CustomerLinksInner]);
            }
            if (data.hasOwnProperty('averageValue')) {
                obj['averageValue'] = CustomerAverageValue.constructFromObject(data['averageValue']);
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('customFields')) {
                obj['customFields'] = ApiClient.convertToType(data['customFields'], Object);
            }
            if (data.hasOwnProperty('defaultPaymentInstrument')) {
                obj['defaultPaymentInstrument'] = PaymentInstrument.constructFromObject(data['defaultPaymentInstrument']);
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('firstName')) {
                obj['firstName'] = ApiClient.convertToType(data['firstName'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('invoiceCount')) {
                obj['invoiceCount'] = ApiClient.convertToType(data['invoiceCount'], 'Number');
            }
            if (data.hasOwnProperty('lastName')) {
                obj['lastName'] = ApiClient.convertToType(data['lastName'], 'String');
            }
            if (data.hasOwnProperty('lastPaymentTime')) {
                obj['lastPaymentTime'] = ApiClient.convertToType(data['lastPaymentTime'], 'Date');
            }
            if (data.hasOwnProperty('lifetimeRevenue')) {
                obj['lifetimeRevenue'] = CustomerLifetimeRevenue.constructFromObject(data['lifetimeRevenue']);
            }
            if (data.hasOwnProperty('paymentCount')) {
                obj['paymentCount'] = ApiClient.convertToType(data['paymentCount'], 'Number');
            }
            if (data.hasOwnProperty('paymentToken')) {
                obj['paymentToken'] = ApiClient.convertToType(data['paymentToken'], 'String');
            }
            if (data.hasOwnProperty('primaryAddress')) {
                obj['primaryAddress'] = ContactObject.constructFromObject(data['primaryAddress']);
            }
            if (data.hasOwnProperty('revision')) {
                obj['revision'] = ApiClient.convertToType(data['revision'], 'Number');
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], [Tag]);
            }
            if (data.hasOwnProperty('updatedTime')) {
                obj['updatedTime'] = ApiClient.convertToType(data['updatedTime'], 'Date');
            }
            if (data.hasOwnProperty('websiteId')) {
                obj['websiteId'] = ApiClient.convertToType(data['websiteId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Customer</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Customer</code>.
     */
    static validateJSON(data) {
        if (data['_embedded']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_embedded'])) {
                throw new Error("Expected the field `_embedded` to be an array in the JSON data but got " + data['_embedded']);
            }
            // validate the optional field `_embedded` (array)
            for (const item of data['_embedded']) {
                CustomerEmbeddedInner.validateJSON(item);
            };
        }
        if (data['_links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_links'])) {
                throw new Error("Expected the field `_links` to be an array in the JSON data but got " + data['_links']);
            }
            // validate the optional field `_links` (array)
            for (const item of data['_links']) {
                CustomerLinksInner.validateJSON(item);
            };
        }
        // validate the optional field `averageValue`
        if (data['averageValue']) { // data not null
          CustomerAverageValue.validateJSON(data['averageValue']);
        }
        // validate the optional field `defaultPaymentInstrument`
        if (data['defaultPaymentInstrument']) { // data not null
          PaymentInstrument.validateJSON(data['defaultPaymentInstrument']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['firstName'] && !(typeof data['firstName'] === 'string' || data['firstName'] instanceof String)) {
            throw new Error("Expected the field `firstName` to be a primitive type in the JSON string but got " + data['firstName']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['lastName'] && !(typeof data['lastName'] === 'string' || data['lastName'] instanceof String)) {
            throw new Error("Expected the field `lastName` to be a primitive type in the JSON string but got " + data['lastName']);
        }
        // validate the optional field `lifetimeRevenue`
        if (data['lifetimeRevenue']) { // data not null
          CustomerLifetimeRevenue.validateJSON(data['lifetimeRevenue']);
        }
        // ensure the json data is a string
        if (data['paymentToken'] && !(typeof data['paymentToken'] === 'string' || data['paymentToken'] instanceof String)) {
            throw new Error("Expected the field `paymentToken` to be a primitive type in the JSON string but got " + data['paymentToken']);
        }
        // validate the optional field `primaryAddress`
        if (data['primaryAddress']) { // data not null
          ContactObject.validateJSON(data['primaryAddress']);
        }
        if (data['tags']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['tags'])) {
                throw new Error("Expected the field `tags` to be an array in the JSON data but got " + data['tags']);
            }
            // validate the optional field `tags` (array)
            for (const item of data['tags']) {
                Tag.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['websiteId'] && !(typeof data['websiteId'] === 'string' || data['websiteId'] instanceof String)) {
            throw new Error("Expected the field `websiteId` to be a primitive type in the JSON string but got " + data['websiteId']);
        }

        return true;
    }


}



/**
 * Any embedded objects available that are requested by the `expand` querystring parameter.
 * @member {Array.<module:model/CustomerEmbeddedInner>} _embedded
 */
Customer.prototype['_embedded'] = undefined;

/**
 * The links related to resource.
 * @member {Array.<module:model/CustomerLinksInner>} _links
 */
Customer.prototype['_links'] = undefined;

/**
 * @member {module:model/CustomerAverageValue} averageValue
 */
Customer.prototype['averageValue'] = undefined;

/**
 * The customer created time.
 * @member {Date} createdTime
 */
Customer.prototype['createdTime'] = undefined;

/**
 * Custom Fields list as a map `{\"custom field name\": \"custom field value\", ...}`. The format must follow the saved format (see Custom Fields section for the formats). 
 * @member {Object} customFields
 */
Customer.prototype['customFields'] = undefined;

/**
 * @member {module:model/PaymentInstrument} defaultPaymentInstrument
 */
Customer.prototype['defaultPaymentInstrument'] = undefined;

/**
 * The customer's email.
 * @member {String} email
 */
Customer.prototype['email'] = undefined;

/**
 * The customer's first name.
 * @member {String} firstName
 */
Customer.prototype['firstName'] = undefined;

/**
 * The customer identifier string.
 * @member {String} id
 */
Customer.prototype['id'] = undefined;

/**
 * An auto-incrementing number based on the sequence of invoices. If set to 0, then this record is a Lead, otherwise is a Customer.
 * @member {Number} invoiceCount
 */
Customer.prototype['invoiceCount'] = undefined;

/**
 * The customer's last name.
 * @member {String} lastName
 */
Customer.prototype['lastName'] = undefined;

/**
 * The most recent time of an approved payment for the customer.
 * @member {Date} lastPaymentTime
 */
Customer.prototype['lastPaymentTime'] = undefined;

/**
 * @member {module:model/CustomerLifetimeRevenue} lifetimeRevenue
 */
Customer.prototype['lifetimeRevenue'] = undefined;

/**
 * The number of approved payments for the customer.
 * @member {Number} paymentCount
 */
Customer.prototype['paymentCount'] = undefined;

/**
 * A write-only payment token; if supplied, it will be converted into a payment instrument and be set as the `defaultPaymentInstrument`. The value of this property will override the `defaultPaymentInstrument` in the case that both are supplied. The token may only be used once before it is expired. 
 * @member {String} paymentToken
 */
Customer.prototype['paymentToken'] = undefined;

/**
 * @member {module:model/ContactObject} primaryAddress
 */
Customer.prototype['primaryAddress'] = undefined;

/**
 * The number of times the customer data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation. 
 * @member {Number} revision
 */
Customer.prototype['revision'] = undefined;

/**
 * A list of customer's tags.
 * @member {Array.<module:model/Tag>} tags
 */
Customer.prototype['tags'] = undefined;

/**
 * The customer updated time.
 * @member {Date} updatedTime
 */
Customer.prototype['updatedTime'] = undefined;

/**
 * The website's ID.
 * @member {String} websiteId
 */
Customer.prototype['websiteId'] = undefined;






export default Customer;

