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
 * The DealerDBModelsLicenseActivationCreate model module.
 * @module model/DealerDBModelsLicenseActivationCreate
 * @version v1
 */
class DealerDBModelsLicenseActivationCreate {
    /**
     * Constructs a new <code>DealerDBModelsLicenseActivationCreate</code>.
     * @alias module:model/DealerDBModelsLicenseActivationCreate
     * @param dealerCode {String} The Dealer Code of the dealer activating the license
     * @param postalCode {String} The dealer's postal code (zip code)
     * @param systemInfo {String} Information about  the system being activated
     * @param voucherCode {String} The Voucher Code to use for activation
     */
    constructor(dealerCode, postalCode, systemInfo, voucherCode) { 
        
        DealerDBModelsLicenseActivationCreate.initialize(this, dealerCode, postalCode, systemInfo, voucherCode);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, dealerCode, postalCode, systemInfo, voucherCode) { 
        obj['DealerCode'] = dealerCode;
        obj['PostalCode'] = postalCode;
        obj['SystemInfo'] = systemInfo;
        obj['VoucherCode'] = voucherCode;
    }

    /**
     * Constructs a <code>DealerDBModelsLicenseActivationCreate</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DealerDBModelsLicenseActivationCreate} obj Optional instance to populate.
     * @return {module:model/DealerDBModelsLicenseActivationCreate} The populated <code>DealerDBModelsLicenseActivationCreate</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DealerDBModelsLicenseActivationCreate();

            if (data.hasOwnProperty('DealerCode')) {
                obj['DealerCode'] = ApiClient.convertToType(data['DealerCode'], 'String');
            }
            if (data.hasOwnProperty('LicenseActivationType')) {
                obj['LicenseActivationType'] = ApiClient.convertToType(data['LicenseActivationType'], 'String');
            }
            if (data.hasOwnProperty('PostalCode')) {
                obj['PostalCode'] = ApiClient.convertToType(data['PostalCode'], 'String');
            }
            if (data.hasOwnProperty('SystemInfo')) {
                obj['SystemInfo'] = ApiClient.convertToType(data['SystemInfo'], 'String');
            }
            if (data.hasOwnProperty('VoucherCode')) {
                obj['VoucherCode'] = ApiClient.convertToType(data['VoucherCode'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DealerDBModelsLicenseActivationCreate</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DealerDBModelsLicenseActivationCreate</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DealerDBModelsLicenseActivationCreate.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['DealerCode'] && !(typeof data['DealerCode'] === 'string' || data['DealerCode'] instanceof String)) {
            throw new Error("Expected the field `DealerCode` to be a primitive type in the JSON string but got " + data['DealerCode']);
        }
        // ensure the json data is a string
        if (data['LicenseActivationType'] && !(typeof data['LicenseActivationType'] === 'string' || data['LicenseActivationType'] instanceof String)) {
            throw new Error("Expected the field `LicenseActivationType` to be a primitive type in the JSON string but got " + data['LicenseActivationType']);
        }
        // ensure the json data is a string
        if (data['PostalCode'] && !(typeof data['PostalCode'] === 'string' || data['PostalCode'] instanceof String)) {
            throw new Error("Expected the field `PostalCode` to be a primitive type in the JSON string but got " + data['PostalCode']);
        }
        // ensure the json data is a string
        if (data['SystemInfo'] && !(typeof data['SystemInfo'] === 'string' || data['SystemInfo'] instanceof String)) {
            throw new Error("Expected the field `SystemInfo` to be a primitive type in the JSON string but got " + data['SystemInfo']);
        }
        // ensure the json data is a string
        if (data['VoucherCode'] && !(typeof data['VoucherCode'] === 'string' || data['VoucherCode'] instanceof String)) {
            throw new Error("Expected the field `VoucherCode` to be a primitive type in the JSON string but got " + data['VoucherCode']);
        }

        return true;
    }


}

DealerDBModelsLicenseActivationCreate.RequiredProperties = ["DealerCode", "PostalCode", "SystemInfo", "VoucherCode"];

/**
 * The Dealer Code of the dealer activating the license
 * @member {String} DealerCode
 */
DealerDBModelsLicenseActivationCreate.prototype['DealerCode'] = undefined;

/**
 * The type of license to create (e.g. EDT, EDT Lite)
 * @member {module:model/DealerDBModelsLicenseActivationCreate.LicenseActivationTypeEnum} LicenseActivationType
 */
DealerDBModelsLicenseActivationCreate.prototype['LicenseActivationType'] = undefined;

/**
 * The dealer's postal code (zip code)
 * @member {String} PostalCode
 */
DealerDBModelsLicenseActivationCreate.prototype['PostalCode'] = undefined;

/**
 * Information about  the system being activated
 * @member {String} SystemInfo
 */
DealerDBModelsLicenseActivationCreate.prototype['SystemInfo'] = undefined;

/**
 * The Voucher Code to use for activation
 * @member {String} VoucherCode
 */
DealerDBModelsLicenseActivationCreate.prototype['VoucherCode'] = undefined;





/**
 * Allowed values for the <code>LicenseActivationType</code> property.
 * @enum {String}
 * @readonly
 */
DealerDBModelsLicenseActivationCreate['LicenseActivationTypeEnum'] = {

    /**
     * value: "EDT"
     * @const
     */
    "EDT": "EDT",

    /**
     * value: "EDTLite"
     * @const
     */
    "EDTLite": "EDTLite"
};



export default DealerDBModelsLicenseActivationCreate;

