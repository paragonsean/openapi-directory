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
 * The UserFederationMapperRepresentation model module.
 * @module model/UserFederationMapperRepresentation
 * @version 1
 */
class UserFederationMapperRepresentation {
    /**
     * Constructs a new <code>UserFederationMapperRepresentation</code>.
     * @alias module:model/UserFederationMapperRepresentation
     */
    constructor() { 
        
        UserFederationMapperRepresentation.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UserFederationMapperRepresentation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UserFederationMapperRepresentation} obj Optional instance to populate.
     * @return {module:model/UserFederationMapperRepresentation} The populated <code>UserFederationMapperRepresentation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UserFederationMapperRepresentation();

            if (data.hasOwnProperty('config')) {
                obj['config'] = ApiClient.convertToType(data['config'], {'String': Object});
            }
            if (data.hasOwnProperty('federationMapperType')) {
                obj['federationMapperType'] = ApiClient.convertToType(data['federationMapperType'], 'String');
            }
            if (data.hasOwnProperty('federationProviderDisplayName')) {
                obj['federationProviderDisplayName'] = ApiClient.convertToType(data['federationProviderDisplayName'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UserFederationMapperRepresentation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UserFederationMapperRepresentation</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['federationMapperType'] && !(typeof data['federationMapperType'] === 'string' || data['federationMapperType'] instanceof String)) {
            throw new Error("Expected the field `federationMapperType` to be a primitive type in the JSON string but got " + data['federationMapperType']);
        }
        // ensure the json data is a string
        if (data['federationProviderDisplayName'] && !(typeof data['federationProviderDisplayName'] === 'string' || data['federationProviderDisplayName'] instanceof String)) {
            throw new Error("Expected the field `federationProviderDisplayName` to be a primitive type in the JSON string but got " + data['federationProviderDisplayName']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * @member {Object.<String, Object>} config
 */
UserFederationMapperRepresentation.prototype['config'] = undefined;

/**
 * @member {String} federationMapperType
 */
UserFederationMapperRepresentation.prototype['federationMapperType'] = undefined;

/**
 * @member {String} federationProviderDisplayName
 */
UserFederationMapperRepresentation.prototype['federationProviderDisplayName'] = undefined;

/**
 * @member {String} id
 */
UserFederationMapperRepresentation.prototype['id'] = undefined;

/**
 * @member {String} name
 */
UserFederationMapperRepresentation.prototype['name'] = undefined;






export default UserFederationMapperRepresentation;

