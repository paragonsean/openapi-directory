/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Genre model module.
 * @module model/Genre
 * @version 1.0.0
 */
class Genre {
    /**
     * Constructs a new <code>Genre</code>.
     * @alias module:model/Genre
     */
    constructor() { 
        
        Genre.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Genre</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Genre} obj Optional instance to populate.
     * @return {module:model/Genre} The populated <code>Genre</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Genre();

            if (data.hasOwnProperty('#text')) {
                obj['#text'] = ApiClient.convertToType(data['#text'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Genre</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Genre</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['#text'] && !(typeof data['#text'] === 'string' || data['#text'] instanceof String)) {
            throw new Error("Expected the field `#text` to be a primitive type in the JSON string but got " + data['#text']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {String} #text
 */
Genre.prototype['#text'] = undefined;

/**
 * @member {String} id
 */
Genre.prototype['id'] = undefined;

/**
 * @member {String} type
 */
Genre.prototype['type'] = undefined;






export default Genre;

