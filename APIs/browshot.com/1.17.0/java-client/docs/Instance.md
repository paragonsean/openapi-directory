

# Instance


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**browser** | [**Browser**](Browser.md) |  |  [optional] |
|**country** | **String** | instance&#39;s country of origin |  [optional] |
|**height** | **Integer** | screen height in pixels |  [optional] |
|**id** | **Integer** | instance ID (required to requests screenshots) |  [optional] |
|**load** | **Float** | instance load:  &lt; 1: new screenshot requests will be processed immediately,  1-2: new screenshot requests will be processed in about two minutes,  2-3: new screenshot requests will be processed in about four minutes,  3-4: new screenshot requests will be processed in about six minutes,  etc.  |  [optional] |
|**screenshotCost** | **Integer** | number of credits for each screenshot |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | public, shared or private |  [optional] |
|**width** | **Integer** | screen width in pixels |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| SHARED | &quot;shared&quot; |
| PRIVATE | &quot;private&quot; |



