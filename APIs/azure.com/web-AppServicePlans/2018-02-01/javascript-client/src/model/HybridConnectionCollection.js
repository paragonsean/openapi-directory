/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import HybridConnectionCollectionValueInner from './HybridConnectionCollectionValueInner';

/**
 * The HybridConnectionCollection model module.
 * @module model/HybridConnectionCollection
 * @version 2018-02-01
 */
class HybridConnectionCollection {
    /**
     * Constructs a new <code>HybridConnectionCollection</code>.
     * Collection of hostname bindings.
     * @alias module:model/HybridConnectionCollection
     * @param value {Array.<module:model/HybridConnectionCollectionValueInner>} Collection of resources.
     */
    constructor(value) { 
        
        HybridConnectionCollection.initialize(this, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, value) { 
        obj['value'] = value;
    }

    /**
     * Constructs a <code>HybridConnectionCollection</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HybridConnectionCollection} obj Optional instance to populate.
     * @return {module:model/HybridConnectionCollection} The populated <code>HybridConnectionCollection</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HybridConnectionCollection();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [HybridConnectionCollectionValueInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HybridConnectionCollection</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HybridConnectionCollection</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of HybridConnectionCollection.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['nextLink'] && !(typeof data['nextLink'] === 'string' || data['nextLink'] instanceof String)) {
            throw new Error("Expected the field `nextLink` to be a primitive type in the JSON string but got " + data['nextLink']);
        }
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                HybridConnectionCollectionValueInner.validateJSON(item);
            };
        }

        return true;
    }


}

HybridConnectionCollection.RequiredProperties = ["value"];

/**
 * Link to next page of resources.
 * @member {String} nextLink
 */
HybridConnectionCollection.prototype['nextLink'] = undefined;

/**
 * Collection of resources.
 * @member {Array.<module:model/HybridConnectionCollectionValueInner>} value
 */
HybridConnectionCollection.prototype['value'] = undefined;






export default HybridConnectionCollection;

