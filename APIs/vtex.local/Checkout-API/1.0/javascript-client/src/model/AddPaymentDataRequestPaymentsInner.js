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
 * The AddPaymentDataRequestPaymentsInner model module.
 * @module model/AddPaymentDataRequestPaymentsInner
 * @version 1.0
 */
class AddPaymentDataRequestPaymentsInner {
    /**
     * Constructs a new <code>AddPaymentDataRequestPaymentsInner</code>.
     * @alias module:model/AddPaymentDataRequestPaymentsInner
     */
    constructor() { 
        
        AddPaymentDataRequestPaymentsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['group'] = 'bankInvoicePaymentGroup';
        obj['hasDefaultBillingAddress'] = false;
        obj['installments'] = 1;
        obj['installmentsInterestRate'] = 0;
        obj['installmentsValue'] = 1;
        obj['paymentSystem'] = 1;
        obj['paymentSystemName'] = 'Boleto Bancário';
        obj['referenceValue'] = 100;
        obj['value'] = 100;
    }

    /**
     * Constructs a <code>AddPaymentDataRequestPaymentsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AddPaymentDataRequestPaymentsInner} obj Optional instance to populate.
     * @return {module:model/AddPaymentDataRequestPaymentsInner} The populated <code>AddPaymentDataRequestPaymentsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AddPaymentDataRequestPaymentsInner();

            if (data.hasOwnProperty('group')) {
                obj['group'] = ApiClient.convertToType(data['group'], 'String');
            }
            if (data.hasOwnProperty('hasDefaultBillingAddress')) {
                obj['hasDefaultBillingAddress'] = ApiClient.convertToType(data['hasDefaultBillingAddress'], 'Boolean');
            }
            if (data.hasOwnProperty('installments')) {
                obj['installments'] = ApiClient.convertToType(data['installments'], 'Number');
            }
            if (data.hasOwnProperty('installmentsInterestRate')) {
                obj['installmentsInterestRate'] = ApiClient.convertToType(data['installmentsInterestRate'], 'Number');
            }
            if (data.hasOwnProperty('installmentsValue')) {
                obj['installmentsValue'] = ApiClient.convertToType(data['installmentsValue'], 'Number');
            }
            if (data.hasOwnProperty('paymentSystem')) {
                obj['paymentSystem'] = ApiClient.convertToType(data['paymentSystem'], 'Number');
            }
            if (data.hasOwnProperty('paymentSystemName')) {
                obj['paymentSystemName'] = ApiClient.convertToType(data['paymentSystemName'], 'String');
            }
            if (data.hasOwnProperty('referenceValue')) {
                obj['referenceValue'] = ApiClient.convertToType(data['referenceValue'], 'Number');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AddPaymentDataRequestPaymentsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AddPaymentDataRequestPaymentsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['group'] && !(typeof data['group'] === 'string' || data['group'] instanceof String)) {
            throw new Error("Expected the field `group` to be a primitive type in the JSON string but got " + data['group']);
        }
        // ensure the json data is a string
        if (data['paymentSystemName'] && !(typeof data['paymentSystemName'] === 'string' || data['paymentSystemName'] instanceof String)) {
            throw new Error("Expected the field `paymentSystemName` to be a primitive type in the JSON string but got " + data['paymentSystemName']);
        }

        return true;
    }


}



/**
 * Payment system group.
 * @member {String} group
 * @default 'bankInvoicePaymentGroup'
 */
AddPaymentDataRequestPaymentsInner.prototype['group'] = 'bankInvoicePaymentGroup';

/**
 * Indicates whether billing address for this payment is the default address.
 * @member {Boolean} hasDefaultBillingAddress
 * @default false
 */
AddPaymentDataRequestPaymentsInner.prototype['hasDefaultBillingAddress'] = false;

/**
 * Selected number of installments.
 * @member {Number} installments
 * @default 1
 */
AddPaymentDataRequestPaymentsInner.prototype['installments'] = 1;

/**
 * Installments' interest rate.
 * @member {Number} installmentsInterestRate
 * @default 0
 */
AddPaymentDataRequestPaymentsInner.prototype['installmentsInterestRate'] = 0;

/**
 * Value of the installments.
 * @member {Number} installmentsValue
 * @default 1
 */
AddPaymentDataRequestPaymentsInner.prototype['installmentsValue'] = 1;

/**
 * Payment system ID.
 * @member {Number} paymentSystem
 * @default 1
 */
AddPaymentDataRequestPaymentsInner.prototype['paymentSystem'] = 1;

/**
 * Payment system name.
 * @member {String} paymentSystemName
 * @default 'Boleto Bancário'
 */
AddPaymentDataRequestPaymentsInner.prototype['paymentSystemName'] = 'Boleto Bancário';

/**
 * Reference value used to calculate total order value with interest.
 * @member {Number} referenceValue
 * @default 100
 */
AddPaymentDataRequestPaymentsInner.prototype['referenceValue'] = 100;

/**
 * Total value assigned to this payment.
 * @member {Number} value
 * @default 100
 */
AddPaymentDataRequestPaymentsInner.prototype['value'] = 100;






export default AddPaymentDataRequestPaymentsInner;

