/**
 * Hotel Search API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 3.0.8
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Method from './Method';

/**
 * The HotelProductPaymentPolicy model module.
 * @module model/HotelProductPaymentPolicy
 * @version 3.0.8
 */
class HotelProductPaymentPolicy {
    /**
     * Constructs a new <code>HotelProductPaymentPolicy</code>.
     * Accepted Payment Methods and Card Types. Several Payment Methods and Card Types may be available.
     * @alias module:model/HotelProductPaymentPolicy
     */
    constructor() { 
        
        HotelProductPaymentPolicy.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>HotelProductPaymentPolicy</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HotelProductPaymentPolicy} obj Optional instance to populate.
     * @return {module:model/HotelProductPaymentPolicy} The populated <code>HotelProductPaymentPolicy</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HotelProductPaymentPolicy();

            if (data.hasOwnProperty('creditCards')) {
                obj['creditCards'] = ApiClient.convertToType(data['creditCards'], ['String']);
            }
            if (data.hasOwnProperty('methods')) {
                obj['methods'] = ApiClient.convertToType(data['methods'], [Method]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HotelProductPaymentPolicy</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HotelProductPaymentPolicy</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['creditCards'])) {
            throw new Error("Expected the field `creditCards` to be an array in the JSON data but got " + data['creditCards']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['methods'])) {
            throw new Error("Expected the field `methods` to be an array in the JSON data but got " + data['methods']);
        }

        return true;
    }


}



/**
 * Accepted Payment Card Types for the `method` CREDIT_CARD
 * @member {Array.<String>} creditCards
 */
HotelProductPaymentPolicy.prototype['creditCards'] = undefined;

/**
 * Accepted Payment Methods
 * @member {Array.<module:model/Method>} methods
 */
HotelProductPaymentPolicy.prototype['methods'] = undefined;






export default HotelProductPaymentPolicy;

