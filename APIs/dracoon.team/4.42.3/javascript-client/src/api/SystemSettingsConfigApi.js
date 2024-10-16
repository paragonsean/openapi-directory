/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AuthConfig from '../model/AuthConfig';
import ErrorResponse from '../model/ErrorResponse';
import EventlogConfig from '../model/EventlogConfig';
import GeneralSettings from '../model/GeneralSettings';
import InfrastructureProperties from '../model/InfrastructureProperties';
import SyslogConfig from '../model/SyslogConfig';
import SystemDefaults from '../model/SystemDefaults';
import UpdateEventlogConfig from '../model/UpdateEventlogConfig';
import UpdateGeneralSettings from '../model/UpdateGeneralSettings';
import UpdateSyslogConfig from '../model/UpdateSyslogConfig';
import UpdateSystemDefaults from '../model/UpdateSystemDefaults';

/**
* SystemSettingsConfig service.
* @module api/SystemSettingsConfigApi
* @version 4.42.3
*/
export default class SystemSettingsConfigApi {

    /**
    * Constructs a new SystemSettingsConfigApi. 
    * @alias module:api/SystemSettingsConfigApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the requestAuthConfig operation.
     * @callback module:api/SystemSettingsConfigApi~requestAuthConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AuthConfig} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request authentication settings
     * <h3 style='padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;'>&#128640; Since v4.6.0</h3>  ### Description:   DRACOON authentication configuration entry point.    ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; read global config</span> and role <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128100; Config Manager</span> of the Provider Customer required.  ### Postcondition: Returns a list of configurable authentication methods.  ### Further Information: Authentication methods are sorted by priority attribute.   Smaller values have higher priority.   Authentication method with highest priority is considered as default.   Priority **MUST** be a positive value.  ### Configurable authentication settings: <details open style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | Authentication Method | Description | | :--- | :--- | | `basic` | **Basic** authentication globally allowed.<br>This option **MUST** be activated to allow users to log in with their credentials stored in the database.<br>Formerly known as `sql`. | | `active_directory` | **Active Directory** authentication globally allowed.<br>This option **MUST** be activated to allow users to log in with their Active Directory credentials. | | `radius` | **RADIUS** authentication globally allowed.<br>This option **MUST** be activated to allow users to log in with their RADIUS username, their PIN and a token password. | | `openid` | **OpenID Connect** authentication globally allowed.This option **MUST** be activated to allow users to log in with their OpenID Connect identity. |  </details>
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/SystemSettingsConfigApi~requestAuthConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AuthConfig}
     */
    requestAuthConfig(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = AuthConfig;
      return this.apiClient.callApi(
        '/v4/system/config/settings/auth', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the requestEventlogConfig operation.
     * @callback module:api/SystemSettingsConfigApi~requestEventlogConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EventlogConfig} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request eventlog settings
     * <h3 style='padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;'>&#128640; Since v4.6.0</h3>  ### Description:   DRACOON eventlog configuration entry point.    ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; read global config</span> and role <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128100; Config Manager</span> of the Provider Customer required.  ### Postcondition: Returns a list of configurable eventlog settings.  ### Further Information: None.  ### Configurable eventlog settings: <details open style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | Setting | Description | Value | | :--- | :--- | :--- | | `enabled` | Determines whether eventlog is enabled. | `true or false` | | `retentionPeriod` | Retention period (in _days_) of eventlog entries.<br>After that period, all entries are deleted. | `Integer between 0 and 9999`<br>If set to `0`: no logs are deleted | | `logIpEnabled` | Determines whether user’s IP address is logged. | `true or false` |  </details>
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/SystemSettingsConfigApi~requestEventlogConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EventlogConfig}
     */
    requestEventlogConfig(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = EventlogConfig;
      return this.apiClient.callApi(
        '/v4/system/config/settings/eventlog', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the requestGeneralSettings operation.
     * @callback module:api/SystemSettingsConfigApi~requestGeneralSettingsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GeneralSettings} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request general settings
     * <h3 style='padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;'>&#128640; Since v4.6.0</h3>  ### Description:   DRACOON general settings configuration entry point.    ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; read global config</span> and role <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128100; Config Manager</span> of the Provider Customer required.  ### Postcondition: Returns a list of configurable general settings.  ### Further Information:  ### Auth token restrictions:  A restriction is a lower bound for a token timeout and defines a duration after which a token is invalidated when it wasn't used.   The access/refresh token validity duration of the client is the upper bound. A token is invalidated - in any case - when it has passed.    Auth token restrictions are enabled by default.  * Default access token validity: **2 hours**   * Default refresh token validity: **30 days**  ### Configurable general settings: <details open style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | Setting | Description | Value | | :--- | :--- | :--- | | `sharePasswordSmsEnabled` | Determines whether sending of share passwords via SMS is allowed. | `true or false` | | `cryptoEnabled` | Determines whether client-side encryption is enabled.<br>Can only be enabled once; disabling is **NOT** possible. | `true or false` | | `emailNotificationButtonEnabled` | Determines whether email notification button is enabled. | `true or false` | | `eulaEnabled` | Determines whether EULA is enabled.<br>Each user has to confirm the EULA at first login. | `true or false` | | `useS3Storage` | Defines if S3 is used as storage backend.<br>Can only be enabled once; disabling is **NOT** possible. | `true or false` | | `s3TagsEnabled` | Determines whether S3 tags are enabled | `true or false` | | `authTokenRestrictions` | Determines auth token restrictions. (e.g. restricted access token validity) | `object` |  </details>  ### Deprecated configurable general settings: <details style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | Setting                           | Description | Value | |:----------------------------------| :--- | :--- | | <del>`mediaServerEnabled`</del>   | Determines whether media server is enabled.<br>Returns boolean value dependent on conjunction of `mediaServerConfigEnabled` AND `mediaServerEnabled` | `true or false` | | <del>`weakPasswordEnabled`</del>  | Determines whether weak password is allowed.<br>Use `GET /system/config/policies/passwords` API to get configured password policies. | `true or false` | | <del>`hideLoginInputFields`</del> | Determines whether input fields for login should be enabled | `true or false` |  </details>
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/SystemSettingsConfigApi~requestGeneralSettingsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GeneralSettings}
     */
    requestGeneralSettings(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GeneralSettings;
      return this.apiClient.callApi(
        '/v4/system/config/settings/general', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the requestInfrastructureProperties operation.
     * @callback module:api/SystemSettingsConfigApi~requestInfrastructurePropertiesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InfrastructureProperties} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request infrastructure properties
     * <h3 style='padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;'>&#128640; Since v4.6.0</h3>  ### Description:   DRACOON infrastructure properties entry point.    ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; read global config</span> and role <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128100; Config Manager</span> of the Provider Customer required.  ### Postcondition: Returns a list of read-only infrastructure properties.  ### Further Information: Source: `core-service.properties`  ### Read-only infrastructure properties: <details open style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | Setting | Description | Value | | :--- | :--- | :--- | | `smsConfigEnabled` | Determines whether sending of share passwords via SMS is **system-wide** enabled. | `true or false` | | `mediaServerConfigEnabled` | Determines whether media server is **system-wide** enabled. | `true or false` | | `s3DefaultRegion` | Suggested S3 region | `Region name` | | `s3EnforceDirectUpload` | Enforce direct upload to S3 | `true or false` | | `dracoonCloud` | Determines if the **DRACOON Core** is deployed in the cloud environment | `true or false` | | `tenantUuid` | Current tenant UUID | `UUID` |  </details>
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/SystemSettingsConfigApi~requestInfrastructurePropertiesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InfrastructureProperties}
     */
    requestInfrastructureProperties(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = InfrastructureProperties;
      return this.apiClient.callApi(
        '/v4/system/config/settings/infrastructure', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the requestSyslogConfig operation.
     * @callback module:api/SystemSettingsConfigApi~requestSyslogConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SyslogConfig} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request syslog settings
     * <h3 style='padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;'>&#128640; Since v4.6.0</h3>  ### Description:   DRACOON syslog configuration entry point.    ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; read global config</span> and role <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128100; Config Manager</span> of the Provider Customer required.  ### Postcondition: Returns a list of configurable syslog settings.  ### Further Information: None.  ### Configurable syslog settings: <details open style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | Setting | Description | Value | | :--- | :--- | :--- | | `enabled` | Determines whether syslog is enabled. | `true or false` | | `host` | Syslog server (IP or FQDN) | `DNS name or IPv4 of a syslog server` | | `port` | Syslog server port | `Valid port number` | | `protocol` | Protocol to connect to syslog server | `TCP or UDP` | | `logIpEnabled` | Determines whether user’s IP address is logged. | `true or false` |  </details>
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/SystemSettingsConfigApi~requestSyslogConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SyslogConfig}
     */
    requestSyslogConfig(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SyslogConfig;
      return this.apiClient.callApi(
        '/v4/system/config/settings/syslog', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the requestSystemDefaults operation.
     * @callback module:api/SystemSettingsConfigApi~requestSystemDefaultsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SystemDefaults} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Request system defaults
     * <h3 style='padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;'>&#128640; Since v4.6.0</h3>  ### Description:   DRACOON system defaults configuration entry point.    ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; read global config</span> and role <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128100; Config Manager</span> of the Provider Customer required.  ### Postcondition: Returns a list of configurable system default values.  ### Further Information: None.  ### Configurable default values <details open style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | Setting | Description | Value | | :--- | :--- | :--- | | `languageDefault` | Defines which language should be default. | `ISO 639-1 code` | | `downloadShareDefaultExpirationPeriod` | Default expiration period for Download Shares in _days_. | `Integer between 0 and 9999` | | `uploadShareDefaultExpirationPeriod` | Default expiration period for Upload Shares in _days_. | `Integer between 0 and 9999` | | `fileDefaultExpirationPeriod` | Default expiration period for all uploaded files in _days_. | `Integer between 0 and 9999` | | `nonmemberViewerDefault` | Defines if new users get the role _Non Member Viewer_ by default | `true or false` |  </details>
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/SystemSettingsConfigApi~requestSystemDefaultsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SystemDefaults}
     */
    requestSystemDefaults(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SystemDefaults;
      return this.apiClient.callApi(
        '/v4/system/config/settings/defaults', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateAuthConfig operation.
     * @callback module:api/SystemSettingsConfigApi~updateAuthConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AuthConfig} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update authentication settings
     * <h3 style='padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;'>&#128640; Since v4.6.0</h3>  ### Description:   DRACOON authentication configuration entry point.   Change configurable authentication settings.  ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; change global config</span> and role <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128100; Config Manager</span> of the Provider Customer required.  ### Postcondition: One or more authentication methods gets changed.  ### Further Information: Authentication methods are sorted by priority attribute.   Smaller values have higher priority.   Authentication method with highest priority is considered as default.   Priority **MUST** be a positive value.  ### Configurable authentication settings: <details open style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | Authentication Method | Description | | :--- | :--- | | `basic` | **Basic** authentication globally allowed.<br>This option **MUST** be activated to allow users to log in with their credentials stored in the database.<br>Formerly known as `sql`. | | `active_directory` | **Active Directory** authentication globally allowed.<br>This option **MUST** be activated to allow users to log in with their Active Directory credentials. | | `radius` | **RADIUS** authentication globally allowed.<br>This option **MUST** be activated to allow users to log in with their RADIUS username, their PIN and a token password. | | `openid` | **OpenID Connect** authentication globally allowed.This option **MUST** be activated to allow users to log in with their OpenID Connect identity. |  </details>
     * @param {module:model/AuthConfig} authConfig 
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/SystemSettingsConfigApi~updateAuthConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AuthConfig}
     */
    updateAuthConfig(authConfig, opts, callback) {
      opts = opts || {};
      let postBody = authConfig;
      // verify the required parameter 'authConfig' is set
      if (authConfig === undefined || authConfig === null) {
        throw new Error("Missing the required parameter 'authConfig' when calling updateAuthConfig");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = AuthConfig;
      return this.apiClient.callApi(
        '/v4/system/config/settings/auth', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateEventlogConfig operation.
     * @callback module:api/SystemSettingsConfigApi~updateEventlogConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EventlogConfig} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update eventlog settings
     * <h3 style='padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;'>&#128640; Since v4.6.0</h3>  ### Description:   DRACOON eventlog configuration entry point.   Change configurable eventlog settings.  ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; change global config</span> and role <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128100; Config Manager</span> of the Provider Customer required.  ### Postcondition: One or more eventlog settings gets changed.  ### Further Information: None.  ### Configurable eventlog settings: <details open style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | Setting | Description | Value | | :--- | :--- | :--- | | `enabled` | Determines whether eventlog is enabled. | `true or false` | | `retentionPeriod` | Retention period (in _days_) of eventlog entries.<br>After that period, all entries are deleted. | `Integer between 0 and 9999`<br>If set to `0`: no logs are deleted<br>Recommended value: 7 | | `logIpEnabled` | Determines whether user’s IP address is logged. | `true or false` |  </details>
     * @param {module:model/UpdateEventlogConfig} updateEventlogConfig 
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/SystemSettingsConfigApi~updateEventlogConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EventlogConfig}
     */
    updateEventlogConfig(updateEventlogConfig, opts, callback) {
      opts = opts || {};
      let postBody = updateEventlogConfig;
      // verify the required parameter 'updateEventlogConfig' is set
      if (updateEventlogConfig === undefined || updateEventlogConfig === null) {
        throw new Error("Missing the required parameter 'updateEventlogConfig' when calling updateEventlogConfig");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = EventlogConfig;
      return this.apiClient.callApi(
        '/v4/system/config/settings/eventlog', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateGeneralSettings operation.
     * @callback module:api/SystemSettingsConfigApi~updateGeneralSettingsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GeneralSettings} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update general settings
     * <h3 style='padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;'>&#128640; Since v4.6.0</h3>  ### Description:   DRACOON general settings configuration entry point.   Change configurable general settings.  ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; change global config</span> and role <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128100; Config Manager</span> of the Provider Customer required.  ### Postcondition: One or more general settings gets changed.  ### Further Information: Auth token restrictions are enabled by default.      * Default access token validity: **2 hours**   * Default refresh token validity: **30 days**  ### Configurable general settings: <details open style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | Setting | Description | Value | | :--- | :--- | :--- | | `sharePasswordSmsEnabled` | Determines whether sending of share passwords via SMS is allowed. | `true or false` | | `cryptoEnabled` | Determines whether client-side encryption is enabled.<br>Can only be enabled once; disabling is **NOT** possible. | `true or false` | | `emailNotificationButtonEnabled` | Determines whether email notification button is enabled. | `true or false` | | `eulaEnabled` | Determines whether EULA is enabled.<br>Each user has to confirm the EULA at first login. | `true or false` | | `s3TagsEnabled` | Determines whether S3 tags are enabled | `true or false` | | `authTokenRestrictions` | Determines auth token restrictions. (e.g. restricted access token validity) | `object` |  </details>  ### Deprecated configurable general settings: <details style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | Setting                           | Description | Value | |:----------------------------------| :--- | :--- | | <del>`mediaServerEnabled`</del>   | Determines whether media server is enabled.<br>**CANNOT** be enabled if media server configuration is disabled in `core-service.properties`.<br>Check `mediaServerConfigEnabled` with `GET /system/config/settings/infrastructure`. | `true or false` | | <del>`weakPasswordEnabled`</del>  | Determines whether weak password is allowed.<br>Use `PUT /system/config/policies/passwords` API to change configured password policies. | `true or false` | | <del>`hideLoginInputFields`</del> | Determines whether input fields for login should be enabled | `true or false` |  </details>
     * @param {module:model/UpdateGeneralSettings} updateGeneralSettings 
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/SystemSettingsConfigApi~updateGeneralSettingsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GeneralSettings}
     */
    updateGeneralSettings(updateGeneralSettings, opts, callback) {
      opts = opts || {};
      let postBody = updateGeneralSettings;
      // verify the required parameter 'updateGeneralSettings' is set
      if (updateGeneralSettings === undefined || updateGeneralSettings === null) {
        throw new Error("Missing the required parameter 'updateGeneralSettings' when calling updateGeneralSettings");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GeneralSettings;
      return this.apiClient.callApi(
        '/v4/system/config/settings/general', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateSyslogConfig operation.
     * @callback module:api/SystemSettingsConfigApi~updateSyslogConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SyslogConfig} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update syslog settings
     * <h3 style='padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;'>&#128640; Since v4.6.0</h3>  ### Description:   DRACOON syslog configuration entry point.   Change configurable syslog settings.  ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; change global config</span> and role <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128100; Config Manager</span> of the Provider Customer required.  ### Postcondition: One or more syslog settings gets changed.  ### Further Information: None.  ### Configurable syslog settings: <details open style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | Setting | Description | Value | | :--- | :--- | :--- | | `enabled` | Set `true` to enable syslog. | `true or false` | | `host` | Syslog server (IP or FQDN) | `DNS name or IPv4 of a syslog server` | | `port` | Syslog server port | `Valid port number` | | `protocol` | Protocol to connect to syslog server | `TCP or UDP` | | `logIpEnabled` | Determines whether user’s IP address is logged. | `true or false` |  </details>
     * @param {module:model/UpdateSyslogConfig} updateSyslogConfig 
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/SystemSettingsConfigApi~updateSyslogConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SyslogConfig}
     */
    updateSyslogConfig(updateSyslogConfig, opts, callback) {
      opts = opts || {};
      let postBody = updateSyslogConfig;
      // verify the required parameter 'updateSyslogConfig' is set
      if (updateSyslogConfig === undefined || updateSyslogConfig === null) {
        throw new Error("Missing the required parameter 'updateSyslogConfig' when calling updateSyslogConfig");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = SyslogConfig;
      return this.apiClient.callApi(
        '/v4/system/config/settings/syslog', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateSystemDefaults operation.
     * @callback module:api/SystemSettingsConfigApi~updateSystemDefaultsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SystemDefaults} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update system defaults
     * <h3 style='padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;'>&#128640; Since v4.6.0</h3>  ### Description:   DRACOON system defaults configuration entry point.   Change configurable system default values.  ### Precondition: Right <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128275; change global config</span> and role <span style='padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;'>&#128100; Config Manager</span> of the Provider Customer required.  ### Postcondition: One or more system default values gets changed.  ### Further Information: None.  ### Configurable default values <details open style=\"padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\"> <summary style=\"cursor: pointer; outline: none\"><strong>Expand</strong></summary>  | Setting | Description | Value | | :--- | :--- | :--- | | `languageDefault` | Defines which language should be default. | `ISO 639-1 code` | | `downloadShareDefaultExpirationPeriod` | Default expiration period for Download Shares in _days_. | `Integer between 0 and 9999`<br>Set `0` to disable. | | `uploadShareDefaultExpirationPeriod` | Default expiration period for Upload Shares in _days_. | `Integer between 0 and 9999`<br>Set `0` to disable. | | `fileDefaultExpirationPeriod` | Default expiration period for all uploaded files in _days_. | `Integer between 0 and 9999`<br>Set `0` to disable. | | `nonmemberViewerDefault` | Defines if new users get the role _Non Member Viewer_ by default | `true or false` |  </details>
     * @param {module:model/UpdateSystemDefaults} updateSystemDefaults 
     * @param {Object} opts Optional parameters
     * @param {String} [xSdsAuthToken] Authentication token
     * @param {module:api/SystemSettingsConfigApi~updateSystemDefaultsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SystemDefaults}
     */
    updateSystemDefaults(updateSystemDefaults, opts, callback) {
      opts = opts || {};
      let postBody = updateSystemDefaults;
      // verify the required parameter 'updateSystemDefaults' is set
      if (updateSystemDefaults === undefined || updateSystemDefaults === null) {
        throw new Error("Missing the required parameter 'updateSystemDefaults' when calling updateSystemDefaults");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Sds-Auth-Token': opts['xSdsAuthToken']
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = SystemDefaults;
      return this.apiClient.callApi(
        '/v4/system/config/settings/defaults', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
