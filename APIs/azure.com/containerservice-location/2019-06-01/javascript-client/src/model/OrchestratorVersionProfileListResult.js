/**
 * ContainerServiceClient
 * The Container Service Client.
 *
 * The version of the OpenAPI document: 2019-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import OrchestratorVersionProfileProperties from './OrchestratorVersionProfileProperties';

/**
 * The OrchestratorVersionProfileListResult model module.
 * @module model/OrchestratorVersionProfileListResult
 * @version 2019-06-01
 */
class OrchestratorVersionProfileListResult {
    /**
     * Constructs a new <code>OrchestratorVersionProfileListResult</code>.
     * The list of versions for supported orchestrators.
     * @alias module:model/OrchestratorVersionProfileListResult
     * @param properties {module:model/OrchestratorVersionProfileProperties} 
     */
    constructor(properties) { 
        
        OrchestratorVersionProfileListResult.initialize(this, properties);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, properties) { 
        obj['properties'] = properties;
    }

    /**
     * Constructs a <code>OrchestratorVersionProfileListResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrchestratorVersionProfileListResult} obj Optional instance to populate.
     * @return {module:model/OrchestratorVersionProfileListResult} The populated <code>OrchestratorVersionProfileListResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrchestratorVersionProfileListResult();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = OrchestratorVersionProfileProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrchestratorVersionProfileListResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrchestratorVersionProfileListResult</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OrchestratorVersionProfileListResult.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          OrchestratorVersionProfileProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

OrchestratorVersionProfileListResult.RequiredProperties = ["properties"];

/**
 * Id of the orchestrator version profile list result.
 * @member {String} id
 */
OrchestratorVersionProfileListResult.prototype['id'] = undefined;

/**
 * Name of the orchestrator version profile list result.
 * @member {String} name
 */
OrchestratorVersionProfileListResult.prototype['name'] = undefined;

/**
 * @member {module:model/OrchestratorVersionProfileProperties} properties
 */
OrchestratorVersionProfileListResult.prototype['properties'] = undefined;

/**
 * Type of the orchestrator version profile list result.
 * @member {String} type
 */
OrchestratorVersionProfileListResult.prototype['type'] = undefined;






export default OrchestratorVersionProfileListResult;

