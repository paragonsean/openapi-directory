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
 * The ShortAccount model module.
 * @module model/ShortAccount
 * @version 2.0.0
 */
class ShortAccount {
    /**
     * Constructs a new <code>ShortAccount</code>.
     * @alias module:model/ShortAccount
     * @param active {Number} Account activity status
     * @param email {String} User email
     * @param firstName {String} First Name
     * @param id {Number} Account id
     * @param institutionId {Number} Account institution
     * @param institutionUserId {String} Account institution user id
     * @param lastName {String} Last Name
     * @param orcidId {String} ORCID iD associated to account
     * @param quota {Number} Total storage available to account, in bytes
     * @param usedQuota {Number} Storage used by the account, in bytes
     * @param userId {Number} User id associated with account, useful for example for adding the account as an author to an item
     */
    constructor(active, email, firstName, id, institutionId, institutionUserId, lastName, orcidId, quota, usedQuota, userId) { 
        
        ShortAccount.initialize(this, active, email, firstName, id, institutionId, institutionUserId, lastName, orcidId, quota, usedQuota, userId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, active, email, firstName, id, institutionId, institutionUserId, lastName, orcidId, quota, usedQuota, userId) { 
        obj['active'] = active;
        obj['email'] = email;
        obj['first_name'] = firstName;
        obj['id'] = id;
        obj['institution_id'] = institutionId;
        obj['institution_user_id'] = institutionUserId;
        obj['last_name'] = lastName;
        obj['orcid_id'] = orcidId;
        obj['quota'] = quota;
        obj['used_quota'] = usedQuota;
        obj['user_id'] = userId;
    }

    /**
     * Constructs a <code>ShortAccount</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ShortAccount} obj Optional instance to populate.
     * @return {module:model/ShortAccount} The populated <code>ShortAccount</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ShortAccount();

            if (data.hasOwnProperty('active')) {
                obj['active'] = ApiClient.convertToType(data['active'], 'Number');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('first_name')) {
                obj['first_name'] = ApiClient.convertToType(data['first_name'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('institution_id')) {
                obj['institution_id'] = ApiClient.convertToType(data['institution_id'], 'Number');
            }
            if (data.hasOwnProperty('institution_user_id')) {
                obj['institution_user_id'] = ApiClient.convertToType(data['institution_user_id'], 'String');
            }
            if (data.hasOwnProperty('last_name')) {
                obj['last_name'] = ApiClient.convertToType(data['last_name'], 'String');
            }
            if (data.hasOwnProperty('orcid_id')) {
                obj['orcid_id'] = ApiClient.convertToType(data['orcid_id'], 'String');
            }
            if (data.hasOwnProperty('quota')) {
                obj['quota'] = ApiClient.convertToType(data['quota'], 'Number');
            }
            if (data.hasOwnProperty('used_quota')) {
                obj['used_quota'] = ApiClient.convertToType(data['used_quota'], 'Number');
            }
            if (data.hasOwnProperty('user_id')) {
                obj['user_id'] = ApiClient.convertToType(data['user_id'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ShortAccount</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ShortAccount</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ShortAccount.RequiredProperties) {
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
        if (data['orcid_id'] && !(typeof data['orcid_id'] === 'string' || data['orcid_id'] instanceof String)) {
            throw new Error("Expected the field `orcid_id` to be a primitive type in the JSON string but got " + data['orcid_id']);
        }

        return true;
    }


}

ShortAccount.RequiredProperties = ["active", "email", "first_name", "id", "institution_id", "institution_user_id", "last_name", "orcid_id", "quota", "used_quota", "user_id"];

/**
 * Account activity status
 * @member {Number} active
 */
ShortAccount.prototype['active'] = undefined;

/**
 * User email
 * @member {String} email
 */
ShortAccount.prototype['email'] = undefined;

/**
 * First Name
 * @member {String} first_name
 */
ShortAccount.prototype['first_name'] = undefined;

/**
 * Account id
 * @member {Number} id
 */
ShortAccount.prototype['id'] = undefined;

/**
 * Account institution
 * @member {Number} institution_id
 */
ShortAccount.prototype['institution_id'] = undefined;

/**
 * Account institution user id
 * @member {String} institution_user_id
 */
ShortAccount.prototype['institution_user_id'] = undefined;

/**
 * Last Name
 * @member {String} last_name
 */
ShortAccount.prototype['last_name'] = undefined;

/**
 * ORCID iD associated to account
 * @member {String} orcid_id
 */
ShortAccount.prototype['orcid_id'] = undefined;

/**
 * Total storage available to account, in bytes
 * @member {Number} quota
 */
ShortAccount.prototype['quota'] = undefined;

/**
 * Storage used by the account, in bytes
 * @member {Number} used_quota
 */
ShortAccount.prototype['used_quota'] = undefined;

/**
 * User id associated with account, useful for example for adding the account as an author to an item
 * @member {Number} user_id
 */
ShortAccount.prototype['user_id'] = undefined;






export default ShortAccount;

