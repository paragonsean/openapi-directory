/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ReleasesGetPublicGroupsForReleaseByHash200ResponseInner model module.
 * @module model/ReleasesGetPublicGroupsForReleaseByHash200ResponseInner
 * @version v0.1
 */
class ReleasesGetPublicGroupsForReleaseByHash200ResponseInner {
    /**
     * Constructs a new <code>ReleasesGetPublicGroupsForReleaseByHash200ResponseInner</code>.
     * @alias module:model/ReleasesGetPublicGroupsForReleaseByHash200ResponseInner
     * @param id {String} The id of the distribution group
     */
    constructor(id) { 
        
        ReleasesGetPublicGroupsForReleaseByHash200ResponseInner.initialize(this, id);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id) { 
        obj['id'] = id;
    }

    /**
     * Constructs a <code>ReleasesGetPublicGroupsForReleaseByHash200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ReleasesGetPublicGroupsForReleaseByHash200ResponseInner} obj Optional instance to populate.
     * @return {module:model/ReleasesGetPublicGroupsForReleaseByHash200ResponseInner} The populated <code>ReleasesGetPublicGroupsForReleaseByHash200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ReleasesGetPublicGroupsForReleaseByHash200ResponseInner();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ReleasesGetPublicGroupsForReleaseByHash200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ReleasesGetPublicGroupsForReleaseByHash200ResponseInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ReleasesGetPublicGroupsForReleaseByHash200ResponseInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}

ReleasesGetPublicGroupsForReleaseByHash200ResponseInner.RequiredProperties = ["id"];

/**
 * The id of the distribution group
 * @member {String} id
 */
ReleasesGetPublicGroupsForReleaseByHash200ResponseInner.prototype['id'] = undefined;






export default ReleasesGetPublicGroupsForReleaseByHash200ResponseInner;

