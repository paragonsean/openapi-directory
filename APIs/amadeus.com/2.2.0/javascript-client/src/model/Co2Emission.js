/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import TravelClass from './TravelClass';

/**
 * The Co2Emission model module.
 * @module model/Co2Emission
 * @version 2.2.0
 */
class Co2Emission {
    /**
     * Constructs a new <code>Co2Emission</code>.
     * @alias module:model/Co2Emission
     */
    constructor() { 
        
        Co2Emission.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Co2Emission</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Co2Emission} obj Optional instance to populate.
     * @return {module:model/Co2Emission} The populated <code>Co2Emission</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Co2Emission();

            if (data.hasOwnProperty('cabin')) {
                obj['cabin'] = TravelClass.constructFromObject(data['cabin']);
            }
            if (data.hasOwnProperty('weight')) {
                obj['weight'] = ApiClient.convertToType(data['weight'], 'Number');
            }
            if (data.hasOwnProperty('weightUnit')) {
                obj['weightUnit'] = ApiClient.convertToType(data['weightUnit'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Co2Emission</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Co2Emission</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['weightUnit'] && !(typeof data['weightUnit'] === 'string' || data['weightUnit'] instanceof String)) {
            throw new Error("Expected the field `weightUnit` to be a primitive type in the JSON string but got " + data['weightUnit']);
        }

        return true;
    }


}



/**
 * @member {module:model/TravelClass} cabin
 */
Co2Emission.prototype['cabin'] = undefined;

/**
 * Weight of Co2 emitted for the concerned segment
 * @member {Number} weight
 */
Co2Emission.prototype['weight'] = undefined;

/**
 * Code to qualify unit as pounds or kilos
 * @member {String} weightUnit
 */
Co2Emission.prototype['weightUnit'] = undefined;






export default Co2Emission;

