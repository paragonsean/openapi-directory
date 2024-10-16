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
 * The DistributionGroupsUserVerifyRequest model module.
 * @module model/DistributionGroupsUserVerifyRequest
 * @version v0.1
 */
class DistributionGroupsUserVerifyRequest {
    /**
     * Constructs a new <code>DistributionGroupsUserVerifyRequest</code>.
     * @alias module:model/DistributionGroupsUserVerifyRequest
     * @param distributionGroupIds {Array.<String>} An array of distribution group ids
     */
    constructor(distributionGroupIds) { 
        
        DistributionGroupsUserVerifyRequest.initialize(this, distributionGroupIds);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, distributionGroupIds) { 
        obj['distribution_group_ids'] = distributionGroupIds;
    }

    /**
     * Constructs a <code>DistributionGroupsUserVerifyRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DistributionGroupsUserVerifyRequest} obj Optional instance to populate.
     * @return {module:model/DistributionGroupsUserVerifyRequest} The populated <code>DistributionGroupsUserVerifyRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DistributionGroupsUserVerifyRequest();

            if (data.hasOwnProperty('distribution_group_ids')) {
                obj['distribution_group_ids'] = ApiClient.convertToType(data['distribution_group_ids'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DistributionGroupsUserVerifyRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DistributionGroupsUserVerifyRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DistributionGroupsUserVerifyRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['distribution_group_ids'])) {
            throw new Error("Expected the field `distribution_group_ids` to be an array in the JSON data but got " + data['distribution_group_ids']);
        }

        return true;
    }


}

DistributionGroupsUserVerifyRequest.RequiredProperties = ["distribution_group_ids"];

/**
 * An array of distribution group ids
 * @member {Array.<String>} distribution_group_ids
 */
DistributionGroupsUserVerifyRequest.prototype['distribution_group_ids'] = undefined;






export default DistributionGroupsUserVerifyRequest;

