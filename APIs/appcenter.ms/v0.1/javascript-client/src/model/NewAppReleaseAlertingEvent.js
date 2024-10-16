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
import NewAppReleaseAlertingEventAllOfAppReleaseProperties from './NewAppReleaseAlertingEventAllOfAppReleaseProperties';

/**
 * The NewAppReleaseAlertingEvent model module.
 * @module model/NewAppReleaseAlertingEvent
 * @version v0.1
 */
class NewAppReleaseAlertingEvent {
    /**
     * Constructs a new <code>NewAppReleaseAlertingEvent</code>.
     * New app release alerting event
     * @alias module:model/NewAppReleaseAlertingEvent
     * @param eventId {String} A unique identifier for this event instance. Useful for deduplication
     * @param eventTimestamp {String} ISO 8601 date time when event was generated
     */
    constructor(eventId, eventTimestamp) { 
        
        NewAppReleaseAlertingEvent.initialize(this, eventId, eventTimestamp);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, eventId, eventTimestamp) { 
        obj['event_id'] = eventId;
        obj['event_timestamp'] = eventTimestamp;
    }

    /**
     * Constructs a <code>NewAppReleaseAlertingEvent</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NewAppReleaseAlertingEvent} obj Optional instance to populate.
     * @return {module:model/NewAppReleaseAlertingEvent} The populated <code>NewAppReleaseAlertingEvent</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NewAppReleaseAlertingEvent();

            if (data.hasOwnProperty('event_id')) {
                obj['event_id'] = ApiClient.convertToType(data['event_id'], 'String');
            }
            if (data.hasOwnProperty('event_timestamp')) {
                obj['event_timestamp'] = ApiClient.convertToType(data['event_timestamp'], 'String');
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ApiClient.convertToType(data['properties'], Object);
            }
            if (data.hasOwnProperty('app_release_properties')) {
                obj['app_release_properties'] = NewAppReleaseAlertingEventAllOfAppReleaseProperties.constructFromObject(data['app_release_properties']);
            }
            if (data.hasOwnProperty('disable_webhook')) {
                obj['disable_webhook'] = ApiClient.convertToType(data['disable_webhook'], 'Boolean');
            }
            if (data.hasOwnProperty('user_ids')) {
                obj['user_ids'] = ApiClient.convertToType(data['user_ids'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NewAppReleaseAlertingEvent</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NewAppReleaseAlertingEvent</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of NewAppReleaseAlertingEvent.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['event_id'] && !(typeof data['event_id'] === 'string' || data['event_id'] instanceof String)) {
            throw new Error("Expected the field `event_id` to be a primitive type in the JSON string but got " + data['event_id']);
        }
        // ensure the json data is a string
        if (data['event_timestamp'] && !(typeof data['event_timestamp'] === 'string' || data['event_timestamp'] instanceof String)) {
            throw new Error("Expected the field `event_timestamp` to be a primitive type in the JSON string but got " + data['event_timestamp']);
        }
        // validate the optional field `app_release_properties`
        if (data['app_release_properties']) { // data not null
          NewAppReleaseAlertingEventAllOfAppReleaseProperties.validateJSON(data['app_release_properties']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['user_ids'])) {
            throw new Error("Expected the field `user_ids` to be an array in the JSON data but got " + data['user_ids']);
        }

        return true;
    }


}

NewAppReleaseAlertingEvent.RequiredProperties = ["event_id", "event_timestamp"];

/**
 * A unique identifier for this event instance. Useful for deduplication
 * @member {String} event_id
 */
NewAppReleaseAlertingEvent.prototype['event_id'] = undefined;

/**
 * ISO 8601 date time when event was generated
 * @member {String} event_timestamp
 */
NewAppReleaseAlertingEvent.prototype['event_timestamp'] = undefined;

/**
 * Obsolete. Use emailProperties.
 * @member {Object} properties
 */
NewAppReleaseAlertingEvent.prototype['properties'] = undefined;

/**
 * @member {module:model/NewAppReleaseAlertingEventAllOfAppReleaseProperties} app_release_properties
 */
NewAppReleaseAlertingEvent.prototype['app_release_properties'] = undefined;

/**
 * indicate whether notify via webhook or not
 * @member {Boolean} disable_webhook
 */
NewAppReleaseAlertingEvent.prototype['disable_webhook'] = undefined;

/**
 * List of users who need to receive an email notification. If this is not null, then only sending emails will be triggered even if the event requires calling webhooks or doing other actions.
 * @member {Array.<String>} user_ids
 */
NewAppReleaseAlertingEvent.prototype['user_ids'] = undefined;






export default NewAppReleaseAlertingEvent;

