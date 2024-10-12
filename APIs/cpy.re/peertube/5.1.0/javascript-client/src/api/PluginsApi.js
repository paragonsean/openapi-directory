/**
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AddPluginRequest from '../model/AddPluginRequest';
import ApiV1PluginsNpmNameSettingsPutRequest from '../model/ApiV1PluginsNpmNameSettingsPutRequest';
import Plugin from '../model/Plugin';
import PluginResponse from '../model/PluginResponse';
import UninstallPluginRequest from '../model/UninstallPluginRequest';

/**
* Plugins service.
* @module api/PluginsApi
* @version 5.1.0
*/
export default class PluginsApi {

    /**
    * Constructs a new PluginsApi. 
    * @alias module:api/PluginsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addPlugin operation.
     * @callback module:api/PluginsApi~addPluginCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Install a plugin
     * @param {Object} opts Optional parameters
     * @param {module:model/AddPluginRequest} [addPluginRequest] 
     * @param {module:api/PluginsApi~addPluginCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addPlugin(opts, callback) {
      opts = opts || {};
      let postBody = opts['addPluginRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/plugins/install', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1PluginsNpmNamePublicSettingsGet operation.
     * @callback module:api/PluginsApi~apiV1PluginsNpmNamePublicSettingsGetCallback
     * @param {String} error Error message, if any.
     * @param {Object.<String, {String: Object}>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a plugin's public settings
     * @param {String} npmName name of the plugin/theme on npmjs.com or in its package.json
     * @param {module:api/PluginsApi~apiV1PluginsNpmNamePublicSettingsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object.<String, {String: Object}>}
     */
    apiV1PluginsNpmNamePublicSettingsGet(npmName, callback) {
      let postBody = null;
      // verify the required parameter 'npmName' is set
      if (npmName === undefined || npmName === null) {
        throw new Error("Missing the required parameter 'npmName' when calling apiV1PluginsNpmNamePublicSettingsGet");
      }

      let pathParams = {
        'npmName': npmName
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = {'String': Object};
      return this.apiClient.callApi(
        '/api/v1/plugins/{npmName}/public-settings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1PluginsNpmNameRegisteredSettingsGet operation.
     * @callback module:api/PluginsApi~apiV1PluginsNpmNameRegisteredSettingsGetCallback
     * @param {String} error Error message, if any.
     * @param {Object.<String, {String: Object}>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a plugin's registered settings
     * @param {String} npmName name of the plugin/theme on npmjs.com or in its package.json
     * @param {module:api/PluginsApi~apiV1PluginsNpmNameRegisteredSettingsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object.<String, {String: Object}>}
     */
    apiV1PluginsNpmNameRegisteredSettingsGet(npmName, callback) {
      let postBody = null;
      // verify the required parameter 'npmName' is set
      if (npmName === undefined || npmName === null) {
        throw new Error("Missing the required parameter 'npmName' when calling apiV1PluginsNpmNameRegisteredSettingsGet");
      }

      let pathParams = {
        'npmName': npmName
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = {'String': Object};
      return this.apiClient.callApi(
        '/api/v1/plugins/{npmName}/registered-settings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV1PluginsNpmNameSettingsPut operation.
     * @callback module:api/PluginsApi~apiV1PluginsNpmNameSettingsPutCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set a plugin's settings
     * @param {String} npmName name of the plugin/theme on npmjs.com or in its package.json
     * @param {Object} opts Optional parameters
     * @param {module:model/ApiV1PluginsNpmNameSettingsPutRequest} [apiV1PluginsNpmNameSettingsPutRequest] 
     * @param {module:api/PluginsApi~apiV1PluginsNpmNameSettingsPutCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV1PluginsNpmNameSettingsPut(npmName, opts, callback) {
      opts = opts || {};
      let postBody = opts['apiV1PluginsNpmNameSettingsPutRequest'];
      // verify the required parameter 'npmName' is set
      if (npmName === undefined || npmName === null) {
        throw new Error("Missing the required parameter 'npmName' when calling apiV1PluginsNpmNameSettingsPut");
      }

      let pathParams = {
        'npmName': npmName
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/plugins/{npmName}/settings', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAvailablePlugins operation.
     * @callback module:api/PluginsApi~getAvailablePluginsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PluginResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List available plugins
     * @param {Object} opts Optional parameters
     * @param {String} [search] 
     * @param {Number} [pluginType] 
     * @param {String} [currentPeerTubeEngine] 
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {String} [sort] Sort column
     * @param {module:api/PluginsApi~getAvailablePluginsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PluginResponse}
     */
    getAvailablePlugins(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'search': opts['search'],
        'pluginType': opts['pluginType'],
        'currentPeerTubeEngine': opts['currentPeerTubeEngine'],
        'start': opts['start'],
        'count': opts['count'],
        'sort': opts['sort']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PluginResponse;
      return this.apiClient.callApi(
        '/api/v1/plugins/available', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPlugin operation.
     * @callback module:api/PluginsApi~getPluginCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Plugin} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a plugin
     * @param {String} npmName name of the plugin/theme on npmjs.com or in its package.json
     * @param {module:api/PluginsApi~getPluginCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Plugin}
     */
    getPlugin(npmName, callback) {
      let postBody = null;
      // verify the required parameter 'npmName' is set
      if (npmName === undefined || npmName === null) {
        throw new Error("Missing the required parameter 'npmName' when calling getPlugin");
      }

      let pathParams = {
        'npmName': npmName
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Plugin;
      return this.apiClient.callApi(
        '/api/v1/plugins/{npmName}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPlugins operation.
     * @callback module:api/PluginsApi~getPluginsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PluginResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List plugins
     * @param {Object} opts Optional parameters
     * @param {Number} [pluginType] 
     * @param {Boolean} [uninstalled] 
     * @param {Number} [start] Offset used to paginate results
     * @param {Number} [count = 15)] Number of items to return
     * @param {String} [sort] Sort column
     * @param {module:api/PluginsApi~getPluginsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PluginResponse}
     */
    getPlugins(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'pluginType': opts['pluginType'],
        'uninstalled': opts['uninstalled'],
        'start': opts['start'],
        'count': opts['count'],
        'sort': opts['sort']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PluginResponse;
      return this.apiClient.callApi(
        '/api/v1/plugins', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the uninstallPlugin operation.
     * @callback module:api/PluginsApi~uninstallPluginCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Uninstall a plugin
     * @param {Object} opts Optional parameters
     * @param {module:model/UninstallPluginRequest} [uninstallPluginRequest] 
     * @param {module:api/PluginsApi~uninstallPluginCallback} callback The callback function, accepting three arguments: error, data, response
     */
    uninstallPlugin(opts, callback) {
      opts = opts || {};
      let postBody = opts['uninstallPluginRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/plugins/uninstall', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updatePlugin operation.
     * @callback module:api/PluginsApi~updatePluginCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a plugin
     * @param {Object} opts Optional parameters
     * @param {module:model/AddPluginRequest} [addPluginRequest] 
     * @param {module:api/PluginsApi~updatePluginCallback} callback The callback function, accepting three arguments: error, data, response
     */
    updatePlugin(opts, callback) {
      opts = opts || {};
      let postBody = opts['addPluginRequest'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2'];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/plugins/update', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
