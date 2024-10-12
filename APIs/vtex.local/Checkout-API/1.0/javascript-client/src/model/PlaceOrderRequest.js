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
import AddMerchantContextDataRequestSalesAssociateData from './AddMerchantContextDataRequestSalesAssociateData';
import PlaceOrderRequestClientProfileData from './PlaceOrderRequestClientProfileData';
import PlaceOrderRequestItemsInner from './PlaceOrderRequestItemsInner';
import PlaceOrderRequestMarketingData from './PlaceOrderRequestMarketingData';
import PlaceOrderRequestPaymentData from './PlaceOrderRequestPaymentData';
import PlaceOrderRequestShippingData from './PlaceOrderRequestShippingData';

/**
 * The PlaceOrderRequest model module.
 * @module model/PlaceOrderRequest
 * @version 1.0
 */
class PlaceOrderRequest {
    /**
     * Constructs a new <code>PlaceOrderRequest</code>.
     * @alias module:model/PlaceOrderRequest
     * @param clientProfileData {module:model/PlaceOrderRequestClientProfileData} 
     * @param items {Array.<module:model/PlaceOrderRequestItemsInner>} Array of objects containing information on each of the order's items.
     * @param paymentData {module:model/PlaceOrderRequestPaymentData} 
     * @param shippingData {module:model/PlaceOrderRequestShippingData} 
     */
    constructor(clientProfileData, items, paymentData, shippingData) { 
        
        PlaceOrderRequest.initialize(this, clientProfileData, items, paymentData, shippingData);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, clientProfileData, items, paymentData, shippingData) { 
        obj['clientProfileData'] = clientProfileData;
        obj['items'] = items;
        obj['openTextField'] = 'open-text-example';
        obj['paymentData'] = paymentData;
        obj['shippingData'] = shippingData;
    }

    /**
     * Constructs a <code>PlaceOrderRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlaceOrderRequest} obj Optional instance to populate.
     * @return {module:model/PlaceOrderRequest} The populated <code>PlaceOrderRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlaceOrderRequest();

            if (data.hasOwnProperty('clientProfileData')) {
                obj['clientProfileData'] = PlaceOrderRequestClientProfileData.constructFromObject(data['clientProfileData']);
            }
            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [PlaceOrderRequestItemsInner]);
            }
            if (data.hasOwnProperty('marketingData')) {
                obj['marketingData'] = PlaceOrderRequestMarketingData.constructFromObject(data['marketingData']);
            }
            if (data.hasOwnProperty('openTextField')) {
                obj['openTextField'] = ApiClient.convertToType(data['openTextField'], 'String');
            }
            if (data.hasOwnProperty('paymentData')) {
                obj['paymentData'] = PlaceOrderRequestPaymentData.constructFromObject(data['paymentData']);
            }
            if (data.hasOwnProperty('salesAssociateData')) {
                obj['salesAssociateData'] = AddMerchantContextDataRequestSalesAssociateData.constructFromObject(data['salesAssociateData']);
            }
            if (data.hasOwnProperty('shippingData')) {
                obj['shippingData'] = PlaceOrderRequestShippingData.constructFromObject(data['shippingData']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlaceOrderRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlaceOrderRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PlaceOrderRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `clientProfileData`
        if (data['clientProfileData']) { // data not null
          PlaceOrderRequestClientProfileData.validateJSON(data['clientProfileData']);
        }
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                PlaceOrderRequestItemsInner.validateJSON(item);
            };
        }
        // validate the optional field `marketingData`
        if (data['marketingData']) { // data not null
          PlaceOrderRequestMarketingData.validateJSON(data['marketingData']);
        }
        // ensure the json data is a string
        if (data['openTextField'] && !(typeof data['openTextField'] === 'string' || data['openTextField'] instanceof String)) {
            throw new Error("Expected the field `openTextField` to be a primitive type in the JSON string but got " + data['openTextField']);
        }
        // validate the optional field `paymentData`
        if (data['paymentData']) { // data not null
          PlaceOrderRequestPaymentData.validateJSON(data['paymentData']);
        }
        // validate the optional field `salesAssociateData`
        if (data['salesAssociateData']) { // data not null
          AddMerchantContextDataRequestSalesAssociateData.validateJSON(data['salesAssociateData']);
        }
        // validate the optional field `shippingData`
        if (data['shippingData']) { // data not null
          PlaceOrderRequestShippingData.validateJSON(data['shippingData']);
        }

        return true;
    }


}

PlaceOrderRequest.RequiredProperties = ["clientProfileData", "items", "paymentData", "shippingData"];

/**
 * @member {module:model/PlaceOrderRequestClientProfileData} clientProfileData
 */
PlaceOrderRequest.prototype['clientProfileData'] = undefined;

/**
 * Array of objects containing information on each of the order's items.
 * @member {Array.<module:model/PlaceOrderRequestItemsInner>} items
 */
PlaceOrderRequest.prototype['items'] = undefined;

/**
 * @member {module:model/PlaceOrderRequestMarketingData} marketingData
 */
PlaceOrderRequest.prototype['marketingData'] = undefined;

/**
 * Optional field meant to hold additional information about the order. We recommend using this field for text, not data formats such as `JSON` even if escaped. For that purpose, see [Creating customizable fields](https://developers.vtex.com/vtex-rest-api/docs/creating-customizable-fields-in-the-cart-with-checkout-api-1)
 * @member {String} openTextField
 * @default 'open-text-example'
 */
PlaceOrderRequest.prototype['openTextField'] = 'open-text-example';

/**
 * @member {module:model/PlaceOrderRequestPaymentData} paymentData
 */
PlaceOrderRequest.prototype['paymentData'] = undefined;

/**
 * @member {module:model/AddMerchantContextDataRequestSalesAssociateData} salesAssociateData
 */
PlaceOrderRequest.prototype['salesAssociateData'] = undefined;

/**
 * @member {module:model/PlaceOrderRequestShippingData} shippingData
 */
PlaceOrderRequest.prototype['shippingData'] = undefined;






export default PlaceOrderRequest;

