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
import OffsetIn from './OffsetIn';

/**
 * The Offsets model module.
 * @module model/Offsets
 * @version 1.0.0
 */
class Offsets {
    /**
     * Constructs a new <code>Offsets</code>.
     * @alias module:model/Offsets
     */
    constructor() { 
        
        Offsets.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Offsets</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Offsets} obj Optional instance to populate.
     * @return {module:model/Offsets} The populated <code>Offsets</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Offsets();

            if (data.hasOwnProperty('offset_in')) {
                obj['offset_in'] = ApiClient.convertToType(data['offset_in'], [OffsetIn]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Offsets</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Offsets</code>.
     */
    static validateJSON(data) {
        if (data['offset_in']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['offset_in'])) {
                throw new Error("Expected the field `offset_in` to be an array in the JSON data but got " + data['offset_in']);
            }
            // validate the optional field `offset_in` (array)
            for (const item of data['offset_in']) {
                OffsetIn.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/OffsetIn>} offset_in
 */
Offsets.prototype['offset_in'] = undefined;






export default Offsets;

