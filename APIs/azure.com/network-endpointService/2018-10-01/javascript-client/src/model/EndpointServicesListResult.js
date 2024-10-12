/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-10-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import EndpointServiceResult from './EndpointServiceResult';

/**
 * The EndpointServicesListResult model module.
 * @module model/EndpointServicesListResult
 * @version 2018-10-01
 */
class EndpointServicesListResult {
    /**
     * Constructs a new <code>EndpointServicesListResult</code>.
     * Response for the ListAvailableEndpointServices API service call.
     * @alias module:model/EndpointServicesListResult
     */
    constructor() { 
        
        EndpointServicesListResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EndpointServicesListResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EndpointServicesListResult} obj Optional instance to populate.
     * @return {module:model/EndpointServicesListResult} The populated <code>EndpointServicesListResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EndpointServicesListResult();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [EndpointServiceResult]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EndpointServicesListResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EndpointServicesListResult</code>.
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
                EndpointServiceResult.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * The URL to get the next set of results.
 * @member {String} nextLink
 */
EndpointServicesListResult.prototype['nextLink'] = undefined;

/**
 * List of available endpoint services in a region.
 * @member {Array.<module:model/EndpointServiceResult>} value
 */
EndpointServicesListResult.prototype['value'] = undefined;






export default EndpointServicesListResult;

