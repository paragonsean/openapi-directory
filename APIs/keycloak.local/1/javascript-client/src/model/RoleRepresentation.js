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
import RoleRepresentationComposites from './RoleRepresentationComposites';

/**
 * The RoleRepresentation model module.
 * @module model/RoleRepresentation
 * @version 1
 */
class RoleRepresentation {
    /**
     * Constructs a new <code>RoleRepresentation</code>.
     * @alias module:model/RoleRepresentation
     */
    constructor() { 
        
        RoleRepresentation.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RoleRepresentation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RoleRepresentation} obj Optional instance to populate.
     * @return {module:model/RoleRepresentation} The populated <code>RoleRepresentation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RoleRepresentation();

            if (data.hasOwnProperty('attributes')) {
                obj['attributes'] = ApiClient.convertToType(data['attributes'], {'String': Object});
            }
            if (data.hasOwnProperty('clientRole')) {
                obj['clientRole'] = ApiClient.convertToType(data['clientRole'], 'Boolean');
            }
            if (data.hasOwnProperty('composite')) {
                obj['composite'] = ApiClient.convertToType(data['composite'], 'Boolean');
            }
            if (data.hasOwnProperty('composites')) {
                obj['composites'] = RoleRepresentationComposites.constructFromObject(data['composites']);
            }
            if (data.hasOwnProperty('containerId')) {
                obj['containerId'] = ApiClient.convertToType(data['containerId'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
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
     * Validates the JSON data with respect to <code>RoleRepresentation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RoleRepresentation</code>.
     */
    static validateJSON(data) {
        // validate the optional field `composites`
        if (data['composites']) { // data not null
          RoleRepresentationComposites.validateJSON(data['composites']);
        }
        // ensure the json data is a string
        if (data['containerId'] && !(typeof data['containerId'] === 'string' || data['containerId'] instanceof String)) {
            throw new Error("Expected the field `containerId` to be a primitive type in the JSON string but got " + data['containerId']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
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
 * @member {Object.<String, Object>} attributes
 */
RoleRepresentation.prototype['attributes'] = undefined;

/**
 * @member {Boolean} clientRole
 */
RoleRepresentation.prototype['clientRole'] = undefined;

/**
 * @member {Boolean} composite
 */
RoleRepresentation.prototype['composite'] = undefined;

/**
 * @member {module:model/RoleRepresentationComposites} composites
 */
RoleRepresentation.prototype['composites'] = undefined;

/**
 * @member {String} containerId
 */
RoleRepresentation.prototype['containerId'] = undefined;

/**
 * @member {String} description
 */
RoleRepresentation.prototype['description'] = undefined;

/**
 * @member {String} id
 */
RoleRepresentation.prototype['id'] = undefined;

/**
 * @member {String} name
 */
RoleRepresentation.prototype['name'] = undefined;






export default RoleRepresentation;

