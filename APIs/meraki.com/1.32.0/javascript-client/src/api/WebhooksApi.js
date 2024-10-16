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
import CreateNetworkWebhooksHttpServerRequest from '../model/CreateNetworkWebhooksHttpServerRequest';
import CreateNetworkWebhooksPayloadTemplateRequest from '../model/CreateNetworkWebhooksPayloadTemplateRequest';
import CreateNetworkWebhooksWebhookTest201Response from '../model/CreateNetworkWebhooksWebhookTest201Response';
import CreateNetworkWebhooksWebhookTestRequest from '../model/CreateNetworkWebhooksWebhookTestRequest';
import GetNetworkWebhooksHttpServers200ResponseInner from '../model/GetNetworkWebhooksHttpServers200ResponseInner';
import GetNetworkWebhooksPayloadTemplates200ResponseInner from '../model/GetNetworkWebhooksPayloadTemplates200ResponseInner';
import GetOrganizationWebhooksLogs200ResponseInner from '../model/GetOrganizationWebhooksLogs200ResponseInner';
import UpdateNetworkWebhooksHttpServerRequest from '../model/UpdateNetworkWebhooksHttpServerRequest';
import UpdateNetworkWebhooksPayloadTemplateRequest from '../model/UpdateNetworkWebhooksPayloadTemplateRequest';

/**
* Webhooks service.
* @module api/WebhooksApi
* @version 1.32.0
*/
export default class WebhooksApi {

