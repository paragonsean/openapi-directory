/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Sort from './Sort';
import UnstableSorts from './UnstableSorts';

/**
 * The Sorts model module.
 * @module model/Sorts
 * @version 1.0.0
 */
class Sorts {
    /**
     * Constructs a new <code>Sorts</code>.
     * @alias module:model/Sorts
     */
    constructor() { 
        
        Sorts.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Sorts</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Sorts} obj Optional instance to populate.
     * @return {module:model/Sorts} The populated <code>Sorts</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Sorts();

            if (data.hasOwnProperty('sort')) {
                obj['sort'] = ApiClient.convertToType(data['sort'], [Sort]);
            }
            if (data.hasOwnProperty('unstable_sorts')) {
                obj['unstable_sorts'] = UnstableSorts.constructFromObject(data['unstable_sorts']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Sorts</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Sorts</code>.
     */
    static validateJSON(data) {
        if (data['sort']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['sort'])) {
                throw new Error("Expected the field `sort` to be an array in the JSON data but got " + data['sort']);
            }
            // validate the optional field `sort` (array)
            for (const item of data['sort']) {
                Sort.validateJSON(item);
            };
        }
        // validate the optional field `unstable_sorts`
        if (data['unstable_sorts']) { // data not null
          UnstableSorts.validateJSON(data['unstable_sorts']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Sort>} sort
 */
Sorts.prototype['sort'] = undefined;

/**
 * @member {module:model/UnstableSorts} unstable_sorts
 */
Sorts.prototype['unstable_sorts'] = undefined;






export default Sorts;

