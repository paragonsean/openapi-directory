/**
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Error from '../model/Error';
import PaginatedChangeDescriptions from '../model/PaginatedChangeDescriptions';

/**
* AuditLog service.
* @module api/AuditLogApi
* @version 1.0
*/
export default class AuditLogApi {

    /**
    * Constructs a new AuditLogApi. 
    * @alias module:api/AuditLogApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the changelogAdhocGet operation.
     * @callback module:api/AuditLogApi~changelogAdhocGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PaginatedChangeDescriptions} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Allows an arbitrary filter to be specified and applied to the org\\'s change log.
     * Perform an adhoc query against the change log for your org. The filter is a JSON encoded FilterSum as defined in this file.
     * @param {Object} opts Optional parameters
     * @param {String} [filter] Encoded FilterSums representing the query you would like to execute. See object definition for details.
     * @param {module:api/AuditLogApi~changelogAdhocGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PaginatedChangeDescriptions}
     */
    changelogAdhocGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'filter': opts['filter']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PaginatedChangeDescriptions;
      return this.apiClient.callApi(
        '/changelog/adhoc', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the changelogClusterGraphClusterKeyGet operation.
     * @callback module:api/AuditLogApi~changelogClusterGraphClusterKeyGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PaginatedChangeDescriptions} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * get changes related to the indicated cluster
     * Gets all changes to a cluster. 
     * @param {String} clusterKey the cluster key to see an audit log for
     * @param {Object} opts Optional parameters
     * @param {Number} [start] The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
     * @param {Number} [end] The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
     * @param {Number} [maxResults] Determines how many ChangeDescription object should be returned to the calling code. 
     * @param {String} [refId] When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
     * @param {module:model/String} [direction] If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
     * @param {module:api/AuditLogApi~changelogClusterGraphClusterKeyGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PaginatedChangeDescriptions}
     */
    changelogClusterGraphClusterKeyGet(clusterKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'clusterKey' is set
      if (clusterKey === undefined || clusterKey === null) {
        throw new Error("Missing the required parameter 'clusterKey' when calling changelogClusterGraphClusterKeyGet");
      }

      let pathParams = {
        'clusterKey': clusterKey
      };
      let queryParams = {
        'start': opts['start'],
        'end': opts['end'],
        'max_results': opts['maxResults'],
        'ref_id': opts['refId'],
        'direction': opts['direction']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PaginatedChangeDescriptions;
      return this.apiClient.callApi(
        '/changelog/cluster-graph/{clusterKey}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the changelogDomainGraphDomainKeyGet operation.
     * @callback module:api/AuditLogApi~changelogDomainGraphDomainKeyGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PaginatedChangeDescriptions} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * get changes related to the indicated domain
     * Gets all changes to a domain, the proxies that front the specified domain, routes within that domain, the shared rules of each route, the clusters connected via route or shared rules. 
     * @param {String} domainKey the domain key to see an audit log for
     * @param {Object} opts Optional parameters
     * @param {Number} [start] The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
     * @param {Number} [end] The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
     * @param {Number} [maxResults] Determines how many ChangeDescription object should be returned to the calling code. 
     * @param {String} [refId] When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
     * @param {module:model/String} [direction] If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
     * @param {module:api/AuditLogApi~changelogDomainGraphDomainKeyGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PaginatedChangeDescriptions}
     */
    changelogDomainGraphDomainKeyGet(domainKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'domainKey' is set
      if (domainKey === undefined || domainKey === null) {
        throw new Error("Missing the required parameter 'domainKey' when calling changelogDomainGraphDomainKeyGet");
      }

      let pathParams = {
        'domainKey': domainKey
      };
      let queryParams = {
        'start': opts['start'],
        'end': opts['end'],
        'max_results': opts['maxResults'],
        'ref_id': opts['refId'],
        'direction': opts['direction']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PaginatedChangeDescriptions;
      return this.apiClient.callApi(
        '/changelog/domain-graph/{domainKey}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the changelogRouteGraphRouteKeyGet operation.
     * @callback module:api/AuditLogApi~changelogRouteGraphRouteKeyGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PaginatedChangeDescriptions} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * get changes related to the indicated route
     * Gets all changes to a route, the domains associated with it, the shared rules it references, and the clusters connected to it. 
     * @param {String} routeKey the route key to see an audit log for
     * @param {Object} opts Optional parameters
     * @param {Number} [start] The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
     * @param {Number} [end] The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
     * @param {Number} [maxResults] Determines how many ChangeDescription object should be returned to the calling code. 
     * @param {String} [refId] When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
     * @param {module:model/String} [direction] If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
     * @param {module:api/AuditLogApi~changelogRouteGraphRouteKeyGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PaginatedChangeDescriptions}
     */
    changelogRouteGraphRouteKeyGet(routeKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'routeKey' is set
      if (routeKey === undefined || routeKey === null) {
        throw new Error("Missing the required parameter 'routeKey' when calling changelogRouteGraphRouteKeyGet");
      }

      let pathParams = {
        'routeKey': routeKey
      };
      let queryParams = {
        'start': opts['start'],
        'end': opts['end'],
        'max_results': opts['maxResults'],
        'ref_id': opts['refId'],
        'direction': opts['direction']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PaginatedChangeDescriptions;
      return this.apiClient.callApi(
        '/changelog/route-graph/{routeKey}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the changelogSharedRulesGraphSharedRulesKeyGet operation.
     * @callback module:api/AuditLogApi~changelogSharedRulesGraphSharedRulesKeyGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PaginatedChangeDescriptions} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * get changes related to the indicated SharedRules
     * Gets all changes associated with set of Shared Rules; the domains using it and the clusters referenced by it. 
     * @param {String} sharedRulesKey the shared rules key to see an audit log for
     * @param {Object} opts Optional parameters
     * @param {Number} [start] The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
     * @param {Number} [end] The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
     * @param {Number} [maxResults] Determines how many ChangeDescription object should be returned to the calling code. 
     * @param {String} [refId] When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
     * @param {module:model/String} [direction] If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
     * @param {module:api/AuditLogApi~changelogSharedRulesGraphSharedRulesKeyGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PaginatedChangeDescriptions}
     */
    changelogSharedRulesGraphSharedRulesKeyGet(sharedRulesKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'sharedRulesKey' is set
      if (sharedRulesKey === undefined || sharedRulesKey === null) {
        throw new Error("Missing the required parameter 'sharedRulesKey' when calling changelogSharedRulesGraphSharedRulesKeyGet");
      }

      let pathParams = {
        'sharedRulesKey': sharedRulesKey
      };
      let queryParams = {
        'start': opts['start'],
        'end': opts['end'],
        'max_results': opts['maxResults'],
        'ref_id': opts['refId'],
        'direction': opts['direction']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PaginatedChangeDescriptions;
      return this.apiClient.callApi(
        '/changelog/shared-rules-graph/{sharedRulesKey}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the changelogZoneZoneKeyGet operation.
     * @callback module:api/AuditLogApi~changelogZoneZoneKeyGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PaginatedChangeDescriptions} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * get changes in a specified zone
     * Retrieve all changes in the specified zone.
     * @param {String} zoneKey the zone key to see an audit log for
     * @param {Object} opts Optional parameters
     * @param {Number} [start] The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
     * @param {Number} [end] The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
     * @param {Number} [maxResults] Determines how many ChangeDescription object should be returned to the calling code. 
     * @param {String} [refId] When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
     * @param {module:model/String} [direction] If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
     * @param {module:api/AuditLogApi~changelogZoneZoneKeyGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PaginatedChangeDescriptions}
     */
    changelogZoneZoneKeyGet(zoneKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'zoneKey' is set
      if (zoneKey === undefined || zoneKey === null) {
        throw new Error("Missing the required parameter 'zoneKey' when calling changelogZoneZoneKeyGet");
      }

      let pathParams = {
        'zoneKey': zoneKey
      };
      let queryParams = {
        'start': opts['start'],
        'end': opts['end'],
        'max_results': opts['maxResults'],
        'ref_id': opts['refId'],
        'direction': opts['direction']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PaginatedChangeDescriptions;
      return this.apiClient.callApi(
        '/changelog/zone/{zoneKey}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
