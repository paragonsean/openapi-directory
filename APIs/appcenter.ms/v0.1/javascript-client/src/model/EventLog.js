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

/**
 * The EventLog model module.
 * @module model/EventLog
 * @version v0.1
 */
class EventLog {
    /**
     * Constructs a new <code>EventLog</code>.
     * Event log.
     * @alias module:model/EventLog
     * @param device {Object} Device characteristics.
     * @param installId {String} Install ID. 
     * @param timestamp {Date} Log creation timestamp. 
     * @param type {module:model/EventLog.TypeEnum} Log type. 
     */
    constructor(device, installId, timestamp, type) { 
        
        EventLog.initialize(this, device, installId, timestamp, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, device, installId, timestamp, type) { 
        obj['id'] = id;
        obj['name'] = name;
        obj['session_id'] = sessionId;
        obj['device'] = device;
        obj['install_id'] = installId;
        obj['timestamp'] = timestamp;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>EventLog</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EventLog} obj Optional instance to populate.
     * @return {module:model/EventLog} The populated <code>EventLog</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EventLog();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('session_id')) {
                obj['session_id'] = ApiClient.convertToType(data['session_id'], 'String');
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ApiClient.convertToType(data['properties'], {'String': 'String'});
            }
            if (data.hasOwnProperty('device')) {
                obj['device'] = ApiClient.convertToType(data['device'], Object);
            }
            if (data.hasOwnProperty('install_id')) {
                obj['install_id'] = ApiClient.convertToType(data['install_id'], 'String');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Date');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EventLog</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EventLog</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EventLog.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
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
        if (data['session_id'] && !(typeof data['session_id'] === 'string' || data['session_id'] instanceof String)) {
            throw new Error("Expected the field `session_id` to be a primitive type in the JSON string but got " + data['session_id']);
        }
        // validate the optional field `device`
        if (data['device']) { // data not null
          Object.validateJSON(data['device']);
        }
        // ensure the json data is a string
        if (data['install_id'] && !(typeof data['install_id'] === 'string' || data['install_id'] instanceof String)) {
            throw new Error("Expected the field `install_id` to be a primitive type in the JSON string but got " + data['install_id']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

EventLog.RequiredProperties = ["id", "name", "session_id", "device", "install_id", "timestamp", "type"];

/**
 * Unique identifier for this event. 
 * @member {String} id
 */
EventLog.prototype['id'] = undefined;

/**
 * Name of the event. 
 * @member {String} name
 */
EventLog.prototype['name'] = undefined;

/**
 * Session ID. 
 * @member {String} session_id
 */
EventLog.prototype['session_id'] = undefined;

/**
 * Additional key/value pair parameters. 
 * @member {Object.<String, String>} properties
 */
EventLog.prototype['properties'] = undefined;

/**
 * Device characteristics.
 * @member {Object} device
 */
EventLog.prototype['device'] = undefined;

/**
 * Install ID. 
 * @member {String} install_id
 */
EventLog.prototype['install_id'] = undefined;

/**
 * Log creation timestamp. 
 * @member {Date} timestamp
 */
EventLog.prototype['timestamp'] = undefined;

/**
 * Log type. 
 * @member {module:model/EventLog.TypeEnum} type
 */
EventLog.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
EventLog['TypeEnum'] = {

    /**
     * value: "event"
     * @const
     */
    "event": "event",

    /**
     * value: "page"
     * @const
     */
    "page": "page",

    /**
     * value: "start_session"
     * @const
     */
    "start_session": "start_session",

    /**
     * value: "error"
     * @const
     */
    "error": "error",

    /**
     * value: "push_installation"
     * @const
     */
    "push_installation": "push_installation",

    /**
     * value: "start_service"
     * @const
     */
    "start_service": "start_service",

    /**
     * value: "custom_properties"
     * @const
     */
    "custom_properties": "custom_properties"
};



export default EventLog;

