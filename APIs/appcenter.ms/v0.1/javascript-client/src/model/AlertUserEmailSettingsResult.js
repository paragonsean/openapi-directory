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
import NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner from './NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner';

/**
 * The AlertUserEmailSettingsResult model module.
 * @module model/AlertUserEmailSettingsResult
 * @version v0.1
 */
class AlertUserEmailSettingsResult {
    /**
     * Constructs a new <code>AlertUserEmailSettingsResult</code>.
     * Alerting Default Email Settings of the user
     * @alias module:model/AlertUserEmailSettingsResult
     * @param requestId {String} Unique request identifier for tracking
     * @param enabled {Boolean} Allows to forcefully disable emails on app or user level
     * @param settings {Array.<module:model/NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner>} The settings the user has for the app
     */
    constructor(requestId, enabled, settings) { 
        
        AlertUserEmailSettingsResult.initialize(this, requestId, enabled, settings);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, requestId, enabled, settings) { 
        obj['request_id'] = requestId;
        obj['enabled'] = enabled;
        obj['settings'] = settings;
    }

    /**
     * Constructs a <code>AlertUserEmailSettingsResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AlertUserEmailSettingsResult} obj Optional instance to populate.
     * @return {module:model/AlertUserEmailSettingsResult} The populated <code>AlertUserEmailSettingsResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AlertUserEmailSettingsResult();

            if (data.hasOwnProperty('request_id')) {
                obj['request_id'] = ApiClient.convertToType(data['request_id'], 'String');
            }
            if (data.hasOwnProperty('eTag')) {
                obj['eTag'] = ApiClient.convertToType(data['eTag'], 'String');
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('settings')) {
                obj['settings'] = ApiClient.convertToType(data['settings'], [NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner]);
            }
            if (data.hasOwnProperty('userId')) {
                obj['userId'] = ApiClient.convertToType(data['userId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AlertUserEmailSettingsResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AlertUserEmailSettingsResult</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AlertUserEmailSettingsResult.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['request_id'] && !(typeof data['request_id'] === 'string' || data['request_id'] instanceof String)) {
            throw new Error("Expected the field `request_id` to be a primitive type in the JSON string but got " + data['request_id']);
        }
        // ensure the json data is a string
        if (data['eTag'] && !(typeof data['eTag'] === 'string' || data['eTag'] instanceof String)) {
            throw new Error("Expected the field `eTag` to be a primitive type in the JSON string but got " + data['eTag']);
        }
        if (data['settings']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['settings'])) {
                throw new Error("Expected the field `settings` to be an array in the JSON data but got " + data['settings']);
            }
            // validate the optional field `settings` (array)
            for (const item of data['settings']) {
                NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['userId'] && !(typeof data['userId'] === 'string' || data['userId'] instanceof String)) {
            throw new Error("Expected the field `userId` to be a primitive type in the JSON string but got " + data['userId']);
        }

        return true;
    }


}

AlertUserEmailSettingsResult.RequiredProperties = ["request_id", "enabled", "settings"];

/**
 * Unique request identifier for tracking
 * @member {String} request_id
 */
AlertUserEmailSettingsResult.prototype['request_id'] = undefined;

/**
 * The ETag of the entity
 * @member {String} eTag
 */
AlertUserEmailSettingsResult.prototype['eTag'] = undefined;

/**
 * Allows to forcefully disable emails on app or user level
 * @member {Boolean} enabled
 */
AlertUserEmailSettingsResult.prototype['enabled'] = undefined;

/**
 * The settings the user has for the app
 * @member {Array.<module:model/NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner>} settings
 */
AlertUserEmailSettingsResult.prototype['settings'] = undefined;

/**
 * The unique id (UUID) of the user
 * @member {String} userId
 */
AlertUserEmailSettingsResult.prototype['userId'] = undefined;






export default AlertUserEmailSettingsResult;

