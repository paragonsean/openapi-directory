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
 * The ProtocolMapperRepresentation model module.
 * @module model/ProtocolMapperRepresentation
 * @version 1
 */
class ProtocolMapperRepresentation {
    /**
     * Constructs a new <code>ProtocolMapperRepresentation</code>.
     * @alias module:model/ProtocolMapperRepresentation
     */
    constructor() { 
        
        ProtocolMapperRepresentation.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProtocolMapperRepresentation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProtocolMapperRepresentation} obj Optional instance to populate.
     * @return {module:model/ProtocolMapperRepresentation} The populated <code>ProtocolMapperRepresentation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProtocolMapperRepresentation();

            if (data.hasOwnProperty('config')) {
                obj['config'] = ApiClient.convertToType(data['config'], {'String': Object});
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('protocol')) {
                obj['protocol'] = ApiClient.convertToType(data['protocol'], 'String');
            }
            if (data.hasOwnProperty('protocolMapper')) {
                obj['protocolMapper'] = ApiClient.convertToType(data['protocolMapper'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProtocolMapperRepresentation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProtocolMapperRepresentation</code>.
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
        if (data['protocol'] && !(typeof data['protocol'] === 'string' || data['protocol'] instanceof String)) {
            throw new Error("Expected the field `protocol` to be a primitive type in the JSON string but got " + data['protocol']);
        }
        // ensure the json data is a string
        if (data['protocolMapper'] && !(typeof data['protocolMapper'] === 'string' || data['protocolMapper'] instanceof String)) {
            throw new Error("Expected the field `protocolMapper` to be a primitive type in the JSON string but got " + data['protocolMapper']);
        }

        return true;
    }


}



/**
 * @member {Object.<String, Object>} config
 */
ProtocolMapperRepresentation.prototype['config'] = undefined;

/**
 * @member {String} id
 */
ProtocolMapperRepresentation.prototype['id'] = undefined;

/**
 * @member {String} name
 */
ProtocolMapperRepresentation.prototype['name'] = undefined;

/**
 * @member {String} protocol
 */
ProtocolMapperRepresentation.prototype['protocol'] = undefined;

/**
 * @member {String} protocolMapper
 */
ProtocolMapperRepresentation.prototype['protocolMapper'] = undefined;






export default ProtocolMapperRepresentation;

