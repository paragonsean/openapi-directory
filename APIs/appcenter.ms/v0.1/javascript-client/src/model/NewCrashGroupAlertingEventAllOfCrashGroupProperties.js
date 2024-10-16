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
 * The NewCrashGroupAlertingEventAllOfCrashGroupProperties model module.
 * @module model/NewCrashGroupAlertingEventAllOfCrashGroupProperties
 * @version v0.1
 */
class NewCrashGroupAlertingEventAllOfCrashGroupProperties {
    /**
     * Constructs a new <code>NewCrashGroupAlertingEventAllOfCrashGroupProperties</code>.
     * Properties of new crash group
     * @alias module:model/NewCrashGroupAlertingEventAllOfCrashGroupProperties
     * @param appDisplayName {String} 
     * @param appPlatform {String} 
     * @param appVersion {String} 
     * @param id {String} 
     * @param name {String} 
     * @param reason {String} 
     * @param stackTrace {Array.<String>} 
     * @param url {String} 
     */
    constructor(appDisplayName, appPlatform, appVersion, id, name, reason, stackTrace, url) { 
        
        NewCrashGroupAlertingEventAllOfCrashGroupProperties.initialize(this, appDisplayName, appPlatform, appVersion, id, name, reason, stackTrace, url);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, appDisplayName, appPlatform, appVersion, id, name, reason, stackTrace, url) { 
        obj['app_display_name'] = appDisplayName;
        obj['app_platform'] = appPlatform;
        obj['app_version'] = appVersion;
        obj['id'] = id;
        obj['name'] = name;
        obj['reason'] = reason;
        obj['stack_trace'] = stackTrace;
        obj['url'] = url;
    }

    /**
     * Constructs a <code>NewCrashGroupAlertingEventAllOfCrashGroupProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NewCrashGroupAlertingEventAllOfCrashGroupProperties} obj Optional instance to populate.
     * @return {module:model/NewCrashGroupAlertingEventAllOfCrashGroupProperties} The populated <code>NewCrashGroupAlertingEventAllOfCrashGroupProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NewCrashGroupAlertingEventAllOfCrashGroupProperties();

            if (data.hasOwnProperty('app_display_name')) {
                obj['app_display_name'] = ApiClient.convertToType(data['app_display_name'], 'String');
            }
            if (data.hasOwnProperty('app_platform')) {
                obj['app_platform'] = ApiClient.convertToType(data['app_platform'], 'String');
            }
            if (data.hasOwnProperty('app_version')) {
                obj['app_version'] = ApiClient.convertToType(data['app_version'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('reason')) {
                obj['reason'] = ApiClient.convertToType(data['reason'], 'String');
            }
            if (data.hasOwnProperty('stack_trace')) {
                obj['stack_trace'] = ApiClient.convertToType(data['stack_trace'], ['String']);
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NewCrashGroupAlertingEventAllOfCrashGroupProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NewCrashGroupAlertingEventAllOfCrashGroupProperties</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of NewCrashGroupAlertingEventAllOfCrashGroupProperties.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['app_display_name'] && !(typeof data['app_display_name'] === 'string' || data['app_display_name'] instanceof String)) {
            throw new Error("Expected the field `app_display_name` to be a primitive type in the JSON string but got " + data['app_display_name']);
        }
        // ensure the json data is a string
        if (data['app_platform'] && !(typeof data['app_platform'] === 'string' || data['app_platform'] instanceof String)) {
            throw new Error("Expected the field `app_platform` to be a primitive type in the JSON string but got " + data['app_platform']);
        }
        // ensure the json data is a string
        if (data['app_version'] && !(typeof data['app_version'] === 'string' || data['app_version'] instanceof String)) {
            throw new Error("Expected the field `app_version` to be a primitive type in the JSON string but got " + data['app_version']);
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
        if (data['reason'] && !(typeof data['reason'] === 'string' || data['reason'] instanceof String)) {
            throw new Error("Expected the field `reason` to be a primitive type in the JSON string but got " + data['reason']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['stack_trace'])) {
            throw new Error("Expected the field `stack_trace` to be an array in the JSON data but got " + data['stack_trace']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}

NewCrashGroupAlertingEventAllOfCrashGroupProperties.RequiredProperties = ["app_display_name", "app_platform", "app_version", "id", "name", "reason", "stack_trace", "url"];

/**
 * @member {String} app_display_name
 */
NewCrashGroupAlertingEventAllOfCrashGroupProperties.prototype['app_display_name'] = undefined;

/**
 * @member {String} app_platform
 */
NewCrashGroupAlertingEventAllOfCrashGroupProperties.prototype['app_platform'] = undefined;

/**
 * @member {String} app_version
 */
NewCrashGroupAlertingEventAllOfCrashGroupProperties.prototype['app_version'] = undefined;

/**
 * @member {String} id
 */
NewCrashGroupAlertingEventAllOfCrashGroupProperties.prototype['id'] = undefined;

/**
 * @member {String} name
 */
NewCrashGroupAlertingEventAllOfCrashGroupProperties.prototype['name'] = undefined;

/**
 * @member {String} reason
 */
NewCrashGroupAlertingEventAllOfCrashGroupProperties.prototype['reason'] = undefined;

/**
 * @member {Array.<String>} stack_trace
 */
NewCrashGroupAlertingEventAllOfCrashGroupProperties.prototype['stack_trace'] = undefined;

/**
 * @member {String} url
 */
NewCrashGroupAlertingEventAllOfCrashGroupProperties.prototype['url'] = undefined;






export default NewCrashGroupAlertingEventAllOfCrashGroupProperties;

