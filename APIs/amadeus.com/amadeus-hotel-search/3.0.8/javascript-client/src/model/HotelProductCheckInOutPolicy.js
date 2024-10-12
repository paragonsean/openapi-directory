/**
 * Hotel Search API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 3.0.8
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import QualifiedFreeText from './QualifiedFreeText';

/**
 * The HotelProductCheckInOutPolicy model module.
 * @module model/HotelProductCheckInOutPolicy
 * @version 3.0.8
 */
class HotelProductCheckInOutPolicy {
    /**
     * Constructs a new <code>HotelProductCheckInOutPolicy</code>.
     * @alias module:model/HotelProductCheckInOutPolicy
     */
    constructor() { 
        
        HotelProductCheckInOutPolicy.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>HotelProductCheckInOutPolicy</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HotelProductCheckInOutPolicy} obj Optional instance to populate.
     * @return {module:model/HotelProductCheckInOutPolicy} The populated <code>HotelProductCheckInOutPolicy</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HotelProductCheckInOutPolicy();

            if (data.hasOwnProperty('checkIn')) {
                obj['checkIn'] = ApiClient.convertToType(data['checkIn'], 'String');
            }
            if (data.hasOwnProperty('checkInDescription')) {
                obj['checkInDescription'] = QualifiedFreeText.constructFromObject(data['checkInDescription']);
            }
            if (data.hasOwnProperty('checkOut')) {
                obj['checkOut'] = ApiClient.convertToType(data['checkOut'], 'String');
            }
            if (data.hasOwnProperty('checkOutDescription')) {
                obj['checkOutDescription'] = QualifiedFreeText.constructFromObject(data['checkOutDescription']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HotelProductCheckInOutPolicy</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HotelProductCheckInOutPolicy</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['checkIn'] && !(typeof data['checkIn'] === 'string' || data['checkIn'] instanceof String)) {
            throw new Error("Expected the field `checkIn` to be a primitive type in the JSON string but got " + data['checkIn']);
        }
        // validate the optional field `checkInDescription`
        if (data['checkInDescription']) { // data not null
          QualifiedFreeText.validateJSON(data['checkInDescription']);
        }
        // ensure the json data is a string
        if (data['checkOut'] && !(typeof data['checkOut'] === 'string' || data['checkOut'] instanceof String)) {
            throw new Error("Expected the field `checkOut` to be a primitive type in the JSON string but got " + data['checkOut']);
        }
        // validate the optional field `checkOutDescription`
        if (data['checkOutDescription']) { // data not null
          QualifiedFreeText.validateJSON(data['checkOutDescription']);
        }

        return true;
    }


}



/**
 * Check-in From time limit in ISO-8601 format [http://www.w3.org/TR/xmlschema-2/#time]
 * @member {String} checkIn
 */
HotelProductCheckInOutPolicy.prototype['checkIn'] = undefined;

/**
 * @member {module:model/QualifiedFreeText} checkInDescription
 */
HotelProductCheckInOutPolicy.prototype['checkInDescription'] = undefined;

/**
 * Check-out Until time limit in ISO-8601 format [http://www.w3.org/TR/xmlschema-2/#time]
 * @member {String} checkOut
 */
HotelProductCheckInOutPolicy.prototype['checkOut'] = undefined;

/**
 * @member {module:model/QualifiedFreeText} checkOutDescription
 */
HotelProductCheckInOutPolicy.prototype['checkOutDescription'] = undefined;






export default HotelProductCheckInOutPolicy;

