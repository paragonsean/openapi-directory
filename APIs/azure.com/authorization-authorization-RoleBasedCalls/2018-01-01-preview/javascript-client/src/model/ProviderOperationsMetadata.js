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
import ProviderOperation from './ProviderOperation';
import ResourceType from './ResourceType';

/**
 * The ProviderOperationsMetadata model module.
 * @module model/ProviderOperationsMetadata
 * @version 2018-01-01-preview
 */
class ProviderOperationsMetadata {
    /**
     * Constructs a new <code>ProviderOperationsMetadata</code>.
     * Provider Operations metadata
     * @alias module:model/ProviderOperationsMetadata
     */
    constructor() { 
        
        ProviderOperationsMetadata.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProviderOperationsMetadata</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProviderOperationsMetadata} obj Optional instance to populate.
     * @return {module:model/ProviderOperationsMetadata} The populated <code>ProviderOperationsMetadata</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProviderOperationsMetadata();

            if (data.hasOwnProperty('displayName')) {
                obj['displayName'] = ApiClient.convertToType(data['displayName'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('operations')) {
                obj['operations'] = ApiClient.convertToType(data['operations'], [ProviderOperation]);
            }
            if (data.hasOwnProperty('resourceTypes')) {
                obj['resourceTypes'] = ApiClient.convertToType(data['resourceTypes'], [ResourceType]);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProviderOperationsMetadata</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProviderOperationsMetadata</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['displayName'] && !(typeof data['displayName'] === 'string' || data['displayName'] instanceof String)) {
            throw new Error("Expected the field `displayName` to be a primitive type in the JSON string but got " + data['displayName']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        if (data['operations']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['operations'])) {
                throw new Error("Expected the field `operations` to be an array in the JSON data but got " + data['operations']);
            }
            // validate the optional field `operations` (array)
            for (const item of data['operations']) {
                ProviderOperation.validateJSON(item);
            };
        }
        if (data['resourceTypes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['resourceTypes'])) {
                throw new Error("Expected the field `resourceTypes` to be an array in the JSON data but got " + data['resourceTypes']);
            }
            // validate the optional field `resourceTypes` (array)
            for (const item of data['resourceTypes']) {
                ResourceType.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * The provider display name.
 * @member {String} displayName
 */
ProviderOperationsMetadata.prototype['displayName'] = undefined;

/**
 * The provider id.
 * @member {String} id
 */
ProviderOperationsMetadata.prototype['id'] = undefined;

/**
 * The provider name.
 * @member {String} name
 */
ProviderOperationsMetadata.prototype['name'] = undefined;

/**
 * The provider operations.
 * @member {Array.<module:model/ProviderOperation>} operations
 */
ProviderOperationsMetadata.prototype['operations'] = undefined;

/**
 * The provider resource types
 * @member {Array.<module:model/ResourceType>} resourceTypes
 */
ProviderOperationsMetadata.prototype['resourceTypes'] = undefined;

/**
 * The provider type.
 * @member {String} type
 */
ProviderOperationsMetadata.prototype['type'] = undefined;






export default ProviderOperationsMetadata;

