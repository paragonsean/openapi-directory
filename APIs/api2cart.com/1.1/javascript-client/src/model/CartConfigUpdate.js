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

/**
 * The CartConfigUpdate model module.
 * @module model/CartConfigUpdate
 * @version 1.1
 */
class CartConfigUpdate {
    /**
     * Constructs a new <code>CartConfigUpdate</code>.
     * @alias module:model/CartConfigUpdate
     */
    constructor() { 
        
        CartConfigUpdate.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CartConfigUpdate</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CartConfigUpdate} obj Optional instance to populate.
     * @return {module:model/CartConfigUpdate} The populated <code>CartConfigUpdate</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CartConfigUpdate();

            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], Object);
            }
            if (data.hasOwnProperty('db_tables_prefix')) {
                obj['db_tables_prefix'] = ApiClient.convertToType(data['db_tables_prefix'], 'String');
            }
            if (data.hasOwnProperty('store_id')) {
                obj['store_id'] = ApiClient.convertToType(data['store_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CartConfigUpdate</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CartConfigUpdate</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['db_tables_prefix'] && !(typeof data['db_tables_prefix'] === 'string' || data['db_tables_prefix'] instanceof String)) {
            throw new Error("Expected the field `db_tables_prefix` to be a primitive type in the JSON string but got " + data['db_tables_prefix']);
        }
        // ensure the json data is a string
        if (data['store_id'] && !(typeof data['store_id'] === 'string' || data['store_id'] instanceof String)) {
            throw new Error("Expected the field `store_id` to be a primitive type in the JSON string but got " + data['store_id']);
        }

        return true;
    }


}



/**
 * This parameter sets the list of params to the shopping cart.
 * @member {Object} custom_fields
 */
CartConfigUpdate.prototype['custom_fields'] = undefined;

/**
 * This parameter is deprecated for this method. Please, use this parameter in method account.config.update
 * @member {String} db_tables_prefix
 */
CartConfigUpdate.prototype['db_tables_prefix'] = undefined;

/**
 * Store Id
 * @member {String} store_id
 */
CartConfigUpdate.prototype['store_id'] = undefined;






export default CartConfigUpdate;

