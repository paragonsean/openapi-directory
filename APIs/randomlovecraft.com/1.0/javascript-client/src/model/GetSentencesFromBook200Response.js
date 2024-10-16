/**
 * Random Lovecraft
 * Random sentences from the complete works of H.P. Lovecraft. CORS-enabled.
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
import Sentence from './Sentence';

/**
 * The GetSentencesFromBook200Response model module.
 * @module model/GetSentencesFromBook200Response
 * @version 1.0
 */
class GetSentencesFromBook200Response {
    /**
     * Constructs a new <code>GetSentencesFromBook200Response</code>.
     * @alias module:model/GetSentencesFromBook200Response
     */
    constructor() { 
        
        GetSentencesFromBook200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetSentencesFromBook200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetSentencesFromBook200Response} obj Optional instance to populate.
     * @return {module:model/GetSentencesFromBook200Response} The populated <code>GetSentencesFromBook200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetSentencesFromBook200Response();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ApiClient.convertToType(data['data'], [Sentence]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetSentencesFromBook200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetSentencesFromBook200Response</code>.
     */
    static validateJSON(data) {
        if (data['data']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['data'])) {
                throw new Error("Expected the field `data` to be an array in the JSON data but got " + data['data']);
            }
            // validate the optional field `data` (array)
            for (const item of data['data']) {
                Sentence.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Sentence>} data
 */
GetSentencesFromBook200Response.prototype['data'] = undefined;






export default GetSentencesFromBook200Response;

