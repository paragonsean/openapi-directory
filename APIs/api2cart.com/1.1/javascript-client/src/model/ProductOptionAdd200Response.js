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
import ProductOptionAdd200ResponseResult from './ProductOptionAdd200ResponseResult';

/**
 * The ProductOptionAdd200Response model module.
 * @module model/ProductOptionAdd200Response
 * @version 1.1
 */
class ProductOptionAdd200Response {
    /**
     * Constructs a new <code>ProductOptionAdd200Response</code>.
     * @alias module:model/ProductOptionAdd200Response
     */
    constructor() { 
        
        ProductOptionAdd200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProductOptionAdd200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProductOptionAdd200Response} obj Optional instance to populate.
     * @return {module:model/ProductOptionAdd200Response} The populated <code>ProductOptionAdd200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProductOptionAdd200Response();

            if (data.hasOwnProperty('result')) {
                obj['result'] = ProductOptionAdd200ResponseResult.constructFromObject(data['result']);
            }
            if (data.hasOwnProperty('return_code')) {
                obj['return_code'] = ApiClient.convertToType(data['return_code'], 'Number');
            }
            if (data.hasOwnProperty('return_message')) {
                obj['return_message'] = ApiClient.convertToType(data['return_message'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProductOptionAdd200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProductOptionAdd200Response</code>.
     */
    static validateJSON(data) {
        // validate the optional field `result`
        if (data['result']) { // data not null
          ProductOptionAdd200ResponseResult.validateJSON(data['result']);
        }
        // ensure the json data is a string
        if (data['return_message'] && !(typeof data['return_message'] === 'string' || data['return_message'] instanceof String)) {
            throw new Error("Expected the field `return_message` to be a primitive type in the JSON string but got " + data['return_message']);
        }

        return true;
    }


}



/**
 * @member {module:model/ProductOptionAdd200ResponseResult} result
 */
ProductOptionAdd200Response.prototype['result'] = undefined;

/**
 * @member {Number} return_code
 */
ProductOptionAdd200Response.prototype['return_code'] = undefined;

/**
 * @member {String} return_message
 */
ProductOptionAdd200Response.prototype['return_message'] = undefined;






export default ProductOptionAdd200Response;

