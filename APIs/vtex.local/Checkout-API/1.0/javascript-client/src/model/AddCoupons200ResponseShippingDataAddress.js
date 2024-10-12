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
 * The AddCoupons200ResponseShippingDataAddress model module.
 * @module model/AddCoupons200ResponseShippingDataAddress
 * @version 1.0
 */
class AddCoupons200ResponseShippingDataAddress {
    /**
     * Constructs a new <code>AddCoupons200ResponseShippingDataAddress</code>.
     * Address information.
     * @alias module:model/AddCoupons200ResponseShippingDataAddress
     */
    constructor() { 
        
        AddCoupons200ResponseShippingDataAddress.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AddCoupons200ResponseShippingDataAddress</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AddCoupons200ResponseShippingDataAddress} obj Optional instance to populate.
     * @return {module:model/AddCoupons200ResponseShippingDataAddress} The populated <code>AddCoupons200ResponseShippingDataAddress</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AddCoupons200ResponseShippingDataAddress();

            if (data.hasOwnProperty('addressId')) {
                obj['addressId'] = ApiClient.convertToType(data['addressId'], 'String');
            }
            if (data.hasOwnProperty('addressType')) {
                obj['addressType'] = ApiClient.convertToType(data['addressType'], 'String');
            }
            if (data.hasOwnProperty('city')) {
                obj['city'] = ApiClient.convertToType(data['city'], 'String');
            }
            if (data.hasOwnProperty('complement')) {
                obj['complement'] = ApiClient.convertToType(data['complement'], 'String');
            }
            if (data.hasOwnProperty('country')) {
                obj['country'] = ApiClient.convertToType(data['country'], 'String');
            }
            if (data.hasOwnProperty('geoCoordinates')) {
                obj['geoCoordinates'] = ApiClient.convertToType(data['geoCoordinates'], ['Number']);
            }
            if (data.hasOwnProperty('isDisposable')) {
                obj['isDisposable'] = ApiClient.convertToType(data['isDisposable'], 'Boolean');
            }
            if (data.hasOwnProperty('neighborhood')) {
                obj['neighborhood'] = ApiClient.convertToType(data['neighborhood'], 'String');
            }
            if (data.hasOwnProperty('number')) {
                obj['number'] = ApiClient.convertToType(data['number'], 'String');
            }
            if (data.hasOwnProperty('postalCode')) {
                obj['postalCode'] = ApiClient.convertToType(data['postalCode'], 'String');
            }
            if (data.hasOwnProperty('receiverName')) {
                obj['receiverName'] = ApiClient.convertToType(data['receiverName'], 'String');
            }
            if (data.hasOwnProperty('reference')) {
                obj['reference'] = ApiClient.convertToType(data['reference'], 'String');
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], 'String');
            }
            if (data.hasOwnProperty('street')) {
                obj['street'] = ApiClient.convertToType(data['street'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AddCoupons200ResponseShippingDataAddress</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AddCoupons200ResponseShippingDataAddress</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['addressId'] && !(typeof data['addressId'] === 'string' || data['addressId'] instanceof String)) {
            throw new Error("Expected the field `addressId` to be a primitive type in the JSON string but got " + data['addressId']);
        }
        // ensure the json data is a string
        if (data['addressType'] && !(typeof data['addressType'] === 'string' || data['addressType'] instanceof String)) {
            throw new Error("Expected the field `addressType` to be a primitive type in the JSON string but got " + data['addressType']);
        }
        // ensure the json data is a string
        if (data['city'] && !(typeof data['city'] === 'string' || data['city'] instanceof String)) {
            throw new Error("Expected the field `city` to be a primitive type in the JSON string but got " + data['city']);
        }
        // ensure the json data is a string
        if (data['complement'] && !(typeof data['complement'] === 'string' || data['complement'] instanceof String)) {
            throw new Error("Expected the field `complement` to be a primitive type in the JSON string but got " + data['complement']);
        }
        // ensure the json data is a string
        if (data['country'] && !(typeof data['country'] === 'string' || data['country'] instanceof String)) {
            throw new Error("Expected the field `country` to be a primitive type in the JSON string but got " + data['country']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['geoCoordinates'])) {
            throw new Error("Expected the field `geoCoordinates` to be an array in the JSON data but got " + data['geoCoordinates']);
        }
        // ensure the json data is a string
        if (data['neighborhood'] && !(typeof data['neighborhood'] === 'string' || data['neighborhood'] instanceof String)) {
            throw new Error("Expected the field `neighborhood` to be a primitive type in the JSON string but got " + data['neighborhood']);
        }
        // ensure the json data is a string
        if (data['number'] && !(typeof data['number'] === 'string' || data['number'] instanceof String)) {
            throw new Error("Expected the field `number` to be a primitive type in the JSON string but got " + data['number']);
        }
        // ensure the json data is a string
        if (data['postalCode'] && !(typeof data['postalCode'] === 'string' || data['postalCode'] instanceof String)) {
            throw new Error("Expected the field `postalCode` to be a primitive type in the JSON string but got " + data['postalCode']);
        }
        // ensure the json data is a string
        if (data['receiverName'] && !(typeof data['receiverName'] === 'string' || data['receiverName'] instanceof String)) {
            throw new Error("Expected the field `receiverName` to be a primitive type in the JSON string but got " + data['receiverName']);
        }
        // ensure the json data is a string
        if (data['reference'] && !(typeof data['reference'] === 'string' || data['reference'] instanceof String)) {
            throw new Error("Expected the field `reference` to be a primitive type in the JSON string but got " + data['reference']);
        }
        // ensure the json data is a string
        if (data['state'] && !(typeof data['state'] === 'string' || data['state'] instanceof String)) {
            throw new Error("Expected the field `state` to be a primitive type in the JSON string but got " + data['state']);
        }
        // ensure the json data is a string
        if (data['street'] && !(typeof data['street'] === 'string' || data['street'] instanceof String)) {
            throw new Error("Expected the field `street` to be a primitive type in the JSON string but got " + data['street']);
        }

        return true;
    }


}



