/**
 * Azure Media Services
 * This Swagger was generated by the API Framework.
 *
 * The version of the OpenAPI document: 2018-07-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ODataError from './ODataError';

/**
 * The ApiError model module.
 * @module model/ApiError
 * @version 2018-07-01
 */
class ApiError {
    /**
     * Constructs a new <code>ApiError</code>.
     * The API error.
     * @alias module:model/ApiError
     */
    constructor() { 
        
        ApiError.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApiError</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiError} obj Optional instance to populate.
     * @return {module:model/ApiError} The populated <code>ApiError</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiError();

            if (data.hasOwnProperty('error')) {
                obj['error'] = ODataError.constructFromObject(data['error']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiError</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiError</code>.
     */
    static validateJSON(data) {
        // validate the optional field `error`
        if (data['error']) { // data not null
          ODataError.validateJSON(data['error']);
        }

        return true;
    }


}



/**
 * @member {module:model/ODataError} error
 */
ApiError.prototype['error'] = undefined;






export default ApiError;

