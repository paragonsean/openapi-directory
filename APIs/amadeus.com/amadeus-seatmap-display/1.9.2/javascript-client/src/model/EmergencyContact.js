/**
 * Seatmap Display
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The EmergencyContact model module.
 * @module model/EmergencyContact
 * @version 1.9.2
 */
class EmergencyContact {
    /**
     * Constructs a new <code>EmergencyContact</code>.
     * emergency contact number
     * @alias module:model/EmergencyContact
     */
    constructor() { 
        
        EmergencyContact.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EmergencyContact</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EmergencyContact} obj Optional instance to populate.
     * @return {module:model/EmergencyContact} The populated <code>EmergencyContact</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EmergencyContact();

            if (data.hasOwnProperty('addresseeName')) {
                obj['addresseeName'] = ApiClient.convertToType(data['addresseeName'], 'String');
            }
            if (data.hasOwnProperty('countryCode')) {
                obj['countryCode'] = ApiClient.convertToType(data['countryCode'], 'String');
            }
            if (data.hasOwnProperty('number')) {
                obj['number'] = ApiClient.convertToType(data['number'], 'String');
            }
            if (data.hasOwnProperty('text')) {
                obj['text'] = ApiClient.convertToType(data['text'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EmergencyContact</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EmergencyContact</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['addresseeName'] && !(typeof data['addresseeName'] === 'string' || data['addresseeName'] instanceof String)) {
            throw new Error("Expected the field `addresseeName` to be a primitive type in the JSON string but got " + data['addresseeName']);
        }
        // ensure the json data is a string
        if (data['countryCode'] && !(typeof data['countryCode'] === 'string' || data['countryCode'] instanceof String)) {
            throw new Error("Expected the field `countryCode` to be a primitive type in the JSON string but got " + data['countryCode']);
        }
        // ensure the json data is a string
        if (data['number'] && !(typeof data['number'] === 'string' || data['number'] instanceof String)) {
            throw new Error("Expected the field `number` to be a primitive type in the JSON string but got " + data['number']);
        }
        // ensure the json data is a string
        if (data['text'] && !(typeof data['text'] === 'string' || data['text'] instanceof String)) {
            throw new Error("Expected the field `text` to be a primitive type in the JSON string but got " + data['text']);
        }

        return true;
    }


}



/**
 * Adressee name (e.g. in case of emergency purpose it corresponds to name of the person to be contacted).
 * @member {String} addresseeName
 */
EmergencyContact.prototype['addresseeName'] = undefined;

/**
 * Country code of the country (ISO3166-1). E.g. \"US\" for the United States
 * @member {String} countryCode
 */
EmergencyContact.prototype['countryCode'] = undefined;

/**
 * Phone number. Composed of digits only. The number of digits depends on the country.
 * @member {String} number
 */
EmergencyContact.prototype['number'] = undefined;

/**
 * additional details
 * @member {String} text
 */
EmergencyContact.prototype['text'] = undefined;






export default EmergencyContact;

