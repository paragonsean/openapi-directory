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
 * The QueryUpdateVersion model module.
 * @module model/QueryUpdateVersion
 * @version 4.0
 */
class QueryUpdateVersion {
    /**
     * Constructs a new <code>QueryUpdateVersion</code>.
     * @alias module:model/QueryUpdateVersion
     * @param id {String} Unique query identifier
     * @param name {String} Query name
     * @param query {String} Boolean query used for content categorization
     */
    constructor(id, name, query) { 
        
        QueryUpdateVersion.initialize(this, id, name, query);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id, name, query) { 
        obj['id'] = id;
        obj['name'] = name;
        obj['query'] = query;
    }

    /**
     * Constructs a <code>QueryUpdateVersion</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/QueryUpdateVersion} obj Optional instance to populate.
     * @return {module:model/QueryUpdateVersion} The populated <code>QueryUpdateVersion</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new QueryUpdateVersion();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('query')) {
                obj['query'] = ApiClient.convertToType(data['query'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>QueryUpdateVersion</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>QueryUpdateVersion</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of QueryUpdateVersion.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['query'] && !(typeof data['query'] === 'string' || data['query'] instanceof String)) {
            throw new Error("Expected the field `query` to be a primitive type in the JSON string but got " + data['query']);
        }

        return true;
    }


}

QueryUpdateVersion.RequiredProperties = ["id", "name", "query"];

/**
 * Unique query identifier
 * @member {String} id
 */
QueryUpdateVersion.prototype['id'] = undefined;

/**
 * Query name
 * @member {String} name
 */
QueryUpdateVersion.prototype['name'] = undefined;

/**
 * Boolean query used for content categorization
 * @member {String} query
 */
QueryUpdateVersion.prototype['query'] = undefined;






export default QueryUpdateVersion;

