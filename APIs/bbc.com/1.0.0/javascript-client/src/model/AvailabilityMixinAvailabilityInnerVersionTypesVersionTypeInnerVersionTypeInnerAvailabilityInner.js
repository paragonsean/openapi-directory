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
import AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes from './AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes';

/**
 * The AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner model module.
 * @module model/AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner
 * @version 1.0.0
 */
class AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner {
    /**
     * Constructs a new <code>AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner</code>.
     * @alias module:model/AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner
     * @param status {String} 
     * @param versionTypes {module:model/AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes} 
     */
    constructor(status, versionTypes) { 
        
        AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner.initialize(this, status, versionTypes);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, status, versionTypes) { 
        obj['status'] = status;
        obj['version_types'] = versionTypes;
    }

    /**
     * Constructs a <code>AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner} obj Optional instance to populate.
     * @return {module:model/AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner} The populated <code>AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner();

            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('version_types')) {
                obj['version_types'] = AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes.constructFromObject(data['version_types']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // validate the optional field `version_types`
        if (data['version_types']) { // data not null
          AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes.validateJSON(data['version_types']);
        }

        return true;
    }


}

AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner.RequiredProperties = ["status", "version_types"];

/**
 * @member {String} status
 */
AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner.prototype['status'] = undefined;

/**
 * @member {module:model/AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInnerVersionTypes} version_types
 */
AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner.prototype['version_types'] = undefined;






export default AvailabilityMixinAvailabilityInnerVersionTypesVersionTypeInnerVersionTypeInnerAvailabilityInner;

