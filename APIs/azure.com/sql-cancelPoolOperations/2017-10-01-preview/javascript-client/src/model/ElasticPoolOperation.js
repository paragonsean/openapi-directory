/**
 * SqlManagementClient
 * The Azure SQL Database management API provides a RESTful set of web APIs that interact with Azure SQL Database services to manage your databases. The API enables users to create, retrieve, update, and delete databases, servers, and other entities.
 *
 * The version of the OpenAPI document: 2017-10-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ElasticPoolOperationProperties from './ElasticPoolOperationProperties';

/**
 * The ElasticPoolOperation model module.
 * @module model/ElasticPoolOperation
 * @version 2017-10-01-preview
 */
class ElasticPoolOperation {
    /**
     * Constructs a new <code>ElasticPoolOperation</code>.
     * A elastic pool operation.
     * @alias module:model/ElasticPoolOperation
     */
    constructor() { 
        
        ElasticPoolOperation.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ElasticPoolOperation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ElasticPoolOperation} obj Optional instance to populate.
     * @return {module:model/ElasticPoolOperation} The populated <code>ElasticPoolOperation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ElasticPoolOperation();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ElasticPoolOperationProperties.constructFromObject(data['properties']);
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
     * Validates the JSON data with respect to <code>ElasticPoolOperation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ElasticPoolOperation</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          ElasticPoolOperationProperties.validateJSON(data['properties']);
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
 * @member {module:model/ElasticPoolOperationProperties} properties
 */
ElasticPoolOperation.prototype['properties'] = undefined;

/**
 * Resource ID.
 * @member {String} id
 */
ElasticPoolOperation.prototype['id'] = undefined;

/**
 * Resource name.
 * @member {String} name
 */
ElasticPoolOperation.prototype['name'] = undefined;

/**
 * Resource type.
 * @member {String} type
 */
ElasticPoolOperation.prototype['type'] = undefined;






export default ElasticPoolOperation;

