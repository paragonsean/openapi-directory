/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GlobalCsmSkuDescriptionCapacity model module.
 * @module model/GlobalCsmSkuDescriptionCapacity
 * @version 2018-02-01
 */
class GlobalCsmSkuDescriptionCapacity {
    /**
     * Constructs a new <code>GlobalCsmSkuDescriptionCapacity</code>.
     * Description of the App Service plan scale options.
     * @alias module:model/GlobalCsmSkuDescriptionCapacity
     */
    constructor() { 
        
        GlobalCsmSkuDescriptionCapacity.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GlobalCsmSkuDescriptionCapacity</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GlobalCsmSkuDescriptionCapacity} obj Optional instance to populate.
     * @return {module:model/GlobalCsmSkuDescriptionCapacity} The populated <code>GlobalCsmSkuDescriptionCapacity</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GlobalCsmSkuDescriptionCapacity();

            if (data.hasOwnProperty('default')) {
                obj['default'] = ApiClient.convertToType(data['default'], 'Number');
            }
            if (data.hasOwnProperty('maximum')) {
                obj['maximum'] = ApiClient.convertToType(data['maximum'], 'Number');
            }
            if (data.hasOwnProperty('minimum')) {
                obj['minimum'] = ApiClient.convertToType(data['minimum'], 'Number');
            }
            if (data.hasOwnProperty('scaleType')) {
                obj['scaleType'] = ApiClient.convertToType(data['scaleType'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GlobalCsmSkuDescriptionCapacity</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GlobalCsmSkuDescriptionCapacity</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['scaleType'] && !(typeof data['scaleType'] === 'string' || data['scaleType'] instanceof String)) {
            throw new Error("Expected the field `scaleType` to be a primitive type in the JSON string but got " + data['scaleType']);
        }

        return true;
    }


}



/**
 * Default number of workers for this App Service plan SKU.
 * @member {Number} default
 */
GlobalCsmSkuDescriptionCapacity.prototype['default'] = undefined;

/**
 * Maximum number of workers for this App Service plan SKU.
 * @member {Number} maximum
 */
GlobalCsmSkuDescriptionCapacity.prototype['maximum'] = undefined;

/**
 * Minimum number of workers for this App Service plan SKU.
 * @member {Number} minimum
 */
GlobalCsmSkuDescriptionCapacity.prototype['minimum'] = undefined;

/**
 * Available scale configurations for an App Service plan.
 * @member {String} scaleType
 */
GlobalCsmSkuDescriptionCapacity.prototype['scaleType'] = undefined;






export default GlobalCsmSkuDescriptionCapacity;

