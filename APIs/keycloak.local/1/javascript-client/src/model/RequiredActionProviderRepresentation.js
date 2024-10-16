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
 * The RequiredActionProviderRepresentation model module.
 * @module model/RequiredActionProviderRepresentation
 * @version 1
 */
class RequiredActionProviderRepresentation {
    /**
     * Constructs a new <code>RequiredActionProviderRepresentation</code>.
     * @alias module:model/RequiredActionProviderRepresentation
     */
    constructor() { 
        
        RequiredActionProviderRepresentation.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RequiredActionProviderRepresentation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RequiredActionProviderRepresentation} obj Optional instance to populate.
     * @return {module:model/RequiredActionProviderRepresentation} The populated <code>RequiredActionProviderRepresentation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RequiredActionProviderRepresentation();

            if (data.hasOwnProperty('alias')) {
                obj['alias'] = ApiClient.convertToType(data['alias'], 'String');
            }
            if (data.hasOwnProperty('config')) {
                obj['config'] = ApiClient.convertToType(data['config'], {'String': Object});
            }
            if (data.hasOwnProperty('defaultAction')) {
                obj['defaultAction'] = ApiClient.convertToType(data['defaultAction'], 'Boolean');
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('priority')) {
                obj['priority'] = ApiClient.convertToType(data['priority'], 'Number');
            }
            if (data.hasOwnProperty('providerId')) {
                obj['providerId'] = ApiClient.convertToType(data['providerId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RequiredActionProviderRepresentation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RequiredActionProviderRepresentation</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['alias'] && !(typeof data['alias'] === 'string' || data['alias'] instanceof String)) {
            throw new Error("Expected the field `alias` to be a primitive type in the JSON string but got " + data['alias']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['providerId'] && !(typeof data['providerId'] === 'string' || data['providerId'] instanceof String)) {
            throw new Error("Expected the field `providerId` to be a primitive type in the JSON string but got " + data['providerId']);
        }

        return true;
    }


}



/**
 * @member {String} alias
 */
RequiredActionProviderRepresentation.prototype['alias'] = undefined;

/**
 * @member {Object.<String, Object>} config
 */
RequiredActionProviderRepresentation.prototype['config'] = undefined;

/**
 * @member {Boolean} defaultAction
 */
RequiredActionProviderRepresentation.prototype['defaultAction'] = undefined;

/**
 * @member {Boolean} enabled
 */
RequiredActionProviderRepresentation.prototype['enabled'] = undefined;

/**
 * @member {String} name
 */
RequiredActionProviderRepresentation.prototype['name'] = undefined;

/**
 * @member {Number} priority
 */
RequiredActionProviderRepresentation.prototype['priority'] = undefined;

/**
 * @member {String} providerId
 */
RequiredActionProviderRepresentation.prototype['providerId'] = undefined;






export default RequiredActionProviderRepresentation;

