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


import ApiClient from "../ApiClient";
import AppDeviceIDRequest from '../model/AppDeviceIDRequest';
import CheckReadyStatusRequest from '../model/CheckReadyStatusRequest';
import Example1 from '../model/Example1';
import Example11 from '../model/Example11';
import Example12 from '../model/Example12';
import Example13 from '../model/Example13';
import Example14 from '../model/Example14';
import Example15 from '../model/Example15';
import Example16 from '../model/Example16';
import TestInternetDownloadSpeedRequest from '../model/TestInternetDownloadSpeedRequest';

/**
* DeviceInfo service.
* @module api/DeviceInfoApi
* @version 2.0
*/
export default class DeviceInfoApi {

    /**
    * Constructs a new DeviceInfoApi. 
    * @alias module:api/DeviceInfoApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the appDeviceID operation.
     * @callback module:api/DeviceInfoApi~appDeviceIDCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Example11} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * App Device ID
     * This gives \"app device id\", \"certificate\" and \"signed data\".   The `app_id` in the request is mandatory and refers to Chromecast backdrop/screensaver app. It has to be set to `E8C28D3C`.    The certificate is valid and issued by `Chromecast ICA 6 (Audio Assist), Google Inc`.  Not sure what the other two are.
     * @param {module:model/AppDeviceIDRequest} appDeviceIDRequest 
     * @param {module:api/DeviceInfoApi~appDeviceIDCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Example11}
     */
    appDeviceID(appDeviceIDRequest, callback) {
      let postBody = appDeviceIDRequest;
      // verify the required parameter 'appDeviceIDRequest' is set
      if (appDeviceIDRequest === undefined || appDeviceIDRequest === null) {
        throw new Error("Missing the required parameter 'appDeviceIDRequest' when calling appDeviceID");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['cast-local-authorization-token'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Example11;
      return this.apiClient.callApi(
        '/get_app_device_id', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the checkReadyStatus operation.
     * @callback module:api/DeviceInfoApi~checkReadyStatusCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Example13} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Check Ready Status
     * **Update:** This seems to have changed now and is no longer possible. The error is also new.  Setting `play_ready_message` to true plays a welcome message on the device saying \"Hi, I'm your Google Assistant. I'm here to help. To learn a few things you can do, continue in the Google Home app.\"
     * @param {module:model/CheckReadyStatusRequest} checkReadyStatusRequest 
     * @param {module:api/DeviceInfoApi~checkReadyStatusCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Example13}
     */
    checkReadyStatus(checkReadyStatusRequest, callback) {
      let postBody = checkReadyStatusRequest;
      // verify the required parameter 'checkReadyStatusRequest' is set
      if (checkReadyStatusRequest === undefined || checkReadyStatusRequest === null) {
        throw new Error("Missing the required parameter 'checkReadyStatusRequest' when calling checkReadyStatus");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['cast-local-authorization-token'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Example13;
      return this.apiClient.callApi(
        '/assistant/check_ready_status', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the eurekaInfo operation.
     * @callback module:api/DeviceInfoApi~eurekaInfoCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Example1} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Eureka Info
     * This gives most of the device info. The GET parameter `param` is a comma separated list of json keys to fetch. Currently, these params are known: `version,audio,name,build_info,detail,device_info,net,wifi,setup,settings,opt_in,opencast,multizone,proxy,night_mode_params,user_eq,room_equalizer,sign,aogh,ultrasound,mesh`  Nested items can also be filtered using the dot notation. Example: `audio.digital`  The `options` GET parameter is always set to `detail` or `detail,sign`. `sign` signs the `nonce` and returns some value.  The `nonce` GET parameter is an integer value signed with needed (see `option` parameter above).
     * @param {String} params 
     * @param {String} options 
     * @param {Number} nonce 
     * @param {module:api/DeviceInfoApi~eurekaInfoCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Example1}
     */
    eurekaInfo(params, options, nonce, callback) {
      let postBody = null;
      // verify the required parameter 'params' is set
      if (params === undefined || params === null) {
        throw new Error("Missing the required parameter 'params' when calling eurekaInfo");
      }
      // verify the required parameter 'options' is set
      if (options === undefined || options === null) {
        throw new Error("Missing the required parameter 'options' when calling eurekaInfo");
      }
      // verify the required parameter 'nonce' is set
      if (nonce === undefined || nonce === null) {
        throw new Error("Missing the required parameter 'nonce' when calling eurekaInfo");
      }

      let pathParams = {
      };
      let queryParams = {
        'params': params,
        'options': options,
        'nonce': nonce
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['cast-local-authorization-token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Example1;
      return this.apiClient.callApi(
        '/eureka_info', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the locales operation.
     * @callback module:api/DeviceInfoApi~localesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Example15>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Locales
     * Simply returns a list of all supported locales.
     * @param {module:api/DeviceInfoApi~localesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Example15>}
     */
    locales(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['cast-local-authorization-token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Example15];
      return this.apiClient.callApi(
        '/supported_locales', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the offer operation.
     * @callback module:api/DeviceInfoApi~offerCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Example12} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Offer
     * This gives a token which is used by the Home app to get offers. The offers themselves are not stored on the device.   A new token is generated for every request.
     * @param {module:api/DeviceInfoApi~offerCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Example12}
     */
    offer(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['cast-local-authorization-token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Example12;
      return this.apiClient.callApi(
        '/offer', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the testInternetDownloadSpeed operation.
     * @callback module:api/DeviceInfoApi~testInternetDownloadSpeedCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Example16} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Test Internet Download Speed
     * **Update:** This seems to have been removed. Returns 404 Not Found.  This endpoint tests internet download speed. Any sample file URL can be provided.
     * @param {module:model/TestInternetDownloadSpeedRequest} testInternetDownloadSpeedRequest 
     * @param {module:api/DeviceInfoApi~testInternetDownloadSpeedCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Example16}
     */
    testInternetDownloadSpeed(testInternetDownloadSpeedRequest, callback) {
      let postBody = testInternetDownloadSpeedRequest;
      // verify the required parameter 'testInternetDownloadSpeedRequest' is set
      if (testInternetDownloadSpeedRequest === undefined || testInternetDownloadSpeedRequest === null) {
        throw new Error("Missing the required parameter 'testInternetDownloadSpeedRequest' when calling testInternetDownloadSpeed");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['cast-local-authorization-token'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Example16;
      return this.apiClient.callApi(
        '/test_internet_download_speed', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the timezones operation.
     * @callback module:api/DeviceInfoApi~timezonesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Example14>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Timezones
     * Simply returns a list of all supported timezones.
     * @param {module:api/DeviceInfoApi~timezonesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Example14>}
     */
    timezones(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['cast-local-authorization-token'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Example14];
      return this.apiClient.callApi(
        '/supported_timezones', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
