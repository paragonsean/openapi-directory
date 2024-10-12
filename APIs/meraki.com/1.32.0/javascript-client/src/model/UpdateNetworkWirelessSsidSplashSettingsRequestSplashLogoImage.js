/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage model module.
 * @module model/UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage
 * @version 1.32.0
 */
class UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage {
    /**
     * Constructs a new <code>UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage</code>.
     * Properties for setting a new image.
     * @alias module:model/UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage
     */
    constructor() { 
        
        UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage} The populated <code>UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage();

            if (data.hasOwnProperty('contents')) {
                obj['contents'] = ApiClient.convertToType(data['contents'], 'Blob');
            }
            if (data.hasOwnProperty('format')) {
                obj['format'] = ApiClient.convertToType(data['format'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['format'] && !(typeof data['format'] === 'string' || data['format'] instanceof String)) {
            throw new Error("Expected the field `format` to be a primitive type in the JSON string but got " + data['format']);
        }

        return true;
    }


}



/**
 * The file contents (a base 64 encoded string) of your new logo.
 * @member {Blob} contents
 */
UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage.prototype['contents'] = undefined;

/**
 * The format of the encoded contents. Supported formats are 'png', 'gif', and jpg'.
 * @member {module:model/UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage.FormatEnum} format
 */
UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage.prototype['format'] = undefined;





/**
 * Allowed values for the <code>format</code> property.
 * @enum {String}
 * @readonly
 */
UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage['FormatEnum'] = {

    /**
     * value: "gif"
     * @const
     */
    "gif": "gif",

    /**
     * value: "jpg"
     * @const
     */
    "jpg": "jpg",

    /**
     * value: "png"
     * @const
     */
    "png": "png"
};



export default UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage;

