/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The OptionalGeoPointContract model module.
 * @module model/OptionalGeoPointContract
 * @version 1.0
 */
class OptionalGeoPointContract {
    /**
     * Constructs a new <code>OptionalGeoPointContract</code>.
     * @alias module:model/OptionalGeoPointContract
     */
    constructor() { 
        
        OptionalGeoPointContract.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OptionalGeoPointContract</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OptionalGeoPointContract} obj Optional instance to populate.
     * @return {module:model/OptionalGeoPointContract} The populated <code>OptionalGeoPointContract</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OptionalGeoPointContract();

            if (data.hasOwnProperty('formatted')) {
                obj['formatted'] = ApiClient.convertToType(data['formatted'], 'String');
            }
            if (data.hasOwnProperty('hasValue')) {
                obj['hasValue'] = ApiClient.convertToType(data['hasValue'], 'Boolean');
            }
            if (data.hasOwnProperty('latitude')) {
                obj['latitude'] = ApiClient.convertToType(data['latitude'], 'Number');
            }
            if (data.hasOwnProperty('longitude')) {
                obj['longitude'] = ApiClient.convertToType(data['longitude'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OptionalGeoPointContract</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OptionalGeoPointContract</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['formatted'] && !(typeof data['formatted'] === 'string' || data['formatted'] instanceof String)) {
            throw new Error("Expected the field `formatted` to be a primitive type in the JSON string but got " + data['formatted']);
        }

        return true;
    }


}



/**
 * @member {String} formatted
 */
OptionalGeoPointContract.prototype['formatted'] = undefined;

/**
 * @member {Boolean} hasValue
 */
OptionalGeoPointContract.prototype['hasValue'] = undefined;

/**
 * @member {Number} latitude
 */
OptionalGeoPointContract.prototype['latitude'] = undefined;

/**
 * @member {Number} longitude
 */
OptionalGeoPointContract.prototype['longitude'] = undefined;






export default OptionalGeoPointContract;

