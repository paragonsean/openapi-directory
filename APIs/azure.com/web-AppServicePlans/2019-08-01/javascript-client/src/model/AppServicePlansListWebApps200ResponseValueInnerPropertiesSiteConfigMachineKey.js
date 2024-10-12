/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey model module.
 * @module model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey
 * @version 2019-08-01
 */
class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey {
    /**
     * Constructs a new <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey</code>.
     * MachineKey of an app.
     * @alias module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey
     */
    constructor() { 
        
        AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey} The populated <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey();

            if (data.hasOwnProperty('decryption')) {
                obj['decryption'] = ApiClient.convertToType(data['decryption'], 'String');
            }
            if (data.hasOwnProperty('decryptionKey')) {
                obj['decryptionKey'] = ApiClient.convertToType(data['decryptionKey'], 'String');
            }
            if (data.hasOwnProperty('validation')) {
                obj['validation'] = ApiClient.convertToType(data['validation'], 'String');
            }
            if (data.hasOwnProperty('validationKey')) {
                obj['validationKey'] = ApiClient.convertToType(data['validationKey'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['decryption'] && !(typeof data['decryption'] === 'string' || data['decryption'] instanceof String)) {
            throw new Error("Expected the field `decryption` to be a primitive type in the JSON string but got " + data['decryption']);
        }
        // ensure the json data is a string
        if (data['decryptionKey'] && !(typeof data['decryptionKey'] === 'string' || data['decryptionKey'] instanceof String)) {
            throw new Error("Expected the field `decryptionKey` to be a primitive type in the JSON string but got " + data['decryptionKey']);
        }
        // ensure the json data is a string
        if (data['validation'] && !(typeof data['validation'] === 'string' || data['validation'] instanceof String)) {
            throw new Error("Expected the field `validation` to be a primitive type in the JSON string but got " + data['validation']);
        }
        // ensure the json data is a string
        if (data['validationKey'] && !(typeof data['validationKey'] === 'string' || data['validationKey'] instanceof String)) {
            throw new Error("Expected the field `validationKey` to be a primitive type in the JSON string but got " + data['validationKey']);
        }

        return true;
    }


}



/**
 * Algorithm used for decryption.
 * @member {String} decryption
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey.prototype['decryption'] = undefined;

/**
 * Decryption key.
 * @member {String} decryptionKey
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey.prototype['decryptionKey'] = undefined;

/**
 * MachineKey validation.
 * @member {String} validation
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey.prototype['validation'] = undefined;

/**
 * Validation key.
 * @member {String} validationKey
 */
AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey.prototype['validationKey'] = undefined;






export default AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey;

