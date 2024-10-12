/**
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01-privatepreview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The TagsObject model module.
 * @module model/TagsObject
 * @version 2018-06-01-privatepreview
 */
class TagsObject {
    /**
     * Constructs a new <code>TagsObject</code>.
     * Tags object for patch operations.
     * @alias module:model/TagsObject
     */
    constructor() { 
        
        TagsObject.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TagsObject</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TagsObject} obj Optional instance to populate.
     * @return {module:model/TagsObject} The populated <code>TagsObject</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TagsObject();

            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], {'String': 'String'});
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TagsObject</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TagsObject</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Resource tags.
 * @member {Object.<String, String>} tags
 */
TagsObject.prototype['tags'] = undefined;






export default TagsObject;

