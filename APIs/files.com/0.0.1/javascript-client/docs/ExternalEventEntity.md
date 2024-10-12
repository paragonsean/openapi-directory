# FilesComApi.ExternalEventEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **String** | Event body | [optional] 
**bodyUrl** | **String** | Link to log file. | [optional] 
**bytesSynced** | **Number** | For sync events, the total number of bytes synced. | [optional] 
**createdAt** | **Date** | External event create date/time | [optional] 
**erroredFiles** | **Number** | For sync events, the number of files that encountered errors. | [optional] 
**eventType** | **String** | Type of event being recorded. | [optional] 
**folderBehaviorId** | **Number** | Folder Behavior ID | [optional] 
**id** | **Number** | Event ID | [optional] 
**remoteServerType** | **String** | Associated Remote Server type, if any | [optional] 
**status** | **String** | Status of event. | [optional] 
**successfulFiles** | **Number** | For sync events, the number of files handled successfully. | [optional] 



## Enum: EventTypeEnum


* `ldap_sync` (value: `"ldap_sync"`)

* `remote_server_sync` (value: `"remote_server_sync"`)

* `lockout` (value: `"lockout"`)

* `ldap_login` (value: `"ldap_login"`)

* `saml_login` (value: `"saml_login"`)

* `client_log` (value: `"client_log"`)

* `pending_work` (value: `"pending_work"`)





## Enum: StatusEnum


* `success` (value: `"success"`)

* `failure` (value: `"failure"`)

* `partial_failure` (value: `"partial_failure"`)

* `in_progress` (value: `"in_progress"`)

* `skipped` (value: `"skipped"`)




