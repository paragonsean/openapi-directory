# airflow_api__stable

AirflowApiStable - JavaScript client for airflow_api__stable
# Overview

To facilitate management, Apache Airflow supports a range of REST API endpoints across its
objects.
This section provides an overview of the API design, methods, and supported use cases.

Most of the endpoints accept `JSON` as input and return `JSON` responses.
This means that you must usually add the following headers to your request:
```
Content-type: application/json
Accept: application/json
```

## Resources

The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its
endpoint's corresponding resource.
The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.

Resource names are used as part of endpoint URLs, as well as in API parameters and responses.

## CRUD Operations

The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources.
You can review the standards for these operations and their standard parameters below.

Some endpoints have special behavior as exceptions.

### Create

To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata
in the request body.
The response returns a `201 Created` response code upon success with the resource's metadata, including
its internal `id`, in the response body.

### Read

The HTTP `GET` request can be used to read a resource or to list a number of resources.

A resource's `id` can be submitted in the request parameters to read a specific resource.
The response usually returns a `200 OK` response code upon success, with the resource's metadata in
the response body.

If a `GET` request does not include a specific resource `id`, it is treated as a list request.
The response usually returns a `200 OK` response code upon success, with an object containing a list
of resources' metadata in the response body.

When reading resources, some common query parameters are usually available. e.g.:
```
v1/connections?limit=25&offset=25
```

|Query Parameter|Type|Description|
|---------------|----|-----------|
|limit|integer|Maximum number of objects to fetch. Usually 25 by default|
|offset|integer|Offset after which to start returning objects. For use with limit query parameter.|

### Update

Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request,
with the fields to modify in the request body.
The response usually returns a `200 OK` response code upon success, with information about the modified
resource in the response body.

### Delete

Deleting a resource requires the resource `id` and is typically executing via an HTTP `DELETE` request.
The response usually returns a `204 No Content` response code upon success.

## Conventions

- Resource names are plural and expressed in camelCase.
- Names are consistent between URL parameter name and field name.

- Field names are in snake_case.
```json
{
    \"name\": \"string\",
    \"slots\": 0,
    \"occupied_slots\": 0,
    \"used_slots\": 0,
    \"queued_slots\": 0,
    \"open_slots\": 0
}
```

### Update Mask

Update mask is available as a query parameter in patch endpoints. It is used to notify the
API which fields you want to update. Using `update_mask` makes it easier to update objects
by helping the server know which fields to update in an object instead of updating all fields.
The update request ignores any fields that aren't specified in the field mask, leaving them with
their current values.

Example:
```
  resource = request.get('/resource/my-id').json()
  resource['my_field'] = 'new-value'
  request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource))
```

## Versioning and Endpoint Lifecycle

- API versioning is not synchronized to specific releases of the Apache Airflow.
- APIs are designed to be backward compatible.
- Any changes to the API will first go through a deprecation phase.

# Trying the API

You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/),
[Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test
the Apache Airflow API.

Note that you will need to pass credentials data.

For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used:
```bash
curl -X PATCH 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\
-H 'Content-Type: application/json' \\
--user \"username:password\" \\
-d '{
    \"is_paused\": true
}'
```

Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/),
it is possible to import the API specifications directly:

1. Download the API specification by clicking the **Download** button at top of this document
2. Import the JSON specification in the graphical tool of your choice.
  - In *Postman*, you can click the **import** button at the top
  - With *Insomnia*, you can just drag-and-drop the file on the UI

Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on
the **Code** button.

## Enabling CORS

[Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
is a browser security feature that restricts HTTP requests that are
initiated from scripts running in the browser.

For details on enabling/configuring CORS, see
[Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).

# Authentication

To be able to meet the requirements of many organizations, Airflow supports many authentication methods,
and it is even possible to add your own method.

If you want to check which auth backend is currently set, you can use
`airflow config get-value api auth_backends` command as in the example below.
```bash
$ airflow config get-value api auth_backends
airflow.api.auth.backend.basic_auth
```
The default is to deny all requests.

For details on configuring the authentication, see
[API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).

# Errors

We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807)
also known as Problem Details for HTTP APIs. As with our normal API responses,
your client must be prepared to gracefully handle additional members of the response.

## Unauthenticated

This indicates that the request has not been applied because it lacks valid authentication
credentials for the target resource. Please check that you have valid credentials.

