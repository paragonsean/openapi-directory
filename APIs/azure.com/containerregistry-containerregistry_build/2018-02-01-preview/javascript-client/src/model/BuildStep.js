/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BuildStepProperties from './BuildStepProperties';
import ProxyResource from './ProxyResource';

/**
 * The BuildStep model module.
 * @module model/BuildStep
 * @version 2018-02-01-preview
 */
class BuildStep {
    /**
     * Constructs a new <code>BuildStep</code>.
     * Build step resource properties
     * @alias module:model/BuildStep
     * @implements module:model/ProxyResource
     */
    constructor() { 
        ProxyResource.initialize(this);
        BuildStep.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BuildStep</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BuildStep} obj Optional instance to populate.
     * @return {module:model/BuildStep} The populated <code>BuildStep</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BuildStep();
            ProxyResource.constructFromObject(data, obj);

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = BuildStepProperties.constructFromObject(data['properties']);
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
     * Validates the JSON data with respect to <code>BuildStep</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BuildStep</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          BuildStepProperties.validateJSON(data['properties']);
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
 * @member {module:model/BuildStepProperties} properties
 */
BuildStep.prototype['properties'] = undefined;

/**
 * The resource ID.
 * @member {String} id
 */
BuildStep.prototype['id'] = undefined;

/**
 * The name of the resource.
 * @member {String} name
 */
BuildStep.prototype['name'] = undefined;

/**
 * The type of the resource.
 * @member {String} type
 */
BuildStep.prototype['type'] = undefined;


// Implement ProxyResource interface:
/**
 * The resource ID.
 * @member {String} id
 */
ProxyResource.prototype['id'] = undefined;
/**
 * The name of the resource.
 * @member {String} name
 */
ProxyResource.prototype['name'] = undefined;
/**
 * The type of the resource.
 * @member {String} type
 */
ProxyResource.prototype['type'] = undefined;




export default BuildStep;

