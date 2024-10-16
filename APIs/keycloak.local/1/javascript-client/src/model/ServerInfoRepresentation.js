/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import MemoryInfoRepresentation from './MemoryInfoRepresentation';
import PasswordPolicyTypeRepresentation from './PasswordPolicyTypeRepresentation';
import ProfileInfoRepresentation from './ProfileInfoRepresentation';
import SystemInfoRepresentation from './SystemInfoRepresentation';

/**
 * The ServerInfoRepresentation model module.
 * @module model/ServerInfoRepresentation
 * @version 1
 */
class ServerInfoRepresentation {
    /**
     * Constructs a new <code>ServerInfoRepresentation</code>.
     * @alias module:model/ServerInfoRepresentation
     */
    constructor() { 
        
        ServerInfoRepresentation.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ServerInfoRepresentation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ServerInfoRepresentation} obj Optional instance to populate.
     * @return {module:model/ServerInfoRepresentation} The populated <code>ServerInfoRepresentation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ServerInfoRepresentation();

            if (data.hasOwnProperty('builtinProtocolMappers')) {
                obj['builtinProtocolMappers'] = ApiClient.convertToType(data['builtinProtocolMappers'], {'String': Object});
            }
            if (data.hasOwnProperty('clientImporters')) {
                obj['clientImporters'] = ApiClient.convertToType(data['clientImporters'], [{'String': Object}]);
            }
            if (data.hasOwnProperty('clientInstallations')) {
                obj['clientInstallations'] = ApiClient.convertToType(data['clientInstallations'], {'String': Object});
            }
            if (data.hasOwnProperty('componentTypes')) {
                obj['componentTypes'] = ApiClient.convertToType(data['componentTypes'], {'String': Object});
            }
            if (data.hasOwnProperty('enums')) {
                obj['enums'] = ApiClient.convertToType(data['enums'], {'String': Object});
            }
            if (data.hasOwnProperty('identityProviders')) {
                obj['identityProviders'] = ApiClient.convertToType(data['identityProviders'], [{'String': Object}]);
            }
            if (data.hasOwnProperty('memoryInfo')) {
                obj['memoryInfo'] = MemoryInfoRepresentation.constructFromObject(data['memoryInfo']);
            }
            if (data.hasOwnProperty('passwordPolicies')) {
                obj['passwordPolicies'] = ApiClient.convertToType(data['passwordPolicies'], [PasswordPolicyTypeRepresentation]);
            }
            if (data.hasOwnProperty('profileInfo')) {
                obj['profileInfo'] = ProfileInfoRepresentation.constructFromObject(data['profileInfo']);
            }
            if (data.hasOwnProperty('protocolMapperTypes')) {
                obj['protocolMapperTypes'] = ApiClient.convertToType(data['protocolMapperTypes'], {'String': Object});
            }
            if (data.hasOwnProperty('providers')) {
                obj['providers'] = ApiClient.convertToType(data['providers'], {'String': Object});
            }
            if (data.hasOwnProperty('socialProviders')) {
                obj['socialProviders'] = ApiClient.convertToType(data['socialProviders'], [{'String': Object}]);
            }
            if (data.hasOwnProperty('systemInfo')) {
                obj['systemInfo'] = SystemInfoRepresentation.constructFromObject(data['systemInfo']);
            }
            if (data.hasOwnProperty('themes')) {
                obj['themes'] = ApiClient.convertToType(data['themes'], {'String': Object});
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ServerInfoRepresentation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ServerInfoRepresentation</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['clientImporters'])) {
            throw new Error("Expected the field `clientImporters` to be an array in the JSON data but got " + data['clientImporters']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['identityProviders'])) {
            throw new Error("Expected the field `identityProviders` to be an array in the JSON data but got " + data['identityProviders']);
        }
        // validate the optional field `memoryInfo`
        if (data['memoryInfo']) { // data not null
          MemoryInfoRepresentation.validateJSON(data['memoryInfo']);
        }
        if (data['passwordPolicies']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['passwordPolicies'])) {
                throw new Error("Expected the field `passwordPolicies` to be an array in the JSON data but got " + data['passwordPolicies']);
            }
            // validate the optional field `passwordPolicies` (array)
            for (const item of data['passwordPolicies']) {
                PasswordPolicyTypeRepresentation.validateJSON(item);
            };
        }
        // validate the optional field `profileInfo`
        if (data['profileInfo']) { // data not null
          ProfileInfoRepresentation.validateJSON(data['profileInfo']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['socialProviders'])) {
            throw new Error("Expected the field `socialProviders` to be an array in the JSON data but got " + data['socialProviders']);
        }
        // validate the optional field `systemInfo`
        if (data['systemInfo']) { // data not null
          SystemInfoRepresentation.validateJSON(data['systemInfo']);
        }

        return true;
    }


}



/**
 * @member {Object.<String, Object>} builtinProtocolMappers
 */
ServerInfoRepresentation.prototype['builtinProtocolMappers'] = undefined;

/**
 * @member {Array.<Object.<String, Object>>} clientImporters
 */
ServerInfoRepresentation.prototype['clientImporters'] = undefined;

/**
 * @member {Object.<String, Object>} clientInstallations
 */
ServerInfoRepresentation.prototype['clientInstallations'] = undefined;

/**
 * @member {Object.<String, Object>} componentTypes
 */
ServerInfoRepresentation.prototype['componentTypes'] = undefined;

/**
 * @member {Object.<String, Object>} enums
 */
ServerInfoRepresentation.prototype['enums'] = undefined;

/**
 * @member {Array.<Object.<String, Object>>} identityProviders
 */
ServerInfoRepresentation.prototype['identityProviders'] = undefined;

/**
 * @member {module:model/MemoryInfoRepresentation} memoryInfo
 */
ServerInfoRepresentation.prototype['memoryInfo'] = undefined;

/**
 * @member {Array.<module:model/PasswordPolicyTypeRepresentation>} passwordPolicies
 */
ServerInfoRepresentation.prototype['passwordPolicies'] = undefined;

/**
 * @member {module:model/ProfileInfoRepresentation} profileInfo
 */
ServerInfoRepresentation.prototype['profileInfo'] = undefined;

/**
 * @member {Object.<String, Object>} protocolMapperTypes
 */
ServerInfoRepresentation.prototype['protocolMapperTypes'] = undefined;

/**
 * @member {Object.<String, Object>} providers
 */
ServerInfoRepresentation.prototype['providers'] = undefined;

/**
 * @member {Array.<Object.<String, Object>>} socialProviders
 */
ServerInfoRepresentation.prototype['socialProviders'] = undefined;

/**
 * @member {module:model/SystemInfoRepresentation} systemInfo
 */
ServerInfoRepresentation.prototype['systemInfo'] = undefined;

/**
 * @member {Object.<String, Object>} themes
 */
ServerInfoRepresentation.prototype['themes'] = undefined;






export default ServerInfoRepresentation;

