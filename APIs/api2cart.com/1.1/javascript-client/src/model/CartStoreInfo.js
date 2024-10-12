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
import Carrier from './Carrier';
import CartChannel from './CartChannel';
import Currency from './Currency';
import Info from './Info';
import Language from './Language';

/**
 * The CartStoreInfo model module.
 * @module model/CartStoreInfo
 * @version 1.1
 */
class CartStoreInfo {
    /**
     * Constructs a new <code>CartStoreInfo</code>.
     * @alias module:model/CartStoreInfo
     */
    constructor() { 
        
        CartStoreInfo.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CartStoreInfo</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CartStoreInfo} obj Optional instance to populate.
     * @return {module:model/CartStoreInfo} The populated <code>CartStoreInfo</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CartStoreInfo();

            if (data.hasOwnProperty('active')) {
                obj['active'] = ApiClient.convertToType(data['active'], 'Boolean');
            }
            if (data.hasOwnProperty('additional_fields')) {
                obj['additional_fields'] = ApiClient.convertToType(data['additional_fields'], Object);
            }
            if (data.hasOwnProperty('carrier_info')) {
                obj['carrier_info'] = ApiClient.convertToType(data['carrier_info'], [Carrier]);
            }
            if (data.hasOwnProperty('channels')) {
                obj['channels'] = ApiClient.convertToType(data['channels'], [CartChannel]);
            }
            if (data.hasOwnProperty('country')) {
                obj['country'] = ApiClient.convertToType(data['country'], 'String');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = Currency.constructFromObject(data['currency']);
            }
            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], Object);
            }
            if (data.hasOwnProperty('default_warehouse_id')) {
                obj['default_warehouse_id'] = ApiClient.convertToType(data['default_warehouse_id'], 'String');
            }
            if (data.hasOwnProperty('dimension_unit')) {
                obj['dimension_unit'] = ApiClient.convertToType(data['dimension_unit'], 'String');
            }
            if (data.hasOwnProperty('language')) {
                obj['language'] = ApiClient.convertToType(data['language'], 'String');
            }
            if (data.hasOwnProperty('multi_store_url')) {
                obj['multi_store_url'] = ApiClient.convertToType(data['multi_store_url'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('prices_include_tax')) {
                obj['prices_include_tax'] = ApiClient.convertToType(data['prices_include_tax'], 'Boolean');
            }
            if (data.hasOwnProperty('root_category_id')) {
                obj['root_category_id'] = ApiClient.convertToType(data['root_category_id'], 'String');
            }
            if (data.hasOwnProperty('store_currencies')) {
                obj['store_currencies'] = ApiClient.convertToType(data['store_currencies'], [Currency]);
            }
            if (data.hasOwnProperty('store_id')) {
                obj['store_id'] = ApiClient.convertToType(data['store_id'], 'String');
            }
            if (data.hasOwnProperty('store_languages')) {
                obj['store_languages'] = ApiClient.convertToType(data['store_languages'], [Language]);
            }
            if (data.hasOwnProperty('store_owner_info')) {
                obj['store_owner_info'] = Info.constructFromObject(data['store_owner_info']);
            }
            if (data.hasOwnProperty('timezone')) {
                obj['timezone'] = ApiClient.convertToType(data['timezone'], 'String');
            }
            if (data.hasOwnProperty('weight_unit')) {
                obj['weight_unit'] = ApiClient.convertToType(data['weight_unit'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CartStoreInfo</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CartStoreInfo</code>.
     */
    static validateJSON(data) {
        if (data['carrier_info']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['carrier_info'])) {
                throw new Error("Expected the field `carrier_info` to be an array in the JSON data but got " + data['carrier_info']);
            }
            // validate the optional field `carrier_info` (array)
            for (const item of data['carrier_info']) {
                Carrier.validateJSON(item);
            };
        }
        if (data['channels']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['channels'])) {
                throw new Error("Expected the field `channels` to be an array in the JSON data but got " + data['channels']);
            }
            // validate the optional field `channels` (array)
            for (const item of data['channels']) {
                CartChannel.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['country'] && !(typeof data['country'] === 'string' || data['country'] instanceof String)) {
            throw new Error("Expected the field `country` to be a primitive type in the JSON string but got " + data['country']);
        }
        // validate the optional field `currency`
        if (data['currency']) { // data not null
          Currency.validateJSON(data['currency']);
        }
        // ensure the json data is a string
        if (data['default_warehouse_id'] && !(typeof data['default_warehouse_id'] === 'string' || data['default_warehouse_id'] instanceof String)) {
            throw new Error("Expected the field `default_warehouse_id` to be a primitive type in the JSON string but got " + data['default_warehouse_id']);
        }
        // ensure the json data is a string
        if (data['dimension_unit'] && !(typeof data['dimension_unit'] === 'string' || data['dimension_unit'] instanceof String)) {
            throw new Error("Expected the field `dimension_unit` to be a primitive type in the JSON string but got " + data['dimension_unit']);
        }
        // ensure the json data is a string
        if (data['language'] && !(typeof data['language'] === 'string' || data['language'] instanceof String)) {
            throw new Error("Expected the field `language` to be a primitive type in the JSON string but got " + data['language']);
        }
        // ensure the json data is a string
        if (data['multi_store_url'] && !(typeof data['multi_store_url'] === 'string' || data['multi_store_url'] instanceof String)) {
            throw new Error("Expected the field `multi_store_url` to be a primitive type in the JSON string but got " + data['multi_store_url']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['root_category_id'] && !(typeof data['root_category_id'] === 'string' || data['root_category_id'] instanceof String)) {
            throw new Error("Expected the field `root_category_id` to be a primitive type in the JSON string but got " + data['root_category_id']);
        }
        if (data['store_currencies']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['store_currencies'])) {
                throw new Error("Expected the field `store_currencies` to be an array in the JSON data but got " + data['store_currencies']);
            }
            // validate the optional field `store_currencies` (array)
            for (const item of data['store_currencies']) {
                Currency.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['store_id'] && !(typeof data['store_id'] === 'string' || data['store_id'] instanceof String)) {
            throw new Error("Expected the field `store_id` to be a primitive type in the JSON string but got " + data['store_id']);
        }
        if (data['store_languages']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['store_languages'])) {
                throw new Error("Expected the field `store_languages` to be an array in the JSON data but got " + data['store_languages']);
            }
            // validate the optional field `store_languages` (array)
            for (const item of data['store_languages']) {
                Language.validateJSON(item);
            };
        }
        // validate the optional field `store_owner_info`
        if (data['store_owner_info']) { // data not null
          Info.validateJSON(data['store_owner_info']);
        }
        // ensure the json data is a string
        if (data['timezone'] && !(typeof data['timezone'] === 'string' || data['timezone'] instanceof String)) {
            throw new Error("Expected the field `timezone` to be a primitive type in the JSON string but got " + data['timezone']);
        }
        // ensure the json data is a string
        if (data['weight_unit'] && !(typeof data['weight_unit'] === 'string' || data['weight_unit'] instanceof String)) {
            throw new Error("Expected the field `weight_unit` to be a primitive type in the JSON string but got " + data['weight_unit']);
        }

        return true;
    }


}



