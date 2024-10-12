/**
 * Interactive documentation for your Premium plan
 *   This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the `GET` button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the `Parameters` section and hit `Execute` to view a full API response. You can then inspect the JSON response, copy the `curl` command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
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
import ValidationError from './ValidationError';

/**
 * The HTTPValidationError model module.
 * @module model/HTTPValidationError
 * @version v1
 */
class HTTPValidationError {
    /**
     * Constructs a new <code>HTTPValidationError</code>.
     * @alias module:model/HTTPValidationError
     */
    constructor() { 
        
        HTTPValidationError.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>HTTPValidationError</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HTTPValidationError} obj Optional instance to populate.
     * @return {module:model/HTTPValidationError} The populated <code>HTTPValidationError</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HTTPValidationError();

            if (data.hasOwnProperty('detail')) {
                obj['detail'] = ApiClient.convertToType(data['detail'], [ValidationError]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HTTPValidationError</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HTTPValidationError</code>.
     */
    static validateJSON(data) {
        if (data['detail']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['detail'])) {
                throw new Error("Expected the field `detail` to be an array in the JSON data but got " + data['detail']);
            }
            // validate the optional field `detail` (array)
            for (const item of data['detail']) {
                ValidationError.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ValidationError>} detail
 */
HTTPValidationError.prototype['detail'] = undefined;






export default HTTPValidationError;

