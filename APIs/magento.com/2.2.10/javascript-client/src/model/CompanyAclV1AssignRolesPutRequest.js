/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import CompanyDataRoleInterface from './CompanyDataRoleInterface';

/**
 * The CompanyAclV1AssignRolesPutRequest model module.
 * @module model/CompanyAclV1AssignRolesPutRequest
 * @version 2.2.10
 */
class CompanyAclV1AssignRolesPutRequest {
    /**
     * Constructs a new <code>CompanyAclV1AssignRolesPutRequest</code>.
     * @alias module:model/CompanyAclV1AssignRolesPutRequest
     * @param roles {Array.<module:model/CompanyDataRoleInterface>} 
     * @param userId {Number} 
     */
    constructor(roles, userId) { 
        
        CompanyAclV1AssignRolesPutRequest.initialize(this, roles, userId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, roles, userId) { 
        obj['roles'] = roles;
        obj['userId'] = userId;
    }

    /**
     * Constructs a <code>CompanyAclV1AssignRolesPutRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CompanyAclV1AssignRolesPutRequest} obj Optional instance to populate.
     * @return {module:model/CompanyAclV1AssignRolesPutRequest} The populated <code>CompanyAclV1AssignRolesPutRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CompanyAclV1AssignRolesPutRequest();

            if (data.hasOwnProperty('roles')) {
                obj['roles'] = ApiClient.convertToType(data['roles'], [CompanyDataRoleInterface]);
            }
            if (data.hasOwnProperty('userId')) {
                obj['userId'] = ApiClient.convertToType(data['userId'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CompanyAclV1AssignRolesPutRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CompanyAclV1AssignRolesPutRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CompanyAclV1AssignRolesPutRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['roles']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['roles'])) {
                throw new Error("Expected the field `roles` to be an array in the JSON data but got " + data['roles']);
            }
            // validate the optional field `roles` (array)
            for (const item of data['roles']) {
                CompanyDataRoleInterface.validateJSON(item);
            };
        }

        return true;
    }


}

CompanyAclV1AssignRolesPutRequest.RequiredProperties = ["roles", "userId"];

/**
 * @member {Array.<module:model/CompanyDataRoleInterface>} roles
 */
CompanyAclV1AssignRolesPutRequest.prototype['roles'] = undefined;

/**
 * @member {Number} userId
 */
CompanyAclV1AssignRolesPutRequest.prototype['userId'] = undefined;






export default CompanyAclV1AssignRolesPutRequest;

