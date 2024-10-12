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
import SetValue from './SetValue';
import TaskStepUpdateParameters from './TaskStepUpdateParameters';

/**
 * The FileTaskStepUpdateParameters model module.
 * @module model/FileTaskStepUpdateParameters
 * @version 2019-06-01-preview
 */
class FileTaskStepUpdateParameters {
    /**
     * Constructs a new <code>FileTaskStepUpdateParameters</code>.
     * The properties of updating a task step.
     * @alias module:model/FileTaskStepUpdateParameters
     * @extends module:model/TaskStepUpdateParameters
     * @implements module:model/TaskStepUpdateParameters
     * @param type {module:model/FileTaskStepUpdateParameters.TypeEnum} The type of the step.
     */
    constructor(type) { 
        TaskStepUpdateParameters.initialize(this, type);
        FileTaskStepUpdateParameters.initialize(this, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, type) { 
    }

    /**
     * Constructs a <code>FileTaskStepUpdateParameters</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FileTaskStepUpdateParameters} obj Optional instance to populate.
     * @return {module:model/FileTaskStepUpdateParameters} The populated <code>FileTaskStepUpdateParameters</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FileTaskStepUpdateParameters();
            TaskStepUpdateParameters.constructFromObject(data, obj);
            TaskStepUpdateParameters.constructFromObject(data, obj);

            if (data.hasOwnProperty('taskFilePath')) {
                obj['taskFilePath'] = ApiClient.convertToType(data['taskFilePath'], 'String');
            }
            if (data.hasOwnProperty('values')) {
                obj['values'] = ApiClient.convertToType(data['values'], [SetValue]);
            }
            if (data.hasOwnProperty('valuesFilePath')) {
                obj['valuesFilePath'] = ApiClient.convertToType(data['valuesFilePath'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FileTaskStepUpdateParameters</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FileTaskStepUpdateParameters</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of FileTaskStepUpdateParameters.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['taskFilePath'] && !(typeof data['taskFilePath'] === 'string' || data['taskFilePath'] instanceof String)) {
            throw new Error("Expected the field `taskFilePath` to be a primitive type in the JSON string but got " + data['taskFilePath']);
        }
        if (data['values']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['values'])) {
                throw new Error("Expected the field `values` to be an array in the JSON data but got " + data['values']);
            }
            // validate the optional field `values` (array)
            for (const item of data['values']) {
                SetValue.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['valuesFilePath'] && !(typeof data['valuesFilePath'] === 'string' || data['valuesFilePath'] instanceof String)) {
            throw new Error("Expected the field `valuesFilePath` to be a primitive type in the JSON string but got " + data['valuesFilePath']);
        }

        return true;
    }


}

FileTaskStepUpdateParameters.RequiredProperties = ["type"];

/**
 * The task template/definition file path relative to the source context.
 * @member {String} taskFilePath
 */
FileTaskStepUpdateParameters.prototype['taskFilePath'] = undefined;

/**
 * The collection of overridable values that can be passed when running a task.
 * @member {Array.<module:model/SetValue>} values
 */
FileTaskStepUpdateParameters.prototype['values'] = undefined;

/**
 * The values/parameters file path relative to the source context.
 * @member {String} valuesFilePath
 */
FileTaskStepUpdateParameters.prototype['valuesFilePath'] = undefined;


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




export default FileTaskStepUpdateParameters;

