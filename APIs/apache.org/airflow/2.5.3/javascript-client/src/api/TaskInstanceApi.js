/**
 * Airflow API (Stable)
 * # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept `JSON` as input and return `JSON` responses. This means that you must usually add the following headers to your request: ``` Content-type: application/json Accept: application/json ```  ## Resources  The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint's corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata in the request body. The response returns a `201 Created` response code upon success with the resource's metadata, including its internal `id`, in the response body.  ### Read  The HTTP `GET` request can be used to read a resource or to list a number of resources.  A resource's `id` can be submitted in the request parameters to read a specific resource. The response usually returns a `200 OK` response code upon success, with the resource's metadata in the response body.  If a `GET` request does not include a specific resource `id`, it is treated as a list request. The response usually returns a `200 OK` response code upon success, with an object containing a list of resources' metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: ``` v1/connections?limit=25&offset=25 ```  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request, with the fields to modify in the request body. The response usually returns a `200 OK` response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource `id` and is typically executing via an HTTP `DELETE` request. The response usually returns a `204 No Content` response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. ```json {     \"name\": \"string\",     \"slots\": 0,     \"occupied_slots\": 0,     \"used_slots\": 0,     \"queued_slots\": 0,     \"open_slots\": 0 } ```  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using `update_mask` makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren't specified in the field mask, leaving them with their current values.  Example: ```   resource = request.get('/resource/my-id').json()   resource['my_field'] = 'new-value'   request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource)) ```  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: ```bash curl -X PATCH 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\ -H 'Content-Type: application/json' \\ --user \"username:password\" \\ -d '{     \"is_paused\": true }' ```  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use `airflow config get-value api auth_backends` command as in the example below. ```bash $ airflow config get-value api auth_backends airflow.api.auth.backend.basic_auth ``` The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, e.g. the resource it tries to create already exists.  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request. 
 *
 * The version of the OpenAPI document: 2.5.3
 * Contact: dev@airflow.apache.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Error from '../model/Error';
import ExtraLinkCollection from '../model/ExtraLinkCollection';
import GetLog200Response from '../model/GetLog200Response';
import ListTaskInstanceForm from '../model/ListTaskInstanceForm';
import SetTaskInstanceNote from '../model/SetTaskInstanceNote';
import TaskInstance from '../model/TaskInstance';
import TaskInstanceCollection from '../model/TaskInstanceCollection';
import TaskInstanceReference from '../model/TaskInstanceReference';
import UpdateTaskInstance from '../model/UpdateTaskInstance';

/**
* TaskInstance service.
* @module api/TaskInstanceApi
* @version 2.5.3
*/
export default class TaskInstanceApi {

