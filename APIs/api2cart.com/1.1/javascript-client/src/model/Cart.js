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
import CartShippingZone from './CartShippingZone';
import CartStoreInfo from './CartStoreInfo';
import CartWarehouse from './CartWarehouse';

/**
 * The Cart model module.
 * @module model/Cart
 * @version 1.1
 */
class Cart {
    /**
     * Constructs a new <code>Cart</code>.
     * @alias module:model/Cart
     */
    constructor() { 
        
        Cart.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Cart</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Cart} obj Optional instance to populate.
     * @return {module:model/Cart} The populated <code>Cart</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Cart();

            if (data.hasOwnProperty('additional_fields')) {
                obj['additional_fields'] = ApiClient.convertToType(data['additional_fields'], Object);
            }
            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], Object);
            }
            if (data.hasOwnProperty('db_prefix')) {
                obj['db_prefix'] = ApiClient.convertToType(data['db_prefix'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('shipping_zones')) {
                obj['shipping_zones'] = ApiClient.convertToType(data['shipping_zones'], [CartShippingZone]);
            }
            if (data.hasOwnProperty('stores_info')) {
                obj['stores_info'] = ApiClient.convertToType(data['stores_info'], [CartStoreInfo]);
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
            if (data.hasOwnProperty('version')) {
                obj['version'] = ApiClient.convertToType(data['version'], 'String');
            }
            if (data.hasOwnProperty('warehouses')) {
                obj['warehouses'] = ApiClient.convertToType(data['warehouses'], [CartWarehouse]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Cart</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Cart</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['db_prefix'] && !(typeof data['db_prefix'] === 'string' || data['db_prefix'] instanceof String)) {
            throw new Error("Expected the field `db_prefix` to be a primitive type in the JSON string but got " + data['db_prefix']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        if (data['shipping_zones']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['shipping_zones'])) {
                throw new Error("Expected the field `shipping_zones` to be an array in the JSON data but got " + data['shipping_zones']);
            }
            // validate the optional field `shipping_zones` (array)
            for (const item of data['shipping_zones']) {
                CartShippingZone.validateJSON(item);
            };
        }
        if (data['stores_info']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['stores_info'])) {
                throw new Error("Expected the field `stores_info` to be an array in the JSON data but got " + data['stores_info']);
            }
            // validate the optional field `stores_info` (array)
            for (const item of data['stores_info']) {
                CartStoreInfo.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }
        // ensure the json data is a string
        if (data['version'] && !(typeof data['version'] === 'string' || data['version'] instanceof String)) {
            throw new Error("Expected the field `version` to be a primitive type in the JSON string but got " + data['version']);
        }
        if (data['warehouses']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['warehouses'])) {
                throw new Error("Expected the field `warehouses` to be an array in the JSON data but got " + data['warehouses']);
            }
            // validate the optional field `warehouses` (array)
            for (const item of data['warehouses']) {
                CartWarehouse.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Object} additional_fields
 */
Cart.prototype['additional_fields'] = undefined;

/**
 * @member {Object} custom_fields
 */
Cart.prototype['custom_fields'] = undefined;

/**
 * @member {String} db_prefix
 */
Cart.prototype['db_prefix'] = undefined;

/**
 * @member {String} name
 */
Cart.prototype['name'] = undefined;

/**
 * @member {Array.<module:model/CartShippingZone>} shipping_zones
 */
Cart.prototype['shipping_zones'] = undefined;

/**
 * @member {Array.<module:model/CartStoreInfo>} stores_info
 */
Cart.prototype['stores_info'] = undefined;

/**
 * @member {String} url
 */
Cart.prototype['url'] = undefined;

/**
 * @member {String} version
 */
Cart.prototype['version'] = undefined;

/**
 * @member {Array.<module:model/CartWarehouse>} warehouses
 */
Cart.prototype['warehouses'] = undefined;






export default Cart;

