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
import CommonSubscription from './CommonSubscription';
import CommonSubscriptionItemsInner from './CommonSubscriptionItemsInner';
import ContactObject from './ContactObject';

/**
 * The CommonOneTimeOrder model module.
 * @module model/CommonOneTimeOrder
 * @version 2.1
 */
class CommonOneTimeOrder {
    /**
     * Constructs a new <code>CommonOneTimeOrder</code>.
     * @alias module:model/CommonOneTimeOrder
     * @implements module:model/CommonSubscription
     */
    constructor() { 
        CommonSubscription.initialize(this);
        CommonOneTimeOrder.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['orderType'] = 'subscription-order';
    }

    /**
     * Constructs a <code>CommonOneTimeOrder</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CommonOneTimeOrder} obj Optional instance to populate.
     * @return {module:model/CommonOneTimeOrder} The populated <code>CommonOneTimeOrder</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CommonOneTimeOrder();
            CommonSubscription.constructFromObject(data, obj);

            if (data.hasOwnProperty('activationTime')) {
                obj['activationTime'] = ApiClient.convertToType(data['activationTime'], 'Date');
            }
            if (data.hasOwnProperty('billingAddress')) {
                obj['billingAddress'] = ApiClient.convertToType(data['billingAddress'], ContactObject);
            }
            if (data.hasOwnProperty('billingStatus')) {
                obj['billingStatus'] = ApiClient.convertToType(data['billingStatus'], 'String');
            }
            if (data.hasOwnProperty('couponIds')) {
                obj['couponIds'] = ApiClient.convertToType(data['couponIds'], ['String']);
            }
            if (data.hasOwnProperty('deliveryAddress')) {
                obj['deliveryAddress'] = ApiClient.convertToType(data['deliveryAddress'], ContactObject);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('initialInvoiceId')) {
                obj['initialInvoiceId'] = ApiClient.convertToType(data['initialInvoiceId'], 'String');
            }
            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [CommonSubscriptionItemsInner]);
            }
            if (data.hasOwnProperty('orderType')) {
                obj['orderType'] = ApiClient.convertToType(data['orderType'], 'String');
            }
            if (data.hasOwnProperty('poNumber')) {
                obj['poNumber'] = ApiClient.convertToType(data['poNumber'], 'String');
            }
            if (data.hasOwnProperty('recentInvoiceId')) {
                obj['recentInvoiceId'] = ApiClient.convertToType(data['recentInvoiceId'], 'String');
            }
            if (data.hasOwnProperty('voidTime')) {
                obj['voidTime'] = ApiClient.convertToType(data['voidTime'], 'Date');
            }
            if (data.hasOwnProperty('websiteId')) {
                obj['websiteId'] = ApiClient.convertToType(data['websiteId'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CommonOneTimeOrder</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CommonOneTimeOrder</code>.
     */
    static validateJSON(data) {
        // validate the optional field `billingAddress`
        if (data['billingAddress']) { // data not null
          ContactObject.validateJSON(data['billingAddress']);
        }
        // ensure the json data is a string
        if (data['billingStatus'] && !(typeof data['billingStatus'] === 'string' || data['billingStatus'] instanceof String)) {
            throw new Error("Expected the field `billingStatus` to be a primitive type in the JSON string but got " + data['billingStatus']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['couponIds'])) {
            throw new Error("Expected the field `couponIds` to be an array in the JSON data but got " + data['couponIds']);
        }
        // validate the optional field `deliveryAddress`
        if (data['deliveryAddress']) { // data not null
          ContactObject.validateJSON(data['deliveryAddress']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['initialInvoiceId'] && !(typeof data['initialInvoiceId'] === 'string' || data['initialInvoiceId'] instanceof String)) {
            throw new Error("Expected the field `initialInvoiceId` to be a primitive type in the JSON string but got " + data['initialInvoiceId']);
        }
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                CommonSubscriptionItemsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['orderType'] && !(typeof data['orderType'] === 'string' || data['orderType'] instanceof String)) {
            throw new Error("Expected the field `orderType` to be a primitive type in the JSON string but got " + data['orderType']);
        }
        // ensure the json data is a string
        if (data['poNumber'] && !(typeof data['poNumber'] === 'string' || data['poNumber'] instanceof String)) {
            throw new Error("Expected the field `poNumber` to be a primitive type in the JSON string but got " + data['poNumber']);
        }
        // ensure the json data is a string
        if (data['recentInvoiceId'] && !(typeof data['recentInvoiceId'] === 'string' || data['recentInvoiceId'] instanceof String)) {
            throw new Error("Expected the field `recentInvoiceId` to be a primitive type in the JSON string but got " + data['recentInvoiceId']);
        }
        // ensure the json data is a string
        if (data['websiteId'] && !(typeof data['websiteId'] === 'string' || data['websiteId'] instanceof String)) {
            throw new Error("Expected the field `websiteId` to be a primitive type in the JSON string but got " + data['websiteId']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * Order activation time.
 * @member {Date} activationTime
 */
CommonOneTimeOrder.prototype['activationTime'] = undefined;

/**
 * Order billing address.
 * @member {module:model/ContactObject} billingAddress
 */
CommonOneTimeOrder.prototype['billingAddress'] = undefined;

/**
 * The billing status of the most recent invoice.  It may help you determine if you should change the service status such as suspending the service. 
 * @member {module:model/CommonOneTimeOrder.BillingStatusEnum} billingStatus
 */
CommonOneTimeOrder.prototype['billingStatus'] = undefined;

/**
 * A list of coupons to redeem on the customer and restrict to this subscription. Read more about [coupons here](https://docs.rebilly.com/docs/dashboard/marketing/coupons-and-discounts/).  This parameter respects the following logic:  - When not passed then applied coupons will not be changed.  - When empty array passed then all applied coupon redemptions will be canceled.  - When list of coupons is passed then not applied yet coupons will be applied, already applied coupons will not change their state, applied coupons that are not presented in passed list will be canceled.  If list of applied coupons on pending order will be changed due to this param during update order,  Invoice for the order will be reissued. 
 * @member {Array.<String>} couponIds
 */
CommonOneTimeOrder.prototype['couponIds'] = undefined;

/**
 * Order delivery address.
 * @member {module:model/ContactObject} deliveryAddress
 */
CommonOneTimeOrder.prototype['deliveryAddress'] = undefined;

/**
 * The order identifier string.
 * @member {String} id
 */
CommonOneTimeOrder.prototype['id'] = undefined;

/**
 * The initial invoice identifier string.
 * @member {String} initialInvoiceId
 */
CommonOneTimeOrder.prototype['initialInvoiceId'] = undefined;

/**
 * @member {Array.<module:model/CommonSubscriptionItemsInner>} items
 */
CommonOneTimeOrder.prototype['items'] = undefined;

/**
 * Specifies the type of order, a subscription or a one-time purchase. 
 * @member {module:model/CommonOneTimeOrder.OrderTypeEnum} orderType
 * @default 'subscription-order'
 */
CommonOneTimeOrder.prototype['orderType'] = 'subscription-order';

/**
 * Purchase order number, will be displayed on the issued invoices.
 * @member {String} poNumber
 */
CommonOneTimeOrder.prototype['poNumber'] = undefined;

/**
 * Most recently issued invoice identifier string. It might not be `paid` yet.
 * @member {String} recentInvoiceId
 */
CommonOneTimeOrder.prototype['recentInvoiceId'] = undefined;

/**
 * Order void time.
 * @member {Date} voidTime
 */
CommonOneTimeOrder.prototype['voidTime'] = undefined;

/**
 * The website identifier string.
 * @member {String} websiteId
 */
CommonOneTimeOrder.prototype['websiteId'] = undefined;

/**
 * One-time order status.
 * @member {module:model/CommonOneTimeOrder.StatusEnum} status
 */
CommonOneTimeOrder.prototype['status'] = undefined;


// Implement CommonSubscription interface:
/**
 * Order activation time.
 * @member {Date} activationTime
 */
CommonSubscription.prototype['activationTime'] = undefined;
/**
 * Order billing address.
 * @member {module:model/ContactObject} billingAddress
 */
CommonSubscription.prototype['billingAddress'] = undefined;
/**
 * The billing status of the most recent invoice.  It may help you determine if you should change the service status such as suspending the service. 
 * @member {module:model/CommonSubscription.BillingStatusEnum} billingStatus
 */
CommonSubscription.prototype['billingStatus'] = undefined;
/**
 * A list of coupons to redeem on the customer and restrict to this subscription. Read more about [coupons here](https://docs.rebilly.com/docs/dashboard/marketing/coupons-and-discounts/).  This parameter respects the following logic:  - When not passed then applied coupons will not be changed.  - When empty array passed then all applied coupon redemptions will be canceled.  - When list of coupons is passed then not applied yet coupons will be applied, already applied coupons will not change their state, applied coupons that are not presented in passed list will be canceled.  If list of applied coupons on pending order will be changed due to this param during update order,  Invoice for the order will be reissued. 
 * @member {Array.<String>} couponIds
 */
CommonSubscription.prototype['couponIds'] = undefined;
/**
 * Order delivery address.
 * @member {module:model/ContactObject} deliveryAddress
 */
CommonSubscription.prototype['deliveryAddress'] = undefined;
/**
 * The order identifier string.
 * @member {String} id
 */
CommonSubscription.prototype['id'] = undefined;
/**
 * The initial invoice identifier string.
 * @member {String} initialInvoiceId
 */
CommonSubscription.prototype['initialInvoiceId'] = undefined;
/**
 * @member {Array.<module:model/CommonSubscriptionItemsInner>} items
 */
CommonSubscription.prototype['items'] = undefined;
/**
 * Specifies the type of order, a subscription or a one-time purchase. 
 * @member {module:model/CommonSubscription.OrderTypeEnum} orderType
 * @default 'subscription-order'
 */
CommonSubscription.prototype['orderType'] = 'subscription-order';
/**
 * Purchase order number, will be displayed on the issued invoices.
 * @member {String} poNumber
 */
CommonSubscription.prototype['poNumber'] = undefined;
/**
 * Most recently issued invoice identifier string. It might not be `paid` yet.
 * @member {String} recentInvoiceId
 */
CommonSubscription.prototype['recentInvoiceId'] = undefined;
/**
 * Order void time.
 * @member {Date} voidTime
 */
CommonSubscription.prototype['voidTime'] = undefined;
/**
 * The website identifier string.
 * @member {String} websiteId
 */
CommonSubscription.prototype['websiteId'] = undefined;



/**
 * Allowed values for the <code>billingStatus</code> property.
 * @enum {String}
 * @readonly
 */
CommonOneTimeOrder['BillingStatusEnum'] = {

    /**
     * value: "unpaid"
     * @const
     */
    "unpaid": "unpaid",

    /**
     * value: "past-due"
     * @const
     */
    "past-due": "past-due",

    /**
     * value: "delinquent"
     * @const
     */
    "delinquent": "delinquent",

    /**
     * value: "paid"
     * @const
     */
    "paid": "paid",

    /**
     * value: "voided"
     * @const
     */
    "voided": "voided",

    /**
     * value: "refunded"
     * @const
     */
    "refunded": "refunded",

    /**
     * value: "disputed"
     * @const
     */
    "disputed": "disputed",

    /**
     * value: "voided"
     * @const
     */
    "voided2": "voided"
};


/**
 * Allowed values for the <code>orderType</code> property.
 * @enum {String}
 * @readonly
 */
CommonOneTimeOrder['OrderTypeEnum'] = {

    /**
     * value: "subscription-order"
     * @const
     */
    "subscription-order": "subscription-order",

    /**
     * value: "one-time-order"
     * @const
     */
    "one-time-order": "one-time-order"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
CommonOneTimeOrder['StatusEnum'] = {

    /**
     * value: "pending"
     * @const
     */
    "pending": "pending",

    /**
     * value: "completed"
     * @const
     */
    "completed": "completed",

    /**
     * value: "abandoned"
     * @const
     */
    "abandoned": "abandoned"
};



export default CommonOneTimeOrder;

