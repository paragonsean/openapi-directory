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


import ApiClient from './ApiClient';
import Action from './model/Action';
import ActionCollection from './model/ActionCollection';
import ActionResource from './model/ActionResource';
import BasicDAGRun from './model/BasicDAGRun';
import ClassReference from './model/ClassReference';
import ClearDagRun from './model/ClearDagRun';
import ClearDagRun200Response from './model/ClearDagRun200Response';
import ClearTaskInstances from './model/ClearTaskInstances';
import CollectionInfo from './model/CollectionInfo';
import Config from './model/Config';
import ConfigOption from './model/ConfigOption';
import ConfigSection from './model/ConfigSection';
import Connection from './model/Connection';
import ConnectionCollection from './model/ConnectionCollection';
import ConnectionCollectionItem from './model/ConnectionCollectionItem';
import ConnectionTest from './model/ConnectionTest';
import CronExpression from './model/CronExpression';
import DAG from './model/DAG';
import DAGCollection from './model/DAGCollection';
import DAGDetail from './model/DAGDetail';
import DAGRun from './model/DAGRun';
import DAGRunCollection from './model/DAGRunCollection';
import DagScheduleDatasetReference from './model/DagScheduleDatasetReference';
import DagState from './model/DagState';
import DagWarning from './model/DagWarning';
import DagWarningCollection from './model/DagWarningCollection';
import Dataset from './model/Dataset';
import DatasetCollection from './model/DatasetCollection';
import DatasetEvent from './model/DatasetEvent';
import DatasetEventCollection from './model/DatasetEventCollection';
import Error from './model/Error';
import EventLog from './model/EventLog';
import EventLogCollection from './model/EventLogCollection';
import ExtraLink from './model/ExtraLink';
import ExtraLinkCollection from './model/ExtraLinkCollection';
import GetDagSource200Response from './model/GetDagSource200Response';
import GetLog200Response from './model/GetLog200Response';
import GetProviders200Response from './model/GetProviders200Response';
import HealthInfo from './model/HealthInfo';
import HealthStatus from './model/HealthStatus';
import ImportError from './model/ImportError';
import ImportErrorCollection from './model/ImportErrorCollection';
import Job from './model/Job';
import ListDagRunsForm from './model/ListDagRunsForm';
import ListTaskInstanceForm from './model/ListTaskInstanceForm';
import MetadatabaseStatus from './model/MetadatabaseStatus';
import PluginCollection from './model/PluginCollection';
import PluginCollectionItem from './model/PluginCollectionItem';
import Pool from './model/Pool';
import PoolCollection from './model/PoolCollection';
import Provider from './model/Provider';
import ProviderCollection from './model/ProviderCollection';
import RelativeDelta from './model/RelativeDelta';
import Resource from './model/Resource';
import Role from './model/Role';
import RoleCollection from './model/RoleCollection';
import SLAMiss from './model/SLAMiss';
import ScheduleInterval from './model/ScheduleInterval';
import SchedulerStatus from './model/SchedulerStatus';
import SetDagRunNote from './model/SetDagRunNote';
import SetTaskInstanceNote from './model/SetTaskInstanceNote';
import Tag from './model/Tag';
import Task from './model/Task';
import TaskCollection from './model/TaskCollection';
import TaskExtraLinksInner from './model/TaskExtraLinksInner';
import TaskInstance from './model/TaskInstance';
import TaskInstanceCollection from './model/TaskInstanceCollection';
import TaskInstanceReference from './model/TaskInstanceReference';
import TaskInstanceReferenceCollection from './model/TaskInstanceReferenceCollection';
import TaskOutletDatasetReference from './model/TaskOutletDatasetReference';
import TaskState from './model/TaskState';
import TimeDelta from './model/TimeDelta';
import Trigger from './model/Trigger';
import TriggerRule from './model/TriggerRule';
import UpdateDagRunState from './model/UpdateDagRunState';
import UpdateTaskInstance from './model/UpdateTaskInstance';
import UpdateTaskInstancesState from './model/UpdateTaskInstancesState';
import User from './model/User';
import UserCollection from './model/UserCollection';
import UserCollectionItem from './model/UserCollectionItem';
import UserCollectionItemRolesInner from './model/UserCollectionItemRolesInner';
import Variable from './model/Variable';
import VariableCollection from './model/VariableCollection';
import VariableCollectionItem from './model/VariableCollectionItem';
import VersionInfo from './model/VersionInfo';
import WeightRule from './model/WeightRule';
import XCom from './model/XCom';
import XComCollection from './model/XComCollection';
import XComCollectionItem from './model/XComCollectionItem';
import ConfigApi from './api/ConfigApi';
import ConnectionApi from './api/ConnectionApi';
import DAGApi from './api/DAGApi';
import DAGRunApi from './api/DAGRunApi';
import DagWarningApi from './api/DagWarningApi';
import DatasetApi from './api/DatasetApi';
import EventLogApi from './api/EventLogApi';
import ImportErrorApi from './api/ImportErrorApi';
import MonitoringApi from './api/MonitoringApi';
import PermissionApi from './api/PermissionApi';
import PluginApi from './api/PluginApi';
import PoolApi from './api/PoolApi';
import ProviderApi from './api/ProviderApi';
import RoleApi from './api/RoleApi';
import TaskInstanceApi from './api/TaskInstanceApi';
import UserApi from './api/UserApi';
import VariableApi from './api/VariableApi';
import XComApi from './api/XComApi';


