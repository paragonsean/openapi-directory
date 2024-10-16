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
 * The DistributionGroupAADGroupResponse model module.
 * @module model/DistributionGroupAADGroupResponse
 * @version v0.1
 */
class DistributionGroupAADGroupResponse {
    /**
     * Constructs a new <code>DistributionGroupAADGroupResponse</code>.
     * @alias module:model/DistributionGroupAADGroupResponse
     */
    constructor() { 
        
        DistributionGroupAADGroupResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DistributionGroupAADGroupResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DistributionGroupAADGroupResponse} obj Optional instance to populate.
     * @return {module:model/DistributionGroupAADGroupResponse} The populated <code>DistributionGroupAADGroupResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DistributionGroupAADGroupResponse();

            if (data.hasOwnProperty('aad_group_id')) {
                obj['aad_group_id'] = ApiClient.convertToType(data['aad_group_id'], 'String');
            }
            if (data.hasOwnProperty('display_name')) {
                obj['display_name'] = ApiClient.convertToType(data['display_name'], 'String');
            }
            if (data.hasOwnProperty('distribution_group_name')) {
                obj['distribution_group_name'] = ApiClient.convertToType(data['distribution_group_name'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('is_aad_group')) {
                obj['is_aad_group'] = ApiClient.convertToType(data['is_aad_group'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DistributionGroupAADGroupResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DistributionGroupAADGroupResponse</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['aad_group_id'] && !(typeof data['aad_group_id'] === 'string' || data['aad_group_id'] instanceof String)) {
            throw new Error("Expected the field `aad_group_id` to be a primitive type in the JSON string but got " + data['aad_group_id']);
        }
        // ensure the json data is a string
        if (data['display_name'] && !(typeof data['display_name'] === 'string' || data['display_name'] instanceof String)) {
            throw new Error("Expected the field `display_name` to be a primitive type in the JSON string but got " + data['display_name']);
        }
        // ensure the json data is a string
        if (data['distribution_group_name'] && !(typeof data['distribution_group_name'] === 'string' || data['distribution_group_name'] instanceof String)) {
            throw new Error("Expected the field `distribution_group_name` to be a primitive type in the JSON string but got " + data['distribution_group_name']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}



/**
 * The AAD unique id (UUID) of the AAD group.
 * @member {String} aad_group_id
 */
DistributionGroupAADGroupResponse.prototype['aad_group_id'] = undefined;

/**
 * The display name of the AAD group
 * @member {String} display_name
 */
DistributionGroupAADGroupResponse.prototype['display_name'] = undefined;

/**
 * The distribution group of the AAD group
 * @member {String} distribution_group_name
 */
DistributionGroupAADGroupResponse.prototype['distribution_group_name'] = undefined;

/**
 * The internal unique id (UUID) of the AAD group.
 * @member {String} id
 */
DistributionGroupAADGroupResponse.prototype['id'] = undefined;

/**
 * @member {Boolean} is_aad_group
 */
DistributionGroupAADGroupResponse.prototype['is_aad_group'] = undefined;






export default DistributionGroupAADGroupResponse;

