

# Station


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**RB** | **Integer** | Regional code |  [optional] |
|**UIC** | **String** | UIC RICS code |  [optional] |
|**abbrev** | **String** | Abbrevation name of station or halt |  [optional] |
|**borderStation** | **Boolean** | Station is at a country border |  [optional] |
|**id** | **Integer** | Identifying number |  [optional] |
|**locationCode** | **String** | Primary location code |  [optional] |
|**name** | **String** | Long name of station or halt |  [optional] |
|**_short** | **String** | Short name of station or halt |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | State of operation |  [optional] |
|**timeTableRelevant** | **Boolean** | Relevant for time table |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of station or halt |  [optional] |
|**validFrom** | **String** | Start date for validity |  [optional] |
|**validTill** | **String** | End date for validity or null if still valid |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| IN_USE | &quot;in use&quot; |
| OUT_OF_SERVICE | &quot;out of service&quot; |
| FORMERLY | &quot;formerly&quot; |
| PLANNED | &quot;planned&quot; |
| STUDY | &quot;study&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ABZW | &quot;Abzw&quot; |
| ANST | &quot;Anst&quot; |
| AWANST | &quot;Awanst&quot; |
| BF | &quot;Bf&quot; |



