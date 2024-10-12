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
 * The AccountUpdate model module.
 * @module model/AccountUpdate
 * @version 2.0.0
 */
class AccountUpdate {
    /**
     * Constructs a new <code>AccountUpdate</code>.
     * @alias module:model/AccountUpdate
     * @param groupId {Number} Not applicable to regular users. This field is reserved to institutions/publishers with access to assign to specific groups
     * @param isActive {Boolean} Is account active
     */
    constructor(groupId, isActive) { 
        
        AccountUpdate.initialize(this, groupId, isActive);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, groupId, isActive) { 
        obj['group_id'] = groupId;
        obj['is_active'] = isActive;
    }

    /**
     * Constructs a <code>AccountUpdate</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccountUpdate} obj Optional instance to populate.
     * @return {module:model/AccountUpdate} The populated <code>AccountUpdate</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccountUpdate();

            if (data.hasOwnProperty('group_id')) {
                obj['group_id'] = ApiClient.convertToType(data['group_id'], 'Number');
            }
            if (data.hasOwnProperty('is_active')) {
                obj['is_active'] = ApiClient.convertToType(data['is_active'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccountUpdate</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccountUpdate</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AccountUpdate.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

AccountUpdate.RequiredProperties = ["group_id", "is_active"];

/**
 * Not applicable to regular users. This field is reserved to institutions/publishers with access to assign to specific groups
 * @member {Number} group_id
 */
AccountUpdate.prototype['group_id'] = undefined;

/**
 * Is account active
 * @member {Boolean} is_active
 */
AccountUpdate.prototype['is_active'] = undefined;






export default AccountUpdate;

