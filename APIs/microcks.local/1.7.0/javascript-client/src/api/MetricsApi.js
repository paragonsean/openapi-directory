/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import DailyInvocationStatistic from '../model/DailyInvocationStatistic';
import TestConformanceMetric from '../model/TestConformanceMetric';
import TestResultSummary from '../model/TestResultSummary';
import WeightedMetricValue from '../model/WeightedMetricValue';

/**
* Metrics service.
* @module api/MetricsApi
* @version 1.7.0
*/
export default class MetricsApi {

    /**
    * Constructs a new MetricsApi. 
    * @alias module:api/MetricsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getAggregatedInvocationsStats operation.
     * @callback module:api/MetricsApi~getAggregatedInvocationsStatsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DailyInvocationStatistic} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get aggregated invocation statistics for a day
     * @param {Object} opts Optional parameters
     * @param {String} [day] The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
     * @param {module:api/MetricsApi~getAggregatedInvocationsStatsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DailyInvocationStatistic}
     */
    getAggregatedInvocationsStats(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'day': opts['day']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['jwt-bearer'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DailyInvocationStatistic;
      return this.apiClient.callApi(
        '/metrics/invocations/global', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getConformanceMetricsAggregation operation.
     * @callback module:api/MetricsApi~getConformanceMetricsAggregationCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/WeightedMetricValue>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get aggregation of conformance metrics
     * @param {module:api/MetricsApi~getConformanceMetricsAggregationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/WeightedMetricValue>}
     */
    getConformanceMetricsAggregation(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['jwt-bearer'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [WeightedMetricValue];
      return this.apiClient.callApi(
        '/metrics/conformance/aggregate', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getInvocationStatsByService operation.
     * @callback module:api/MetricsApi~getInvocationStatsByServiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DailyInvocationStatistic} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get invocation statistics for Service
     * @param {String} serviceName Name of service to get statistics for
     * @param {String} serviceVersion Version of service to get statistics for
     * @param {Object} opts Optional parameters
     * @param {String} [day] The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
     * @param {module:api/MetricsApi~getInvocationStatsByServiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DailyInvocationStatistic}
     */
    getInvocationStatsByService(serviceName, serviceVersion, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'serviceName' is set
      if (serviceName === undefined || serviceName === null) {
        throw new Error("Missing the required parameter 'serviceName' when calling getInvocationStatsByService");
      }
      // verify the required parameter 'serviceVersion' is set
      if (serviceVersion === undefined || serviceVersion === null) {
        throw new Error("Missing the required parameter 'serviceVersion' when calling getInvocationStatsByService");
      }

      let pathParams = {
        'serviceName': serviceName,
        'serviceVersion': serviceVersion
      };
      let queryParams = {
        'day': opts['day']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['jwt-bearer'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DailyInvocationStatistic;
      return this.apiClient.callApi(
        '/metrics/invocations/{serviceName}/{serviceVersion}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLatestAggregatedInvocationsStats operation.
     * @callback module:api/MetricsApi~getLatestAggregatedInvocationsStatsCallback
     * @param {String} error Error message, if any.
     * @param {Object.<String, {String: Number}>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get aggregated invocations statistics for latest days
     * @param {Object} opts Optional parameters
     * @param {Number} [limit] Number of days to get back in time. Default is 20.
     * @param {module:api/MetricsApi~getLatestAggregatedInvocationsStatsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object.<String, {String: Number}>}
     */
    getLatestAggregatedInvocationsStats(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['jwt-bearer'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = {'String': 'Number'};
      return this.apiClient.callApi(
        '/metrics/invocations/global/latest', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLatestTestResults operation.
     * @callback module:api/MetricsApi~getLatestTestResultsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/TestResultSummary>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get latest tests results
     * @param {Object} opts Optional parameters
     * @param {Number} [limit] Number of days to consider for test results to return. Default is 7 (one week)
     * @param {module:api/MetricsApi~getLatestTestResultsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/TestResultSummary>}
     */
    getLatestTestResults(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['jwt-bearer'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [TestResultSummary];
      return this.apiClient.callApi(
        '/metrics/tests/latest', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getServiceTestConformanceMetric operation.
     * @callback module:api/MetricsApi~getServiceTestConformanceMetricCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TestConformanceMetric} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get conformance metrics for a Service
     * @param {String} serviceId Unique Services identifier this metrics are related to
     * @param {module:api/MetricsApi~getServiceTestConformanceMetricCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TestConformanceMetric}
     */
    getServiceTestConformanceMetric(serviceId, callback) {
      let postBody = null;
      // verify the required parameter 'serviceId' is set
      if (serviceId === undefined || serviceId === null) {
        throw new Error("Missing the required parameter 'serviceId' when calling getServiceTestConformanceMetric");
      }

      let pathParams = {
        'serviceId': serviceId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['jwt-bearer'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TestConformanceMetric;
      return this.apiClient.callApi(
        '/metrics/conformance/service/{serviceId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTopIvnocationsStatsByDay operation.
     * @callback module:api/MetricsApi~getTopIvnocationsStatsByDayCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/DailyInvocationStatistic>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get top invocation statistics for a day
     * @param {Object} opts Optional parameters
     * @param {String} [day] The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
     * @param {Number} [limit] The number of top invoked mocks to return
     * @param {module:api/MetricsApi~getTopIvnocationsStatsByDayCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/DailyInvocationStatistic>}
     */
    getTopIvnocationsStatsByDay(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'day': opts['day'],
        'limit': opts['limit']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['jwt-bearer'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [DailyInvocationStatistic];
      return this.apiClient.callApi(
        '/metrics/invocations/top', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