    /**
    * Constructs a new TaskInstanceApi. 
    * @alias module:api/TaskInstanceApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getExtraLinks operation.
     * @callback module:api/TaskInstanceApi~getExtraLinksCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExtraLinkCollection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List extra links
     * List extra links for task instance. 
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {String} taskId The task ID.
     * @param {module:api/TaskInstanceApi~getExtraLinksCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExtraLinkCollection}
     */
    getExtraLinks(dagId, dagRunId, taskId, callback) {
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling getExtraLinks");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling getExtraLinks");
      }
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling getExtraLinks");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId,
        'task_id': taskId
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
      let returnType = ExtraLinkCollection;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/links', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLog operation.
     * @callback module:api/TaskInstanceApi~getLogCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetLog200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get logs
     * Get logs for a specific task instance and its try number.
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {String} taskId The task ID.
     * @param {Number} taskTryNumber The task try number.
     * @param {Object} opts Optional parameters
     * @param {Boolean} [fullContent] A full content will be returned. By default, only the first fragment will be returned. 
     * @param {Number} [mapIndex] Filter on map index for mapped task.
     * @param {String} [token] A token that allows you to continue fetching logs. If passed, it will specify the location from which the download should be continued. 
     * @param {module:api/TaskInstanceApi~getLogCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetLog200Response}
     */
    getLog(dagId, dagRunId, taskId, taskTryNumber, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling getLog");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling getLog");
      }
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling getLog");
      }
      // verify the required parameter 'taskTryNumber' is set
      if (taskTryNumber === undefined || taskTryNumber === null) {
        throw new Error("Missing the required parameter 'taskTryNumber' when calling getLog");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId,
        'task_id': taskId,
        'task_try_number': taskTryNumber
      };
      let queryParams = {
        'full_content': opts['fullContent'],
        'map_index': opts['mapIndex'],
        'token': opts['token']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/plain'];
      let returnType = GetLog200Response;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{task_try_number}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMappedTaskInstance operation.
     * @callback module:api/TaskInstanceApi~getMappedTaskInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskInstance} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a mapped task instance
     * Get details of a mapped task instance.  *New in version 2.3.0* 
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {String} taskId The task ID.
     * @param {Number} mapIndex The map index.
     * @param {module:api/TaskInstanceApi~getMappedTaskInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskInstance}
     */
    getMappedTaskInstance(dagId, dagRunId, taskId, mapIndex, callback) {
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling getMappedTaskInstance");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling getMappedTaskInstance");
      }
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling getMappedTaskInstance");
      }
      // verify the required parameter 'mapIndex' is set
      if (mapIndex === undefined || mapIndex === null) {
        throw new Error("Missing the required parameter 'mapIndex' when calling getMappedTaskInstance");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId,
        'task_id': taskId,
        'map_index': mapIndex
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
      let returnType = TaskInstance;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMappedTaskInstances operation.
     * @callback module:api/TaskInstanceApi~getMappedTaskInstancesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskInstanceCollection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List mapped task instances
     * Get details of all mapped task instances.  *New in version 2.3.0* 
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {String} taskId The task ID.
     * @param {Object} opts Optional parameters
     * @param {Number} [limit = 100)] The numbers of items to return.
     * @param {Number} [offset] The number of items to skip before starting to collect the result set.
     * @param {Date} [executionDateGte] Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period. 
     * @param {Date} [executionDateLte] Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period. 
     * @param {Date} [startDateGte] Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
     * @param {Date} [startDateLte] Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
     * @param {Date} [endDateGte] Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
     * @param {Date} [endDateLte] Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
     * @param {Number} [durationGte] Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period. 
     * @param {Number} [durationLte] Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range. 
     * @param {Array.<String>} [state] The value can be repeated to retrieve multiple matching values (OR condition).
     * @param {Array.<String>} [pool] The value can be repeated to retrieve multiple matching values (OR condition).
     * @param {Array.<String>} [queue] The value can be repeated to retrieve multiple matching values (OR condition).
     * @param {String} [orderBy] The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
     * @param {module:api/TaskInstanceApi~getMappedTaskInstancesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskInstanceCollection}
     */
    getMappedTaskInstances(dagId, dagRunId, taskId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling getMappedTaskInstances");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling getMappedTaskInstances");
      }
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling getMappedTaskInstances");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId,
        'task_id': taskId
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'execution_date_gte': opts['executionDateGte'],
        'execution_date_lte': opts['executionDateLte'],
        'start_date_gte': opts['startDateGte'],
        'start_date_lte': opts['startDateLte'],
        'end_date_gte': opts['endDateGte'],
        'end_date_lte': opts['endDateLte'],
        'duration_gte': opts['durationGte'],
        'duration_lte': opts['durationLte'],
        'state': this.apiClient.buildCollectionParam(opts['state'], 'multi'),
        'pool': this.apiClient.buildCollectionParam(opts['pool'], 'multi'),
        'queue': this.apiClient.buildCollectionParam(opts['queue'], 'multi'),
        'order_by': opts['orderBy']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskInstanceCollection;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/listMapped', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTaskInstance operation.
     * @callback module:api/TaskInstanceApi~getTaskInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskInstance} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a task instance
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {String} taskId The task ID.
     * @param {module:api/TaskInstanceApi~getTaskInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskInstance}
     */
    getTaskInstance(dagId, dagRunId, taskId, callback) {
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling getTaskInstance");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling getTaskInstance");
      }
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling getTaskInstance");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId,
        'task_id': taskId
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
      let returnType = TaskInstance;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTaskInstances operation.
     * @callback module:api/TaskInstanceApi~getTaskInstancesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskInstanceCollection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List task instances
     * This endpoint allows specifying `~` as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and DAG runs. 
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {Object} opts Optional parameters
     * @param {Date} [executionDateGte] Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period. 
     * @param {Date} [executionDateLte] Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period. 
     * @param {Date} [startDateGte] Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
     * @param {Date} [startDateLte] Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
     * @param {Date} [endDateGte] Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
     * @param {Date} [endDateLte] Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
     * @param {Number} [durationGte] Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period. 
     * @param {Number} [durationLte] Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range. 
     * @param {Array.<String>} [state] The value can be repeated to retrieve multiple matching values (OR condition).
     * @param {Array.<String>} [pool] The value can be repeated to retrieve multiple matching values (OR condition).
     * @param {Array.<String>} [queue] The value can be repeated to retrieve multiple matching values (OR condition).
     * @param {Number} [limit = 100)] The numbers of items to return.
     * @param {Number} [offset] The number of items to skip before starting to collect the result set.
     * @param {module:api/TaskInstanceApi~getTaskInstancesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskInstanceCollection}
     */
    getTaskInstances(dagId, dagRunId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling getTaskInstances");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling getTaskInstances");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId
      };
      let queryParams = {
        'execution_date_gte': opts['executionDateGte'],
        'execution_date_lte': opts['executionDateLte'],
        'start_date_gte': opts['startDateGte'],
        'start_date_lte': opts['startDateLte'],
        'end_date_gte': opts['endDateGte'],
        'end_date_lte': opts['endDateLte'],
        'duration_gte': opts['durationGte'],
        'duration_lte': opts['durationLte'],
        'state': this.apiClient.buildCollectionParam(opts['state'], 'multi'),
        'pool': this.apiClient.buildCollectionParam(opts['pool'], 'multi'),
        'queue': this.apiClient.buildCollectionParam(opts['queue'], 'multi'),
        'limit': opts['limit'],
        'offset': opts['offset']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskInstanceCollection;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTaskInstancesBatch operation.
     * @callback module:api/TaskInstanceApi~getTaskInstancesBatchCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskInstanceCollection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List task instances (batch)
     * List task instances from all DAGs and DAG runs. This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limits. 
     * @param {module:model/ListTaskInstanceForm} listTaskInstanceForm 
     * @param {module:api/TaskInstanceApi~getTaskInstancesBatchCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskInstanceCollection}
     */
    getTaskInstancesBatch(listTaskInstanceForm, callback) {
      let postBody = listTaskInstanceForm;
      // verify the required parameter 'listTaskInstanceForm' is set
      if (listTaskInstanceForm === undefined || listTaskInstanceForm === null) {
        throw new Error("Missing the required parameter 'listTaskInstanceForm' when calling getTaskInstancesBatch");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = TaskInstanceCollection;
      return this.apiClient.callApi(
        '/dags/~/dagRuns/~/taskInstances/list', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patchMappedTaskInstance operation.
     * @callback module:api/TaskInstanceApi~patchMappedTaskInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskInstanceReference} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates the state of a mapped task instance
     * Updates the state for single mapped task instance. *New in version 2.5.0* 
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {String} taskId The task ID.
     * @param {Number} mapIndex The map index.
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateTaskInstance} [updateTaskInstance] Parameters of action
     * @param {module:api/TaskInstanceApi~patchMappedTaskInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskInstanceReference}
     */
    patchMappedTaskInstance(dagId, dagRunId, taskId, mapIndex, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateTaskInstance'];
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling patchMappedTaskInstance");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling patchMappedTaskInstance");
      }
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling patchMappedTaskInstance");
      }
      // verify the required parameter 'mapIndex' is set
      if (mapIndex === undefined || mapIndex === null) {
        throw new Error("Missing the required parameter 'mapIndex' when calling patchMappedTaskInstance");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId,
        'task_id': taskId,
        'map_index': mapIndex
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = TaskInstanceReference;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patchTaskInstance operation.
     * @callback module:api/TaskInstanceApi~patchTaskInstanceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskInstanceReference} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates the state of a task instance
     * Updates the state for single task instance. *New in version 2.5.0* 
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {String} taskId The task ID.
     * @param {module:model/UpdateTaskInstance} updateTaskInstance Parameters of action
     * @param {module:api/TaskInstanceApi~patchTaskInstanceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskInstanceReference}
     */
    patchTaskInstance(dagId, dagRunId, taskId, updateTaskInstance, callback) {
      let postBody = updateTaskInstance;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling patchTaskInstance");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling patchTaskInstance");
      }
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling patchTaskInstance");
      }
      // verify the required parameter 'updateTaskInstance' is set
      if (updateTaskInstance === undefined || updateTaskInstance === null) {
        throw new Error("Missing the required parameter 'updateTaskInstance' when calling patchTaskInstance");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId,
        'task_id': taskId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = TaskInstanceReference;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the setMappedTaskInstanceNote operation.
     * @callback module:api/TaskInstanceApi~setMappedTaskInstanceNoteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskInstance} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the TaskInstance note.
     * Update the manual user note of a mapped Task Instance.  *New in version 2.5.0* 
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {String} taskId The task ID.
     * @param {Number} mapIndex The map index.
     * @param {module:model/SetTaskInstanceNote} setTaskInstanceNote Parameters of set Task Instance note.
     * @param {module:api/TaskInstanceApi~setMappedTaskInstanceNoteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskInstance}
     */
    setMappedTaskInstanceNote(dagId, dagRunId, taskId, mapIndex, setTaskInstanceNote, callback) {
      let postBody = setTaskInstanceNote;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling setMappedTaskInstanceNote");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling setMappedTaskInstanceNote");
      }
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling setMappedTaskInstanceNote");
      }
      // verify the required parameter 'mapIndex' is set
      if (mapIndex === undefined || mapIndex === null) {
        throw new Error("Missing the required parameter 'mapIndex' when calling setMappedTaskInstanceNote");
      }
      // verify the required parameter 'setTaskInstanceNote' is set
      if (setTaskInstanceNote === undefined || setTaskInstanceNote === null) {
        throw new Error("Missing the required parameter 'setTaskInstanceNote' when calling setMappedTaskInstanceNote");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId,
        'task_id': taskId,
        'map_index': mapIndex
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = TaskInstance;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}/setNote', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the setTaskInstanceNote operation.
     * @callback module:api/TaskInstanceApi~setTaskInstanceNoteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskInstance} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the TaskInstance note.
     * Update the manual user note of a non-mapped Task Instance.  *New in version 2.5.0* 
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {String} taskId The task ID.
     * @param {module:model/SetTaskInstanceNote} setTaskInstanceNote Parameters of set Task Instance note.
     * @param {module:api/TaskInstanceApi~setTaskInstanceNoteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskInstance}
     */
    setTaskInstanceNote(dagId, dagRunId, taskId, setTaskInstanceNote, callback) {
      let postBody = setTaskInstanceNote;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling setTaskInstanceNote");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling setTaskInstanceNote");
      }
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling setTaskInstanceNote");
      }
      // verify the required parameter 'setTaskInstanceNote' is set
      if (setTaskInstanceNote === undefined || setTaskInstanceNote === null) {
        throw new Error("Missing the required parameter 'setTaskInstanceNote' when calling setTaskInstanceNote");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId,
        'task_id': taskId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = TaskInstance;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/setNote', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
