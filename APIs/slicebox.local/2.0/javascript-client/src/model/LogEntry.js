/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The LogEntry model module.
 * @module model/LogEntry
 * @version 2.0
 */
class LogEntry {
    /**
     * Constructs a new <code>LogEntry</code>.
     * @alias module:model/LogEntry
     */
    constructor() { 
        
        LogEntry.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LogEntry</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LogEntry} obj Optional instance to populate.
     * @return {module:model/LogEntry} The populated <code>LogEntry</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LogEntry();

            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'Number');
            }
            if (data.hasOwnProperty('entryType')) {
                obj['entryType'] = ApiClient.convertToType(data['entryType'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('subject')) {
                obj['subject'] = ApiClient.convertToType(data['subject'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LogEntry</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LogEntry</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['entryType'] && !(typeof data['entryType'] === 'string' || data['entryType'] instanceof String)) {
            throw new Error("Expected the field `entryType` to be a primitive type in the JSON string but got " + data['entryType']);
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // ensure the json data is a string
        if (data['subject'] && !(typeof data['subject'] === 'string' || data['subject'] instanceof String)) {
            throw new Error("Expected the field `subject` to be a primitive type in the JSON string but got " + data['subject']);
        }

        return true;
    }


}



/**
 * @member {Number} created
 */
LogEntry.prototype['created'] = undefined;

/**
 * @member {String} entryType
 */
LogEntry.prototype['entryType'] = undefined;

/**
 * @member {Number} id
 */
LogEntry.prototype['id'] = undefined;

/**
 * @member {String} message
 */
LogEntry.prototype['message'] = undefined;

/**
 * @member {String} subject
 */
LogEntry.prototype['subject'] = undefined;






export default LogEntry;

