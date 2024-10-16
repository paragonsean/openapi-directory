/**
 * Mailsquad
 * MailSquad offers an affordable and super easy way to create, send and track delightful emails.
 *
 * The version of the OpenAPI document: 0.9
 * Contact: support@mailsquad.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ContactCustomFieldSchema from './ContactCustomFieldSchema';
import ContactListEventCustomization from './ContactListEventCustomization';

/**
 * The ContactListUpdate model module.
 * @module model/ContactListUpdate
 * @version 0.9
 */
class ContactListUpdate {
    /**
     * Constructs a new <code>ContactListUpdate</code>.
     * @alias module:model/ContactListUpdate
     */
    constructor() { 
        
        ContactListUpdate.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ContactListUpdate</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ContactListUpdate} obj Optional instance to populate.
     * @return {module:model/ContactListUpdate} The populated <code>ContactListUpdate</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ContactListUpdate();

            if (data.hasOwnProperty('customfields')) {
                obj['customfields'] = ApiClient.convertToType(data['customfields'], [ContactCustomFieldSchema]);
            }
            if (data.hasOwnProperty('eventcustomizations')) {
                obj['eventcustomizations'] = ApiClient.convertToType(data['eventcustomizations'], [ContactListEventCustomization]);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ContactListUpdate</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ContactListUpdate</code>.
     */
    static validateJSON(data) {
        if (data['customfields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['customfields'])) {
                throw new Error("Expected the field `customfields` to be an array in the JSON data but got " + data['customfields']);
            }
            // validate the optional field `customfields` (array)
            for (const item of data['customfields']) {
                ContactCustomFieldSchema.validateJSON(item);
            };
        }
        if (data['eventcustomizations']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['eventcustomizations'])) {
                throw new Error("Expected the field `eventcustomizations` to be an array in the JSON data but got " + data['eventcustomizations']);
            }
            // validate the optional field `eventcustomizations` (array)
            for (const item of data['eventcustomizations']) {
                ContactListEventCustomization.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * Array of ContactCustomFieldSchema
 * @member {Array.<module:model/ContactCustomFieldSchema>} customfields
 */
ContactListUpdate.prototype['customfields'] = undefined;

/**
 * Array of ContactListEventCustomization
 * @member {Array.<module:model/ContactListEventCustomization>} eventcustomizations
 */
ContactListUpdate.prototype['eventcustomizations'] = undefined;

/**
 * Name of the contact list
 * @member {String} name
 */
ContactListUpdate.prototype['name'] = undefined;






export default ContactListUpdate;