/**
 * @member {Boolean} active
 */
CartStoreInfo.prototype['active'] = undefined;

/**
 * @member {Object} additional_fields
 */
CartStoreInfo.prototype['additional_fields'] = undefined;

/**
 * @member {Array.<module:model/Carrier>} carrier_info
 */
CartStoreInfo.prototype['carrier_info'] = undefined;

/**
 * @member {Array.<module:model/CartChannel>} channels
 */
CartStoreInfo.prototype['channels'] = undefined;

/**
 * @member {String} country
 */
CartStoreInfo.prototype['country'] = undefined;

/**
 * @member {module:model/Currency} currency
 */
CartStoreInfo.prototype['currency'] = undefined;

/**
 * @member {Object} custom_fields
 */
CartStoreInfo.prototype['custom_fields'] = undefined;

/**
 * @member {String} default_warehouse_id
 */
CartStoreInfo.prototype['default_warehouse_id'] = undefined;

/**
 * @member {String} dimension_unit
 */
CartStoreInfo.prototype['dimension_unit'] = undefined;

/**
 * @member {String} language
 */
CartStoreInfo.prototype['language'] = undefined;

/**
 * @member {String} multi_store_url
 */
CartStoreInfo.prototype['multi_store_url'] = undefined;

/**
 * @member {String} name
 */
CartStoreInfo.prototype['name'] = undefined;

/**
 * @member {Boolean} prices_include_tax
 */
CartStoreInfo.prototype['prices_include_tax'] = undefined;

/**
 * @member {String} root_category_id
 */
CartStoreInfo.prototype['root_category_id'] = undefined;

/**
 * @member {Array.<module:model/Currency>} store_currencies
 */
CartStoreInfo.prototype['store_currencies'] = undefined;

/**
 * @member {String} store_id
 */
CartStoreInfo.prototype['store_id'] = undefined;

/**
 * @member {Array.<module:model/Language>} store_languages
 */
CartStoreInfo.prototype['store_languages'] = undefined;

/**
 * @member {module:model/Info} store_owner_info
 */
CartStoreInfo.prototype['store_owner_info'] = undefined;

/**
 * @member {String} timezone
 */
CartStoreInfo.prototype['timezone'] = undefined;

/**
 * @member {String} weight_unit
 */
CartStoreInfo.prototype['weight_unit'] = undefined;






export default CartStoreInfo;

