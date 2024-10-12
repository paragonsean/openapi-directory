/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-04-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BaseImageDependency from './BaseImageDependency';
import SetValue from './SetValue';
import TaskStepProperties from './TaskStepProperties';

/**
 * The EncodedTaskStep model module.
 * @module model/EncodedTaskStep
 * @version 2019-04-01
 */
class EncodedTaskStep {
    /**
     * Constructs a new <code>EncodedTaskStep</code>.
     * The properties of a encoded task step.
     * @alias module:model/EncodedTaskStep
     * @extends module:model/TaskStepProperties
     * @implements module:model/TaskStepProperties
     */
    constructor() { 
        TaskStepProperties.initialize(this);
        EncodedTaskStep.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['encodedTaskContent'] = encodedTaskContent;
    }

    /**
     * Constructs a <code>EncodedTaskStep</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EncodedTaskStep} obj Optional instance to populate.
     * @return {module:model/EncodedTaskStep} The populated <code>EncodedTaskStep</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EncodedTaskStep();
            TaskStepProperties.constructFromObject(data, obj);
            TaskStepProperties.constructFromObject(data, obj);

            if (data.hasOwnProperty('encodedTaskContent')) {
                obj['encodedTaskContent'] = ApiClient.convertToType(data['encodedTaskContent'], 'String');
            }
            if (data.hasOwnProperty('encodedValuesContent')) {
                obj['encodedValuesContent'] = ApiClient.convertToType(data['encodedValuesContent'], 'String');
            }
            if (data.hasOwnProperty('values')) {
                obj['values'] = ApiClient.convertToType(data['values'], [SetValue]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EncodedTaskStep</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EncodedTaskStep</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EncodedTaskStep.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['encodedTaskContent'] && !(typeof data['encodedTaskContent'] === 'string' || data['encodedTaskContent'] instanceof String)) {
            throw new Error("Expected the field `encodedTaskContent` to be a primitive type in the JSON string but got " + data['encodedTaskContent']);
        }
        // ensure the json data is a string
        if (data['encodedValuesContent'] && !(typeof data['encodedValuesContent'] === 'string' || data['encodedValuesContent'] instanceof String)) {
            throw new Error("Expected the field `encodedValuesContent` to be a primitive type in the JSON string but got " + data['encodedValuesContent']);
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

        return true;
    }


}

EncodedTaskStep.RequiredProperties = ["encodedTaskContent"];

/**
 * Base64 encoded value of the template/definition file content.
 * @member {String} encodedTaskContent
 */
EncodedTaskStep.prototype['encodedTaskContent'] = undefined;

/**
 * Base64 encoded value of the parameters/values file content.
 * @member {String} encodedValuesContent
 */
EncodedTaskStep.prototype['encodedValuesContent'] = undefined;

/**
 * The collection of overridable values that can be passed when running a task.
 * @member {Array.<module:model/SetValue>} values
 */
EncodedTaskStep.prototype['values'] = undefined;


// Implement TaskStepProperties interface:
/**
 * List of base image dependencies for a step.
 * @member {Array.<module:model/BaseImageDependency>} baseImageDependencies
 */
TaskStepProperties.prototype['baseImageDependencies'] = undefined;
/**
 * The token (git PAT or SAS token of storage account blob) associated with the context for a step.
 * @member {String} contextAccessToken
 */
TaskStepProperties.prototype['contextAccessToken'] = undefined;
/**
 * The URL(absolute or relative) of the source context for the task step.
 * @member {String} contextPath
 */
TaskStepProperties.prototype['contextPath'] = undefined;
/**
 * The type of the step.
 * @member {module:model/TaskStepProperties.TypeEnum} type
 */
TaskStepProperties.prototype['type'] = undefined;




export default EncodedTaskStep;

