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
import OverrideTaskStepProperties from './OverrideTaskStepProperties';
import RunRequest from './RunRequest';

/**
 * The TaskRunRequest model module.
 * @module model/TaskRunRequest
 * @version 2019-06-01-preview
 */
class TaskRunRequest {
    /**
     * Constructs a new <code>TaskRunRequest</code>.
     * The parameters for a task run request.
     * @alias module:model/TaskRunRequest
     * @extends module:model/RunRequest
     * @implements module:model/RunRequest
     * @param type {String} The type of the run request.
     */
    constructor(type) { 
        RunRequest.initialize(this, type);
        TaskRunRequest.initialize(this, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, type) { 
        obj['taskId'] = taskId;
    }

    /**
     * Constructs a <code>TaskRunRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TaskRunRequest} obj Optional instance to populate.
     * @return {module:model/TaskRunRequest} The populated <code>TaskRunRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TaskRunRequest();
            RunRequest.constructFromObject(data, obj);
            RunRequest.constructFromObject(data, obj);

            if (data.hasOwnProperty('overrideTaskStepProperties')) {
                obj['overrideTaskStepProperties'] = OverrideTaskStepProperties.constructFromObject(data['overrideTaskStepProperties']);
            }
            if (data.hasOwnProperty('taskId')) {
                obj['taskId'] = ApiClient.convertToType(data['taskId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TaskRunRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TaskRunRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TaskRunRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `overrideTaskStepProperties`
        if (data['overrideTaskStepProperties']) { // data not null
          OverrideTaskStepProperties.validateJSON(data['overrideTaskStepProperties']);
        }
        // ensure the json data is a string
        if (data['taskId'] && !(typeof data['taskId'] === 'string' || data['taskId'] instanceof String)) {
            throw new Error("Expected the field `taskId` to be a primitive type in the JSON string but got " + data['taskId']);
        }

        return true;
    }


}

TaskRunRequest.RequiredProperties = ["taskId", "type"];

/**
 * @member {module:model/OverrideTaskStepProperties} overrideTaskStepProperties
 */
TaskRunRequest.prototype['overrideTaskStepProperties'] = undefined;

/**
 * The resource ID of task against which run has to be queued.
 * @member {String} taskId
 */
TaskRunRequest.prototype['taskId'] = undefined;


// Implement RunRequest interface:
/**
 * The value that indicates whether archiving is enabled for the run or not.
 * @member {Boolean} isArchiveEnabled
 * @default false
 */
RunRequest.prototype['isArchiveEnabled'] = false;
/**
 * The type of the run request.
 * @member {String} type
 */
RunRequest.prototype['type'] = undefined;




export default TaskRunRequest;

