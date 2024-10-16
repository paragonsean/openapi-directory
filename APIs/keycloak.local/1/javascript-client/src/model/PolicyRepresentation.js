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
import ResourceRepresentation from './ResourceRepresentation';
import ScopeRepresentation from './ScopeRepresentation';

/**
 * The PolicyRepresentation model module.
 * @module model/PolicyRepresentation
 * @version 1
 */
class PolicyRepresentation {
    /**
     * Constructs a new <code>PolicyRepresentation</code>.
     * @alias module:model/PolicyRepresentation
     */
    constructor() { 
        
        PolicyRepresentation.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PolicyRepresentation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PolicyRepresentation} obj Optional instance to populate.
     * @return {module:model/PolicyRepresentation} The populated <code>PolicyRepresentation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PolicyRepresentation();

            if (data.hasOwnProperty('config')) {
                obj['config'] = ApiClient.convertToType(data['config'], {'String': Object});
            }
            if (data.hasOwnProperty('decisionStrategy')) {
                obj['decisionStrategy'] = ApiClient.convertToType(data['decisionStrategy'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('logic')) {
                obj['logic'] = ApiClient.convertToType(data['logic'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('owner')) {
                obj['owner'] = ApiClient.convertToType(data['owner'], 'String');
            }
            if (data.hasOwnProperty('policies')) {
                obj['policies'] = ApiClient.convertToType(data['policies'], ['String']);
            }
            if (data.hasOwnProperty('resources')) {
                obj['resources'] = ApiClient.convertToType(data['resources'], ['String']);
            }
            if (data.hasOwnProperty('resourcesData')) {
                obj['resourcesData'] = ApiClient.convertToType(data['resourcesData'], [ResourceRepresentation]);
            }
            if (data.hasOwnProperty('scopes')) {
                obj['scopes'] = ApiClient.convertToType(data['scopes'], ['String']);
            }
            if (data.hasOwnProperty('scopesData')) {
                obj['scopesData'] = ApiClient.convertToType(data['scopesData'], [ScopeRepresentation]);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PolicyRepresentation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PolicyRepresentation</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['decisionStrategy'] && !(typeof data['decisionStrategy'] === 'string' || data['decisionStrategy'] instanceof String)) {
            throw new Error("Expected the field `decisionStrategy` to be a primitive type in the JSON string but got " + data['decisionStrategy']);
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
        if (data['logic'] && !(typeof data['logic'] === 'string' || data['logic'] instanceof String)) {
            throw new Error("Expected the field `logic` to be a primitive type in the JSON string but got " + data['logic']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['owner'] && !(typeof data['owner'] === 'string' || data['owner'] instanceof String)) {
            throw new Error("Expected the field `owner` to be a primitive type in the JSON string but got " + data['owner']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['policies'])) {
            throw new Error("Expected the field `policies` to be an array in the JSON data but got " + data['policies']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['resources'])) {
            throw new Error("Expected the field `resources` to be an array in the JSON data but got " + data['resources']);
        }
        if (data['resourcesData']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['resourcesData'])) {
                throw new Error("Expected the field `resourcesData` to be an array in the JSON data but got " + data['resourcesData']);
            }
            // validate the optional field `resourcesData` (array)
            for (const item of data['resourcesData']) {
                ResourceRepresentation.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['scopes'])) {
            throw new Error("Expected the field `scopes` to be an array in the JSON data but got " + data['scopes']);
        }
        if (data['scopesData']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['scopesData'])) {
                throw new Error("Expected the field `scopesData` to be an array in the JSON data but got " + data['scopesData']);
            }
            // validate the optional field `scopesData` (array)
            for (const item of data['scopesData']) {
                ScopeRepresentation.validateJSON(item);
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
 * @member {Object.<String, Object>} config
 */
PolicyRepresentation.prototype['config'] = undefined;

/**
 * @member {module:model/PolicyRepresentation.DecisionStrategyEnum} decisionStrategy
 */
PolicyRepresentation.prototype['decisionStrategy'] = undefined;

/**
 * @member {String} description
 */
PolicyRepresentation.prototype['description'] = undefined;

/**
 * @member {String} id
 */
PolicyRepresentation.prototype['id'] = undefined;

/**
 * @member {module:model/PolicyRepresentation.LogicEnum} logic
 */
PolicyRepresentation.prototype['logic'] = undefined;

/**
 * @member {String} name
 */
PolicyRepresentation.prototype['name'] = undefined;

/**
 * @member {String} owner
 */
PolicyRepresentation.prototype['owner'] = undefined;

/**
 * @member {Array.<String>} policies
 */
PolicyRepresentation.prototype['policies'] = undefined;

/**
 * @member {Array.<String>} resources
 */
PolicyRepresentation.prototype['resources'] = undefined;

/**
 * @member {Array.<module:model/ResourceRepresentation>} resourcesData
 */
PolicyRepresentation.prototype['resourcesData'] = undefined;

/**
 * @member {Array.<String>} scopes
 */
PolicyRepresentation.prototype['scopes'] = undefined;

/**
 * @member {Array.<module:model/ScopeRepresentation>} scopesData
 */
PolicyRepresentation.prototype['scopesData'] = undefined;

/**
 * @member {String} type
 */
PolicyRepresentation.prototype['type'] = undefined;





/**
 * Allowed values for the <code>decisionStrategy</code> property.
 * @enum {String}
 * @readonly
 */
PolicyRepresentation['DecisionStrategyEnum'] = {

    /**
     * value: "AFFIRMATIVE"
     * @const
     */
    "AFFIRMATIVE": "AFFIRMATIVE",

    /**
     * value: "UNANIMOUS"
     * @const
     */
    "UNANIMOUS": "UNANIMOUS",

    /**
     * value: "CONSENSUS"
     * @const
     */
    "CONSENSUS": "CONSENSUS"
};


/**
 * Allowed values for the <code>logic</code> property.
 * @enum {String}
 * @readonly
 */
PolicyRepresentation['LogicEnum'] = {

    /**
     * value: "POSITIVE"
     * @const
     */
    "POSITIVE": "POSITIVE",

    /**
     * value: "NEGATIVE"
     * @const
     */
    "NEGATIVE": "NEGATIVE"
};



export default PolicyRepresentation;

