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
 * The WebhooksList200ResponseValuesInner model module.
 * @module model/WebhooksList200ResponseValuesInner
 * @version v0.1
 */
class WebhooksList200ResponseValuesInner {
    /**
     * Constructs a new <code>WebhooksList200ResponseValuesInner</code>.
     * Alerting webhook
     * @alias module:model/WebhooksList200ResponseValuesInner
     * @param eventTypes {Array.<module:model/WebhooksList200ResponseValuesInner.EventTypesEnum>} Event types enabled for webhook
     * @param name {String} display name of the webhook
     * @param url {String} target url of the webhook
     */
    constructor(eventTypes, name, url) { 
        
        WebhooksList200ResponseValuesInner.initialize(this, eventTypes, name, url);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, eventTypes, name, url) { 
        obj['event_types'] = eventTypes;
        obj['name'] = name;
        obj['url'] = url;
    }

    /**
     * Constructs a <code>WebhooksList200ResponseValuesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WebhooksList200ResponseValuesInner} obj Optional instance to populate.
     * @return {module:model/WebhooksList200ResponseValuesInner} The populated <code>WebhooksList200ResponseValuesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WebhooksList200ResponseValuesInner();

            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('event_types')) {
                obj['event_types'] = ApiClient.convertToType(data['event_types'], ['String']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WebhooksList200ResponseValuesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WebhooksList200ResponseValuesInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of WebhooksList200ResponseValuesInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['event_types'])) {
            throw new Error("Expected the field `event_types` to be an array in the JSON data but got " + data['event_types']);
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
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}

WebhooksList200ResponseValuesInner.RequiredProperties = ["event_types", "name", "url"];

/**
 * Allows eanble/disable webhook
 * @member {Boolean} enabled
 */
WebhooksList200ResponseValuesInner.prototype['enabled'] = undefined;

/**
 * Event types enabled for webhook
 * @member {Array.<module:model/WebhooksList200ResponseValuesInner.EventTypesEnum>} event_types
 */
WebhooksList200ResponseValuesInner.prototype['event_types'] = undefined;

/**
 * The unique id (UUID) of the webhook
 * @member {String} id
 */
WebhooksList200ResponseValuesInner.prototype['id'] = undefined;

/**
 * display name of the webhook
 * @member {String} name
 */
WebhooksList200ResponseValuesInner.prototype['name'] = undefined;

/**
 * target url of the webhook
 * @member {String} url
 */
WebhooksList200ResponseValuesInner.prototype['url'] = undefined;





/**
 * Allowed values for the <code>eventTypes</code> property.
 * @enum {String}
 * @readonly
 */
WebhooksList200ResponseValuesInner['EventTypesEnum'] = {

    /**
     * value: "newCrashGroupCreated"
     * @const
     */
    "newCrashGroupCreated": "newCrashGroupCreated",

    /**
     * value: "newAppReleased"
     * @const
     */
    "newAppReleased": "newAppReleased"
};



export default WebhooksList200ResponseValuesInner;

