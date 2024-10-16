/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The DealerDBModelsLicenseActivationUpdate model module.
 * @module model/DealerDBModelsLicenseActivationUpdate
 * @version v1
 */
class DealerDBModelsLicenseActivationUpdate {
    /**
     * Constructs a new <code>DealerDBModelsLicenseActivationUpdate</code>.
     * @alias module:model/DealerDBModelsLicenseActivationUpdate
     * @param licenseVersion {String} The license version to update
     */
    constructor(licenseVersion) { 
        
        DealerDBModelsLicenseActivationUpdate.initialize(this, licenseVersion);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, licenseVersion) { 
        obj['LicenseVersion'] = licenseVersion;
    }

    /**
     * Constructs a <code>DealerDBModelsLicenseActivationUpdate</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DealerDBModelsLicenseActivationUpdate} obj Optional instance to populate.
     * @return {module:model/DealerDBModelsLicenseActivationUpdate} The populated <code>DealerDBModelsLicenseActivationUpdate</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DealerDBModelsLicenseActivationUpdate();

            if (data.hasOwnProperty('LicenseVersion')) {
                obj['LicenseVersion'] = ApiClient.convertToType(data['LicenseVersion'], 'String');
            }
            if (data.hasOwnProperty('SystemInfo')) {
                obj['SystemInfo'] = ApiClient.convertToType(data['SystemInfo'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DealerDBModelsLicenseActivationUpdate</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DealerDBModelsLicenseActivationUpdate</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DealerDBModelsLicenseActivationUpdate.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['LicenseVersion'] && !(typeof data['LicenseVersion'] === 'string' || data['LicenseVersion'] instanceof String)) {
            throw new Error("Expected the field `LicenseVersion` to be a primitive type in the JSON string but got " + data['LicenseVersion']);
        }
        // ensure the json data is a string
        if (data['SystemInfo'] && !(typeof data['SystemInfo'] === 'string' || data['SystemInfo'] instanceof String)) {
            throw new Error("Expected the field `SystemInfo` to be a primitive type in the JSON string but got " + data['SystemInfo']);
        }

        return true;
    }


}

DealerDBModelsLicenseActivationUpdate.RequiredProperties = ["LicenseVersion"];

/**
 * The license version to update
 * @member {String} LicenseVersion
 */
DealerDBModelsLicenseActivationUpdate.prototype['LicenseVersion'] = undefined;

/**
 * Information about  the system being activated
 * @member {String} SystemInfo
 */
DealerDBModelsLicenseActivationUpdate.prototype['SystemInfo'] = undefined;






export default DealerDBModelsLicenseActivationUpdate;

