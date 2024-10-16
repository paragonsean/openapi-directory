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

/**
 * The ContactListEventCustomization model module.
 * @module model/ContactListEventCustomization
 * @version 0.9
 */
class ContactListEventCustomization {
    /**
     * Constructs a new <code>ContactListEventCustomization</code>.
     * @alias module:model/ContactListEventCustomization
     * @param type {Number} Type (   1- Subscribe confirmation request landing page   2- Subscribe opt-in landing page   3- Unsubscribe confirmation landing page ) 
     */
    constructor(type) { 
        
        ContactListEventCustomization.initialize(this, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, type) { 
        obj['type'] = type;
    }

    /**
     * Constructs a <code>ContactListEventCustomization</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ContactListEventCustomization} obj Optional instance to populate.
     * @return {module:model/ContactListEventCustomization} The populated <code>ContactListEventCustomization</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ContactListEventCustomization();

            if (data.hasOwnProperty('redirecturl')) {
                obj['redirecturl'] = ApiClient.convertToType(data['redirecturl'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ContactListEventCustomization</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ContactListEventCustomization</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ContactListEventCustomization.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['redirecturl'] && !(typeof data['redirecturl'] === 'string' || data['redirecturl'] instanceof String)) {
            throw new Error("Expected the field `redirecturl` to be a primitive type in the JSON string but got " + data['redirecturl']);
        }

        return true;
    }


}

ContactListEventCustomization.RequiredProperties = ["type"];

/**
 * full url of the destination landing page
 * @member {String} redirecturl
 */
ContactListEventCustomization.prototype['redirecturl'] = undefined;

/**
 * Type (   1- Subscribe confirmation request landing page   2- Subscribe opt-in landing page   3- Unsubscribe confirmation landing page ) 
 * @member {Number} type
 */
ContactListEventCustomization.prototype['type'] = undefined;






export default ContactListEventCustomization;

