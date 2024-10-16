/**
 * Background Removal API
 * Remove the background of any image
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import RemovebgPost402ResponseErrorsInner from './RemovebgPost402ResponseErrorsInner';

/**
 * The RemovebgPost402Response model module.
 * @module model/RemovebgPost402Response
 * @version 1.0.0
 */
class RemovebgPost402Response {
    /**
     * Constructs a new <code>RemovebgPost402Response</code>.
     * @alias module:model/RemovebgPost402Response
     */
    constructor() { 
        
        RemovebgPost402Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RemovebgPost402Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RemovebgPost402Response} obj Optional instance to populate.
     * @return {module:model/RemovebgPost402Response} The populated <code>RemovebgPost402Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RemovebgPost402Response();

            if (data.hasOwnProperty('errors')) {
                obj['errors'] = ApiClient.convertToType(data['errors'], [RemovebgPost402ResponseErrorsInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RemovebgPost402Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RemovebgPost402Response</code>.
     */
    static validateJSON(data) {
        if (data['errors']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['errors'])) {
                throw new Error("Expected the field `errors` to be an array in the JSON data but got " + data['errors']);
            }
            // validate the optional field `errors` (array)
            for (const item of data['errors']) {
                RemovebgPost402ResponseErrorsInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/RemovebgPost402ResponseErrorsInner>} errors
 */
RemovebgPost402Response.prototype['errors'] = undefined;






export default RemovebgPost402Response;

