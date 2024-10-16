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
 * The AppDistributionGroupUsersRequest model module.
 * @module model/AppDistributionGroupUsersRequest
 * @version v0.1
 */
class AppDistributionGroupUsersRequest {
    /**
     * Constructs a new <code>AppDistributionGroupUsersRequest</code>.
     * @alias module:model/AppDistributionGroupUsersRequest
     */
    constructor() { 
        
        AppDistributionGroupUsersRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppDistributionGroupUsersRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppDistributionGroupUsersRequest} obj Optional instance to populate.
     * @return {module:model/AppDistributionGroupUsersRequest} The populated <code>AppDistributionGroupUsersRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppDistributionGroupUsersRequest();

            if (data.hasOwnProperty('member_ids')) {
                obj['member_ids'] = ApiClient.convertToType(data['member_ids'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppDistributionGroupUsersRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppDistributionGroupUsersRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['member_ids'])) {
            throw new Error("Expected the field `member_ids` to be an array in the JSON data but got " + data['member_ids']);
        }

        return true;
    }


}



/**
 * @member {Array.<String>} member_ids
 */
AppDistributionGroupUsersRequest.prototype['member_ids'] = undefined;






export default AppDistributionGroupUsersRequest;

