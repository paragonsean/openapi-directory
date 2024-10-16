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
 * The TextToSpeech model module.
 * @module model/TextToSpeech
 * @version V2
 */
class TextToSpeech {
    /**
     * Constructs a new <code>TextToSpeech</code>.
     * Request object is used to create a sound from provided text using text to speech engine
     * @alias module:model/TextToSpeech
     */
    constructor() { 
        
        TextToSpeech.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TextToSpeech</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TextToSpeech} obj Optional instance to populate.
     * @return {module:model/TextToSpeech} The populated <code>TextToSpeech</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TextToSpeech();

            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('voice')) {
                obj['voice'] = ApiClient.convertToType(data['voice'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TextToSpeech</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TextToSpeech</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // ensure the json data is a string
        if (data['voice'] && !(typeof data['voice'] === 'string' || data['voice'] instanceof String)) {
            throw new Error("Expected the field `voice` to be a primitive type in the JSON string but got " + data['voice']);
        }

        return true;
    }


}



/**
 * A text to be turned into sound
 * @member {String} message
 */
TextToSpeech.prototype['message'] = undefined;

/**
 * A voice to be used. Available values: MALE1, FEMALE1 , FEMALE2, SPANISH1, FRENCHCANADIAN1
 * @member {module:model/TextToSpeech.VoiceEnum} voice
 */
TextToSpeech.prototype['voice'] = undefined;





/**
 * Allowed values for the <code>voice</code> property.
 * @enum {String}
 * @readonly
 */
TextToSpeech['VoiceEnum'] = {

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



export default TextToSpeech;

