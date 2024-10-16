/**
 * Story
 * This API is the main entry point for creating, editing and publishing analytics throught the Presalytics API
 *
 * The version of the OpenAPI document: 0.3.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BaseModel from './BaseModel';

/**
 * The PermissionType model module.
 * @module model/PermissionType
 * @version 0.3.1
 */
class PermissionType {
    /**
     * Constructs a new <code>PermissionType</code>.
     * A permission type that can be applied to story collaborator
     * @alias module:model/PermissionType
     * @implements module:model/BaseModel
     */
    constructor() { 
        BaseModel.initialize(this);
        PermissionType.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PermissionType</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PermissionType} obj Optional instance to populate.
     * @return {module:model/PermissionType} The populated <code>PermissionType</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PermissionType();
            BaseModel.constructFromObject(data, obj);

            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'Date');
            }
            if (data.hasOwnProperty('created_by')) {
                obj['created_by'] = ApiClient.convertToType(data['created_by'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'Date');
            }
            if (data.hasOwnProperty('updated_by')) {
                obj['updated_by'] = ApiClient.convertToType(data['updated_by'], 'String');
            }
            if (data.hasOwnProperty('can_add_collaborators')) {
                obj['can_add_collaborators'] = ApiClient.convertToType(data['can_add_collaborators'], 'Boolean');
            }
            if (data.hasOwnProperty('can_delete')) {
                obj['can_delete'] = ApiClient.convertToType(data['can_delete'], 'Boolean');
            }
            if (data.hasOwnProperty('can_edit')) {
                obj['can_edit'] = ApiClient.convertToType(data['can_edit'], 'Boolean');
            }
            if (data.hasOwnProperty('can_view')) {
                obj['can_view'] = ApiClient.convertToType(data['can_view'], 'Boolean');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PermissionType</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PermissionType</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['created_by'] && !(typeof data['created_by'] === 'string' || data['created_by'] instanceof String)) {
            throw new Error("Expected the field `created_by` to be a primitive type in the JSON string but got " + data['created_by']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['updated_by'] && !(typeof data['updated_by'] === 'string' || data['updated_by'] instanceof String)) {
            throw new Error("Expected the field `updated_by` to be a primitive type in the JSON string but got " + data['updated_by']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * @member {Date} created_at
 */
PermissionType.prototype['created_at'] = undefined;

/**
 * @member {String} created_by
 */
PermissionType.prototype['created_by'] = undefined;

/**
 * @member {String} id
 */
PermissionType.prototype['id'] = undefined;

/**
 * @member {Date} updated_at
 */
PermissionType.prototype['updated_at'] = undefined;

/**
 * @member {String} updated_by
 */
PermissionType.prototype['updated_by'] = undefined;

/**
 * @member {Boolean} can_add_collaborators
 */
PermissionType.prototype['can_add_collaborators'] = undefined;

/**
 * @member {Boolean} can_delete
 */
PermissionType.prototype['can_delete'] = undefined;

/**
 * @member {Boolean} can_edit
 */
PermissionType.prototype['can_edit'] = undefined;

/**
 * @member {Boolean} can_view
 */
PermissionType.prototype['can_view'] = undefined;

/**
 * @member {String} name
 */
PermissionType.prototype['name'] = undefined;


// Implement BaseModel interface:
/**
 * @member {Date} created_at
 */
BaseModel.prototype['created_at'] = undefined;
/**
 * @member {String} created_by
 */
BaseModel.prototype['created_by'] = undefined;
/**
 * @member {String} id
 */
BaseModel.prototype['id'] = undefined;
/**
 * @member {Date} updated_at
 */
BaseModel.prototype['updated_at'] = undefined;
/**
 * @member {String} updated_by
 */
BaseModel.prototype['updated_by'] = undefined;




export default PermissionType;

