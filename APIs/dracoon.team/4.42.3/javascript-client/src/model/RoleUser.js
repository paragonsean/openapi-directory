/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import UserInfo from './UserInfo';

/**
 * The RoleUser model module.
 * @module model/RoleUser
 * @version 4.42.3
 */
class RoleUser {
    /**
     * Constructs a new <code>RoleUser</code>.
     * User information
     * @alias module:model/RoleUser
     * @param displayName {String} &#128679; Deprecated since v4.11.0  Display name  use information from `UserInfo` instead to combine a display name
     * @param id {Number} &#128679; Deprecated since v4.11.0  Unique identifier for the user  use `id` from `UserInfo` instead
     * @param isMember {Boolean} Is user member of the role
     * @param userInfo {module:model/UserInfo} 
     */
    constructor(displayName, id, isMember, userInfo) { 
        
        RoleUser.initialize(this, displayName, id, isMember, userInfo);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, displayName, id, isMember, userInfo) { 
        obj['displayName'] = displayName;
        obj['id'] = id;
        obj['isMember'] = isMember;
        obj['userInfo'] = userInfo;
    }

    /**
     * Constructs a <code>RoleUser</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RoleUser} obj Optional instance to populate.
     * @return {module:model/RoleUser} The populated <code>RoleUser</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RoleUser();

            if (data.hasOwnProperty('displayName')) {
                obj['displayName'] = ApiClient.convertToType(data['displayName'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('isMember')) {
                obj['isMember'] = ApiClient.convertToType(data['isMember'], 'Boolean');
            }
            if (data.hasOwnProperty('userInfo')) {
                obj['userInfo'] = UserInfo.constructFromObject(data['userInfo']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RoleUser</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RoleUser</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RoleUser.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['displayName'] && !(typeof data['displayName'] === 'string' || data['displayName'] instanceof String)) {
            throw new Error("Expected the field `displayName` to be a primitive type in the JSON string but got " + data['displayName']);
        }
        // validate the optional field `userInfo`
        if (data['userInfo']) { // data not null
          UserInfo.validateJSON(data['userInfo']);
        }

        return true;
    }


}

RoleUser.RequiredProperties = ["displayName", "id", "isMember", "userInfo"];

/**
 * &#128679; Deprecated since v4.11.0  Display name  use information from `UserInfo` instead to combine a display name
 * @member {String} displayName
 */
RoleUser.prototype['displayName'] = undefined;

/**
 * &#128679; Deprecated since v4.11.0  Unique identifier for the user  use `id` from `UserInfo` instead
 * @member {Number} id
 */
RoleUser.prototype['id'] = undefined;

/**
 * Is user member of the role
 * @member {Boolean} isMember
 */
RoleUser.prototype['isMember'] = undefined;

/**
 * @member {module:model/UserInfo} userInfo
 */
RoleUser.prototype['userInfo'] = undefined;






export default RoleUser;

