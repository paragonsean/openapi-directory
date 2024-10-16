/**
 * OnSched Consumer API
 * Build secure and scalable custom apps for Online Booking. Our flexible API provides many options for availability and booking.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ResourceListViewModel from '../model/ResourceListViewModel';
import ServiceAllocationListViewModel from '../model/ServiceAllocationListViewModel';
import ServiceAllocationViewModel from '../model/ServiceAllocationViewModel';
import ServiceListViewModel from '../model/ServiceListViewModel';
import ServiceSortOrder from '../model/ServiceSortOrder';
import ServiceViewModel from '../model/ServiceViewModel';
import ServicesScope from '../model/ServicesScope';

/**
* Services service.
* @module api/ServicesApi
* @version v1
*/
export default class ServicesApi {

    /**
    * Constructs a new ServicesApi. 
    * @alias module:api/ServicesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the consumerV1ServicesAllocationsIdGet operation.
     * @callback module:api/ServicesApi~consumerV1ServicesAllocationsIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ServiceAllocationViewModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Service Allocation
     * <p>Use this endpoint to return a <b>Service Allocation</b> object. A valid <b>serviceAllocation id</b> is required. Find service allocation id's by using the <i>GET/consumer​/v1​/services​/{id}​/allocations</i> endpoint.</p>
     * @param {String} id id of serviceAllocation object
     * @param {module:api/ServicesApi~consumerV1ServicesAllocationsIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ServiceAllocationViewModel}
     */
    consumerV1ServicesAllocationsIdGet(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling consumerV1ServicesAllocationsIdGet");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ServiceAllocationViewModel;
      return this.apiClient.callApi(
        '/consumer/v1/services/allocations/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consumerV1ServicesGet operation.
     * @callback module:api/ServicesApi~consumerV1ServicesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ServiceListViewModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List Services
     * <p>Use this endpoint to <b>List Services</b> available at your business location and/or company. If not specified, the business location defaults to the primary business location. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.</p>
     * @param {Object} opts Optional parameters
     * @param {String} [locationId] id of business location, defaults to primary business location
     * @param {Number} [serviceGroupId] Filter by groupId
     * @param {Boolean} [defaultService] Filter by default service, default is false
     * @param {Boolean} [allLocations] Search All Locations, default is false
     * @param {module:model/ServicesScope} [scope] Filter by scope, Company, Location or All, default is All
     * @param {String} [name] Filter by Name, supports Partial name search
     * @param {String} [serviceId] Filter by ServiceId, using this parameter would ignore all other parameters
     * @param {Number} [offset] Starting row of page, default 0
     * @param {Number} [limit] Page limit default 20, max 100
     * @param {module:model/ServiceSortOrder} [sortOrder] Sort results using Natural Sort or Sorted alphabetically by Service Names, default is natural
     * @param {Boolean} [sortDescending] Sort results in Descending Order, default true
     * @param {module:api/ServicesApi~consumerV1ServicesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ServiceListViewModel}
     */
    consumerV1ServicesGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'locationId': opts['locationId'],
        'serviceGroupId': opts['serviceGroupId'],
        'defaultService': opts['defaultService'],
        'allLocations': opts['allLocations'],
        'scope': opts['scope'],
        'name': opts['name'],
        'serviceId': opts['serviceId'],
        'offset': opts['offset'],
        'limit': opts['limit'],
        'sortOrder': opts['sortOrder'],
        'sortDescending': opts['sortDescending']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ServiceListViewModel;
      return this.apiClient.callApi(
        '/consumer/v1/services', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consumerV1ServicesIdAllocationsGet operation.
     * @callback module:api/ServicesApi~consumerV1ServicesIdAllocationsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ServiceAllocationListViewModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List Service Allocations
     * <p>Use this endpoint to return a <b>List of Service Allocations</b> associated with the requested service. A valid <b>service id</b> is required. Allocations are used for Event type services/bookings. Retrieve all allocations for a location by passing in zero as the service id. Otherwise, to get allocations for a specific service supply the service id. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further. For more information: <a href=\"https://docs.onsched.com/reference/post_setup-v1-services-id-allocations\">Create Service Allocations</a></p>
     * @param {String} id id of service to list allocations for, 0 for all
     * @param {Object} opts Optional parameters
     * @param {String} [locationId] id of the location, defaults to the primary location
     * @param {String} [resourceId] id of the resource to filter on
     * @param {Date} [startDate] Format YYYY-MM-DD: Filter allocations on/after startDate
     * @param {Date} [endDate] Format YYYY-MM-DD. Filter allocations on/before endDate
     * @param {Number} [offset] Starting row of page, default 0
     * @param {Number} [limit] Page limit default 20, max 100
     * @param {module:api/ServicesApi~consumerV1ServicesIdAllocationsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ServiceAllocationListViewModel}
     */
    consumerV1ServicesIdAllocationsGet(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling consumerV1ServicesIdAllocationsGet");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'locationId': opts['locationId'],
        'resourceId': opts['resourceId'],
        'startDate': opts['startDate'],
        'endDate': opts['endDate'],
        'offset': opts['offset'],
        'limit': opts['limit']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ServiceAllocationListViewModel;
      return this.apiClient.callApi(
        '/consumer/v1/services/{id}/allocations', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consumerV1ServicesIdGet operation.
     * @callback module:api/ServicesApi~consumerV1ServicesIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ServiceViewModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Service
     * <p>Use this endpoint to return a <b>Service</b> object. A valid <b>service id</b> is required. Find service id's by using the <i>GET /consumer/v1/services</i> endpoint.</p>
     * @param {Number} id id of service object
     * @param {module:api/ServicesApi~consumerV1ServicesIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ServiceViewModel}
     */
    consumerV1ServicesIdGet(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling consumerV1ServicesIdGet");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ServiceViewModel;
      return this.apiClient.callApi(
        '/consumer/v1/services/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consumerV1ServicesIdResourcesGet operation.
     * @callback module:api/ServicesApi~consumerV1ServicesIdResourcesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ResourceListViewModel} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List Resources for Service
     * <p>Use this endpoint to return a list of <b>Resources that provide the Service requested</b>. A valid <b>service id</b> is required. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.</p>
     * @param {String} id id of service object
     * @param {Object} opts Optional parameters
     * @param {String} [locationId] id of business location, defaults to primary business location
     * @param {Number} [offset] Starting row of page, default 0
     * @param {Number} [limit] Page limit default 20, max 100
     * @param {module:api/ServicesApi~consumerV1ServicesIdResourcesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ResourceListViewModel}
     */
    consumerV1ServicesIdResourcesGet(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling consumerV1ServicesIdResourcesGet");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'locationId': opts['locationId'],
        'offset': opts['offset'],
        'limit': opts['limit']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ResourceListViewModel;
      return this.apiClient.callApi(
        '/consumer/v1/services/{id}/resources', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
