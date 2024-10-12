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
import PlaceOrderRequestItemsInnerBundleItemsInner from './PlaceOrderRequestItemsInnerBundleItemsInner';
import PlaceOrderRequestItemsInnerItemAttachment from './PlaceOrderRequestItemsInnerItemAttachment';
import PlaceOrderRequestItemsInnerPriceTagsInner from './PlaceOrderRequestItemsInnerPriceTagsInner';

/**
 * The PlaceOrderRequestItemsInner model module.
 * @module model/PlaceOrderRequestItemsInner
 * @version 1.0
 */
class PlaceOrderRequestItemsInner {
    /**
     * Constructs a new <code>PlaceOrderRequestItemsInner</code>.
     * @alias module:model/PlaceOrderRequestItemsInner
     * @param id {String} The SKU ID.
     * @param quantity {Number} The quantity of items of this specific SKU in the cart to be simulated.
     * @param seller {String} The ID of the seller responsible for this SKU. This ID can be found in your VTEX Admin.
     */
    constructor(id, quantity, seller) { 
        
        PlaceOrderRequestItemsInner.initialize(this, id, quantity, seller);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id, quantity, seller) { 
        obj['id'] = id;
        obj['isGift'] = false;
        obj['measurementUnit'] = 'g';
        obj['quantity'] = quantity;
        obj['seller'] = seller;
        obj['unitMultiplier'] = 1;
    }

