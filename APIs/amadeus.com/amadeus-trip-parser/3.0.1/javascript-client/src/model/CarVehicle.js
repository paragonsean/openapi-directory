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
 * The CarVehicle model module.
 * @module model/CarVehicle
 * @version 3.0.1
 */
class CarVehicle {
    /**
     * Constructs a new <code>CarVehicle</code>.
     * @alias module:model/CarVehicle
     */
    constructor() { 
        
        CarVehicle.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CarVehicle</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CarVehicle} obj Optional instance to populate.
     * @return {module:model/CarVehicle} The populated <code>CarVehicle</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CarVehicle();

            if (data.hasOwnProperty('acrissCode')) {
                obj['acrissCode'] = ApiClient.convertToType(data['acrissCode'], 'String');
            }
            if (data.hasOwnProperty('carModel')) {
                obj['carModel'] = ApiClient.convertToType(data['carModel'], 'String');
            }
            if (data.hasOwnProperty('doors')) {
                obj['doors'] = ApiClient.convertToType(data['doors'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CarVehicle</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CarVehicle</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['acrissCode'] && !(typeof data['acrissCode'] === 'string' || data['acrissCode'] instanceof String)) {
            throw new Error("Expected the field `acrissCode` to be a primitive type in the JSON string but got " + data['acrissCode']);
        }
        // ensure the json data is a string
        if (data['carModel'] && !(typeof data['carModel'] === 'string' || data['carModel'] instanceof String)) {
            throw new Error("Expected the field `carModel` to be a primitive type in the JSON string but got " + data['carModel']);
        }

        return true;
    }


}



/**
 * Association of car rental industry systems standards
 * @member {String} acrissCode
 */
CarVehicle.prototype['acrissCode'] = undefined;

/**
 * Car model name
 * @member {String} carModel
 */
CarVehicle.prototype['carModel'] = undefined;

/**
 * Number of doors
 * @member {Number} doors
 */
CarVehicle.prototype['doors'] = undefined;






export default CarVehicle;

