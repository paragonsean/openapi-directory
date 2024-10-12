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
import AsymmetricEncryptedSecret from './AsymmetricEncryptedSecret';

/**
 * The SecuritySettingsProperties model module.
 * @module model/SecuritySettingsProperties
 * @version 2019-03-01
 */
class SecuritySettingsProperties {
    /**
     * Constructs a new <code>SecuritySettingsProperties</code>.
     * The properties of security settings.
     * @alias module:model/SecuritySettingsProperties
     * @param deviceAdminPassword {module:model/AsymmetricEncryptedSecret} 
     */
    constructor(deviceAdminPassword) { 
        
        SecuritySettingsProperties.initialize(this, deviceAdminPassword);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, deviceAdminPassword) { 
        obj['deviceAdminPassword'] = deviceAdminPassword;
    }

    /**
     * Constructs a <code>SecuritySettingsProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SecuritySettingsProperties} obj Optional instance to populate.
     * @return {module:model/SecuritySettingsProperties} The populated <code>SecuritySettingsProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SecuritySettingsProperties();

            if (data.hasOwnProperty('deviceAdminPassword')) {
                obj['deviceAdminPassword'] = AsymmetricEncryptedSecret.constructFromObject(data['deviceAdminPassword']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SecuritySettingsProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SecuritySettingsProperties</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SecuritySettingsProperties.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `deviceAdminPassword`
        if (data['deviceAdminPassword']) { // data not null
          AsymmetricEncryptedSecret.validateJSON(data['deviceAdminPassword']);
        }

        return true;
    }


}

SecuritySettingsProperties.RequiredProperties = ["deviceAdminPassword"];

/**
 * @member {module:model/AsymmetricEncryptedSecret} deviceAdminPassword
 */
SecuritySettingsProperties.prototype['deviceAdminPassword'] = undefined;






export default SecuritySettingsProperties;

