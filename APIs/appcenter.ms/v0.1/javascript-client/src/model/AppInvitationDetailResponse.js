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
import AppInvitationsList200ResponseDistributionGroup from './AppInvitationsList200ResponseDistributionGroup';
import AppInvitationsList200ResponseInvitedBy from './AppInvitationsList200ResponseInvitedBy';
import AppsList200ResponseInner from './AppsList200ResponseInner';

/**
 * The AppInvitationDetailResponse model module.
 * @module model/AppInvitationDetailResponse
 * @version v0.1
 */
class AppInvitationDetailResponse {
    /**
     * Constructs a new <code>AppInvitationDetailResponse</code>.
     * @alias module:model/AppInvitationDetailResponse
     * @param app {module:model/AppsList200ResponseInner} 
     * @param email {String} The email address of the invited user
     * @param id {String} The unique ID (UUID) of the invitation
     * @param inviteType {module:model/AppInvitationDetailResponse.InviteTypeEnum} The invitation type
     * @param invitedBy {module:model/AppInvitationsList200ResponseInvitedBy} 
     * @param isExistingUser {Boolean} Indicates whether the invited user already exists
     */
    constructor(app, email, id, inviteType, invitedBy, isExistingUser) { 
        
        AppInvitationDetailResponse.initialize(this, app, email, id, inviteType, invitedBy, isExistingUser);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, app, email, id, inviteType, invitedBy, isExistingUser) { 
        obj['app'] = app;
        obj['email'] = email;
        obj['id'] = id;
        obj['invite_type'] = inviteType;
        obj['invited_by'] = invitedBy;
        obj['is_existing_user'] = isExistingUser;
    }

    /**
     * Constructs a <code>AppInvitationDetailResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppInvitationDetailResponse} obj Optional instance to populate.
     * @return {module:model/AppInvitationDetailResponse} The populated <code>AppInvitationDetailResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppInvitationDetailResponse();

            if (data.hasOwnProperty('app')) {
                obj['app'] = AppsList200ResponseInner.constructFromObject(data['app']);
            }
            if (data.hasOwnProperty('app_count')) {
                obj['app_count'] = ApiClient.convertToType(data['app_count'], 'Number');
            }
            if (data.hasOwnProperty('distribution_group')) {
                obj['distribution_group'] = AppInvitationsList200ResponseDistributionGroup.constructFromObject(data['distribution_group']);
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('invite_type')) {
                obj['invite_type'] = ApiClient.convertToType(data['invite_type'], 'String');
            }
            if (data.hasOwnProperty('invited_by')) {
                obj['invited_by'] = AppInvitationsList200ResponseInvitedBy.constructFromObject(data['invited_by']);
            }
            if (data.hasOwnProperty('is_existing_user')) {
                obj['is_existing_user'] = ApiClient.convertToType(data['is_existing_user'], 'Boolean');
            }
            if (data.hasOwnProperty('permissions')) {
                obj['permissions'] = ApiClient.convertToType(data['permissions'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppInvitationDetailResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppInvitationDetailResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AppInvitationDetailResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `app`
        if (data['app']) { // data not null
          AppsList200ResponseInner.validateJSON(data['app']);
        }
        // validate the optional field `distribution_group`
        if (data['distribution_group']) { // data not null
          AppInvitationsList200ResponseDistributionGroup.validateJSON(data['distribution_group']);
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
        if (data['invite_type'] && !(typeof data['invite_type'] === 'string' || data['invite_type'] instanceof String)) {
            throw new Error("Expected the field `invite_type` to be a primitive type in the JSON string but got " + data['invite_type']);
        }
        // validate the optional field `invited_by`
        if (data['invited_by']) { // data not null
          AppInvitationsList200ResponseInvitedBy.validateJSON(data['invited_by']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['permissions'])) {
            throw new Error("Expected the field `permissions` to be an array in the JSON data but got " + data['permissions']);
        }

        return true;
    }


}

AppInvitationDetailResponse.RequiredProperties = ["app", "email", "id", "invite_type", "invited_by", "is_existing_user"];

/**
 * @member {module:model/AppsList200ResponseInner} app
 */
AppInvitationDetailResponse.prototype['app'] = undefined;

/**
 * The number of apps in the group
 * @member {Number} app_count
 */
AppInvitationDetailResponse.prototype['app_count'] = undefined;

/**
 * @member {module:model/AppInvitationsList200ResponseDistributionGroup} distribution_group
 */
AppInvitationDetailResponse.prototype['distribution_group'] = undefined;

/**
 * The email address of the invited user
 * @member {String} email
 */
AppInvitationDetailResponse.prototype['email'] = undefined;

/**
 * The unique ID (UUID) of the invitation
 * @member {String} id
 */
AppInvitationDetailResponse.prototype['id'] = undefined;

/**
 * The invitation type
 * @member {module:model/AppInvitationDetailResponse.InviteTypeEnum} invite_type
 */
AppInvitationDetailResponse.prototype['invite_type'] = undefined;

/**
 * @member {module:model/AppInvitationsList200ResponseInvitedBy} invited_by
 */
AppInvitationDetailResponse.prototype['invited_by'] = undefined;

/**
 * Indicates whether the invited user already exists
 * @member {Boolean} is_existing_user
 */
AppInvitationDetailResponse.prototype['is_existing_user'] = undefined;

/**
 * The permissions the user has for the app
 * @member {Array.<module:model/AppInvitationDetailResponse.PermissionsEnum>} permissions
 */
AppInvitationDetailResponse.prototype['permissions'] = undefined;





/**
 * Allowed values for the <code>invite_type</code> property.
 * @enum {String}
 * @readonly
 */
AppInvitationDetailResponse['InviteTypeEnum'] = {

    /**
     * value: "developer"
     * @const
     */
    "developer": "developer",

    /**
     * value: "tester"
     * @const
     */
    "tester": "tester"
};


/**
 * Allowed values for the <code>permissions</code> property.
 * @enum {String}
 * @readonly
 */
AppInvitationDetailResponse['PermissionsEnum'] = {

    /**
     * value: "manager"
     * @const
     */
    "manager": "manager",

    /**
     * value: "developer"
     * @const
     */
    "developer": "developer",

    /**
     * value: "viewer"
     * @const
     */
    "viewer": "viewer",

    /**
     * value: "tester"
     * @const
     */
    "tester": "tester"
};



export default AppInvitationDetailResponse;

