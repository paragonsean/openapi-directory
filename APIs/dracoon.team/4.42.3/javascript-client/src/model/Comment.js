/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import UserInfo from './UserInfo';

/**
 * The Comment model module.
 * @module model/Comment
 * @version 4.42.3
 */
class Comment {
    /**
     * Constructs a new <code>Comment</code>.
     * Node comment information
     * @alias module:model/Comment
     * @param createdAt {Date} Creation date
     * @param createdBy {module:model/UserInfo} 
     * @param id {Number} Comment ID
     * @param isChanged {Boolean} Determines whether comment was edited or not
     * @param isDeleted {Boolean} Determines whether comment was deleted or not
     * @param text {String} Comment text
     * @param updatedAt {Date} Modification date
     * @param updatedBy {module:model/UserInfo} 
     */
    constructor(createdAt, createdBy, id, isChanged, isDeleted, text, updatedAt, updatedBy) { 
        
        Comment.initialize(this, createdAt, createdBy, id, isChanged, isDeleted, text, updatedAt, updatedBy);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, createdAt, createdBy, id, isChanged, isDeleted, text, updatedAt, updatedBy) { 
        obj['createdAt'] = createdAt;
        obj['createdBy'] = createdBy;
        obj['id'] = id;
        obj['isChanged'] = isChanged;
        obj['isDeleted'] = isDeleted;
        obj['text'] = text;
        obj['updatedAt'] = updatedAt;
        obj['updatedBy'] = updatedBy;
    }

    /**
     * Constructs a <code>Comment</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Comment} obj Optional instance to populate.
     * @return {module:model/Comment} The populated <code>Comment</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Comment();

            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'Date');
            }
            if (data.hasOwnProperty('createdBy')) {
                obj['createdBy'] = UserInfo.constructFromObject(data['createdBy']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('isChanged')) {
                obj['isChanged'] = ApiClient.convertToType(data['isChanged'], 'Boolean');
            }
            if (data.hasOwnProperty('isDeleted')) {
                obj['isDeleted'] = ApiClient.convertToType(data['isDeleted'], 'Boolean');
            }
            if (data.hasOwnProperty('text')) {
                obj['text'] = ApiClient.convertToType(data['text'], 'String');
            }
            if (data.hasOwnProperty('updatedAt')) {
                obj['updatedAt'] = ApiClient.convertToType(data['updatedAt'], 'Date');
            }
            if (data.hasOwnProperty('updatedBy')) {
                obj['updatedBy'] = UserInfo.constructFromObject(data['updatedBy']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Comment</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Comment</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Comment.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `createdBy`
        if (data['createdBy']) { // data not null
          UserInfo.validateJSON(data['createdBy']);
        }
        // ensure the json data is a string
        if (data['text'] && !(typeof data['text'] === 'string' || data['text'] instanceof String)) {
            throw new Error("Expected the field `text` to be a primitive type in the JSON string but got " + data['text']);
        }
        // validate the optional field `updatedBy`
        if (data['updatedBy']) { // data not null
          UserInfo.validateJSON(data['updatedBy']);
        }

        return true;
    }


}

Comment.RequiredProperties = ["createdAt", "createdBy", "id", "isChanged", "isDeleted", "text", "updatedAt", "updatedBy"];

/**
 * Creation date
 * @member {Date} createdAt
 */
Comment.prototype['createdAt'] = undefined;

/**
 * @member {module:model/UserInfo} createdBy
 */
Comment.prototype['createdBy'] = undefined;

/**
 * Comment ID
 * @member {Number} id
 */
Comment.prototype['id'] = undefined;

/**
 * Determines whether comment was edited or not
 * @member {Boolean} isChanged
 */
Comment.prototype['isChanged'] = undefined;

/**
 * Determines whether comment was deleted or not
 * @member {Boolean} isDeleted
 */
Comment.prototype['isDeleted'] = undefined;

/**
 * Comment text
 * @member {String} text
 */
Comment.prototype['text'] = undefined;

/**
 * Modification date
 * @member {Date} updatedAt
 */
Comment.prototype['updatedAt'] = undefined;

/**
 * @member {module:model/UserInfo} updatedBy
 */
Comment.prototype['updatedBy'] = undefined;






export default Comment;

