/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import OneWayCombinations from './OneWayCombinations';

/**
 * The CollectionMeta model module.
 * @module model/CollectionMeta
 * @version 2.2.0
 */
class CollectionMeta {
    /**
     * Constructs a new <code>CollectionMeta</code>.
     * @alias module:model/CollectionMeta
     */
    constructor() { 
        
        CollectionMeta.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CollectionMeta</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CollectionMeta} obj Optional instance to populate.
     * @return {module:model/CollectionMeta} The populated <code>CollectionMeta</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CollectionMeta();

            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('oneWayCombinations')) {
                obj['oneWayCombinations'] = ApiClient.convertToType(data['oneWayCombinations'], [OneWayCombinations]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CollectionMeta</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CollectionMeta</code>.
     */
    static validateJSON(data) {
        if (data['oneWayCombinations']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['oneWayCombinations'])) {
                throw new Error("Expected the field `oneWayCombinations` to be an array in the JSON data but got " + data['oneWayCombinations']);
            }
            // validate the optional field `oneWayCombinations` (array)
            for (const item of data['oneWayCombinations']) {
                OneWayCombinations.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Number} count
 */
CollectionMeta.prototype['count'] = undefined;

/**
 * @member {Array.<module:model/OneWayCombinations>} oneWayCombinations
 */
CollectionMeta.prototype['oneWayCombinations'] = undefined;






export default CollectionMeta;

