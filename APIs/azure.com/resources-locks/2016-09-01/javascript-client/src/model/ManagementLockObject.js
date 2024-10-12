/**
 * ManagementLockClient
 * Azure resources can be locked to prevent other users in your organization from deleting or modifying resources.
 *
 * The version of the OpenAPI document: 2016-09-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ManagementLockProperties from './ManagementLockProperties';

/**
 * The ManagementLockObject model module.
 * @module model/ManagementLockObject
 * @version 2016-09-01
 */
class ManagementLockObject {
    /**
     * Constructs a new <code>ManagementLockObject</code>.
     * The lock information.
     * @alias module:model/ManagementLockObject
     * @param properties {module:model/ManagementLockProperties} 
     */
    constructor(properties) { 
        
        ManagementLockObject.initialize(this, properties);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, properties) { 
        obj['properties'] = properties;
    }

    /**
     * Constructs a <code>ManagementLockObject</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ManagementLockObject} obj Optional instance to populate.
     * @return {module:model/ManagementLockObject} The populated <code>ManagementLockObject</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ManagementLockObject();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ManagementLockProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ManagementLockObject</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ManagementLockObject</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ManagementLockObject.RequiredProperties) {
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
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          ManagementLockProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

ManagementLockObject.RequiredProperties = ["properties"];

/**
 * The resource ID of the lock.
 * @member {String} id
 */
ManagementLockObject.prototype['id'] = undefined;

/**
 * The name of the lock.
 * @member {String} name
 */
ManagementLockObject.prototype['name'] = undefined;

/**
 * @member {module:model/ManagementLockProperties} properties
 */
ManagementLockObject.prototype['properties'] = undefined;

/**
 * The resource type of the lock - Microsoft.Authorization/locks.
 * @member {String} type
 */
ManagementLockObject.prototype['type'] = undefined;






export default ManagementLockObject;

