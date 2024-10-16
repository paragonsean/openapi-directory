/**
 * Personnel Data
 * API for reading and writing personnel data incl. data about attendances and absences
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
import Attribute from './Attribute';

/**
 * The Office model module.
 * @module model/Office
 * @version 1.0
 */
class Office {
    /**
     * Constructs a new <code>Office</code>.
     * @alias module:model/Office
     * @implements module:model/Attribute
     * @param label {String} 
     * @param value {Object} 
     */
    constructor(label, value) { 
        Attribute.initialize(this, label, value);
        Office.initialize(this, label, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, label, value) { 
        obj['label'] = label;
    }

    /**
     * Constructs a <code>Office</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Office} obj Optional instance to populate.
     * @return {module:model/Office} The populated <code>Office</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Office();
            Attribute.constructFromObject(data, obj);

            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], Object);
            }
            if (data.hasOwnProperty('label')) {
                obj['label'] = ApiClient.convertToType(data['label'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Office</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Office</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Office.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `value`
        if (data['value']) { // data not null
          Object.validateJSON(data['value']);
        }
        // ensure the json data is a string
        if (data['label'] && !(typeof data['label'] === 'string' || data['label'] instanceof String)) {
            throw new Error("Expected the field `label` to be a primitive type in the JSON string but got " + data['label']);
        }

        return true;
    }


}

Office.RequiredProperties = ["label", "value"];

/**
 * @member {Object} value
 */
Office.prototype['value'] = undefined;

/**
 * @member {String} label
 */
Office.prototype['label'] = undefined;


// Implement Attribute interface:
/**
 * @member {String} label
 */
Attribute.prototype['label'] = undefined;
/**
 * @member {Object} value
 */
Attribute.prototype['value'] = undefined;




export default Office;

