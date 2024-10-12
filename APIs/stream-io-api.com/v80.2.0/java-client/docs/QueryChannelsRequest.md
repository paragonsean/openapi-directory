

# QueryChannelsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** |  |  [optional] |
|**connectionId** | **String** |  |  [optional] |
|**filterConditions** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**limit** | **Integer** | Number of channels to limit |  [optional] |
|**memberLimit** | **Integer** | Number of members to limit |  [optional] |
|**messageLimit** | **Integer** | Number of messages to limit |  [optional] |
|**offset** | **Integer** | Channel pagination offset |  [optional] |
|**presence** | **Boolean** |  |  [optional] |
|**sort** | [**List&lt;SortParamRequest&gt;**](SortParamRequest.md) | List of sort parameters |  |
|**state** | **Boolean** | Whether to update channel state or not |  [optional] |
|**user** | **UserObjectRequest** |  |  [optional] |
|**userId** | **String** |  |  [optional] |
|**watch** | **Boolean** | Whether to start watching found channels or not |  [optional] |



