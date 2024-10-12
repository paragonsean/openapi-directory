/**
 * MIMIC REST API
 * This is the API for MIMIC client to connect to MIMIC daemon.
 *
 * The version of the OpenAPI document: 21.00
 * Contact: support@gambitcomm.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ConfigWEB from '../model/ConfigWEB';

/**
* WEB service.
* @module api/WEBApi
* @version 21.00
*/
export default class WEBApi {

    /**
    * Constructs a new WEBApi. 
    * @alias module:api/WEBApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the protocolWebGetArgs operation.
     * @callback module:api/WEBApi~protocolWebGetArgsCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show the agent's WEB argument structure
     * Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap
     * @param {Number} agentNum Agent to show the WEB argument structure
     * @param {module:api/WEBApi~protocolWebGetArgsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    protocolWebGetArgs(agentNum, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolWebGetArgs");
      }

      let pathParams = {
        'agentNum': agentNum
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/web/get/args', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolWebGetConfig operation.
     * @callback module:api/WEBApi~protocolWebGetConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ConfigWEB} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show the agent's WEB configuration
     * Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap
     * @param {Number} agentNum Agent to show the WEB configuration
     * @param {module:api/WEBApi~protocolWebGetConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ConfigWEB}
     */
    protocolWebGetConfig(agentNum, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolWebGetConfig");
      }

