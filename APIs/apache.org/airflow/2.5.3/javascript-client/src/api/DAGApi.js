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
import ClearTaskInstances from '../model/ClearTaskInstances';
import DAG from '../model/DAG';
import DAGCollection from '../model/DAGCollection';
import DAGDetail from '../model/DAGDetail';
import Error from '../model/Error';
import GetDagSource200Response from '../model/GetDagSource200Response';
import Task from '../model/Task';
import TaskCollection from '../model/TaskCollection';
import TaskInstanceReferenceCollection from '../model/TaskInstanceReferenceCollection';
import UpdateTaskInstancesState from '../model/UpdateTaskInstancesState';

/**
* DAG service.
* @module api/DAGApi
* @version 2.5.3
*/
export default class DAGApi {

    /**
    * Constructs a new DAGApi. 
    * @alias module:api/DAGApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the deleteDag operation.
     * @callback module:api/DAGApi~deleteDagCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a DAG
     * Deletes all metadata related to the DAG, including finished DAG Runs and Tasks. Logs are not deleted. This action cannot be undone.  *New in version 2.2.0* 
     * @param {String} dagId The DAG ID.
     * @param {module:api/DAGApi~deleteDagCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteDag(dagId, callback) {
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling deleteDag");
      }

      let pathParams = {
        'dag_id': dagId
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
      let returnType = null;
      return this.apiClient.callApi(
        '/dags/{dag_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDag operation.
     * @callback module:api/DAGApi~getDagCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DAG} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get basic information about a DAG
     * Presents only information available in database (DAGModel). If you need detailed information, consider using GET /dags/{dag_id}/details. 
     * @param {String} dagId The DAG ID.
     * @param {module:api/DAGApi~getDagCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DAG}
     */
    getDag(dagId, callback) {
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling getDag");
      }

