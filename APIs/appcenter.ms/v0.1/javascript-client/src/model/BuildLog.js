/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The BuildLog model module.
 * @module model/BuildLog
 * @version v0.1
 */
class BuildLog {
    /**
     * Constructs a new <code>BuildLog</code>.
     * @alias module:model/BuildLog
     */
    constructor() { 
        
        BuildLog.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BuildLog</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BuildLog} obj Optional instance to populate.
     * @return {module:model/BuildLog} The populated <code>BuildLog</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BuildLog();

            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BuildLog</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BuildLog</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['value'])) {
            throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
        }

        return true;
    }


}



/**
 * @member {Array.<String>} value
 */
BuildLog.prototype['value'] = undefined;






export default BuildLog;

