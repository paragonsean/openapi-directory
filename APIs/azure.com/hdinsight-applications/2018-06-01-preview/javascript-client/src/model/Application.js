/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ApplicationProperties from './ApplicationProperties';

/**
 * The Application model module.
 * @module model/Application
 * @version 2018-06-01-preview
 */
class Application {
    /**
     * Constructs a new <code>Application</code>.
     * The HDInsight cluster application
     * @alias module:model/Application
     */
    constructor() { 
        
        Application.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Application</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Application} obj Optional instance to populate.
     * @return {module:model/Application} The populated <code>Application</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Application();

            if (data.hasOwnProperty('etag')) {
                obj['etag'] = ApiClient.convertToType(data['etag'], 'String');
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ApplicationProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], {'String': 'String'});
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Application</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Application</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['etag'] && !(typeof data['etag'] === 'string' || data['etag'] instanceof String)) {
            throw new Error("Expected the field `etag` to be a primitive type in the JSON string but got " + data['etag']);
        }
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          ApplicationProperties.validateJSON(data['properties']);
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
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * The ETag for the application
 * @member {String} etag
 */
Application.prototype['etag'] = undefined;

/**
 * @member {module:model/ApplicationProperties} properties
 */
Application.prototype['properties'] = undefined;

/**
 * The tags for the application.
 * @member {Object.<String, String>} tags
 */
Application.prototype['tags'] = undefined;

/**
 * Fully qualified resource Id for the resource.
 * @member {String} id
 */
Application.prototype['id'] = undefined;

/**
 * The name of the resource
 * @member {String} name
 */
Application.prototype['name'] = undefined;

/**
 * The type of the resource.
 * @member {String} type
 */
Application.prototype['type'] = undefined;






export default Application;

