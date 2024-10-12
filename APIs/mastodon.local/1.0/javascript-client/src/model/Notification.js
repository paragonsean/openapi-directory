/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Account from './Account';
import Status from './Status';

/**
 * The Notification model module.
 * @module model/Notification
 * @version 1.0
 */
class Notification {
    /**
     * Constructs a new <code>Notification</code>.
     * Represents a notification of an event relevant to the user.
     * @alias module:model/Notification
     * @param account {module:model/Account} 
     * @param createdAt {Date} The timestamp of the notification. ISO 8601 Datetime.
     * @param id {String} The id of the notification in the database. Cast from an integer, but not guaranteed to be a number.
     * @param type {module:model/Notification.TypeEnum} The type of event that resulted in the notification.
     */
    constructor(account, createdAt, id, type) { 
        
        Notification.initialize(this, account, createdAt, id, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, account, createdAt, id, type) { 
        obj['account'] = account;
        obj['created_at'] = createdAt;
        obj['id'] = id;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>Notification</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Notification} obj Optional instance to populate.
     * @return {module:model/Notification} The populated <code>Notification</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Notification();

            if (data.hasOwnProperty('account')) {
                obj['account'] = Account.constructFromObject(data['account']);
            }
            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = Status.constructFromObject(data['status']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Notification</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Notification</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Notification.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `account`
        if (data['account']) { // data not null
          Account.validateJSON(data['account']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `status`
        if (data['status']) { // data not null
          Status.validateJSON(data['status']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

Notification.RequiredProperties = ["account", "created_at", "id", "type"];

/**
 * @member {module:model/Account} account
 */
Notification.prototype['account'] = undefined;

/**
 * The timestamp of the notification. ISO 8601 Datetime.
 * @member {Date} created_at
 */
Notification.prototype['created_at'] = undefined;

/**
 * The id of the notification in the database. Cast from an integer, but not guaranteed to be a number.
 * @member {String} id
 */
Notification.prototype['id'] = undefined;

/**
 * @member {module:model/Status} status
 */
Notification.prototype['status'] = undefined;

/**
 * The type of event that resulted in the notification.
 * @member {module:model/Notification.TypeEnum} type
 */
Notification.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
Notification['TypeEnum'] = {

    /**
     * value: "follow"
     * @const
     */
    "follow": "follow",

    /**
     * value: "follow_request"
     * @const
     */
    "follow_request": "follow_request",

    /**
     * value: "mention"
     * @const
     */
    "mention": "mention",

    /**
     * value: "reblog"
     * @const
     */
    "reblog": "reblog",

    /**
     * value: "favourite"
     * @const
     */
    "favourite": "favourite",

    /**
     * value: "poll"
     * @const
     */
    "poll": "poll",

    /**
     * value: "status"
     * @const
     */
    "status": "status"
};



export default Notification;

