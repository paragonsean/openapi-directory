/**
 * Flight Availibilities Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The OperatingFlight model module.
 * @module model/OperatingFlight
 * @version 1.0.2
 */
class OperatingFlight {
    /**
     * Constructs a new <code>OperatingFlight</code>.
     * information about the operating flight
     * @alias module:model/OperatingFlight
     */
    constructor() { 
        
        OperatingFlight.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OperatingFlight</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OperatingFlight} obj Optional instance to populate.
     * @return {module:model/OperatingFlight} The populated <code>OperatingFlight</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OperatingFlight();

            if (data.hasOwnProperty('carrierCode')) {
                obj['carrierCode'] = ApiClient.convertToType(data['carrierCode'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OperatingFlight</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OperatingFlight</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['carrierCode'] && !(typeof data['carrierCode'] === 'string' || data['carrierCode'] instanceof String)) {
            throw new Error("Expected the field `carrierCode` to be a primitive type in the JSON string but got " + data['carrierCode']);
        }

        return true;
    }


}



/**
 * providing the airline / carrier code
 * @member {String} carrierCode
 */
OperatingFlight.prototype['carrierCode'] = undefined;






export default OperatingFlight;

