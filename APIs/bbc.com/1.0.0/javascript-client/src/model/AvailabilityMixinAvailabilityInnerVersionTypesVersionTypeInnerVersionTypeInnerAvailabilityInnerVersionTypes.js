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
import AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypesVersionTypeInner from './AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypesVersionTypeInner';

/**
 * The AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes model module.
 * @module model/AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes
 * @version 1.0.0
 */
class AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes {
    /**
     * Constructs a new <code>AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes</code>.
     * @alias module:model/AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes
     * @param versionType {Array.<module:model/AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypesVersionTypeInner>} 
     */
    constructor(versionType) { 
        
        AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes.initialize(this, versionType);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, versionType) { 
        obj['version_type'] = versionType;
    }

    /**
     * Constructs a <code>AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes} obj Optional instance to populate.
     * @return {module:model/AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes} The populated <code>AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes();

            if (data.hasOwnProperty('version_type')) {
                obj['version_type'] = ApiClient.convertToType(data['version_type'], [AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypesVersionTypeInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['version_type']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['version_type'])) {
                throw new Error("Expected the field `version_type` to be an array in the JSON data but got " + data['version_type']);
            }
            // validate the optional field `version_type` (array)
            for (const item of data['version_type']) {
                AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypesVersionTypeInner.validateJSON(item);
            };
        }

        return true;
    }


}

AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes.RequiredProperties = ["version_type"];

/**
 * @member {Array.<module:model/AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypesVersionTypeInner>} version_type
 */
AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes.prototype['version_type'] = undefined;






export default AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes;

