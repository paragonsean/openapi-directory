/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2019-07-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import RedisResource from './RedisResource';

/**
 * The RedisListResult model module.
 * @module model/RedisListResult
 * @version 2019-07-01
 */
class RedisListResult {
    /**
     * Constructs a new <code>RedisListResult</code>.
     * The response of list Redis operation.
     * @alias module:model/RedisListResult
     */
    constructor() { 
        
        RedisListResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RedisListResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RedisListResult} obj Optional instance to populate.
     * @return {module:model/RedisListResult} The populated <code>RedisListResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RedisListResult();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [RedisResource]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RedisListResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RedisListResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['nextLink'] && !(typeof data['nextLink'] === 'string' || data['nextLink'] instanceof String)) {
            throw new Error("Expected the field `nextLink` to be a primitive type in the JSON string but got " + data['nextLink']);
        }
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                RedisResource.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Link for next page of results.
 * @member {String} nextLink
 */
RedisListResult.prototype['nextLink'] = undefined;

/**
 * List of Redis cache instances.
 * @member {Array.<module:model/RedisResource>} value
 */
RedisListResult.prototype['value'] = undefined;






export default RedisListResult;

