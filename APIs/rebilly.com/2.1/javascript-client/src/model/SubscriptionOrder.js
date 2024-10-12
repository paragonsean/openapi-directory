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
import CommonSubscriptionItemsInner from './CommonSubscriptionItemsInner';
import CommonSubscriptionOrder from './CommonSubscriptionOrder';
import CommonSubscriptionOrderAllOfLineItemSubtotal from './CommonSubscriptionOrderAllOfLineItemSubtotal';
import CommonSubscriptionOrderAllOfRecurringInterval from './CommonSubscriptionOrderAllOfRecurringInterval';
import CommonSubscriptionOrderAllOfTrial from './CommonSubscriptionOrderAllOfTrial';
import ContactObject from './ContactObject';
import InvoiceTimeShift from './InvoiceTimeShift';
import RiskMetadata from './RiskMetadata';
import SubscriptionCancellationState from './SubscriptionCancellationState';
import SubscriptionMetadata from './SubscriptionMetadata';
import SubscriptionMetadataEmbeddedInner from './SubscriptionMetadataEmbeddedInner';
import SubscriptionMetadataLinksInner from './SubscriptionMetadataLinksInner';
import UpcomingInvoiceItem from './UpcomingInvoiceItem';

/**
 * The SubscriptionOrder model module.
 * @module model/SubscriptionOrder
 * @version 2.1
 */
