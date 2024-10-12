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

import ApiClient from '../ApiClient';
import Job from './Job';
import SLAMiss from './SLAMiss';
import TaskState from './TaskState';
import Trigger from './Trigger';

/**
 * The TaskInstance model module.
 * @module model/TaskInstance
 * @version 2.5.3
 */
class TaskInstance {
    /**
     * Constructs a new <code>TaskInstance</code>.
     * @alias module:model/TaskInstance
     */
    constructor() { 
        
        TaskInstance.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TaskInstance</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TaskInstance} obj Optional instance to populate.
     * @return {module:model/TaskInstance} The populated <code>TaskInstance</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TaskInstance();

            if (data.hasOwnProperty('dag_id')) {
                obj['dag_id'] = ApiClient.convertToType(data['dag_id'], 'String');
            }
            if (data.hasOwnProperty('dag_run_id')) {
                obj['dag_run_id'] = ApiClient.convertToType(data['dag_run_id'], 'String');
            }
            if (data.hasOwnProperty('duration')) {
                obj['duration'] = ApiClient.convertToType(data['duration'], 'Number');
            }
            if (data.hasOwnProperty('end_date')) {
                obj['end_date'] = ApiClient.convertToType(data['end_date'], 'String');
            }
            if (data.hasOwnProperty('execution_date')) {
                obj['execution_date'] = ApiClient.convertToType(data['execution_date'], 'String');
            }
            if (data.hasOwnProperty('executor_config')) {
                obj['executor_config'] = ApiClient.convertToType(data['executor_config'], 'String');
            }
            if (data.hasOwnProperty('hostname')) {
                obj['hostname'] = ApiClient.convertToType(data['hostname'], 'String');
            }
            if (data.hasOwnProperty('map_index')) {
                obj['map_index'] = ApiClient.convertToType(data['map_index'], 'Number');
            }
            if (data.hasOwnProperty('max_tries')) {
                obj['max_tries'] = ApiClient.convertToType(data['max_tries'], 'Number');
            }
            if (data.hasOwnProperty('note')) {
                obj['note'] = ApiClient.convertToType(data['note'], 'String');
            }
            if (data.hasOwnProperty('operator')) {
                obj['operator'] = ApiClient.convertToType(data['operator'], 'String');
            }
            if (data.hasOwnProperty('pid')) {
                obj['pid'] = ApiClient.convertToType(data['pid'], 'Number');
            }
            if (data.hasOwnProperty('pool')) {
                obj['pool'] = ApiClient.convertToType(data['pool'], 'String');
            }
            if (data.hasOwnProperty('pool_slots')) {
                obj['pool_slots'] = ApiClient.convertToType(data['pool_slots'], 'Number');
            }
            if (data.hasOwnProperty('priority_weight')) {
                obj['priority_weight'] = ApiClient.convertToType(data['priority_weight'], 'Number');
            }
            if (data.hasOwnProperty('queue')) {
                obj['queue'] = ApiClient.convertToType(data['queue'], 'String');
            }
            if (data.hasOwnProperty('queued_when')) {
                obj['queued_when'] = ApiClient.convertToType(data['queued_when'], 'String');
            }
            if (data.hasOwnProperty('rendered_fields')) {
                obj['rendered_fields'] = ApiClient.convertToType(data['rendered_fields'], Object);
            }
            if (data.hasOwnProperty('sla_miss')) {
                obj['sla_miss'] = SLAMiss.constructFromObject(data['sla_miss']);
            }
            if (data.hasOwnProperty('start_date')) {
                obj['start_date'] = ApiClient.convertToType(data['start_date'], 'String');
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = TaskState.constructFromObject(data['state']);
            }
            if (data.hasOwnProperty('task_id')) {
                obj['task_id'] = ApiClient.convertToType(data['task_id'], 'String');
            }
            if (data.hasOwnProperty('trigger')) {
                obj['trigger'] = Trigger.constructFromObject(data['trigger']);
            }
            if (data.hasOwnProperty('triggerer_job')) {
                obj['triggerer_job'] = Job.constructFromObject(data['triggerer_job']);
            }
            if (data.hasOwnProperty('try_number')) {
                obj['try_number'] = ApiClient.convertToType(data['try_number'], 'Number');
            }
            if (data.hasOwnProperty('unixname')) {
                obj['unixname'] = ApiClient.convertToType(data['unixname'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TaskInstance</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TaskInstance</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['dag_id'] && !(typeof data['dag_id'] === 'string' || data['dag_id'] instanceof String)) {
            throw new Error("Expected the field `dag_id` to be a primitive type in the JSON string but got " + data['dag_id']);
        }
        // ensure the json data is a string
        if (data['dag_run_id'] && !(typeof data['dag_run_id'] === 'string' || data['dag_run_id'] instanceof String)) {
            throw new Error("Expected the field `dag_run_id` to be a primitive type in the JSON string but got " + data['dag_run_id']);
        }
        // ensure the json data is a string
        if (data['end_date'] && !(typeof data['end_date'] === 'string' || data['end_date'] instanceof String)) {
            throw new Error("Expected the field `end_date` to be a primitive type in the JSON string but got " + data['end_date']);
        }
        // ensure the json data is a string
        if (data['execution_date'] && !(typeof data['execution_date'] === 'string' || data['execution_date'] instanceof String)) {
            throw new Error("Expected the field `execution_date` to be a primitive type in the JSON string but got " + data['execution_date']);
        }
        // ensure the json data is a string
        if (data['executor_config'] && !(typeof data['executor_config'] === 'string' || data['executor_config'] instanceof String)) {
            throw new Error("Expected the field `executor_config` to be a primitive type in the JSON string but got " + data['executor_config']);
        }
        // ensure the json data is a string
        if (data['hostname'] && !(typeof data['hostname'] === 'string' || data['hostname'] instanceof String)) {
            throw new Error("Expected the field `hostname` to be a primitive type in the JSON string but got " + data['hostname']);
        }
        // ensure the json data is a string
        if (data['note'] && !(typeof data['note'] === 'string' || data['note'] instanceof String)) {
            throw new Error("Expected the field `note` to be a primitive type in the JSON string but got " + data['note']);
        }
        // ensure the json data is a string
        if (data['operator'] && !(typeof data['operator'] === 'string' || data['operator'] instanceof String)) {
            throw new Error("Expected the field `operator` to be a primitive type in the JSON string but got " + data['operator']);
        }
        // ensure the json data is a string
        if (data['pool'] && !(typeof data['pool'] === 'string' || data['pool'] instanceof String)) {
            throw new Error("Expected the field `pool` to be a primitive type in the JSON string but got " + data['pool']);
        }
        // ensure the json data is a string
        if (data['queue'] && !(typeof data['queue'] === 'string' || data['queue'] instanceof String)) {
            throw new Error("Expected the field `queue` to be a primitive type in the JSON string but got " + data['queue']);
        }
        // ensure the json data is a string
        if (data['queued_when'] && !(typeof data['queued_when'] === 'string' || data['queued_when'] instanceof String)) {
            throw new Error("Expected the field `queued_when` to be a primitive type in the JSON string but got " + data['queued_when']);
        }
        // validate the optional field `sla_miss`
        if (data['sla_miss']) { // data not null
          SLAMiss.validateJSON(data['sla_miss']);
        }
        // ensure the json data is a string
        if (data['start_date'] && !(typeof data['start_date'] === 'string' || data['start_date'] instanceof String)) {
            throw new Error("Expected the field `start_date` to be a primitive type in the JSON string but got " + data['start_date']);
        }
        // ensure the json data is a string
        if (data['task_id'] && !(typeof data['task_id'] === 'string' || data['task_id'] instanceof String)) {
            throw new Error("Expected the field `task_id` to be a primitive type in the JSON string but got " + data['task_id']);
        }
        // validate the optional field `trigger`
        if (data['trigger']) { // data not null
          Trigger.validateJSON(data['trigger']);
        }
        // validate the optional field `triggerer_job`
        if (data['triggerer_job']) { // data not null
          Job.validateJSON(data['triggerer_job']);
        }
        // ensure the json data is a string
        if (data['unixname'] && !(typeof data['unixname'] === 'string' || data['unixname'] instanceof String)) {
            throw new Error("Expected the field `unixname` to be a primitive type in the JSON string but got " + data['unixname']);
        }

        return true;
    }


}



/**
 * @member {String} dag_id
 */
TaskInstance.prototype['dag_id'] = undefined;

/**
 * The DagRun ID for this task instance  *New in version 2.3.0* 
 * @member {String} dag_run_id
 */
TaskInstance.prototype['dag_run_id'] = undefined;

/**
 * @member {Number} duration
 */
TaskInstance.prototype['duration'] = undefined;

/**
 * @member {String} end_date
 */
TaskInstance.prototype['end_date'] = undefined;

/**
 * @member {String} execution_date
 */
TaskInstance.prototype['execution_date'] = undefined;

/**
 * @member {String} executor_config
 */
TaskInstance.prototype['executor_config'] = undefined;

/**
 * @member {String} hostname
 */
TaskInstance.prototype['hostname'] = undefined;

/**
 * @member {Number} map_index
 */
TaskInstance.prototype['map_index'] = undefined;

/**
 * @member {Number} max_tries
 */
TaskInstance.prototype['max_tries'] = undefined;

/**
 * Contains manually entered notes by the user about the TaskInstance.  *New in version 2.5.0* 
 * @member {String} note
 */
TaskInstance.prototype['note'] = undefined;

/**
 * *Changed in version 2.1.1*&#58; Field becomes nullable. 
 * @member {String} operator
 */
TaskInstance.prototype['operator'] = undefined;

/**
 * @member {Number} pid
 */
TaskInstance.prototype['pid'] = undefined;

/**
 * @member {String} pool
 */
TaskInstance.prototype['pool'] = undefined;

/**
 * @member {Number} pool_slots
 */
TaskInstance.prototype['pool_slots'] = undefined;

/**
 * @member {Number} priority_weight
 */
TaskInstance.prototype['priority_weight'] = undefined;

/**
 * @member {String} queue
 */
TaskInstance.prototype['queue'] = undefined;

/**
 * @member {String} queued_when
 */
TaskInstance.prototype['queued_when'] = undefined;

/**
 * JSON object describing rendered fields.  *New in version 2.3.0* 
 * @member {Object} rendered_fields
 */
TaskInstance.prototype['rendered_fields'] = undefined;

/**
 * @member {module:model/SLAMiss} sla_miss
 */
TaskInstance.prototype['sla_miss'] = undefined;

/**
 * @member {String} start_date
 */
TaskInstance.prototype['start_date'] = undefined;

/**
 * @member {module:model/TaskState} state
 */
TaskInstance.prototype['state'] = undefined;

/**
 * @member {String} task_id
 */
TaskInstance.prototype['task_id'] = undefined;

/**
 * @member {module:model/Trigger} trigger
 */
TaskInstance.prototype['trigger'] = undefined;

/**
 * @member {module:model/Job} triggerer_job
 */
TaskInstance.prototype['triggerer_job'] = undefined;

/**
 * @member {Number} try_number
 */
TaskInstance.prototype['try_number'] = undefined;

/**
 * @member {String} unixname
 */
TaskInstance.prototype['unixname'] = undefined;






export default TaskInstance;

