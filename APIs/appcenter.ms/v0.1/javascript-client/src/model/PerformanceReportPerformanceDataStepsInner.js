/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PerformanceReportPerformanceDataStepsInnerSamplesInner from './PerformanceReportPerformanceDataStepsInnerSamplesInner';

/**
 * The PerformanceReportPerformanceDataStepsInner model module.
 * @module model/PerformanceReportPerformanceDataStepsInner
 * @version v0.1
 */
class PerformanceReportPerformanceDataStepsInner {
    /**
     * Constructs a new <code>PerformanceReportPerformanceDataStepsInner</code>.
     * @alias module:model/PerformanceReportPerformanceDataStepsInner
     */
    constructor() { 
        
        PerformanceReportPerformanceDataStepsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PerformanceReportPerformanceDataStepsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PerformanceReportPerformanceDataStepsInner} obj Optional instance to populate.
     * @return {module:model/PerformanceReportPerformanceDataStepsInner} The populated <code>PerformanceReportPerformanceDataStepsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PerformanceReportPerformanceDataStepsInner();

            if (data.hasOwnProperty('avg-cpu')) {
                obj['avg-cpu'] = ApiClient.convertToType(data['avg-cpu'], 'Number');
            }
            if (data.hasOwnProperty('avg-mem')) {
                obj['avg-mem'] = ApiClient.convertToType(data['avg-mem'], 'Number');
            }
            if (data.hasOwnProperty('elapsed-secs')) {
                obj['elapsed-secs'] = ApiClient.convertToType(data['elapsed-secs'], 'Number');
            }
            if (data.hasOwnProperty('elapsed-secs-end')) {
                obj['elapsed-secs-end'] = ApiClient.convertToType(data['elapsed-secs-end'], 'Number');
            }
            if (data.hasOwnProperty('elapsed-secs-start')) {
                obj['elapsed-secs-start'] = ApiClient.convertToType(data['elapsed-secs-start'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('samples')) {
                obj['samples'] = ApiClient.convertToType(data['samples'], [PerformanceReportPerformanceDataStepsInnerSamplesInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PerformanceReportPerformanceDataStepsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PerformanceReportPerformanceDataStepsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        if (data['samples']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['samples'])) {
                throw new Error("Expected the field `samples` to be an array in the JSON data but got " + data['samples']);
            }
            // validate the optional field `samples` (array)
            for (const item of data['samples']) {
                PerformanceReportPerformanceDataStepsInnerSamplesInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Number} avg-cpu
 */
PerformanceReportPerformanceDataStepsInner.prototype['avg-cpu'] = undefined;

/**
 * @member {Number} avg-mem
 */
PerformanceReportPerformanceDataStepsInner.prototype['avg-mem'] = undefined;

/**
 * @member {Number} elapsed-secs
 */
PerformanceReportPerformanceDataStepsInner.prototype['elapsed-secs'] = undefined;

/**
 * @member {Number} elapsed-secs-end
 */
PerformanceReportPerformanceDataStepsInner.prototype['elapsed-secs-end'] = undefined;

/**
 * @member {Number} elapsed-secs-start
 */
PerformanceReportPerformanceDataStepsInner.prototype['elapsed-secs-start'] = undefined;

/**
 * @member {String} id
 */
PerformanceReportPerformanceDataStepsInner.prototype['id'] = undefined;

/**
 * @member {String} name
 */
PerformanceReportPerformanceDataStepsInner.prototype['name'] = undefined;

/**
 * @member {Array.<module:model/PerformanceReportPerformanceDataStepsInnerSamplesInner>} samples
 */
PerformanceReportPerformanceDataStepsInner.prototype['samples'] = undefined;






export default PerformanceReportPerformanceDataStepsInner;

