/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on the ApiVersionSet entity associated with your Azure API Management deployment. Using this entity you create and manage API Version Sets that are used to group APIs for consistent versioning.
 *
 * The version of the OpenAPI document: 2018-01-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ApiVersionSetUpdateParametersProperties from './ApiVersionSetUpdateParametersProperties';

/**
 * The ApiVersionSetUpdateParameters model module.
 * @module model/ApiVersionSetUpdateParameters
 * @version 2018-01-01
 */
class ApiVersionSetUpdateParameters {
    /**
     * Constructs a new <code>ApiVersionSetUpdateParameters</code>.
     * Parameters to update or create an Api Version Set Contract.
     * @alias module:model/ApiVersionSetUpdateParameters
     */
    constructor() { 
        
        ApiVersionSetUpdateParameters.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApiVersionSetUpdateParameters</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiVersionSetUpdateParameters} obj Optional instance to populate.
     * @return {module:model/ApiVersionSetUpdateParameters} The populated <code>ApiVersionSetUpdateParameters</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiVersionSetUpdateParameters();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ApiVersionSetUpdateParametersProperties.constructFromObject(data['properties']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiVersionSetUpdateParameters</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiVersionSetUpdateParameters</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          ApiVersionSetUpdateParametersProperties.validateJSON(data['properties']);
        }

        return true;
    }


}



/**
 * @member {module:model/ApiVersionSetUpdateParametersProperties} properties
 */
ApiVersionSetUpdateParameters.prototype['properties'] = undefined;






export default ApiVersionSetUpdateParameters;

