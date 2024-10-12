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
import PluginList from './PluginList';

/**
 * The CartPluginList200ResponseResult model module.
 * @module model/CartPluginList200ResponseResult
 * @version 1.1
 */
class CartPluginList200ResponseResult {
    /**
     * Constructs a new <code>CartPluginList200ResponseResult</code>.
     * @alias module:model/CartPluginList200ResponseResult
     */
    constructor() { 
        
        CartPluginList200ResponseResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CartPluginList200ResponseResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CartPluginList200ResponseResult} obj Optional instance to populate.
     * @return {module:model/CartPluginList200ResponseResult} The populated <code>CartPluginList200ResponseResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CartPluginList200ResponseResult();

            if (data.hasOwnProperty('all_plugins')) {
                obj['all_plugins'] = ApiClient.convertToType(data['all_plugins'], 'Number');
            }
            if (data.hasOwnProperty('plugins')) {
                obj['plugins'] = ApiClient.convertToType(data['plugins'], [PluginList]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CartPluginList200ResponseResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CartPluginList200ResponseResult</code>.
     */
    static validateJSON(data) {
        if (data['plugins']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['plugins'])) {
                throw new Error("Expected the field `plugins` to be an array in the JSON data but got " + data['plugins']);
            }
            // validate the optional field `plugins` (array)
            for (const item of data['plugins']) {
                PluginList.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Number} all_plugins
 */
CartPluginList200ResponseResult.prototype['all_plugins'] = undefined;

/**
 * @member {Array.<module:model/PluginList>} plugins
 */
CartPluginList200ResponseResult.prototype['plugins'] = undefined;






export default CartPluginList200ResponseResult;

