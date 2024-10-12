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
import Product from './Product';

/**
 * The ProductVariantList200ResponseResult model module.
 * @module model/ProductVariantList200ResponseResult
 * @version 1.1
 */
class ProductVariantList200ResponseResult {
    /**
     * Constructs a new <code>ProductVariantList200ResponseResult</code>.
     * @alias module:model/ProductVariantList200ResponseResult
     */
    constructor() { 
        
        ProductVariantList200ResponseResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProductVariantList200ResponseResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProductVariantList200ResponseResult} obj Optional instance to populate.
     * @return {module:model/ProductVariantList200ResponseResult} The populated <code>ProductVariantList200ResponseResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProductVariantList200ResponseResult();

            if (data.hasOwnProperty('variant')) {
                obj['variant'] = ApiClient.convertToType(data['variant'], [Product]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProductVariantList200ResponseResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProductVariantList200ResponseResult</code>.
     */
    static validateJSON(data) {
        if (data['variant']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['variant'])) {
                throw new Error("Expected the field `variant` to be an array in the JSON data but got " + data['variant']);
            }
            // validate the optional field `variant` (array)
            for (const item of data['variant']) {
                Product.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Product>} variant
 */
ProductVariantList200ResponseResult.prototype['variant'] = undefined;






export default ProductVariantList200ResponseResult;

