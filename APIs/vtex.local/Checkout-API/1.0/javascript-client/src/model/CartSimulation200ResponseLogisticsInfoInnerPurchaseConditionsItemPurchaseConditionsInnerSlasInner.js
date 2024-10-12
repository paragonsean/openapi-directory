/**
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner from './AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner';
import CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows from './CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows';
import CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow from './CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow';
import CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo from './CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo';

/**
 * The CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner model module.
 * @module model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner
 * @version 1.0
 */
class CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner {
    /**
     * Constructs a new <code>CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner</code>.
     * @alias module:model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner
     */
    constructor() { 
        
        CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner} obj Optional instance to populate.
     * @return {module:model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner} The populated <code>CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner();

            if (data.hasOwnProperty('availableDeliveryWindows')) {
                obj['availableDeliveryWindows'] = CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.constructFromObject(data['availableDeliveryWindows']);
            }
            if (data.hasOwnProperty('deliveryChannel')) {
                obj['deliveryChannel'] = ApiClient.convertToType(data['deliveryChannel'], 'String');
            }
            if (data.hasOwnProperty('deliveryIds')) {
                obj['deliveryIds'] = ApiClient.convertToType(data['deliveryIds'], [AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner]);
            }
            if (data.hasOwnProperty('deliveryWindow')) {
                obj['deliveryWindow'] = CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow.constructFromObject(data['deliveryWindow']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('listPrice')) {
                obj['listPrice'] = ApiClient.convertToType(data['listPrice'], 'Number');
            }
            if (data.hasOwnProperty('lockTTL')) {
                obj['lockTTL'] = ApiClient.convertToType(data['lockTTL'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('pickupDistance')) {
                obj['pickupDistance'] = ApiClient.convertToType(data['pickupDistance'], 'Number');
            }
            if (data.hasOwnProperty('pickupPointId')) {
                obj['pickupPointId'] = ApiClient.convertToType(data['pickupPointId'], 'String');
            }
            if (data.hasOwnProperty('pickupStoreInfo')) {
                obj['pickupStoreInfo'] = CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo.constructFromObject(data['pickupStoreInfo']);
            }
            if (data.hasOwnProperty('polygonName')) {
                obj['polygonName'] = ApiClient.convertToType(data['polygonName'], 'String');
            }
            if (data.hasOwnProperty('price')) {
                obj['price'] = ApiClient.convertToType(data['price'], 'Number');
            }
            if (data.hasOwnProperty('shippingEstimate')) {
                obj['shippingEstimate'] = ApiClient.convertToType(data['shippingEstimate'], 'String');
            }
            if (data.hasOwnProperty('shippingEstimateDate')) {
                obj['shippingEstimateDate'] = ApiClient.convertToType(data['shippingEstimateDate'], 'String');
            }
            if (data.hasOwnProperty('tax')) {
                obj['tax'] = ApiClient.convertToType(data['tax'], 'Number');
            }
            if (data.hasOwnProperty('transitTime')) {
                obj['transitTime'] = ApiClient.convertToType(data['transitTime'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner</code>.
     */
    static validateJSON(data) {
        // validate the optional field `availableDeliveryWindows`
        if (data['availableDeliveryWindows']) { // data not null
          CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.validateJSON(data['availableDeliveryWindows']);
        }
        // ensure the json data is a string
        if (data['deliveryChannel'] && !(typeof data['deliveryChannel'] === 'string' || data['deliveryChannel'] instanceof String)) {
            throw new Error("Expected the field `deliveryChannel` to be a primitive type in the JSON string but got " + data['deliveryChannel']);
        }
        if (data['deliveryIds']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['deliveryIds'])) {
                throw new Error("Expected the field `deliveryIds` to be an array in the JSON data but got " + data['deliveryIds']);
            }
            // validate the optional field `deliveryIds` (array)
            for (const item of data['deliveryIds']) {
                AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner.validateJSON(item);
            };
        }
        // validate the optional field `deliveryWindow`
        if (data['deliveryWindow']) { // data not null
          CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow.validateJSON(data['deliveryWindow']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['lockTTL'] && !(typeof data['lockTTL'] === 'string' || data['lockTTL'] instanceof String)) {
            throw new Error("Expected the field `lockTTL` to be a primitive type in the JSON string but got " + data['lockTTL']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['pickupPointId'] && !(typeof data['pickupPointId'] === 'string' || data['pickupPointId'] instanceof String)) {
            throw new Error("Expected the field `pickupPointId` to be a primitive type in the JSON string but got " + data['pickupPointId']);
        }
        // validate the optional field `pickupStoreInfo`
        if (data['pickupStoreInfo']) { // data not null
          CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo.validateJSON(data['pickupStoreInfo']);
        }
        // ensure the json data is a string
        if (data['polygonName'] && !(typeof data['polygonName'] === 'string' || data['polygonName'] instanceof String)) {
            throw new Error("Expected the field `polygonName` to be a primitive type in the JSON string but got " + data['polygonName']);
        }
        // ensure the json data is a string
        if (data['shippingEstimate'] && !(typeof data['shippingEstimate'] === 'string' || data['shippingEstimate'] instanceof String)) {
            throw new Error("Expected the field `shippingEstimate` to be a primitive type in the JSON string but got " + data['shippingEstimate']);
        }
        // ensure the json data is a string
        if (data['shippingEstimateDate'] && !(typeof data['shippingEstimateDate'] === 'string' || data['shippingEstimateDate'] instanceof String)) {
            throw new Error("Expected the field `shippingEstimateDate` to be a primitive type in the JSON string but got " + data['shippingEstimateDate']);
        }
        // ensure the json data is a string
        if (data['transitTime'] && !(typeof data['transitTime'] === 'string' || data['transitTime'] instanceof String)) {
            throw new Error("Expected the field `transitTime` to be a primitive type in the JSON string but got " + data['transitTime']);
        }

        return true;
    }


}



/**
 * @member {module:model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows} availableDeliveryWindows
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['availableDeliveryWindows'] = undefined;

/**
 * Delivery channel.
 * @member {String} deliveryChannel
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['deliveryChannel'] = undefined;

/**
 * Information on each delivery ID.
 * @member {Array.<module:model/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner>} deliveryIds
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['deliveryIds'] = undefined;

/**
 * @member {module:model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow} deliveryWindow
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['deliveryWindow'] = undefined;

/**
 * SLA ID.
 * @member {String} id
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['id'] = undefined;

/**
 * List price in cents.
 * @member {Number} listPrice
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['listPrice'] = undefined;

/**
 * Estimate date of delivery.
 * @member {String} lockTTL
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['lockTTL'] = undefined;

/**
 * SLA name.
 * @member {String} name
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['name'] = undefined;

/**
 * Pickup point distance.
 * @member {Number} pickupDistance
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['pickupDistance'] = undefined;

/**
 * Pickup point ID.
 * @member {String} pickupPointId
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['pickupPointId'] = undefined;

/**
 * @member {module:model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo} pickupStoreInfo
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['pickupStoreInfo'] = undefined;

/**
 * Polygon name.
 * @member {String} polygonName
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['polygonName'] = undefined;

/**
 * Price in cents.
 * @member {Number} price
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['price'] = undefined;

/**
 * Shipping estimate. For instance, \"three business days\" will be represented as `3bd`.
 * @member {String} shippingEstimate
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['shippingEstimate'] = undefined;

/**
 * Shipping estimate date.
 * @member {String} shippingEstimateDate
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['shippingEstimateDate'] = undefined;

/**
 * Tax in cents.
 * @member {Number} tax
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['tax'] = undefined;

/**
 * Transit time. For instance, \"three business days\" is represented as `3bd`.
 * @member {String} transitTime
 */
CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.prototype['transitTime'] = undefined;






export default CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner;

