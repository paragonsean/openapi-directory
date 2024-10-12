/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import FlightObject from './FlightObject';
import Pagination from './Pagination';

/**
 * The FlightObjectListResponse model module.
 * @module model/FlightObjectListResponse
 * @version v1
 */
class FlightObjectListResponse {
    /**
     * Constructs a new <code>FlightObjectListResponse</code>.
     * @alias module:model/FlightObjectListResponse
     */
    constructor() { 
        
        FlightObjectListResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FlightObjectListResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FlightObjectListResponse} obj Optional instance to populate.
     * @return {module:model/FlightObjectListResponse} The populated <code>FlightObjectListResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FlightObjectListResponse();

            if (data.hasOwnProperty('pagination')) {
                obj['pagination'] = Pagination.constructFromObject(data['pagination']);
            }
            if (data.hasOwnProperty('resources')) {
                obj['resources'] = ApiClient.convertToType(data['resources'], [FlightObject]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FlightObjectListResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FlightObjectListResponse</code>.
     */
    static validateJSON(data) {
        // validate the optional field `pagination`
        if (data['pagination']) { // data not null
          Pagination.validateJSON(data['pagination']);
        }
        if (data['resources']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['resources'])) {
                throw new Error("Expected the field `resources` to be an array in the JSON data but got " + data['resources']);
            }
            // validate the optional field `resources` (array)
            for (const item of data['resources']) {
                FlightObject.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/Pagination} pagination
 */
FlightObjectListResponse.prototype['pagination'] = undefined;

/**
 * Resources corresponding to the list request.
 * @member {Array.<module:model/FlightObject>} resources
 */
FlightObjectListResponse.prototype['resources'] = undefined;






export default FlightObjectListResponse;

