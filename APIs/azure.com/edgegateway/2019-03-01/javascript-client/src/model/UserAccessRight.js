/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UserAccessRight model module.
 * @module model/UserAccessRight
 * @version 2019-03-01
 */
class UserAccessRight {
    /**
     * Constructs a new <code>UserAccessRight</code>.
     * The mapping between a particular user and the access type on the SMB share.
     * @alias module:model/UserAccessRight
     * @param accessType {module:model/UserAccessRight.AccessTypeEnum} Type of access to be allowed for the user.
     * @param userId {String} User ID (already existing in the device).
     */
    constructor(accessType, userId) { 
        
        UserAccessRight.initialize(this, accessType, userId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, accessType, userId) { 
        obj['accessType'] = accessType;
        obj['userId'] = userId;
    }

    /**
     * Constructs a <code>UserAccessRight</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UserAccessRight} obj Optional instance to populate.
     * @return {module:model/UserAccessRight} The populated <code>UserAccessRight</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UserAccessRight();

            if (data.hasOwnProperty('accessType')) {
                obj['accessType'] = ApiClient.convertToType(data['accessType'], 'String');
            }
            if (data.hasOwnProperty('userId')) {
                obj['userId'] = ApiClient.convertToType(data['userId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UserAccessRight</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UserAccessRight</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UserAccessRight.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['accessType'] && !(typeof data['accessType'] === 'string' || data['accessType'] instanceof String)) {
            throw new Error("Expected the field `accessType` to be a primitive type in the JSON string but got " + data['accessType']);
        }
        // ensure the json data is a string
        if (data['userId'] && !(typeof data['userId'] === 'string' || data['userId'] instanceof String)) {
            throw new Error("Expected the field `userId` to be a primitive type in the JSON string but got " + data['userId']);
        }

        return true;
    }


}

UserAccessRight.RequiredProperties = ["accessType", "userId"];

/**
 * Type of access to be allowed for the user.
 * @member {module:model/UserAccessRight.AccessTypeEnum} accessType
 */
UserAccessRight.prototype['accessType'] = undefined;

/**
 * User ID (already existing in the device).
 * @member {String} userId
 */
UserAccessRight.prototype['userId'] = undefined;





/**
 * Allowed values for the <code>accessType</code> property.
 * @enum {String}
 * @readonly
 */
UserAccessRight['AccessTypeEnum'] = {

    /**
     * value: "Change"
     * @const
     */
    "Change": "Change",

    /**
     * value: "Read"
     * @const
     */
    "Read": "Read",

    /**
     * value: "Custom"
     * @const
     */
    "Custom": "Custom"
};



export default UserAccessRight;

