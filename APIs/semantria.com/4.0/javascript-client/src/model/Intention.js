/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Intention model module.
 * @module model/Intention
 * @version 4.0
 */
class Intention {
    /**
     * Constructs a new <code>Intention</code>.
     * @alias module:model/Intention
     * @param evidencePhrase {String} The phrase which expressed the intention
     * @param type {String} The classification of the intention detected (buy, quit, etc.)
     * @param what {String} The object of the intention (if detected)
     * @param who {String} The author of the intention (if detected)
     */
    constructor(evidencePhrase, type, what, who) { 
        
        Intention.initialize(this, evidencePhrase, type, what, who);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, evidencePhrase, type, what, who) { 
        obj['evidence_phrase'] = evidencePhrase;
        obj['type'] = type;
        obj['what'] = what;
        obj['who'] = who;
    }

    /**
     * Constructs a <code>Intention</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Intention} obj Optional instance to populate.
     * @return {module:model/Intention} The populated <code>Intention</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Intention();

            if (data.hasOwnProperty('evidence_phrase')) {
                obj['evidence_phrase'] = ApiClient.convertToType(data['evidence_phrase'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('what')) {
                obj['what'] = ApiClient.convertToType(data['what'], 'String');
            }
            if (data.hasOwnProperty('who')) {
                obj['who'] = ApiClient.convertToType(data['who'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Intention</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Intention</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Intention.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['evidence_phrase'] && !(typeof data['evidence_phrase'] === 'string' || data['evidence_phrase'] instanceof String)) {
            throw new Error("Expected the field `evidence_phrase` to be a primitive type in the JSON string but got " + data['evidence_phrase']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // ensure the json data is a string
        if (data['what'] && !(typeof data['what'] === 'string' || data['what'] instanceof String)) {
            throw new Error("Expected the field `what` to be a primitive type in the JSON string but got " + data['what']);
        }
        // ensure the json data is a string
        if (data['who'] && !(typeof data['who'] === 'string' || data['who'] instanceof String)) {
            throw new Error("Expected the field `who` to be a primitive type in the JSON string but got " + data['who']);
        }

        return true;
    }


}

Intention.RequiredProperties = ["evidence_phrase", "type", "what", "who"];

/**
 * The phrase which expressed the intention
 * @member {String} evidence_phrase
 */
Intention.prototype['evidence_phrase'] = undefined;

/**
 * The classification of the intention detected (buy, quit, etc.)
 * @member {String} type
 */
Intention.prototype['type'] = undefined;

/**
 * The object of the intention (if detected)
 * @member {String} what
 */
Intention.prototype['what'] = undefined;

/**
 * The author of the intention (if detected)
 * @member {String} who
 */
Intention.prototype['who'] = undefined;






export default Intention;

