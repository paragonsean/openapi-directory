/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import UpdateNetworkMerakiAuthUserRequestAuthorizationsInner from './UpdateNetworkMerakiAuthUserRequestAuthorizationsInner';

/**
 * The UpdateNetworkMerakiAuthUserRequest model module.
 * @module model/UpdateNetworkMerakiAuthUserRequest
 * @version 1.32.0
 */
class UpdateNetworkMerakiAuthUserRequest {
    /**
     * Constructs a new <code>UpdateNetworkMerakiAuthUserRequest</code>.
     * @alias module:model/UpdateNetworkMerakiAuthUserRequest
     */
    constructor() { 
        
        UpdateNetworkMerakiAuthUserRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkMerakiAuthUserRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkMerakiAuthUserRequest} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkMerakiAuthUserRequest} The populated <code>UpdateNetworkMerakiAuthUserRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkMerakiAuthUserRequest();

            if (data.hasOwnProperty('authorizations')) {
                obj['authorizations'] = ApiClient.convertToType(data['authorizations'], [UpdateNetworkMerakiAuthUserRequestAuthorizationsInner]);
            }
            if (data.hasOwnProperty('emailPasswordToUser')) {
                obj['emailPasswordToUser'] = ApiClient.convertToType(data['emailPasswordToUser'], 'Boolean');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkMerakiAuthUserRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkMerakiAuthUserRequest</code>.
     */
    static validateJSON(data) {
        if (data['authorizations']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['authorizations'])) {
                throw new Error("Expected the field `authorizations` to be an array in the JSON data but got " + data['authorizations']);
            }
            // validate the optional field `authorizations` (array)
            for (const item of data['authorizations']) {
                UpdateNetworkMerakiAuthUserRequestAuthorizationsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['password'] && !(typeof data['password'] === 'string' || data['password'] instanceof String)) {
            throw new Error("Expected the field `password` to be a primitive type in the JSON string but got " + data['password']);
        }

        return true;
    }


}



/**
 * Authorization zones and expiration dates for the user.
 * @member {Array.<module:model/UpdateNetworkMerakiAuthUserRequestAuthorizationsInner>} authorizations
 */
UpdateNetworkMerakiAuthUserRequest.prototype['authorizations'] = undefined;

/**
 * Whether or not Meraki should email the password to user. Default is false.
 * @member {Boolean} emailPasswordToUser
 */
UpdateNetworkMerakiAuthUserRequest.prototype['emailPasswordToUser'] = undefined;

/**
 * Name of the user. Only allowed If the user is not Dashboard administrator.
 * @member {String} name
 */
UpdateNetworkMerakiAuthUserRequest.prototype['name'] = undefined;

/**
 * The password for this user account. Only allowed If the user is not Dashboard administrator.
 * @member {String} password
 */
UpdateNetworkMerakiAuthUserRequest.prototype['password'] = undefined;






export default UpdateNetworkMerakiAuthUserRequest;

