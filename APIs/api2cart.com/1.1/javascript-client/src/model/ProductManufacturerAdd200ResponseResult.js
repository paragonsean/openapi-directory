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
 * The ProductManufacturerAdd200ResponseResult model module.
 * @module model/ProductManufacturerAdd200ResponseResult
 * @version 1.1
 */
class ProductManufacturerAdd200ResponseResult {
    /**
     * Constructs a new <code>ProductManufacturerAdd200ResponseResult</code>.
     * @alias module:model/ProductManufacturerAdd200ResponseResult
     */
    constructor() { 
        
        ProductManufacturerAdd200ResponseResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProductManufacturerAdd200ResponseResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProductManufacturerAdd200ResponseResult} obj Optional instance to populate.
     * @return {module:model/ProductManufacturerAdd200ResponseResult} The populated <code>ProductManufacturerAdd200ResponseResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProductManufacturerAdd200ResponseResult();

            if (data.hasOwnProperty('manufacturer_id')) {
                obj['manufacturer_id'] = ApiClient.convertToType(data['manufacturer_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProductManufacturerAdd200ResponseResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProductManufacturerAdd200ResponseResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['manufacturer_id'] && !(typeof data['manufacturer_id'] === 'string' || data['manufacturer_id'] instanceof String)) {
            throw new Error("Expected the field `manufacturer_id` to be a primitive type in the JSON string but got " + data['manufacturer_id']);
        }

        return true;
    }


}



/**
 * @member {String} manufacturer_id
 */
ProductManufacturerAdd200ResponseResult.prototype['manufacturer_id'] = undefined;






export default ProductManufacturerAdd200ResponseResult;

