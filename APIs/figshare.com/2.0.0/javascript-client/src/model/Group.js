/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Group model module.
 * @module model/Group
 * @version 2.0.0
 */
class Group {
    /**
     * Constructs a new <code>Group</code>.
     * @alias module:model/Group
     * @param associationCriteria {String} HR code associated with group, if code exists
     * @param id {Number} Group id
     * @param name {String} Group name
     * @param parentId {Number} Parent group if any
     * @param resourceId {String} Group resource id
     */
    constructor(associationCriteria, id, name, parentId, resourceId) { 
        
        Group.initialize(this, associationCriteria, id, name, parentId, resourceId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, associationCriteria, id, name, parentId, resourceId) { 
        obj['association_criteria'] = associationCriteria;
        obj['id'] = id;
        obj['name'] = name;
        obj['parent_id'] = parentId;
        obj['resource_id'] = resourceId;
    }

    /**
     * Constructs a <code>Group</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Group} obj Optional instance to populate.
     * @return {module:model/Group} The populated <code>Group</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Group();

            if (data.hasOwnProperty('association_criteria')) {
                obj['association_criteria'] = ApiClient.convertToType(data['association_criteria'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('parent_id')) {
                obj['parent_id'] = ApiClient.convertToType(data['parent_id'], 'Number');
            }
            if (data.hasOwnProperty('resource_id')) {
                obj['resource_id'] = ApiClient.convertToType(data['resource_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Group</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Group</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Group.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['association_criteria'] && !(typeof data['association_criteria'] === 'string' || data['association_criteria'] instanceof String)) {
            throw new Error("Expected the field `association_criteria` to be a primitive type in the JSON string but got " + data['association_criteria']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['resource_id'] && !(typeof data['resource_id'] === 'string' || data['resource_id'] instanceof String)) {
            throw new Error("Expected the field `resource_id` to be a primitive type in the JSON string but got " + data['resource_id']);
        }

        return true;
    }


}

Group.RequiredProperties = ["association_criteria", "id", "name", "parent_id", "resource_id"];

/**
 * HR code associated with group, if code exists
 * @member {String} association_criteria
 */
Group.prototype['association_criteria'] = undefined;

/**
 * Group id
 * @member {Number} id
 */
Group.prototype['id'] = undefined;

/**
 * Group name
 * @member {String} name
 */
Group.prototype['name'] = undefined;

/**
 * Parent group if any
 * @member {Number} parent_id
 */
Group.prototype['parent_id'] = undefined;

/**
 * Group resource id
 * @member {String} resource_id
 */
Group.prototype['resource_id'] = undefined;






export default Group;

