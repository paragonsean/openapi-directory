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


import ApiClient from "../ApiClient";
import CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest from '../model/CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest';
import GetNetworkApplianceTrafficShapingUplinkBandwidth200Response from '../model/GetNetworkApplianceTrafficShapingUplinkBandwidth200Response';
import GetNetworkApplianceTrafficShapingUplinkSelection200Response from '../model/GetNetworkApplianceTrafficShapingUplinkSelection200Response';
import UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest from '../model/UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest';
import UpdateNetworkApplianceTrafficShapingRequest from '../model/UpdateNetworkApplianceTrafficShapingRequest';
import UpdateNetworkApplianceTrafficShapingRulesRequest from '../model/UpdateNetworkApplianceTrafficShapingRulesRequest';
import UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest from '../model/UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest';
import UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest from '../model/UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest';
import UpdateNetworkWirelessSsidTrafficShapingRulesRequest from '../model/UpdateNetworkWirelessSsidTrafficShapingRulesRequest';

/**
* TrafficShaping service.
* @module api/TrafficShapingApi
* @version 1.32.0
*/
export default class TrafficShapingApi {

    /**
    * Constructs a new TrafficShapingApi. 
    * @alias module:api/TrafficShapingApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createNetworkApplianceTrafficShapingCustomPerformanceClass_1 operation.
     * @callback module:api/TrafficShapingApi~createNetworkApplianceTrafficShapingCustomPerformanceClass_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a custom performance class for an MX network
     * Add a custom performance class for an MX network
     * @param {String} networkId 
     * @param {module:model/CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest} createNetworkApplianceTrafficShapingCustomPerformanceClassRequest 
     * @param {module:api/TrafficShapingApi~createNetworkApplianceTrafficShapingCustomPerformanceClass_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    createNetworkApplianceTrafficShapingCustomPerformanceClass_1(networkId, createNetworkApplianceTrafficShapingCustomPerformanceClassRequest, callback) {
      let postBody = createNetworkApplianceTrafficShapingCustomPerformanceClassRequest;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling createNetworkApplianceTrafficShapingCustomPerformanceClass_1");
      }
      // verify the required parameter 'createNetworkApplianceTrafficShapingCustomPerformanceClassRequest' is set
      if (createNetworkApplianceTrafficShapingCustomPerformanceClassRequest === undefined || createNetworkApplianceTrafficShapingCustomPerformanceClassRequest === null) {
        throw new Error("Missing the required parameter 'createNetworkApplianceTrafficShapingCustomPerformanceClassRequest' when calling createNetworkApplianceTrafficShapingCustomPerformanceClass_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteNetworkApplianceTrafficShapingCustomPerformanceClass_1 operation.
     * @callback module:api/TrafficShapingApi~deleteNetworkApplianceTrafficShapingCustomPerformanceClass_1Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a custom performance class from an MX network
     * Delete a custom performance class from an MX network
     * @param {String} networkId 
     * @param {String} customPerformanceClassId 
     * @param {module:api/TrafficShapingApi~deleteNetworkApplianceTrafficShapingCustomPerformanceClass_1Callback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteNetworkApplianceTrafficShapingCustomPerformanceClass_1(networkId, customPerformanceClassId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling deleteNetworkApplianceTrafficShapingCustomPerformanceClass_1");
      }
      // verify the required parameter 'customPerformanceClassId' is set
      if (customPerformanceClassId === undefined || customPerformanceClassId === null) {
        throw new Error("Missing the required parameter 'customPerformanceClassId' when calling deleteNetworkApplianceTrafficShapingCustomPerformanceClass_1");
      }

      let pathParams = {
        'networkId': networkId,
        'customPerformanceClassId': customPerformanceClassId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkApplianceTrafficShapingCustomPerformanceClass_1 operation.
     * @callback module:api/TrafficShapingApi~getNetworkApplianceTrafficShapingCustomPerformanceClass_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return a custom performance class for an MX network
     * Return a custom performance class for an MX network
     * @param {String} networkId 
     * @param {String} customPerformanceClassId 
     * @param {module:api/TrafficShapingApi~getNetworkApplianceTrafficShapingCustomPerformanceClass_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getNetworkApplianceTrafficShapingCustomPerformanceClass_1(networkId, customPerformanceClassId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkApplianceTrafficShapingCustomPerformanceClass_1");
      }
      // verify the required parameter 'customPerformanceClassId' is set
      if (customPerformanceClassId === undefined || customPerformanceClassId === null) {
        throw new Error("Missing the required parameter 'customPerformanceClassId' when calling getNetworkApplianceTrafficShapingCustomPerformanceClass_1");
      }

      let pathParams = {
        'networkId': networkId,
        'customPerformanceClassId': customPerformanceClassId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkApplianceTrafficShapingCustomPerformanceClasses_1 operation.
     * @callback module:api/TrafficShapingApi~getNetworkApplianceTrafficShapingCustomPerformanceClasses_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List all custom performance classes for an MX network
     * List all custom performance classes for an MX network
     * @param {String} networkId 
     * @param {module:api/TrafficShapingApi~getNetworkApplianceTrafficShapingCustomPerformanceClasses_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getNetworkApplianceTrafficShapingCustomPerformanceClasses_1(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkApplianceTrafficShapingCustomPerformanceClasses_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Object];
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkApplianceTrafficShapingRules_1 operation.
     * @callback module:api/TrafficShapingApi~getNetworkApplianceTrafficShapingRules_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Display the traffic shaping settings rules for an MX network
     * Display the traffic shaping settings rules for an MX network
     * @param {String} networkId 
     * @param {module:api/TrafficShapingApi~getNetworkApplianceTrafficShapingRules_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getNetworkApplianceTrafficShapingRules_1(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkApplianceTrafficShapingRules_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/trafficShaping/rules', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkApplianceTrafficShapingUplinkBandwidth_1 operation.
     * @callback module:api/TrafficShapingApi~getNetworkApplianceTrafficShapingUplinkBandwidth_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkApplianceTrafficShapingUplinkBandwidth200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns the uplink bandwidth limits for your MX network
     * Returns the uplink bandwidth limits for your MX network. This may not reflect the affected device's hardware capabilities.  For more information on your device's hardware capabilities, please consult our MX Family Datasheet - [https://meraki.cisco.com/product-collateral/mx-family-datasheet/?file]
     * @param {String} networkId 
     * @param {module:api/TrafficShapingApi~getNetworkApplianceTrafficShapingUplinkBandwidth_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkApplianceTrafficShapingUplinkBandwidth200Response}
     */
    getNetworkApplianceTrafficShapingUplinkBandwidth_1(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkApplianceTrafficShapingUplinkBandwidth_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetNetworkApplianceTrafficShapingUplinkBandwidth200Response;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/trafficShaping/uplinkBandwidth', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkApplianceTrafficShapingUplinkSelection_1 operation.
     * @callback module:api/TrafficShapingApi~getNetworkApplianceTrafficShapingUplinkSelection_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkApplianceTrafficShapingUplinkSelection200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show uplink selection settings for an MX network
     * Show uplink selection settings for an MX network
     * @param {String} networkId 
     * @param {module:api/TrafficShapingApi~getNetworkApplianceTrafficShapingUplinkSelection_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkApplianceTrafficShapingUplinkSelection200Response}
     */
    getNetworkApplianceTrafficShapingUplinkSelection_1(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkApplianceTrafficShapingUplinkSelection_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetNetworkApplianceTrafficShapingUplinkSelection200Response;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/trafficShaping/uplinkSelection', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkApplianceTrafficShaping_1 operation.
     * @callback module:api/TrafficShapingApi~getNetworkApplianceTrafficShaping_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Display the traffic shaping settings for an MX network
     * Display the traffic shaping settings for an MX network
     * @param {String} networkId 
     * @param {module:api/TrafficShapingApi~getNetworkApplianceTrafficShaping_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getNetworkApplianceTrafficShaping_1(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkApplianceTrafficShaping_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/trafficShaping', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkTrafficShapingApplicationCategories_1 operation.
     * @callback module:api/TrafficShapingApi~getNetworkTrafficShapingApplicationCategories_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns the application categories for traffic shaping rules.
     * Returns the application categories for traffic shaping rules.
     * @param {String} networkId 
     * @param {module:api/TrafficShapingApi~getNetworkTrafficShapingApplicationCategories_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getNetworkTrafficShapingApplicationCategories_1(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkTrafficShapingApplicationCategories_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/trafficShaping/applicationCategories', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkTrafficShapingDscpTaggingOptions_1 operation.
     * @callback module:api/TrafficShapingApi~getNetworkTrafficShapingDscpTaggingOptions_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns the available DSCP tagging options for your traffic shaping rules.
     * Returns the available DSCP tagging options for your traffic shaping rules.
     * @param {String} networkId 
     * @param {module:api/TrafficShapingApi~getNetworkTrafficShapingDscpTaggingOptions_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getNetworkTrafficShapingDscpTaggingOptions_1(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkTrafficShapingDscpTaggingOptions_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Object];
      return this.apiClient.callApi(
        '/networks/{networkId}/trafficShaping/dscpTaggingOptions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkWirelessSsidTrafficShapingRules_2 operation.
     * @callback module:api/TrafficShapingApi~getNetworkWirelessSsidTrafficShapingRules_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Display the traffic shaping settings for a SSID on an MR network
     * Display the traffic shaping settings for a SSID on an MR network
     * @param {String} networkId 
     * @param {String} number 
     * @param {module:api/TrafficShapingApi~getNetworkWirelessSsidTrafficShapingRules_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getNetworkWirelessSsidTrafficShapingRules_2(networkId, number, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkWirelessSsidTrafficShapingRules_2");
      }
      // verify the required parameter 'number' is set
      if (number === undefined || number === null) {
        throw new Error("Missing the required parameter 'number' when calling getNetworkWirelessSsidTrafficShapingRules_2");
      }

      let pathParams = {
        'networkId': networkId,
        'number': number
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkApplianceTrafficShapingCustomPerformanceClass_1 operation.
     * @callback module:api/TrafficShapingApi~updateNetworkApplianceTrafficShapingCustomPerformanceClass_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a custom performance class for an MX network
     * Update a custom performance class for an MX network
     * @param {String} networkId 
     * @param {String} customPerformanceClassId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest} [updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest] 
     * @param {module:api/TrafficShapingApi~updateNetworkApplianceTrafficShapingCustomPerformanceClass_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateNetworkApplianceTrafficShapingCustomPerformanceClass_1(networkId, customPerformanceClassId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkApplianceTrafficShapingCustomPerformanceClassRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkApplianceTrafficShapingCustomPerformanceClass_1");
      }
      // verify the required parameter 'customPerformanceClassId' is set
      if (customPerformanceClassId === undefined || customPerformanceClassId === null) {
        throw new Error("Missing the required parameter 'customPerformanceClassId' when calling updateNetworkApplianceTrafficShapingCustomPerformanceClass_1");
      }

      let pathParams = {
        'networkId': networkId,
        'customPerformanceClassId': customPerformanceClassId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkApplianceTrafficShapingRules_1 operation.
     * @callback module:api/TrafficShapingApi~updateNetworkApplianceTrafficShapingRules_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the traffic shaping settings rules for an MX network
     * Update the traffic shaping settings rules for an MX network
     * @param {String} networkId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkApplianceTrafficShapingRulesRequest} [updateNetworkApplianceTrafficShapingRulesRequest] 
     * @param {module:api/TrafficShapingApi~updateNetworkApplianceTrafficShapingRules_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateNetworkApplianceTrafficShapingRules_1(networkId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkApplianceTrafficShapingRulesRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkApplianceTrafficShapingRules_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/trafficShaping/rules', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkApplianceTrafficShapingUplinkBandwidth_1 operation.
     * @callback module:api/TrafficShapingApi~updateNetworkApplianceTrafficShapingUplinkBandwidth_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates the uplink bandwidth settings for your MX network.
     * Updates the uplink bandwidth settings for your MX network.
     * @param {String} networkId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest} [updateNetworkApplianceTrafficShapingUplinkBandwidthRequest] 
     * @param {module:api/TrafficShapingApi~updateNetworkApplianceTrafficShapingUplinkBandwidth_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateNetworkApplianceTrafficShapingUplinkBandwidth_1(networkId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkApplianceTrafficShapingUplinkBandwidthRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkApplianceTrafficShapingUplinkBandwidth_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/trafficShaping/uplinkBandwidth', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkApplianceTrafficShapingUplinkSelection_1 operation.
     * @callback module:api/TrafficShapingApi~updateNetworkApplianceTrafficShapingUplinkSelection_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkApplianceTrafficShapingUplinkSelection200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update uplink selection settings for an MX network
     * Update uplink selection settings for an MX network
     * @param {String} networkId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest} [updateNetworkApplianceTrafficShapingUplinkSelectionRequest] 
     * @param {module:api/TrafficShapingApi~updateNetworkApplianceTrafficShapingUplinkSelection_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkApplianceTrafficShapingUplinkSelection200Response}
     */
    updateNetworkApplianceTrafficShapingUplinkSelection_1(networkId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkApplianceTrafficShapingUplinkSelectionRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkApplianceTrafficShapingUplinkSelection_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetNetworkApplianceTrafficShapingUplinkSelection200Response;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/trafficShaping/uplinkSelection', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkApplianceTrafficShaping_1 operation.
     * @callback module:api/TrafficShapingApi~updateNetworkApplianceTrafficShaping_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the traffic shaping settings for an MX network
     * Update the traffic shaping settings for an MX network
     * @param {String} networkId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkApplianceTrafficShapingRequest} [updateNetworkApplianceTrafficShapingRequest] 
     * @param {module:api/TrafficShapingApi~updateNetworkApplianceTrafficShaping_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateNetworkApplianceTrafficShaping_1(networkId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkApplianceTrafficShapingRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkApplianceTrafficShaping_1");
      }

      let pathParams = {
        'networkId': networkId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/appliance/trafficShaping', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkWirelessSsidTrafficShapingRules_2 operation.
     * @callback module:api/TrafficShapingApi~updateNetworkWirelessSsidTrafficShapingRules_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the traffic shaping settings for an SSID on an MR network
     * Update the traffic shaping settings for an SSID on an MR network
     * @param {String} networkId 
     * @param {String} number 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkWirelessSsidTrafficShapingRulesRequest} [updateNetworkWirelessSsidTrafficShapingRulesRequest] 
     * @param {module:api/TrafficShapingApi~updateNetworkWirelessSsidTrafficShapingRules_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateNetworkWirelessSsidTrafficShapingRules_2(networkId, number, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkWirelessSsidTrafficShapingRulesRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkWirelessSsidTrafficShapingRules_2");
      }
      // verify the required parameter 'number' is set
      if (number === undefined || number === null) {
        throw new Error("Missing the required parameter 'number' when calling updateNetworkWirelessSsidTrafficShapingRules_2");
      }

      let pathParams = {
        'networkId': networkId,
        'number': number
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
