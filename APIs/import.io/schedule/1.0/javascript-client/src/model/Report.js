/**
 * import.io
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
 * The Report model module.
 * @module model/Report
 * @version 1.0
 */
class Report {
    /**
     * Constructs a new <code>Report</code>.
     * @alias module:model/Report
     */
    constructor() { 
        
        Report.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Report</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Report} obj Optional instance to populate.
     * @return {module:model/Report} The populated <code>Report</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Report();

            if (data.hasOwnProperty('configId')) {
                obj['configId'] = ApiClient.convertToType(data['configId'], 'String');
            }
            if (data.hasOwnProperty('guid')) {
                obj['guid'] = ApiClient.convertToType(data['guid'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('published')) {
                obj['published'] = ApiClient.convertToType(data['published'], 'Boolean');
            }
            if (data.hasOwnProperty('reportId')) {
                obj['reportId'] = ApiClient.convertToType(data['reportId'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('summary')) {
                obj['summary'] = ApiClient.convertToType(data['summary'], Object);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Report</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Report</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['configId'] && !(typeof data['configId'] === 'string' || data['configId'] instanceof String)) {
            throw new Error("Expected the field `configId` to be a primitive type in the JSON string but got " + data['configId']);
        }
        // ensure the json data is a string
        if (data['guid'] && !(typeof data['guid'] === 'string' || data['guid'] instanceof String)) {
            throw new Error("Expected the field `guid` to be a primitive type in the JSON string but got " + data['guid']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['reportId'] && !(typeof data['reportId'] === 'string' || data['reportId'] instanceof String)) {
            throw new Error("Expected the field `reportId` to be a primitive type in the JSON string but got " + data['reportId']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {String} configId
 */
Report.prototype['configId'] = undefined;

/**
 * @member {String} guid
 */
Report.prototype['guid'] = undefined;

/**
 * @member {String} name
 */
Report.prototype['name'] = undefined;

/**
 * @member {Boolean} published
 */
Report.prototype['published'] = undefined;

/**
 * @member {String} reportId
 */
Report.prototype['reportId'] = undefined;

/**
 * @member {String} status
 */
Report.prototype['status'] = undefined;

/**
 * @member {Object} summary
 */
Report.prototype['summary'] = undefined;

/**
 * @member {String} type
 */
Report.prototype['type'] = undefined;






export default Report;

