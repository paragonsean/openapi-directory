

# ExternalEventEntity

List External Events

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | Event body |  [optional] |
|**bodyUrl** | **String** | Link to log file. |  [optional] |
|**bytesSynced** | **Integer** | For sync events, the total number of bytes synced. |  [optional] |
|**createdAt** | **OffsetDateTime** | External event create date/time |  [optional] |
|**erroredFiles** | **Integer** | For sync events, the number of files that encountered errors. |  [optional] |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | Type of event being recorded. |  [optional] |
|**folderBehaviorId** | **Integer** | Folder Behavior ID |  [optional] |
|**id** | **Integer** | Event ID |  [optional] |
|**remoteServerType** | **String** | Associated Remote Server type, if any |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of event. |  [optional] |
|**successfulFiles** | **Integer** | For sync events, the number of files handled successfully. |  [optional] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| LDAP_SYNC | &quot;ldap_sync&quot; |
| REMOTE_SERVER_SYNC | &quot;remote_server_sync&quot; |
| LOCKOUT | &quot;lockout&quot; |
| LDAP_LOGIN | &quot;ldap_login&quot; |
| SAML_LOGIN | &quot;saml_login&quot; |
| CLIENT_LOG | &quot;client_log&quot; |
| PENDING_WORK | &quot;pending_work&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| FAILURE | &quot;failure&quot; |
| PARTIAL_FAILURE | &quot;partial_failure&quot; |
| IN_PROGRESS | &quot;in_progress&quot; |
| SKIPPED | &quot;skipped&quot; |



