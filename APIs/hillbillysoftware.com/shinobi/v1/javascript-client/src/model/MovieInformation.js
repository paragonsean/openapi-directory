/**
 * shinobiapi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The MovieInformation model module.
 * @module model/MovieInformation
 * @version v1
 */
class MovieInformation {
    /**
     * Constructs a new <code>MovieInformation</code>.
     * @alias module:model/MovieInformation
     */
    constructor() { 
        
        MovieInformation.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>MovieInformation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MovieInformation} obj Optional instance to populate.
     * @return {module:model/MovieInformation} The populated <code>MovieInformation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MovieInformation();

            if (data.hasOwnProperty('ID')) {
                obj['ID'] = ApiClient.convertToType(data['ID'], 'String');
            }
            if (data.hasOwnProperty('ImdbID')) {
                obj['ImdbID'] = ApiClient.convertToType(data['ImdbID'], 'String');
            }
            if (data.hasOwnProperty('ReleaseYear')) {
                obj['ReleaseYear'] = ApiClient.convertToType(data['ReleaseYear'], 'String');
            }
            if (data.hasOwnProperty('Runtime')) {
                obj['Runtime'] = ApiClient.convertToType(data['Runtime'], 'String');
            }
            if (data.hasOwnProperty('Synopsis')) {
                obj['Synopsis'] = ApiClient.convertToType(data['Synopsis'], 'String');
            }
            if (data.hasOwnProperty('Title')) {
                obj['Title'] = ApiClient.convertToType(data['Title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MovieInformation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MovieInformation</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['ID'] && !(typeof data['ID'] === 'string' || data['ID'] instanceof String)) {
            throw new Error("Expected the field `ID` to be a primitive type in the JSON string but got " + data['ID']);
        }
        // ensure the json data is a string
        if (data['ImdbID'] && !(typeof data['ImdbID'] === 'string' || data['ImdbID'] instanceof String)) {
            throw new Error("Expected the field `ImdbID` to be a primitive type in the JSON string but got " + data['ImdbID']);
        }
        // ensure the json data is a string
        if (data['ReleaseYear'] && !(typeof data['ReleaseYear'] === 'string' || data['ReleaseYear'] instanceof String)) {
            throw new Error("Expected the field `ReleaseYear` to be a primitive type in the JSON string but got " + data['ReleaseYear']);
        }
        // ensure the json data is a string
        if (data['Runtime'] && !(typeof data['Runtime'] === 'string' || data['Runtime'] instanceof String)) {
            throw new Error("Expected the field `Runtime` to be a primitive type in the JSON string but got " + data['Runtime']);
        }
        // ensure the json data is a string
        if (data['Synopsis'] && !(typeof data['Synopsis'] === 'string' || data['Synopsis'] instanceof String)) {
            throw new Error("Expected the field `Synopsis` to be a primitive type in the JSON string but got " + data['Synopsis']);
        }
        // ensure the json data is a string
        if (data['Title'] && !(typeof data['Title'] === 'string' || data['Title'] instanceof String)) {
            throw new Error("Expected the field `Title` to be a primitive type in the JSON string but got " + data['Title']);
        }

        return true;
    }


}



/**
 * @member {String} ID
 */
MovieInformation.prototype['ID'] = undefined;

/**
 * @member {String} ImdbID
 */
MovieInformation.prototype['ImdbID'] = undefined;

/**
 * @member {String} ReleaseYear
 */
MovieInformation.prototype['ReleaseYear'] = undefined;

/**
 * @member {String} Runtime
 */
MovieInformation.prototype['Runtime'] = undefined;

/**
 * @member {String} Synopsis
 */
MovieInformation.prototype['Synopsis'] = undefined;

/**
 * @member {String} Title
 */
MovieInformation.prototype['Title'] = undefined;






export default MovieInformation;

