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
 * The ProvisioningProfile model module.
 * @module model/ProvisioningProfile
 * @version v0.1
 */
class ProvisioningProfile {
    /**
     * Constructs a new <code>ProvisioningProfile</code>.
     * An object containing information about an iOS provisioning profile.
     * @alias module:model/ProvisioningProfile
     * @param applicationIdentifier {String} The application identifier.
     * @param expiredAt {String} The profile's expiration date in RFC 3339 format, i.e. 2017-07-21T17:32:28Z
     * @param name {String} The name of the provisioning profile.
     * @param profileType {module:model/ProvisioningProfile.ProfileTypeEnum} 
     * @param teamIdentifier {String} The team identifier.
     */
    constructor(applicationIdentifier, expiredAt, name, profileType, teamIdentifier) { 
        
        ProvisioningProfile.initialize(this, applicationIdentifier, expiredAt, name, profileType, teamIdentifier);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, applicationIdentifier, expiredAt, name, profileType, teamIdentifier) { 
        obj['application_identifier'] = applicationIdentifier;
        obj['expired_at'] = expiredAt;
        obj['name'] = name;
        obj['profile_type'] = profileType;
        obj['team_identifier'] = teamIdentifier;
    }

    /**
     * Constructs a <code>ProvisioningProfile</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProvisioningProfile} obj Optional instance to populate.
     * @return {module:model/ProvisioningProfile} The populated <code>ProvisioningProfile</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProvisioningProfile();

            if (data.hasOwnProperty('application_identifier')) {
                obj['application_identifier'] = ApiClient.convertToType(data['application_identifier'], 'String');
            }
            if (data.hasOwnProperty('expired_at')) {
                obj['expired_at'] = ApiClient.convertToType(data['expired_at'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('profile_type')) {
                obj['profile_type'] = ApiClient.convertToType(data['profile_type'], 'String');
            }
            if (data.hasOwnProperty('team_identifier')) {
                obj['team_identifier'] = ApiClient.convertToType(data['team_identifier'], 'String');
            }
            if (data.hasOwnProperty('udids')) {
                obj['udids'] = ApiClient.convertToType(data['udids'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProvisioningProfile</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProvisioningProfile</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ProvisioningProfile.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['application_identifier'] && !(typeof data['application_identifier'] === 'string' || data['application_identifier'] instanceof String)) {
            throw new Error("Expected the field `application_identifier` to be a primitive type in the JSON string but got " + data['application_identifier']);
        }
        // ensure the json data is a string
        if (data['expired_at'] && !(typeof data['expired_at'] === 'string' || data['expired_at'] instanceof String)) {
            throw new Error("Expected the field `expired_at` to be a primitive type in the JSON string but got " + data['expired_at']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['profile_type'] && !(typeof data['profile_type'] === 'string' || data['profile_type'] instanceof String)) {
            throw new Error("Expected the field `profile_type` to be a primitive type in the JSON string but got " + data['profile_type']);
        }
        // ensure the json data is a string
        if (data['team_identifier'] && !(typeof data['team_identifier'] === 'string' || data['team_identifier'] instanceof String)) {
            throw new Error("Expected the field `team_identifier` to be a primitive type in the JSON string but got " + data['team_identifier']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['udids'])) {
            throw new Error("Expected the field `udids` to be an array in the JSON data but got " + data['udids']);
        }

        return true;
    }


}

ProvisioningProfile.RequiredProperties = ["application_identifier", "expired_at", "name", "profile_type", "team_identifier"];

/**
 * The application identifier.
 * @member {String} application_identifier
 */
ProvisioningProfile.prototype['application_identifier'] = undefined;

/**
 * The profile's expiration date in RFC 3339 format, i.e. 2017-07-21T17:32:28Z
 * @member {String} expired_at
 */
ProvisioningProfile.prototype['expired_at'] = undefined;

/**
 * The name of the provisioning profile.
 * @member {String} name
 */
ProvisioningProfile.prototype['name'] = undefined;

/**
 * @member {module:model/ProvisioningProfile.ProfileTypeEnum} profile_type
 */
ProvisioningProfile.prototype['profile_type'] = undefined;

/**
 * The team identifier.
 * @member {String} team_identifier
 */
ProvisioningProfile.prototype['team_identifier'] = undefined;

/**
 * @member {Array.<String>} udids
 */
ProvisioningProfile.prototype['udids'] = undefined;





/**
 * Allowed values for the <code>profile_type</code> property.
 * @enum {String}
 * @readonly
 */
ProvisioningProfile['ProfileTypeEnum'] = {

    /**
     * value: "adhoc"
     * @const
     */
    "adhoc": "adhoc",

    /**
     * value: "enterprise"
     * @const
     */
    "enterprise": "enterprise",

    /**
     * value: "other"
     * @const
     */
    "other": "other"
};



export default ProvisioningProfile;

