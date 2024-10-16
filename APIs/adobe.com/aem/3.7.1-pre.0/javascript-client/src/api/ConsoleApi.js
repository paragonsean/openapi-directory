/**
 * Adobe Experience Manager (AEM) API
 * Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
 *
 * The version of the OpenAPI document: 3.7.1-pre.0
 * Contact: opensource@shinesolutions.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import BundleInfo from '../model/BundleInfo';
import SamlConfigurationInfo from '../model/SamlConfigurationInfo';

/**
* Console service.
* @module api/ConsoleApi
* @version 3.7.1-pre.0
*/
export default class ConsoleApi {

    /**
    * Constructs a new ConsoleApi. 
    * @alias module:api/ConsoleApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getAemProductInfo operation.
     * @callback module:api/ConsoleApi~getAemProductInfoCallback
     * @param {String} error Error message, if any.
     * @param {Array.<String>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:api/ConsoleApi~getAemProductInfoCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<String>}
     */
    getAemProductInfo(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['aemAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ['String'];
      return this.apiClient.callApi(
        '/system/console/status-productinfo.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getBundleInfo operation.
     * @callback module:api/ConsoleApi~getBundleInfoCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BundleInfo} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} name 
     * @param {module:api/ConsoleApi~getBundleInfoCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BundleInfo}
     */
    getBundleInfo(name, callback) {
      let postBody = null;
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling getBundleInfo");
      }

      let pathParams = {
        'name': name
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['aemAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = BundleInfo;
      return this.apiClient.callApi(
        '/system/console/bundles/{name}.json', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getConfigMgr operation.
     * @callback module:api/ConsoleApi~getConfigMgrCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:api/ConsoleApi~getConfigMgrCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    getConfigMgr(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['aemAuth'];
      let contentTypes = [];
      let accepts = ['text/xml'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/system/console/configMgr', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postBundle operation.
     * @callback module:api/ConsoleApi~postBundleCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} name 
     * @param {String} action 
     * @param {module:api/ConsoleApi~postBundleCallback} callback The callback function, accepting three arguments: error, data, response
     */
    postBundle(name, action, callback) {
      let postBody = null;
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling postBundle");
      }
      // verify the required parameter 'action' is set
      if (action === undefined || action === null) {
        throw new Error("Missing the required parameter 'action' when calling postBundle");
      }

      let pathParams = {
        'name': name
      };
      let queryParams = {
        'action': action
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['aemAuth'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/system/console/bundles/{name}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postJmxRepository operation.
     * @callback module:api/ConsoleApi~postJmxRepositoryCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} action 
     * @param {module:api/ConsoleApi~postJmxRepositoryCallback} callback The callback function, accepting three arguments: error, data, response
     */
    postJmxRepository(action, callback) {
      let postBody = null;
      // verify the required parameter 'action' is set
      if (action === undefined || action === null) {
        throw new Error("Missing the required parameter 'action' when calling postJmxRepository");
      }

      let pathParams = {
        'action': action
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['aemAuth'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/system/console/jmx/com.adobe.granite:type=Repository/op/{action}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postSamlConfiguration operation.
     * @callback module:api/ConsoleApi~postSamlConfigurationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SamlConfigurationInfo} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {Boolean} [post] 
     * @param {Boolean} [apply] 
     * @param {Boolean} [_delete] 
     * @param {String} [action] 
     * @param {String} [location] 
     * @param {Array.<String>} [path] 
     * @param {Number} [serviceRanking] 
     * @param {String} [idpUrl] 
     * @param {String} [idpCertAlias] 
     * @param {Boolean} [idpHttpRedirect] 
     * @param {String} [serviceProviderEntityId] 
     * @param {String} [assertionConsumerServiceURL] 
     * @param {String} [spPrivateKeyAlias] 
     * @param {String} [keyStorePassword] 
     * @param {String} [defaultRedirectUrl] 
     * @param {String} [userIDAttribute] 
     * @param {Boolean} [useEncryption] 
     * @param {Boolean} [createUser] 
     * @param {Boolean} [addGroupMemberships] 
     * @param {String} [groupMembershipAttribute] 
     * @param {Array.<String>} [defaultGroups] 
     * @param {String} [nameIdFormat] 
     * @param {Array.<String>} [synchronizeAttributes] 
     * @param {Boolean} [handleLogout] 
     * @param {String} [logoutUrl] 
     * @param {Number} [clockTolerance] 
     * @param {String} [digestMethod] 
     * @param {String} [signatureMethod] 
     * @param {String} [userIntermediatePath] 
     * @param {Array.<String>} [propertylist] 
     * @param {module:api/ConsoleApi~postSamlConfigurationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SamlConfigurationInfo}
     */
    postSamlConfiguration(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'post': opts['post'],
        'apply': opts['apply'],
        'delete': opts['_delete'],
        'action': opts['action'],
        '$location': opts['location'],
        'path': this.apiClient.buildCollectionParam(opts['path'], 'multi'),
        'service.ranking': opts['serviceRanking'],
        'idpUrl': opts['idpUrl'],
        'idpCertAlias': opts['idpCertAlias'],
        'idpHttpRedirect': opts['idpHttpRedirect'],
        'serviceProviderEntityId': opts['serviceProviderEntityId'],
        'assertionConsumerServiceURL': opts['assertionConsumerServiceURL'],
        'spPrivateKeyAlias': opts['spPrivateKeyAlias'],
        'keyStorePassword': opts['keyStorePassword'],
        'defaultRedirectUrl': opts['defaultRedirectUrl'],
        'userIDAttribute': opts['userIDAttribute'],
        'useEncryption': opts['useEncryption'],
        'createUser': opts['createUser'],
        'addGroupMemberships': opts['addGroupMemberships'],
        'groupMembershipAttribute': opts['groupMembershipAttribute'],
        'defaultGroups': this.apiClient.buildCollectionParam(opts['defaultGroups'], 'multi'),
        'nameIdFormat': opts['nameIdFormat'],
        'synchronizeAttributes': this.apiClient.buildCollectionParam(opts['synchronizeAttributes'], 'multi'),
        'handleLogout': opts['handleLogout'],
        'logoutUrl': opts['logoutUrl'],
        'clockTolerance': opts['clockTolerance'],
        'digestMethod': opts['digestMethod'],
        'signatureMethod': opts['signatureMethod'],
        'userIntermediatePath': opts['userIntermediatePath'],
        'propertylist': this.apiClient.buildCollectionParam(opts['propertylist'], 'csv')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['aemAuth'];
      let contentTypes = [];
      let accepts = ['text/plain'];
      let returnType = SamlConfigurationInfo;
      return this.apiClient.callApi(
        '/system/console/configMgr/com.adobe.granite.auth.saml.SamlAuthenticationHandler', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
