/**
 * www.zoomconnect.com
 * The world's greatest SMS API
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The WebServiceSendVoiceMessageResponse model module.
 * @module model/WebServiceSendVoiceMessageResponse
 * @version 1
 */
class WebServiceSendVoiceMessageResponse {
    /**
     * Constructs a new <code>WebServiceSendVoiceMessageResponse</code>.
     * WebServiceSendVoiceMessageResponse
     * @alias module:model/WebServiceSendVoiceMessageResponse
     */
    constructor() { 
        
        WebServiceSendVoiceMessageResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>WebServiceSendVoiceMessageResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WebServiceSendVoiceMessageResponse} obj Optional instance to populate.
     * @return {module:model/WebServiceSendVoiceMessageResponse} The populated <code>WebServiceSendVoiceMessageResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WebServiceSendVoiceMessageResponse();

            if (data.hasOwnProperty('error')) {
                obj['error'] = ApiClient.convertToType(data['error'], 'String');
            }
            if (data.hasOwnProperty('voiceMessageId')) {
                obj['voiceMessageId'] = ApiClient.convertToType(data['voiceMessageId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WebServiceSendVoiceMessageResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WebServiceSendVoiceMessageResponse</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['error'] && !(typeof data['error'] === 'string' || data['error'] instanceof String)) {
            throw new Error("Expected the field `error` to be a primitive type in the JSON string but got " + data['error']);
        }
        // ensure the json data is a string
        if (data['voiceMessageId'] && !(typeof data['voiceMessageId'] === 'string' || data['voiceMessageId'] instanceof String)) {
            throw new Error("Expected the field `voiceMessageId` to be a primitive type in the JSON string but got " + data['voiceMessageId']);
        }

        return true;
    }


}



/**
 * @member {String} error
 */
WebServiceSendVoiceMessageResponse.prototype['error'] = undefined;

/**
 * @member {String} voiceMessageId
 */
WebServiceSendVoiceMessageResponse.prototype['voiceMessageId'] = undefined;






export default WebServiceSendVoiceMessageResponse;

