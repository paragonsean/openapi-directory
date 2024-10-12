/**
 * groov View Public API
 * #### Revised: 2019-11-21  ### Overview groov View Public API revision 1. 
 *
 * The version of the OpenAPI document: R4.2a
 * Contact: developer@opto22.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import TagValue from './TagValue';

/**
 * The StringArrayValue model module.
 * @module model/StringArrayValue
 * @version R4.2a
 */
class StringArrayValue {
    /**
     * Constructs a new <code>StringArrayValue</code>.
     * @alias module:model/StringArrayValue
     * @extends module:model/TagValue
     * @implements module:model/TagValue
     * @param valueType {String} 
     * @param value {Array.<String>} 
     */
    constructor(valueType, value) { 
        TagValue.initialize(this, valueType);
        StringArrayValue.initialize(this, valueType, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, valueType, value) { 
        obj['value'] = value;
    }

    /**
     * Constructs a <code>StringArrayValue</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/StringArrayValue} obj Optional instance to populate.
     * @return {module:model/StringArrayValue} The populated <code>StringArrayValue</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new StringArrayValue();
            TagValue.constructFromObject(data, obj);
            TagValue.constructFromObject(data, obj);

            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>StringArrayValue</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>StringArrayValue</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of StringArrayValue.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['value'])) {
            throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
        }

        return true;
    }


}

StringArrayValue.RequiredProperties = ["value", "valueType"];

/**
 * @member {Array.<String>} value
 */
StringArrayValue.prototype['value'] = undefined;


// Implement TagValue interface:
/**
 * @member {String} valueType
 */
TagValue.prototype['valueType'] = undefined;




export default StringArrayValue;

