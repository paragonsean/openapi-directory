/**
 * Google Home
 * # Google Home Local API This is an unofficial documentation of the local API used by the Home app to communicate with GH devices. [GitHub Repo](https://github.com/rithvikvibhu/GHLocalApi)  [![GitHub stars](https://img.shields.io/github/stars/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/stargazers) [![GitHub license](https://img.shields.io/github/license/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/blob/master/LICENSE.md)  ## Getting Started  Requests must be made over HTTPS, port 8443, so the base URL for these endpoints is: `https://<google-home-ip>:8443/setup/`  Get the IP of Google Home from the Google Home app (Device Settings -> End of the list) or from your router.  GET requests are simple, in the browser kind.   POST requests need to set the header (when there's a body): `content-type: application/json`  ## Authentication  Since June 2019, most requests (with exceptions like `/setup/eureka_info`) need a local authorization token.  There are 3 kinds of tokens involved here:  ### Local Authorization Token This token must be sent in all requests in the header `cast-local-authorization-token`. It is short-lived (~1 day) and may change unexpectedly (with a sync, change in homegraph, etc.) ##### Get this token - With access to an android device, [get this token directly by either method](https://gist.github.com/rithvikvibhu/1a0f4937af957ef6a78453e3be482c1f). - Without a device, or to integrate it with a script, use an access token to get the homegraph and extract the token. To get an access token, read the next section. Check the example section for more info.  ### Access Token This is a standard google oauth2 access token. It is in the form `ya29.***`. This gives access to the Google Home Foyer API. These expire in an hour. Use this to get the homegraph (and then the local authorization token above). ##### Get this token To get this access token, either a Google account username/password or a Google Master Token is needed. More info in the gist. Use the script [from this gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d).  ### Master Token This is in the form `aas_et/_***` and can be used to request access tokens. ##### Get this token The same [script in the gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d) that gets the access token can also get the master token. Needs Google account creds.  ## Example  Here's the whole flow from just a pair of username/password to using the local API.  Prerequisites: - [grpcurl](https://github.com/fullstorydev/grpcurl) - [Proto files](https://drive.google.com/drive/folders/1RvnN3y-G23pd2SWHmfV_7sef8QU5GNF4?usp=sharing) (preserve folder structure)  ### 1. Get an access token with the script - Download get_tokens.py - Fill in username and password ```sh python3 get_tokens.py # Note down the access token printed. ```  ### 2. Use the access token and get home graph - This prints the json and uses jq to parse and filter out the fields deviceName and localAuthToken - This will give a list of all devices and their local auth tokens ```sh ./grpcurl -H 'authorization: Bearer ya29.a0Af****' \\  -import-path /path/to/protos \\  -proto /path/to/protos/google/internal/home/foyer/v1.proto \\  googlehomefoyer-pa.googleapis.com:443 \\  google.internal.home.foyer.v1.StructuresService/GetHomeGraph | jq '.home.devices[] | {deviceName, localAuthToken}' # Note down the local auth token for the device you want. ```  ### 3. Make the call to the local device using the local auth token ```sh curl -H \"cast-local-authorization-token: LOCAL_AUTH_TOKEN\" --verbose --insecure https://192.168.0.18:8443/setup/bluetooth/status ```
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Capabilities model module.
 * @module model/Capabilities
 * @version 2.0
 */
