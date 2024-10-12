/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ImageTagCreateEntry from './ImageTagCreateEntry';

/**
 * The ImageTagCreateSummary model module.
 * @module model/ImageTagCreateSummary
 * @version 3.1
 */
class ImageTagCreateSummary {
    /**
     * Constructs a new <code>ImageTagCreateSummary</code>.
     * @alias module:model/ImageTagCreateSummary
     */
    constructor() { 
        
        ImageTagCreateSummary.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageTagCreateSummary</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageTagCreateSummary} obj Optional instance to populate.
     * @return {module:model/ImageTagCreateSummary} The populated <code>ImageTagCreateSummary</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageTagCreateSummary();

            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], [ImageTagCreateEntry]);
            }
            if (data.hasOwnProperty('duplicated')) {
                obj['duplicated'] = ApiClient.convertToType(data['duplicated'], [ImageTagCreateEntry]);
            }
            if (data.hasOwnProperty('exceeded')) {
                obj['exceeded'] = ApiClient.convertToType(data['exceeded'], [ImageTagCreateEntry]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageTagCreateSummary</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageTagCreateSummary</code>.
     */
    static validateJSON(data) {
        if (data['created']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['created'])) {
                throw new Error("Expected the field `created` to be an array in the JSON data but got " + data['created']);
            }
            // validate the optional field `created` (array)
            for (const item of data['created']) {
                ImageTagCreateEntry.validateJSON(item);
            };
        }
        if (data['duplicated']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['duplicated'])) {
                throw new Error("Expected the field `duplicated` to be an array in the JSON data but got " + data['duplicated']);
            }
            // validate the optional field `duplicated` (array)
            for (const item of data['duplicated']) {
                ImageTagCreateEntry.validateJSON(item);
            };
        }
        if (data['exceeded']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['exceeded'])) {
                throw new Error("Expected the field `exceeded` to be an array in the JSON data but got " + data['exceeded']);
            }
            // validate the optional field `exceeded` (array)
            for (const item of data['exceeded']) {
                ImageTagCreateEntry.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ImageTagCreateEntry>} created
 */
ImageTagCreateSummary.prototype['created'] = undefined;

/**
 * @member {Array.<module:model/ImageTagCreateEntry>} duplicated
 */
ImageTagCreateSummary.prototype['duplicated'] = undefined;

/**
 * @member {Array.<module:model/ImageTagCreateEntry>} exceeded
 */
ImageTagCreateSummary.prototype['exceeded'] = undefined;






export default ImageTagCreateSummary;

