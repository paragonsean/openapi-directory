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
 * The AddClientProfileRequest model module.
 * @module model/AddClientProfileRequest
 * @version 1.0
 */
class AddClientProfileRequest {
    /**
     * Constructs a new <code>AddClientProfileRequest</code>.
     * Customer&#39;s profile information.
     * @alias module:model/AddClientProfileRequest
     * @param document {String} Document number informed by the customer.
     * @param documentType {String} Type of the document informed by the customer.
     * @param email {String} Customer's email address.
     * @param firstName {String} Customer's first name.
     * @param lastName {String} Customer's last name.
     */
    constructor(document, documentType, email, firstName, lastName) { 
        
        AddClientProfileRequest.initialize(this, document, documentType, email, firstName, lastName);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, document, documentType, email, firstName, lastName) { 
        obj['corporateDocument'] = '12345678000100';
        obj['corporateName'] = 'company-name';
        obj['corporatePhone'] = '+551100988887777';
        obj['document'] = document || '123456789';
        obj['documentType'] = documentType || 'cpf';
        obj['email'] = email || 'customer@examplemail.com';
        obj['firstName'] = firstName || 'first-name';
        obj['isCorporate'] = false;
        obj['lastName'] = lastName || 'last-name';
        obj['phone'] = '+55110988887777';
        obj['stateInscription'] = '12345678';
        obj['tradeName'] = 'trade-name';
    }

    /**
     * Constructs a <code>AddClientProfileRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AddClientProfileRequest} obj Optional instance to populate.
     * @return {module:model/AddClientProfileRequest} The populated <code>AddClientProfileRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AddClientProfileRequest();

            if (data.hasOwnProperty('corporateDocument')) {
                obj['corporateDocument'] = ApiClient.convertToType(data['corporateDocument'], 'String');
            }
            if (data.hasOwnProperty('corporateName')) {
                obj['corporateName'] = ApiClient.convertToType(data['corporateName'], 'String');
            }
            if (data.hasOwnProperty('corporatePhone')) {
                obj['corporatePhone'] = ApiClient.convertToType(data['corporatePhone'], 'String');
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
     * Validates the JSON data with respect to <code>AddClientProfileRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AddClientProfileRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AddClientProfileRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
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

AddClientProfileRequest.RequiredProperties = ["document", "documentType", "email", "firstName", "lastName"];

/**
 * Corporate document, if the customer is a legal entity.
 * @member {String} corporateDocument
 * @default '12345678000100'
 */
AddClientProfileRequest.prototype['corporateDocument'] = '12345678000100';

/**
 * Company name, if the customer is a legal entity.
 * @member {String} corporateName
 * @default 'company-name'
 */
AddClientProfileRequest.prototype['corporateName'] = 'company-name';

/**
 * Corporate phone number, if the customer is a legal entity.
 * @member {String} corporatePhone
 * @default '+551100988887777'
 */
AddClientProfileRequest.prototype['corporatePhone'] = '+551100988887777';

/**
 * Document number informed by the customer.
 * @member {String} document
 * @default '123456789'
 */
AddClientProfileRequest.prototype['document'] = '123456789';

/**
 * Type of the document informed by the customer.
 * @member {String} documentType
 * @default 'cpf'
 */
AddClientProfileRequest.prototype['documentType'] = 'cpf';

/**
 * Customer's email address.
 * @member {String} email
 * @default 'customer@examplemail.com'
 */
AddClientProfileRequest.prototype['email'] = 'customer@examplemail.com';

/**
 * Customer's first name.
 * @member {String} firstName
 * @default 'first-name'
 */
AddClientProfileRequest.prototype['firstName'] = 'first-name';

/**
 * `true` if the customer is a legal entity.
 * @member {Boolean} isCorporate
 * @default false
 */
AddClientProfileRequest.prototype['isCorporate'] = false;

/**
 * Customer's last name.
 * @member {String} lastName
 * @default 'last-name'
 */
AddClientProfileRequest.prototype['lastName'] = 'last-name';

/**
 * Customer's phone number.
 * @member {String} phone
 * @default '+55110988887777'
 */
AddClientProfileRequest.prototype['phone'] = '+55110988887777';

/**
 * State inscription, if the customer is a legal entity.
 * @member {String} stateInscription
 * @default '12345678'
 */
AddClientProfileRequest.prototype['stateInscription'] = '12345678';

/**
 * Trade name, if the customer is a legal entity.
 * @member {String} tradeName
 * @default 'trade-name'
 */
AddClientProfileRequest.prototype['tradeName'] = 'trade-name';






export default AddClientProfileRequest;