    /**
     * Constructs a <code>PlaceOrderRequestItemsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlaceOrderRequestItemsInner} obj Optional instance to populate.
     * @return {module:model/PlaceOrderRequestItemsInner} The populated <code>PlaceOrderRequestItemsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlaceOrderRequestItemsInner();

            if (data.hasOwnProperty('attachments')) {
                obj['attachments'] = ApiClient.convertToType(data['attachments'], ['String']);
            }
            if (data.hasOwnProperty('bundleItems')) {
                obj['bundleItems'] = ApiClient.convertToType(data['bundleItems'], [PlaceOrderRequestItemsInnerBundleItemsInner]);
            }
            if (data.hasOwnProperty('commission')) {
                obj['commission'] = ApiClient.convertToType(data['commission'], 'Number');
            }
            if (data.hasOwnProperty('freightCommission')) {
                obj['freightCommission'] = ApiClient.convertToType(data['freightCommission'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('isGift')) {
                obj['isGift'] = ApiClient.convertToType(data['isGift'], 'Boolean');
            }
            if (data.hasOwnProperty('itemAttachment')) {
                obj['itemAttachment'] = PlaceOrderRequestItemsInnerItemAttachment.constructFromObject(data['itemAttachment']);
            }
            if (data.hasOwnProperty('measurementUnit')) {
                obj['measurementUnit'] = ApiClient.convertToType(data['measurementUnit'], 'String');
            }
            if (data.hasOwnProperty('price')) {
                obj['price'] = ApiClient.convertToType(data['price'], 'Number');
            }
            if (data.hasOwnProperty('priceTags')) {
                obj['priceTags'] = ApiClient.convertToType(data['priceTags'], [PlaceOrderRequestItemsInnerPriceTagsInner]);
            }
            if (data.hasOwnProperty('quantity')) {
                obj['quantity'] = ApiClient.convertToType(data['quantity'], 'Number');
            }
            if (data.hasOwnProperty('seller')) {
                obj['seller'] = ApiClient.convertToType(data['seller'], 'String');
            }
            if (data.hasOwnProperty('unitMultiplier')) {
                obj['unitMultiplier'] = ApiClient.convertToType(data['unitMultiplier'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlaceOrderRequestItemsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlaceOrderRequestItemsInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PlaceOrderRequestItemsInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['attachments'])) {
            throw new Error("Expected the field `attachments` to be an array in the JSON data but got " + data['attachments']);
        }
        if (data['bundleItems']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['bundleItems'])) {
                throw new Error("Expected the field `bundleItems` to be an array in the JSON data but got " + data['bundleItems']);
            }
            // validate the optional field `bundleItems` (array)
            for (const item of data['bundleItems']) {
                PlaceOrderRequestItemsInnerBundleItemsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `itemAttachment`
        if (data['itemAttachment']) { // data not null
          PlaceOrderRequestItemsInnerItemAttachment.validateJSON(data['itemAttachment']);
        }
        // ensure the json data is a string
        if (data['measurementUnit'] && !(typeof data['measurementUnit'] === 'string' || data['measurementUnit'] instanceof String)) {
            throw new Error("Expected the field `measurementUnit` to be a primitive type in the JSON string but got " + data['measurementUnit']);
        }
        if (data['priceTags']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['priceTags'])) {
                throw new Error("Expected the field `priceTags` to be an array in the JSON data but got " + data['priceTags']);
            }
            // validate the optional field `priceTags` (array)
            for (const item of data['priceTags']) {
                PlaceOrderRequestItemsInnerPriceTagsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['seller'] && !(typeof data['seller'] === 'string' || data['seller'] instanceof String)) {
            throw new Error("Expected the field `seller` to be a primitive type in the JSON string but got " + data['seller']);
        }

        return true;
    }


}

PlaceOrderRequestItemsInner.RequiredProperties = ["id", "quantity", "seller"];

/**
 * Array containing information on attachments.
 * @member {Array.<String>} attachments
 */
PlaceOrderRequestItemsInner.prototype['attachments'] = undefined;

/**
 * Information on services sold along with the SKU. Example: a gift package.
 * @member {Array.<module:model/PlaceOrderRequestItemsInnerBundleItemsInner>} bundleItems
 */
PlaceOrderRequestItemsInner.prototype['bundleItems'] = undefined;

/**
 * Comission.
 * @member {Number} commission
 */
PlaceOrderRequestItemsInner.prototype['commission'] = undefined;

/**
 * Freight comission
 * @member {Number} freightCommission
 */
PlaceOrderRequestItemsInner.prototype['freightCommission'] = undefined;

/**
 * The SKU ID.
 * @member {String} id
 */
PlaceOrderRequestItemsInner.prototype['id'] = undefined;

/**
 * Indicates whether the order is a gift.
 * @member {Boolean} isGift
 * @default false
 */
PlaceOrderRequestItemsInner.prototype['isGift'] = false;

/**
 * @member {module:model/PlaceOrderRequestItemsInnerItemAttachment} itemAttachment
 */
PlaceOrderRequestItemsInner.prototype['itemAttachment'] = undefined;

/**
 * SKU measurement unit.
 * @member {String} measurementUnit
 * @default 'g'
 */
PlaceOrderRequestItemsInner.prototype['measurementUnit'] = 'g';

/**
 * Item price within the context of the order without separating cents. For example, $24.99 is represented `2499`.
 * @member {Number} price
 */
PlaceOrderRequestItemsInner.prototype['price'] = undefined;

/**
 * Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order.
 * @member {Array.<module:model/PlaceOrderRequestItemsInnerPriceTagsInner>} priceTags
 */
PlaceOrderRequestItemsInner.prototype['priceTags'] = undefined;

/**
 * The quantity of items of this specific SKU in the cart to be simulated.
 * @member {Number} quantity
 */
PlaceOrderRequestItemsInner.prototype['quantity'] = undefined;

/**
 * The ID of the seller responsible for this SKU. This ID can be found in your VTEX Admin.
 * @member {String} seller
 */
PlaceOrderRequestItemsInner.prototype['seller'] = undefined;

/**
 * SKU unit multiplier.
 * @member {Number} unitMultiplier
 * @default 1
 */
PlaceOrderRequestItemsInner.prototype['unitMultiplier'] = 1;






export default PlaceOrderRequestItemsInner;

