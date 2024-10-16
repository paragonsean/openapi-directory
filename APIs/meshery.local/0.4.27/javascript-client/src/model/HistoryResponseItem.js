/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The HistoryResponseItem model module.
 * @module model/HistoryResponseItem
 * @version 0.4.27
 */
class HistoryResponseItem {
    /**
     * Constructs a new <code>HistoryResponseItem</code>.
     * HistoryResponseItem individual image layer information in response to ImageHistory operation
     * @alias module:model/HistoryResponseItem
     * @param comment {String} comment
     * @param created {Number} created
     * @param createdBy {String} created by
     * @param id {String} Id
     * @param size {Number} size
     * @param tags {Array.<String>} tags
     */
    constructor(comment, created, createdBy, id, size, tags) { 
        
        HistoryResponseItem.initialize(this, comment, created, createdBy, id, size, tags);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, comment, created, createdBy, id, size, tags) { 
        obj['Comment'] = comment;
        obj['Created'] = created;
        obj['CreatedBy'] = createdBy;
        obj['Id'] = id;
        obj['Size'] = size;
        obj['Tags'] = tags;
    }

    /**
     * Constructs a <code>HistoryResponseItem</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HistoryResponseItem} obj Optional instance to populate.
     * @return {module:model/HistoryResponseItem} The populated <code>HistoryResponseItem</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HistoryResponseItem();

            if (data.hasOwnProperty('Comment')) {
                obj['Comment'] = ApiClient.convertToType(data['Comment'], 'String');
            }
            if (data.hasOwnProperty('Created')) {
                obj['Created'] = ApiClient.convertToType(data['Created'], 'Number');
            }
            if (data.hasOwnProperty('CreatedBy')) {
                obj['CreatedBy'] = ApiClient.convertToType(data['CreatedBy'], 'String');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'String');
            }
            if (data.hasOwnProperty('Size')) {
                obj['Size'] = ApiClient.convertToType(data['Size'], 'Number');
            }
            if (data.hasOwnProperty('Tags')) {
                obj['Tags'] = ApiClient.convertToType(data['Tags'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HistoryResponseItem</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HistoryResponseItem</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of HistoryResponseItem.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['Comment'] && !(typeof data['Comment'] === 'string' || data['Comment'] instanceof String)) {
            throw new Error("Expected the field `Comment` to be a primitive type in the JSON string but got " + data['Comment']);
        }
        // ensure the json data is a string
        if (data['CreatedBy'] && !(typeof data['CreatedBy'] === 'string' || data['CreatedBy'] instanceof String)) {
            throw new Error("Expected the field `CreatedBy` to be a primitive type in the JSON string but got " + data['CreatedBy']);
        }
        // ensure the json data is a string
        if (data['Id'] && !(typeof data['Id'] === 'string' || data['Id'] instanceof String)) {
            throw new Error("Expected the field `Id` to be a primitive type in the JSON string but got " + data['Id']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['Tags'])) {
            throw new Error("Expected the field `Tags` to be an array in the JSON data but got " + data['Tags']);
        }

        return true;
    }


}

HistoryResponseItem.RequiredProperties = ["Comment", "Created", "CreatedBy", "Id", "Size", "Tags"];

/**
 * comment
 * @member {String} Comment
 */
HistoryResponseItem.prototype['Comment'] = undefined;

/**
 * created
 * @member {Number} Created
 */
HistoryResponseItem.prototype['Created'] = undefined;

/**
 * created by
 * @member {String} CreatedBy
 */
HistoryResponseItem.prototype['CreatedBy'] = undefined;

/**
 * Id
 * @member {String} Id
 */
HistoryResponseItem.prototype['Id'] = undefined;

/**
 * size
 * @member {Number} Size
 */
HistoryResponseItem.prototype['Size'] = undefined;

/**
 * tags
 * @member {Array.<String>} Tags
 */
HistoryResponseItem.prototype['Tags'] = undefined;






export default HistoryResponseItem;

