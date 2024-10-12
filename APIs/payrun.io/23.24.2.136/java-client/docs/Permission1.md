

# Permission1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The permissions&#39; description |  [optional] |
|**expression** | **String** | The permissions&#39; expression |  [optional] |
|**name** | **String** | The permissions&#39; name |  [optional] |
|**policy** | [**PolicyEnum**](#PolicyEnum) | The permissions&#39; policy |  [optional] |
|**verbs** | [**VerbsEnum**](#VerbsEnum) | The permissions&#39; verbs |  [optional] |



## Enum: PolicyEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;Allow&quot; |
| DENY | &quot;Deny&quot; |



## Enum: VerbsEnum

| Name | Value |
|---- | -----|
| READ | &quot;Read&quot; |
| WRITE | &quot;Write&quot; |
| DELETE | &quot;Delete&quot; |
| ALL | &quot;All&quot; |



