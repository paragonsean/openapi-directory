/**
 * Highways England API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Sites from './Sites';

/**
 * The SiteTypeLayer model module.
 * @module model/SiteTypeLayer
 * @version v1
 */
class SiteTypeLayer {
    /**
     * Constructs a new <code>SiteTypeLayer</code>.
     * @alias module:model/SiteTypeLayer
     */
    constructor() { 
        
        SiteTypeLayer.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SiteTypeLayer</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SiteTypeLayer} obj Optional instance to populate.
     * @return {module:model/SiteTypeLayer} The populated <code>SiteTypeLayer</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SiteTypeLayer();

            if (data.hasOwnProperty('Sites')) {
                obj['Sites'] = ApiClient.convertToType(data['Sites'], [Sites]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SiteTypeLayer</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SiteTypeLayer</code>.
     */
    static validateJSON(data) {
        if (data['Sites']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Sites'])) {
                throw new Error("Expected the field `Sites` to be an array in the JSON data but got " + data['Sites']);
            }
            // validate the optional field `Sites` (array)
            for (const item of data['Sites']) {
                Sites.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Sites>} Sites
 */
SiteTypeLayer.prototype['Sites'] = undefined;






export default SiteTypeLayer;

