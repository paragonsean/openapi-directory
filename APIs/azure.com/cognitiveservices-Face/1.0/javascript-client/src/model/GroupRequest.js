/**
 * Face Client
 * An API for face detection, verification, and identification.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GroupRequest model module.
 * @module model/GroupRequest
 * @version 1.0
 */
class GroupRequest {
    /**
     * Constructs a new <code>GroupRequest</code>.
     * Request body for group request.
     * @alias module:model/GroupRequest
     * @param faceIds {Array.<String>} Array of candidate faceId created by Face - Detect. The maximum is 1000 faces
     */
    constructor(faceIds) { 
        
        GroupRequest.initialize(this, faceIds);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, faceIds) { 
        obj['faceIds'] = faceIds;
    }

    /**
     * Constructs a <code>GroupRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GroupRequest} obj Optional instance to populate.
     * @return {module:model/GroupRequest} The populated <code>GroupRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GroupRequest();

            if (data.hasOwnProperty('faceIds')) {
                obj['faceIds'] = ApiClient.convertToType(data['faceIds'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GroupRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GroupRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GroupRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['faceIds'])) {
            throw new Error("Expected the field `faceIds` to be an array in the JSON data but got " + data['faceIds']);
        }

        return true;
    }


}

GroupRequest.RequiredProperties = ["faceIds"];

/**
 * Array of candidate faceId created by Face - Detect. The maximum is 1000 faces
 * @member {Array.<String>} faceIds
 */
GroupRequest.prototype['faceIds'] = undefined;






export default GroupRequest;

