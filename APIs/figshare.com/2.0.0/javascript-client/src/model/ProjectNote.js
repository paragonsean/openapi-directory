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
 * The ProjectNote model module.
 * @module model/ProjectNote
 * @version 2.0.0
 */
class ProjectNote {
    /**
     * Constructs a new <code>ProjectNote</code>.
     * @alias module:model/ProjectNote
     * @param _abstract {String} Note Abstract - short/truncated content
     * @param createdDate {String} Date when note was created
     * @param id {Number} Project note id
     * @param modifiedDate {String} Date when note was last modified
     * @param userId {Number} User who wrote the note
     * @param userName {String} Username of the one who wrote the note
     */
    constructor(_abstract, createdDate, id, modifiedDate, userId, userName) { 
        
        ProjectNote.initialize(this, _abstract, createdDate, id, modifiedDate, userId, userName);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, _abstract, createdDate, id, modifiedDate, userId, userName) { 
        obj['abstract'] = _abstract;
        obj['created_date'] = createdDate;
        obj['id'] = id;
        obj['modified_date'] = modifiedDate;
        obj['user_id'] = userId;
        obj['user_name'] = userName;
    }

    /**
     * Constructs a <code>ProjectNote</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProjectNote} obj Optional instance to populate.
     * @return {module:model/ProjectNote} The populated <code>ProjectNote</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProjectNote();

            if (data.hasOwnProperty('abstract')) {
                obj['abstract'] = ApiClient.convertToType(data['abstract'], 'String');
            }
            if (data.hasOwnProperty('created_date')) {
                obj['created_date'] = ApiClient.convertToType(data['created_date'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('modified_date')) {
                obj['modified_date'] = ApiClient.convertToType(data['modified_date'], 'String');
            }
            if (data.hasOwnProperty('user_id')) {
                obj['user_id'] = ApiClient.convertToType(data['user_id'], 'Number');
            }
            if (data.hasOwnProperty('user_name')) {
                obj['user_name'] = ApiClient.convertToType(data['user_name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProjectNote</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProjectNote</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ProjectNote.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['abstract'] && !(typeof data['abstract'] === 'string' || data['abstract'] instanceof String)) {
            throw new Error("Expected the field `abstract` to be a primitive type in the JSON string but got " + data['abstract']);
        }
        // ensure the json data is a string
        if (data['created_date'] && !(typeof data['created_date'] === 'string' || data['created_date'] instanceof String)) {
            throw new Error("Expected the field `created_date` to be a primitive type in the JSON string but got " + data['created_date']);
        }
        // ensure the json data is a string
        if (data['modified_date'] && !(typeof data['modified_date'] === 'string' || data['modified_date'] instanceof String)) {
            throw new Error("Expected the field `modified_date` to be a primitive type in the JSON string but got " + data['modified_date']);
        }
        // ensure the json data is a string
        if (data['user_name'] && !(typeof data['user_name'] === 'string' || data['user_name'] instanceof String)) {
            throw new Error("Expected the field `user_name` to be a primitive type in the JSON string but got " + data['user_name']);
        }

        return true;
    }


}

ProjectNote.RequiredProperties = ["abstract", "created_date", "id", "modified_date", "user_id", "user_name"];

/**
 * Note Abstract - short/truncated content
 * @member {String} abstract
 */
ProjectNote.prototype['abstract'] = undefined;

/**
 * Date when note was created
 * @member {String} created_date
 */
ProjectNote.prototype['created_date'] = undefined;

/**
 * Project note id
 * @member {Number} id
 */
ProjectNote.prototype['id'] = undefined;

/**
 * Date when note was last modified
 * @member {String} modified_date
 */
ProjectNote.prototype['modified_date'] = undefined;

/**
 * User who wrote the note
 * @member {Number} user_id
 */
ProjectNote.prototype['user_id'] = undefined;

/**
 * Username of the one who wrote the note
 * @member {String} user_name
 */
ProjectNote.prototype['user_name'] = undefined;






export default ProjectNote;

