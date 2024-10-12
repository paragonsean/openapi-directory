/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2020-01-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import FrontendEndpoint from './FrontendEndpoint';

/**
 * The FrontendEndpointsListResult model module.
 * @module model/FrontendEndpointsListResult
 * @version 2020-01-01
 */
class FrontendEndpointsListResult {
    /**
     * Constructs a new <code>FrontendEndpointsListResult</code>.
     * Result of the request to list frontend endpoints. It contains a list of Frontend endpoint objects and a URL link to get the next set of results.
     * @alias module:model/FrontendEndpointsListResult
     */
    constructor() { 
        
        FrontendEndpointsListResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FrontendEndpointsListResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FrontendEndpointsListResult} obj Optional instance to populate.
     * @return {module:model/FrontendEndpointsListResult} The populated <code>FrontendEndpointsListResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FrontendEndpointsListResult();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [FrontendEndpoint]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FrontendEndpointsListResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FrontendEndpointsListResult</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['nextLink'] && !(typeof data['nextLink'] === 'string' || data['nextLink'] instanceof String)) {
            throw new Error("Expected the field `nextLink` to be a primitive type in the JSON string but got " + data['nextLink']);
        }
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                FrontendEndpoint.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * URL to get the next set of frontend endpoints if there are any.
 * @member {String} nextLink
 */
FrontendEndpointsListResult.prototype['nextLink'] = undefined;

/**
 * List of Frontend endpoints within a Front Door.
 * @member {Array.<module:model/FrontendEndpoint>} value
 */
FrontendEndpointsListResult.prototype['value'] = undefined;






export default FrontendEndpointsListResult;