    /**
    * Constructs a new WebhooksApi. 
    * @alias module:api/WebhooksApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createNetworkWebhooksHttpServer_1 operation.
     * @callback module:api/WebhooksApi~createNetworkWebhooksHttpServer_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkWebhooksHttpServers200ResponseInner} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add an HTTP server to a network
     * Add an HTTP server to a network
     * @param {String} networkId 
     * @param {module:model/CreateNetworkWebhooksHttpServerRequest} createNetworkWebhooksHttpServerRequest 
     * @param {module:api/WebhooksApi~createNetworkWebhooksHttpServer_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkWebhooksHttpServers200ResponseInner}
     */
    createNetworkWebhooksHttpServer_1(networkId, createNetworkWebhooksHttpServerRequest, callback) {
      let postBody = createNetworkWebhooksHttpServerRequest;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling createNetworkWebhooksHttpServer_1");
      }
      // verify the required parameter 'createNetworkWebhooksHttpServerRequest' is set
      if (createNetworkWebhooksHttpServerRequest === undefined || createNetworkWebhooksHttpServerRequest === null) {
        throw new Error("Missing the required parameter 'createNetworkWebhooksHttpServerRequest' when calling createNetworkWebhooksHttpServer_1");
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
      let returnType = GetNetworkWebhooksHttpServers200ResponseInner;
      return this.apiClient.callApi(
        '/networks/{networkId}/webhooks/httpServers', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createNetworkWebhooksPayloadTemplate_1 operation.
     * @callback module:api/WebhooksApi~createNetworkWebhooksPayloadTemplate_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkWebhooksPayloadTemplates200ResponseInner} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a webhook payload template for a network
     * Create a webhook payload template for a network
     * @param {String} networkId 
     * @param {module:model/CreateNetworkWebhooksPayloadTemplateRequest} createNetworkWebhooksPayloadTemplateRequest 
     * @param {module:api/WebhooksApi~createNetworkWebhooksPayloadTemplate_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkWebhooksPayloadTemplates200ResponseInner}
     */
    createNetworkWebhooksPayloadTemplate_1(networkId, createNetworkWebhooksPayloadTemplateRequest, callback) {
      let postBody = createNetworkWebhooksPayloadTemplateRequest;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling createNetworkWebhooksPayloadTemplate_1");
      }
      // verify the required parameter 'createNetworkWebhooksPayloadTemplateRequest' is set
      if (createNetworkWebhooksPayloadTemplateRequest === undefined || createNetworkWebhooksPayloadTemplateRequest === null) {
        throw new Error("Missing the required parameter 'createNetworkWebhooksPayloadTemplateRequest' when calling createNetworkWebhooksPayloadTemplate_1");
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
      let returnType = GetNetworkWebhooksPayloadTemplates200ResponseInner;
      return this.apiClient.callApi(
        '/networks/{networkId}/webhooks/payloadTemplates', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createNetworkWebhooksWebhookTest_1 operation.
     * @callback module:api/WebhooksApi~createNetworkWebhooksWebhookTest_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateNetworkWebhooksWebhookTest201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Send a test webhook for a network
     * Send a test webhook for a network
     * @param {String} networkId 
     * @param {module:model/CreateNetworkWebhooksWebhookTestRequest} createNetworkWebhooksWebhookTestRequest 
     * @param {module:api/WebhooksApi~createNetworkWebhooksWebhookTest_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateNetworkWebhooksWebhookTest201Response}
     */
    createNetworkWebhooksWebhookTest_1(networkId, createNetworkWebhooksWebhookTestRequest, callback) {
      let postBody = createNetworkWebhooksWebhookTestRequest;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling createNetworkWebhooksWebhookTest_1");
      }
      // verify the required parameter 'createNetworkWebhooksWebhookTestRequest' is set
      if (createNetworkWebhooksWebhookTestRequest === undefined || createNetworkWebhooksWebhookTestRequest === null) {
        throw new Error("Missing the required parameter 'createNetworkWebhooksWebhookTestRequest' when calling createNetworkWebhooksWebhookTest_1");
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
      let returnType = CreateNetworkWebhooksWebhookTest201Response;
      return this.apiClient.callApi(
        '/networks/{networkId}/webhooks/webhookTests', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteNetworkWebhooksHttpServer_1 operation.
     * @callback module:api/WebhooksApi~deleteNetworkWebhooksHttpServer_1Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an HTTP server from a network
     * Delete an HTTP server from a network
     * @param {String} networkId 
     * @param {String} httpServerId 
     * @param {module:api/WebhooksApi~deleteNetworkWebhooksHttpServer_1Callback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteNetworkWebhooksHttpServer_1(networkId, httpServerId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling deleteNetworkWebhooksHttpServer_1");
      }
      // verify the required parameter 'httpServerId' is set
      if (httpServerId === undefined || httpServerId === null) {
        throw new Error("Missing the required parameter 'httpServerId' when calling deleteNetworkWebhooksHttpServer_1");
      }

      let pathParams = {
        'networkId': networkId,
        'httpServerId': httpServerId
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
        '/networks/{networkId}/webhooks/httpServers/{httpServerId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteNetworkWebhooksPayloadTemplate_1 operation.
     * @callback module:api/WebhooksApi~deleteNetworkWebhooksPayloadTemplate_1Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Destroy a webhook payload template for a network
     * Destroy a webhook payload template for a network. Does not work for included templates ('wpt_00001', 'wpt_00002', 'wpt_00003', 'wpt_00004', 'wpt_00005' or 'wpt_00006')
     * @param {String} networkId 
     * @param {String} payloadTemplateId 
     * @param {module:api/WebhooksApi~deleteNetworkWebhooksPayloadTemplate_1Callback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteNetworkWebhooksPayloadTemplate_1(networkId, payloadTemplateId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling deleteNetworkWebhooksPayloadTemplate_1");
      }
      // verify the required parameter 'payloadTemplateId' is set
      if (payloadTemplateId === undefined || payloadTemplateId === null) {
        throw new Error("Missing the required parameter 'payloadTemplateId' when calling deleteNetworkWebhooksPayloadTemplate_1");
      }

      let pathParams = {
        'networkId': networkId,
        'payloadTemplateId': payloadTemplateId
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
        '/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkWebhooksHttpServer_1 operation.
     * @callback module:api/WebhooksApi~getNetworkWebhooksHttpServer_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkWebhooksHttpServers200ResponseInner} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return an HTTP server for a network
     * Return an HTTP server for a network
     * @param {String} networkId 
     * @param {String} httpServerId 
     * @param {module:api/WebhooksApi~getNetworkWebhooksHttpServer_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkWebhooksHttpServers200ResponseInner}
     */
    getNetworkWebhooksHttpServer_1(networkId, httpServerId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkWebhooksHttpServer_1");
      }
      // verify the required parameter 'httpServerId' is set
      if (httpServerId === undefined || httpServerId === null) {
        throw new Error("Missing the required parameter 'httpServerId' when calling getNetworkWebhooksHttpServer_1");
      }

      let pathParams = {
        'networkId': networkId,
        'httpServerId': httpServerId
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
      let returnType = GetNetworkWebhooksHttpServers200ResponseInner;
      return this.apiClient.callApi(
        '/networks/{networkId}/webhooks/httpServers/{httpServerId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkWebhooksHttpServers_1 operation.
     * @callback module:api/WebhooksApi~getNetworkWebhooksHttpServers_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetNetworkWebhooksHttpServers200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the HTTP servers for a network
     * List the HTTP servers for a network
     * @param {String} networkId 
     * @param {module:api/WebhooksApi~getNetworkWebhooksHttpServers_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetNetworkWebhooksHttpServers200ResponseInner>}
     */
    getNetworkWebhooksHttpServers_1(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkWebhooksHttpServers_1");
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
      let returnType = [GetNetworkWebhooksHttpServers200ResponseInner];
      return this.apiClient.callApi(
        '/networks/{networkId}/webhooks/httpServers', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkWebhooksPayloadTemplate_1 operation.
     * @callback module:api/WebhooksApi~getNetworkWebhooksPayloadTemplate_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkWebhooksPayloadTemplates200ResponseInner} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the webhook payload template for a network
     * Get the webhook payload template for a network
     * @param {String} networkId 
     * @param {String} payloadTemplateId 
     * @param {module:api/WebhooksApi~getNetworkWebhooksPayloadTemplate_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkWebhooksPayloadTemplates200ResponseInner}
     */
    getNetworkWebhooksPayloadTemplate_1(networkId, payloadTemplateId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkWebhooksPayloadTemplate_1");
      }
      // verify the required parameter 'payloadTemplateId' is set
      if (payloadTemplateId === undefined || payloadTemplateId === null) {
        throw new Error("Missing the required parameter 'payloadTemplateId' when calling getNetworkWebhooksPayloadTemplate_1");
      }

      let pathParams = {
        'networkId': networkId,
        'payloadTemplateId': payloadTemplateId
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
      let returnType = GetNetworkWebhooksPayloadTemplates200ResponseInner;
      return this.apiClient.callApi(
        '/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkWebhooksPayloadTemplates_1 operation.
     * @callback module:api/WebhooksApi~getNetworkWebhooksPayloadTemplates_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetNetworkWebhooksPayloadTemplates200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the webhook payload templates for a network
     * List the webhook payload templates for a network
     * @param {String} networkId 
     * @param {module:api/WebhooksApi~getNetworkWebhooksPayloadTemplates_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetNetworkWebhooksPayloadTemplates200ResponseInner>}
     */
    getNetworkWebhooksPayloadTemplates_1(networkId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkWebhooksPayloadTemplates_1");
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
      let returnType = [GetNetworkWebhooksPayloadTemplates200ResponseInner];
      return this.apiClient.callApi(
        '/networks/{networkId}/webhooks/payloadTemplates', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getNetworkWebhooksWebhookTest_1 operation.
     * @callback module:api/WebhooksApi~getNetworkWebhooksWebhookTest_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateNetworkWebhooksWebhookTest201Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return the status of a webhook test for a network
     * Return the status of a webhook test for a network
     * @param {String} networkId 
     * @param {String} webhookTestId 
     * @param {module:api/WebhooksApi~getNetworkWebhooksWebhookTest_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateNetworkWebhooksWebhookTest201Response}
     */
    getNetworkWebhooksWebhookTest_1(networkId, webhookTestId, callback) {
      let postBody = null;
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling getNetworkWebhooksWebhookTest_1");
      }
      // verify the required parameter 'webhookTestId' is set
      if (webhookTestId === undefined || webhookTestId === null) {
        throw new Error("Missing the required parameter 'webhookTestId' when calling getNetworkWebhooksWebhookTest_1");
      }

      let pathParams = {
        'networkId': networkId,
        'webhookTestId': webhookTestId
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
      let returnType = CreateNetworkWebhooksWebhookTest201Response;
      return this.apiClient.callApi(
        '/networks/{networkId}/webhooks/webhookTests/{webhookTestId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationWebhooksAlertTypes_1 operation.
     * @callback module:api/WebhooksApi~getOrganizationWebhooksAlertTypes_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return a list of alert types to be used with managing webhook alerts
     * Return a list of alert types to be used with managing webhook alerts
     * @param {String} organizationId 
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [productType] Filter sample alerts to a specific product type
     * @param {module:api/WebhooksApi~getOrganizationWebhooksAlertTypes_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getOrganizationWebhooksAlertTypes_1(organizationId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationWebhooksAlertTypes_1");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
        'productType': opts['productType']
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
        '/organizations/{organizationId}/webhooks/alertTypes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationWebhooksLogs_1 operation.
     * @callback module:api/WebhooksApi~getOrganizationWebhooksLogs_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetOrganizationWebhooksLogs200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return the log of webhook POSTs sent
     * Return the log of webhook POSTs sent
     * @param {String} organizationId 
     * @param {Object} opts Optional parameters
     * @param {String} [t0] The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
     * @param {String} [t1] The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
     * @param {Number} [timespan] The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
     * @param {Number} [perPage] The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
     * @param {String} [startingAfter] A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {String} [endingBefore] A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {String} [url] The URL the webhook was sent to
     * @param {module:api/WebhooksApi~getOrganizationWebhooksLogs_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetOrganizationWebhooksLogs200ResponseInner>}
     */
    getOrganizationWebhooksLogs_1(organizationId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationWebhooksLogs_1");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
        't0': opts['t0'],
        't1': opts['t1'],
        'timespan': opts['timespan'],
        'perPage': opts['perPage'],
        'startingAfter': opts['startingAfter'],
        'endingBefore': opts['endingBefore'],
        'url': opts['url']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [GetOrganizationWebhooksLogs200ResponseInner];
      return this.apiClient.callApi(
        '/organizations/{organizationId}/webhooks/logs', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkWebhooksHttpServer_1 operation.
     * @callback module:api/WebhooksApi~updateNetworkWebhooksHttpServer_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkWebhooksHttpServers200ResponseInner} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an HTTP server
     * Update an HTTP server. To change a URL, create a new HTTP server.
     * @param {String} networkId 
     * @param {String} httpServerId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkWebhooksHttpServerRequest} [updateNetworkWebhooksHttpServerRequest] 
     * @param {module:api/WebhooksApi~updateNetworkWebhooksHttpServer_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkWebhooksHttpServers200ResponseInner}
     */
    updateNetworkWebhooksHttpServer_1(networkId, httpServerId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkWebhooksHttpServerRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkWebhooksHttpServer_1");
      }
      // verify the required parameter 'httpServerId' is set
      if (httpServerId === undefined || httpServerId === null) {
        throw new Error("Missing the required parameter 'httpServerId' when calling updateNetworkWebhooksHttpServer_1");
      }

      let pathParams = {
        'networkId': networkId,
        'httpServerId': httpServerId
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
      let returnType = GetNetworkWebhooksHttpServers200ResponseInner;
      return this.apiClient.callApi(
        '/networks/{networkId}/webhooks/httpServers/{httpServerId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateNetworkWebhooksPayloadTemplate_1 operation.
     * @callback module:api/WebhooksApi~updateNetworkWebhooksPayloadTemplate_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetNetworkWebhooksPayloadTemplates200ResponseInner} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a webhook payload template for a network
     * Update a webhook payload template for a network
     * @param {String} networkId 
     * @param {String} payloadTemplateId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateNetworkWebhooksPayloadTemplateRequest} [updateNetworkWebhooksPayloadTemplateRequest] 
     * @param {module:api/WebhooksApi~updateNetworkWebhooksPayloadTemplate_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetNetworkWebhooksPayloadTemplates200ResponseInner}
     */
    updateNetworkWebhooksPayloadTemplate_1(networkId, payloadTemplateId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateNetworkWebhooksPayloadTemplateRequest'];
      // verify the required parameter 'networkId' is set
      if (networkId === undefined || networkId === null) {
        throw new Error("Missing the required parameter 'networkId' when calling updateNetworkWebhooksPayloadTemplate_1");
      }
      // verify the required parameter 'payloadTemplateId' is set
      if (payloadTemplateId === undefined || payloadTemplateId === null) {
        throw new Error("Missing the required parameter 'payloadTemplateId' when calling updateNetworkWebhooksPayloadTemplate_1");
      }

      let pathParams = {
        'networkId': networkId,
        'payloadTemplateId': payloadTemplateId
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
      let returnType = GetNetworkWebhooksPayloadTemplates200ResponseInner;
      return this.apiClient.callApi(
        '/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
