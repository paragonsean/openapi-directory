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
import Customer from './Customer';

/**
 * The ResponseCustomerListResult model module.
 * @module model/ResponseCustomerListResult
 * @version 1.1
 */
class ResponseCustomerListResult {
    /**
     * Constructs a new <code>ResponseCustomerListResult</code>.
     * @alias module:model/ResponseCustomerListResult
     */
    constructor() { 
        
        ResponseCustomerListResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ResponseCustomerListResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ResponseCustomerListResult} obj Optional instance to populate.
     * @return {module:model/ResponseCustomerListResult} The populated <code>ResponseCustomerListResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ResponseCustomerListResult();

            if (data.hasOwnProperty('additional_fields')) {
                obj['additional_fields'] = ApiClient.convertToType(data['additional_fields'], Object);
            }
            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], Object);
            }
            if (data.hasOwnProperty('customer')) {
                obj['customer'] = ApiClient.convertToType(data['customer'], [Customer]);
            }
            if (data.hasOwnProperty('customers_count')) {
                obj['customers_count'] = ApiClient.convertToType(data['customers_count'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ResponseCustomerListResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ResponseCustomerListResult</code>.
     */
    static validateJSON(data) {
        if (data['customer']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['customer'])) {
                throw new Error("Expected the field `customer` to be an array in the JSON data but got " + data['customer']);
            }
            // validate the optional field `customer` (array)
            for (const item of data['customer']) {
                Customer.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Object} additional_fields
 */
ResponseCustomerListResult.prototype['additional_fields'] = undefined;

/**
 * @member {Object} custom_fields
 */
ResponseCustomerListResult.prototype['custom_fields'] = undefined;

/**
 * @member {Array.<module:model/Customer>} customer
 */
ResponseCustomerListResult.prototype['customer'] = undefined;

/**
 * @member {Number} customers_count
 */
ResponseCustomerListResult.prototype['customers_count'] = undefined;






export default ResponseCustomerListResult;

