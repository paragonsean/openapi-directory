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

/**
 * The ProjectExport model module.
 * @module model/ProjectExport
 * @version 3.2
 */
class ProjectExport {
    /**
     * Constructs a new <code>ProjectExport</code>.
     * Represents information about a project export.
     * @alias module:model/ProjectExport
     */
    constructor() { 
        
        ProjectExport.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProjectExport</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProjectExport} obj Optional instance to populate.
     * @return {module:model/ProjectExport} The populated <code>ProjectExport</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProjectExport();

            if (data.hasOwnProperty('estimatedImportTimeInMS')) {
                obj['estimatedImportTimeInMS'] = ApiClient.convertToType(data['estimatedImportTimeInMS'], 'Number');
            }
            if (data.hasOwnProperty('imageCount')) {
                obj['imageCount'] = ApiClient.convertToType(data['imageCount'], 'Number');
            }
            if (data.hasOwnProperty('iterationCount')) {
                obj['iterationCount'] = ApiClient.convertToType(data['iterationCount'], 'Number');
            }
            if (data.hasOwnProperty('regionCount')) {
                obj['regionCount'] = ApiClient.convertToType(data['regionCount'], 'Number');
            }
            if (data.hasOwnProperty('tagCount')) {
                obj['tagCount'] = ApiClient.convertToType(data['tagCount'], 'Number');
            }
            if (data.hasOwnProperty('token')) {
                obj['token'] = ApiClient.convertToType(data['token'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProjectExport</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProjectExport</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['token'] && !(typeof data['token'] === 'string' || data['token'] instanceof String)) {
            throw new Error("Expected the field `token` to be a primitive type in the JSON string but got " + data['token']);
        }

        return true;
    }


}



/**
 * Estimated time this project will take to import, can change based on network connectivity and load between  source and destination regions.
 * @member {Number} estimatedImportTimeInMS
 */
ProjectExport.prototype['estimatedImportTimeInMS'] = undefined;

/**
 * Count of images that will be exported.
 * @member {Number} imageCount
 */
ProjectExport.prototype['imageCount'] = undefined;

/**
 * Count of iterations that will be exported.
 * @member {Number} iterationCount
 */
ProjectExport.prototype['iterationCount'] = undefined;

/**
 * Count of regions that will be exported.
 * @member {Number} regionCount
 */
ProjectExport.prototype['regionCount'] = undefined;

/**
 * Count of tags that will be exported.
 * @member {Number} tagCount
 */
ProjectExport.prototype['tagCount'] = undefined;

/**
 * Opaque token that should be passed to ImportProject to perform the import. This token grants access to import this  project to all that have the token.
 * @member {String} token
 */
ProjectExport.prototype['token'] = undefined;






export default ProjectExport;

