/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The CallRecipient model module.
 * @module model/CallRecipient
 * @version V2
 */
class CallRecipient {
    /**
     * Constructs a new <code>CallRecipient</code>.
     * Recipient of a campaign action. Can be a phone number, contact, or contact list with attributes added to action. It is required to specify one of this values
     * @alias module:model/CallRecipient
     */
    constructor() { 
        
        CallRecipient.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CallRecipient</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CallRecipient} obj Optional instance to populate.
     * @return {module:model/CallRecipient} The populated <code>CallRecipient</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CallRecipient();

            if (data.hasOwnProperty('attributes')) {
                obj['attributes'] = ApiClient.convertToType(data['attributes'], {'String': 'String'});
            }
            if (data.hasOwnProperty('contactId')) {
                obj['contactId'] = ApiClient.convertToType(data['contactId'], 'Number');
            }
            if (data.hasOwnProperty('dialplanXml')) {
                obj['dialplanXml'] = ApiClient.convertToType(data['dialplanXml'], 'String');
            }
            if (data.hasOwnProperty('fromNumber')) {
                obj['fromNumber'] = ApiClient.convertToType(data['fromNumber'], 'String');
            }
            if (data.hasOwnProperty('liveMessage')) {
                obj['liveMessage'] = ApiClient.convertToType(data['liveMessage'], 'String');
            }
            if (data.hasOwnProperty('liveMessageSoundId')) {
                obj['liveMessageSoundId'] = ApiClient.convertToType(data['liveMessageSoundId'], 'Number');
            }
            if (data.hasOwnProperty('machineMessage')) {
                obj['machineMessage'] = ApiClient.convertToType(data['machineMessage'], 'String');
            }
            if (data.hasOwnProperty('machineMessageSoundId')) {
                obj['machineMessageSoundId'] = ApiClient.convertToType(data['machineMessageSoundId'], 'Number');
            }
            if (data.hasOwnProperty('phoneNumber')) {
                obj['phoneNumber'] = ApiClient.convertToType(data['phoneNumber'], 'String');
            }
            if (data.hasOwnProperty('transferDigit')) {
                obj['transferDigit'] = ApiClient.convertToType(data['transferDigit'], 'String');
            }
            if (data.hasOwnProperty('transferMessage')) {
                obj['transferMessage'] = ApiClient.convertToType(data['transferMessage'], 'String');
            }
            if (data.hasOwnProperty('transferMessageSoundId')) {
                obj['transferMessageSoundId'] = ApiClient.convertToType(data['transferMessageSoundId'], 'Number');
            }
            if (data.hasOwnProperty('transferNumber')) {
                obj['transferNumber'] = ApiClient.convertToType(data['transferNumber'], 'String');
            }
            if (data.hasOwnProperty('voice')) {
                obj['voice'] = ApiClient.convertToType(data['voice'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CallRecipient</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CallRecipient</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['dialplanXml'] && !(typeof data['dialplanXml'] === 'string' || data['dialplanXml'] instanceof String)) {
            throw new Error("Expected the field `dialplanXml` to be a primitive type in the JSON string but got " + data['dialplanXml']);
        }
        // ensure the json data is a string
        if (data['fromNumber'] && !(typeof data['fromNumber'] === 'string' || data['fromNumber'] instanceof String)) {
            throw new Error("Expected the field `fromNumber` to be a primitive type in the JSON string but got " + data['fromNumber']);
        }
        // ensure the json data is a string
        if (data['liveMessage'] && !(typeof data['liveMessage'] === 'string' || data['liveMessage'] instanceof String)) {
            throw new Error("Expected the field `liveMessage` to be a primitive type in the JSON string but got " + data['liveMessage']);
        }
        // ensure the json data is a string
        if (data['machineMessage'] && !(typeof data['machineMessage'] === 'string' || data['machineMessage'] instanceof String)) {
            throw new Error("Expected the field `machineMessage` to be a primitive type in the JSON string but got " + data['machineMessage']);
        }
        // ensure the json data is a string
        if (data['phoneNumber'] && !(typeof data['phoneNumber'] === 'string' || data['phoneNumber'] instanceof String)) {
            throw new Error("Expected the field `phoneNumber` to be a primitive type in the JSON string but got " + data['phoneNumber']);
        }
        // ensure the json data is a string
        if (data['transferDigit'] && !(typeof data['transferDigit'] === 'string' || data['transferDigit'] instanceof String)) {
            throw new Error("Expected the field `transferDigit` to be a primitive type in the JSON string but got " + data['transferDigit']);
        }
        // ensure the json data is a string
        if (data['transferMessage'] && !(typeof data['transferMessage'] === 'string' || data['transferMessage'] instanceof String)) {
            throw new Error("Expected the field `transferMessage` to be a primitive type in the JSON string but got " + data['transferMessage']);
        }
        // ensure the json data is a string
        if (data['transferNumber'] && !(typeof data['transferNumber'] === 'string' || data['transferNumber'] instanceof String)) {
            throw new Error("Expected the field `transferNumber` to be a primitive type in the JSON string but got " + data['transferNumber']);
        }
        // ensure the json data is a string
        if (data['voice'] && !(typeof data['voice'] === 'string' || data['voice'] instanceof String)) {
            throw new Error("Expected the field `voice` to be a primitive type in the JSON string but got " + data['voice']);
        }

        return true;
    }


}



/**
 * Map of user-defined string attributes associated with recipient
 * @member {Object.<String, String>} attributes
 */
CallRecipient.prototype['attributes'] = undefined;

/**
 * An id of existing contact used as recipient
 * @member {Number} contactId
 */
CallRecipient.prototype['contactId'] = undefined;

/**
 * An IVR xml document describing dialplan to setup an IVR broadcast. If dialplan is set there is no need to set live, machine and transfer sounds (or vice versa)
 * @member {String} dialplanXml
 */
CallRecipient.prototype['dialplanXml'] = undefined;

/**
 * ~
 * @member {String} fromNumber
 */
CallRecipient.prototype['fromNumber'] = undefined;

/**
 * Text to be turned into a sound, this text will be played when the phone is answered
 * @member {String} liveMessage
 */
CallRecipient.prototype['liveMessage'] = undefined;

/**
 * An id of a sound file to play if phone is answered
 * @member {Number} liveMessageSoundId
 */
CallRecipient.prototype['liveMessageSoundId'] = undefined;

/**
 * Text to be used to turn into sound, this text will be played when answering machine is detected
 * @member {String} machineMessage
 */
CallRecipient.prototype['machineMessage'] = undefined;

/**
 * An id of a sound file to play if answering machine is detected
 * @member {Number} machineMessageSoundId
 */
CallRecipient.prototype['machineMessageSoundId'] = undefined;

/**
 * Recipient's phone number in E.164 format (11-digit) or short code. Example: 12132000384
 * @member {String} phoneNumber
 */
CallRecipient.prototype['phoneNumber'] = undefined;

/**
 * A digit pressed to initiate the transfer
 * @member {String} transferDigit
 */
CallRecipient.prototype['transferDigit'] = undefined;

/**
 * Text to be turned into sound, this text will be played when the transfer digit is played
 * @member {String} transferMessage
 */
CallRecipient.prototype['transferMessage'] = undefined;

/**
 * An id of a sound file to play if call is transferred
 * @member {Number} transferMessageSoundId
 */
CallRecipient.prototype['transferMessageSoundId'] = undefined;

/**
 * Phone number in E.164 format (11-digit) to transfer the call to. Example: 12132000384
 * @member {String} transferNumber
 */
CallRecipient.prototype['transferNumber'] = undefined;

/**
 * The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1)
 * @member {module:model/CallRecipient.VoiceEnum} voice
 */
CallRecipient.prototype['voice'] = undefined;





/**
 * Allowed values for the <code>voice</code> property.
 * @enum {String}
 * @readonly
 */
CallRecipient['VoiceEnum'] = {

    /**
     * value: "MALE1"
     * @const
     */
    "MALE1": "MALE1",

    /**
     * value: "FEMALE1"
     * @const
     */
    "FEMALE1": "FEMALE1",

    /**
     * value: "FEMALE2"
     * @const
     */
    "FEMALE2": "FEMALE2",

    /**
     * value: "SPANISH1"
     * @const
     */
    "SPANISH1": "SPANISH1",

    /**
     * value: "FRENCHCANADIAN1"
     * @const
     */
    "FRENCHCANADIAN1": "FRENCHCANADIAN1"
};



export default CallRecipient;

