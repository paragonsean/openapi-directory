/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
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
import EntityName from './EntityName';

/**
 * The NamesResponse model module.
 * @module model/NamesResponse
 * @version 1.0.0
 */
class NamesResponse {
    /**
     * Constructs a new <code>NamesResponse</code>.
     * @alias module:model/NamesResponse
     */
    constructor() { 
        
        NamesResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>NamesResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NamesResponse} obj Optional instance to populate.
     * @return {module:model/NamesResponse} The populated <code>NamesResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NamesResponse();

            if (data.hasOwnProperty('entities')) {
                obj['entities'] = ApiClient.convertToType(data['entities'], [EntityName]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NamesResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NamesResponse</code>.
     */
    static validateJSON(data) {
        if (data['entities']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['entities'])) {
                throw new Error("Expected the field `entities` to be an array in the JSON data but got " + data['entities']);
            }
            // validate the optional field `entities` (array)
            for (const item of data['entities']) {
                EntityName.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/EntityName>} entities
 */
NamesResponse.prototype['entities'] = undefined;






export default NamesResponse;

