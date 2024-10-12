/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2016-11-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The TrustedIdProviderProperties model module.
 * @module model/TrustedIdProviderProperties
 * @version 2016-11-01
 */
class TrustedIdProviderProperties {
    /**
     * Constructs a new <code>TrustedIdProviderProperties</code>.
     * The trusted identity provider properties.
     * @alias module:model/TrustedIdProviderProperties
     */
    constructor() { 
        
        TrustedIdProviderProperties.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TrustedIdProviderProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TrustedIdProviderProperties} obj Optional instance to populate.
     * @return {module:model/TrustedIdProviderProperties} The populated <code>TrustedIdProviderProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TrustedIdProviderProperties();

            if (data.hasOwnProperty('idProvider')) {
                obj['idProvider'] = ApiClient.convertToType(data['idProvider'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TrustedIdProviderProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TrustedIdProviderProperties</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['idProvider'] && !(typeof data['idProvider'] === 'string' || data['idProvider'] instanceof String)) {
            throw new Error("Expected the field `idProvider` to be a primitive type in the JSON string but got " + data['idProvider']);
        }

        return true;
    }


}



/**
 * The URL of this trusted identity provider.
 * @member {String} idProvider
 */
TrustedIdProviderProperties.prototype['idProvider'] = undefined;






export default TrustedIdProviderProperties;

