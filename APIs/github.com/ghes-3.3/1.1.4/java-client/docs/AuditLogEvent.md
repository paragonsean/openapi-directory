

# AuditLogEvent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atTimestamp** | **Integer** | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |  [optional] |
|**documentId** | **String** | A unique identifier for an audit event. |  [optional] |
|**action** | **String** | The name of the action that was performed, for example &#x60;user.login&#x60; or &#x60;repo.create&#x60;. |  [optional] |
|**active** | **Boolean** |  |  [optional] |
|**activeWas** | **Boolean** |  |  [optional] |
|**actor** | **String** | The actor who performed the action. |  [optional] |
|**actorId** | **Integer** | The id of the actor who performed the action. |  [optional] |
|**actorLocation** | [**AuditLogEventActorLocation**](AuditLogEventActorLocation.md) |  |  [optional] |
|**blockedUser** | **String** | The username of the account being blocked. |  [optional] |
|**business** | **String** |  |  [optional] |
|**businessId** | **Integer** |  |  [optional] |
|**config** | **List&lt;Object&gt;** |  |  [optional] |
|**configWas** | **List&lt;Object&gt;** |  |  [optional] |
|**contentType** | **String** |  |  [optional] |
|**createdAt** | **Integer** | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |  [optional] |
|**data** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**deployKeyFingerprint** | **String** |  |  [optional] |
|**emoji** | **String** |  |  [optional] |
|**events** | **List&lt;Object&gt;** |  |  [optional] |
|**eventsWere** | **List&lt;Object&gt;** |  |  [optional] |
|**explanation** | **String** |  |  [optional] |
|**fingerprint** | **String** |  |  [optional] |
|**hookId** | **Integer** |  |  [optional] |
|**limitedAvailability** | **Boolean** |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**oldUser** | **String** |  |  [optional] |
|**opensshPublicKey** | **String** |  |  [optional] |
|**operationType** | **String** |  |  [optional] |
|**org** | **String** |  |  [optional] |
|**orgId** | **Integer** |  |  [optional] |
|**previousVisibility** | **String** |  |  [optional] |
|**readOnly** | **Boolean** |  |  [optional] |
|**repo** | **String** | The name of the repository. |  [optional] |
|**repository** | **String** | The name of the repository. |  [optional] |
|**repositoryPublic** | **Boolean** |  |  [optional] |
|**targetLogin** | **String** |  |  [optional] |
|**team** | **String** |  |  [optional] |
|**transportProtocol** | **Integer** | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |  [optional] |
|**transportProtocolName** | **String** | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |  [optional] |
|**user** | **String** | The user that was affected by the action performed (if available). |  [optional] |
|**userId** | **Integer** |  |  [optional] |
|**visibility** | **String** | The repository visibility, for example &#x60;public&#x60; or &#x60;private&#x60;. |  [optional] |



