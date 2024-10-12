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
 * The CreateAccountByVerifiedMobileRequest model module.
 * @module model/CreateAccountByVerifiedMobileRequest
 * @version 1.0
 */
class CreateAccountByVerifiedMobileRequest {
    /**
     * Constructs a new <code>CreateAccountByVerifiedMobileRequest</code>.
     * @alias module:model/CreateAccountByVerifiedMobileRequest
     * @param txnId {String} 
     */
    constructor(txnId) { 
        
        CreateAccountByVerifiedMobileRequest.initialize(this, txnId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, txnId) { 
        obj['txnId'] = txnId;
    }

    /**
     * Constructs a <code>CreateAccountByVerifiedMobileRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateAccountByVerifiedMobileRequest} obj Optional instance to populate.
     * @return {module:model/CreateAccountByVerifiedMobileRequest} The populated <code>CreateAccountByVerifiedMobileRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateAccountByVerifiedMobileRequest();

            if (data.hasOwnProperty('address')) {
                obj['address'] = ApiClient.convertToType(data['address'], 'String');
            }
            if (data.hasOwnProperty('dayOfBirth')) {
                obj['dayOfBirth'] = ApiClient.convertToType(data['dayOfBirth'], 'String');
            }
            if (data.hasOwnProperty('districtCode')) {
                obj['districtCode'] = ApiClient.convertToType(data['districtCode'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('firstName')) {
                obj['firstName'] = ApiClient.convertToType(data['firstName'], 'String');
            }
            if (data.hasOwnProperty('gender')) {
                obj['gender'] = ApiClient.convertToType(data['gender'], 'String');
            }
            if (data.hasOwnProperty('healthId')) {
                obj['healthId'] = ApiClient.convertToType(data['healthId'], 'String');
            }
            if (data.hasOwnProperty('lastName')) {
                obj['lastName'] = ApiClient.convertToType(data['lastName'], 'String');
            }
            if (data.hasOwnProperty('middleName')) {
                obj['middleName'] = ApiClient.convertToType(data['middleName'], 'String');
            }
            if (data.hasOwnProperty('monthOfBirth')) {
                obj['monthOfBirth'] = ApiClient.convertToType(data['monthOfBirth'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
            if (data.hasOwnProperty('pincode')) {
                obj['pincode'] = ApiClient.convertToType(data['pincode'], 'Number');
            }
            if (data.hasOwnProperty('profilePhoto')) {
                obj['profilePhoto'] = ApiClient.convertToType(data['profilePhoto'], 'String');
            }
            if (data.hasOwnProperty('restrictions')) {
                obj['restrictions'] = ApiClient.convertToType(data['restrictions'], 'String');
            }
            if (data.hasOwnProperty('stateCode')) {
                obj['stateCode'] = ApiClient.convertToType(data['stateCode'], 'String');
            }
            if (data.hasOwnProperty('subdistrictCode')) {
                obj['subdistrictCode'] = ApiClient.convertToType(data['subdistrictCode'], 'String');
            }
            if (data.hasOwnProperty('token')) {
                obj['token'] = ApiClient.convertToType(data['token'], 'String');
            }
            if (data.hasOwnProperty('townCode')) {
                obj['townCode'] = ApiClient.convertToType(data['townCode'], 'String');
            }
            if (data.hasOwnProperty('txnId')) {
                obj['txnId'] = ApiClient.convertToType(data['txnId'], 'String');
            }
            if (data.hasOwnProperty('villageCode')) {
                obj['villageCode'] = ApiClient.convertToType(data['villageCode'], 'String');
            }
            if (data.hasOwnProperty('wardCode')) {
                obj['wardCode'] = ApiClient.convertToType(data['wardCode'], 'String');
            }
            if (data.hasOwnProperty('yearOfBirth')) {
                obj['yearOfBirth'] = ApiClient.convertToType(data['yearOfBirth'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateAccountByVerifiedMobileRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateAccountByVerifiedMobileRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateAccountByVerifiedMobileRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['address'] && !(typeof data['address'] === 'string' || data['address'] instanceof String)) {
            throw new Error("Expected the field `address` to be a primitive type in the JSON string but got " + data['address']);
        }
        // ensure the json data is a string
        if (data['dayOfBirth'] && !(typeof data['dayOfBirth'] === 'string' || data['dayOfBirth'] instanceof String)) {
            throw new Error("Expected the field `dayOfBirth` to be a primitive type in the JSON string but got " + data['dayOfBirth']);
        }
        // ensure the json data is a string
        if (data['districtCode'] && !(typeof data['districtCode'] === 'string' || data['districtCode'] instanceof String)) {
            throw new Error("Expected the field `districtCode` to be a primitive type in the JSON string but got " + data['districtCode']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['firstName'] && !(typeof data['firstName'] === 'string' || data['firstName'] instanceof String)) {
            throw new Error("Expected the field `firstName` to be a primitive type in the JSON string but got " + data['firstName']);
        }
        // ensure the json data is a string
        if (data['gender'] && !(typeof data['gender'] === 'string' || data['gender'] instanceof String)) {
            throw new Error("Expected the field `gender` to be a primitive type in the JSON string but got " + data['gender']);
        }
        // ensure the json data is a string
        if (data['healthId'] && !(typeof data['healthId'] === 'string' || data['healthId'] instanceof String)) {
            throw new Error("Expected the field `healthId` to be a primitive type in the JSON string but got " + data['healthId']);
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
        if (data['monthOfBirth'] && !(typeof data['monthOfBirth'] === 'string' || data['monthOfBirth'] instanceof String)) {
            throw new Error("Expected the field `monthOfBirth` to be a primitive type in the JSON string but got " + data['monthOfBirth']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
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
        if (data['stateCode'] && !(typeof data['stateCode'] === 'string' || data['stateCode'] instanceof String)) {
            throw new Error("Expected the field `stateCode` to be a primitive type in the JSON string but got " + data['stateCode']);
        }
        // ensure the json data is a string
        if (data['subdistrictCode'] && !(typeof data['subdistrictCode'] === 'string' || data['subdistrictCode'] instanceof String)) {
            throw new Error("Expected the field `subdistrictCode` to be a primitive type in the JSON string but got " + data['subdistrictCode']);
        }
        // ensure the json data is a string
        if (data['token'] && !(typeof data['token'] === 'string' || data['token'] instanceof String)) {
            throw new Error("Expected the field `token` to be a primitive type in the JSON string but got " + data['token']);
        }
        // ensure the json data is a string
        if (data['townCode'] && !(typeof data['townCode'] === 'string' || data['townCode'] instanceof String)) {
            throw new Error("Expected the field `townCode` to be a primitive type in the JSON string but got " + data['townCode']);
        }
        // ensure the json data is a string
        if (data['txnId'] && !(typeof data['txnId'] === 'string' || data['txnId'] instanceof String)) {
            throw new Error("Expected the field `txnId` to be a primitive type in the JSON string but got " + data['txnId']);
        }
        // ensure the json data is a string
        if (data['villageCode'] && !(typeof data['villageCode'] === 'string' || data['villageCode'] instanceof String)) {
            throw new Error("Expected the field `villageCode` to be a primitive type in the JSON string but got " + data['villageCode']);
        }
        // ensure the json data is a string
        if (data['wardCode'] && !(typeof data['wardCode'] === 'string' || data['wardCode'] instanceof String)) {
            throw new Error("Expected the field `wardCode` to be a primitive type in the JSON string but got " + data['wardCode']);
        }
        // ensure the json data is a string
        if (data['yearOfBirth'] && !(typeof data['yearOfBirth'] === 'string' || data['yearOfBirth'] instanceof String)) {
            throw new Error("Expected the field `yearOfBirth` to be a primitive type in the JSON string but got " + data['yearOfBirth']);
        }

        return true;
    }


}

CreateAccountByVerifiedMobileRequest.RequiredProperties = ["txnId"];

/**
 * @member {String} address
 */
CreateAccountByVerifiedMobileRequest.prototype['address'] = undefined;

/**
 * @member {String} dayOfBirth
 */
CreateAccountByVerifiedMobileRequest.prototype['dayOfBirth'] = undefined;

/**
 * @member {String} districtCode
 */
CreateAccountByVerifiedMobileRequest.prototype['districtCode'] = undefined;

/**
 * @member {String} email
 */
CreateAccountByVerifiedMobileRequest.prototype['email'] = undefined;

/**
 * @member {String} firstName
 */
CreateAccountByVerifiedMobileRequest.prototype['firstName'] = undefined;

/**
 * @member {String} gender
 */
CreateAccountByVerifiedMobileRequest.prototype['gender'] = undefined;

/**
 * @member {String} healthId
 */
CreateAccountByVerifiedMobileRequest.prototype['healthId'] = undefined;

/**
 * @member {String} lastName
 */
CreateAccountByVerifiedMobileRequest.prototype['lastName'] = undefined;

/**
 * @member {String} middleName
 */
CreateAccountByVerifiedMobileRequest.prototype['middleName'] = undefined;

/**
 * @member {String} monthOfBirth
 */
CreateAccountByVerifiedMobileRequest.prototype['monthOfBirth'] = undefined;

/**
 * @member {String} name
 */
CreateAccountByVerifiedMobileRequest.prototype['name'] = undefined;

/**
 * @member {String} password
 */
CreateAccountByVerifiedMobileRequest.prototype['password'] = undefined;

/**
 * @member {Number} pincode
 */
CreateAccountByVerifiedMobileRequest.prototype['pincode'] = undefined;

/**
 * @member {String} profilePhoto
 */
CreateAccountByVerifiedMobileRequest.prototype['profilePhoto'] = undefined;

/**
 * @member {String} restrictions
 */
CreateAccountByVerifiedMobileRequest.prototype['restrictions'] = undefined;

/**
 * @member {String} stateCode
 */
CreateAccountByVerifiedMobileRequest.prototype['stateCode'] = undefined;

/**
 * @member {String} subdistrictCode
 */
CreateAccountByVerifiedMobileRequest.prototype['subdistrictCode'] = undefined;

/**
 * @member {String} token
 */
CreateAccountByVerifiedMobileRequest.prototype['token'] = undefined;

/**
 * @member {String} townCode
 */
CreateAccountByVerifiedMobileRequest.prototype['townCode'] = undefined;

/**
 * @member {String} txnId
 */
CreateAccountByVerifiedMobileRequest.prototype['txnId'] = undefined;

/**
 * @member {String} villageCode
 */
CreateAccountByVerifiedMobileRequest.prototype['villageCode'] = undefined;

/**
 * @member {String} wardCode
 */
CreateAccountByVerifiedMobileRequest.prototype['wardCode'] = undefined;

/**
 * @member {String} yearOfBirth
 */
CreateAccountByVerifiedMobileRequest.prototype['yearOfBirth'] = undefined;






export default CreateAccountByVerifiedMobileRequest;