class Capabilities {
    /**
     * Constructs a new <code>Capabilities</code>.
     * @alias module:model/Capabilities
     * @param aoghSupported {Boolean} 
     * @param assistantSupported {Boolean} 
     * @param audioHdrSupported {Boolean} 
     * @param audioSurroundModeSupported {Boolean} 
     * @param bleSupported {Boolean} 
     * @param bluetoothAudioSinkSupported {Boolean} 
     * @param bluetoothAudioSourceSupported {Boolean} 
     * @param bluetoothSupported {Boolean} 
     * @param cloudcastSupported {Boolean} 
     * @param contentFiltersSupported {Boolean} 
     * @param displaySupported {Boolean} 
     * @param fdrSupported {Boolean} 
     * @param hdmiPrefer50hzSupported {Boolean} 
     * @param hdmiPreferHighFpsSupported {Boolean} 
     * @param hotspotSupported {Boolean} 
     * @param httpsSetupSupported {Boolean} 
     * @param inputManagementSupported {Boolean} 
     * @param keepHotspotUntilConnectedSupported {Boolean} 
     * @param multiUserSupported {Boolean} 
     * @param multichannelGroupSupported {Boolean} 
     * @param multizoneSupported {Boolean} 
     * @param nightModeSupported {Boolean} 
     * @param nightModeSupportedV2 {Boolean} 
     * @param opencastSupported {Boolean} 
     * @param previewChannelSupported {Boolean} 
     * @param rebootSupported {Boolean} 
     * @param remoteDuckingSupported {Boolean} 
     * @param separateTtsVolumeSupported {Boolean} 
     * @param setupSupported {Boolean} 
     * @param sleepModeSupported {Boolean} 
     * @param statsSupported {Boolean} 
     * @param systemSoundEffectsSupported {Boolean} 
     * @param userEqSupported {Boolean} 
     * @param wifiAutoSaveSupported {Boolean} 
     * @param wifiRegulatoryDomainLocked {Boolean} 
     * @param wifiSupported {Boolean} 
     */
    constructor(aoghSupported, assistantSupported, audioHdrSupported, audioSurroundModeSupported, bleSupported, bluetoothAudioSinkSupported, bluetoothAudioSourceSupported, bluetoothSupported, cloudcastSupported, contentFiltersSupported, displaySupported, fdrSupported, hdmiPrefer50hzSupported, hdmiPreferHighFpsSupported, hotspotSupported, httpsSetupSupported, inputManagementSupported, keepHotspotUntilConnectedSupported, multiUserSupported, multichannelGroupSupported, multizoneSupported, nightModeSupported, nightModeSupportedV2, opencastSupported, previewChannelSupported, rebootSupported, remoteDuckingSupported, separateTtsVolumeSupported, setupSupported, sleepModeSupported, statsSupported, systemSoundEffectsSupported, userEqSupported, wifiAutoSaveSupported, wifiRegulatoryDomainLocked, wifiSupported) { 
        
        Capabilities.initialize(this, aoghSupported, assistantSupported, audioHdrSupported, audioSurroundModeSupported, bleSupported, bluetoothAudioSinkSupported, bluetoothAudioSourceSupported, bluetoothSupported, cloudcastSupported, contentFiltersSupported, displaySupported, fdrSupported, hdmiPrefer50hzSupported, hdmiPreferHighFpsSupported, hotspotSupported, httpsSetupSupported, inputManagementSupported, keepHotspotUntilConnectedSupported, multiUserSupported, multichannelGroupSupported, multizoneSupported, nightModeSupported, nightModeSupportedV2, opencastSupported, previewChannelSupported, rebootSupported, remoteDuckingSupported, separateTtsVolumeSupported, setupSupported, sleepModeSupported, statsSupported, systemSoundEffectsSupported, userEqSupported, wifiAutoSaveSupported, wifiRegulatoryDomainLocked, wifiSupported);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, aoghSupported, assistantSupported, audioHdrSupported, audioSurroundModeSupported, bleSupported, bluetoothAudioSinkSupported, bluetoothAudioSourceSupported, bluetoothSupported, cloudcastSupported, contentFiltersSupported, displaySupported, fdrSupported, hdmiPrefer50hzSupported, hdmiPreferHighFpsSupported, hotspotSupported, httpsSetupSupported, inputManagementSupported, keepHotspotUntilConnectedSupported, multiUserSupported, multichannelGroupSupported, multizoneSupported, nightModeSupported, nightModeSupportedV2, opencastSupported, previewChannelSupported, rebootSupported, remoteDuckingSupported, separateTtsVolumeSupported, setupSupported, sleepModeSupported, statsSupported, systemSoundEffectsSupported, userEqSupported, wifiAutoSaveSupported, wifiRegulatoryDomainLocked, wifiSupported) { 
        obj['aogh_supported'] = aoghSupported;
        obj['assistant_supported'] = assistantSupported;
        obj['audio_hdr_supported'] = audioHdrSupported;
        obj['audio_surround_mode_supported'] = audioSurroundModeSupported;
        obj['ble_supported'] = bleSupported;
        obj['bluetooth_audio_sink_supported'] = bluetoothAudioSinkSupported;
        obj['bluetooth_audio_source_supported'] = bluetoothAudioSourceSupported;
        obj['bluetooth_supported'] = bluetoothSupported;
        obj['cloudcast_supported'] = cloudcastSupported;
        obj['content_filters_supported'] = contentFiltersSupported;
        obj['display_supported'] = displaySupported;
        obj['fdr_supported'] = fdrSupported;
        obj['hdmi_prefer_50hz_supported'] = hdmiPrefer50hzSupported;
        obj['hdmi_prefer_high_fps_supported'] = hdmiPreferHighFpsSupported;
        obj['hotspot_supported'] = hotspotSupported;
        obj['https_setup_supported'] = httpsSetupSupported;
        obj['input_management_supported'] = inputManagementSupported;
        obj['keep_hotspot_until_connected_supported'] = keepHotspotUntilConnectedSupported;
        obj['multi_user_supported'] = multiUserSupported;
        obj['multichannel_group_supported'] = multichannelGroupSupported;
        obj['multizone_supported'] = multizoneSupported;
        obj['night_mode_supported'] = nightModeSupported;
        obj['night_mode_supported_v2'] = nightModeSupportedV2;
        obj['opencast_supported'] = opencastSupported;
        obj['preview_channel_supported'] = previewChannelSupported;
        obj['reboot_supported'] = rebootSupported;
        obj['remote_ducking_supported'] = remoteDuckingSupported;
        obj['separate_tts_volume_supported'] = separateTtsVolumeSupported;
        obj['setup_supported'] = setupSupported;
        obj['sleep_mode_supported'] = sleepModeSupported;
        obj['stats_supported'] = statsSupported;
        obj['system_sound_effects_supported'] = systemSoundEffectsSupported;
        obj['user_eq_supported'] = userEqSupported;
        obj['wifi_auto_save_supported'] = wifiAutoSaveSupported;
        obj['wifi_regulatory_domain_locked'] = wifiRegulatoryDomainLocked;
        obj['wifi_supported'] = wifiSupported;
    }

