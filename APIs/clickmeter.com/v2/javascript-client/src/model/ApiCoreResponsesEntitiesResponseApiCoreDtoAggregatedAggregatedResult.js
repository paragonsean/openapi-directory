/**
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ApiCoreDtoAggregatedAggregatedResult from './ApiCoreDtoAggregatedAggregatedResult';

/**
 * The ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult model module.
 * @module model/ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult
 * @version v2
 */
class ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult {
    /**
     * Constructs a new <code>ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult</code>.
     * @alias module:model/ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult
     */
    constructor() { 
        
        ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult} obj Optional instance to populate.
     * @return {module:model/ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult} The populated <code>ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult();

            if (data.hasOwnProperty('entities')) {
                obj['entities'] = ApiClient.convertToType(data['entities'], [ApiCoreDtoAggregatedAggregatedResult]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult</code>.
     */
    static validateJSON(data) {
        if (data['entities']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['entities'])) {
                throw new Error("Expected the field `entities` to be an array in the JSON data but got " + data['entities']);
            }
            // validate the optional field `entities` (array)
            for (const item of data['entities']) {
                ApiCoreDtoAggregatedAggregatedResult.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ApiCoreDtoAggregatedAggregatedResult>} entities
 */
ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult.prototype['entities'] = undefined;






export default ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult;

