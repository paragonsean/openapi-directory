# MimicRestApi.MQTTApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolMqttClientGetProtstate**](MQTTApi.md#protocolMqttClientGetProtstate) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/get/protstate | Show the agent&#39;s MQTT TCP connection state
[**protocolMqttClientGetState**](MQTTApi.md#protocolMqttClientGetState) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/get/state | Show the agent&#39;s MQTT state
[**protocolMqttClientMessageCard**](MQTTApi.md#protocolMqttClientMessageCard) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/message/card | Show the agent&#39;s current messages&#39; cardinality
[**protocolMqttClientMessageGet**](MQTTApi.md#protocolMqttClientMessageGet) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/message/get/{msgNum}/{attr} | Show the agent&#39;s message attributes
[**protocolMqttClientMessageSet**](MQTTApi.md#protocolMqttClientMessageSet) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/message/set/{msgNum}/{attr}/{value} | Set the agent&#39;s message attributes
[**protocolMqttClientResubscribe**](MQTTApi.md#protocolMqttClientResubscribe) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/resubscribe/{subNum} | Restart receiving messages from a subcription of the agent
[**protocolMqttClientRuntimeAbort**](MQTTApi.md#protocolMqttClientRuntimeAbort) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/runtime/abort | Abort agent&#39;s MQTT TCP session without sending DISCONNECT command
[**protocolMqttClientRuntimeConnect**](MQTTApi.md#protocolMqttClientRuntimeConnect) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/runtime/connect | Start agent&#39;s MQTT TCP session
[**protocolMqttClientRuntimeDisconnect**](MQTTApi.md#protocolMqttClientRuntimeDisconnect) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/runtime/disconnect | Disconnect agent&#39;s MQTT TCP session by sending DISCONNECT command
[**protocolMqttClientSetBroker**](MQTTApi.md#protocolMqttClientSetBroker) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/broker/{brokerAddr} | Set the agent&#39;s MQTT TCP connection target broker
[**protocolMqttClientSetCleansession**](MQTTApi.md#protocolMqttClientSetCleansession) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/cleansession/{cleanOrNot} | Set the agent&#39;s MQTT session
[**protocolMqttClientSetClientid**](MQTTApi.md#protocolMqttClientSetClientid) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/clientid/{clientID} | Set the agent&#39;s MQTT client ID
[**protocolMqttClientSetKeepalive**](MQTTApi.md#protocolMqttClientSetKeepalive) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/keepalive/{aliveTime} | Set the agent&#39;s MQTT TCP keepalive
[**protocolMqttClientSetOnDisconnect**](MQTTApi.md#protocolMqttClientSetOnDisconnect) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/on_disconnect/{action} | Set the agent&#39;s MQTT disconnection action
[**protocolMqttClientSetPassword**](MQTTApi.md#protocolMqttClientSetPassword) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/password/{password} | Set the agent&#39;s MQTT client password
[**protocolMqttClientSetPort**](MQTTApi.md#protocolMqttClientSetPort) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/port/{port} | Set the agent&#39;s MQTT TCP connection target port
[**protocolMqttClientSetUsername**](MQTTApi.md#protocolMqttClientSetUsername) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/username/{username} | Set the agent&#39;s MQTT client username
[**protocolMqttClientSetWillmsg**](MQTTApi.md#protocolMqttClientSetWillmsg) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/willmsg/{msg} | Set the agent&#39;s MQTT client&#39;s will
[**protocolMqttClientSetWillqos**](MQTTApi.md#protocolMqttClientSetWillqos) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/willqos/{qos} | Set the agent&#39;s MQTT will message&#39;s QOS field
[**protocolMqttClientSetWillretain**](MQTTApi.md#protocolMqttClientSetWillretain) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/willretain/{retain} | Set the agent&#39;s MQTT retained will
[**protocolMqttClientSetWilltopic**](MQTTApi.md#protocolMqttClientSetWilltopic) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/set/willtopic/{topic} | Set the agent&#39;s MQTT client will&#39;s topic
[**protocolMqttClientSubscribeCard**](MQTTApi.md#protocolMqttClientSubscribeCard) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/subscribe/card | Show the agent&#39;s current subscriptions&#39; cardinality
[**protocolMqttClientSubscribeGet**](MQTTApi.md#protocolMqttClientSubscribeGet) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/subscribe/get/{subNum}/{attr} | Show the agent&#39;s subscription attributes
[**protocolMqttClientSubscribeSet**](MQTTApi.md#protocolMqttClientSubscribeSet) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/subscribe/set/{subNum}/{attr}/{value} | Set the agent&#39;s subscribe attributes
[**protocolMqttClientUnsubscribe**](MQTTApi.md#protocolMqttClientUnsubscribe) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/client/unsubscribe/{subNum} | Stops receiving messages from a subcription of the agent
[**protocolMqttGetArgs**](MQTTApi.md#protocolMqttGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/get/args | Show the agent&#39;s MQTT argument structure
[**protocolMqttGetConfig**](MQTTApi.md#protocolMqttGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/get/config | Show the agent&#39;s MQTT configuration
[**protocolMqttGetStatistics**](MQTTApi.md#protocolMqttGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/get/statistics | Show the agent&#39;s MQTT statistics
[**protocolMqttGetStatsHdr**](MQTTApi.md#protocolMqttGetStatsHdr) | **GET** /mimic/protocol/msg/mqtt/get/stats_hdr | Show the MQTT statistics headers
[**protocolMqttGetTrace**](MQTTApi.md#protocolMqttGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/mqtt/get/trace | Show the agent&#39;s MQTT traffic tracing
[**protocolMqttSetConfig**](MQTTApi.md#protocolMqttSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/set/config/{argument}/{value} | Set the agent&#39;s MQTT configuration
[**protocolMqttSetTrace**](MQTTApi.md#protocolMqttSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/mqtt/set/trace/{enableOrNot} | Set the agent&#39;s MQTT traffic tracing



## protocolMqttClientGetProtstate

> [Number] protocolMqttClientGetProtstate(agentNum)

Show the agent&#39;s MQTT TCP connection state

0 - stopped, 2 - disconnected, 3 - connecting, 4 - connected, 5 - waiting for CONNACK, 6 - waiting for SUBACK, 7 - CONNACK received, in steady state

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to show MQTT state
apiInstance.protocolMqttClientGetProtstate(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show MQTT state | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientGetState

> [Number] protocolMqttClientGetState(agentNum)

Show the agent&#39;s MQTT state

0 means stopped, 1 means running

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to show MQTT state
apiInstance.protocolMqttClientGetState(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show MQTT state | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientMessageCard

> [Number] protocolMqttClientMessageCard(agentNum)

Show the agent&#39;s current messages&#39; cardinality

0 or more

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to show MQTT message state
apiInstance.protocolMqttClientMessageCard(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show MQTT message state | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientMessageGet

> [String] protocolMqttClientMessageGet(agentNum, msgNum, attr)

Show the agent&#39;s message attributes

Attribute can be topic, interval, count, sent , pre, post, properties(list of PUBLISH properties), properties.i (i-th PUBLISH property), properties.PROP-NAME (PUBLISH property with name PROP-NAME)

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to show MQTT state
let msgNum = 56; // Number | Message Number
let attr = "attr_example"; // String | Attribute
apiInstance.protocolMqttClientMessageGet(agentNum, msgNum, attr, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show MQTT state | 
 **msgNum** | **Number**| Message Number | 
 **attr** | **String**| Attribute | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientMessageSet

> [String] protocolMqttClientMessageSet(agentNum, msgNum, attr, value)

Set the agent&#39;s message attributes

Attribute can not be sent or properties . Use set/{msgNum}/count/{value} together with get/{msgNum}/count to throttle the outgoing MQTT message to the broker.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to show MQTT state
let msgNum = 56; // Number | Message Number
let attr = "attr_example"; // String | Attribute
let value = "value_example"; // String | Value
apiInstance.protocolMqttClientMessageSet(agentNum, msgNum, attr, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show MQTT state | 
 **msgNum** | **Number**| Message Number | 
 **attr** | **String**| Attribute | 
 **value** | **String**| Value | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientResubscribe

> String protocolMqttClientResubscribe(agentNum, subNum)

Restart receiving messages from a subcription of the agent

Restarts a subscription

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to change MQTT state
let subNum = 56; // Number | Subscription Number
apiInstance.protocolMqttClientResubscribe(agentNum, subNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to change MQTT state | 
 **subNum** | **Number**| Subscription Number | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientRuntimeAbort

> [String] protocolMqttClientRuntimeAbort(agentNum)

Abort agent&#39;s MQTT TCP session without sending DISCONNECT command

Abort a connection

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT behavior
apiInstance.protocolMqttClientRuntimeAbort(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT behavior | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientRuntimeConnect

> [String] protocolMqttClientRuntimeConnect(agentNum)

Start agent&#39;s MQTT TCP session

Start a connection

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT behavior
apiInstance.protocolMqttClientRuntimeConnect(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT behavior | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientRuntimeDisconnect

> [String] protocolMqttClientRuntimeDisconnect(agentNum)

Disconnect agent&#39;s MQTT TCP session by sending DISCONNECT command

Graceful disconnect

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT behavior
apiInstance.protocolMqttClientRuntimeDisconnect(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT behavior | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSetBroker

> [Number] protocolMqttClientSetBroker(agentNum, brokerAddr)

Set the agent&#39;s MQTT TCP connection target broker

Broker IP address

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT config
let brokerAddr = "brokerAddr_example"; // String | Broker address
apiInstance.protocolMqttClientSetBroker(agentNum, brokerAddr, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT config | 
 **brokerAddr** | **String**| Broker address | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSetCleansession

> [Number] protocolMqttClientSetCleansession(agentNum, cleanOrNot)

Set the agent&#39;s MQTT session

1 for clean session , 0 not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT config
let cleanOrNot = 56; // Number | Clean session
apiInstance.protocolMqttClientSetCleansession(agentNum, cleanOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT config | 
 **cleanOrNot** | **Number**| Clean session | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSetClientid

> [Number] protocolMqttClientSetClientid(agentNum, clientID)

Set the agent&#39;s MQTT client ID

MQTT client ID

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT config
let clientID = "clientID_example"; // String | Client ID
apiInstance.protocolMqttClientSetClientid(agentNum, clientID, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT config | 
 **clientID** | **String**| Client ID | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSetKeepalive

> [Number] protocolMqttClientSetKeepalive(agentNum, aliveTime)

Set the agent&#39;s MQTT TCP keepalive

Keep alive the TCP connection

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT config
let aliveTime = 56; // Number | period to send keepalive messages
apiInstance.protocolMqttClientSetKeepalive(agentNum, aliveTime, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT config | 
 **aliveTime** | **Number**| period to send keepalive messages | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSetOnDisconnect

> [Number] protocolMqttClientSetOnDisconnect(agentNum, action)

Set the agent&#39;s MQTT disconnection action

Action to take when MQTT session is disconnected

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT config
let action = "action_example"; // String | Action to take
apiInstance.protocolMqttClientSetOnDisconnect(agentNum, action, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT config | 
 **action** | **String**| Action to take | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSetPassword

> [Number] protocolMqttClientSetPassword(agentNum, password)

Set the agent&#39;s MQTT client password

Client password

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT config
let password = "password_example"; // String | Password
apiInstance.protocolMqttClientSetPassword(agentNum, password, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT config | 
 **password** | **String**| Password | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSetPort

> [Number] protocolMqttClientSetPort(agentNum, port)

Set the agent&#39;s MQTT TCP connection target port

target TCP port

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT config
let port = "port_example"; // String | TCP port
apiInstance.protocolMqttClientSetPort(agentNum, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT config | 
 **port** | **String**| TCP port | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSetUsername

> [Number] protocolMqttClientSetUsername(agentNum, username)

Set the agent&#39;s MQTT client username

Client username

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT config
let username = "username_example"; // String | User name
apiInstance.protocolMqttClientSetUsername(agentNum, username, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT config | 
 **username** | **String**| User name | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSetWillmsg

> [Number] protocolMqttClientSetWillmsg(agentNum, msg)

Set the agent&#39;s MQTT client&#39;s will

Will message

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT config
let msg = "msg_example"; // String | Will message
apiInstance.protocolMqttClientSetWillmsg(agentNum, msg, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT config | 
 **msg** | **String**| Will message | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSetWillqos

> [Number] protocolMqttClientSetWillqos(agentNum, qos)

Set the agent&#39;s MQTT will message&#39;s QOS field

QOS field

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT config
let qos = "qos_example"; // String | Quality of service field
apiInstance.protocolMqttClientSetWillqos(agentNum, qos, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT config | 
 **qos** | **String**| Quality of service field | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSetWillretain

> [Number] protocolMqttClientSetWillretain(agentNum, retain)

Set the agent&#39;s MQTT retained will

Retaining will

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT config
let retain = "retain_example"; // String | Retaining will
apiInstance.protocolMqttClientSetWillretain(agentNum, retain, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT config | 
 **retain** | **String**| Retaining will | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSetWilltopic

> [Number] protocolMqttClientSetWilltopic(agentNum, topic)

Set the agent&#39;s MQTT client will&#39;s topic

Will topic for the will message

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set MQTT config
let topic = "topic_example"; // String | topic
apiInstance.protocolMqttClientSetWilltopic(agentNum, topic, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set MQTT config | 
 **topic** | **String**| topic | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSubscribeCard

> [Number] protocolMqttClientSubscribeCard(agentNum)

Show the agent&#39;s current subscriptions&#39; cardinality

0 or more

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to show MQTT subscription state
apiInstance.protocolMqttClientSubscribeCard(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show MQTT subscription state | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSubscribeGet

> [String] protocolMqttClientSubscribeGet(agentNum, subNum, attr)

Show the agent&#39;s subscription attributes

Attribute can be topic, properties(list of SUBSCRIBE properties), properties.i (i-th SUBSCRIBE property), properties.PROP-NAME (SUBSCRIBE property with name PROP-NAME)

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to show MQTT state
let subNum = 56; // Number | Subscribe Number
let attr = "attr_example"; // String | Attribute
apiInstance.protocolMqttClientSubscribeGet(agentNum, subNum, attr, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show MQTT state | 
 **subNum** | **Number**| Subscribe Number | 
 **attr** | **String**| Attribute | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientSubscribeSet

> [String] protocolMqttClientSubscribeSet(agentNum, subNum, attr, value)

Set the agent&#39;s subscribe attributes

Attribute can not be properties .

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to show MQTT state
let subNum = 56; // Number | Subscribe Number
let attr = "attr_example"; // String | Attribute
let value = "value_example"; // String | Value
apiInstance.protocolMqttClientSubscribeSet(agentNum, subNum, attr, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show MQTT state | 
 **subNum** | **Number**| Subscribe Number | 
 **attr** | **String**| Attribute | 
 **value** | **String**| Value | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttClientUnsubscribe

> String protocolMqttClientUnsubscribe(agentNum, subNum)

Stops receiving messages from a subcription of the agent

Stops a subscription

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to change MQTT state
let subNum = 56; // Number | Subscription Number
apiInstance.protocolMqttClientUnsubscribe(agentNum, subNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to change MQTT state | 
 **subNum** | **Number**| Subscription Number | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttGetArgs

> Object protocolMqttGetArgs(agentNum)

Show the agent&#39;s MQTT argument structure

Agent&#39;s MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to show the MQTT argument structure
apiInstance.protocolMqttGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the MQTT argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttGetConfig

> ConfigMQTT protocolMqttGetConfig(agentNum)

Show the agent&#39;s MQTT configuration

Agent&#39;s MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to show the MQTT configuration
apiInstance.protocolMqttGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the MQTT configuration | 

### Return type

[**ConfigMQTT**](ConfigMQTT.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttGetStatistics

> [Number] protocolMqttGetStatistics(agentNum)

Show the agent&#39;s MQTT statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to show MQTT statistics
apiInstance.protocolMqttGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show MQTT statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttGetStatsHdr

> [String] protocolMqttGetStatsHdr()

Show the MQTT statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
apiInstance.protocolMqttGetStatsHdr((error, data, response) => {
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

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttGetTrace

> ConfigMQTT protocolMqttGetTrace(agentNum)

Show the agent&#39;s MQTT traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to show whether MQTT tracing is enabled
apiInstance.protocolMqttGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether MQTT tracing is enabled | 

### Return type

[**ConfigMQTT**](ConfigMQTT.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttSetConfig

> String protocolMqttSetConfig(agentNum, argument, value)

Set the agent&#39;s MQTT configuration

Agent&#39;s MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set the MQTT configuration
let argument = "argument_example"; // String | Parameter to set the MQTT configuration
let value = "value_example"; // String | Value to set the MQTT configuration
apiInstance.protocolMqttSetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the MQTT configuration | 
 **argument** | **String**| Parameter to set the MQTT configuration | 
 **value** | **String**| Value to set the MQTT configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolMqttSetTrace

> String protocolMqttSetTrace(agentNum, enableOrNot)

Set the agent&#39;s MQTT traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.MQTTApi();
let agentNum = 56; // Number | Agent to set the MQTT tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the MQTT tracing
apiInstance.protocolMqttSetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the MQTT tracing | 
 **enableOrNot** | **String**| Value to set the MQTT tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

