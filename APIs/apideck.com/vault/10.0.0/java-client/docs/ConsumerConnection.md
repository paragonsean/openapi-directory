

# ConsumerConnection


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authType** | **AuthType** |  |  [optional] |
|**consumerId** | **String** |  |  [optional] |
|**createdAt** | **String** |  |  [optional] |
|**enabled** | **Boolean** |  |  [optional] |
|**icon** | **String** |  |  [optional] |
|**id** | **String** |  |  [optional] [readonly] |
|**logo** | **String** |  |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** | Attach your own consumer specific metadata |  [optional] |
|**name** | **String** |  |  [optional] |
|**serviceId** | **String** |  |  [optional] |
|**settings** | **Object** | Connection settings. Values will persist to &#x60;form_fields&#x60; with corresponding id |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  [optional] |
|**tagLine** | **String** |  |  [optional] [readonly] |
|**unifiedApi** | **String** |  |  [optional] |
|**updatedAt** | **String** |  |  [optional] |
|**website** | **String** |  |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| CALLABLE | &quot;callable&quot; |
| ADDED | &quot;added&quot; |
| CONFIGURED | &quot;configured&quot; |
| AUTHORIZED | &quot;authorized&quot; |



