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
import PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow from './PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow';

/**
 * The PlaceOrderRequestShippingDataLogisticsInfoInner model module.
 * @module model/PlaceOrderRequestShippingDataLogisticsInfoInner
 * @version 1.0
 */
class PlaceOrderRequestShippingDataLogisticsInfoInner {
    /**
     * Constructs a new <code>PlaceOrderRequestShippingDataLogisticsInfoInner</code>.
     * @alias module:model/PlaceOrderRequestShippingDataLogisticsInfoInner
     * @param itemIndex {Number} Index of the item in the `items` array, starting from 0.
     * @param price {Number} Shipping price for the item. Does not account for the whole order's shipping price.
     * @param selectedSla {String} Selected shipping option
     */
    constructor(itemIndex, price, selectedSla) { 
        
        PlaceOrderRequestShippingDataLogisticsInfoInner.initialize(this, itemIndex, price, selectedSla);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, itemIndex, price, selectedSla) { 
        obj['itemIndex'] = itemIndex || 0;
        obj['lockTTL'] = '8d';
        obj['price'] = price || 1099;
        obj['selectedSla'] = selectedSla || 'Express';
        obj['shippingEstimate'] = '7d';
    }

    /**
     * Constructs a <code>PlaceOrderRequestShippingDataLogisticsInfoInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlaceOrderRequestShippingDataLogisticsInfoInner} obj Optional instance to populate.
     * @return {module:model/PlaceOrderRequestShippingDataLogisticsInfoInner} The populated <code>PlaceOrderRequestShippingDataLogisticsInfoInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlaceOrderRequestShippingDataLogisticsInfoInner();

            if (data.hasOwnProperty('deliveryWindow')) {
                obj['deliveryWindow'] = PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow.constructFromObject(data['deliveryWindow']);
            }
            if (data.hasOwnProperty('itemIndex')) {
                obj['itemIndex'] = ApiClient.convertToType(data['itemIndex'], 'Number');
            }
            if (data.hasOwnProperty('lockTTL')) {
                obj['lockTTL'] = ApiClient.convertToType(data['lockTTL'], 'String');
            }
            if (data.hasOwnProperty('price')) {
                obj['price'] = ApiClient.convertToType(data['price'], 'Number');
            }
            if (data.hasOwnProperty('selectedSla')) {
                obj['selectedSla'] = ApiClient.convertToType(data['selectedSla'], 'String');
            }
            if (data.hasOwnProperty('shippingEstimate')) {
                obj['shippingEstimate'] = ApiClient.convertToType(data['shippingEstimate'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlaceOrderRequestShippingDataLogisticsInfoInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlaceOrderRequestShippingDataLogisticsInfoInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PlaceOrderRequestShippingDataLogisticsInfoInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `deliveryWindow`
        if (data['deliveryWindow']) { // data not null
          PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow.validateJSON(data['deliveryWindow']);
        }
        // ensure the json data is a string
        if (data['lockTTL'] && !(typeof data['lockTTL'] === 'string' || data['lockTTL'] instanceof String)) {
            throw new Error("Expected the field `lockTTL` to be a primitive type in the JSON string but got " + data['lockTTL']);
        }
        // ensure the json data is a string
        if (data['selectedSla'] && !(typeof data['selectedSla'] === 'string' || data['selectedSla'] instanceof String)) {
            throw new Error("Expected the field `selectedSla` to be a primitive type in the JSON string but got " + data['selectedSla']);
        }
        // ensure the json data is a string
        if (data['shippingEstimate'] && !(typeof data['shippingEstimate'] === 'string' || data['shippingEstimate'] instanceof String)) {
            throw new Error("Expected the field `shippingEstimate` to be a primitive type in the JSON string but got " + data['shippingEstimate']);
        }

        return true;
    }


}

PlaceOrderRequestShippingDataLogisticsInfoInner.RequiredProperties = ["itemIndex", "price", "selectedSla"];

/**
 * @member {module:model/PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow} deliveryWindow
 */
PlaceOrderRequestShippingDataLogisticsInfoInner.prototype['deliveryWindow'] = undefined;

/**
 * Index of the item in the `items` array, starting from 0.
 * @member {Number} itemIndex
 * @default 0
 */
PlaceOrderRequestShippingDataLogisticsInfoInner.prototype['itemIndex'] = 0;

/**
 * Logistics reservation waiting time.
 * @member {String} lockTTL
 * @default '8d'
 */
PlaceOrderRequestShippingDataLogisticsInfoInner.prototype['lockTTL'] = '8d';

/**
 * Shipping price for the item. Does not account for the whole order's shipping price.
 * @member {Number} price
 * @default 1099
 */
PlaceOrderRequestShippingDataLogisticsInfoInner.prototype['price'] = 1099;

/**
 * Selected shipping option
 * @member {String} selectedSla
 * @default 'Express'
 */
PlaceOrderRequestShippingDataLogisticsInfoInner.prototype['selectedSla'] = 'Express';

/**
 * Estimated time until delivery for the item.
 * @member {String} shippingEstimate
 * @default '7d'
 */
PlaceOrderRequestShippingDataLogisticsInfoInner.prototype['shippingEstimate'] = '7d';






export default PlaceOrderRequestShippingDataLogisticsInfoInner;

