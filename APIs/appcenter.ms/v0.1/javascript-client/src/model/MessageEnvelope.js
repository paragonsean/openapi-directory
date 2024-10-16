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
 * The MessageEnvelope model module.
 * @module model/MessageEnvelope
 * @version v0.1
 */
class MessageEnvelope {
    /**
     * Constructs a new <code>MessageEnvelope</code>.
     * Envelope for messages sent to actors
     * @alias module:model/MessageEnvelope
     */
    constructor() { 
        
        MessageEnvelope.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>MessageEnvelope</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MessageEnvelope} obj Optional instance to populate.
     * @return {module:model/MessageEnvelope} The populated <code>MessageEnvelope</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MessageEnvelope();

            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], Object);
            }
            if (data.hasOwnProperty('messageId')) {
                obj['messageId'] = ApiClient.convertToType(data['messageId'], 'String');
            }
            if (data.hasOwnProperty('messageType')) {
                obj['messageType'] = ApiClient.convertToType(data['messageType'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MessageEnvelope</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MessageEnvelope</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['messageId'] && !(typeof data['messageId'] === 'string' || data['messageId'] instanceof String)) {
            throw new Error("Expected the field `messageId` to be a primitive type in the JSON string but got " + data['messageId']);
        }
        // ensure the json data is a string
        if (data['messageType'] && !(typeof data['messageType'] === 'string' || data['messageType'] instanceof String)) {
            throw new Error("Expected the field `messageType` to be a primitive type in the JSON string but got " + data['messageType']);
        }

        return true;
    }


}



/**
 * Body of the message
 * @member {Object} message
 */
MessageEnvelope.prototype['message'] = undefined;

/**
 * Unique id of the message
 * @member {String} messageId
 */
MessageEnvelope.prototype['messageId'] = undefined;

/**
 * Type of the message
 * @member {String} messageType
 */
MessageEnvelope.prototype['messageType'] = undefined;






export default MessageEnvelope;

