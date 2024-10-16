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
 * The EventSetting model module.
 * @module model/EventSetting
 * @version v0.1
 */
class EventSetting {
    /**
     * Constructs a new <code>EventSetting</code>.
     * Event Setting
     * @alias module:model/EventSetting
     * @param eventType {module:model/EventSetting.EventTypeEnum} Event Name
     * @param value {module:model/EventSetting.ValueEnum} Frequency of event
     */
    constructor(eventType, value) { 
        
        EventSetting.initialize(this, eventType, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, eventType, value) { 
        obj['event_type'] = eventType;
        obj['value'] = value;
    }

    /**
     * Constructs a <code>EventSetting</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EventSetting} obj Optional instance to populate.
     * @return {module:model/EventSetting} The populated <code>EventSetting</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EventSetting();

            if (data.hasOwnProperty('default_value')) {
                obj['default_value'] = ApiClient.convertToType(data['default_value'], 'String');
            }
            if (data.hasOwnProperty('event_type')) {
                obj['event_type'] = ApiClient.convertToType(data['event_type'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EventSetting</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EventSetting</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EventSetting.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['default_value'] && !(typeof data['default_value'] === 'string' || data['default_value'] instanceof String)) {
            throw new Error("Expected the field `default_value` to be a primitive type in the JSON string but got " + data['default_value']);
        }
        // ensure the json data is a string
        if (data['event_type'] && !(typeof data['event_type'] === 'string' || data['event_type'] instanceof String)) {
            throw new Error("Expected the field `event_type` to be a primitive type in the JSON string but got " + data['event_type']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}

EventSetting.RequiredProperties = ["event_type", "value"];

/**
 * Default frequency of event
 * @member {module:model/EventSetting.DefaultValueEnum} default_value
 */
EventSetting.prototype['default_value'] = undefined;

/**
 * Event Name
 * @member {module:model/EventSetting.EventTypeEnum} event_type
 */
EventSetting.prototype['event_type'] = undefined;

/**
 * Frequency of event
 * @member {module:model/EventSetting.ValueEnum} value
 */
EventSetting.prototype['value'] = undefined;





/**
 * Allowed values for the <code>default_value</code> property.
 * @enum {String}
 * @readonly
 */
EventSetting['DefaultValueEnum'] = {

    /**
     * value: "Disabled"
     * @const
     */
    "Disabled": "Disabled",

    /**
     * value: "Individual"
     * @const
     */
    "Individual": "Individual",

    /**
     * value: "Daily"
     * @const
     */
    "Daily": "Daily",

    /**
     * value: "DailyAndIndividual"
     * @const
     */
    "DailyAndIndividual": "DailyAndIndividual"
};


/**
 * Allowed values for the <code>event_type</code> property.
 * @enum {String}
 * @readonly
 */
EventSetting['EventTypeEnum'] = {

    /**
     * value: "crash_newCrashGroupCreated"
     * @const
     */
    "crash_newCrashGroupCreated": "crash_newCrashGroupCreated"
};


/**
 * Allowed values for the <code>value</code> property.
 * @enum {String}
 * @readonly
 */
EventSetting['ValueEnum'] = {

    /**
     * value: "Disabled"
     * @const
     */
    "Disabled": "Disabled",

    /**
     * value: "Individual"
     * @const
     */
    "Individual": "Individual",

    /**
     * value: "Daily"
     * @const
     */
    "Daily": "Daily",

    /**
     * value: "DailyAndIndividual"
     * @const
     */
    "DailyAndIndividual": "DailyAndIndividual",

    /**
     * value: "Default"
     * @const
     */
    "Default": "Default"
};



export default EventSetting;

