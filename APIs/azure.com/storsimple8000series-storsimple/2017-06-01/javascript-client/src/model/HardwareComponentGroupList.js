/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import HardwareComponentGroup from './HardwareComponentGroup';

/**
 * The HardwareComponentGroupList model module.
 * @module model/HardwareComponentGroupList
 * @version 2017-06-01
 */
class HardwareComponentGroupList {
    /**
     * Constructs a new <code>HardwareComponentGroupList</code>.
     * The collection of hardware component groups.
     * @alias module:model/HardwareComponentGroupList
     * @param value {Array.<module:model/HardwareComponentGroup>} The value.
     */
    constructor(value) { 
        
        HardwareComponentGroupList.initialize(this, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, value) { 
        obj['value'] = value;
    }

    /**
     * Constructs a <code>HardwareComponentGroupList</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HardwareComponentGroupList} obj Optional instance to populate.
     * @return {module:model/HardwareComponentGroupList} The populated <code>HardwareComponentGroupList</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HardwareComponentGroupList();

            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [HardwareComponentGroup]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HardwareComponentGroupList</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HardwareComponentGroupList</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of HardwareComponentGroupList.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                HardwareComponentGroup.validateJSON(item);
            };
        }

        return true;
    }


}

HardwareComponentGroupList.RequiredProperties = ["value"];

/**
 * The value.
 * @member {Array.<module:model/HardwareComponentGroup>} value
 */
HardwareComponentGroupList.prototype['value'] = undefined;






export default HardwareComponentGroupList;