class SubscriptionOrder {
    /**
     * Constructs a new <code>SubscriptionOrder</code>.
     * @alias module:model/SubscriptionOrder
     * @implements module:model/CommonSubscriptionOrder
     * @implements module:model/SubscriptionCancellationState
     * @implements module:model/SubscriptionMetadata
     * @param items {Array.<module:model/CommonSubscriptionItemsInner>} 
     * @param orderType {module:model/SubscriptionOrder.OrderTypeEnum} Specifies the type of order, a subscription or a one-time purchase. 
     * @param websiteId {String} The website identifier string.
     * @param customerId {String} The customer identifier string.
     */
    constructor(items, orderType, websiteId, customerId) { 
        CommonSubscriptionOrder.initialize(this);SubscriptionCancellationState.initialize(this);SubscriptionMetadata.initialize(this);
        SubscriptionOrder.initialize(this, items, orderType, websiteId, customerId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, items, orderType, websiteId, customerId) { 
        obj['items'] = items;
        obj['orderType'] = orderType || 'subscription-order';
        obj['websiteId'] = websiteId;
        obj['autopay'] = true;
        obj['isTrialOnly'] = false;
        obj['customerId'] = customerId;
    }

    /**
     * Constructs a <code>SubscriptionOrder</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SubscriptionOrder} obj Optional instance to populate.
     * @return {module:model/SubscriptionOrder} The populated <code>SubscriptionOrder</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SubscriptionOrder();
            CommonSubscriptionOrder.constructFromObject(data, obj);
            SubscriptionCancellationState.constructFromObject(data, obj);
            SubscriptionMetadata.constructFromObject(data, obj);

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
            if (data.hasOwnProperty('autopay')) {
                obj['autopay'] = ApiClient.convertToType(data['autopay'], 'Boolean');
            }
            if (data.hasOwnProperty('endTime')) {
                obj['endTime'] = ApiClient.convertToType(data['endTime'], 'Date');
            }
            if (data.hasOwnProperty('inTrial')) {
                obj['inTrial'] = ApiClient.convertToType(data['inTrial'], 'Boolean');
            }
            if (data.hasOwnProperty('invoiceTimeShift')) {
                obj['invoiceTimeShift'] = ApiClient.convertToType(data['invoiceTimeShift'], InvoiceTimeShift);
            }
            if (data.hasOwnProperty('isTrialOnly')) {
                obj['isTrialOnly'] = ApiClient.convertToType(data['isTrialOnly'], 'Boolean');
            }
            if (data.hasOwnProperty('lineItemSubtotal')) {
                obj['lineItemSubtotal'] = CommonSubscriptionOrderAllOfLineItemSubtotal.constructFromObject(data['lineItemSubtotal']);
            }
            if (data.hasOwnProperty('lineItems')) {
                obj['lineItems'] = ApiClient.convertToType(data['lineItems'], Array);
            }
            if (data.hasOwnProperty('rebillNumber')) {
                obj['rebillNumber'] = ApiClient.convertToType(data['rebillNumber'], 'Number');
            }
            if (data.hasOwnProperty('recurringInterval')) {
                obj['recurringInterval'] = CommonSubscriptionOrderAllOfRecurringInterval.constructFromObject(data['recurringInterval']);
            }
            if (data.hasOwnProperty('renewalTime')) {
                obj['renewalTime'] = ApiClient.convertToType(data['renewalTime'], 'Date');
            }
            if (data.hasOwnProperty('startTime')) {
                obj['startTime'] = ApiClient.convertToType(data['startTime'], 'Date');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('trial')) {
                obj['trial'] = CommonSubscriptionOrderAllOfTrial.constructFromObject(data['trial']);
            }
            if (data.hasOwnProperty('cancelCategory')) {
                obj['cancelCategory'] = ApiClient.convertToType(data['cancelCategory'], 'String');
            }
            if (data.hasOwnProperty('cancelDescription')) {
                obj['cancelDescription'] = ApiClient.convertToType(data['cancelDescription'], 'String');
            }
            if (data.hasOwnProperty('canceledBy')) {
                obj['canceledBy'] = ApiClient.convertToType(data['canceledBy'], 'String');
            }
            if (data.hasOwnProperty('canceledTime')) {
                obj['canceledTime'] = ApiClient.convertToType(data['canceledTime'], 'Date');
            }
            if (data.hasOwnProperty('_embedded')) {
                obj['_embedded'] = ApiClient.convertToType(data['_embedded'], [SubscriptionMetadataEmbeddedInner]);
            }
            if (data.hasOwnProperty('_links')) {
                obj['_links'] = ApiClient.convertToType(data['_links'], [SubscriptionMetadataLinksInner]);
            }
            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Date');
            }
            if (data.hasOwnProperty('customFields')) {
                obj['customFields'] = ApiClient.convertToType(data['customFields'], Object);
            }
            if (data.hasOwnProperty('revision')) {
                obj['revision'] = ApiClient.convertToType(data['revision'], 'Number');
            }
            if (data.hasOwnProperty('riskMetadata')) {
                obj['riskMetadata'] = ApiClient.convertToType(data['riskMetadata'], RiskMetadata);
            }
            if (data.hasOwnProperty('updatedTime')) {
                obj['updatedTime'] = ApiClient.convertToType(data['updatedTime'], 'Date');
            }
            if (data.hasOwnProperty('customerId')) {
                obj['customerId'] = ApiClient.convertToType(data['customerId'], 'String');
            }
            if (data.hasOwnProperty('renewalReminderNumber')) {
                obj['renewalReminderNumber'] = ApiClient.convertToType(data['renewalReminderNumber'], 'Number');
            }
            if (data.hasOwnProperty('renewalReminderTime')) {
                obj['renewalReminderTime'] = ApiClient.convertToType(data['renewalReminderTime'], 'Date');
            }
            if (data.hasOwnProperty('trialReminderNumber')) {
                obj['trialReminderNumber'] = ApiClient.convertToType(data['trialReminderNumber'], 'Number');
            }
            if (data.hasOwnProperty('trialReminderTime')) {
                obj['trialReminderTime'] = ApiClient.convertToType(data['trialReminderTime'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SubscriptionOrder</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SubscriptionOrder</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SubscriptionOrder.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
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
        // validate the optional field `invoiceTimeShift`
        if (data['invoiceTimeShift']) { // data not null
          InvoiceTimeShift.validateJSON(data['invoiceTimeShift']);
        }
        // validate the optional field `lineItemSubtotal`
        if (data['lineItemSubtotal']) { // data not null
          CommonSubscriptionOrderAllOfLineItemSubtotal.validateJSON(data['lineItemSubtotal']);
        }
        if (data['lineItems']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['lineItems'])) {
                throw new Error("Expected the field `lineItems` to be an array in the JSON data but got " + data['lineItems']);
            }
            // validate the optional field `lineItems` (array)
            for (const item of data['lineItems']) {
                UpcomingInvoiceItem.validateJSON(item);
            };
        }
        // validate the optional field `recurringInterval`
        if (data['recurringInterval']) { // data not null
          CommonSubscriptionOrderAllOfRecurringInterval.validateJSON(data['recurringInterval']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // validate the optional field `trial`
        if (data['trial']) { // data not null
          CommonSubscriptionOrderAllOfTrial.validateJSON(data['trial']);
        }
        // ensure the json data is a string
        if (data['cancelCategory'] && !(typeof data['cancelCategory'] === 'string' || data['cancelCategory'] instanceof String)) {
            throw new Error("Expected the field `cancelCategory` to be a primitive type in the JSON string but got " + data['cancelCategory']);
        }
        // ensure the json data is a string
        if (data['cancelDescription'] && !(typeof data['cancelDescription'] === 'string' || data['cancelDescription'] instanceof String)) {
            throw new Error("Expected the field `cancelDescription` to be a primitive type in the JSON string but got " + data['cancelDescription']);
        }
        // ensure the json data is a string
        if (data['canceledBy'] && !(typeof data['canceledBy'] === 'string' || data['canceledBy'] instanceof String)) {
            throw new Error("Expected the field `canceledBy` to be a primitive type in the JSON string but got " + data['canceledBy']);
        }
        if (data['_embedded']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_embedded'])) {
                throw new Error("Expected the field `_embedded` to be an array in the JSON data but got " + data['_embedded']);
            }
            // validate the optional field `_embedded` (array)
            for (const item of data['_embedded']) {
                SubscriptionMetadataEmbeddedInner.validateJSON(item);
            };
        }
        if (data['_links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['_links'])) {
                throw new Error("Expected the field `_links` to be an array in the JSON data but got " + data['_links']);
            }
            // validate the optional field `_links` (array)
            for (const item of data['_links']) {
                SubscriptionMetadataLinksInner.validateJSON(item);
            };
        }
        // validate the optional field `riskMetadata`
        if (data['riskMetadata']) { // data not null
          RiskMetadata.validateJSON(data['riskMetadata']);
        }
        // ensure the json data is a string
        if (data['customerId'] && !(typeof data['customerId'] === 'string' || data['customerId'] instanceof String)) {
            throw new Error("Expected the field `customerId` to be a primitive type in the JSON string but got " + data['customerId']);
        }

        return true;
    }


}

SubscriptionOrder.RequiredProperties = ["items", "orderType", "websiteId", "customerId"];

/**
 * Order activation time.
 * @member {Date} activationTime
 */
SubscriptionOrder.prototype['activationTime'] = undefined;

/**
 * Order billing address.
 * @member {module:model/ContactObject} billingAddress
 */
SubscriptionOrder.prototype['billingAddress'] = undefined;

/**
 * The billing status of the most recent invoice.  It may help you determine if you should change the service status such as suspending the service. 
 * @member {module:model/SubscriptionOrder.BillingStatusEnum} billingStatus
 */
SubscriptionOrder.prototype['billingStatus'] = undefined;

/**
 * A list of coupons to redeem on the customer and restrict to this subscription. Read more about [coupons here](https://docs.rebilly.com/docs/dashboard/marketing/coupons-and-discounts/).  This parameter respects the following logic:  - When not passed then applied coupons will not be changed.  - When empty array passed then all applied coupon redemptions will be canceled.  - When list of coupons is passed then not applied yet coupons will be applied, already applied coupons will not change their state, applied coupons that are not presented in passed list will be canceled.  If list of applied coupons on pending order will be changed due to this param during update order,  Invoice for the order will be reissued. 
 * @member {Array.<String>} couponIds
 */
SubscriptionOrder.prototype['couponIds'] = undefined;

/**
 * Order delivery address.
 * @member {module:model/ContactObject} deliveryAddress
 */
SubscriptionOrder.prototype['deliveryAddress'] = undefined;

/**
 * The order identifier string.
 * @member {String} id
 */
SubscriptionOrder.prototype['id'] = undefined;

/**
 * The initial invoice identifier string.
 * @member {String} initialInvoiceId
 */
SubscriptionOrder.prototype['initialInvoiceId'] = undefined;

/**
 * @member {Array.<module:model/CommonSubscriptionItemsInner>} items
 */
SubscriptionOrder.prototype['items'] = undefined;

/**
 * Specifies the type of order, a subscription or a one-time purchase. 
 * @member {module:model/SubscriptionOrder.OrderTypeEnum} orderType
 * @default 'subscription-order'
 */
SubscriptionOrder.prototype['orderType'] = 'subscription-order';

/**
 * Purchase order number, will be displayed on the issued invoices.
 * @member {String} poNumber
 */
SubscriptionOrder.prototype['poNumber'] = undefined;

/**
 * Most recently issued invoice identifier string. It might not be `paid` yet.
 * @member {String} recentInvoiceId
 */
SubscriptionOrder.prototype['recentInvoiceId'] = undefined;

/**
 * Order void time.
 * @member {Date} voidTime
 */
SubscriptionOrder.prototype['voidTime'] = undefined;

/**
 * The website identifier string.
 * @member {String} websiteId
 */
SubscriptionOrder.prototype['websiteId'] = undefined;

/**
 * Autopay determines if a payment attempt will be automatic.
 * @member {Boolean} autopay
 * @default true
 */
SubscriptionOrder.prototype['autopay'] = true;

/**
 * Subscription end time.
 * @member {Date} endTime
 */
SubscriptionOrder.prototype['endTime'] = undefined;

/**
 * True if the subscription is currently in a trial period.
 * @member {Boolean} inTrial
 */
SubscriptionOrder.prototype['inTrial'] = undefined;

/**
 * You can shift issue time and due time of invoices for this subscription. This setting overrides plan settings. To use plan settings, set `null`. To use multiple plans in one subscription they all must have the same billing period, this property allows to subscribe to different plans. 
 * @member {module:model/InvoiceTimeShift} invoiceTimeShift
 */
SubscriptionOrder.prototype['invoiceTimeShift'] = undefined;

/**
 * Whether a subscription ends after a trial period. Recurring settings are ignored if it's `true`.
 * @member {Boolean} isTrialOnly
 * @default false
 */
SubscriptionOrder.prototype['isTrialOnly'] = false;

/**
 * @member {module:model/CommonSubscriptionOrderAllOfLineItemSubtotal} lineItemSubtotal
 */
SubscriptionOrder.prototype['lineItemSubtotal'] = undefined;

/**
 * Subscription line items which queue until the next renewal (or interim) invoice is issued for the subscription.
 * @member {Array.<module:model/UpcomingInvoiceItem>} lineItems
 */
SubscriptionOrder.prototype['lineItems'] = undefined;

/**
 * The current period number.
 * @member {Number} rebillNumber
 */
SubscriptionOrder.prototype['rebillNumber'] = undefined;

/**
 * @member {module:model/CommonSubscriptionOrderAllOfRecurringInterval} recurringInterval
 */
SubscriptionOrder.prototype['recurringInterval'] = undefined;

/**
 * Subscription renewal time.
 * @member {Date} renewalTime
 */
SubscriptionOrder.prototype['renewalTime'] = undefined;

/**
 * Subscription start time.  When the value is sent as null, it will use the current time. This value can't be in past more than one service period.
 * @member {Date} startTime
 */
SubscriptionOrder.prototype['startTime'] = undefined;

/**
 * The status of the subscription service. A subscription starts in the `pending` status, and will become `active` when the service period begins. 
 * @member {module:model/SubscriptionOrder.StatusEnum} status
 */
SubscriptionOrder.prototype['status'] = undefined;

/**
 * @member {module:model/CommonSubscriptionOrderAllOfTrial} trial
 */
SubscriptionOrder.prototype['trial'] = undefined;

/**
 * Cancel category.
 * @member {module:model/SubscriptionOrder.CancelCategoryEnum} cancelCategory
 */
SubscriptionOrder.prototype['cancelCategory'] = undefined;

/**
 * Cancel reason description in free form.
 * @member {String} cancelDescription
 */
SubscriptionOrder.prototype['cancelDescription'] = undefined;

/**
 * Canceled by.
 * @member {module:model/SubscriptionOrder.CanceledByEnum} canceledBy
 */
SubscriptionOrder.prototype['canceledBy'] = undefined;

/**
 * Subscription order canceled time.
 * @member {Date} canceledTime
 */
SubscriptionOrder.prototype['canceledTime'] = undefined;

/**
 * Any embedded objects available that are requested by the `expand` querystring parameter.
 * @member {Array.<module:model/SubscriptionMetadataEmbeddedInner>} _embedded
 */
SubscriptionOrder.prototype['_embedded'] = undefined;

/**
 * The links related to resource.
 * @member {Array.<module:model/SubscriptionMetadataLinksInner>} _links
 */
SubscriptionOrder.prototype['_links'] = undefined;

/**
 * Order created time.
 * @member {Date} createdTime
 */
SubscriptionOrder.prototype['createdTime'] = undefined;

/**
 * Custom Fields list as a map `{\"custom field name\": \"custom field value\", ...}`. The format must follow the saved format (see Custom Fields section for the formats). 
 * @member {Object} customFields
 */
SubscriptionOrder.prototype['customFields'] = undefined;

/**
 * The number of times the order data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation. 
 * @member {Number} revision
 */
SubscriptionOrder.prototype['revision'] = undefined;

/**
 * Risk metadata. If null, the value would coalesce to the risk metadata captured when creating the payment token.
 * @member {module:model/RiskMetadata} riskMetadata
 */
SubscriptionOrder.prototype['riskMetadata'] = undefined;

/**
 * Order updated time.
 * @member {Date} updatedTime
 */
SubscriptionOrder.prototype['updatedTime'] = undefined;

/**
 * The customer identifier string.
 * @member {String} customerId
 */
SubscriptionOrder.prototype['customerId'] = undefined;

/**
 * Number of renewal reminder events triggered.
 * @member {Number} renewalReminderNumber
 */
SubscriptionOrder.prototype['renewalReminderNumber'] = undefined;

/**
 * Time renewal reminder event will be triggered.
 * @member {Date} renewalReminderTime
 */
SubscriptionOrder.prototype['renewalReminderTime'] = undefined;

/**
 * Number of renewal reminder events triggered.
 * @member {Number} trialReminderNumber
 */
SubscriptionOrder.prototype['trialReminderNumber'] = undefined;

/**
 * Time renewal reminder event will be triggered.
 * @member {Date} trialReminderTime
 */
SubscriptionOrder.prototype['trialReminderTime'] = undefined;


// Implement CommonSubscriptionOrder interface:
/**
 * Order activation time.
 * @member {Date} activationTime
 */
CommonSubscriptionOrder.prototype['activationTime'] = undefined;
/**
 * Order billing address.
 * @member {module:model/ContactObject} billingAddress
 */
CommonSubscriptionOrder.prototype['billingAddress'] = undefined;
/**
 * The billing status of the most recent invoice.  It may help you determine if you should change the service status such as suspending the service. 
 * @member {module:model/CommonSubscriptionOrder.BillingStatusEnum} billingStatus
 */
CommonSubscriptionOrder.prototype['billingStatus'] = undefined;
/**
 * A list of coupons to redeem on the customer and restrict to this subscription. Read more about [coupons here](https://docs.rebilly.com/docs/dashboard/marketing/coupons-and-discounts/).  This parameter respects the following logic:  - When not passed then applied coupons will not be changed.  - When empty array passed then all applied coupon redemptions will be canceled.  - When list of coupons is passed then not applied yet coupons will be applied, already applied coupons will not change their state, applied coupons that are not presented in passed list will be canceled.  If list of applied coupons on pending order will be changed due to this param during update order,  Invoice for the order will be reissued. 
 * @member {Array.<String>} couponIds
 */
CommonSubscriptionOrder.prototype['couponIds'] = undefined;
/**
 * Order delivery address.
 * @member {module:model/ContactObject} deliveryAddress
 */
CommonSubscriptionOrder.prototype['deliveryAddress'] = undefined;
/**
 * The order identifier string.
 * @member {String} id
 */
CommonSubscriptionOrder.prototype['id'] = undefined;
/**
 * The initial invoice identifier string.
 * @member {String} initialInvoiceId
 */
CommonSubscriptionOrder.prototype['initialInvoiceId'] = undefined;
/**
 * @member {Array.<module:model/CommonSubscriptionItemsInner>} items
 */
CommonSubscriptionOrder.prototype['items'] = undefined;
/**
 * Specifies the type of order, a subscription or a one-time purchase. 
 * @member {module:model/CommonSubscriptionOrder.OrderTypeEnum} orderType
 * @default 'subscription-order'
 */
CommonSubscriptionOrder.prototype['orderType'] = 'subscription-order';
/**
 * Purchase order number, will be displayed on the issued invoices.
 * @member {String} poNumber
 */
CommonSubscriptionOrder.prototype['poNumber'] = undefined;
/**
 * Most recently issued invoice identifier string. It might not be `paid` yet.
 * @member {String} recentInvoiceId
 */
CommonSubscriptionOrder.prototype['recentInvoiceId'] = undefined;
/**
 * Order void time.
 * @member {Date} voidTime
 */
CommonSubscriptionOrder.prototype['voidTime'] = undefined;
/**
 * The website identifier string.
 * @member {String} websiteId
 */
CommonSubscriptionOrder.prototype['websiteId'] = undefined;
/**
 * Autopay determines if a payment attempt will be automatic.
 * @member {Boolean} autopay
 * @default true
 */
CommonSubscriptionOrder.prototype['autopay'] = true;
/**
 * Subscription end time.
 * @member {Date} endTime
 */
CommonSubscriptionOrder.prototype['endTime'] = undefined;
/**
 * True if the subscription is currently in a trial period.
 * @member {Boolean} inTrial
 */
CommonSubscriptionOrder.prototype['inTrial'] = undefined;
/**
 * You can shift issue time and due time of invoices for this subscription. This setting overrides plan settings. To use plan settings, set `null`. To use multiple plans in one subscription they all must have the same billing period, this property allows to subscribe to different plans. 
 * @member {module:model/InvoiceTimeShift} invoiceTimeShift
 */
CommonSubscriptionOrder.prototype['invoiceTimeShift'] = undefined;
/**
 * Whether a subscription ends after a trial period. Recurring settings are ignored if it's `true`.
 * @member {Boolean} isTrialOnly
 * @default false
 */
CommonSubscriptionOrder.prototype['isTrialOnly'] = false;
/**
 * @member {module:model/CommonSubscriptionOrderAllOfLineItemSubtotal} lineItemSubtotal
 */
CommonSubscriptionOrder.prototype['lineItemSubtotal'] = undefined;
/**
 * Subscription line items which queue until the next renewal (or interim) invoice is issued for the subscription.
 * @member {Array.<module:model/UpcomingInvoiceItem>} lineItems
 */
CommonSubscriptionOrder.prototype['lineItems'] = undefined;
/**
 * The current period number.
 * @member {Number} rebillNumber
 */
CommonSubscriptionOrder.prototype['rebillNumber'] = undefined;
/**
 * @member {module:model/CommonSubscriptionOrderAllOfRecurringInterval} recurringInterval
 */
CommonSubscriptionOrder.prototype['recurringInterval'] = undefined;
/**
 * Subscription renewal time.
 * @member {Date} renewalTime
 */
CommonSubscriptionOrder.prototype['renewalTime'] = undefined;
/**
 * Subscription start time.  When the value is sent as null, it will use the current time. This value can't be in past more than one service period.
 * @member {Date} startTime
 */
CommonSubscriptionOrder.prototype['startTime'] = undefined;
/**
 * The status of the subscription service. A subscription starts in the `pending` status, and will become `active` when the service period begins. 
 * @member {module:model/CommonSubscriptionOrder.StatusEnum} status
 */
CommonSubscriptionOrder.prototype['status'] = undefined;
/**
 * @member {module:model/CommonSubscriptionOrderAllOfTrial} trial
 */
CommonSubscriptionOrder.prototype['trial'] = undefined;
// Implement SubscriptionCancellationState interface:
/**
 * Cancel category.
 * @member {module:model/SubscriptionCancellationState.CancelCategoryEnum} cancelCategory
 */
SubscriptionCancellationState.prototype['cancelCategory'] = undefined;
/**
 * Cancel reason description in free form.
 * @member {String} cancelDescription
 */
SubscriptionCancellationState.prototype['cancelDescription'] = undefined;
/**
 * Canceled by.
 * @member {module:model/SubscriptionCancellationState.CanceledByEnum} canceledBy
 */
SubscriptionCancellationState.prototype['canceledBy'] = undefined;
/**
 * Subscription order canceled time.
 * @member {Date} canceledTime
 */
SubscriptionCancellationState.prototype['canceledTime'] = undefined;
// Implement SubscriptionMetadata interface:
/**
 * Any embedded objects available that are requested by the `expand` querystring parameter.
 * @member {Array.<module:model/SubscriptionMetadataEmbeddedInner>} _embedded
 */
SubscriptionMetadata.prototype['_embedded'] = undefined;
/**
 * The links related to resource.
 * @member {Array.<module:model/SubscriptionMetadataLinksInner>} _links
 */
SubscriptionMetadata.prototype['_links'] = undefined;
/**
 * Order created time.
 * @member {Date} createdTime
 */
SubscriptionMetadata.prototype['createdTime'] = undefined;
/**
 * Custom Fields list as a map `{\"custom field name\": \"custom field value\", ...}`. The format must follow the saved format (see Custom Fields section for the formats). 
 * @member {Object} customFields
 */
SubscriptionMetadata.prototype['customFields'] = undefined;
/**
 * The number of times the order data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation. 
 * @member {Number} revision
 */
SubscriptionMetadata.prototype['revision'] = undefined;
/**
 * Risk metadata. If null, the value would coalesce to the risk metadata captured when creating the payment token.
 * @member {module:model/RiskMetadata} riskMetadata
 */
SubscriptionMetadata.prototype['riskMetadata'] = undefined;
/**
 * Order updated time.
 * @member {Date} updatedTime
 */
SubscriptionMetadata.prototype['updatedTime'] = undefined;



/**
 * Allowed values for the <code>billingStatus</code> property.
 * @enum {String}
 * @readonly
 */
SubscriptionOrder['BillingStatusEnum'] = {

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
SubscriptionOrder['OrderTypeEnum'] = {

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
SubscriptionOrder['StatusEnum'] = {

    /**
     * value: "pending"
     * @const
     */
    "pending": "pending",

    /**
     * value: "active"
     * @const
     */
    "active": "active",

    /**
     * value: "canceled"
     * @const
     */
    "canceled": "canceled",

    /**
     * value: "churned"
     * @const
     */
    "churned": "churned",

    /**
     * value: "suspended"
     * @const
     */
    "suspended": "suspended",

    /**
     * value: "paused"
     * @const
     */
    "paused": "paused",

    /**
     * value: "abandoned"
     * @const
     */
    "abandoned": "abandoned",

    /**
     * value: "trial-ended"
     * @const
     */
    "trial-ended": "trial-ended"
};


/**
 * Allowed values for the <code>cancelCategory</code> property.
 * @enum {String}
 * @readonly
 */
SubscriptionOrder['CancelCategoryEnum'] = {

    /**
     * value: "billing-failure"
     * @const
     */
    "billing-failure": "billing-failure",

    /**
     * value: "did-not-use"
     * @const
     */
    "did-not-use": "did-not-use",

    /**
     * value: "did-not-want"
     * @const
     */
    "did-not-want": "did-not-want",

    /**
     * value: "missing-features"
     * @const
     */
    "missing-features": "missing-features",

    /**
     * value: "bugs-or-problems"
     * @const
     */
    "bugs-or-problems": "bugs-or-problems",

    /**
     * value: "do-not-remember"
     * @const
     */
    "do-not-remember": "do-not-remember",

    /**
     * value: "risk-warning"
     * @const
     */
    "risk-warning": "risk-warning",

    /**
     * value: "contract-expired"
     * @const
     */
    "contract-expired": "contract-expired",

    /**
     * value: "too-expensive"
     * @const
     */
    "too-expensive": "too-expensive",

    /**
     * value: "never-started"
     * @const
     */
    "never-started": "never-started",

    /**
     * value: "switched-plan"
     * @const
     */
    "switched-plan": "switched-plan",

    /**
     * value: "other"
     * @const
     */
    "other": "other"
};


/**
 * Allowed values for the <code>canceledBy</code> property.
 * @enum {String}
 * @readonly
 */
SubscriptionOrder['CanceledByEnum'] = {

    /**
     * value: "merchant"
     * @const
     */
    "merchant": "merchant",

    /**
     * value: "customer"
     * @const
     */
    "customer": "customer",

    /**
     * value: "rebilly"
     * @const
     */
    "rebilly": "rebilly"
};



export default SubscriptionOrder;