      let pathParams = {
        'agentNum': agentNum
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ConfigWEB;
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/web/get/config', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolWebGetStatistics operation.
     * @callback module:api/WEBApi~protocolWebGetStatisticsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<Number>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show the agent's WEB statistics
     * Statistics of fields indicated in the headers
     * @param {Number} agentNum Agent to show WEB statistics
     * @param {module:api/WEBApi~protocolWebGetStatisticsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Number>}
     */
    protocolWebGetStatistics(agentNum, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolWebGetStatistics");
      }

      let pathParams = {
        'agentNum': agentNum
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ['Number'];
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/web/get/statistics', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolWebGetStatsHdr operation.
     * @callback module:api/WEBApi~protocolWebGetStatsHdrCallback
     * @param {String} error Error message, if any.
     * @param {Array.<String>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show the WEB statistics headers
     * The headers of statistics fields
     * @param {module:api/WEBApi~protocolWebGetStatsHdrCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<String>}
     */
    protocolWebGetStatsHdr(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ['String'];
      return this.apiClient.callApi(
        '/mimic/protocol/msg/web/get/stats_hdr', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolWebGetTrace operation.
     * @callback module:api/WEBApi~protocolWebGetTraceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ConfigWEB} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show the agent's WEB traffic tracing
     * Trace 1 means enabled, 0 means not
     * @param {Number} agentNum Agent to show whether WEB tracing is enabled
     * @param {module:api/WEBApi~protocolWebGetTraceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ConfigWEB}
     */
    protocolWebGetTrace(agentNum, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolWebGetTrace");
      }

      let pathParams = {
        'agentNum': agentNum
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ConfigWEB;
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/web/get/trace', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolWebPortAdd operation.
     * @callback module:api/WEBApi~protocolWebPortAddCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add the agent's WEB port
     * Add port
     * @param {Number} agentNum Agent to add WEB port
     * @param {Number} port TCP port
     * @param {module:api/WEBApi~protocolWebPortAddCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    protocolWebPortAdd(agentNum, port, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolWebPortAdd");
      }
      // verify the required parameter 'port' is set
      if (port === undefined || port === null) {
        throw new Error("Missing the required parameter 'port' when calling protocolWebPortAdd");
      }

      let pathParams = {
        'agentNum': agentNum,
        'port': port
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/web/port/add/{port}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolWebPortExists operation.
     * @callback module:api/WEBApi~protocolWebPortExistsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<String>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show the agent's WEB port
     * Check the port. 1 means existing, 0 means not
     * @param {Number} agentNum Agent to show WEB configuration
     * @param {Number} port TCP port
     * @param {module:api/WEBApi~protocolWebPortExistsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<String>}
     */
    protocolWebPortExists(agentNum, port, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolWebPortExists");
      }
      // verify the required parameter 'port' is set
      if (port === undefined || port === null) {
        throw new Error("Missing the required parameter 'port' when calling protocolWebPortExists");
      }

      let pathParams = {
        'agentNum': agentNum,
        'port': port
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ['String'];
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/web/port/exists/{port}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolWebPortRemove operation.
     * @callback module:api/WEBApi~protocolWebPortRemoveCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove the agent's WEB port
     * Remove port
     * @param {Number} agentNum Agent to remove WEB port
     * @param {Number} port TCP port
     * @param {module:api/WEBApi~protocolWebPortRemoveCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    protocolWebPortRemove(agentNum, port, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolWebPortRemove");
      }
      // verify the required parameter 'port' is set
      if (port === undefined || port === null) {
        throw new Error("Missing the required parameter 'port' when calling protocolWebPortRemove");
      }

      let pathParams = {
        'agentNum': agentNum,
        'port': port
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/web/port/remove/{port}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolWebPortSet operation.
     * @callback module:api/WEBApi~protocolWebPortSetCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set the agent's WEB port attribute
     * Set port
     * @param {Number} agentNum Agent to set WEB port
     * @param {Number} port TCP port
     * @param {String} protocol Encryption or related protocol
     * @param {String} version Encryption or related protocol version
     * @param {module:api/WEBApi~protocolWebPortSetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    protocolWebPortSet(agentNum, port, protocol, version, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolWebPortSet");
      }
      // verify the required parameter 'port' is set
      if (port === undefined || port === null) {
        throw new Error("Missing the required parameter 'port' when calling protocolWebPortSet");
      }
      // verify the required parameter 'protocol' is set
      if (protocol === undefined || protocol === null) {
        throw new Error("Missing the required parameter 'protocol' when calling protocolWebPortSet");
      }
      // verify the required parameter 'version' is set
      if (version === undefined || version === null) {
        throw new Error("Missing the required parameter 'version' when calling protocolWebPortSet");
      }

      let pathParams = {
        'agentNum': agentNum,
        'port': port,
        'protocol': protocol,
        'version': version
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/web/port/set/{port}/{protocol}/{version}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolWebPortStart operation.
     * @callback module:api/WEBApi~protocolWebPortStartCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Start the agent's WEB port
     * Start port
     * @param {Number} agentNum Agent to start WEB port
     * @param {Number} port TCP port
     * @param {module:api/WEBApi~protocolWebPortStartCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    protocolWebPortStart(agentNum, port, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolWebPortStart");
      }
      // verify the required parameter 'port' is set
      if (port === undefined || port === null) {
        throw new Error("Missing the required parameter 'port' when calling protocolWebPortStart");
      }

      let pathParams = {
        'agentNum': agentNum,
        'port': port
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/web/port/start/{port}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolWebPortStop operation.
     * @callback module:api/WEBApi~protocolWebPortStopCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Stop the agent's WEB port
     * Stop port
     * @param {Number} agentNum Agent to stop WEB port
     * @param {Number} port TCP port
     * @param {module:api/WEBApi~protocolWebPortStopCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    protocolWebPortStop(agentNum, port, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolWebPortStop");
      }
      // verify the required parameter 'port' is set
      if (port === undefined || port === null) {
        throw new Error("Missing the required parameter 'port' when calling protocolWebPortStop");
      }

      let pathParams = {
        'agentNum': agentNum,
        'port': port
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/web/port/stop/{port}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolWebSetConfig operation.
     * @callback module:api/WEBApi~protocolWebSetConfigCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set the agent's WEB configuration
     * Agent's WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap
     * @param {Number} agentNum Agent to set the WEB configuration
     * @param {String} argument Parameter to set the WEB configuration
     * @param {String} value Value to set the WEB configuration
     * @param {module:api/WEBApi~protocolWebSetConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    protocolWebSetConfig(agentNum, argument, value, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolWebSetConfig");
      }
      // verify the required parameter 'argument' is set
      if (argument === undefined || argument === null) {
        throw new Error("Missing the required parameter 'argument' when calling protocolWebSetConfig");
      }
      // verify the required parameter 'value' is set
      if (value === undefined || value === null) {
        throw new Error("Missing the required parameter 'value' when calling protocolWebSetConfig");
      }

      let pathParams = {
        'agentNum': agentNum,
        'argument': argument,
        'value': value
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/web/set/config/{argument}/{value}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolWebSetTrace operation.
     * @callback module:api/WEBApi~protocolWebSetTraceCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set the agent's WEB traffic tracing
     * 1 to enable, 0 to disable
     * @param {Number} agentNum Agent to set the WEB tracing
     * @param {String} enableOrNot Value to set the WEB tracing
     * @param {module:api/WEBApi~protocolWebSetTraceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    protocolWebSetTrace(agentNum, enableOrNot, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolWebSetTrace");
      }
      // verify the required parameter 'enableOrNot' is set
      if (enableOrNot === undefined || enableOrNot === null) {
        throw new Error("Missing the required parameter 'enableOrNot' when calling protocolWebSetTrace");
      }

      let pathParams = {
        'agentNum': agentNum,
        'enableOrNot': enableOrNot
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['basicAuth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/web/set/trace/{enableOrNot}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
