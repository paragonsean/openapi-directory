/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The CreateAccountWithAadhaarOtp model module.
 * @module model/CreateAccountWithAadhaarOtp
 * @version 1.0
 */
class CreateAccountWithAadhaarOtp {
    /**
     * Constructs a new <code>CreateAccountWithAadhaarOtp</code>.
     * @alias module:model/CreateAccountWithAadhaarOtp
     */
    constructor() { 
        
        CreateAccountWithAadhaarOtp.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CreateAccountWithAadhaarOtp</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateAccountWithAadhaarOtp} obj Optional instance to populate.
     * @return {module:model/CreateAccountWithAadhaarOtp} The populated <code>CreateAccountWithAadhaarOtp</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateAccountWithAadhaarOtp();

            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('firstName')) {
                obj['firstName'] = ApiClient.convertToType(data['firstName'], 'String');
            }
            if (data.hasOwnProperty('lastName')) {
                obj['lastName'] = ApiClient.convertToType(data['lastName'], 'String');
            }
            if (data.hasOwnProperty('middleName')) {
                obj['middleName'] = ApiClient.convertToType(data['middleName'], 'String');
            }
            if (data.hasOwnProperty('mobile')) {
                obj['mobile'] = ApiClient.convertToType(data['mobile'], 'String');
            }
            if (data.hasOwnProperty('otp')) {
                obj['otp'] = ApiClient.convertToType(data['otp'], 'String');
            }
            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
            if (data.hasOwnProperty('profilePhoto')) {
                obj['profilePhoto'] = ApiClient.convertToType(data['profilePhoto'], 'String');
            }
            if (data.hasOwnProperty('restrictions')) {
                obj['restrictions'] = ApiClient.convertToType(data['restrictions'], 'String');
            }
            if (data.hasOwnProperty('txnId')) {
                obj['txnId'] = ApiClient.convertToType(data['txnId'], 'String');
            }
            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateAccountWithAadhaarOtp</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateAccountWithAadhaarOtp</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['firstName'] && !(typeof data['firstName'] === 'string' || data['firstName'] instanceof String)) {
            throw new Error("Expected the field `firstName` to be a primitive type in the JSON string but got " + data['firstName']);
        }
        // ensure the json data is a string
        if (data['lastName'] && !(typeof data['lastName'] === 'string' || data['lastName'] instanceof String)) {
            throw new Error("Expected the field `lastName` to be a primitive type in the JSON string but got " + data['lastName']);
        }
        // ensure the json data is a string
        if (data['middleName'] && !(typeof data['middleName'] === 'string' || data['middleName'] instanceof String)) {
            throw new Error("Expected the field `middleName` to be a primitive type in the JSON string but got " + data['middleName']);
        }
        // ensure the json data is a string
        if (data['mobile'] && !(typeof data['mobile'] === 'string' || data['mobile'] instanceof String)) {
            throw new Error("Expected the field `mobile` to be a primitive type in the JSON string but got " + data['mobile']);
        }
        // ensure the json data is a string
        if (data['otp'] && !(typeof data['otp'] === 'string' || data['otp'] instanceof String)) {
            throw new Error("Expected the field `otp` to be a primitive type in the JSON string but got " + data['otp']);
        }
        // ensure the json data is a string
        if (data['password'] && !(typeof data['password'] === 'string' || data['password'] instanceof String)) {
            throw new Error("Expected the field `password` to be a primitive type in the JSON string but got " + data['password']);
        }
        // ensure the json data is a string
        if (data['profilePhoto'] && !(typeof data['profilePhoto'] === 'string' || data['profilePhoto'] instanceof String)) {
            throw new Error("Expected the field `profilePhoto` to be a primitive type in the JSON string but got " + data['profilePhoto']);
        }
        // ensure the json data is a string
        if (data['restrictions'] && !(typeof data['restrictions'] === 'string' || data['restrictions'] instanceof String)) {
            throw new Error("Expected the field `restrictions` to be a primitive type in the JSON string but got " + data['restrictions']);
        }
        // ensure the json data is a string
        if (data['txnId'] && !(typeof data['txnId'] === 'string' || data['txnId'] instanceof String)) {
            throw new Error("Expected the field `txnId` to be a primitive type in the JSON string but got " + data['txnId']);
        }
        // ensure the json data is a string
        if (data['username'] && !(typeof data['username'] === 'string' || data['username'] instanceof String)) {
            throw new Error("Expected the field `username` to be a primitive type in the JSON string but got " + data['username']);
        }

        return true;
    }


}



/**
 * @member {String} email
 */
CreateAccountWithAadhaarOtp.prototype['email'] = undefined;

/**
 * @member {String} firstName
 */
CreateAccountWithAadhaarOtp.prototype['firstName'] = undefined;

/**
 * @member {String} lastName
 */
CreateAccountWithAadhaarOtp.prototype['lastName'] = undefined;

/**
 * @member {String} middleName
 */
CreateAccountWithAadhaarOtp.prototype['middleName'] = undefined;

/**
 * @member {String} mobile
 */
CreateAccountWithAadhaarOtp.prototype['mobile'] = undefined;

/**
 * @member {String} otp
 */
CreateAccountWithAadhaarOtp.prototype['otp'] = undefined;

/**
 * @member {String} password
 */
CreateAccountWithAadhaarOtp.prototype['password'] = undefined;

/**
 * @member {String} profilePhoto
 */
CreateAccountWithAadhaarOtp.prototype['profilePhoto'] = undefined;

/**
 * @member {String} restrictions
 */
CreateAccountWithAadhaarOtp.prototype['restrictions'] = undefined;

/**
 * @member {String} txnId
 */
CreateAccountWithAadhaarOtp.prototype['txnId'] = undefined;

/**
 * @member {String} username
 */
CreateAccountWithAadhaarOtp.prototype['username'] = undefined;






export default CreateAccountWithAadhaarOtp;

