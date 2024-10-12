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
import ApiVersionSetContractProperties from './ApiVersionSetContractProperties';

/**
 * The ApiVersionSetContract model module.
 * @module model/ApiVersionSetContract
 * @version 2018-01-01
 */
class ApiVersionSetContract {
    /**
     * Constructs a new <code>ApiVersionSetContract</code>.
     * Api Version Set Contract details.
     * @alias module:model/ApiVersionSetContract
     */
    constructor() { 
        
        ApiVersionSetContract.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApiVersionSetContract</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiVersionSetContract} obj Optional instance to populate.
     * @return {module:model/ApiVersionSetContract} The populated <code>ApiVersionSetContract</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiVersionSetContract();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ApiVersionSetContractProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiVersionSetContract</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiVersionSetContract</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          ApiVersionSetContractProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {module:model/ApiVersionSetContractProperties} properties
 */
ApiVersionSetContract.prototype['properties'] = undefined;

/**
 * Resource ID.
 * @member {String} id
 */
ApiVersionSetContract.prototype['id'] = undefined;

/**
 * Resource name.
 * @member {String} name
 */
ApiVersionSetContract.prototype['name'] = undefined;

/**
 * Resource type for API Management resource.
 * @member {String} type
 */
ApiVersionSetContract.prototype['type'] = undefined;






export default ApiVersionSetContract;

