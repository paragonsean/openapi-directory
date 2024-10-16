/**
 * Blazemeter API Explorer
 * Live API Documentation
 *
 * The version of the OpenAPI document: 4
 * Contact: support@blazemeter.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UserModel1 model module.
 * @module model/UserModel1
 * @version 4
 */
class UserModel1 {
    /**
     * Constructs a new <code>UserModel1</code>.
     * UserModel1 Model
     * @alias module:model/UserModel1
     * @param currentPassword {String} 
     * @param newPassword {String} 
     */
    constructor(currentPassword, newPassword) { 
        
        UserModel1.initialize(this, currentPassword, newPassword);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, currentPassword, newPassword) { 
        obj['currentPassword'] = currentPassword;
        obj['newPassword'] = newPassword;
    }

    /**
     * Constructs a <code>UserModel1</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UserModel1} obj Optional instance to populate.
     * @return {module:model/UserModel1} The populated <code>UserModel1</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UserModel1();

            if (data.hasOwnProperty('currentPassword')) {
                obj['currentPassword'] = ApiClient.convertToType(data['currentPassword'], 'String');
            }
            if (data.hasOwnProperty('newPassword')) {
                obj['newPassword'] = ApiClient.convertToType(data['newPassword'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UserModel1</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UserModel1</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UserModel1.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['currentPassword'] && !(typeof data['currentPassword'] === 'string' || data['currentPassword'] instanceof String)) {
            throw new Error("Expected the field `currentPassword` to be a primitive type in the JSON string but got " + data['currentPassword']);
        }
        // ensure the json data is a string
        if (data['newPassword'] && !(typeof data['newPassword'] === 'string' || data['newPassword'] instanceof String)) {
            throw new Error("Expected the field `newPassword` to be a primitive type in the JSON string but got " + data['newPassword']);
        }

        return true;
    }


}

UserModel1.RequiredProperties = ["currentPassword", "newPassword"];

/**
 * @member {String} currentPassword
 */
UserModel1.prototype['currentPassword'] = undefined;

/**
 * @member {String} newPassword
 */
UserModel1.prototype['newPassword'] = undefined;






export default UserModel1;

