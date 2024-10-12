/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Document model module.
 * @module model/Document
 * @version 1.9.0
 */
class Document {
    /**
     * Constructs a new <code>Document</code>.
     * the information that are found on an ID document
     * @alias module:model/Document
     */
    constructor() { 
        
        Document.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Document</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Document} obj Optional instance to populate.
     * @return {module:model/Document} The populated <code>Document</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Document();

            if (data.hasOwnProperty('birthPlace')) {
                obj['birthPlace'] = ApiClient.convertToType(data['birthPlace'], 'String');
            }
            if (data.hasOwnProperty('expiryDate')) {
                obj['expiryDate'] = ApiClient.convertToType(data['expiryDate'], 'Date');
            }
            if (data.hasOwnProperty('issuanceCountry')) {
                obj['issuanceCountry'] = ApiClient.convertToType(data['issuanceCountry'], 'String');
            }
            if (data.hasOwnProperty('issuanceDate')) {
                obj['issuanceDate'] = ApiClient.convertToType(data['issuanceDate'], 'Date');
            }
            if (data.hasOwnProperty('issuanceLocation')) {
                obj['issuanceLocation'] = ApiClient.convertToType(data['issuanceLocation'], 'String');
            }
            if (data.hasOwnProperty('nationality')) {
                obj['nationality'] = ApiClient.convertToType(data['nationality'], 'String');
            }
            if (data.hasOwnProperty('number')) {
                obj['number'] = ApiClient.convertToType(data['number'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Document</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Document</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['birthPlace'] && !(typeof data['birthPlace'] === 'string' || data['birthPlace'] instanceof String)) {
            throw new Error("Expected the field `birthPlace` to be a primitive type in the JSON string but got " + data['birthPlace']);
        }
        // ensure the json data is a string
        if (data['issuanceCountry'] && !(typeof data['issuanceCountry'] === 'string' || data['issuanceCountry'] instanceof String)) {
            throw new Error("Expected the field `issuanceCountry` to be a primitive type in the JSON string but got " + data['issuanceCountry']);
        }
        // ensure the json data is a string
        if (data['issuanceLocation'] && !(typeof data['issuanceLocation'] === 'string' || data['issuanceLocation'] instanceof String)) {
            throw new Error("Expected the field `issuanceLocation` to be a primitive type in the JSON string but got " + data['issuanceLocation']);
        }
        // ensure the json data is a string
        if (data['nationality'] && !(typeof data['nationality'] === 'string' || data['nationality'] instanceof String)) {
            throw new Error("Expected the field `nationality` to be a primitive type in the JSON string but got " + data['nationality']);
        }
        // ensure the json data is a string
        if (data['number'] && !(typeof data['number'] === 'string' || data['number'] instanceof String)) {
            throw new Error("Expected the field `number` to be a primitive type in the JSON string but got " + data['number']);
        }

        return true;
    }


}



/**
 * Birth place as indicated on the document
 * @member {String} birthPlace
 */
Document.prototype['birthPlace'] = undefined;

/**
 * Date after which the document is not valid anymore.
 * @member {Date} expiryDate
 */
Document.prototype['expiryDate'] = undefined;

/**
 * [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the country that issued the document
 * @member {String} issuanceCountry
 */
Document.prototype['issuanceCountry'] = undefined;

/**
 * Date at which the document has been issued.
 * @member {Date} issuanceDate
 */
Document.prototype['issuanceDate'] = undefined;

/**
 * A more precise information concerning the place where the document has been issued, when available. It may be a country, a state, a city or any other type of location. e.g. New-York
 * @member {String} issuanceLocation
 */
Document.prototype['issuanceLocation'] = undefined;

/**
 * [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the nationality appearing on the document
 * @member {String} nationality
 */
Document.prototype['nationality'] = undefined;

/**
 * The document number (shown on the document) . E.g. QFU514563221J
 * @member {String} number
 */
Document.prototype['number'] = undefined;






export default Document;

