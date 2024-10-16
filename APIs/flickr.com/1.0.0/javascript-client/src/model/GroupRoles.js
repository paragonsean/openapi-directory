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
 * The GroupRoles model module.
 * @module model/GroupRoles
 * @version 1.0.0
 */
class GroupRoles {
    /**
     * Constructs a new <code>GroupRoles</code>.
     * @alias module:model/GroupRoles
     */
    constructor() { 
        
        GroupRoles.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GroupRoles</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GroupRoles} obj Optional instance to populate.
     * @return {module:model/GroupRoles} The populated <code>GroupRoles</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GroupRoles();

            if (data.hasOwnProperty('admin')) {
                obj['admin'] = ApiClient.convertToType(data['admin'], 'String');
            }
            if (data.hasOwnProperty('member')) {
                obj['member'] = ApiClient.convertToType(data['member'], 'String');
            }
            if (data.hasOwnProperty('moderator')) {
                obj['moderator'] = ApiClient.convertToType(data['moderator'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GroupRoles</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GroupRoles</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['admin'] && !(typeof data['admin'] === 'string' || data['admin'] instanceof String)) {
            throw new Error("Expected the field `admin` to be a primitive type in the JSON string but got " + data['admin']);
        }
        // ensure the json data is a string
        if (data['member'] && !(typeof data['member'] === 'string' || data['member'] instanceof String)) {
            throw new Error("Expected the field `member` to be a primitive type in the JSON string but got " + data['member']);
        }
        // ensure the json data is a string
        if (data['moderator'] && !(typeof data['moderator'] === 'string' || data['moderator'] instanceof String)) {
            throw new Error("Expected the field `moderator` to be a primitive type in the JSON string but got " + data['moderator']);
        }

        return true;
    }


}



/**
 * @member {String} admin
 */
GroupRoles.prototype['admin'] = undefined;

/**
 * @member {String} member
 */
GroupRoles.prototype['member'] = undefined;

/**
 * @member {String} moderator
 */
GroupRoles.prototype['moderator'] = undefined;






export default GroupRoles;

