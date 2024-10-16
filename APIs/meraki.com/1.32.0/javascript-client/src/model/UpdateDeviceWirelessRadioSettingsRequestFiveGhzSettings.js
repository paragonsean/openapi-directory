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
 * The UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings model module.
 * @module model/UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings
 * @version 1.32.0
 */
class UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings {
    /**
     * Constructs a new <code>UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings</code>.
     * Manual radio settings for 5 GHz.
     * @alias module:model/UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings
     */
    constructor() { 
        
        UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings} obj Optional instance to populate.
     * @return {module:model/UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings} The populated <code>UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings();

            if (data.hasOwnProperty('channel')) {
                obj['channel'] = ApiClient.convertToType(data['channel'], 'Number');
            }
            if (data.hasOwnProperty('channelWidth')) {
                obj['channelWidth'] = ApiClient.convertToType(data['channelWidth'], 'Number');
            }
            if (data.hasOwnProperty('targetPower')) {
                obj['targetPower'] = ApiClient.convertToType(data['targetPower'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Sets a manual channel for 5 GHz. Can be '36', '40', '44', '48', '52', '56', '60', '64', '100', '104', '108', '112', '116', '120', '124', '128', '132', '136', '140', '144', '149', '153', '157', '161', '165', '169', '173' or '177' or null for using auto channel.
 * @member {module:model/UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings.ChannelEnum} channel
 */
UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings.prototype['channel'] = undefined;

/**
 * Sets a manual channel for 5 GHz. Can be '0', '20', '40', '80' or '160' or null for using auto channel width.
 * @member {module:model/UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings.ChannelWidthEnum} channelWidth
 */
UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings.prototype['channelWidth'] = undefined;

/**
 * Set a manual target power for 5 GHz. Can be between '8' or '30' or null for using auto power range.
 * @member {Number} targetPower
 */
UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings.prototype['targetPower'] = undefined;





/**
 * Allowed values for the <code>channel</code> property.
 * @enum {Number}
 * @readonly
 */
UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings['ChannelEnum'] = {

    /**
     * value: 36
     * @const
     */
    "36": 36,

    /**
     * value: 40
     * @const
     */
    "40": 40,

    /**
     * value: 44
     * @const
     */
    "44": 44,

    /**
     * value: 48
     * @const
     */
    "48": 48,

    /**
     * value: 52
     * @const
     */
    "52": 52,

    /**
     * value: 56
     * @const
     */
    "56": 56,

    /**
     * value: 60
     * @const
     */
    "60": 60,

    /**
     * value: 64
     * @const
     */
    "64": 64,

    /**
     * value: 100
     * @const
     */
    "100": 100,

    /**
     * value: 104
     * @const
     */
    "104": 104,

    /**
     * value: 108
     * @const
     */
    "108": 108,

    /**
     * value: 112
     * @const
     */
    "112": 112,

    /**
     * value: 116
     * @const
     */
    "116": 116,

    /**
     * value: 120
     * @const
     */
    "120": 120,

    /**
     * value: 124
     * @const
     */
    "124": 124,

    /**
     * value: 128
     * @const
     */
    "128": 128,

    /**
     * value: 132
     * @const
     */
    "132": 132,

    /**
     * value: 136
     * @const
     */
    "136": 136,

    /**
     * value: 140
     * @const
     */
    "140": 140,

    /**
     * value: 144
     * @const
     */
    "144": 144,

    /**
     * value: 149
     * @const
     */
    "149": 149,

    /**
     * value: 153
     * @const
     */
    "153": 153,

    /**
     * value: 157
     * @const
     */
    "157": 157,

    /**
     * value: 161
     * @const
     */
    "161": 161,

    /**
     * value: 165
     * @const
     */
    "165": 165,

    /**
     * value: 169
     * @const
     */
    "169": 169,

    /**
     * value: 173
     * @const
     */
    "173": 173,

    /**
     * value: 177
     * @const
     */
    "177": 177
};


/**
 * Allowed values for the <code>channelWidth</code> property.
 * @enum {Number}
 * @readonly
 */
UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings['ChannelWidthEnum'] = {

    /**
     * value: 0
     * @const
     */
    "0": 0,

    /**
     * value: 20
     * @const
     */
    "20": 20,

    /**
     * value: 40
     * @const
     */
    "40": 40,

    /**
     * value: 80
     * @const
     */
    "80": 80,

    /**
     * value: 160
     * @const
     */
    "160": 160
};



export default UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings;

