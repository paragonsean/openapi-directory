/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ShareMessage model module.
 * @module model/ShareMessage
 * @version 2.0
 */
class ShareMessage {
    /**
     * Constructs a new <code>ShareMessage</code>.
     * @alias module:model/ShareMessage
     */
    constructor() { 
        
        ShareMessage.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ShareMessage</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ShareMessage} obj Optional instance to populate.
     * @return {module:model/ShareMessage} The populated <code>ShareMessage</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ShareMessage();

            if (data.hasOwnProperty('body')) {
                obj['body'] = ApiClient.convertToType(data['body'], 'String');
            }
            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('modified')) {
                obj['modified'] = ApiClient.convertToType(data['modified'], 'Date');
            }
            if (data.hasOwnProperty('shareId')) {
                obj['shareId'] = ApiClient.convertToType(data['shareId'], 'Number');
            }
            if (data.hasOwnProperty('subject')) {
                obj['subject'] = ApiClient.convertToType(data['subject'], 'String');
            }
            if (data.hasOwnProperty('userId')) {
                obj['userId'] = ApiClient.convertToType(data['userId'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ShareMessage</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ShareMessage</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['body'] && !(typeof data['body'] === 'string' || data['body'] instanceof String)) {
            throw new Error("Expected the field `body` to be a primitive type in the JSON string but got " + data['body']);
        }
        // ensure the json data is a string
        if (data['subject'] && !(typeof data['subject'] === 'string' || data['subject'] instanceof String)) {
            throw new Error("Expected the field `subject` to be a primitive type in the JSON string but got " + data['subject']);
        }

        return true;
    }


}



/**
 * Share invitation message text.
 * @member {String} body
 */
ShareMessage.prototype['body'] = undefined;

/**
 * Timestamp of message creation.
 * @member {Date} created
 */
ShareMessage.prototype['created'] = undefined;

/**
 * Message id.
 * @member {Number} id
 */
ShareMessage.prototype['id'] = undefined;

/**
 * Timestamp of message modification.
 * @member {Date} modified
 */
ShareMessage.prototype['modified'] = undefined;

/**
 * ID of associated share
 * @member {Number} shareId
 */
ShareMessage.prototype['shareId'] = undefined;

/**
 * Share invitation message subject.
 * @member {String} subject
 */
ShareMessage.prototype['subject'] = undefined;

/**
 * User ID who generated share invite
 * @member {Number} userId
 */
ShareMessage.prototype['userId'] = undefined;






export default ShareMessage;

