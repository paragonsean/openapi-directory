/**
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import FilterProducts from './FilterProducts';

/**
 * The FilterSums model module.
 * @module model/FilterSums
 * @version 1.0
 */
class FilterSums {
    /**
     * Constructs a new <code>FilterSums</code>.
     * @alias module:model/FilterSums
     */
    constructor() { 
        
        FilterSums.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FilterSums</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FilterSums} obj Optional instance to populate.
     * @return {module:model/FilterSums} The populated <code>FilterSums</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FilterSums();

            if (data.hasOwnProperty('or')) {
                obj['or'] = ApiClient.convertToType(data['or'], [FilterProducts]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FilterSums</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FilterSums</code>.
     */
    static validateJSON(data) {
        if (data['or']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['or'])) {
                throw new Error("Expected the field `or` to be an array in the JSON data but got " + data['or']);
            }
            // validate the optional field `or` (array)
            for (const item of data['or']) {
                FilterProducts.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * An array of changelog filters that will be joined via logical OR.
 * @member {Array.<module:model/FilterProducts>} or
 */
FilterSums.prototype['or'] = undefined;






export default FilterSums;

