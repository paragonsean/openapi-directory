/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The TaskStatusVO model module.
 * @module model/TaskStatusVO
 * @version 1.0
 */
class TaskStatusVO {
    /**
     * Constructs a new <code>TaskStatusVO</code>.
     * Java type: com.noosh.nooshapi.vo.TaskStatusVO
     * @alias module:model/TaskStatusVO
     */
    constructor() { 
        
        TaskStatusVO.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TaskStatusVO</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TaskStatusVO} obj Optional instance to populate.
     * @return {module:model/TaskStatusVO} The populated <code>TaskStatusVO</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TaskStatusVO();

            if (data.hasOwnProperty('task_status_id')) {
                obj['task_status_id'] = ApiClient.convertToType(data['task_status_id'], 'Number');
            }
            if (data.hasOwnProperty('task_status_name')) {
                obj['task_status_name'] = ApiClient.convertToType(data['task_status_name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TaskStatusVO</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TaskStatusVO</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['task_status_name'] && !(typeof data['task_status_name'] === 'string' || data['task_status_name'] instanceof String)) {
            throw new Error("Expected the field `task_status_name` to be a primitive type in the JSON string but got " + data['task_status_name']);
        }

        return true;
    }


}



/**
 * 
 * @member {Number} task_status_id
 */
TaskStatusVO.prototype['task_status_id'] = undefined;

/**
 * 
 * @member {String} task_status_name
 */
TaskStatusVO.prototype['task_status_name'] = undefined;






export default TaskStatusVO;

