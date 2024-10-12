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
import ConfigIPMI from '../model/ConfigIPMI';

/**
* IPMI service.
* @module api/IPMIApi
* @version 21.00
*/
export default class IPMIApi {

    /**
    * Constructs a new IPMIApi. 
    * @alias module:api/IPMIApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the protocolIpmiGetArgs operation.
     * @callback module:api/IPMIApi~protocolIpmiGetArgsCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show the agent's IPMI argument structure
     * Agent's IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap
     * @param {Number} agentNum Agent to show the IPMI argument structure
     * @param {module:api/IPMIApi~protocolIpmiGetArgsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    protocolIpmiGetArgs(agentNum, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolIpmiGetArgs");
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
        '/mimic/agent/{agentNum}/protocol/msg/ipmi/get/args', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolIpmiGetAttr operation.
     * @callback module:api/IPMIApi~protocolIpmiGetAttrCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show the outgoing message's attributes
     * Attribute can be working_authtype ,session_id, outbound_seq, inbound_seq , field_N
     * @param {Number} agentNum Agent to set the IPMI tracing
     * @param {String} attr Attribute
     * @param {module:api/IPMIApi~protocolIpmiGetAttrCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    protocolIpmiGetAttr(agentNum, attr, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolIpmiGetAttr");
      }
      // verify the required parameter 'attr' is set
      if (attr === undefined || attr === null) {
        throw new Error("Missing the required parameter 'attr' when calling protocolIpmiGetAttr");
      }

      let pathParams = {
        'agentNum': agentNum,
        'attr': attr
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
        '/mimic/agent/{agentNum}/protocol/msg/ipmi/get/{attr}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolIpmiGetConfig operation.
     * @callback module:api/IPMIApi~protocolIpmiGetConfigCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ConfigIPMI} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show the agent's IPMI configuration
     * Agent's IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap
     * @param {Number} agentNum Agent to show the IPMI configuration
     * @param {module:api/IPMIApi~protocolIpmiGetConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ConfigIPMI}
     */
    protocolIpmiGetConfig(agentNum, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolIpmiGetConfig");
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
      let returnType = ConfigIPMI;
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/ipmi/get/config', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolIpmiGetStatistics operation.
     * @callback module:api/IPMIApi~protocolIpmiGetStatisticsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<Number>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show the agent's IPMI statistics
     * Statistics of fields indicated in the headers
     * @param {Number} agentNum Agent to show IPMI statistics
     * @param {module:api/IPMIApi~protocolIpmiGetStatisticsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Number>}
     */
    protocolIpmiGetStatistics(agentNum, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolIpmiGetStatistics");
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
        '/mimic/agent/{agentNum}/protocol/msg/ipmi/get/statistics', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolIpmiGetStatsHdr operation.
     * @callback module:api/IPMIApi~protocolIpmiGetStatsHdrCallback
     * @param {String} error Error message, if any.
     * @param {Array.<String>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show the IPMI statistics headers
     * The headers of statistics fields
     * @param {module:api/IPMIApi~protocolIpmiGetStatsHdrCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<String>}
     */
    protocolIpmiGetStatsHdr(callback) {
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
        '/mimic/protocol/msg/ipmi/get/stats_hdr', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolIpmiGetTrace operation.
     * @callback module:api/IPMIApi~protocolIpmiGetTraceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ConfigIPMI} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show the agent's IPMI traffic tracing
     * Trace 1 means enabled, 0 means not
     * @param {Number} agentNum Agent to show whether IPMI tracing is enabled
     * @param {module:api/IPMIApi~protocolIpmiGetTraceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ConfigIPMI}
     */
    protocolIpmiGetTrace(agentNum, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolIpmiGetTrace");
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
      let returnType = ConfigIPMI;
      return this.apiClient.callApi(
        '/mimic/agent/{agentNum}/protocol/msg/ipmi/get/trace', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolIpmiSetAttr operation.
     * @callback module:api/IPMIApi~protocolIpmiSetAttrCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set the outgoing message's attributes
     * Attribute can be working_authtype ,session_id, outbound_seq, inbound_seq , field_N
     * @param {Number} agentNum Agent to set the IPMI tracing
     * @param {String} attr Attribute
     * @param {String} value 
     * @param {module:api/IPMIApi~protocolIpmiSetAttrCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    protocolIpmiSetAttr(agentNum, attr, value, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolIpmiSetAttr");
      }
      // verify the required parameter 'attr' is set
      if (attr === undefined || attr === null) {
        throw new Error("Missing the required parameter 'attr' when calling protocolIpmiSetAttr");
      }
      // verify the required parameter 'value' is set
      if (value === undefined || value === null) {
        throw new Error("Missing the required parameter 'value' when calling protocolIpmiSetAttr");
      }

      let pathParams = {
        'agentNum': agentNum,
        'attr': attr,
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
        '/mimic/agent/{agentNum}/protocol/msg/ipmi/set/{attr}/{value}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolIpmiSetConfig operation.
     * @callback module:api/IPMIApi~protocolIpmiSetConfigCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set the agent's IPMI configuration
     * Agent's IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap
     * @param {Number} agentNum Agent to set the IPMI configuration
     * @param {String} argument Parameter to set the IPMI configuration
     * @param {String} value Value to set the IPMI configuration
     * @param {module:api/IPMIApi~protocolIpmiSetConfigCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    protocolIpmiSetConfig(agentNum, argument, value, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolIpmiSetConfig");
      }
      // verify the required parameter 'argument' is set
      if (argument === undefined || argument === null) {
        throw new Error("Missing the required parameter 'argument' when calling protocolIpmiSetConfig");
      }
      // verify the required parameter 'value' is set
      if (value === undefined || value === null) {
        throw new Error("Missing the required parameter 'value' when calling protocolIpmiSetConfig");
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
        '/mimic/agent/{agentNum}/protocol/msg/ipmi/set/config/{argument}/{value}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the protocolIpmiSetTrace operation.
     * @callback module:api/IPMIApi~protocolIpmiSetTraceCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set the agent's IPMI traffic tracing
     * 1 to enable, 0 to disable
     * @param {Number} agentNum Agent to set the IPMI tracing
     * @param {String} enableOrNot Value to set the IPMI tracing
     * @param {module:api/IPMIApi~protocolIpmiSetTraceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    protocolIpmiSetTrace(agentNum, enableOrNot, callback) {
      let postBody = null;
      // verify the required parameter 'agentNum' is set
      if (agentNum === undefined || agentNum === null) {
        throw new Error("Missing the required parameter 'agentNum' when calling protocolIpmiSetTrace");
      }
      // verify the required parameter 'enableOrNot' is set
      if (enableOrNot === undefined || enableOrNot === null) {
        throw new Error("Missing the required parameter 'enableOrNot' when calling protocolIpmiSetTrace");
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
        '/mimic/agent/{agentNum}/protocol/msg/ipmi/set/trace/{enableOrNot}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
