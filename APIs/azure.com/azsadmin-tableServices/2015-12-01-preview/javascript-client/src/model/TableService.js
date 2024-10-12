/**
 * StorageManagementClient
 * The Admin Storage Management Client.
 *
 * The version of the OpenAPI document: 2015-12-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import TableServiceProperties from './TableServiceProperties';

/**
 * The TableService model module.
 * @module model/TableService
 * @version 2015-12-01-preview
 */
class TableService {
    /**
     * Constructs a new <code>TableService</code>.
     * Table service.
     * @alias module:model/TableService
     */
    constructor() { 
        
        TableService.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TableService</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TableService} obj Optional instance to populate.
     * @return {module:model/TableService} The populated <code>TableService</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TableService();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = TableServiceProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('location')) {
                obj['location'] = ApiClient.convertToType(data['location'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], {'String': 'String'});
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TableService</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TableService</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          TableServiceProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['location'] && !(typeof data['location'] === 'string' || data['location'] instanceof String)) {
            throw new Error("Expected the field `location` to be a primitive type in the JSON string but got " + data['location']);
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
 * @member {module:model/TableServiceProperties} properties
 */
TableService.prototype['properties'] = undefined;

/**
 * Resource ID.
 * @member {String} id
 */
TableService.prototype['id'] = undefined;

/**
 * Resource location.
 * @member {String} location
 */
TableService.prototype['location'] = undefined;

/**
 * Resource Name.
 * @member {String} name
 */
TableService.prototype['name'] = undefined;

/**
 * Resource tags.
 * @member {Object.<String, String>} tags
 */
TableService.prototype['tags'] = undefined;

/**
 * Resource type.
 * @member {String} type
 */
TableService.prototype['type'] = undefined;






export default TableService;

