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
 * The OrgInvitationsListPending200ResponseInner model module.
 * @module model/OrgInvitationsListPending200ResponseInner
 * @version v0.1
 */
class OrgInvitationsListPending200ResponseInner {
    /**
     * Constructs a new <code>OrgInvitationsListPending200ResponseInner</code>.
     * @alias module:model/OrgInvitationsListPending200ResponseInner
     * @param email {String} The email address of the invited user
     * @param id {String} The unique ID (UUID) of the invitation
     * @param role {String} The role assigned to the invited user
     */
    constructor(email, id, role) { 
        
        OrgInvitationsListPending200ResponseInner.initialize(this, email, id, role);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, email, id, role) { 
        obj['email'] = email;
        obj['id'] = id;
        obj['role'] = role;
    }

    /**
     * Constructs a <code>OrgInvitationsListPending200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrgInvitationsListPending200ResponseInner} obj Optional instance to populate.
     * @return {module:model/OrgInvitationsListPending200ResponseInner} The populated <code>OrgInvitationsListPending200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrgInvitationsListPending200ResponseInner();

            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('role')) {
                obj['role'] = ApiClient.convertToType(data['role'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrgInvitationsListPending200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrgInvitationsListPending200ResponseInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OrgInvitationsListPending200ResponseInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['role'] && !(typeof data['role'] === 'string' || data['role'] instanceof String)) {
            throw new Error("Expected the field `role` to be a primitive type in the JSON string but got " + data['role']);
        }

        return true;
    }


}

OrgInvitationsListPending200ResponseInner.RequiredProperties = ["email", "id", "role"];

/**
 * The email address of the invited user
 * @member {String} email
 */
OrgInvitationsListPending200ResponseInner.prototype['email'] = undefined;

/**
 * The unique ID (UUID) of the invitation
 * @member {String} id
 */
OrgInvitationsListPending200ResponseInner.prototype['id'] = undefined;

/**
 * The role assigned to the invited user
 * @member {String} role
 */
OrgInvitationsListPending200ResponseInner.prototype['role'] = undefined;






export default OrgInvitationsListPending200ResponseInner;

