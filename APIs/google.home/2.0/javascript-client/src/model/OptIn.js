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
 * The OptIn model module.
 * @module model/OptIn
 * @version 2.0
 */
class OptIn {
    /**
     * Constructs a new <code>OptIn</code>.
     * @alias module:model/OptIn
     * @param audioHdr {Boolean} 
     * @param audioSurroundMode {Number} 
     * @param autoplayOnSignal {Boolean} 
     * @param cloudIpc {Boolean} 
     * @param hdmiPrefer50hz {Boolean} 
     * @param hdmiPreferHighFps {Boolean} 
     * @param managedMode {Boolean} 
     * @param opencast {Boolean} 
     * @param previewChannel {Boolean} 
     * @param remoteDucking {Boolean} 
     * @param stats {Boolean} 
     * @param uiFlipped {Boolean} 
     * @param wpa3SupportEnabled {Boolean} 
     */
    constructor(audioHdr, audioSurroundMode, autoplayOnSignal, cloudIpc, hdmiPrefer50hz, hdmiPreferHighFps, managedMode, opencast, previewChannel, remoteDucking, stats, uiFlipped, wpa3SupportEnabled) { 
        
        OptIn.initialize(this, audioHdr, audioSurroundMode, autoplayOnSignal, cloudIpc, hdmiPrefer50hz, hdmiPreferHighFps, managedMode, opencast, previewChannel, remoteDucking, stats, uiFlipped, wpa3SupportEnabled);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, audioHdr, audioSurroundMode, autoplayOnSignal, cloudIpc, hdmiPrefer50hz, hdmiPreferHighFps, managedMode, opencast, previewChannel, remoteDucking, stats, uiFlipped, wpa3SupportEnabled) { 
        obj['audio_hdr'] = audioHdr;
        obj['audio_surround_mode'] = audioSurroundMode;
        obj['autoplay_on_signal'] = autoplayOnSignal;
        obj['cloud_ipc'] = cloudIpc;
        obj['hdmi_prefer_50hz'] = hdmiPrefer50hz;
        obj['hdmi_prefer_high_fps'] = hdmiPreferHighFps;
        obj['managed_mode'] = managedMode;
        obj['opencast'] = opencast;
        obj['preview_channel'] = previewChannel;
        obj['remote_ducking'] = remoteDucking;
        obj['stats'] = stats;
        obj['ui_flipped'] = uiFlipped;
        obj['wpa3_support_enabled'] = wpa3SupportEnabled;
    }

    /**
     * Constructs a <code>OptIn</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OptIn} obj Optional instance to populate.
     * @return {module:model/OptIn} The populated <code>OptIn</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OptIn();

            if (data.hasOwnProperty('audio_hdr')) {
                obj['audio_hdr'] = ApiClient.convertToType(data['audio_hdr'], 'Boolean');
            }
            if (data.hasOwnProperty('audio_surround_mode')) {
                obj['audio_surround_mode'] = ApiClient.convertToType(data['audio_surround_mode'], 'Number');
            }
            if (data.hasOwnProperty('autoplay_on_signal')) {
                obj['autoplay_on_signal'] = ApiClient.convertToType(data['autoplay_on_signal'], 'Boolean');
            }
            if (data.hasOwnProperty('cloud_ipc')) {
                obj['cloud_ipc'] = ApiClient.convertToType(data['cloud_ipc'], 'Boolean');
            }
            if (data.hasOwnProperty('hdmi_prefer_50hz')) {
                obj['hdmi_prefer_50hz'] = ApiClient.convertToType(data['hdmi_prefer_50hz'], 'Boolean');
            }
            if (data.hasOwnProperty('hdmi_prefer_high_fps')) {
                obj['hdmi_prefer_high_fps'] = ApiClient.convertToType(data['hdmi_prefer_high_fps'], 'Boolean');
            }
            if (data.hasOwnProperty('managed_mode')) {
                obj['managed_mode'] = ApiClient.convertToType(data['managed_mode'], 'Boolean');
            }
            if (data.hasOwnProperty('opencast')) {
                obj['opencast'] = ApiClient.convertToType(data['opencast'], 'Boolean');
            }
            if (data.hasOwnProperty('preview_channel')) {
                obj['preview_channel'] = ApiClient.convertToType(data['preview_channel'], 'Boolean');
            }
            if (data.hasOwnProperty('remote_ducking')) {
                obj['remote_ducking'] = ApiClient.convertToType(data['remote_ducking'], 'Boolean');
            }
            if (data.hasOwnProperty('stats')) {
                obj['stats'] = ApiClient.convertToType(data['stats'], 'Boolean');
            }
            if (data.hasOwnProperty('ui_flipped')) {
                obj['ui_flipped'] = ApiClient.convertToType(data['ui_flipped'], 'Boolean');
            }
            if (data.hasOwnProperty('wpa3_support_enabled')) {
                obj['wpa3_support_enabled'] = ApiClient.convertToType(data['wpa3_support_enabled'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OptIn</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OptIn</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OptIn.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

OptIn.RequiredProperties = ["audio_hdr", "audio_surround_mode", "autoplay_on_signal", "cloud_ipc", "hdmi_prefer_50hz", "hdmi_prefer_high_fps", "managed_mode", "opencast", "preview_channel", "remote_ducking", "stats", "ui_flipped", "wpa3_support_enabled"];

/**
 * @member {Boolean} audio_hdr
 */
OptIn.prototype['audio_hdr'] = undefined;

/**
 * @member {Number} audio_surround_mode
 */
OptIn.prototype['audio_surround_mode'] = undefined;

/**
 * @member {Boolean} autoplay_on_signal
 */
OptIn.prototype['autoplay_on_signal'] = undefined;

/**
 * @member {Boolean} cloud_ipc
 */
OptIn.prototype['cloud_ipc'] = undefined;

/**
 * @member {Boolean} hdmi_prefer_50hz
 */
OptIn.prototype['hdmi_prefer_50hz'] = undefined;

/**
 * @member {Boolean} hdmi_prefer_high_fps
 */
OptIn.prototype['hdmi_prefer_high_fps'] = undefined;

/**
 * @member {Boolean} managed_mode
 */
OptIn.prototype['managed_mode'] = undefined;

/**
 * @member {Boolean} opencast
 */
OptIn.prototype['opencast'] = undefined;

/**
 * @member {Boolean} preview_channel
 */
OptIn.prototype['preview_channel'] = undefined;

/**
 * @member {Boolean} remote_ducking
 */
OptIn.prototype['remote_ducking'] = undefined;

/**
 * @member {Boolean} stats
 */
OptIn.prototype['stats'] = undefined;

/**
 * @member {Boolean} ui_flipped
 */
OptIn.prototype['ui_flipped'] = undefined;

/**
 * @member {Boolean} wpa3_support_enabled
 */
OptIn.prototype['wpa3_support_enabled'] = undefined;






export default OptIn;

