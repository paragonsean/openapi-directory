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
import UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage from './UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage';

/**
 * The UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo model module.
 * @module model/UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo
 * @version 1.32.0
 */
class UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo {
    /**
     * Constructs a new <code>UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo</code>.
     * The logo used in the splash page.
     * @alias module:model/UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo
     */
    constructor() { 
        
        UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo} The populated <code>UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo();

            if (data.hasOwnProperty('extension')) {
                obj['extension'] = ApiClient.convertToType(data['extension'], 'String');
            }
            if (data.hasOwnProperty('image')) {
                obj['image'] = UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage.constructFromObject(data['image']);
            }
            if (data.hasOwnProperty('md5')) {
                obj['md5'] = ApiClient.convertToType(data['md5'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['extension'] && !(typeof data['extension'] === 'string' || data['extension'] instanceof String)) {
            throw new Error("Expected the field `extension` to be a primitive type in the JSON string but got " + data['extension']);
        }
        // validate the optional field `image`
        if (data['image']) { // data not null
          UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage.validateJSON(data['image']);
        }
        // ensure the json data is a string
        if (data['md5'] && !(typeof data['md5'] === 'string' || data['md5'] instanceof String)) {
            throw new Error("Expected the field `md5` to be a primitive type in the JSON string but got " + data['md5']);
        }

        return true;
    }


}



/**
 * The extension of the logo file.
 * @member {String} extension
 */
UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo.prototype['extension'] = undefined;

/**
 * @member {module:model/UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogoImage} image
 */
UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo.prototype['image'] = undefined;

/**
 * The MD5 value of the logo file. Setting this to null will remove the logo from the splash page.
 * @member {String} md5
 */
UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo.prototype['md5'] = undefined;






export default UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo;

