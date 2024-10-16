/**
 * RESTful4Up
 * RESTful API 4 Unipacker
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

/**
 * The EmulationOutput200Response model module.
 * @module model/EmulationOutput200Response
 * @version 1.0.0
 */
class EmulationOutput200Response {
    /**
     * Constructs a new <code>EmulationOutput200Response</code>.
     * @alias module:model/EmulationOutput200Response
     * @param output {Array.<String>} 
     */
    constructor(output) { 
        
        EmulationOutput200Response.initialize(this, output);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, output) { 
        obj['output'] = output;
    }

    /**
     * Constructs a <code>EmulationOutput200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EmulationOutput200Response} obj Optional instance to populate.
     * @return {module:model/EmulationOutput200Response} The populated <code>EmulationOutput200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EmulationOutput200Response();

            if (data.hasOwnProperty('output')) {
                obj['output'] = ApiClient.convertToType(data['output'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EmulationOutput200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EmulationOutput200Response</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EmulationOutput200Response.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['output'])) {
            throw new Error("Expected the field `output` to be an array in the JSON data but got " + data['output']);
        }

        return true;
    }


}

EmulationOutput200Response.RequiredProperties = ["output"];

/**
 * @member {Array.<String>} output
 */
EmulationOutput200Response.prototype['output'] = undefined;






export default EmulationOutput200Response;