/**
 * Address ID.
 * @member {String} addressId
 */
AddCoupons200ResponseShippingDataAddress.prototype['addressId'] = undefined;

/**
 * Type of address. For example, `Residential` or `Pickup`.
 * @member {String} addressType
 */
AddCoupons200ResponseShippingDataAddress.prototype['addressType'] = undefined;

/**
 * City of the shipping address.
 * @member {String} city
 */
AddCoupons200ResponseShippingDataAddress.prototype['city'] = undefined;

/**
 * Complement to the shipping address, in case it applies.
 * @member {String} complement
 */
AddCoupons200ResponseShippingDataAddress.prototype['complement'] = undefined;

/**
 * Three letter ISO code of the country of the shipping address.
 * @member {String} country
 */
AddCoupons200ResponseShippingDataAddress.prototype['country'] = undefined;

/**
 * Array containing two floats with geocoordinates, first longitude, then latitude.
 * @member {Array.<Number>} geoCoordinates
 */
AddCoupons200ResponseShippingDataAddress.prototype['geoCoordinates'] = undefined;

/**
 * Indicates whether address is disposable.
 * @member {Boolean} isDisposable
 */
AddCoupons200ResponseShippingDataAddress.prototype['isDisposable'] = undefined;

/**
 * Neighborhood of the shipping address.
 * @member {String} neighborhood
 */
AddCoupons200ResponseShippingDataAddress.prototype['neighborhood'] = undefined;

/**
 * Number of the building, house or apartment in the shipping address.
 * @member {String} number
 */
AddCoupons200ResponseShippingDataAddress.prototype['number'] = undefined;

/**
 * Postal code.
 * @member {String} postalCode
 */
AddCoupons200ResponseShippingDataAddress.prototype['postalCode'] = undefined;

/**
 * Name of the person who is going to receive the order.
 * @member {String} receiverName
 */
AddCoupons200ResponseShippingDataAddress.prototype['receiverName'] = undefined;

/**
 * Complement that might help locate the shipping address more precisely in case of delivery.
 * @member {String} reference
 */
AddCoupons200ResponseShippingDataAddress.prototype['reference'] = undefined;

/**
 * State of the shipping address.
 * @member {String} state
 */
AddCoupons200ResponseShippingDataAddress.prototype['state'] = undefined;

/**
 * Street of the shipping address.
 * @member {String} street
 */
AddCoupons200ResponseShippingDataAddress.prototype['street'] = undefined;






export default AddCoupons200ResponseShippingDataAddress;

