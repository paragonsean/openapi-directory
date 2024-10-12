/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import RegionProposal from './RegionProposal';

/**
 * The ImageRegionProposal model module.
 * @module model/ImageRegionProposal
 * @version 3.2
 */
class ImageRegionProposal {
    /**
     * Constructs a new <code>ImageRegionProposal</code>.
     * @alias module:model/ImageRegionProposal
     */
    constructor() { 
        
        ImageRegionProposal.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageRegionProposal</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageRegionProposal} obj Optional instance to populate.
     * @return {module:model/ImageRegionProposal} The populated <code>ImageRegionProposal</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageRegionProposal();

            if (data.hasOwnProperty('imageId')) {
                obj['imageId'] = ApiClient.convertToType(data['imageId'], 'String');
            }
            if (data.hasOwnProperty('projectId')) {
                obj['projectId'] = ApiClient.convertToType(data['projectId'], 'String');
            }
            if (data.hasOwnProperty('proposals')) {
                obj['proposals'] = ApiClient.convertToType(data['proposals'], [RegionProposal]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageRegionProposal</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageRegionProposal</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['imageId'] && !(typeof data['imageId'] === 'string' || data['imageId'] instanceof String)) {
            throw new Error("Expected the field `imageId` to be a primitive type in the JSON string but got " + data['imageId']);
        }
        // ensure the json data is a string
        if (data['projectId'] && !(typeof data['projectId'] === 'string' || data['projectId'] instanceof String)) {
            throw new Error("Expected the field `projectId` to be a primitive type in the JSON string but got " + data['projectId']);
        }
        if (data['proposals']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['proposals'])) {
                throw new Error("Expected the field `proposals` to be an array in the JSON data but got " + data['proposals']);
            }
            // validate the optional field `proposals` (array)
            for (const item of data['proposals']) {
                RegionProposal.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {String} imageId
 */
ImageRegionProposal.prototype['imageId'] = undefined;

/**
 * @member {String} projectId
 */
ImageRegionProposal.prototype['projectId'] = undefined;

/**
 * @member {Array.<module:model/RegionProposal>} proposals
 */
ImageRegionProposal.prototype['proposals'] = undefined;






export default ImageRegionProposal;

