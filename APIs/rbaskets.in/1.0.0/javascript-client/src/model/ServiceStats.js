/**
 * Request Baskets API
 * RESTful API of [Request Baskets](https://rbaskets.in) service.  Request Baskets is an open source project of a service to collect HTTP requests and inspect them via RESTful API or web UI.  Check out the [project page](https://github.com/darklynx/request-baskets) for more detailed description. 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BasketInfo from './BasketInfo';

/**
 * The ServiceStats model module.
 * @module model/ServiceStats
 * @version 1.0.0
 */
class ServiceStats {
    /**
     * Constructs a new <code>ServiceStats</code>.
     * @alias module:model/ServiceStats
     */
    constructor() { 
        
        ServiceStats.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ServiceStats</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ServiceStats} obj Optional instance to populate.
     * @return {module:model/ServiceStats} The populated <code>ServiceStats</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ServiceStats();

            if (data.hasOwnProperty('avg_basket_size')) {
                obj['avg_basket_size'] = ApiClient.convertToType(data['avg_basket_size'], 'Number');
            }
            if (data.hasOwnProperty('baskets_count')) {
                obj['baskets_count'] = ApiClient.convertToType(data['baskets_count'], 'Number');
            }
            if (data.hasOwnProperty('empty_baskets_count')) {
                obj['empty_baskets_count'] = ApiClient.convertToType(data['empty_baskets_count'], 'Number');
            }
            if (data.hasOwnProperty('max_basket_size')) {
                obj['max_basket_size'] = ApiClient.convertToType(data['max_basket_size'], 'Number');
            }
            if (data.hasOwnProperty('requests_count')) {
                obj['requests_count'] = ApiClient.convertToType(data['requests_count'], 'Number');
            }
            if (data.hasOwnProperty('requests_total_count')) {
                obj['requests_total_count'] = ApiClient.convertToType(data['requests_total_count'], 'Number');
            }
            if (data.hasOwnProperty('top_baskets_recent')) {
                obj['top_baskets_recent'] = ApiClient.convertToType(data['top_baskets_recent'], [BasketInfo]);
            }
            if (data.hasOwnProperty('top_baskets_size')) {
                obj['top_baskets_size'] = ApiClient.convertToType(data['top_baskets_size'], [BasketInfo]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ServiceStats</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ServiceStats</code>.
     */
    static validateJSON(data) {
        if (data['top_baskets_recent']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['top_baskets_recent'])) {
                throw new Error("Expected the field `top_baskets_recent` to be an array in the JSON data but got " + data['top_baskets_recent']);
            }
            // validate the optional field `top_baskets_recent` (array)
            for (const item of data['top_baskets_recent']) {
                BasketInfo.validateJSON(item);
            };
        }
        if (data['top_baskets_size']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['top_baskets_size'])) {
                throw new Error("Expected the field `top_baskets_size` to be an array in the JSON data but got " + data['top_baskets_size']);
            }
            // validate the optional field `top_baskets_size` (array)
            for (const item of data['top_baskets_size']) {
                BasketInfo.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Average size of a basket in the system, empty baskets are not taken into account
 * @member {Number} avg_basket_size
 */
ServiceStats.prototype['avg_basket_size'] = undefined;

/**
 * Total number of baskets managed by service
 * @member {Number} baskets_count
 */
ServiceStats.prototype['baskets_count'] = undefined;

/**
 * Number of empty baskets
 * @member {Number} empty_baskets_count
 */
ServiceStats.prototype['empty_baskets_count'] = undefined;

/**
 * Size of the biggest basket that processed the top most number of HTTP requests
 * @member {Number} max_basket_size
 */
ServiceStats.prototype['max_basket_size'] = undefined;

/**
 * Number of HTTP requests currently stored by service
 * @member {Number} requests_count
 */
ServiceStats.prototype['requests_count'] = undefined;

/**
 * Total number of HTTP requests processed by service
 * @member {Number} requests_total_count
 */
ServiceStats.prototype['requests_total_count'] = undefined;

/**
 * Collection of top baskets recently active
 * @member {Array.<module:model/BasketInfo>} top_baskets_recent
 */
ServiceStats.prototype['top_baskets_recent'] = undefined;

/**
 * Collection of top basket by size
 * @member {Array.<module:model/BasketInfo>} top_baskets_size
 */
ServiceStats.prototype['top_baskets_size'] = undefined;






export default ServiceStats;

