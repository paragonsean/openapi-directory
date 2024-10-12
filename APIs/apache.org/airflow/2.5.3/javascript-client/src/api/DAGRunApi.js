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
import ClearDagRun from '../model/ClearDagRun';
import ClearDagRun200Response from '../model/ClearDagRun200Response';
import DAGRun from '../model/DAGRun';
import DAGRunCollection from '../model/DAGRunCollection';
import DatasetEventCollection from '../model/DatasetEventCollection';
import Error from '../model/Error';
import ListDagRunsForm from '../model/ListDagRunsForm';
import SetDagRunNote from '../model/SetDagRunNote';
import UpdateDagRunState from '../model/UpdateDagRunState';

/**
* DAGRun service.
* @module api/DAGRunApi
* @version 2.5.3
*/
export default class DAGRunApi {

    /**
    * Constructs a new DAGRunApi. 
    * @alias module:api/DAGRunApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the clearDagRun operation.
     * @callback module:api/DAGRunApi~clearDagRunCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClearDagRun200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Clear a DAG run
     * Clear a DAG run.  *New in version 2.4.0* 
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {module:model/ClearDagRun} clearDagRun 
     * @param {module:api/DAGRunApi~clearDagRunCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClearDagRun200Response}
     */
    clearDagRun(dagId, dagRunId, clearDagRun, callback) {
      let postBody = clearDagRun;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling clearDagRun");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling clearDagRun");
      }
      // verify the required parameter 'clearDagRun' is set
      if (clearDagRun === undefined || clearDagRun === null) {
        throw new Error("Missing the required parameter 'clearDagRun' when calling clearDagRun");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId
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
      let returnType = ClearDagRun200Response;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}/clear', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteDagRun operation.
     * @callback module:api/DAGRunApi~deleteDagRunCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a DAG run
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {module:api/DAGRunApi~deleteDagRunCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteDagRun(dagId, dagRunId, callback) {
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling deleteDagRun");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling deleteDagRun");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId
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
        '/dags/{dag_id}/dagRuns/{dag_run_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDagRun operation.
     * @callback module:api/DAGRunApi~getDagRunCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DAGRun} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a DAG run
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {module:api/DAGRunApi~getDagRunCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DAGRun}
     */
    getDagRun(dagId, dagRunId, callback) {
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling getDagRun");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling getDagRun");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId
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
      let returnType = DAGRun;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDagRuns operation.
     * @callback module:api/DAGRunApi~getDagRunsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DAGRunCollection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List DAG runs
     * This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs. 
     * @param {String} dagId The DAG ID.
     * @param {Object} opts Optional parameters
     * @param {Number} [limit = 100)] The numbers of items to return.
     * @param {Number} [offset] The number of items to skip before starting to collect the result set.
     * @param {Date} [executionDateGte] Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period. 
     * @param {Date} [executionDateLte] Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period. 
     * @param {Date} [startDateGte] Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
     * @param {Date} [startDateLte] Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
     * @param {Date} [endDateGte] Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
     * @param {Date} [endDateLte] Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
     * @param {Array.<String>} [state] The value can be repeated to retrieve multiple matching values (OR condition).
     * @param {String} [orderBy] The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
     * @param {module:api/DAGRunApi~getDagRunsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DAGRunCollection}
     */
    getDagRuns(dagId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling getDagRuns");
      }

      let pathParams = {
        'dag_id': dagId
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
        'state': this.apiClient.buildCollectionParam(opts['state'], 'multi'),
        'order_by': opts['orderBy']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DAGRunCollection;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getDagRunsBatch operation.
     * @callback module:api/DAGRunApi~getDagRunsBatchCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DAGRunCollection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List DAG runs (batch)
     * This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit. 
     * @param {module:model/ListDagRunsForm} listDagRunsForm 
     * @param {module:api/DAGRunApi~getDagRunsBatchCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DAGRunCollection}
     */
    getDagRunsBatch(listDagRunsForm, callback) {
      let postBody = listDagRunsForm;
      // verify the required parameter 'listDagRunsForm' is set
      if (listDagRunsForm === undefined || listDagRunsForm === null) {
        throw new Error("Missing the required parameter 'listDagRunsForm' when calling getDagRunsBatch");
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
      let returnType = DAGRunCollection;
      return this.apiClient.callApi(
        '/dags/~/dagRuns/list', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getUpstreamDatasetEvents operation.
     * @callback module:api/DAGRunApi~getUpstreamDatasetEventsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DatasetEventCollection} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get dataset events for a DAG run
     * Get datasets for a dag run.  *New in version 2.4.0* 
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {module:api/DAGRunApi~getUpstreamDatasetEventsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DatasetEventCollection}
     */
    getUpstreamDatasetEvents(dagId, dagRunId, callback) {
      let postBody = null;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling getUpstreamDatasetEvents");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling getUpstreamDatasetEvents");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId
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
      let returnType = DatasetEventCollection;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}/upstreamDatasetEvents', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postDagRun operation.
     * @callback module:api/DAGRunApi~postDagRunCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DAGRun} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Trigger a new DAG run
     * @param {String} dagId The DAG ID.
     * @param {module:model/DAGRun} dAGRun 
     * @param {module:api/DAGRunApi~postDagRunCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DAGRun}
     */
    postDagRun(dagId, dAGRun, callback) {
      let postBody = dAGRun;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling postDagRun");
      }
      // verify the required parameter 'dAGRun' is set
      if (dAGRun === undefined || dAGRun === null) {
        throw new Error("Missing the required parameter 'dAGRun' when calling postDagRun");
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
      let returnType = DAGRun;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the setDagRunNote operation.
     * @callback module:api/DAGRunApi~setDagRunNoteCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DAGRun} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update the DagRun note.
     * Update the manual user note of a DagRun.  *New in version 2.5.0* 
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {module:model/SetDagRunNote} setDagRunNote Parameters of set DagRun note.
     * @param {module:api/DAGRunApi~setDagRunNoteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DAGRun}
     */
    setDagRunNote(dagId, dagRunId, setDagRunNote, callback) {
      let postBody = setDagRunNote;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling setDagRunNote");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling setDagRunNote");
      }
      // verify the required parameter 'setDagRunNote' is set
      if (setDagRunNote === undefined || setDagRunNote === null) {
        throw new Error("Missing the required parameter 'setDagRunNote' when calling setDagRunNote");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId
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
      let returnType = DAGRun;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}/setNote', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateDagRunState operation.
     * @callback module:api/DAGRunApi~updateDagRunStateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DAGRun} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Modify a DAG run
     * Modify a DAG run.  *New in version 2.2.0* 
     * @param {String} dagId The DAG ID.
     * @param {String} dagRunId The DAG run ID.
     * @param {module:model/UpdateDagRunState} updateDagRunState 
     * @param {module:api/DAGRunApi~updateDagRunStateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DAGRun}
     */
    updateDagRunState(dagId, dagRunId, updateDagRunState, callback) {
      let postBody = updateDagRunState;
      // verify the required parameter 'dagId' is set
      if (dagId === undefined || dagId === null) {
        throw new Error("Missing the required parameter 'dagId' when calling updateDagRunState");
      }
      // verify the required parameter 'dagRunId' is set
      if (dagRunId === undefined || dagRunId === null) {
        throw new Error("Missing the required parameter 'dagRunId' when calling updateDagRunState");
      }
      // verify the required parameter 'updateDagRunState' is set
      if (updateDagRunState === undefined || updateDagRunState === null) {
        throw new Error("Missing the required parameter 'updateDagRunState' when calling updateDagRunState");
      }

      let pathParams = {
        'dag_id': dagId,
        'dag_run_id': dagRunId
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
      let returnType = DAGRun;
      return this.apiClient.callApi(
        '/dags/{dag_id}/dagRuns/{dag_run_id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
