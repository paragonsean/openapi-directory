/**
 * AutomationManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-01-15
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import DscCompilationJobProperties from './DscCompilationJobProperties';

/**
 * The DscCompilationJob model module.
 * @module model/DscCompilationJob
 * @version 2018-01-15
 */
class DscCompilationJob {
    /**
     * Constructs a new <code>DscCompilationJob</code>.
     * Definition of the Dsc Compilation job.
     * @alias module:model/DscCompilationJob
     */
    constructor() { 
        
        DscCompilationJob.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DscCompilationJob</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DscCompilationJob} obj Optional instance to populate.
     * @return {module:model/DscCompilationJob} The populated <code>DscCompilationJob</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DscCompilationJob();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = DscCompilationJobProperties.constructFromObject(data['properties']);
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
     * Validates the JSON data with respect to <code>DscCompilationJob</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DscCompilationJob</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          DscCompilationJobProperties.validateJSON(data['properties']);
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
 * @member {module:model/DscCompilationJobProperties} properties
 */
DscCompilationJob.prototype['properties'] = undefined;

/**
 * Fully qualified resource Id for the resource
 * @member {String} id
 */
DscCompilationJob.prototype['id'] = undefined;

/**
 * The name of the resource
 * @member {String} name
 */
DscCompilationJob.prototype['name'] = undefined;

/**
 * The type of the resource.
 * @member {String} type
 */
DscCompilationJob.prototype['type'] = undefined;






export default DscCompilationJob;

