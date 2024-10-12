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
import OrderPreestimateShipping from './OrderPreestimateShipping';

/**
 * The ResponseOrderPreestimateShippingListResult model module.
 * @module model/ResponseOrderPreestimateShippingListResult
 * @version 1.1
 */
class ResponseOrderPreestimateShippingListResult {
    /**
     * Constructs a new <code>ResponseOrderPreestimateShippingListResult</code>.
     * @alias module:model/ResponseOrderPreestimateShippingListResult
     */
    constructor() { 
        
        ResponseOrderPreestimateShippingListResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ResponseOrderPreestimateShippingListResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ResponseOrderPreestimateShippingListResult} obj Optional instance to populate.
     * @return {module:model/ResponseOrderPreestimateShippingListResult} The populated <code>ResponseOrderPreestimateShippingListResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ResponseOrderPreestimateShippingListResult();

            if (data.hasOwnProperty('additional_fields')) {
                obj['additional_fields'] = ApiClient.convertToType(data['additional_fields'], Object);
            }
            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], Object);
            }
            if (data.hasOwnProperty('preestimate_shippings')) {
                obj['preestimate_shippings'] = ApiClient.convertToType(data['preestimate_shippings'], [OrderPreestimateShipping]);
            }
            if (data.hasOwnProperty('preestimate_shippings_count')) {
                obj['preestimate_shippings_count'] = ApiClient.convertToType(data['preestimate_shippings_count'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ResponseOrderPreestimateShippingListResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ResponseOrderPreestimateShippingListResult</code>.
     */
    static validateJSON(data) {
        if (data['preestimate_shippings']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['preestimate_shippings'])) {
                throw new Error("Expected the field `preestimate_shippings` to be an array in the JSON data but got " + data['preestimate_shippings']);
            }
            // validate the optional field `preestimate_shippings` (array)
            for (const item of data['preestimate_shippings']) {
                OrderPreestimateShipping.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Object} additional_fields
 */
ResponseOrderPreestimateShippingListResult.prototype['additional_fields'] = undefined;

/**
 * @member {Object} custom_fields
 */
ResponseOrderPreestimateShippingListResult.prototype['custom_fields'] = undefined;

/**
 * @member {Array.<module:model/OrderPreestimateShipping>} preestimate_shippings
 */
ResponseOrderPreestimateShippingListResult.prototype['preestimate_shippings'] = undefined;

/**
 * @member {Number} preestimate_shippings_count
 */
ResponseOrderPreestimateShippingListResult.prototype['preestimate_shippings_count'] = undefined;






export default ResponseOrderPreestimateShippingListResult;

