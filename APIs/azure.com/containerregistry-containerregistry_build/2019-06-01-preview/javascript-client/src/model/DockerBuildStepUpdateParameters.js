/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Argument from './Argument';
import TaskStepUpdateParameters from './TaskStepUpdateParameters';

/**
 * The DockerBuildStepUpdateParameters model module.
 * @module model/DockerBuildStepUpdateParameters
 * @version 2019-06-01-preview
 */
class DockerBuildStepUpdateParameters {
    /**
     * Constructs a new <code>DockerBuildStepUpdateParameters</code>.
     * The properties for updating a docker build step.
     * @alias module:model/DockerBuildStepUpdateParameters
     * @extends module:model/TaskStepUpdateParameters
     * @implements module:model/TaskStepUpdateParameters
     * @param type {module:model/DockerBuildStepUpdateParameters.TypeEnum} The type of the step.
     */
    constructor(type) { 
        TaskStepUpdateParameters.initialize(this, type);
        DockerBuildStepUpdateParameters.initialize(this, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, type) { 
    }

    /**
     * Constructs a <code>DockerBuildStepUpdateParameters</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DockerBuildStepUpdateParameters} obj Optional instance to populate.
     * @return {module:model/DockerBuildStepUpdateParameters} The populated <code>DockerBuildStepUpdateParameters</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DockerBuildStepUpdateParameters();
            TaskStepUpdateParameters.constructFromObject(data, obj);
            TaskStepUpdateParameters.constructFromObject(data, obj);

            if (data.hasOwnProperty('arguments')) {
                obj['arguments'] = ApiClient.convertToType(data['arguments'], [Argument]);
            }
            if (data.hasOwnProperty('dockerFilePath')) {
                obj['dockerFilePath'] = ApiClient.convertToType(data['dockerFilePath'], 'String');
            }
            if (data.hasOwnProperty('imageNames')) {
                obj['imageNames'] = ApiClient.convertToType(data['imageNames'], ['String']);
            }
            if (data.hasOwnProperty('isPushEnabled')) {
                obj['isPushEnabled'] = ApiClient.convertToType(data['isPushEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('noCache')) {
                obj['noCache'] = ApiClient.convertToType(data['noCache'], 'Boolean');
            }
            if (data.hasOwnProperty('target')) {
                obj['target'] = ApiClient.convertToType(data['target'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DockerBuildStepUpdateParameters</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DockerBuildStepUpdateParameters</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DockerBuildStepUpdateParameters.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['arguments']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['arguments'])) {
                throw new Error("Expected the field `arguments` to be an array in the JSON data but got " + data['arguments']);
            }
            // validate the optional field `arguments` (array)
            for (const item of data['arguments']) {
                Argument.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['dockerFilePath'] && !(typeof data['dockerFilePath'] === 'string' || data['dockerFilePath'] instanceof String)) {
            throw new Error("Expected the field `dockerFilePath` to be a primitive type in the JSON string but got " + data['dockerFilePath']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['imageNames'])) {
            throw new Error("Expected the field `imageNames` to be an array in the JSON data but got " + data['imageNames']);
        }
        // ensure the json data is a string
        if (data['target'] && !(typeof data['target'] === 'string' || data['target'] instanceof String)) {
            throw new Error("Expected the field `target` to be a primitive type in the JSON string but got " + data['target']);
        }

        return true;
    }


}

DockerBuildStepUpdateParameters.RequiredProperties = ["type"];

/**
 * The collection of override arguments to be used when executing this build step.
 * @member {Array.<module:model/Argument>} arguments
 */
DockerBuildStepUpdateParameters.prototype['arguments'] = undefined;

/**
 * The Docker file path relative to the source context.
 * @member {String} dockerFilePath
 */
DockerBuildStepUpdateParameters.prototype['dockerFilePath'] = undefined;

/**
 * The fully qualified image names including the repository and tag.
 * @member {Array.<String>} imageNames
 */
DockerBuildStepUpdateParameters.prototype['imageNames'] = undefined;

/**
 * The value of this property indicates whether the image built should be pushed to the registry or not.
 * @member {Boolean} isPushEnabled
 */
DockerBuildStepUpdateParameters.prototype['isPushEnabled'] = undefined;

/**
 * The value of this property indicates whether the image cache is enabled or not.
 * @member {Boolean} noCache
 */
DockerBuildStepUpdateParameters.prototype['noCache'] = undefined;

/**
 * The name of the target build stage for the docker build.
 * @member {String} target
 */
DockerBuildStepUpdateParameters.prototype['target'] = undefined;


// Implement TaskStepUpdateParameters interface:
/**
 * The token (git PAT or SAS token of storage account blob) associated with the context for a step.
 * @member {String} contextAccessToken
 */
TaskStepUpdateParameters.prototype['contextAccessToken'] = undefined;
/**
 * The URL(absolute or relative) of the source context for the task step.
 * @member {String} contextPath
 */
TaskStepUpdateParameters.prototype['contextPath'] = undefined;
/**
 * The type of the step.
 * @member {module:model/TaskStepUpdateParameters.TypeEnum} type
 */
TaskStepUpdateParameters.prototype['type'] = undefined;




export default DockerBuildStepUpdateParameters;