    /**
     * Constructs a <code>Capabilities</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Capabilities} obj Optional instance to populate.
     * @return {module:model/Capabilities} The populated <code>Capabilities</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Capabilities();

            if (data.hasOwnProperty('aogh_supported')) {
                obj['aogh_supported'] = ApiClient.convertToType(data['aogh_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('assistant_supported')) {
                obj['assistant_supported'] = ApiClient.convertToType(data['assistant_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('audio_hdr_supported')) {
                obj['audio_hdr_supported'] = ApiClient.convertToType(data['audio_hdr_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('audio_surround_mode_supported')) {
                obj['audio_surround_mode_supported'] = ApiClient.convertToType(data['audio_surround_mode_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('ble_supported')) {
                obj['ble_supported'] = ApiClient.convertToType(data['ble_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('bluetooth_audio_sink_supported')) {
                obj['bluetooth_audio_sink_supported'] = ApiClient.convertToType(data['bluetooth_audio_sink_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('bluetooth_audio_source_supported')) {
                obj['bluetooth_audio_source_supported'] = ApiClient.convertToType(data['bluetooth_audio_source_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('bluetooth_supported')) {
                obj['bluetooth_supported'] = ApiClient.convertToType(data['bluetooth_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('cloudcast_supported')) {
                obj['cloudcast_supported'] = ApiClient.convertToType(data['cloudcast_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('content_filters_supported')) {
                obj['content_filters_supported'] = ApiClient.convertToType(data['content_filters_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('display_supported')) {
                obj['display_supported'] = ApiClient.convertToType(data['display_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('fdr_supported')) {
                obj['fdr_supported'] = ApiClient.convertToType(data['fdr_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('hdmi_prefer_50hz_supported')) {
                obj['hdmi_prefer_50hz_supported'] = ApiClient.convertToType(data['hdmi_prefer_50hz_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('hdmi_prefer_high_fps_supported')) {
                obj['hdmi_prefer_high_fps_supported'] = ApiClient.convertToType(data['hdmi_prefer_high_fps_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('hotspot_supported')) {
                obj['hotspot_supported'] = ApiClient.convertToType(data['hotspot_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('https_setup_supported')) {
                obj['https_setup_supported'] = ApiClient.convertToType(data['https_setup_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('input_management_supported')) {
                obj['input_management_supported'] = ApiClient.convertToType(data['input_management_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('keep_hotspot_until_connected_supported')) {
                obj['keep_hotspot_until_connected_supported'] = ApiClient.convertToType(data['keep_hotspot_until_connected_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('multi_user_supported')) {
                obj['multi_user_supported'] = ApiClient.convertToType(data['multi_user_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('multichannel_group_supported')) {
                obj['multichannel_group_supported'] = ApiClient.convertToType(data['multichannel_group_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('multizone_supported')) {
                obj['multizone_supported'] = ApiClient.convertToType(data['multizone_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('night_mode_supported')) {
                obj['night_mode_supported'] = ApiClient.convertToType(data['night_mode_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('night_mode_supported_v2')) {
                obj['night_mode_supported_v2'] = ApiClient.convertToType(data['night_mode_supported_v2'], 'Boolean');
            }
            if (data.hasOwnProperty('opencast_supported')) {
                obj['opencast_supported'] = ApiClient.convertToType(data['opencast_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('preview_channel_supported')) {
                obj['preview_channel_supported'] = ApiClient.convertToType(data['preview_channel_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('reboot_supported')) {
                obj['reboot_supported'] = ApiClient.convertToType(data['reboot_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('remote_ducking_supported')) {
                obj['remote_ducking_supported'] = ApiClient.convertToType(data['remote_ducking_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('separate_tts_volume_supported')) {
                obj['separate_tts_volume_supported'] = ApiClient.convertToType(data['separate_tts_volume_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('setup_supported')) {
                obj['setup_supported'] = ApiClient.convertToType(data['setup_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('sleep_mode_supported')) {
                obj['sleep_mode_supported'] = ApiClient.convertToType(data['sleep_mode_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('stats_supported')) {
                obj['stats_supported'] = ApiClient.convertToType(data['stats_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('system_sound_effects_supported')) {
                obj['system_sound_effects_supported'] = ApiClient.convertToType(data['system_sound_effects_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('user_eq_supported')) {
                obj['user_eq_supported'] = ApiClient.convertToType(data['user_eq_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('wifi_auto_save_supported')) {
                obj['wifi_auto_save_supported'] = ApiClient.convertToType(data['wifi_auto_save_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('wifi_regulatory_domain_locked')) {
                obj['wifi_regulatory_domain_locked'] = ApiClient.convertToType(data['wifi_regulatory_domain_locked'], 'Boolean');
            }
            if (data.hasOwnProperty('wifi_supported')) {
                obj['wifi_supported'] = ApiClient.convertToType(data['wifi_supported'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Capabilities</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Capabilities</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Capabilities.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

Capabilities.RequiredProperties = ["aogh_supported", "assistant_supported", "audio_hdr_supported", "audio_surround_mode_supported", "ble_supported", "bluetooth_audio_sink_supported", "bluetooth_audio_source_supported", "bluetooth_supported", "cloudcast_supported", "content_filters_supported", "display_supported", "fdr_supported", "hdmi_prefer_50hz_supported", "hdmi_prefer_high_fps_supported", "hotspot_supported", "https_setup_supported", "input_management_supported", "keep_hotspot_until_connected_supported", "multi_user_supported", "multichannel_group_supported", "multizone_supported", "night_mode_supported", "night_mode_supported_v2", "opencast_supported", "preview_channel_supported", "reboot_supported", "remote_ducking_supported", "separate_tts_volume_supported", "setup_supported", "sleep_mode_supported", "stats_supported", "system_sound_effects_supported", "user_eq_supported", "wifi_auto_save_supported", "wifi_regulatory_domain_locked", "wifi_supported"];

/**
 * @member {Boolean} aogh_supported
 */
Capabilities.prototype['aogh_supported'] = undefined;

/**
 * @member {Boolean} assistant_supported
 */
Capabilities.prototype['assistant_supported'] = undefined;

/**
 * @member {Boolean} audio_hdr_supported
 */
Capabilities.prototype['audio_hdr_supported'] = undefined;

/**
 * @member {Boolean} audio_surround_mode_supported
 */
Capabilities.prototype['audio_surround_mode_supported'] = undefined;

/**
 * @member {Boolean} ble_supported
 */
Capabilities.prototype['ble_supported'] = undefined;

/**
 * @member {Boolean} bluetooth_audio_sink_supported
 */
Capabilities.prototype['bluetooth_audio_sink_supported'] = undefined;

/**
 * @member {Boolean} bluetooth_audio_source_supported
 */
Capabilities.prototype['bluetooth_audio_source_supported'] = undefined;

/**
 * @member {Boolean} bluetooth_supported
 */
Capabilities.prototype['bluetooth_supported'] = undefined;

/**
 * @member {Boolean} cloudcast_supported
 */
Capabilities.prototype['cloudcast_supported'] = undefined;

/**
 * @member {Boolean} content_filters_supported
 */
Capabilities.prototype['content_filters_supported'] = undefined;

/**
 * @member {Boolean} display_supported
 */
Capabilities.prototype['display_supported'] = undefined;

/**
 * @member {Boolean} fdr_supported
 */
Capabilities.prototype['fdr_supported'] = undefined;

/**
 * @member {Boolean} hdmi_prefer_50hz_supported
 */
Capabilities.prototype['hdmi_prefer_50hz_supported'] = undefined;

/**
 * @member {Boolean} hdmi_prefer_high_fps_supported
 */
Capabilities.prototype['hdmi_prefer_high_fps_supported'] = undefined;

/**
 * @member {Boolean} hotspot_supported
 */
Capabilities.prototype['hotspot_supported'] = undefined;

/**
 * @member {Boolean} https_setup_supported
 */
Capabilities.prototype['https_setup_supported'] = undefined;

/**
 * @member {Boolean} input_management_supported
 */
Capabilities.prototype['input_management_supported'] = undefined;

/**
 * @member {Boolean} keep_hotspot_until_connected_supported
 */
Capabilities.prototype['keep_hotspot_until_connected_supported'] = undefined;

/**
 * @member {Boolean} multi_user_supported
 */
Capabilities.prototype['multi_user_supported'] = undefined;

/**
 * @member {Boolean} multichannel_group_supported
 */
Capabilities.prototype['multichannel_group_supported'] = undefined;

/**
 * @member {Boolean} multizone_supported
 */
Capabilities.prototype['multizone_supported'] = undefined;

/**
 * @member {Boolean} night_mode_supported
 */
Capabilities.prototype['night_mode_supported'] = undefined;

/**
 * @member {Boolean} night_mode_supported_v2
 */
Capabilities.prototype['night_mode_supported_v2'] = undefined;

/**
 * @member {Boolean} opencast_supported
 */
Capabilities.prototype['opencast_supported'] = undefined;

/**
 * @member {Boolean} preview_channel_supported
 */
Capabilities.prototype['preview_channel_supported'] = undefined;

/**
 * @member {Boolean} reboot_supported
 */
Capabilities.prototype['reboot_supported'] = undefined;

/**
 * @member {Boolean} remote_ducking_supported
 */
Capabilities.prototype['remote_ducking_supported'] = undefined;

/**
 * @member {Boolean} separate_tts_volume_supported
 */
Capabilities.prototype['separate_tts_volume_supported'] = undefined;

/**
 * @member {Boolean} setup_supported
 */
Capabilities.prototype['setup_supported'] = undefined;

/**
 * @member {Boolean} sleep_mode_supported
 */
Capabilities.prototype['sleep_mode_supported'] = undefined;

/**
 * @member {Boolean} stats_supported
 */
Capabilities.prototype['stats_supported'] = undefined;

/**
 * @member {Boolean} system_sound_effects_supported
 */
Capabilities.prototype['system_sound_effects_supported'] = undefined;

/**
 * @member {Boolean} user_eq_supported
 */
Capabilities.prototype['user_eq_supported'] = undefined;

/**
 * @member {Boolean} wifi_auto_save_supported
 */
Capabilities.prototype['wifi_auto_save_supported'] = undefined;

/**
 * @member {Boolean} wifi_regulatory_domain_locked
 */
Capabilities.prototype['wifi_regulatory_domain_locked'] = undefined;

/**
 * @member {Boolean} wifi_supported
 */
Capabilities.prototype['wifi_supported'] = undefined;






export default Capabilities;