      let pathParams = {
        'dag_id': dagId
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
      let returnType = DAG;
      return this.apiClient.callApi(
        '/dags/{dag_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDagDetails operation.
     * @callback module:api/DAGApi~getDagDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DAGDetail} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a simplified representation of DAG
     * The response contains many DAG attributes, so the response can be large. If possible, consider using GET /dags/{dag_id}. 
     * @param {String} dagId The DAG ID.
     * @param {module:api/DAGApi~getDagDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DAGDetail}
     */
    getDagDetails(dagId, callback) {
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling getDagDetails");
      }

      let pathParams = {
        'dag_id': dagId
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
      let returnType = DAGDetail;
      return this.apiClient.callApi(
        '/dags/{dag_id}/details', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDagSource operation.
     * @callback module:api/DAGApi~getDagSourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDagSource200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a source code
     * Get a source code using file token. 
     * @param {String} fileToken The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change. 
     * @param {module:api/DAGApi~getDagSourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDagSource200Response}
     */
    getDagSource(fileToken, callback) {
      let postBody = null;
      // verify the required parameter 'fileToken' is set
      if (fileToken === undefined || fileToken === null) {
        throw new Error("Missing the required parameter 'fileToken' when calling getDagSource");
      }

      let pathParams = {
        'file_token': fileToken
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'plain/text'];
      let returnType = GetDagSource200Response;
      return this.apiClient.callApi(
        '/dagSources/{file_token}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDags operation.
     * @callback module:api/DAGApi~getDagsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DAGCollection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List DAGs
     * List DAGs in the database. `dag_id_pattern` can be set to match dags of a specific pattern 
     * @param {Object} opts Optional parameters
     * @param {Number} [limit = 100)] The numbers of items to return.
     * @param {Number} [offset] The number of items to skip before starting to collect the result set.
     * @param {String} [orderBy] The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
     * @param {Array.<String>} [tags] List of tags to filter results.  *New in version 2.2.0* 
     * @param {Boolean} [onlyActive = true)] Only filter active DAGs.  *New in version 2.1.1* 
     * @param {String} [dagIdPattern] If set, only return DAGs with dag_ids matching this pattern. 
     * @param {module:api/DAGApi~getDagsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DAGCollection}
     */
    getDags(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'order_by': opts['orderBy'],
        'tags': this.apiClient.buildCollectionParam(opts['tags'], 'multi'),
        'only_active': opts['onlyActive'],
        'dag_id_pattern': opts['dagIdPattern']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DAGCollection;
      return this.apiClient.callApi(
        '/dags', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTask operation.
     * @callback module:api/DAGApi~getTaskCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Task} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get simplified representation of a task
     * @param {String} dagId The DAG ID.
     * @param {String} taskId The task ID.
     * @param {module:api/DAGApi~getTaskCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Task}
     */
    getTask(dagId, taskId, callback) {
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling getTask");
      }
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling getTask");
      }

      let pathParams = {
        'dag_id': dagId,
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
      let returnType = Task;
      return this.apiClient.callApi(
        '/dags/{dag_id}/tasks/{task_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTasks operation.
     * @callback module:api/DAGApi~getTasksCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskCollection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get tasks for DAG
     * @param {String} dagId The DAG ID.
     * @param {Object} opts Optional parameters
     * @param {String} [orderBy] The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
     * @param {module:api/DAGApi~getTasksCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskCollection}
     */
    getTasks(dagId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling getTasks");
      }

      let pathParams = {
        'dag_id': dagId
      };
      let queryParams = {
        'order_by': opts['orderBy']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskCollection;
      return this.apiClient.callApi(
        '/dags/{dag_id}/tasks', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patchDag operation.
     * @callback module:api/DAGApi~patchDagCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DAG} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a DAG
     * @param {String} dagId The DAG ID.
     * @param {module:model/DAG} DAG 
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} [updateMask] The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. 
     * @param {module:api/DAGApi~patchDagCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DAG}
     */
    patchDag(dagId, DAG, opts, callback) {
      opts = opts || {};
      let postBody = DAG;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling patchDag");
      }
      // verify the required parameter 'DAG' is set
      if (DAG === undefined || DAG === null) {
        throw new Error("Missing the required parameter 'DAG' when calling patchDag");
      }

      let pathParams = {
        'dag_id': dagId
      };
      let queryParams = {
        'update_mask': this.apiClient.buildCollectionParam(opts['updateMask'], 'csv')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DAG;
      return this.apiClient.callApi(
        '/dags/{dag_id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patchDags operation.
     * @callback module:api/DAGApi~patchDagsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DAGCollection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update DAGs
     * Update DAGs of a given dag_id_pattern using UpdateMask. This endpoint allows specifying `~` as the dag_id_pattern to update all DAGs. *New in version 2.3.0* 
     * @param {String} dagIdPattern If set, only update DAGs with dag_ids matching this pattern. 
     * @param {module:model/DAG} DAG 
     * @param {Object} opts Optional parameters
     * @param {Number} [limit = 100)] The numbers of items to return.
     * @param {Number} [offset] The number of items to skip before starting to collect the result set.
     * @param {Array.<String>} [tags] List of tags to filter results.  *New in version 2.2.0* 
     * @param {Array.<String>} [updateMask] The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. 
     * @param {Boolean} [onlyActive = true)] Only filter active DAGs.  *New in version 2.1.1* 
     * @param {module:api/DAGApi~patchDagsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DAGCollection}
     */
    patchDags(dagIdPattern, DAG, opts, callback) {
      opts = opts || {};
      let postBody = DAG;
      // verify the required parameter 'dagIdPattern' is set
      if (dagIdPattern === undefined || dagIdPattern === null) {
        throw new Error("Missing the required parameter 'dagIdPattern' when calling patchDags");
      }
      // verify the required parameter 'DAG' is set
      if (DAG === undefined || DAG === null) {
        throw new Error("Missing the required parameter 'DAG' when calling patchDags");
      }

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'tags': this.apiClient.buildCollectionParam(opts['tags'], 'multi'),
        'update_mask': this.apiClient.buildCollectionParam(opts['updateMask'], 'csv'),
        'only_active': opts['onlyActive'],
        'dag_id_pattern': dagIdPattern
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DAGCollection;
      return this.apiClient.callApi(
        '/dags', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postClearTaskInstances operation.
     * @callback module:api/DAGApi~postClearTaskInstancesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskInstanceReferenceCollection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Clear a set of task instances
     * Clears a set of task instances associated with the DAG for a specified date range. 
     * @param {String} dagId The DAG ID.
     * @param {module:model/ClearTaskInstances} clearTaskInstances Parameters of action
     * @param {module:api/DAGApi~postClearTaskInstancesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskInstanceReferenceCollection}
     */
    postClearTaskInstances(dagId, clearTaskInstances, callback) {
      let postBody = clearTaskInstances;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling postClearTaskInstances");
      }
      // verify the required parameter 'clearTaskInstances' is set
      if (clearTaskInstances === undefined || clearTaskInstances === null) {
        throw new Error("Missing the required parameter 'clearTaskInstances' when calling postClearTaskInstances");
      }

      let pathParams = {
        'dag_id': dagId
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
      let returnType = TaskInstanceReferenceCollection;
      return this.apiClient.callApi(
        '/dags/{dag_id}/clearTaskInstances', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postSetTaskInstancesState operation.
     * @callback module:api/DAGApi~postSetTaskInstancesStateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskInstanceReferenceCollection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Set a state of task instances
     * Updates the state for multiple task instances simultaneously. 
     * @param {String} dagId The DAG ID.
     * @param {module:model/UpdateTaskInstancesState} updateTaskInstancesState Parameters of action
     * @param {module:api/DAGApi~postSetTaskInstancesStateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskInstanceReferenceCollection}
     */
    postSetTaskInstancesState(dagId, updateTaskInstancesState, callback) {
      let postBody = updateTaskInstancesState;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling postSetTaskInstancesState");
      }
      // verify the required parameter 'updateTaskInstancesState' is set
      if (updateTaskInstancesState === undefined || updateTaskInstancesState === null) {
        throw new Error("Missing the required parameter 'updateTaskInstancesState' when calling postSetTaskInstancesState");
      }

      let pathParams = {
        'dag_id': dagId
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
      let returnType = TaskInstanceReferenceCollection;
      return this.apiClient.callApi(
        '/dags/{dag_id}/updateTaskInstancesState', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
