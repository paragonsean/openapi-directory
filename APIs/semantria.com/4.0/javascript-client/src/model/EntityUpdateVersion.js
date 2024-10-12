/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The EntityUpdateVersion model module.
 * @module model/EntityUpdateVersion
 * @version 4.0
 */
class EntityUpdateVersion {
    /**
     * Constructs a new <code>EntityUpdateVersion</code>.
     * @alias module:model/EntityUpdateVersion
     * @param id {String} Unique user entity identifier
     * @param label {String} Descriptive label for the entity, e.g. Wikipedia URL
     * @param name {String} Entity name
     * @param normalized {String} Normalized form of the entity. Will replace entity name in the output
     * @param type {String} Type of the entity (Company, Person, any custom type)
     */
    constructor(id, label, name, normalized, type) { 
        
        EntityUpdateVersion.initialize(this, id, label, name, normalized, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id, label, name, normalized, type) { 
        obj['id'] = id;
        obj['label'] = label;
        obj['name'] = name;
        obj['normalized'] = normalized;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>EntityUpdateVersion</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EntityUpdateVersion} obj Optional instance to populate.
     * @return {module:model/EntityUpdateVersion} The populated <code>EntityUpdateVersion</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EntityUpdateVersion();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('label')) {
                obj['label'] = ApiClient.convertToType(data['label'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('normalized')) {
                obj['normalized'] = ApiClient.convertToType(data['normalized'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EntityUpdateVersion</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EntityUpdateVersion</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EntityUpdateVersion.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['label'] && !(typeof data['label'] === 'string' || data['label'] instanceof String)) {
            throw new Error("Expected the field `label` to be a primitive type in the JSON string but got " + data['label']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['normalized'] && !(typeof data['normalized'] === 'string' || data['normalized'] instanceof String)) {
            throw new Error("Expected the field `normalized` to be a primitive type in the JSON string but got " + data['normalized']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

EntityUpdateVersion.RequiredProperties = ["id", "label", "name", "normalized", "type"];

/**
 * Unique user entity identifier
 * @member {String} id
 */
EntityUpdateVersion.prototype['id'] = undefined;

/**
 * Descriptive label for the entity, e.g. Wikipedia URL
 * @member {String} label
 */
EntityUpdateVersion.prototype['label'] = undefined;

/**
 * Entity name
 * @member {String} name
 */
EntityUpdateVersion.prototype['name'] = undefined;

/**
 * Normalized form of the entity. Will replace entity name in the output
 * @member {String} normalized
 */
EntityUpdateVersion.prototype['normalized'] = undefined;

/**
 * Type of the entity (Company, Person, any custom type)
 * @member {String} type
 */
EntityUpdateVersion.prototype['type'] = undefined;






export default EntityUpdateVersion;

