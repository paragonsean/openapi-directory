/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ManagedAccountDto model module.
 * @module model/ManagedAccountDto
 * @version V2
 */
class ManagedAccountDto {
    /**
     * Constructs a new <code>ManagedAccountDto</code>.
     * ~
     * @alias module:model/ManagedAccountDto
     */
    constructor() { 
        
        ManagedAccountDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ManagedAccountDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ManagedAccountDto} obj Optional instance to populate.
     * @return {module:model/ManagedAccountDto} The populated <code>ManagedAccountDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ManagedAccountDto();

            if (data.hasOwnProperty('accountHolderId')) {
                obj['accountHolderId'] = ApiClient.convertToType(data['accountHolderId'], 'String');
            }
            if (data.hasOwnProperty('credits')) {
                obj['credits'] = ApiClient.convertToType(data['credits'], 'Number');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('lastLogin')) {
                obj['lastLogin'] = ApiClient.convertToType(data['lastLogin'], 'Date');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ManagedAccountDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ManagedAccountDto</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['accountHolderId'] && !(typeof data['accountHolderId'] === 'string' || data['accountHolderId'] instanceof String)) {
            throw new Error("Expected the field `accountHolderId` to be a primitive type in the JSON string but got " + data['accountHolderId']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['state'] && !(typeof data['state'] === 'string' || data['state'] instanceof String)) {
            throw new Error("Expected the field `state` to be a primitive type in the JSON string but got " + data['state']);
        }

        return true;
    }


}



/**
 * ~
 * @member {String} accountHolderId
 */
ManagedAccountDto.prototype['accountHolderId'] = undefined;

/**
 * ~
 * @member {Number} credits
 */
ManagedAccountDto.prototype['credits'] = undefined;

/**
 * ~
 * @member {String} email
 */
ManagedAccountDto.prototype['email'] = undefined;

/**
 * ~
 * @member {String} id
 */
ManagedAccountDto.prototype['id'] = undefined;

/**
 * ~
 * @member {Date} lastLogin
 */
ManagedAccountDto.prototype['lastLogin'] = undefined;

/**
 * ~
 * @member {String} name
 */
ManagedAccountDto.prototype['name'] = undefined;

/**
 * ~
 * @member {module:model/ManagedAccountDto.StateEnum} state
 */
ManagedAccountDto.prototype['state'] = undefined;





/**
 * Allowed values for the <code>state</code> property.
 * @enum {String}
 * @readonly
 */
ManagedAccountDto['StateEnum'] = {

    /**
     * value: "ACTIVE"
     * @const
     */
    "ACTIVE": "ACTIVE",

    /**
     * value: "PENDING"
     * @const
     */
    "PENDING": "PENDING",

    /**
     * value: "PENDING_VERIFICATION"
     * @const
     */
    "PENDING_VERIFICATION": "PENDING_VERIFICATION",

    /**
     * value: "IN_REVIEW"
     * @const
     */
    "IN_REVIEW": "IN_REVIEW"
};



export default ManagedAccountDto;

