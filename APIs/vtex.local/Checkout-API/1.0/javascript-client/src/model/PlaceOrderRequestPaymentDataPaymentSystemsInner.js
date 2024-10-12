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
import PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator from './PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator';

/**
 * The PlaceOrderRequestPaymentDataPaymentSystemsInner model module.
 * @module model/PlaceOrderRequestPaymentDataPaymentSystemsInner
 * @version 1.0
 */
class PlaceOrderRequestPaymentDataPaymentSystemsInner {
    /**
     * Constructs a new <code>PlaceOrderRequestPaymentDataPaymentSystemsInner</code>.
     * @alias module:model/PlaceOrderRequestPaymentDataPaymentSystemsInner
     */
    constructor() { 
        
        PlaceOrderRequestPaymentDataPaymentSystemsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['description'] = 'description-example';
        obj['isCustom'] = false;
        obj['requiresDocument'] = false;
        obj['selected'] = false;
        obj['stringId'] = '12345abc';
        obj['template'] = 'creditCardPaymentGroup-template';
    }

    /**
     * Constructs a <code>PlaceOrderRequestPaymentDataPaymentSystemsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlaceOrderRequestPaymentDataPaymentSystemsInner} obj Optional instance to populate.
     * @return {module:model/PlaceOrderRequestPaymentDataPaymentSystemsInner} The populated <code>PlaceOrderRequestPaymentDataPaymentSystemsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlaceOrderRequestPaymentDataPaymentSystemsInner();

            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('groupName')) {
                obj['groupName'] = ApiClient.convertToType(data['groupName'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('isCustom')) {
                obj['isCustom'] = ApiClient.convertToType(data['isCustom'], 'Boolean');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('requiresDocument')) {
                obj['requiresDocument'] = ApiClient.convertToType(data['requiresDocument'], 'Boolean');
            }
            if (data.hasOwnProperty('selected')) {
                obj['selected'] = ApiClient.convertToType(data['selected'], 'Boolean');
            }
            if (data.hasOwnProperty('stringId')) {
                obj['stringId'] = ApiClient.convertToType(data['stringId'], 'String');
            }
            if (data.hasOwnProperty('template')) {
                obj['template'] = ApiClient.convertToType(data['template'], 'String');
            }
            if (data.hasOwnProperty('validator')) {
                obj['validator'] = PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator.constructFromObject(data['validator']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlaceOrderRequestPaymentDataPaymentSystemsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlaceOrderRequestPaymentDataPaymentSystemsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['groupName'] && !(typeof data['groupName'] === 'string' || data['groupName'] instanceof String)) {
            throw new Error("Expected the field `groupName` to be a primitive type in the JSON string but got " + data['groupName']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['stringId'] && !(typeof data['stringId'] === 'string' || data['stringId'] instanceof String)) {
            throw new Error("Expected the field `stringId` to be a primitive type in the JSON string but got " + data['stringId']);
        }
        // ensure the json data is a string
        if (data['template'] && !(typeof data['template'] === 'string' || data['template'] instanceof String)) {
            throw new Error("Expected the field `template` to be a primitive type in the JSON string but got " + data['template']);
        }
        // validate the optional field `validator`
        if (data['validator']) { // data not null
          PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator.validateJSON(data['validator']);
        }

        return true;
    }


}



/**
 * Description.
 * @member {String} description
 * @default 'description-example'
 */
PlaceOrderRequestPaymentDataPaymentSystemsInner.prototype['description'] = 'description-example';

/**
 * Payment group name.
 * @member {String} groupName
 */
PlaceOrderRequestPaymentDataPaymentSystemsInner.prototype['groupName'] = undefined;

/**
 * Payment system ID.
 * @member {Number} id
 */
PlaceOrderRequestPaymentDataPaymentSystemsInner.prototype['id'] = undefined;

/**
 * Indicates whether it is custom.
 * @member {Boolean} isCustom
 * @default false
 */
PlaceOrderRequestPaymentDataPaymentSystemsInner.prototype['isCustom'] = false;

/**
 * Payment system name.
 * @member {String} name
 */
PlaceOrderRequestPaymentDataPaymentSystemsInner.prototype['name'] = undefined;

/**
 * Indicates whether a document is required.
 * @member {Boolean} requiresDocument
 * @default false
 */
PlaceOrderRequestPaymentDataPaymentSystemsInner.prototype['requiresDocument'] = false;

/**
 * Indicates whether this payment system has been selected.
 * @member {Boolean} selected
 * @default false
 */
PlaceOrderRequestPaymentDataPaymentSystemsInner.prototype['selected'] = false;

/**
 * String ID.
 * @member {String} stringId
 * @default '12345abc'
 */
PlaceOrderRequestPaymentDataPaymentSystemsInner.prototype['stringId'] = '12345abc';

/**
 * Template.
 * @member {String} template
 * @default 'creditCardPaymentGroup-template'
 */
PlaceOrderRequestPaymentDataPaymentSystemsInner.prototype['template'] = 'creditCardPaymentGroup-template';

/**
 * @member {module:model/PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator} validator
 */
PlaceOrderRequestPaymentDataPaymentSystemsInner.prototype['validator'] = undefined;






export default PlaceOrderRequestPaymentDataPaymentSystemsInner;

