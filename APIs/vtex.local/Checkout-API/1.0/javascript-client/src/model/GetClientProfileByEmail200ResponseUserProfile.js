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
 * The GetClientProfileByEmail200ResponseUserProfile model module.
 * @module model/GetClientProfileByEmail200ResponseUserProfile
 * @version 1.0
 */
class GetClientProfileByEmail200ResponseUserProfile {
    /**
     * Constructs a new <code>GetClientProfileByEmail200ResponseUserProfile</code>.
     * Customer profile information.
     * @alias module:model/GetClientProfileByEmail200ResponseUserProfile
     */
    constructor() { 
        
        GetClientProfileByEmail200ResponseUserProfile.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['isCorporate'] = false;
    }

    /**
     * Constructs a <code>GetClientProfileByEmail200ResponseUserProfile</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetClientProfileByEmail200ResponseUserProfile} obj Optional instance to populate.
     * @return {module:model/GetClientProfileByEmail200ResponseUserProfile} The populated <code>GetClientProfileByEmail200ResponseUserProfile</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetClientProfileByEmail200ResponseUserProfile();

            if (data.hasOwnProperty('corporateDocument')) {
                obj['corporateDocument'] = ApiClient.convertToType(data['corporateDocument'], 'String');
            }
            if (data.hasOwnProperty('corporateName')) {
                obj['corporateName'] = ApiClient.convertToType(data['corporateName'], 'String');
            }
            if (data.hasOwnProperty('corporatePhone')) {
                obj['corporatePhone'] = ApiClient.convertToType(data['corporatePhone'], 'String');
            }
            if (data.hasOwnProperty('customerClass')) {
                obj['customerClass'] = ApiClient.convertToType(data['customerClass'], 'String');
            }
            if (data.hasOwnProperty('document')) {
                obj['document'] = ApiClient.convertToType(data['document'], 'String');
            }
            if (data.hasOwnProperty('documentType')) {
                obj['documentType'] = ApiClient.convertToType(data['documentType'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('firstName')) {
                obj['firstName'] = ApiClient.convertToType(data['firstName'], 'String');
            }
            if (data.hasOwnProperty('isCorporate')) {
                obj['isCorporate'] = ApiClient.convertToType(data['isCorporate'], 'Boolean');
            }
            if (data.hasOwnProperty('lastName')) {
                obj['lastName'] = ApiClient.convertToType(data['lastName'], 'String');
            }
            if (data.hasOwnProperty('phone')) {
                obj['phone'] = ApiClient.convertToType(data['phone'], 'String');
            }
            if (data.hasOwnProperty('profileCompleteOnLoading')) {
                obj['profileCompleteOnLoading'] = ApiClient.convertToType(data['profileCompleteOnLoading'], 'String');
            }
            if (data.hasOwnProperty('profileErrorOnLoading')) {
                obj['profileErrorOnLoading'] = ApiClient.convertToType(data['profileErrorOnLoading'], 'String');
            }
            if (data.hasOwnProperty('stateInscription')) {
                obj['stateInscription'] = ApiClient.convertToType(data['stateInscription'], 'String');
            }
            if (data.hasOwnProperty('tradeName')) {
                obj['tradeName'] = ApiClient.convertToType(data['tradeName'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetClientProfileByEmail200ResponseUserProfile</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetClientProfileByEmail200ResponseUserProfile</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['corporateDocument'] && !(typeof data['corporateDocument'] === 'string' || data['corporateDocument'] instanceof String)) {
            throw new Error("Expected the field `corporateDocument` to be a primitive type in the JSON string but got " + data['corporateDocument']);
        }
        // ensure the json data is a string
        if (data['corporateName'] && !(typeof data['corporateName'] === 'string' || data['corporateName'] instanceof String)) {
            throw new Error("Expected the field `corporateName` to be a primitive type in the JSON string but got " + data['corporateName']);
        }
        // ensure the json data is a string
        if (data['corporatePhone'] && !(typeof data['corporatePhone'] === 'string' || data['corporatePhone'] instanceof String)) {
            throw new Error("Expected the field `corporatePhone` to be a primitive type in the JSON string but got " + data['corporatePhone']);
        }
        // ensure the json data is a string
        if (data['customerClass'] && !(typeof data['customerClass'] === 'string' || data['customerClass'] instanceof String)) {
            throw new Error("Expected the field `customerClass` to be a primitive type in the JSON string but got " + data['customerClass']);
        }
        // ensure the json data is a string
        if (data['document'] && !(typeof data['document'] === 'string' || data['document'] instanceof String)) {
            throw new Error("Expected the field `document` to be a primitive type in the JSON string but got " + data['document']);
        }
        // ensure the json data is a string
        if (data['documentType'] && !(typeof data['documentType'] === 'string' || data['documentType'] instanceof String)) {
            throw new Error("Expected the field `documentType` to be a primitive type in the JSON string but got " + data['documentType']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['firstName'] && !(typeof data['firstName'] === 'string' || data['firstName'] instanceof String)) {
            throw new Error("Expected the field `firstName` to be a primitive type in the JSON string but got " + data['firstName']);
        }
        // ensure the json data is a string
        if (data['lastName'] && !(typeof data['lastName'] === 'string' || data['lastName'] instanceof String)) {
            throw new Error("Expected the field `lastName` to be a primitive type in the JSON string but got " + data['lastName']);
        }
        // ensure the json data is a string
        if (data['phone'] && !(typeof data['phone'] === 'string' || data['phone'] instanceof String)) {
            throw new Error("Expected the field `phone` to be a primitive type in the JSON string but got " + data['phone']);
        }
        // ensure the json data is a string
        if (data['profileCompleteOnLoading'] && !(typeof data['profileCompleteOnLoading'] === 'string' || data['profileCompleteOnLoading'] instanceof String)) {
            throw new Error("Expected the field `profileCompleteOnLoading` to be a primitive type in the JSON string but got " + data['profileCompleteOnLoading']);
        }
        // ensure the json data is a string
        if (data['profileErrorOnLoading'] && !(typeof data['profileErrorOnLoading'] === 'string' || data['profileErrorOnLoading'] instanceof String)) {
            throw new Error("Expected the field `profileErrorOnLoading` to be a primitive type in the JSON string but got " + data['profileErrorOnLoading']);
        }
        // ensure the json data is a string
        if (data['stateInscription'] && !(typeof data['stateInscription'] === 'string' || data['stateInscription'] instanceof String)) {
            throw new Error("Expected the field `stateInscription` to be a primitive type in the JSON string but got " + data['stateInscription']);
        }
        // ensure the json data is a string
        if (data['tradeName'] && !(typeof data['tradeName'] === 'string' || data['tradeName'] instanceof String)) {
            throw new Error("Expected the field `tradeName` to be a primitive type in the JSON string but got " + data['tradeName']);
        }

        return true;
    }


}



/**
 * Document. Used for corporate clients.
 * @member {String} corporateDocument
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['corporateDocument'] = undefined;

/**
 * Name of the company. Used for corporate clients.
 * @member {String} corporateName
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['corporateName'] = undefined;

/**
 * Telephone number. Used for corporate clients.
 * @member {String} corporatePhone
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['corporatePhone'] = undefined;

/**
 * Customer class.
 * @member {String} customerClass
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['customerClass'] = undefined;

/**
 * Document.
 * @member {String} document
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['document'] = undefined;

/**
 * Document type.
 * @member {String} documentType
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['documentType'] = undefined;

/**
 * Email address.
 * @member {String} email
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['email'] = undefined;

/**
 * First name.
 * @member {String} firstName
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['firstName'] = undefined;

/**
 * Indicates whether client is corporate.
 * @member {Boolean} isCorporate
 * @default false
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['isCorporate'] = false;

/**
 * Last name.
 * @member {String} lastName
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['lastName'] = undefined;

/**
 * Telephone number.
 * @member {String} phone
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['phone'] = undefined;

/**
 * Profile complete when loading.
 * @member {String} profileCompleteOnLoading
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['profileCompleteOnLoading'] = undefined;

/**
 * Profile error when loading.
 * @member {String} profileErrorOnLoading
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['profileErrorOnLoading'] = undefined;

/**
 * State inscription. Used for corporate clients.
 * @member {String} stateInscription
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['stateInscription'] = undefined;

/**
 * Trade name. Used for corporate clients.
 * @member {String} tradeName
 */
GetClientProfileByEmail200ResponseUserProfile.prototype['tradeName'] = undefined;






export default GetClientProfileByEmail200ResponseUserProfile;

