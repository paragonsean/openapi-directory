/**
 * Trip Parser
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 3.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Address model module.
 * @module model/Address
 * @version 3.0.1
 */
class Address {
    /**
     * Constructs a new <code>Address</code>.
     * Address information
     * @alias module:model/Address
     */
    constructor() { 
        
        Address.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Address</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Address} obj Optional instance to populate.
     * @return {module:model/Address} The populated <code>Address</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Address();

            if (data.hasOwnProperty('category')) {
                obj['category'] = ApiClient.convertToType(data['category'], 'String');
            }
            if (data.hasOwnProperty('cityName')) {
                obj['cityName'] = ApiClient.convertToType(data['cityName'], 'String');
            }
            if (data.hasOwnProperty('countryCode')) {
                obj['countryCode'] = ApiClient.convertToType(data['countryCode'], 'String');
            }
            if (data.hasOwnProperty('lines')) {
                obj['lines'] = ApiClient.convertToType(data['lines'], ['String']);
            }
            if (data.hasOwnProperty('postalBox')) {
                obj['postalBox'] = ApiClient.convertToType(data['postalBox'], 'String');
            }
            if (data.hasOwnProperty('postalCode')) {
                obj['postalCode'] = ApiClient.convertToType(data['postalCode'], 'String');
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], 'String');
            }
            if (data.hasOwnProperty('stateCode')) {
                obj['stateCode'] = ApiClient.convertToType(data['stateCode'], 'String');
            }
            if (data.hasOwnProperty('text')) {
                obj['text'] = ApiClient.convertToType(data['text'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Address</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Address</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['category'] && !(typeof data['category'] === 'string' || data['category'] instanceof String)) {
            throw new Error("Expected the field `category` to be a primitive type in the JSON string but got " + data['category']);
        }
        // ensure the json data is a string
        if (data['cityName'] && !(typeof data['cityName'] === 'string' || data['cityName'] instanceof String)) {
            throw new Error("Expected the field `cityName` to be a primitive type in the JSON string but got " + data['cityName']);
        }
        // ensure the json data is a string
        if (data['countryCode'] && !(typeof data['countryCode'] === 'string' || data['countryCode'] instanceof String)) {
            throw new Error("Expected the field `countryCode` to be a primitive type in the JSON string but got " + data['countryCode']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['lines'])) {
            throw new Error("Expected the field `lines` to be an array in the JSON data but got " + data['lines']);
        }
        // ensure the json data is a string
        if (data['postalBox'] && !(typeof data['postalBox'] === 'string' || data['postalBox'] instanceof String)) {
            throw new Error("Expected the field `postalBox` to be a primitive type in the JSON string but got " + data['postalBox']);
        }
        // ensure the json data is a string
        if (data['postalCode'] && !(typeof data['postalCode'] === 'string' || data['postalCode'] instanceof String)) {
            throw new Error("Expected the field `postalCode` to be a primitive type in the JSON string but got " + data['postalCode']);
        }
        // ensure the json data is a string
        if (data['state'] && !(typeof data['state'] === 'string' || data['state'] instanceof String)) {
            throw new Error("Expected the field `state` to be a primitive type in the JSON string but got " + data['state']);
        }
        // ensure the json data is a string
        if (data['stateCode'] && !(typeof data['stateCode'] === 'string' || data['stateCode'] instanceof String)) {
            throw new Error("Expected the field `stateCode` to be a primitive type in the JSON string but got " + data['stateCode']);
        }
        // ensure the json data is a string
        if (data['text'] && !(typeof data['text'] === 'string' || data['text'] instanceof String)) {
            throw new Error("Expected the field `text` to be a primitive type in the JSON string but got " + data['text']);
        }

        return true;
    }


}



/**
 * Category of the contact element
 * @member {String} category
 */
Address.prototype['category'] = undefined;

/**
 * Full city name. Example: Dublin
 * @member {String} cityName
 */
Address.prototype['cityName'] = undefined;

/**
 * ISO 3166-1 country code
 * @member {String} countryCode
 */
Address.prototype['countryCode'] = undefined;

/**
 * Line 1 = Street address, Line 2 = Apartment, suite, unit, building, floor, etc
 * @member {Array.<String>} lines
 */
Address.prototype['lines'] = undefined;

/**
 * E.g. BP 220
 * @member {String} postalBox
 */
Address.prototype['postalBox'] = undefined;

/**
 * Example: 74130
 * @member {String} postalCode
 */
Address.prototype['postalCode'] = undefined;

/**
 * State, province or country name
 * @member {String} state
 */
Address.prototype['state'] = undefined;

/**
 * State code (two character standard IATA state code)
 * @member {String} stateCode
 */
Address.prototype['stateCode'] = undefined;

/**
 * Field containing a full unformatted address. Only applicable when the fields lines, postalCode, countryCode, cityName are not filled.
 * @member {String} text
 */
Address.prototype['text'] = undefined;






export default Address;

