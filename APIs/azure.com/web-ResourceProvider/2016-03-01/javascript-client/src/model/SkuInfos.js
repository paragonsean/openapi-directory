/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-03-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import GlobalCsmSkuDescription from './GlobalCsmSkuDescription';

/**
 * The SkuInfos model module.
 * @module model/SkuInfos
 * @version 2016-03-01
 */
class SkuInfos {
    /**
     * Constructs a new <code>SkuInfos</code>.
     * Collection of SKU information.
     * @alias module:model/SkuInfos
     */
    constructor() { 
        
        SkuInfos.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SkuInfos</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SkuInfos} obj Optional instance to populate.
     * @return {module:model/SkuInfos} The populated <code>SkuInfos</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SkuInfos();

            if (data.hasOwnProperty('resourceType')) {
                obj['resourceType'] = ApiClient.convertToType(data['resourceType'], 'String');
            }
            if (data.hasOwnProperty('skus')) {
                obj['skus'] = ApiClient.convertToType(data['skus'], [GlobalCsmSkuDescription]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SkuInfos</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SkuInfos</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['resourceType'] && !(typeof data['resourceType'] === 'string' || data['resourceType'] instanceof String)) {
            throw new Error("Expected the field `resourceType` to be a primitive type in the JSON string but got " + data['resourceType']);
        }
        if (data['skus']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['skus'])) {
                throw new Error("Expected the field `skus` to be an array in the JSON data but got " + data['skus']);
            }
            // validate the optional field `skus` (array)
            for (const item of data['skus']) {
                GlobalCsmSkuDescription.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Resource type that this SKU applies to.
 * @member {String} resourceType
 */
SkuInfos.prototype['resourceType'] = undefined;

/**
 * List of SKUs the subscription is able to use.
 * @member {Array.<module:model/GlobalCsmSkuDescription>} skus
 */
SkuInfos.prototype['skus'] = undefined;






export default SkuInfos;

