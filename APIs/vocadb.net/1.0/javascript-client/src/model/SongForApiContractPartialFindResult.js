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
import SongForApiContract from './SongForApiContract';

/**
 * The SongForApiContractPartialFindResult model module.
 * @module model/SongForApiContractPartialFindResult
 * @version 1.0
 */
class SongForApiContractPartialFindResult {
    /**
     * Constructs a new <code>SongForApiContractPartialFindResult</code>.
     * @alias module:model/SongForApiContractPartialFindResult
     */
    constructor() { 
        
        SongForApiContractPartialFindResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SongForApiContractPartialFindResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SongForApiContractPartialFindResult} obj Optional instance to populate.
     * @return {module:model/SongForApiContractPartialFindResult} The populated <code>SongForApiContractPartialFindResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SongForApiContractPartialFindResult();

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [SongForApiContract]);
            }
            if (data.hasOwnProperty('term')) {
                obj['term'] = ApiClient.convertToType(data['term'], 'String');
            }
            if (data.hasOwnProperty('totalCount')) {
                obj['totalCount'] = ApiClient.convertToType(data['totalCount'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SongForApiContractPartialFindResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SongForApiContractPartialFindResult</code>.
     */
    static validateJSON(data) {
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                SongForApiContract.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['term'] && !(typeof data['term'] === 'string' || data['term'] instanceof String)) {
            throw new Error("Expected the field `term` to be a primitive type in the JSON string but got " + data['term']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/SongForApiContract>} items
 */
SongForApiContractPartialFindResult.prototype['items'] = undefined;

/**
 * @member {String} term
 */
SongForApiContractPartialFindResult.prototype['term'] = undefined;

/**
 * @member {Number} totalCount
 */
SongForApiContractPartialFindResult.prototype['totalCount'] = undefined;






export default SongForApiContractPartialFindResult;

