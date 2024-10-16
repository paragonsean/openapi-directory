/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
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
import PodcastError from './PodcastError';

/**
 * The PodcastErrorResponse model module.
 * @module model/PodcastErrorResponse
 * @version 1.0.0
 */
class PodcastErrorResponse {
    /**
     * Constructs a new <code>PodcastErrorResponse</code>.
     * @alias module:model/PodcastErrorResponse
     */
    constructor() { 
        
        PodcastErrorResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PodcastErrorResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PodcastErrorResponse} obj Optional instance to populate.
     * @return {module:model/PodcastErrorResponse} The populated <code>PodcastErrorResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PodcastErrorResponse();

            if (data.hasOwnProperty('$schema')) {
                obj['$schema'] = ApiClient.convertToType(data['$schema'], 'String');
            }
            if (data.hasOwnProperty('errors')) {
                obj['errors'] = ApiClient.convertToType(data['errors'], [PodcastError]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PodcastErrorResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PodcastErrorResponse</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['$schema'] && !(typeof data['$schema'] === 'string' || data['$schema'] instanceof String)) {
            throw new Error("Expected the field `$schema` to be a primitive type in the JSON string but got " + data['$schema']);
        }
        if (data['errors']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['errors'])) {
                throw new Error("Expected the field `errors` to be an array in the JSON data but got " + data['errors']);
            }
            // validate the optional field `errors` (array)
            for (const item of data['errors']) {
                PodcastError.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {String} $schema
 */
PodcastErrorResponse.prototype['$schema'] = undefined;

/**
 * @member {Array.<module:model/PodcastError>} errors
 */
PodcastErrorResponse.prototype['errors'] = undefined;






export default PodcastErrorResponse;