/**
* # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept &#x60;JSON&#x60; as input and return &#x60;JSON&#x60; responses. This means that you must usually add the following headers to your request: &#x60;&#x60;&#x60; Content-type: application/json Accept: application/json &#x60;&#x60;&#x60;  ## Resources  The term &#x60;resource&#x60; refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint&#39;s corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: &#x60;dagRuns&#x60;.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP &#x60;POST&#x60; request with the resource&#39;s required metadata in the request body. The response returns a &#x60;201 Created&#x60; response code upon success with the resource&#39;s metadata, including its internal &#x60;id&#x60;, in the response body.  ### Read  The HTTP &#x60;GET&#x60; request can be used to read a resource or to list a number of resources.  A resource&#39;s &#x60;id&#x60; can be submitted in the request parameters to read a specific resource. The response usually returns a &#x60;200 OK&#x60; response code upon success, with the resource&#39;s metadata in the response body.  If a &#x60;GET&#x60; request does not include a specific resource &#x60;id&#x60;, it is treated as a list request. The response usually returns a &#x60;200 OK&#x60; response code upon success, with an object containing a list of resources&#39; metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: &#x60;&#x60;&#x60; v1/connections?limit&#x3D;25&amp;offset&#x3D;25 &#x60;&#x60;&#x60;  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource &#x60;id&#x60;, and is typically done using an HTTP &#x60;PATCH&#x60; request, with the fields to modify in the request body. The response usually returns a &#x60;200 OK&#x60; response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource &#x60;id&#x60; and is typically executing via an HTTP &#x60;DELETE&#x60; request. The response usually returns a &#x60;204 No Content&#x60; response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. &#x60;&#x60;&#x60;json {     \&quot;name\&quot;: \&quot;string\&quot;,     \&quot;slots\&quot;: 0,     \&quot;occupied_slots\&quot;: 0,     \&quot;used_slots\&quot;: 0,     \&quot;queued_slots\&quot;: 0,     \&quot;open_slots\&quot;: 0 } &#x60;&#x60;&#x60;  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using &#x60;update_mask&#x60; makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren&#39;t specified in the field mask, leaving them with their current values.  Example: &#x60;&#x60;&#x60;   resource &#x3D; request.get(&#39;/resource/my-id&#39;).json()   resource[&#39;my_field&#39;] &#x3D; &#39;new-value&#39;   request.patch(&#39;/resource/my-id?update_mask&#x3D;my_field&#39;, data&#x3D;json.dumps(resource)) &#x60;&#x60;&#x60;  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: &#x60;&#x60;&#x60;bash curl -X PATCH &#39;https://example.com/api/v1/dags/{dag_id}?update_mask&#x3D;is_paused&#39; \\ -H &#39;Content-Type: application/json&#39; \\ --user \&quot;username:password\&quot; \\ -d &#39;{     \&quot;is_paused\&quot;: true }&#39; &#x60;&#x60;&#x60;  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use &#x60;airflow config get-value api auth_backends&#x60; command as in the example below. &#x60;&#x60;&#x60;bash $ airflow config get-value api auth_backends airflow.api.auth.backend.basic_auth &#x60;&#x60;&#x60; The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, e.g. the resource it tries to create already exists.  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request. .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var AirflowApiStable = require('index'); // See note below*.
* var xxxSvc = new AirflowApiStable.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new AirflowApiStable.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new AirflowApiStable.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new AirflowApiStable.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2.5.3
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Action model constructor.
     * @property {module:model/Action}
     */
    Action,

    /**
     * The ActionCollection model constructor.
     * @property {module:model/ActionCollection}
     */
    ActionCollection,

    /**
     * The ActionResource model constructor.
     * @property {module:model/ActionResource}
     */
    ActionResource,

    /**
     * The BasicDAGRun model constructor.
     * @property {module:model/BasicDAGRun}
     */
    BasicDAGRun,

    /**
     * The ClassReference model constructor.
     * @property {module:model/ClassReference}
     */
    ClassReference,

    /**
     * The ClearDagRun model constructor.
     * @property {module:model/ClearDagRun}
     */
    ClearDagRun,

    /**
     * The ClearDagRun200Response model constructor.
     * @property {module:model/ClearDagRun200Response}
     */
    ClearDagRun200Response,

    /**
     * The ClearTaskInstances model constructor.
     * @property {module:model/ClearTaskInstances}
     */
    ClearTaskInstances,

    /**
     * The CollectionInfo model constructor.
     * @property {module:model/CollectionInfo}
     */
    CollectionInfo,

    /**
     * The Config model constructor.
     * @property {module:model/Config}
     */
    Config,

    /**
     * The ConfigOption model constructor.
     * @property {module:model/ConfigOption}
     */
    ConfigOption,

    /**
     * The ConfigSection model constructor.
     * @property {module:model/ConfigSection}
     */
    ConfigSection,

    /**
     * The Connection model constructor.
     * @property {module:model/Connection}
     */
    Connection,

    /**
     * The ConnectionCollection model constructor.
     * @property {module:model/ConnectionCollection}
     */
    ConnectionCollection,

    /**
     * The ConnectionCollectionItem model constructor.
     * @property {module:model/ConnectionCollectionItem}
     */
    ConnectionCollectionItem,

    /**
     * The ConnectionTest model constructor.
     * @property {module:model/ConnectionTest}
     */
    ConnectionTest,

    /**
     * The CronExpression model constructor.
     * @property {module:model/CronExpression}
     */
    CronExpression,

    /**
     * The DAG model constructor.
     * @property {module:model/DAG}
     */
    DAG,

    /**
     * The DAGCollection model constructor.
     * @property {module:model/DAGCollection}
     */
    DAGCollection,

    /**
     * The DAGDetail model constructor.
     * @property {module:model/DAGDetail}
     */
    DAGDetail,

    /**
     * The DAGRun model constructor.
     * @property {module:model/DAGRun}
     */
    DAGRun,

    /**
     * The DAGRunCollection model constructor.
     * @property {module:model/DAGRunCollection}
     */
    DAGRunCollection,

    /**
     * The DagScheduleDatasetReference model constructor.
     * @property {module:model/DagScheduleDatasetReference}
     */
    DagScheduleDatasetReference,

    /**
     * The DagState model constructor.
     * @property {module:model/DagState}
     */
    DagState,

    /**
     * The DagWarning model constructor.
     * @property {module:model/DagWarning}
     */
    DagWarning,

    /**
     * The DagWarningCollection model constructor.
     * @property {module:model/DagWarningCollection}
     */
    DagWarningCollection,

    /**
     * The Dataset model constructor.
     * @property {module:model/Dataset}
     */
    Dataset,

    /**
     * The DatasetCollection model constructor.
     * @property {module:model/DatasetCollection}
     */
    DatasetCollection,

    /**
     * The DatasetEvent model constructor.
     * @property {module:model/DatasetEvent}
     */
    DatasetEvent,

    /**
     * The DatasetEventCollection model constructor.
     * @property {module:model/DatasetEventCollection}
     */
    DatasetEventCollection,

    /**
     * The Error model constructor.
     * @property {module:model/Error}
     */
    Error,

    /**
     * The EventLog model constructor.
     * @property {module:model/EventLog}
     */
    EventLog,

    /**
     * The EventLogCollection model constructor.
     * @property {module:model/EventLogCollection}
     */
    EventLogCollection,

    /**
     * The ExtraLink model constructor.
     * @property {module:model/ExtraLink}
     */
    ExtraLink,

    /**
     * The ExtraLinkCollection model constructor.
     * @property {module:model/ExtraLinkCollection}
     */
    ExtraLinkCollection,

    /**
     * The GetDagSource200Response model constructor.
     * @property {module:model/GetDagSource200Response}
     */
    GetDagSource200Response,

    /**
     * The GetLog200Response model constructor.
     * @property {module:model/GetLog200Response}
     */
    GetLog200Response,

    /**
     * The GetProviders200Response model constructor.
     * @property {module:model/GetProviders200Response}
     */
    GetProviders200Response,

    /**
     * The HealthInfo model constructor.
     * @property {module:model/HealthInfo}
     */
    HealthInfo,

    /**
     * The HealthStatus model constructor.
     * @property {module:model/HealthStatus}
     */
    HealthStatus,

    /**
     * The ImportError model constructor.
     * @property {module:model/ImportError}
     */
    ImportError,

    /**
     * The ImportErrorCollection model constructor.
     * @property {module:model/ImportErrorCollection}
     */
    ImportErrorCollection,

    /**
     * The Job model constructor.
     * @property {module:model/Job}
     */
    Job,

    /**
     * The ListDagRunsForm model constructor.
     * @property {module:model/ListDagRunsForm}
     */
    ListDagRunsForm,

    /**
     * The ListTaskInstanceForm model constructor.
     * @property {module:model/ListTaskInstanceForm}
     */
    ListTaskInstanceForm,

    /**
     * The MetadatabaseStatus model constructor.
     * @property {module:model/MetadatabaseStatus}
     */
    MetadatabaseStatus,

    /**
     * The PluginCollection model constructor.
     * @property {module:model/PluginCollection}
     */
    PluginCollection,

    /**
     * The PluginCollectionItem model constructor.
     * @property {module:model/PluginCollectionItem}
     */
    PluginCollectionItem,

    /**
     * The Pool model constructor.
     * @property {module:model/Pool}
     */
    Pool,

    /**
     * The PoolCollection model constructor.
     * @property {module:model/PoolCollection}
     */
    PoolCollection,

    /**
     * The Provider model constructor.
     * @property {module:model/Provider}
     */
    Provider,

    /**
     * The ProviderCollection model constructor.
     * @property {module:model/ProviderCollection}
     */
    ProviderCollection,

    /**
     * The RelativeDelta model constructor.
     * @property {module:model/RelativeDelta}
     */
    RelativeDelta,

    /**
     * The Resource model constructor.
     * @property {module:model/Resource}
     */
    Resource,

    /**
     * The Role model constructor.
     * @property {module:model/Role}
     */
    Role,

    /**
     * The RoleCollection model constructor.
     * @property {module:model/RoleCollection}
     */
    RoleCollection,

    /**
     * The SLAMiss model constructor.
     * @property {module:model/SLAMiss}
     */
    SLAMiss,

    /**
     * The ScheduleInterval model constructor.
     * @property {module:model/ScheduleInterval}
     */
    ScheduleInterval,

    /**
     * The SchedulerStatus model constructor.
     * @property {module:model/SchedulerStatus}
     */
    SchedulerStatus,

    /**
     * The SetDagRunNote model constructor.
     * @property {module:model/SetDagRunNote}
     */
    SetDagRunNote,

    /**
     * The SetTaskInstanceNote model constructor.
     * @property {module:model/SetTaskInstanceNote}
     */
    SetTaskInstanceNote,

    /**
     * The Tag model constructor.
     * @property {module:model/Tag}
     */
    Tag,

    /**
     * The Task model constructor.
     * @property {module:model/Task}
     */
    Task,

    /**
     * The TaskCollection model constructor.
     * @property {module:model/TaskCollection}
     */
    TaskCollection,

    /**
     * The TaskExtraLinksInner model constructor.
     * @property {module:model/TaskExtraLinksInner}
     */
    TaskExtraLinksInner,

    /**
     * The TaskInstance model constructor.
     * @property {module:model/TaskInstance}
     */
    TaskInstance,

    /**
     * The TaskInstanceCollection model constructor.
     * @property {module:model/TaskInstanceCollection}
     */
    TaskInstanceCollection,

    /**
     * The TaskInstanceReference model constructor.
     * @property {module:model/TaskInstanceReference}
     */
    TaskInstanceReference,

    /**
     * The TaskInstanceReferenceCollection model constructor.
     * @property {module:model/TaskInstanceReferenceCollection}
     */
    TaskInstanceReferenceCollection,

    /**
     * The TaskOutletDatasetReference model constructor.
     * @property {module:model/TaskOutletDatasetReference}
     */
    TaskOutletDatasetReference,

    /**
     * The TaskState model constructor.
     * @property {module:model/TaskState}
     */
    TaskState,

    /**
     * The TimeDelta model constructor.
     * @property {module:model/TimeDelta}
     */
    TimeDelta,

    /**
     * The Trigger model constructor.
     * @property {module:model/Trigger}
     */
    Trigger,

    /**
     * The TriggerRule model constructor.
     * @property {module:model/TriggerRule}
     */
    TriggerRule,

    /**
     * The UpdateDagRunState model constructor.
     * @property {module:model/UpdateDagRunState}
     */
    UpdateDagRunState,

    /**
     * The UpdateTaskInstance model constructor.
     * @property {module:model/UpdateTaskInstance}
     */
    UpdateTaskInstance,

    /**
     * The UpdateTaskInstancesState model constructor.
     * @property {module:model/UpdateTaskInstancesState}
     */
    UpdateTaskInstancesState,

    /**
     * The User model constructor.
     * @property {module:model/User}
     */
    User,

    /**
     * The UserCollection model constructor.
     * @property {module:model/UserCollection}
     */
    UserCollection,

    /**
     * The UserCollectionItem model constructor.
     * @property {module:model/UserCollectionItem}
     */
    UserCollectionItem,

    /**
     * The UserCollectionItemRolesInner model constructor.
     * @property {module:model/UserCollectionItemRolesInner}
     */
    UserCollectionItemRolesInner,

    /**
     * The Variable model constructor.
     * @property {module:model/Variable}
     */
    Variable,

    /**
     * The VariableCollection model constructor.
     * @property {module:model/VariableCollection}
     */
    VariableCollection,

    /**
     * The VariableCollectionItem model constructor.
     * @property {module:model/VariableCollectionItem}
     */
    VariableCollectionItem,

    /**
     * The VersionInfo model constructor.
     * @property {module:model/VersionInfo}
     */
    VersionInfo,

    /**
     * The WeightRule model constructor.
     * @property {module:model/WeightRule}
     */
    WeightRule,

    /**
     * The XCom model constructor.
     * @property {module:model/XCom}
     */
    XCom,

    /**
     * The XComCollection model constructor.
     * @property {module:model/XComCollection}
     */
    XComCollection,

    /**
     * The XComCollectionItem model constructor.
     * @property {module:model/XComCollectionItem}
     */
    XComCollectionItem,

    /**
    * The ConfigApi service constructor.
    * @property {module:api/ConfigApi}
    */
    ConfigApi,

    /**
    * The ConnectionApi service constructor.
    * @property {module:api/ConnectionApi}
    */
    ConnectionApi,

    /**
    * The DAGApi service constructor.
    * @property {module:api/DAGApi}
    */
    DAGApi,

    /**
    * The DAGRunApi service constructor.
    * @property {module:api/DAGRunApi}
    */
    DAGRunApi,

    /**
    * The DagWarningApi service constructor.
    * @property {module:api/DagWarningApi}
    */
    DagWarningApi,

    /**
    * The DatasetApi service constructor.
    * @property {module:api/DatasetApi}
    */
    DatasetApi,

    /**
    * The EventLogApi service constructor.
    * @property {module:api/EventLogApi}
    */
    EventLogApi,

    /**
    * The ImportErrorApi service constructor.
    * @property {module:api/ImportErrorApi}
    */
    ImportErrorApi,

    /**
    * The MonitoringApi service constructor.
    * @property {module:api/MonitoringApi}
    */
    MonitoringApi,

    /**
    * The PermissionApi service constructor.
    * @property {module:api/PermissionApi}
    */
    PermissionApi,

    /**
    * The PluginApi service constructor.
    * @property {module:api/PluginApi}
    */
    PluginApi,

    /**
    * The PoolApi service constructor.
    * @property {module:api/PoolApi}
    */
    PoolApi,

    /**
    * The ProviderApi service constructor.
    * @property {module:api/ProviderApi}
    */
    ProviderApi,

    /**
    * The RoleApi service constructor.
    * @property {module:api/RoleApi}
    */
    RoleApi,

    /**
    * The TaskInstanceApi service constructor.
    * @property {module:api/TaskInstanceApi}
    */
    TaskInstanceApi,

    /**
    * The UserApi service constructor.
    * @property {module:api/UserApi}
    */
    UserApi,

    /**
    * The VariableApi service constructor.
    * @property {module:api/VariableApi}
    */
    VariableApi,

    /**
    * The XComApi service constructor.
    * @property {module:api/XComApi}
    */
    XComApi
};
