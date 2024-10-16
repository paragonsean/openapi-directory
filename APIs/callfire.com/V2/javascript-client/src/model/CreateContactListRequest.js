/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Contact from './Contact';

/**
 * The CreateContactListRequest model module.
 * @module model/CreateContactListRequest
 * @version V2
 */
class CreateContactListRequest {
    /**
     * Constructs a new <code>CreateContactListRequest</code>.
     * A request object is used to create a contact list from one of available contact sources
     * @alias module:model/CreateContactListRequest
     */
    constructor() { 
        
        CreateContactListRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CreateContactListRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateContactListRequest} obj Optional instance to populate.
     * @return {module:model/CreateContactListRequest} The populated <code>CreateContactListRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateContactListRequest();

            if (data.hasOwnProperty('contactIds')) {
                obj['contactIds'] = ApiClient.convertToType(data['contactIds'], ['Number']);
            }
            if (data.hasOwnProperty('contactNumbers')) {
                obj['contactNumbers'] = ApiClient.convertToType(data['contactNumbers'], ['String']);
            }
            if (data.hasOwnProperty('contactNumbersField')) {
                obj['contactNumbersField'] = ApiClient.convertToType(data['contactNumbersField'], 'String');
            }
            if (data.hasOwnProperty('contacts')) {
                obj['contacts'] = ApiClient.convertToType(data['contacts'], [Contact]);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('useCustomFields')) {
                obj['useCustomFields'] = ApiClient.convertToType(data['useCustomFields'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateContactListRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateContactListRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['contactIds'])) {
            throw new Error("Expected the field `contactIds` to be an array in the JSON data but got " + data['contactIds']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['contactNumbers'])) {
            throw new Error("Expected the field `contactNumbers` to be an array in the JSON data but got " + data['contactNumbers']);
        }
        // ensure the json data is a string
        if (data['contactNumbersField'] && !(typeof data['contactNumbersField'] === 'string' || data['contactNumbersField'] instanceof String)) {
            throw new Error("Expected the field `contactNumbersField` to be a primitive type in the JSON string but got " + data['contactNumbersField']);
        }
        if (data['contacts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['contacts'])) {
                throw new Error("Expected the field `contacts` to be an array in the JSON data but got " + data['contacts']);
            }
            // validate the optional field `contacts` (array)
            for (const item of data['contacts']) {
                Contact.validateJSON(item);
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
 * A list of ids of existing contacts in CallFire system
 * @member {Array.<Number>} contactIds
 */
CreateContactListRequest.prototype['contactIds'] = undefined;

/**
 * List of numbers in E.164 format (11-digit). Example: 12132000384
 * @member {Array.<String>} contactNumbers
 */
CreateContactListRequest.prototype['contactNumbers'] = undefined;

/**
 * A type of a phone number (homePhone, workPhone, mobilePhone). This parameter is used with contactNumbers and specifies which types of phone numbers are included to a contact list
 * @member {String} contactNumbersField
 */
CreateContactListRequest.prototype['contactNumbersField'] = undefined;

/**
 * A list of new contact objects to be added
 * @member {Array.<module:model/Contact>} contacts
 */
CreateContactListRequest.prototype['contacts'] = undefined;

/**
 * A name of a contact list
 * @member {String} name
 */
CreateContactListRequest.prototype['name'] = undefined;

/**
 * A flag to indicate how to define property names for contacts. If true, uses the field and property names exactly as defined. If false will assign custom properties and fields to A, B, C, etc
 * @member {Boolean} useCustomFields
 */
CreateContactListRequest.prototype['useCustomFields'] = undefined;






export default CreateContactListRequest;

