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
import SelfLink from './SelfLink';
import TimelineExtraData from './TimelineExtraData';

/**
 * The OrderTimeline model module.
 * @module model/OrderTimeline
 * @version 2.1
 */
class OrderTimeline {
    /**
     * Constructs a new <code>OrderTimeline</code>.
     * @alias module:model/OrderTimeline
     */
    constructor() { 
        
        OrderTimeline.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OrderTimeline</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderTimeline} obj Optional instance to populate.
     * @return {module:model/OrderTimeline} The populated <code>OrderTimeline</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderTimeline();

            if (data.hasOwnProperty('_links')) {
                obj['_links'] = ApiClient.convertToType(data['_links'], [SelfLink]);
            }
            if (data.hasOwnProperty('extraData')) {
                obj['extraData'] = TimelineExtraData.constructFromObject(data['extraData']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('occurredTime')) {
                obj['occurredTime'] = ApiClient.convertToType(data['occurredTime'], 'Date');
            }
            if (data.hasOwnProperty('triggeredBy')) {
                obj['triggeredBy'] = ApiClient.convertToType(data['triggeredBy'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderTimeline</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderTimeline</code>.
     */
    static validateJSON(data) {
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
        // validate the optional field `extraData`
        if (data['extraData']) { // data not null
          TimelineExtraData.validateJSON(data['extraData']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // ensure the json data is a string
        if (data['triggeredBy'] && !(typeof data['triggeredBy'] === 'string' || data['triggeredBy'] instanceof String)) {
            throw new Error("Expected the field `triggeredBy` to be a primitive type in the JSON string but got " + data['triggeredBy']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * The links related to resource.
 * @member {Array.<module:model/SelfLink>} _links
 */
OrderTimeline.prototype['_links'] = undefined;

/**
 * @member {module:model/TimelineExtraData} extraData
 */
OrderTimeline.prototype['extraData'] = undefined;

/**
 * The Timeline message identifier string.
 * @member {String} id
 */
OrderTimeline.prototype['id'] = undefined;

/**
 * The message that describes the message details.
 * @member {String} message
 */
OrderTimeline.prototype['message'] = undefined;

/**
 * Timeline message time.
 * @member {Date} occurredTime
 */
OrderTimeline.prototype['occurredTime'] = undefined;

/**
 * Shows who or what triggered the Timeline message.
 * @member {module:model/OrderTimeline.TriggeredByEnum} triggeredBy
 */
OrderTimeline.prototype['triggeredBy'] = undefined;

/**
 * Timeline message type.
 * @member {module:model/OrderTimeline.TypeEnum} type
 */
OrderTimeline.prototype['type'] = undefined;





/**
 * Allowed values for the <code>triggeredBy</code> property.
 * @enum {String}
 * @readonly
 */
OrderTimeline['TriggeredByEnum'] = {

    /**
     * value: "rebilly"
     * @const
     */
    "rebilly": "rebilly",

    /**
     * value: "app"
     * @const
     */
    "app": "app",

    /**
     * value: "direct-api"
     * @const
     */
    "direct-api": "direct-api"
};


/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
OrderTimeline['TypeEnum'] = {

    /**
     * value: "timeline-comment-created"
     * @const
     */
    "timeline-comment-created": "timeline-comment-created",

    /**
     * value: "order-renewed"
     * @const
     */
    "order-renewed": "order-renewed",

    /**
     * value: "order-activated"
     * @const
     */
    "order-activated": "order-activated",

    /**
     * value: "order-completed"
     * @const
     */
    "order-completed": "order-completed",

    /**
     * value: "order-reactivated"
     * @const
     */
    "order-reactivated": "order-reactivated",

    /**
     * value: "order-canceled"
     * @const
     */
    "order-canceled": "order-canceled",

    /**
     * value: "order-upgraded"
     * @const
     */
    "order-upgraded": "order-upgraded",

    /**
     * value: "order-downgraded"
     * @const
     */
    "order-downgraded": "order-downgraded",

    /**
     * value: "order-billing-address-changed"
     * @const
     */
    "order-billing-address-changed": "order-billing-address-changed",

    /**
     * value: "order-delivery-address-changed"
     * @const
     */
    "order-delivery-address-changed": "order-delivery-address-changed",

    /**
     * value: "order-renewal-time-changed"
     * @const
     */
    "order-renewal-time-changed": "order-renewal-time-changed",

    /**
     * value: "order-churned"
     * @const
     */
    "order-churned": "order-churned",

    /**
     * value: "order-custom-fields-changed"
     * @const
     */
    "order-custom-fields-changed": "order-custom-fields-changed",

    /**
     * value: "order-items-changed"
     * @const
     */
    "order-items-changed": "order-items-changed",

    /**
     * value: "order-billing-anchor-changed"
     * @const
     */
    "order-billing-anchor-changed": "order-billing-anchor-changed",

    /**
     * value: "order-recurring-interval-changed"
     * @const
     */
    "order-recurring-interval-changed": "order-recurring-interval-changed",

    /**
     * value: "order-risk-metadata-changed"
     * @const
     */
    "order-risk-metadata-changed": "order-risk-metadata-changed",

    /**
     * value: "order-paid-early"
     * @const
     */
    "order-paid-early": "order-paid-early",

    /**
     * value: "order-quantity-changed"
     * @const
     */
    "order-quantity-changed": "order-quantity-changed",

    /**
     * value: "email-message-sent"
     * @const
     */
    "email-message-sent": "email-message-sent",

    /**
     * value: "coupon-applied"
     * @const
     */
    "coupon-applied": "coupon-applied",

    /**
     * value: "invoice-created"
     * @const
     */
    "invoice-created": "invoice-created",

    /**
     * value: "invoice-issued"
     * @const
     */
    "invoice-issued": "invoice-issued",

    /**
     * value: "invoice-abandoned"
     * @const
     */
    "invoice-abandoned": "invoice-abandoned",

    /**
     * value: "invoice-voided"
     * @const
     */
    "invoice-voided": "invoice-voided",

    /**
     * value: "invoice-past-due"
     * @const
     */
    "invoice-past-due": "invoice-past-due",

    /**
     * value: "invoice-paid"
     * @const
     */
    "invoice-paid": "invoice-paid",

    /**
     * value: "invoice-partially-paid"
     * @const
     */
    "invoice-partially-paid": "invoice-partially-paid",

    /**
     * value: "invoice-disputed"
     * @const
     */
    "invoice-disputed": "invoice-disputed",

    /**
     * value: "invoice-refunded"
     * @const
     */
    "invoice-refunded": "invoice-refunded",

    /**
     * value: "invoice-partially-refunded"
     * @const
     */
    "invoice-partially-refunded": "invoice-partially-refunded",

    /**
     * value: "invoice-renewal-payment-declined"
     * @const
     */
    "invoice-renewal-payment-declined": "invoice-renewal-payment-declined"
};



export default OrderTimeline;

