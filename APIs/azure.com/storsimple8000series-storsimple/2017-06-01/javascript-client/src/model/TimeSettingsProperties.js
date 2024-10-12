/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The TimeSettingsProperties model module.
 * @module model/TimeSettingsProperties
 * @version 2017-06-01
 */
class TimeSettingsProperties {
    /**
     * Constructs a new <code>TimeSettingsProperties</code>.
     * The properties of time settings of a device.
     * @alias module:model/TimeSettingsProperties
     * @param timeZone {String} The timezone of device, like '(UTC -06:00) Central America'
     */
    constructor(timeZone) { 
        
        TimeSettingsProperties.initialize(this, timeZone);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, timeZone) { 
        obj['timeZone'] = timeZone;
    }

    /**
     * Constructs a <code>TimeSettingsProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TimeSettingsProperties} obj Optional instance to populate.
     * @return {module:model/TimeSettingsProperties} The populated <code>TimeSettingsProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TimeSettingsProperties();

            if (data.hasOwnProperty('primaryTimeServer')) {
                obj['primaryTimeServer'] = ApiClient.convertToType(data['primaryTimeServer'], 'String');
            }
            if (data.hasOwnProperty('secondaryTimeServer')) {
                obj['secondaryTimeServer'] = ApiClient.convertToType(data['secondaryTimeServer'], ['String']);
            }
            if (data.hasOwnProperty('timeZone')) {
                obj['timeZone'] = ApiClient.convertToType(data['timeZone'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TimeSettingsProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TimeSettingsProperties</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TimeSettingsProperties.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['primaryTimeServer'] && !(typeof data['primaryTimeServer'] === 'string' || data['primaryTimeServer'] instanceof String)) {
            throw new Error("Expected the field `primaryTimeServer` to be a primitive type in the JSON string but got " + data['primaryTimeServer']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['secondaryTimeServer'])) {
            throw new Error("Expected the field `secondaryTimeServer` to be an array in the JSON data but got " + data['secondaryTimeServer']);
        }
        // ensure the json data is a string
        if (data['timeZone'] && !(typeof data['timeZone'] === 'string' || data['timeZone'] instanceof String)) {
            throw new Error("Expected the field `timeZone` to be a primitive type in the JSON string but got " + data['timeZone']);
        }

        return true;
    }


}

TimeSettingsProperties.RequiredProperties = ["timeZone"];

/**
 * The primary Network Time Protocol (NTP) server name, like 'time.windows.com'.
 * @member {String} primaryTimeServer
 */
TimeSettingsProperties.prototype['primaryTimeServer'] = undefined;

/**
 * The secondary Network Time Protocol (NTP) server name, like 'time.contoso.com'. It's optional.
 * @member {Array.<String>} secondaryTimeServer
 */
TimeSettingsProperties.prototype['secondaryTimeServer'] = undefined;

/**
 * The timezone of device, like '(UTC -06:00) Central America'
 * @member {String} timeZone
 */
TimeSettingsProperties.prototype['timeZone'] = undefined;






export default TimeSettingsProperties;

