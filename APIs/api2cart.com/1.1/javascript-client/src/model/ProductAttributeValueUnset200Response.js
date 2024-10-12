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
import ProductAttributeValueUnset200ResponseResult from './ProductAttributeValueUnset200ResponseResult';

/**
 * The ProductAttributeValueUnset200Response model module.
 * @module model/ProductAttributeValueUnset200Response
 * @version 1.1
 */
class ProductAttributeValueUnset200Response {
    /**
     * Constructs a new <code>ProductAttributeValueUnset200Response</code>.
     * @alias module:model/ProductAttributeValueUnset200Response
     */
    constructor() { 
        
        ProductAttributeValueUnset200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProductAttributeValueUnset200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProductAttributeValueUnset200Response} obj Optional instance to populate.
     * @return {module:model/ProductAttributeValueUnset200Response} The populated <code>ProductAttributeValueUnset200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProductAttributeValueUnset200Response();

            if (data.hasOwnProperty('result')) {
                obj['result'] = ProductAttributeValueUnset200ResponseResult.constructFromObject(data['result']);
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
     * Validates the JSON data with respect to <code>ProductAttributeValueUnset200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProductAttributeValueUnset200Response</code>.
     */
    static validateJSON(data) {
        // validate the optional field `result`
        if (data['result']) { // data not null
          ProductAttributeValueUnset200ResponseResult.validateJSON(data['result']);
        }
        // ensure the json data is a string
        if (data['return_message'] && !(typeof data['return_message'] === 'string' || data['return_message'] instanceof String)) {
            throw new Error("Expected the field `return_message` to be a primitive type in the JSON string but got " + data['return_message']);
        }

        return true;
    }


}



/**
 * @member {module:model/ProductAttributeValueUnset200ResponseResult} result
 */
ProductAttributeValueUnset200Response.prototype['result'] = undefined;

/**
 * @member {Number} return_code
 */
ProductAttributeValueUnset200Response.prototype['return_code'] = undefined;

/**
 * @member {String} return_message
 */
ProductAttributeValueUnset200Response.prototype['return_message'] = undefined;






export default ProductAttributeValueUnset200Response;

