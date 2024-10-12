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

/**
 * The PlaceOrderFromExistingOrderFormRequest model module.
 * @module model/PlaceOrderFromExistingOrderFormRequest
 * @version 1.0
 */
class PlaceOrderFromExistingOrderFormRequest {
    /**
     * Constructs a new <code>PlaceOrderFromExistingOrderFormRequest</code>.
     * @alias module:model/PlaceOrderFromExistingOrderFormRequest
     * @param interestValue {Number} Interest rate to be used in case it applies.
     * @param referenceId {String} ID of the `orderForm` corresponding to the cart from which to place the order. This is the same as the `orderFormId` parameter.
     * @param referenceValue {Number} Reference value of the order for calculating interest if that is the case. Can be equal to the total value and does not separate cents. For example, $24.99 is represented `2499`.
     * @param value {Number} Total value of the order without separating cents. For example, $24.99 is represented `2499`.
     */
    constructor(interestValue, referenceId, referenceValue, value) { 
        
        PlaceOrderFromExistingOrderFormRequest.initialize(this, interestValue, referenceId, referenceValue, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, interestValue, referenceId, referenceValue, value) { 
        obj['interestValue'] = interestValue || 0;
        obj['optinNewsLetter'] = false;
        obj['referenceId'] = referenceId || '41a22925298a4ddca95318131a25b000';
        obj['referenceValue'] = referenceValue || 6800;
        obj['savePersonalData'] = false;
        obj['value'] = value || 6800;
    }

    /**
     * Constructs a <code>PlaceOrderFromExistingOrderFormRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlaceOrderFromExistingOrderFormRequest} obj Optional instance to populate.
     * @return {module:model/PlaceOrderFromExistingOrderFormRequest} The populated <code>PlaceOrderFromExistingOrderFormRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlaceOrderFromExistingOrderFormRequest();

            if (data.hasOwnProperty('interestValue')) {
                obj['interestValue'] = ApiClient.convertToType(data['interestValue'], 'Number');
            }
            if (data.hasOwnProperty('optinNewsLetter')) {
                obj['optinNewsLetter'] = ApiClient.convertToType(data['optinNewsLetter'], 'Boolean');
            }
            if (data.hasOwnProperty('referenceId')) {
                obj['referenceId'] = ApiClient.convertToType(data['referenceId'], 'String');
            }
            if (data.hasOwnProperty('referenceValue')) {
                obj['referenceValue'] = ApiClient.convertToType(data['referenceValue'], 'Number');
            }
            if (data.hasOwnProperty('savePersonalData')) {
                obj['savePersonalData'] = ApiClient.convertToType(data['savePersonalData'], 'Boolean');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlaceOrderFromExistingOrderFormRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlaceOrderFromExistingOrderFormRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PlaceOrderFromExistingOrderFormRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['referenceId'] && !(typeof data['referenceId'] === 'string' || data['referenceId'] instanceof String)) {
            throw new Error("Expected the field `referenceId` to be a primitive type in the JSON string but got " + data['referenceId']);
        }

        return true;
    }


}

PlaceOrderFromExistingOrderFormRequest.RequiredProperties = ["interestValue", "referenceId", "referenceValue", "value"];

/**
 * Interest rate to be used in case it applies.
 * @member {Number} interestValue
 * @default 0
 */
PlaceOrderFromExistingOrderFormRequest.prototype['interestValue'] = 0;

/**
 * True if the shopper opted to receive the newsletter.
 * @member {Boolean} optinNewsLetter
 * @default false
 */
PlaceOrderFromExistingOrderFormRequest.prototype['optinNewsLetter'] = false;

/**
 * ID of the `orderForm` corresponding to the cart from which to place the order. This is the same as the `orderFormId` parameter.
 * @member {String} referenceId
 * @default '41a22925298a4ddca95318131a25b000'
 */
PlaceOrderFromExistingOrderFormRequest.prototype['referenceId'] = '41a22925298a4ddca95318131a25b000';

/**
 * Reference value of the order for calculating interest if that is the case. Can be equal to the total value and does not separate cents. For example, $24.99 is represented `2499`.
 * @member {Number} referenceValue
 * @default 6800
 */
PlaceOrderFromExistingOrderFormRequest.prototype['referenceValue'] = 6800;

/**
 * `true` if the shopper's data provided during checkout should be saved for future reference.
 * @member {Boolean} savePersonalData
 * @default false
 */
PlaceOrderFromExistingOrderFormRequest.prototype['savePersonalData'] = false;

/**
 * Total value of the order without separating cents. For example, $24.99 is represented `2499`.
 * @member {Number} value
 * @default 6800
 */
PlaceOrderFromExistingOrderFormRequest.prototype['value'] = 6800;






export default PlaceOrderFromExistingOrderFormRequest;

