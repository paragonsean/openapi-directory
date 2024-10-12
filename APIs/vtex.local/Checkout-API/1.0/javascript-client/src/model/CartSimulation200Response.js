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
import CartSimulation200ResponseItemsInner from './CartSimulation200ResponseItemsInner';
import CartSimulation200ResponseLogisticsInfoInner from './CartSimulation200ResponseLogisticsInfoInner';
import CartSimulation200ResponsePaymentData from './CartSimulation200ResponsePaymentData';
import CartSimulation200ResponseRatesAndBenefitsData from './CartSimulation200ResponseRatesAndBenefitsData';

/**
 * The CartSimulation200Response model module.
 * @module model/CartSimulation200Response
 * @version 1.0
 */
class CartSimulation200Response {
    /**
     * Constructs a new <code>CartSimulation200Response</code>.
     * @alias module:model/CartSimulation200Response
     */
    constructor() { 
        
        CartSimulation200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CartSimulation200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CartSimulation200Response} obj Optional instance to populate.
     * @return {module:model/CartSimulation200Response} The populated <code>CartSimulation200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CartSimulation200Response();

            if (data.hasOwnProperty('country')) {
                obj['country'] = ApiClient.convertToType(data['country'], 'String');
            }
            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [CartSimulation200ResponseItemsInner]);
            }
            if (data.hasOwnProperty('logisticsInfo')) {
                obj['logisticsInfo'] = ApiClient.convertToType(data['logisticsInfo'], [CartSimulation200ResponseLogisticsInfoInner]);
            }
            if (data.hasOwnProperty('marketingData')) {
                obj['marketingData'] = ApiClient.convertToType(data['marketingData'], Object);
            }
            if (data.hasOwnProperty('paymentData')) {
                obj['paymentData'] = CartSimulation200ResponsePaymentData.constructFromObject(data['paymentData']);
            }
            if (data.hasOwnProperty('postalCode')) {
                obj['postalCode'] = ApiClient.convertToType(data['postalCode'], 'String');
            }
            if (data.hasOwnProperty('ratesAndBenefitsData')) {
                obj['ratesAndBenefitsData'] = CartSimulation200ResponseRatesAndBenefitsData.constructFromObject(data['ratesAndBenefitsData']);
            }
            if (data.hasOwnProperty('selectableGifts')) {
                obj['selectableGifts'] = ApiClient.convertToType(data['selectableGifts'], [Object]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CartSimulation200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CartSimulation200Response</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['country'] && !(typeof data['country'] === 'string' || data['country'] instanceof String)) {
            throw new Error("Expected the field `country` to be a primitive type in the JSON string but got " + data['country']);
        }
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                CartSimulation200ResponseItemsInner.validateJSON(item);
            };
        }
        if (data['logisticsInfo']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['logisticsInfo'])) {
                throw new Error("Expected the field `logisticsInfo` to be an array in the JSON data but got " + data['logisticsInfo']);
            }
            // validate the optional field `logisticsInfo` (array)
            for (const item of data['logisticsInfo']) {
                CartSimulation200ResponseLogisticsInfoInner.validateJSON(item);
            };
        }
        // validate the optional field `paymentData`
        if (data['paymentData']) { // data not null
          CartSimulation200ResponsePaymentData.validateJSON(data['paymentData']);
        }
        // ensure the json data is a string
        if (data['postalCode'] && !(typeof data['postalCode'] === 'string' || data['postalCode'] instanceof String)) {
            throw new Error("Expected the field `postalCode` to be a primitive type in the JSON string but got " + data['postalCode']);
        }
        // validate the optional field `ratesAndBenefitsData`
        if (data['ratesAndBenefitsData']) { // data not null
          CartSimulation200ResponseRatesAndBenefitsData.validateJSON(data['ratesAndBenefitsData']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['selectableGifts'])) {
            throw new Error("Expected the field `selectableGifts` to be an array in the JSON data but got " + data['selectableGifts']);
        }

        return true;
    }


}



/**
 * Three letter ISO code of the country of the shipping address.
 * @member {String} country
 */
CartSimulation200Response.prototype['country'] = undefined;

/**
 * Information on each item in the cart.
 * @member {Array.<module:model/CartSimulation200ResponseItemsInner>} items
 */
CartSimulation200Response.prototype['items'] = undefined;

/**
 * Array with logistics information on each item of the `items` array in the `orderForm`.
 * @member {Array.<module:model/CartSimulation200ResponseLogisticsInfoInner>} logisticsInfo
 */
CartSimulation200Response.prototype['logisticsInfo'] = undefined;

/**
 * Object containing promotion data such as coupon tracking information and internal or external UTMs.
 * @member {Object} marketingData
 */
CartSimulation200Response.prototype['marketingData'] = undefined;

/**
 * @member {module:model/CartSimulation200ResponsePaymentData} paymentData
 */
CartSimulation200Response.prototype['paymentData'] = undefined;

/**
 * Postal Code.
 * @member {String} postalCode
 */
CartSimulation200Response.prototype['postalCode'] = undefined;

/**
 * @member {module:model/CartSimulation200ResponseRatesAndBenefitsData} ratesAndBenefitsData
 */
CartSimulation200Response.prototype['ratesAndBenefitsData'] = undefined;

/**
 * Array containing the data of the item selected as a gift.
 * @member {Array.<Object>} selectableGifts
 */
CartSimulation200Response.prototype['selectableGifts'] = undefined;






export default CartSimulation200Response;

