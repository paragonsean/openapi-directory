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
import ClassReference from './ClassReference';
import DAG from './DAG';
import TaskExtraLinksInner from './TaskExtraLinksInner';
import TimeDelta from './TimeDelta';
import TriggerRule from './TriggerRule';
import WeightRule from './WeightRule';

/**
 * The Task model module.
 * @module model/Task
 * @version 2.5.3
 */
class Task {
    /**
     * Constructs a new <code>Task</code>.
     * For details see: [airflow.models.BaseOperator](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/index.html#airflow.models.BaseOperator) 
     * @alias module:model/Task
     */
    constructor() { 
        
        Task.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Task</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Task} obj Optional instance to populate.
     * @return {module:model/Task} The populated <code>Task</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Task();

            if (data.hasOwnProperty('class_ref')) {
                obj['class_ref'] = ClassReference.constructFromObject(data['class_ref']);
            }
            if (data.hasOwnProperty('depends_on_past')) {
                obj['depends_on_past'] = ApiClient.convertToType(data['depends_on_past'], 'Boolean');
            }
            if (data.hasOwnProperty('downstream_task_ids')) {
                obj['downstream_task_ids'] = ApiClient.convertToType(data['downstream_task_ids'], ['String']);
            }
            if (data.hasOwnProperty('end_date')) {
                obj['end_date'] = ApiClient.convertToType(data['end_date'], 'Date');
            }
            if (data.hasOwnProperty('execution_timeout')) {
                obj['execution_timeout'] = TimeDelta.constructFromObject(data['execution_timeout']);
            }
            if (data.hasOwnProperty('extra_links')) {
                obj['extra_links'] = ApiClient.convertToType(data['extra_links'], [TaskExtraLinksInner]);
            }
            if (data.hasOwnProperty('is_mapped')) {
                obj['is_mapped'] = ApiClient.convertToType(data['is_mapped'], 'Boolean');
            }
            if (data.hasOwnProperty('owner')) {
                obj['owner'] = ApiClient.convertToType(data['owner'], 'String');
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
            if (data.hasOwnProperty('retries')) {
                obj['retries'] = ApiClient.convertToType(data['retries'], 'Number');
            }
            if (data.hasOwnProperty('retry_delay')) {
                obj['retry_delay'] = TimeDelta.constructFromObject(data['retry_delay']);
            }
            if (data.hasOwnProperty('retry_exponential_backoff')) {
                obj['retry_exponential_backoff'] = ApiClient.convertToType(data['retry_exponential_backoff'], 'Boolean');
            }
            if (data.hasOwnProperty('start_date')) {
                obj['start_date'] = ApiClient.convertToType(data['start_date'], 'Date');
            }
            if (data.hasOwnProperty('sub_dag')) {
                obj['sub_dag'] = DAG.constructFromObject(data['sub_dag']);
            }
            if (data.hasOwnProperty('task_id')) {
                obj['task_id'] = ApiClient.convertToType(data['task_id'], 'String');
            }
            if (data.hasOwnProperty('template_fields')) {
                obj['template_fields'] = ApiClient.convertToType(data['template_fields'], ['String']);
            }
            if (data.hasOwnProperty('trigger_rule')) {
                obj['trigger_rule'] = TriggerRule.constructFromObject(data['trigger_rule']);
            }
            if (data.hasOwnProperty('ui_color')) {
                obj['ui_color'] = ApiClient.convertToType(data['ui_color'], 'String');
            }
            if (data.hasOwnProperty('ui_fgcolor')) {
                obj['ui_fgcolor'] = ApiClient.convertToType(data['ui_fgcolor'], 'String');
            }
            if (data.hasOwnProperty('wait_for_downstream')) {
                obj['wait_for_downstream'] = ApiClient.convertToType(data['wait_for_downstream'], 'Boolean');
            }
            if (data.hasOwnProperty('weight_rule')) {
                obj['weight_rule'] = WeightRule.constructFromObject(data['weight_rule']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Task</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Task</code>.
     */
    static validateJSON(data) {
        // validate the optional field `class_ref`
        if (data['class_ref']) { // data not null
          ClassReference.validateJSON(data['class_ref']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['downstream_task_ids'])) {
            throw new Error("Expected the field `downstream_task_ids` to be an array in the JSON data but got " + data['downstream_task_ids']);
        }
        // validate the optional field `execution_timeout`
        if (data['execution_timeout']) { // data not null
          TimeDelta.validateJSON(data['execution_timeout']);
        }
        if (data['extra_links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['extra_links'])) {
                throw new Error("Expected the field `extra_links` to be an array in the JSON data but got " + data['extra_links']);
            }
            // validate the optional field `extra_links` (array)
            for (const item of data['extra_links']) {
                TaskExtraLinksInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['owner'] && !(typeof data['owner'] === 'string' || data['owner'] instanceof String)) {
            throw new Error("Expected the field `owner` to be a primitive type in the JSON string but got " + data['owner']);
        }
        // ensure the json data is a string
        if (data['pool'] && !(typeof data['pool'] === 'string' || data['pool'] instanceof String)) {
            throw new Error("Expected the field `pool` to be a primitive type in the JSON string but got " + data['pool']);
        }
        // ensure the json data is a string
        if (data['queue'] && !(typeof data['queue'] === 'string' || data['queue'] instanceof String)) {
            throw new Error("Expected the field `queue` to be a primitive type in the JSON string but got " + data['queue']);
        }
        // validate the optional field `retry_delay`
        if (data['retry_delay']) { // data not null
          TimeDelta.validateJSON(data['retry_delay']);
        }
        // validate the optional field `sub_dag`
        if (data['sub_dag']) { // data not null
          DAG.validateJSON(data['sub_dag']);
        }
        // ensure the json data is a string
        if (data['task_id'] && !(typeof data['task_id'] === 'string' || data['task_id'] instanceof String)) {
            throw new Error("Expected the field `task_id` to be a primitive type in the JSON string but got " + data['task_id']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['template_fields'])) {
            throw new Error("Expected the field `template_fields` to be an array in the JSON data but got " + data['template_fields']);
        }
        // ensure the json data is a string
        if (data['ui_color'] && !(typeof data['ui_color'] === 'string' || data['ui_color'] instanceof String)) {
            throw new Error("Expected the field `ui_color` to be a primitive type in the JSON string but got " + data['ui_color']);
        }
        // ensure the json data is a string
        if (data['ui_fgcolor'] && !(typeof data['ui_fgcolor'] === 'string' || data['ui_fgcolor'] instanceof String)) {
            throw new Error("Expected the field `ui_fgcolor` to be a primitive type in the JSON string but got " + data['ui_fgcolor']);
        }

        return true;
    }


}



/**
 * @member {module:model/ClassReference} class_ref
 */
Task.prototype['class_ref'] = undefined;

/**
 * @member {Boolean} depends_on_past
 */
Task.prototype['depends_on_past'] = undefined;

/**
 * @member {Array.<String>} downstream_task_ids
 */
Task.prototype['downstream_task_ids'] = undefined;

/**
 * @member {Date} end_date
 */
Task.prototype['end_date'] = undefined;

/**
 * @member {module:model/TimeDelta} execution_timeout
 */
Task.prototype['execution_timeout'] = undefined;

/**
 * @member {Array.<module:model/TaskExtraLinksInner>} extra_links
 */
Task.prototype['extra_links'] = undefined;

/**
 * @member {Boolean} is_mapped
 */
Task.prototype['is_mapped'] = undefined;

/**
 * @member {String} owner
 */
Task.prototype['owner'] = undefined;

/**
 * @member {String} pool
 */
Task.prototype['pool'] = undefined;

/**
 * @member {Number} pool_slots
 */
Task.prototype['pool_slots'] = undefined;

/**
 * @member {Number} priority_weight
 */
Task.prototype['priority_weight'] = undefined;

/**
 * @member {String} queue
 */
Task.prototype['queue'] = undefined;

/**
 * @member {Number} retries
 */
Task.prototype['retries'] = undefined;

/**
 * @member {module:model/TimeDelta} retry_delay
 */
Task.prototype['retry_delay'] = undefined;

/**
 * @member {Boolean} retry_exponential_backoff
 */
Task.prototype['retry_exponential_backoff'] = undefined;

/**
 * @member {Date} start_date
 */
Task.prototype['start_date'] = undefined;

/**
 * @member {module:model/DAG} sub_dag
 */
Task.prototype['sub_dag'] = undefined;

/**
 * @member {String} task_id
 */
Task.prototype['task_id'] = undefined;

/**
 * @member {Array.<String>} template_fields
 */
Task.prototype['template_fields'] = undefined;

/**
 * @member {module:model/TriggerRule} trigger_rule
 */
Task.prototype['trigger_rule'] = undefined;

/**
 * Color in hexadecimal notation.
 * @member {String} ui_color
 */
Task.prototype['ui_color'] = undefined;

/**
 * Color in hexadecimal notation.
 * @member {String} ui_fgcolor
 */
Task.prototype['ui_fgcolor'] = undefined;

/**
 * @member {Boolean} wait_for_downstream
 */
Task.prototype['wait_for_downstream'] = undefined;

/**
 * @member {module:model/WeightRule} weight_rule
 */
Task.prototype['weight_rule'] = undefined;






export default Task;

