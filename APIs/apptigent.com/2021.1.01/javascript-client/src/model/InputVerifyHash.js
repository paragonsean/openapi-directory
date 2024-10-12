/**
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The InputVerifyHash model module.
 * @module model/InputVerifyHash
 * @version 2021.1.01
 */
class InputVerifyHash {
    /**
     * Constructs a new <code>InputVerifyHash</code>.
     * @alias module:model/InputVerifyHash
     * @param algorithm {module:model/InputVerifyHash.AlgorithmEnum} Hash algorithm
     * @param hash {String} Hashed result
     * @param input {String} Original source string
     */
    constructor(algorithm, hash, input) { 
        
        InputVerifyHash.initialize(this, algorithm, hash, input);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, algorithm, hash, input) { 
        obj['algorithm'] = algorithm;
        obj['hash'] = hash;
        obj['input'] = input;
    }

    /**
     * Constructs a <code>InputVerifyHash</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InputVerifyHash} obj Optional instance to populate.
     * @return {module:model/InputVerifyHash} The populated <code>InputVerifyHash</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InputVerifyHash();

            if (data.hasOwnProperty('algorithm')) {
                obj['algorithm'] = ApiClient.convertToType(data['algorithm'], 'String');
            }
            if (data.hasOwnProperty('hash')) {
                obj['hash'] = ApiClient.convertToType(data['hash'], 'String');
            }
            if (data.hasOwnProperty('input')) {
                obj['input'] = ApiClient.convertToType(data['input'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>InputVerifyHash</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>InputVerifyHash</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of InputVerifyHash.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['algorithm'] && !(typeof data['algorithm'] === 'string' || data['algorithm'] instanceof String)) {
            throw new Error("Expected the field `algorithm` to be a primitive type in the JSON string but got " + data['algorithm']);
        }
        // ensure the json data is a string
        if (data['hash'] && !(typeof data['hash'] === 'string' || data['hash'] instanceof String)) {
            throw new Error("Expected the field `hash` to be a primitive type in the JSON string but got " + data['hash']);
        }
        // ensure the json data is a string
        if (data['input'] && !(typeof data['input'] === 'string' || data['input'] instanceof String)) {
            throw new Error("Expected the field `input` to be a primitive type in the JSON string but got " + data['input']);
        }

        return true;
    }


}

InputVerifyHash.RequiredProperties = ["algorithm", "hash", "input"];

/**
 * Hash algorithm
 * @member {module:model/InputVerifyHash.AlgorithmEnum} algorithm
 */
InputVerifyHash.prototype['algorithm'] = undefined;

/**
 * Hashed result
 * @member {String} hash
 */
InputVerifyHash.prototype['hash'] = undefined;

/**
 * Original source string
 * @member {String} input
 */
InputVerifyHash.prototype['input'] = undefined;





/**
 * Allowed values for the <code>algorithm</code> property.
 * @enum {String}
 * @readonly
 */
InputVerifyHash['AlgorithmEnum'] = {

    /**
     * value: "MD5"
     * @const
     */
    "MD5": "MD5",

    /**
     * value: "SHA1"
     * @const
     */
    "SHA1": "SHA1",

    /**
     * value: "SHA256"
     * @const
     */
    "SHA256": "SHA256",

    /**
     * value: "SHA384"
     * @const
     */
    "SHA384": "SHA384",

    /**
     * value: "SHA512"
     * @const
     */
    "SHA512": "SHA512"
};



export default InputVerifyHash;

