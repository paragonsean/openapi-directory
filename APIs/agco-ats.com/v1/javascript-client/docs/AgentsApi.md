# AgcoApi.AgentsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agentsDeleteAgent**](AgentsApi.md#agentsDeleteAgent) | **DELETE** /api/v2/agents/{agentID} | Delete an Agent
[**agentsGetAgentActivityRun**](AgentsApi.md#agentsGetAgentActivityRun) | **GET** /api/v2/agents/{agentID}/ActivityRun | Get an Agent&#39;s ActivityRun
[**agentsGetAgentAsync**](AgentsApi.md#agentsGetAgentAsync) | **GET** /api/v2/agents/{agentID} | Get Agent
[**agentsGetAgents**](AgentsApi.md#agentsGetAgents) | **GET** /api/v2/agents | Get Agents
[**agentsGetCurrentAgentActivityRun**](AgentsApi.md#agentsGetCurrentAgentActivityRun) | **GET** /api/v2/agents/Current/ActivityRun | Get the ActivityRun of Agent associated with the current user
[**agentsGetCurrentAgentAsync**](AgentsApi.md#agentsGetCurrentAgentAsync) | **GET** /api/v2/agents/Current | Get Agent associated with the current user
[**agentsPostAgent**](AgentsApi.md#agentsPostAgent) | **POST** /api/v2/agents | Create an Agent
[**agentsPutAgent**](AgentsApi.md#agentsPutAgent) | **PUT** /api/v2/agents/{agentID} | Update an Agent
[**agentsPutAgentActivityRun**](AgentsApi.md#agentsPutAgentActivityRun) | **PUT** /api/v2/agents/{agentID}/ActivityRun | Update the ActivityRun assigned to the Agent.
[**agentsPutAgentStatus**](AgentsApi.md#agentsPutAgentStatus) | **PUT** /api/v2/agents/{agentID}/Status | Update an Agent



## agentsDeleteAgent

> agentsDeleteAgent(agentID)

Delete an Agent

Deletes an Agent. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AgentsApi();
let agentID = 56; // Number | The id of the Agent to delete.
apiInstance.agentsDeleteAgent(agentID, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentID** | **Number**| The id of the Agent to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## agentsGetAgentActivityRun

> BuildSystemSharedDTOActivityRun agentsGetAgentActivityRun(agentID)

Get an Agent&#39;s ActivityRun

Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun              assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AgentsApi();
let agentID = 56; // Number | The id of the Agent to get.
apiInstance.agentsGetAgentActivityRun(agentID, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentID** | **Number**| The id of the Agent to get. | 

### Return type

[**BuildSystemSharedDTOActivityRun**](BuildSystemSharedDTOActivityRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## agentsGetAgentAsync

> BuildSystemSharedDTOAgent agentsGetAgentAsync(agentID)

Get Agent

Gets an Agent by ID. When successful, the response is the requested Agent.  If unsuccessful,              an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AgentsApi();
let agentID = 56; // Number | The id of the Agent to get.
apiInstance.agentsGetAgentAsync(agentID, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentID** | **Number**| The id of the Agent to get. | 

### Return type

[**BuildSystemSharedDTOAgent**](BuildSystemSharedDTOAgent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## agentsGetAgents

> APIPagedResponseBuildSystemSharedDTOAgent agentsGetAgents(opts)

Get Agents

Gets a collection of Agents. When successful, the response is a PagedResponse of Agents.                If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AgentsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56 // Number | Optional. The page offset.  If not specified, the default page offset is 0.
};
apiInstance.agentsGetAgents(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **Number**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseBuildSystemSharedDTOAgent**](APIPagedResponseBuildSystemSharedDTOAgent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## agentsGetCurrentAgentActivityRun

> BuildSystemSharedDTOActivityRun agentsGetCurrentAgentActivityRun()

Get the ActivityRun of Agent associated with the current user

Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun              assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AgentsApi();
apiInstance.agentsGetCurrentAgentActivityRun((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**BuildSystemSharedDTOActivityRun**](BuildSystemSharedDTOActivityRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## agentsGetCurrentAgentAsync

> BuildSystemSharedDTOAgent agentsGetCurrentAgentAsync()

Get Agent associated with the current user

Gets the Agent associated with the current user. When successful, the response is the requested Agent.  If unsuccessful,              an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AgentsApi();
apiInstance.agentsGetCurrentAgentAsync((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**BuildSystemSharedDTOAgent**](BuildSystemSharedDTOAgent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## agentsPostAgent

> Number agentsPostAgent(buildSystemSharedDTOAgent)

Create an Agent

Creates an Agent.  The body of the POST is the Agent to create.  The AgentID will be assigned              on creation of the Agent.  When successful, the response is the AgentID.  If unsuccessful, an              appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AgentsApi();
let buildSystemSharedDTOAgent = new AgcoApi.BuildSystemSharedDTOAgent(); // BuildSystemSharedDTOAgent | The Agent to create.  The AgentID will be assigned on creation of the Agent.
apiInstance.agentsPostAgent(buildSystemSharedDTOAgent, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buildSystemSharedDTOAgent** | [**BuildSystemSharedDTOAgent**](BuildSystemSharedDTOAgent.md)| The Agent to create.  The AgentID will be assigned on creation of the Agent. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## agentsPutAgent

> agentsPutAgent(agentID, buildSystemSharedDTOAgent)

Update an Agent

Updates an Agent.  The body of the PUT is the updated Agent.  When successful, the response is empty.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AgentsApi();
let agentID = 56; // Number | The id of the Agent to update.
let buildSystemSharedDTOAgent = new AgcoApi.BuildSystemSharedDTOAgent(); // BuildSystemSharedDTOAgent | The updated Agent
apiInstance.agentsPutAgent(agentID, buildSystemSharedDTOAgent, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentID** | **Number**| The id of the Agent to update. | 
 **buildSystemSharedDTOAgent** | [**BuildSystemSharedDTOAgent**](BuildSystemSharedDTOAgent.md)| The updated Agent | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## agentsPutAgentActivityRun

> agentsPutAgentActivityRun(agentID, buildSystemSharedDTOActivityRun)

Update the ActivityRun assigned to the Agent.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AgentsApi();
let agentID = 56; // Number | The id of the Agent to update.
let buildSystemSharedDTOActivityRun = new AgcoApi.BuildSystemSharedDTOActivityRun(); // BuildSystemSharedDTOActivityRun | The ActivityRun assigned to the agent.  Only the ActivityRunID is used.
apiInstance.agentsPutAgentActivityRun(agentID, buildSystemSharedDTOActivityRun, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentID** | **Number**| The id of the Agent to update. | 
 **buildSystemSharedDTOActivityRun** | [**BuildSystemSharedDTOActivityRun**](BuildSystemSharedDTOActivityRun.md)| The ActivityRun assigned to the agent.  Only the ActivityRunID is used. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## agentsPutAgentStatus

> agentsPutAgentStatus(agentID, buildSystemSharedDTOAgentStatus)

Update an Agent

Updates the status of an Agent.The body of the PUT is the updated Agent status.  When successful,              the response is empty.If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AgentsApi();
let agentID = 56; // Number | The id of the Agent to update.
let buildSystemSharedDTOAgentStatus = new AgcoApi.BuildSystemSharedDTOAgentStatus(); // BuildSystemSharedDTOAgentStatus | The updated AgentStatus.
apiInstance.agentsPutAgentStatus(agentID, buildSystemSharedDTOAgentStatus, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentID** | **Number**| The id of the Agent to update. | 
 **buildSystemSharedDTOAgentStatus** | [**BuildSystemSharedDTOAgentStatus**](BuildSystemSharedDTOAgentStatus.md)| The updated AgentStatus. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

