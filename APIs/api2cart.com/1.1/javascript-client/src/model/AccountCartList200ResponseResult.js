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
import AccountCartList200ResponseResultCartsInner from './AccountCartList200ResponseResultCartsInner';

/**
 * The AccountCartList200ResponseResult model module.
 * @module model/AccountCartList200ResponseResult
 * @version 1.1
 */
class AccountCartList200ResponseResult {
    /**
     * Constructs a new <code>AccountCartList200ResponseResult</code>.
     * @alias module:model/AccountCartList200ResponseResult
     */
    constructor() { 
        
        AccountCartList200ResponseResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AccountCartList200ResponseResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccountCartList200ResponseResult} obj Optional instance to populate.
     * @return {module:model/AccountCartList200ResponseResult} The populated <code>AccountCartList200ResponseResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccountCartList200ResponseResult();

            if (data.hasOwnProperty('carts')) {
                obj['carts'] = ApiClient.convertToType(data['carts'], [AccountCartList200ResponseResultCartsInner]);
            }
            if (data.hasOwnProperty('carts_count')) {
                obj['carts_count'] = ApiClient.convertToType(data['carts_count'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccountCartList200ResponseResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccountCartList200ResponseResult</code>.
     */
    static validateJSON(data) {
        if (data['carts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['carts'])) {
                throw new Error("Expected the field `carts` to be an array in the JSON data but got " + data['carts']);
            }
            // validate the optional field `carts` (array)
            for (const item of data['carts']) {
                AccountCartList200ResponseResultCartsInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/AccountCartList200ResponseResultCartsInner>} carts
 */
AccountCartList200ResponseResult.prototype['carts'] = undefined;

/**
 * @member {Number} carts_count
 */
AccountCartList200ResponseResult.prototype['carts_count'] = undefined;






export default AccountCartList200ResponseResult;

