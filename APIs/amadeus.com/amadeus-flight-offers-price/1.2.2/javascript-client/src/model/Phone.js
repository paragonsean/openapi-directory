/**
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PhoneDeviceType from './PhoneDeviceType';

/**
 * The Phone model module.
 * @module model/Phone
 * @version 1.2.2
 */
class Phone {
    /**
     * Constructs a new <code>Phone</code>.
     * phone information
     * @alias module:model/Phone
     */
    constructor() { 
        
        Phone.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Phone</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Phone} obj Optional instance to populate.
     * @return {module:model/Phone} The populated <code>Phone</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Phone();

            if (data.hasOwnProperty('countryCallingCode')) {
                obj['countryCallingCode'] = ApiClient.convertToType(data['countryCallingCode'], 'String');
            }
            if (data.hasOwnProperty('deviceType')) {
                obj['deviceType'] = PhoneDeviceType.constructFromObject(data['deviceType']);
            }
            if (data.hasOwnProperty('number')) {
                obj['number'] = ApiClient.convertToType(data['number'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Phone</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Phone</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['countryCallingCode'] && !(typeof data['countryCallingCode'] === 'string' || data['countryCallingCode'] instanceof String)) {
            throw new Error("Expected the field `countryCallingCode` to be a primitive type in the JSON string but got " + data['countryCallingCode']);
        }
        // ensure the json data is a string
        if (data['number'] && !(typeof data['number'] === 'string' || data['number'] instanceof String)) {
            throw new Error("Expected the field `number` to be a primitive type in the JSON string but got " + data['number']);
        }

        return true;
    }


}



/**
 * Country calling code of the phone number, as defined by the International Communication Union. Examples - \"1\" for US, \"371\" for Latvia.
 * @member {String} countryCallingCode
 */
Phone.prototype['countryCallingCode'] = undefined;

/**
 * @member {module:model/PhoneDeviceType} deviceType
 */
Phone.prototype['deviceType'] = undefined;

/**
 * Phone number. Composed of digits only. The number of digits depends on the country.
 * @member {String} number
 */
Phone.prototype['number'] = undefined;






export default Phone;

