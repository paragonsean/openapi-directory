/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GroupBlast model module.
 * @module model/GroupBlast
 * @version 1.0.0
 */
class GroupBlast {
    /**
     * Constructs a new <code>GroupBlast</code>.
     * @alias module:model/GroupBlast
     */
    constructor() { 
        
        GroupBlast.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GroupBlast</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GroupBlast} obj Optional instance to populate.
     * @return {module:model/GroupBlast} The populated <code>GroupBlast</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GroupBlast();

            if (data.hasOwnProperty('_content')) {
                obj['_content'] = ApiClient.convertToType(data['_content'], 'String');
            }
            if (data.hasOwnProperty('date_blast_added')) {
                obj['date_blast_added'] = ApiClient.convertToType(data['date_blast_added'], 'String');
            }
            if (data.hasOwnProperty('user_id')) {
                obj['user_id'] = ApiClient.convertToType(data['user_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GroupBlast</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GroupBlast</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['_content'] && !(typeof data['_content'] === 'string' || data['_content'] instanceof String)) {
            throw new Error("Expected the field `_content` to be a primitive type in the JSON string but got " + data['_content']);
        }
        // ensure the json data is a string
        if (data['date_blast_added'] && !(typeof data['date_blast_added'] === 'string' || data['date_blast_added'] instanceof String)) {
            throw new Error("Expected the field `date_blast_added` to be a primitive type in the JSON string but got " + data['date_blast_added']);
        }
        // ensure the json data is a string
        if (data['user_id'] && !(typeof data['user_id'] === 'string' || data['user_id'] instanceof String)) {
            throw new Error("Expected the field `user_id` to be a primitive type in the JSON string but got " + data['user_id']);
        }

        return true;
    }


}



/**
 * @member {String} _content
 */
GroupBlast.prototype['_content'] = undefined;

/**
 * @member {String} date_blast_added
 */
GroupBlast.prototype['date_blast_added'] = undefined;

/**
 * @member {String} user_id
 */
GroupBlast.prototype['user_id'] = undefined;






export default GroupBlast;

