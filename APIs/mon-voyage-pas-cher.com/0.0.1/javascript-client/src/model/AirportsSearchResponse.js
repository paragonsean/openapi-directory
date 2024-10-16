/**
 * Mon-voyage-pas-cher.com Public API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import DataAirportsSearch from './DataAirportsSearch';

/**
 * The AirportsSearchResponse model module.
 * @module model/AirportsSearchResponse
 * @version 0.0.1
 */
class AirportsSearchResponse {
    /**
     * Constructs a new <code>AirportsSearchResponse</code>.
     * This section provides response schema of Airport Search Response
     * @alias module:model/AirportsSearchResponse
     */
    constructor() { 
        
        AirportsSearchResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AirportsSearchResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AirportsSearchResponse} obj Optional instance to populate.
     * @return {module:model/AirportsSearchResponse} The populated <code>AirportsSearchResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AirportsSearchResponse();

            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('data')) {
                obj['data'] = ApiClient.convertToType(data['data'], [DataAirportsSearch]);
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AirportsSearchResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AirportsSearchResponse</code>.
     */
    static validateJSON(data) {
        if (data['data']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['data'])) {
                throw new Error("Expected the field `data` to be an array in the JSON data but got " + data['data']);
            }
            // validate the optional field `data` (array)
            for (const item of data['data']) {
                DataAirportsSearch.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * @member {Number} count
 */
AirportsSearchResponse.prototype['count'] = undefined;

/**
 * @member {Array.<module:model/DataAirportsSearch>} data
 */
AirportsSearchResponse.prototype['data'] = undefined;

/**
 * @member {String} message
 */
AirportsSearchResponse.prototype['message'] = undefined;

/**
 * Status of the response
 * @member {String} status
 */
AirportsSearchResponse.prototype['status'] = undefined;






export default AirportsSearchResponse;

