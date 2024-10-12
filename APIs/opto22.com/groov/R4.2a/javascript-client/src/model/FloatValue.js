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
 * The FloatValue model module.
 * @module model/FloatValue
 * @version R4.2a
 */
class FloatValue {
    /**
     * Constructs a new <code>FloatValue</code>.
     * @alias module:model/FloatValue
     * @extends module:model/TagValue
     * @implements module:model/TagValue
     * @param valueType {String} 
     * @param value {Number} 
     */
    constructor(valueType, value) { 
        TagValue.initialize(this, valueType);
        FloatValue.initialize(this, valueType, value);
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
     * Constructs a <code>FloatValue</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FloatValue} obj Optional instance to populate.
     * @return {module:model/FloatValue} The populated <code>FloatValue</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FloatValue();
            TagValue.constructFromObject(data, obj);
            TagValue.constructFromObject(data, obj);

            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FloatValue</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FloatValue</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of FloatValue.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

FloatValue.RequiredProperties = ["value", "valueType"];

/**
 * @member {Number} value
 */
FloatValue.prototype['value'] = undefined;


// Implement TagValue interface:
/**
 * @member {String} valueType
 */
TagValue.prototype['valueType'] = undefined;




export default FloatValue;

