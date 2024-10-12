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
 * The AccountCreate model module.
 * @module model/AccountCreate
 * @version 2.0.0
 */
class AccountCreate {
    /**
     * Constructs a new <code>AccountCreate</code>.
     * @alias module:model/AccountCreate
     * @param email {String} Email of account
     * @param firstName {String} First Name
     */
    constructor(email, firstName) { 
        
        AccountCreate.initialize(this, email, firstName);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, email, firstName) { 
        obj['email'] = email;
        obj['first_name'] = firstName || '';
        obj['institution_user_id'] = '';
        obj['last_name'] = '';
        obj['symplectic_user_id'] = '';
    }

    /**
     * Constructs a <code>AccountCreate</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccountCreate} obj Optional instance to populate.
     * @return {module:model/AccountCreate} The populated <code>AccountCreate</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccountCreate();

            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('first_name')) {
                obj['first_name'] = ApiClient.convertToType(data['first_name'], 'String');
            }
            if (data.hasOwnProperty('group_id')) {
                obj['group_id'] = ApiClient.convertToType(data['group_id'], 'Number');
            }
            if (data.hasOwnProperty('institution_user_id')) {
                obj['institution_user_id'] = ApiClient.convertToType(data['institution_user_id'], 'String');
            }
            if (data.hasOwnProperty('is_active')) {
                obj['is_active'] = ApiClient.convertToType(data['is_active'], 'Boolean');
            }
            if (data.hasOwnProperty('last_name')) {
                obj['last_name'] = ApiClient.convertToType(data['last_name'], 'String');
            }
            if (data.hasOwnProperty('quota')) {
                obj['quota'] = ApiClient.convertToType(data['quota'], 'Number');
            }
            if (data.hasOwnProperty('symplectic_user_id')) {
                obj['symplectic_user_id'] = ApiClient.convertToType(data['symplectic_user_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccountCreate</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccountCreate</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AccountCreate.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['first_name'] && !(typeof data['first_name'] === 'string' || data['first_name'] instanceof String)) {
            throw new Error("Expected the field `first_name` to be a primitive type in the JSON string but got " + data['first_name']);
        }
        // ensure the json data is a string
        if (data['institution_user_id'] && !(typeof data['institution_user_id'] === 'string' || data['institution_user_id'] instanceof String)) {
            throw new Error("Expected the field `institution_user_id` to be a primitive type in the JSON string but got " + data['institution_user_id']);
        }
        // ensure the json data is a string
        if (data['last_name'] && !(typeof data['last_name'] === 'string' || data['last_name'] instanceof String)) {
            throw new Error("Expected the field `last_name` to be a primitive type in the JSON string but got " + data['last_name']);
        }
        // ensure the json data is a string
        if (data['symplectic_user_id'] && !(typeof data['symplectic_user_id'] === 'string' || data['symplectic_user_id'] instanceof String)) {
            throw new Error("Expected the field `symplectic_user_id` to be a primitive type in the JSON string but got " + data['symplectic_user_id']);
        }

        return true;
    }


}

AccountCreate.RequiredProperties = ["email", "first_name"];

/**
 * Email of account
 * @member {String} email
 */
AccountCreate.prototype['email'] = undefined;

/**
 * First Name
 * @member {String} first_name
 * @default ''
 */
AccountCreate.prototype['first_name'] = '';

/**
 * Not applicable to regular users. This field is reserved to institutions/publishers with access to assign to specific groups
 * @member {Number} group_id
 */
AccountCreate.prototype['group_id'] = undefined;

/**
 * Institution user id
 * @member {String} institution_user_id
 * @default ''
 */
AccountCreate.prototype['institution_user_id'] = '';

/**
 * Is account active
 * @member {Boolean} is_active
 */
AccountCreate.prototype['is_active'] = undefined;

/**
 * Last Name
 * @member {String} last_name
 * @default ''
 */
AccountCreate.prototype['last_name'] = '';

/**
 * Account quota
 * @member {Number} quota
 */
AccountCreate.prototype['quota'] = undefined;

/**
 * Symplectic user id
 * @member {String} symplectic_user_id
 * @default ''
 */
AccountCreate.prototype['symplectic_user_id'] = '';






export default AccountCreate;

