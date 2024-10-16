/**
 * OnSched Consumer API
 * Build secure and scalable custom apps for Online Booking. Our flexible API provides many options for availability and booking.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AddressUpdateModel from './AddressUpdateModel';
import ContactUpdateModel from './ContactUpdateModel';
import CustomFieldUpdateModel from './CustomFieldUpdateModel';

/**
 * The CustomerUpdateModel model module.
 * @module model/CustomerUpdateModel
 * @version v1
 */
class CustomerUpdateModel {
    /**
     * Constructs a new <code>CustomerUpdateModel</code>.
     * @alias module:model/CustomerUpdateModel
     */
    constructor() { 
        
        CustomerUpdateModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CustomerUpdateModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CustomerUpdateModel} obj Optional instance to populate.
     * @return {module:model/CustomerUpdateModel} The populated <code>CustomerUpdateModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CustomerUpdateModel();

            if (data.hasOwnProperty('address')) {
                obj['address'] = AddressUpdateModel.constructFromObject(data['address']);
            }
            if (data.hasOwnProperty('contact')) {
                obj['contact'] = ContactUpdateModel.constructFromObject(data['contact']);
            }
            if (data.hasOwnProperty('customFields')) {
                obj['customFields'] = CustomFieldUpdateModel.constructFromObject(data['customFields']);
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('firstname')) {
                obj['firstname'] = ApiClient.convertToType(data['firstname'], 'String');
            }
            if (data.hasOwnProperty('lastname')) {
                obj['lastname'] = ApiClient.convertToType(data['lastname'], 'String');
            }
            if (data.hasOwnProperty('locationId')) {
                obj['locationId'] = ApiClient.convertToType(data['locationId'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('notificationType')) {
                obj['notificationType'] = ApiClient.convertToType(data['notificationType'], 'String');
            }
            if (data.hasOwnProperty('stripeCustomerId')) {
                obj['stripeCustomerId'] = ApiClient.convertToType(data['stripeCustomerId'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CustomerUpdateModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CustomerUpdateModel</code>.
     */
    static validateJSON(data) {
        // validate the optional field `address`
        if (data['address']) { // data not null
          AddressUpdateModel.validateJSON(data['address']);
        }
        // validate the optional field `contact`
        if (data['contact']) { // data not null
          ContactUpdateModel.validateJSON(data['contact']);
        }
        // validate the optional field `customFields`
        if (data['customFields']) { // data not null
          CustomFieldUpdateModel.validateJSON(data['customFields']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['firstname'] && !(typeof data['firstname'] === 'string' || data['firstname'] instanceof String)) {
            throw new Error("Expected the field `firstname` to be a primitive type in the JSON string but got " + data['firstname']);
        }
        // ensure the json data is a string
        if (data['lastname'] && !(typeof data['lastname'] === 'string' || data['lastname'] instanceof String)) {
            throw new Error("Expected the field `lastname` to be a primitive type in the JSON string but got " + data['lastname']);
        }
        // ensure the json data is a string
        if (data['locationId'] && !(typeof data['locationId'] === 'string' || data['locationId'] instanceof String)) {
            throw new Error("Expected the field `locationId` to be a primitive type in the JSON string but got " + data['locationId']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['notificationType'] && !(typeof data['notificationType'] === 'string' || data['notificationType'] instanceof String)) {
            throw new Error("Expected the field `notificationType` to be a primitive type in the JSON string but got " + data['notificationType']);
        }
        // ensure the json data is a string
        if (data['stripeCustomerId'] && !(typeof data['stripeCustomerId'] === 'string' || data['stripeCustomerId'] instanceof String)) {
            throw new Error("Expected the field `stripeCustomerId` to be a primitive type in the JSON string but got " + data['stripeCustomerId']);
        }

        return true;
    }


}



/**
 * @member {module:model/AddressUpdateModel} address
 */
CustomerUpdateModel.prototype['address'] = undefined;

/**
 * @member {module:model/ContactUpdateModel} contact
 */
CustomerUpdateModel.prototype['contact'] = undefined;

/**
 * @member {module:model/CustomFieldUpdateModel} customFields
 */
CustomerUpdateModel.prototype['customFields'] = undefined;

/**
 * @member {String} email
 */
CustomerUpdateModel.prototype['email'] = undefined;

/**
 * @member {String} firstname
 */
CustomerUpdateModel.prototype['firstname'] = undefined;

/**
 * @member {String} lastname
 */
CustomerUpdateModel.prototype['lastname'] = undefined;

/**
 * @member {String} locationId
 */
CustomerUpdateModel.prototype['locationId'] = undefined;

/**
 * @member {String} name
 */
CustomerUpdateModel.prototype['name'] = undefined;

/**
 * 0 = default(Email), 1 = Email, 2 = SMS, 3 = Email and SMS
 * @member {String} notificationType
 */
CustomerUpdateModel.prototype['notificationType'] = undefined;

/**
 * @member {String} stripeCustomerId
 */
CustomerUpdateModel.prototype['stripeCustomerId'] = undefined;

/**
 * @member {Number} type
 */
CustomerUpdateModel.prototype['type'] = undefined;






export default CustomerUpdateModel;

