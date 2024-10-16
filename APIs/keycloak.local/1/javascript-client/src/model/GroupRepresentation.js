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

/**
 * The GroupRepresentation model module.
 * @module model/GroupRepresentation
 * @version 1
 */
class GroupRepresentation {
    /**
     * Constructs a new <code>GroupRepresentation</code>.
     * @alias module:model/GroupRepresentation
     */
    constructor() { 
        
        GroupRepresentation.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GroupRepresentation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GroupRepresentation} obj Optional instance to populate.
     * @return {module:model/GroupRepresentation} The populated <code>GroupRepresentation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GroupRepresentation();

            if (data.hasOwnProperty('access')) {
                obj['access'] = ApiClient.convertToType(data['access'], {'String': Object});
            }
            if (data.hasOwnProperty('attributes')) {
                obj['attributes'] = ApiClient.convertToType(data['attributes'], {'String': Object});
            }
            if (data.hasOwnProperty('clientRoles')) {
                obj['clientRoles'] = ApiClient.convertToType(data['clientRoles'], {'String': Object});
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('path')) {
                obj['path'] = ApiClient.convertToType(data['path'], 'String');
            }
            if (data.hasOwnProperty('realmRoles')) {
                obj['realmRoles'] = ApiClient.convertToType(data['realmRoles'], ['String']);
            }
            if (data.hasOwnProperty('subGroups')) {
                obj['subGroups'] = ApiClient.convertToType(data['subGroups'], [GroupRepresentation]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GroupRepresentation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GroupRepresentation</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['path'] && !(typeof data['path'] === 'string' || data['path'] instanceof String)) {
            throw new Error("Expected the field `path` to be a primitive type in the JSON string but got " + data['path']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['realmRoles'])) {
            throw new Error("Expected the field `realmRoles` to be an array in the JSON data but got " + data['realmRoles']);
        }
        if (data['subGroups']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['subGroups'])) {
                throw new Error("Expected the field `subGroups` to be an array in the JSON data but got " + data['subGroups']);
            }
            // validate the optional field `subGroups` (array)
            for (const item of data['subGroups']) {
                GroupRepresentation.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Object.<String, Object>} access
 */
GroupRepresentation.prototype['access'] = undefined;

/**
 * @member {Object.<String, Object>} attributes
 */
GroupRepresentation.prototype['attributes'] = undefined;

/**
 * @member {Object.<String, Object>} clientRoles
 */
GroupRepresentation.prototype['clientRoles'] = undefined;

/**
 * @member {String} id
 */
GroupRepresentation.prototype['id'] = undefined;

/**
 * @member {String} name
 */
GroupRepresentation.prototype['name'] = undefined;

/**
 * @member {String} path
 */
GroupRepresentation.prototype['path'] = undefined;

/**
 * @member {Array.<String>} realmRoles
 */
GroupRepresentation.prototype['realmRoles'] = undefined;

/**
 * @member {Array.<module:model/GroupRepresentation>} subGroups
 */
GroupRepresentation.prototype['subGroups'] = undefined;






export default GroupRepresentation;

