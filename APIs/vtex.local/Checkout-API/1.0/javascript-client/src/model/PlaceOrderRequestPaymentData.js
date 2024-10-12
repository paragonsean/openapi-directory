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
import PlaceOrderRequestPaymentDataGiftCardsInner from './PlaceOrderRequestPaymentDataGiftCardsInner';
import PlaceOrderRequestPaymentDataPaymentSystemsInner from './PlaceOrderRequestPaymentDataPaymentSystemsInner';
import PlaceOrderRequestPaymentDataPaymentsInner from './PlaceOrderRequestPaymentDataPaymentsInner';

/**
 * The PlaceOrderRequestPaymentData model module.
 * @module model/PlaceOrderRequestPaymentData
 * @version 1.0
 */
class PlaceOrderRequestPaymentData {
    /**
     * Constructs a new <code>PlaceOrderRequestPaymentData</code>.
     * Payment infomation.
     * @alias module:model/PlaceOrderRequestPaymentData
     * @param payments {Array.<module:model/PlaceOrderRequestPaymentDataPaymentsInner>} Payment information.
     */
    constructor(payments) { 
        
        PlaceOrderRequestPaymentData.initialize(this, payments);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, payments) { 
        obj['payments'] = payments;
        obj['updateStatus'] = 'updated';
    }

    /**
     * Constructs a <code>PlaceOrderRequestPaymentData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlaceOrderRequestPaymentData} obj Optional instance to populate.
     * @return {module:model/PlaceOrderRequestPaymentData} The populated <code>PlaceOrderRequestPaymentData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlaceOrderRequestPaymentData();

            if (data.hasOwnProperty('giftCardMessages')) {
                obj['giftCardMessages'] = ApiClient.convertToType(data['giftCardMessages'], [Object]);
            }
            if (data.hasOwnProperty('giftCards')) {
                obj['giftCards'] = ApiClient.convertToType(data['giftCards'], [PlaceOrderRequestPaymentDataGiftCardsInner]);
            }
            if (data.hasOwnProperty('paymentSystems')) {
                obj['paymentSystems'] = ApiClient.convertToType(data['paymentSystems'], [PlaceOrderRequestPaymentDataPaymentSystemsInner]);
            }
            if (data.hasOwnProperty('payments')) {
                obj['payments'] = ApiClient.convertToType(data['payments'], [PlaceOrderRequestPaymentDataPaymentsInner]);
            }
            if (data.hasOwnProperty('updateStatus')) {
                obj['updateStatus'] = ApiClient.convertToType(data['updateStatus'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlaceOrderRequestPaymentData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlaceOrderRequestPaymentData</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PlaceOrderRequestPaymentData.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['giftCardMessages'])) {
            throw new Error("Expected the field `giftCardMessages` to be an array in the JSON data but got " + data['giftCardMessages']);
        }
        if (data['giftCards']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['giftCards'])) {
                throw new Error("Expected the field `giftCards` to be an array in the JSON data but got " + data['giftCards']);
            }
            // validate the optional field `giftCards` (array)
            for (const item of data['giftCards']) {
                PlaceOrderRequestPaymentDataGiftCardsInner.validateJSON(item);
            };
        }
        if (data['paymentSystems']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['paymentSystems'])) {
                throw new Error("Expected the field `paymentSystems` to be an array in the JSON data but got " + data['paymentSystems']);
            }
            // validate the optional field `paymentSystems` (array)
            for (const item of data['paymentSystems']) {
                PlaceOrderRequestPaymentDataPaymentSystemsInner.validateJSON(item);
            };
        }
        if (data['payments']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['payments'])) {
                throw new Error("Expected the field `payments` to be an array in the JSON data but got " + data['payments']);
            }
            // validate the optional field `payments` (array)
            for (const item of data['payments']) {
                PlaceOrderRequestPaymentDataPaymentsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['updateStatus'] && !(typeof data['updateStatus'] === 'string' || data['updateStatus'] instanceof String)) {
            throw new Error("Expected the field `updateStatus` to be a primitive type in the JSON string but got " + data['updateStatus']);
        }

        return true;
    }


}

PlaceOrderRequestPaymentData.RequiredProperties = ["payments"];

/**
 * Array of gift card messages.
 * @member {Array.<Object>} giftCardMessages
 */
PlaceOrderRequestPaymentData.prototype['giftCardMessages'] = undefined;

/**
 * Gift card information, if it applies to the order.
 * @member {Array.<module:model/PlaceOrderRequestPaymentDataGiftCardsInner>} giftCards
 */
PlaceOrderRequestPaymentData.prototype['giftCards'] = undefined;

/**
 * Information on payment systems.
 * @member {Array.<module:model/PlaceOrderRequestPaymentDataPaymentSystemsInner>} paymentSystems
 */
PlaceOrderRequestPaymentData.prototype['paymentSystems'] = undefined;

/**
 * Payment information.
 * @member {Array.<module:model/PlaceOrderRequestPaymentDataPaymentsInner>} payments
 */
PlaceOrderRequestPaymentData.prototype['payments'] = undefined;

/**
 * Indicates whether this object's information is up to date according to the order's items. An order can not be placed if `\"outdated\"`
 * @member {String} updateStatus
 * @default 'updated'
 */
PlaceOrderRequestPaymentData.prototype['updateStatus'] = 'updated';






export default PlaceOrderRequestPaymentData;