## PermissionDenied

This response means that the server understood the request but refuses to authorize
it because it lacks sufficient rights to the resource. It happens when you do not have the
necessary permission to execute the action you performed. You need to get the appropriate
permissions in other to resolve this error.

## BadRequest

This response means that the server cannot or will not process the request due to something
that is perceived to be a client error (e.g., malformed request syntax, invalid request message
framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.

## NotFound

This client error response indicates that the server cannot find the requested resource.

## MethodNotAllowed

Indicates that the request method is known by the server but is not supported by the target resource.

## NotAcceptable

The target resource does not have a current representation that would be acceptable to the user
agent, according to the proactive negotiation header fields received in the request, and the
server is unwilling to supply a default representation.

## AlreadyExists

The request could not be completed due to a conflict with the current state of the target
resource, e.g. the resource it tries to create already exists.

## Unknown

This means that the server encountered an unexpected condition that prevented it from
fulfilling the request.

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.5.3
- Package version: 2.5.3
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://airflow.apache.org](https://airflow.apache.org)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install airflow_api__stable --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your airflow_api__stable from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var AirflowApiStable = require('airflow_api__stable');


var api = new AirflowApiStable.ConfigApi()
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.getConfig(callback);

```

## Documentation for API Endpoints

All URIs are relative to */api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AirflowApiStable.ConfigApi* | [**getConfig**](docs/ConfigApi.md#getConfig) | **GET** /config | Get current configuration
*AirflowApiStable.ConnectionApi* | [**deleteConnection**](docs/ConnectionApi.md#deleteConnection) | **DELETE** /connections/{connection_id} | Delete a connection
*AirflowApiStable.ConnectionApi* | [**getConnection**](docs/ConnectionApi.md#getConnection) | **GET** /connections/{connection_id} | Get a connection
*AirflowApiStable.ConnectionApi* | [**getConnections**](docs/ConnectionApi.md#getConnections) | **GET** /connections | List connections
*AirflowApiStable.ConnectionApi* | [**patchConnection**](docs/ConnectionApi.md#patchConnection) | **PATCH** /connections/{connection_id} | Update a connection
*AirflowApiStable.ConnectionApi* | [**postConnection**](docs/ConnectionApi.md#postConnection) | **POST** /connections | Create a connection
*AirflowApiStable.ConnectionApi* | [**testConnection**](docs/ConnectionApi.md#testConnection) | **POST** /connections/test | Test a connection
*AirflowApiStable.DAGApi* | [**deleteDag**](docs/DAGApi.md#deleteDag) | **DELETE** /dags/{dag_id} | Delete a DAG
*AirflowApiStable.DAGApi* | [**getDag**](docs/DAGApi.md#getDag) | **GET** /dags/{dag_id} | Get basic information about a DAG
*AirflowApiStable.DAGApi* | [**getDagDetails**](docs/DAGApi.md#getDagDetails) | **GET** /dags/{dag_id}/details | Get a simplified representation of DAG
*AirflowApiStable.DAGApi* | [**getDagSource**](docs/DAGApi.md#getDagSource) | **GET** /dagSources/{file_token} | Get a source code
*AirflowApiStable.DAGApi* | [**getDags**](docs/DAGApi.md#getDags) | **GET** /dags | List DAGs
*AirflowApiStable.DAGApi* | [**getTask**](docs/DAGApi.md#getTask) | **GET** /dags/{dag_id}/tasks/{task_id} | Get simplified representation of a task
*AirflowApiStable.DAGApi* | [**getTasks**](docs/DAGApi.md#getTasks) | **GET** /dags/{dag_id}/tasks | Get tasks for DAG
*AirflowApiStable.DAGApi* | [**patchDag**](docs/DAGApi.md#patchDag) | **PATCH** /dags/{dag_id} | Update a DAG
*AirflowApiStable.DAGApi* | [**patchDags**](docs/DAGApi.md#patchDags) | **PATCH** /dags | Update DAGs
*AirflowApiStable.DAGApi* | [**postClearTaskInstances**](docs/DAGApi.md#postClearTaskInstances) | **POST** /dags/{dag_id}/clearTaskInstances | Clear a set of task instances
*AirflowApiStable.DAGApi* | [**postSetTaskInstancesState**](docs/DAGApi.md#postSetTaskInstancesState) | **POST** /dags/{dag_id}/updateTaskInstancesState | Set a state of task instances
*AirflowApiStable.DAGRunApi* | [**clearDagRun**](docs/DAGRunApi.md#clearDagRun) | **POST** /dags/{dag_id}/dagRuns/{dag_run_id}/clear | Clear a DAG run
*AirflowApiStable.DAGRunApi* | [**deleteDagRun**](docs/DAGRunApi.md#deleteDagRun) | **DELETE** /dags/{dag_id}/dagRuns/{dag_run_id} | Delete a DAG run
*AirflowApiStable.DAGRunApi* | [**getDagRun**](docs/DAGRunApi.md#getDagRun) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id} | Get a DAG run
*AirflowApiStable.DAGRunApi* | [**getDagRuns**](docs/DAGRunApi.md#getDagRuns) | **GET** /dags/{dag_id}/dagRuns | List DAG runs
*AirflowApiStable.DAGRunApi* | [**getDagRunsBatch**](docs/DAGRunApi.md#getDagRunsBatch) | **POST** /dags/~/dagRuns/list | List DAG runs (batch)
*AirflowApiStable.DAGRunApi* | [**getUpstreamDatasetEvents**](docs/DAGRunApi.md#getUpstreamDatasetEvents) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/upstreamDatasetEvents | Get dataset events for a DAG run
*AirflowApiStable.DAGRunApi* | [**postDagRun**](docs/DAGRunApi.md#postDagRun) | **POST** /dags/{dag_id}/dagRuns | Trigger a new DAG run
*AirflowApiStable.DAGRunApi* | [**setDagRunNote**](docs/DAGRunApi.md#setDagRunNote) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/setNote | Update the DagRun note.
*AirflowApiStable.DAGRunApi* | [**updateDagRunState**](docs/DAGRunApi.md#updateDagRunState) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id} | Modify a DAG run
*AirflowApiStable.DagWarningApi* | [**getDagWarnings**](docs/DagWarningApi.md#getDagWarnings) | **GET** /dagWarnings | List dag warnings
*AirflowApiStable.DatasetApi* | [**getDataset**](docs/DatasetApi.md#getDataset) | **GET** /datasets/{uri} | Get a dataset
*AirflowApiStable.DatasetApi* | [**getDatasetEvents**](docs/DatasetApi.md#getDatasetEvents) | **GET** /datasets/events | Get dataset events
*AirflowApiStable.DatasetApi* | [**getDatasets**](docs/DatasetApi.md#getDatasets) | **GET** /datasets | List datasets
*AirflowApiStable.DatasetApi* | [**getUpstreamDatasetEvents_0**](docs/DatasetApi.md#getUpstreamDatasetEvents_0) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/upstreamDatasetEvents | Get dataset events for a DAG run
*AirflowApiStable.EventLogApi* | [**getEventLog**](docs/EventLogApi.md#getEventLog) | **GET** /eventLogs/{event_log_id} | Get a log entry
*AirflowApiStable.EventLogApi* | [**getEventLogs**](docs/EventLogApi.md#getEventLogs) | **GET** /eventLogs | List log entries
*AirflowApiStable.ImportErrorApi* | [**getImportError**](docs/ImportErrorApi.md#getImportError) | **GET** /importErrors/{import_error_id} | Get an import error
*AirflowApiStable.ImportErrorApi* | [**getImportErrors**](docs/ImportErrorApi.md#getImportErrors) | **GET** /importErrors | List import errors
*AirflowApiStable.MonitoringApi* | [**getHealth**](docs/MonitoringApi.md#getHealth) | **GET** /health | Get instance status
*AirflowApiStable.MonitoringApi* | [**getVersion**](docs/MonitoringApi.md#getVersion) | **GET** /version | Get version information
*AirflowApiStable.PermissionApi* | [**getPermissions**](docs/PermissionApi.md#getPermissions) | **GET** /permissions | List permissions
*AirflowApiStable.PluginApi* | [**getPlugins**](docs/PluginApi.md#getPlugins) | **GET** /plugins | Get a list of loaded plugins
*AirflowApiStable.PoolApi* | [**deletePool**](docs/PoolApi.md#deletePool) | **DELETE** /pools/{pool_name} | Delete a pool
*AirflowApiStable.PoolApi* | [**getPool**](docs/PoolApi.md#getPool) | **GET** /pools/{pool_name} | Get a pool
*AirflowApiStable.PoolApi* | [**getPools**](docs/PoolApi.md#getPools) | **GET** /pools | List pools
*AirflowApiStable.PoolApi* | [**patchPool**](docs/PoolApi.md#patchPool) | **PATCH** /pools/{pool_name} | Update a pool
*AirflowApiStable.PoolApi* | [**postPool**](docs/PoolApi.md#postPool) | **POST** /pools | Create a pool
*AirflowApiStable.ProviderApi* | [**getProviders**](docs/ProviderApi.md#getProviders) | **GET** /providers | List providers
*AirflowApiStable.RoleApi* | [**deleteRole**](docs/RoleApi.md#deleteRole) | **DELETE** /roles/{role_name} | Delete a role
*AirflowApiStable.RoleApi* | [**getRole**](docs/RoleApi.md#getRole) | **GET** /roles/{role_name} | Get a role
*AirflowApiStable.RoleApi* | [**getRoles**](docs/RoleApi.md#getRoles) | **GET** /roles | List roles
*AirflowApiStable.RoleApi* | [**patchRole**](docs/RoleApi.md#patchRole) | **PATCH** /roles/{role_name} | Update a role
*AirflowApiStable.RoleApi* | [**postRole**](docs/RoleApi.md#postRole) | **POST** /roles | Create a role
*AirflowApiStable.TaskInstanceApi* | [**getExtraLinks**](docs/TaskInstanceApi.md#getExtraLinks) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/links | List extra links
*AirflowApiStable.TaskInstanceApi* | [**getLog**](docs/TaskInstanceApi.md#getLog) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{task_try_number} | Get logs
*AirflowApiStable.TaskInstanceApi* | [**getMappedTaskInstance**](docs/TaskInstanceApi.md#getMappedTaskInstance) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index} | Get a mapped task instance
*AirflowApiStable.TaskInstanceApi* | [**getMappedTaskInstances**](docs/TaskInstanceApi.md#getMappedTaskInstances) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/listMapped | List mapped task instances
*AirflowApiStable.TaskInstanceApi* | [**getTaskInstance**](docs/TaskInstanceApi.md#getTaskInstance) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id} | Get a task instance
*AirflowApiStable.TaskInstanceApi* | [**getTaskInstances**](docs/TaskInstanceApi.md#getTaskInstances) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances | List task instances
*AirflowApiStable.TaskInstanceApi* | [**getTaskInstancesBatch**](docs/TaskInstanceApi.md#getTaskInstancesBatch) | **POST** /dags/~/dagRuns/~/taskInstances/list | List task instances (batch)
*AirflowApiStable.TaskInstanceApi* | [**patchMappedTaskInstance**](docs/TaskInstanceApi.md#patchMappedTaskInstance) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index} | Updates the state of a mapped task instance
*AirflowApiStable.TaskInstanceApi* | [**patchTaskInstance**](docs/TaskInstanceApi.md#patchTaskInstance) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id} | Updates the state of a task instance
*AirflowApiStable.TaskInstanceApi* | [**setMappedTaskInstanceNote**](docs/TaskInstanceApi.md#setMappedTaskInstanceNote) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}/setNote | Update the TaskInstance note.
*AirflowApiStable.TaskInstanceApi* | [**setTaskInstanceNote**](docs/TaskInstanceApi.md#setTaskInstanceNote) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/setNote | Update the TaskInstance note.
*AirflowApiStable.UserApi* | [**deleteUser**](docs/UserApi.md#deleteUser) | **DELETE** /users/{username} | Delete a user
*AirflowApiStable.UserApi* | [**getUser**](docs/UserApi.md#getUser) | **GET** /users/{username} | Get a user
*AirflowApiStable.UserApi* | [**getUsers**](docs/UserApi.md#getUsers) | **GET** /users | List users
*AirflowApiStable.UserApi* | [**patchUser**](docs/UserApi.md#patchUser) | **PATCH** /users/{username} | Update a user
*AirflowApiStable.UserApi* | [**postUser**](docs/UserApi.md#postUser) | **POST** /users | Create a user
*AirflowApiStable.VariableApi* | [**deleteVariable**](docs/VariableApi.md#deleteVariable) | **DELETE** /variables/{variable_key} | Delete a variable
*AirflowApiStable.VariableApi* | [**getVariable**](docs/VariableApi.md#getVariable) | **GET** /variables/{variable_key} | Get a variable
*AirflowApiStable.VariableApi* | [**getVariables**](docs/VariableApi.md#getVariables) | **GET** /variables | List variables
*AirflowApiStable.VariableApi* | [**patchVariable**](docs/VariableApi.md#patchVariable) | **PATCH** /variables/{variable_key} | Update a variable
*AirflowApiStable.VariableApi* | [**postVariables**](docs/VariableApi.md#postVariables) | **POST** /variables | Create a variable
*AirflowApiStable.XComApi* | [**getXcomEntries**](docs/XComApi.md#getXcomEntries) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries | List XCom entries
*AirflowApiStable.XComApi* | [**getXcomEntry**](docs/XComApi.md#getXcomEntry) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key} | Get an XCom entry


## Documentation for Models

 - [AirflowApiStable.Action](docs/Action.md)
 - [AirflowApiStable.ActionCollection](docs/ActionCollection.md)
 - [AirflowApiStable.ActionResource](docs/ActionResource.md)
 - [AirflowApiStable.BasicDAGRun](docs/BasicDAGRun.md)
 - [AirflowApiStable.ClassReference](docs/ClassReference.md)
 - [AirflowApiStable.ClearDagRun](docs/ClearDagRun.md)
 - [AirflowApiStable.ClearDagRun200Response](docs/ClearDagRun200Response.md)
 - [AirflowApiStable.ClearTaskInstances](docs/ClearTaskInstances.md)
 - [AirflowApiStable.CollectionInfo](docs/CollectionInfo.md)
 - [AirflowApiStable.Config](docs/Config.md)
 - [AirflowApiStable.ConfigOption](docs/ConfigOption.md)
 - [AirflowApiStable.ConfigSection](docs/ConfigSection.md)
 - [AirflowApiStable.Connection](docs/Connection.md)
 - [AirflowApiStable.ConnectionCollection](docs/ConnectionCollection.md)
 - [AirflowApiStable.ConnectionCollectionItem](docs/ConnectionCollectionItem.md)
 - [AirflowApiStable.ConnectionTest](docs/ConnectionTest.md)
 - [AirflowApiStable.CronExpression](docs/CronExpression.md)
 - [AirflowApiStable.DAG](docs/DAG.md)
 - [AirflowApiStable.DAGCollection](docs/DAGCollection.md)
 - [AirflowApiStable.DAGDetail](docs/DAGDetail.md)
 - [AirflowApiStable.DAGRun](docs/DAGRun.md)
 - [AirflowApiStable.DAGRunCollection](docs/DAGRunCollection.md)
 - [AirflowApiStable.DagScheduleDatasetReference](docs/DagScheduleDatasetReference.md)
 - [AirflowApiStable.DagState](docs/DagState.md)
 - [AirflowApiStable.DagWarning](docs/DagWarning.md)
 - [AirflowApiStable.DagWarningCollection](docs/DagWarningCollection.md)
 - [AirflowApiStable.Dataset](docs/Dataset.md)
 - [AirflowApiStable.DatasetCollection](docs/DatasetCollection.md)
 - [AirflowApiStable.DatasetEvent](docs/DatasetEvent.md)
 - [AirflowApiStable.DatasetEventCollection](docs/DatasetEventCollection.md)
 - [AirflowApiStable.Error](docs/Error.md)
 - [AirflowApiStable.EventLog](docs/EventLog.md)
 - [AirflowApiStable.EventLogCollection](docs/EventLogCollection.md)
 - [AirflowApiStable.ExtraLink](docs/ExtraLink.md)
 - [AirflowApiStable.ExtraLinkCollection](docs/ExtraLinkCollection.md)
 - [AirflowApiStable.GetDagSource200Response](docs/GetDagSource200Response.md)
 - [AirflowApiStable.GetLog200Response](docs/GetLog200Response.md)
 - [AirflowApiStable.GetProviders200Response](docs/GetProviders200Response.md)
 - [AirflowApiStable.HealthInfo](docs/HealthInfo.md)
 - [AirflowApiStable.HealthStatus](docs/HealthStatus.md)
 - [AirflowApiStable.ImportError](docs/ImportError.md)
 - [AirflowApiStable.ImportErrorCollection](docs/ImportErrorCollection.md)
 - [AirflowApiStable.Job](docs/Job.md)
 - [AirflowApiStable.ListDagRunsForm](docs/ListDagRunsForm.md)
 - [AirflowApiStable.ListTaskInstanceForm](docs/ListTaskInstanceForm.md)
 - [AirflowApiStable.MetadatabaseStatus](docs/MetadatabaseStatus.md)
 - [AirflowApiStable.PluginCollection](docs/PluginCollection.md)
 - [AirflowApiStable.PluginCollectionItem](docs/PluginCollectionItem.md)
 - [AirflowApiStable.Pool](docs/Pool.md)
 - [AirflowApiStable.PoolCollection](docs/PoolCollection.md)
 - [AirflowApiStable.Provider](docs/Provider.md)
 - [AirflowApiStable.ProviderCollection](docs/ProviderCollection.md)
 - [AirflowApiStable.RelativeDelta](docs/RelativeDelta.md)
 - [AirflowApiStable.Resource](docs/Resource.md)
 - [AirflowApiStable.Role](docs/Role.md)
 - [AirflowApiStable.RoleCollection](docs/RoleCollection.md)
 - [AirflowApiStable.SLAMiss](docs/SLAMiss.md)
 - [AirflowApiStable.ScheduleInterval](docs/ScheduleInterval.md)
 - [AirflowApiStable.SchedulerStatus](docs/SchedulerStatus.md)
 - [AirflowApiStable.SetDagRunNote](docs/SetDagRunNote.md)
 - [AirflowApiStable.SetTaskInstanceNote](docs/SetTaskInstanceNote.md)
 - [AirflowApiStable.Tag](docs/Tag.md)
 - [AirflowApiStable.Task](docs/Task.md)
 - [AirflowApiStable.TaskCollection](docs/TaskCollection.md)
 - [AirflowApiStable.TaskExtraLinksInner](docs/TaskExtraLinksInner.md)
 - [AirflowApiStable.TaskInstance](docs/TaskInstance.md)
 - [AirflowApiStable.TaskInstanceCollection](docs/TaskInstanceCollection.md)
 - [AirflowApiStable.TaskInstanceReference](docs/TaskInstanceReference.md)
 - [AirflowApiStable.TaskInstanceReferenceCollection](docs/TaskInstanceReferenceCollection.md)
 - [AirflowApiStable.TaskOutletDatasetReference](docs/TaskOutletDatasetReference.md)
 - [AirflowApiStable.TaskState](docs/TaskState.md)
 - [AirflowApiStable.TimeDelta](docs/TimeDelta.md)
 - [AirflowApiStable.Trigger](docs/Trigger.md)
 - [AirflowApiStable.TriggerRule](docs/TriggerRule.md)
 - [AirflowApiStable.UpdateDagRunState](docs/UpdateDagRunState.md)
 - [AirflowApiStable.UpdateTaskInstance](docs/UpdateTaskInstance.md)
 - [AirflowApiStable.UpdateTaskInstancesState](docs/UpdateTaskInstancesState.md)
 - [AirflowApiStable.User](docs/User.md)
 - [AirflowApiStable.UserCollection](docs/UserCollection.md)
 - [AirflowApiStable.UserCollectionItem](docs/UserCollectionItem.md)
 - [AirflowApiStable.UserCollectionItemRolesInner](docs/UserCollectionItemRolesInner.md)
 - [AirflowApiStable.Variable](docs/Variable.md)
 - [AirflowApiStable.VariableCollection](docs/VariableCollection.md)
 - [AirflowApiStable.VariableCollectionItem](docs/VariableCollectionItem.md)
 - [AirflowApiStable.VersionInfo](docs/VersionInfo.md)
 - [AirflowApiStable.WeightRule](docs/WeightRule.md)
 - [AirflowApiStable.XCom](docs/XCom.md)
 - [AirflowApiStable.XComCollection](docs/XComCollection.md)
 - [AirflowApiStable.XComCollectionItem](docs/XComCollectionItem.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### Basic

- **Type**: HTTP basic authentication

### GoogleOpenId


### Kerberos


