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
import AvailableMediaSetsMediaSetsMediaSetInner from './AvailableMediaSetsMediaSetsMediaSetInner';

/**
 * The AvailableMediaSetsMediaSets model module.
 * @module model/AvailableMediaSetsMediaSets
 * @version 1.0.0
 */
class AvailableMediaSetsMediaSets {
    /**
     * Constructs a new <code>AvailableMediaSetsMediaSets</code>.
     * @alias module:model/AvailableMediaSetsMediaSets
     * @param mediaSet {Array.<module:model/AvailableMediaSetsMediaSetsMediaSetInner>} 
     */
    constructor(mediaSet) { 
        
        AvailableMediaSetsMediaSets.initialize(this, mediaSet);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, mediaSet) { 
        obj['media_set'] = mediaSet;
    }

    /**
     * Constructs a <code>AvailableMediaSetsMediaSets</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AvailableMediaSetsMediaSets} obj Optional instance to populate.
     * @return {module:model/AvailableMediaSetsMediaSets} The populated <code>AvailableMediaSetsMediaSets</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AvailableMediaSetsMediaSets();

            if (data.hasOwnProperty('media_set')) {
                obj['media_set'] = ApiClient.convertToType(data['media_set'], [AvailableMediaSetsMediaSetsMediaSetInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AvailableMediaSetsMediaSets</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AvailableMediaSetsMediaSets</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AvailableMediaSetsMediaSets.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['media_set']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['media_set'])) {
                throw new Error("Expected the field `media_set` to be an array in the JSON data but got " + data['media_set']);
            }
            // validate the optional field `media_set` (array)
            for (const item of data['media_set']) {
                AvailableMediaSetsMediaSetsMediaSetInner.validateJSON(item);
            };
        }

        return true;
    }


}

AvailableMediaSetsMediaSets.RequiredProperties = ["media_set"];

/**
 * @member {Array.<module:model/AvailableMediaSetsMediaSetsMediaSetInner>} media_set
 */
AvailableMediaSetsMediaSets.prototype['media_set'] = undefined;






export default AvailableMediaSetsMediaSets;

