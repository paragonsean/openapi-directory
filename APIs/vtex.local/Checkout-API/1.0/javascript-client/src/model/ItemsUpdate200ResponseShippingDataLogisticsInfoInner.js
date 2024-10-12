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
import AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner from './AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner';
import ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner from './ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner';

/**
 * The ItemsUpdate200ResponseShippingDataLogisticsInfoInner model module.
 * @module model/ItemsUpdate200ResponseShippingDataLogisticsInfoInner
 * @version 1.0
 */
class ItemsUpdate200ResponseShippingDataLogisticsInfoInner {
    /**
     * Constructs a new <code>ItemsUpdate200ResponseShippingDataLogisticsInfoInner</code>.
     * @alias module:model/ItemsUpdate200ResponseShippingDataLogisticsInfoInner
     */
    constructor() { 
        
        ItemsUpdate200ResponseShippingDataLogisticsInfoInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ItemsUpdate200ResponseShippingDataLogisticsInfoInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ItemsUpdate200ResponseShippingDataLogisticsInfoInner} obj Optional instance to populate.
     * @return {module:model/ItemsUpdate200ResponseShippingDataLogisticsInfoInner} The populated <code>ItemsUpdate200ResponseShippingDataLogisticsInfoInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ItemsUpdate200ResponseShippingDataLogisticsInfoInner();

            if (data.hasOwnProperty('addressId')) {
                obj['addressId'] = ApiClient.convertToType(data['addressId'], 'String');
            }
            if (data.hasOwnProperty('deliveryChannels')) {
                obj['deliveryChannels'] = ApiClient.convertToType(data['deliveryChannels'], [AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner]);
            }
            if (data.hasOwnProperty('itemId')) {
                obj['itemId'] = ApiClient.convertToType(data['itemId'], 'String');
            }
            if (data.hasOwnProperty('itemIndex')) {
                obj['itemIndex'] = ApiClient.convertToType(data['itemIndex'], 'Number');
            }
            if (data.hasOwnProperty('selectedDeliveryChannel')) {
                obj['selectedDeliveryChannel'] = ApiClient.convertToType(data['selectedDeliveryChannel'], 'String');
            }
            if (data.hasOwnProperty('selectedSla')) {
                obj['selectedSla'] = ApiClient.convertToType(data['selectedSla'], 'String');
            }
            if (data.hasOwnProperty('shipsTo')) {
                obj['shipsTo'] = ApiClient.convertToType(data['shipsTo'], ['String']);
            }
            if (data.hasOwnProperty('slas')) {
                obj['slas'] = ApiClient.convertToType(data['slas'], [ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ItemsUpdate200ResponseShippingDataLogisticsInfoInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ItemsUpdate200ResponseShippingDataLogisticsInfoInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['addressId'] && !(typeof data['addressId'] === 'string' || data['addressId'] instanceof String)) {
            throw new Error("Expected the field `addressId` to be a primitive type in the JSON string but got " + data['addressId']);
        }
        if (data['deliveryChannels']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['deliveryChannels'])) {
                throw new Error("Expected the field `deliveryChannels` to be an array in the JSON data but got " + data['deliveryChannels']);
            }
            // validate the optional field `deliveryChannels` (array)
            for (const item of data['deliveryChannels']) {
                AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['itemId'] && !(typeof data['itemId'] === 'string' || data['itemId'] instanceof String)) {
            throw new Error("Expected the field `itemId` to be a primitive type in the JSON string but got " + data['itemId']);
        }
        // ensure the json data is a string
        if (data['selectedDeliveryChannel'] && !(typeof data['selectedDeliveryChannel'] === 'string' || data['selectedDeliveryChannel'] instanceof String)) {
            throw new Error("Expected the field `selectedDeliveryChannel` to be a primitive type in the JSON string but got " + data['selectedDeliveryChannel']);
        }
        // ensure the json data is a string
        if (data['selectedSla'] && !(typeof data['selectedSla'] === 'string' || data['selectedSla'] instanceof String)) {
            throw new Error("Expected the field `selectedSla` to be a primitive type in the JSON string but got " + data['selectedSla']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['shipsTo'])) {
            throw new Error("Expected the field `shipsTo` to be an array in the JSON data but got " + data['shipsTo']);
        }
        if (data['slas']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['slas'])) {
                throw new Error("Expected the field `slas` to be an array in the JSON data but got " + data['slas']);
            }
            // validate the optional field `slas` (array)
            for (const item of data['slas']) {
                ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Address ID.
 * @member {String} addressId
 */
ItemsUpdate200ResponseShippingDataLogisticsInfoInner.prototype['addressId'] = undefined;

/**
 * List of available delivery channels.
 * @member {Array.<module:model/AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner>} deliveryChannels
 */
ItemsUpdate200ResponseShippingDataLogisticsInfoInner.prototype['deliveryChannels'] = undefined;

/**
 * Item ID.
 * @member {String} itemId
 */
ItemsUpdate200ResponseShippingDataLogisticsInfoInner.prototype['itemId'] = undefined;

/**
 * Index corresponding to the position of the object in the `items` array.
 * @member {Number} itemIndex
 */
ItemsUpdate200ResponseShippingDataLogisticsInfoInner.prototype['itemIndex'] = undefined;

/**
 * Delivery channel selected by the customer.
 * @member {String} selectedDeliveryChannel
 */
ItemsUpdate200ResponseShippingDataLogisticsInfoInner.prototype['selectedDeliveryChannel'] = undefined;

/**
 * SLA selected by the customer.
 * @member {String} selectedSla
 */
ItemsUpdate200ResponseShippingDataLogisticsInfoInner.prototype['selectedSla'] = undefined;

/**
 * List of countries that the item may be shipped to.
 * @member {Array.<String>} shipsTo
 */
ItemsUpdate200ResponseShippingDataLogisticsInfoInner.prototype['shipsTo'] = undefined;

/**
 * Information on available SLAs.
 * @member {Array.<module:model/ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner>} slas
 */
ItemsUpdate200ResponseShippingDataLogisticsInfoInner.prototype['slas'] = undefined;






export default ItemsUpdate200ResponseShippingDataLogisticsInfoInner;

