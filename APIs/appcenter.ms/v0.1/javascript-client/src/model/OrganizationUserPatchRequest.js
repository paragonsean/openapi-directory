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
 * The OrganizationUserPatchRequest model module.
 * @module model/OrganizationUserPatchRequest
 * @version v0.1
 */
class OrganizationUserPatchRequest {
    /**
     * Constructs a new <code>OrganizationUserPatchRequest</code>.
     * @alias module:model/OrganizationUserPatchRequest
     */
    constructor() { 
        
        OrganizationUserPatchRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OrganizationUserPatchRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrganizationUserPatchRequest} obj Optional instance to populate.
     * @return {module:model/OrganizationUserPatchRequest} The populated <code>OrganizationUserPatchRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrganizationUserPatchRequest();

            if (data.hasOwnProperty('role')) {
                obj['role'] = ApiClient.convertToType(data['role'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrganizationUserPatchRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrganizationUserPatchRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['role'] && !(typeof data['role'] === 'string' || data['role'] instanceof String)) {
            throw new Error("Expected the field `role` to be a primitive type in the JSON string but got " + data['role']);
        }

        return true;
    }


}



/**
 * The user's role in the organizatiion
 * @member {module:model/OrganizationUserPatchRequest.RoleEnum} role
 */
OrganizationUserPatchRequest.prototype['role'] = undefined;





/**
 * Allowed values for the <code>role</code> property.
 * @enum {String}
 * @readonly
 */
OrganizationUserPatchRequest['RoleEnum'] = {

    /**
     * value: "admin"
     * @const
     */
    "admin": "admin",

    /**
     * value: "collaborator"
     * @const
     */
    "collaborator": "collaborator",

    /**
     * value: "member"
     * @const
     */
    "member": "member"
};



export default OrganizationUserPatchRequest;

