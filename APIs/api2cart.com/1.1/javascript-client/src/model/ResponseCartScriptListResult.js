/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Script from './Script';

/**
 * The ResponseCartScriptListResult model module.
 * @module model/ResponseCartScriptListResult
 * @version 1.1
 */
class ResponseCartScriptListResult {
    /**
     * Constructs a new <code>ResponseCartScriptListResult</code>.
     * @alias module:model/ResponseCartScriptListResult
     */
    constructor() { 
        
        ResponseCartScriptListResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ResponseCartScriptListResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ResponseCartScriptListResult} obj Optional instance to populate.
     * @return {module:model/ResponseCartScriptListResult} The populated <code>ResponseCartScriptListResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ResponseCartScriptListResult();

            if (data.hasOwnProperty('additional_fields')) {
                obj['additional_fields'] = ApiClient.convertToType(data['additional_fields'], Object);
            }
            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], Object);
            }
            if (data.hasOwnProperty('scripts')) {
                obj['scripts'] = ApiClient.convertToType(data['scripts'], [Script]);
            }
            if (data.hasOwnProperty('total_count')) {
                obj['total_count'] = ApiClient.convertToType(data['total_count'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ResponseCartScriptListResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ResponseCartScriptListResult</code>.
     */
    static validateJSON(data) {
        if (data['scripts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['scripts'])) {
                throw new Error("Expected the field `scripts` to be an array in the JSON data but got " + data['scripts']);
            }
            // validate the optional field `scripts` (array)
            for (const item of data['scripts']) {
                Script.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Object} additional_fields
 */
ResponseCartScriptListResult.prototype['additional_fields'] = undefined;

/**
 * @member {Object} custom_fields
 */
ResponseCartScriptListResult.prototype['custom_fields'] = undefined;

/**
 * @member {Array.<module:model/Script>} scripts
 */
ResponseCartScriptListResult.prototype['scripts'] = undefined;

/**
 * @member {Number} total_count
 */
ResponseCartScriptListResult.prototype['total_count'] = undefined;






export default ResponseCartScriptListResult;

