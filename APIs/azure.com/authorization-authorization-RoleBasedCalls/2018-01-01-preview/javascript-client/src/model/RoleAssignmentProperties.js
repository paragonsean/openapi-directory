/**
 * AuthorizationManagementClient
 * Role based access control provides you a way to apply granular level policy administration down to individual resources or resource groups. These operations enable you to manage role definitions and role assignments. A role definition describes the set of actions that can be performed on resources. A role assignment grants access to Azure Active Directory users.
 *
 * The version of the OpenAPI document: 2018-01-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The RoleAssignmentProperties model module.
 * @module model/RoleAssignmentProperties
 * @version 2018-01-01-preview
 */
class RoleAssignmentProperties {
    /**
     * Constructs a new <code>RoleAssignmentProperties</code>.
     * Role assignment properties.
     * @alias module:model/RoleAssignmentProperties
     */
    constructor() { 
        
        RoleAssignmentProperties.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RoleAssignmentProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RoleAssignmentProperties} obj Optional instance to populate.
     * @return {module:model/RoleAssignmentProperties} The populated <code>RoleAssignmentProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RoleAssignmentProperties();

            if (data.hasOwnProperty('canDelegate')) {
                obj['canDelegate'] = ApiClient.convertToType(data['canDelegate'], 'Boolean');
            }
            if (data.hasOwnProperty('principalId')) {
                obj['principalId'] = ApiClient.convertToType(data['principalId'], 'String');
            }
            if (data.hasOwnProperty('roleDefinitionId')) {
                obj['roleDefinitionId'] = ApiClient.convertToType(data['roleDefinitionId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RoleAssignmentProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RoleAssignmentProperties</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['principalId'] && !(typeof data['principalId'] === 'string' || data['principalId'] instanceof String)) {
            throw new Error("Expected the field `principalId` to be a primitive type in the JSON string but got " + data['principalId']);
        }
        // ensure the json data is a string
        if (data['roleDefinitionId'] && !(typeof data['roleDefinitionId'] === 'string' || data['roleDefinitionId'] instanceof String)) {
            throw new Error("Expected the field `roleDefinitionId` to be a primitive type in the JSON string but got " + data['roleDefinitionId']);
        }

        return true;
    }


}



/**
 * The delgation flag used for creating a role assignment
 * @member {Boolean} canDelegate
 */
RoleAssignmentProperties.prototype['canDelegate'] = undefined;

/**
 * The principal ID assigned to the role. This maps to the ID inside the Active Directory. It can point to a user, service principal, or security group.
 * @member {String} principalId
 */
RoleAssignmentProperties.prototype['principalId'] = undefined;

/**
 * The role definition ID used in the role assignment.
 * @member {String} roleDefinitionId
 */
RoleAssignmentProperties.prototype['roleDefinitionId'] = undefined;






export default RoleAssignmentProperties;

