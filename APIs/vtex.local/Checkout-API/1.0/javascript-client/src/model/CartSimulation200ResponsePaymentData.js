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
import CartSimulation200ResponsePaymentDataPaymentSystemsInner from './CartSimulation200ResponsePaymentDataPaymentSystemsInner';

/**
 * The CartSimulation200ResponsePaymentData model module.
 * @module model/CartSimulation200ResponsePaymentData
 * @version 1.0
 */
class CartSimulation200ResponsePaymentData {
    /**
     * Constructs a new <code>CartSimulation200ResponsePaymentData</code>.
     * Payment data information.
     * @alias module:model/CartSimulation200ResponsePaymentData
     */
    constructor() { 
        
        CartSimulation200ResponsePaymentData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CartSimulation200ResponsePaymentData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CartSimulation200ResponsePaymentData} obj Optional instance to populate.
     * @return {module:model/CartSimulation200ResponsePaymentData} The populated <code>CartSimulation200ResponsePaymentData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CartSimulation200ResponsePaymentData();

            if (data.hasOwnProperty('availableAccounts')) {
                obj['availableAccounts'] = ApiClient.convertToType(data['availableAccounts'], [Object]);
            }
            if (data.hasOwnProperty('availableAssociations')) {
                obj['availableAssociations'] = ApiClient.convertToType(data['availableAssociations'], Object);
            }
            if (data.hasOwnProperty('availableTokens')) {
                obj['availableTokens'] = ApiClient.convertToType(data['availableTokens'], [Object]);
            }
            if (data.hasOwnProperty('giftCardMessages')) {
                obj['giftCardMessages'] = ApiClient.convertToType(data['giftCardMessages'], [Object]);
            }
            if (data.hasOwnProperty('giftCards')) {
                obj['giftCards'] = ApiClient.convertToType(data['giftCards'], [Object]);
            }
            if (data.hasOwnProperty('installmentOptions')) {
                obj['installmentOptions'] = ApiClient.convertToType(data['installmentOptions'], [Object]);
            }
            if (data.hasOwnProperty('paymentSystems')) {
                obj['paymentSystems'] = ApiClient.convertToType(data['paymentSystems'], [CartSimulation200ResponsePaymentDataPaymentSystemsInner]);
            }
            if (data.hasOwnProperty('payments')) {
                obj['payments'] = ApiClient.convertToType(data['payments'], [Object]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CartSimulation200ResponsePaymentData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CartSimulation200ResponsePaymentData</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['availableAccounts'])) {
            throw new Error("Expected the field `availableAccounts` to be an array in the JSON data but got " + data['availableAccounts']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['availableTokens'])) {
            throw new Error("Expected the field `availableTokens` to be an array in the JSON data but got " + data['availableTokens']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['giftCardMessages'])) {
            throw new Error("Expected the field `giftCardMessages` to be an array in the JSON data but got " + data['giftCardMessages']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['giftCards'])) {
            throw new Error("Expected the field `giftCards` to be an array in the JSON data but got " + data['giftCards']);
        }
        if (data['paymentSystems']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['paymentSystems'])) {
                throw new Error("Expected the field `paymentSystems` to be an array in the JSON data but got " + data['paymentSystems']);
            }
            // validate the optional field `paymentSystems` (array)
            for (const item of data['paymentSystems']) {
                CartSimulation200ResponsePaymentDataPaymentSystemsInner.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['payments'])) {
            throw new Error("Expected the field `payments` to be an array in the JSON data but got " + data['payments']);
        }

        return true;
    }


}



/**
 * Available accounts.
 * @member {Array.<Object>} availableAccounts
 */
CartSimulation200ResponsePaymentData.prototype['availableAccounts'] = undefined;

/**
 * Available associations.
 * @member {Object} availableAssociations
 */
CartSimulation200ResponsePaymentData.prototype['availableAssociations'] = undefined;

/**
 * Available tokens.
 * @member {Array.<Object>} availableTokens
 */
CartSimulation200ResponsePaymentData.prototype['availableTokens'] = undefined;

/**
 * Array of gift card messages.
 * @member {Array.<Object>} giftCardMessages
 */
CartSimulation200ResponsePaymentData.prototype['giftCardMessages'] = undefined;

/**
 * Gift card information, if it applies to the order.
 * @member {Array.<Object>} giftCards
 */
CartSimulation200ResponsePaymentData.prototype['giftCards'] = undefined;

/**
 * Installment options information.
 * @member {Array.<Object>} installmentOptions
 */
CartSimulation200ResponsePaymentData.prototype['installmentOptions'] = undefined;

/**
 * Information on payment systems.
 * @member {Array.<module:model/CartSimulation200ResponsePaymentDataPaymentSystemsInner>} paymentSystems
 */
CartSimulation200ResponsePaymentData.prototype['paymentSystems'] = undefined;

/**
 * Information on each payment.
 * @member {Array.<Object>} payments
 */
CartSimulation200ResponsePaymentData.prototype['payments'] = undefined;






export default CartSimulation200ResponsePaymentData;

