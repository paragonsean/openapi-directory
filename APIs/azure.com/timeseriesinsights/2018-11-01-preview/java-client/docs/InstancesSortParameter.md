

# InstancesSortParameter

Definition of how time series instances are sorted before being returned by search instances call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**by** | [**ByEnum**](#ByEnum) | Value to use for sorting of the time series instances before being returned by search instances call. When it is set to &#39;Rank&#39;, the returned instances are sorted based on the relevance. When it is set to &#39;DisplayName&#39;, the returned results are sorted based on the display name. Display name is the name of the instance if it exists, otherwise, display name is the time series ID. Default is &#39;Rank&#39;. |  [optional] |



## Enum: ByEnum

| Name | Value |
|---- | -----|
| RANK | &quot;Rank&quot; |
| DISPLAY_NAME | &quot;DisplayName&quot; |



