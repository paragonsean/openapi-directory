/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GuestUsersPoliciesConfig model module.
 * @module model/GuestUsersPoliciesConfig
 * @version 4.42.3
 */
class GuestUsersPoliciesConfig {
    /**
     * Constructs a new <code>GuestUsersPoliciesConfig</code>.
     * Set of guest user policies
     * @alias module:model/GuestUsersPoliciesConfig
     * @param isInviteUsersEnabled {Boolean} Determines whether the invite of users to rooms is enabled.
     */
    constructor(isInviteUsersEnabled) { 
        
        GuestUsersPoliciesConfig.initialize(this, isInviteUsersEnabled);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, isInviteUsersEnabled) { 
        obj['isInviteUsersEnabled'] = isInviteUsersEnabled;
    }

    /**
     * Constructs a <code>GuestUsersPoliciesConfig</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GuestUsersPoliciesConfig} obj Optional instance to populate.
     * @return {module:model/GuestUsersPoliciesConfig} The populated <code>GuestUsersPoliciesConfig</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GuestUsersPoliciesConfig();

            if (data.hasOwnProperty('isInviteUsersEnabled')) {
                obj['isInviteUsersEnabled'] = ApiClient.convertToType(data['isInviteUsersEnabled'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GuestUsersPoliciesConfig</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GuestUsersPoliciesConfig</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GuestUsersPoliciesConfig.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

GuestUsersPoliciesConfig.RequiredProperties = ["isInviteUsersEnabled"];

/**
 * Determines whether the invite of users to rooms is enabled.
 * @member {Boolean} isInviteUsersEnabled
 */
GuestUsersPoliciesConfig.prototype['isInviteUsersEnabled'] = undefined;






export default GuestUsersPoliciesConfig;

