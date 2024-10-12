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

/**
 * The TagValue model module.
 * @module model/TagValue
 * @version R4.2a
 */
class TagValue {
    /**
     * Constructs a new <code>TagValue</code>.
     * @alias module:model/TagValue
     * @param valueType {String} 
     */
    constructor(valueType) { 
        
        TagValue.initialize(this, valueType);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, valueType) { 
        obj['valueType'] = valueType;
    }

    /**
     * Constructs a <code>TagValue</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TagValue} obj Optional instance to populate.
     * @return {module:model/TagValue} The populated <code>TagValue</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TagValue();

            if (data.hasOwnProperty('valueType')) {
                obj['valueType'] = ApiClient.convertToType(data['valueType'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TagValue</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TagValue</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TagValue.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['valueType'] && !(typeof data['valueType'] === 'string' || data['valueType'] instanceof String)) {
            throw new Error("Expected the field `valueType` to be a primitive type in the JSON string but got " + data['valueType']);
        }

        return true;
    }


}

TagValue.RequiredProperties = ["valueType"];

/**
 * @member {String} valueType
 */
TagValue.prototype['valueType'] = undefined;






export default TagValue;

