

# ProductVisibility

A product to be made visible to a user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**productId** | **String** | The product ID to make visible to the user. Required for each item in the productVisibility list. |  [optional] |
|**trackIds** | **List&lt;String&gt;** | Grants the user visibility to the specified product track(s), identified by trackIds. |  [optional] |
|**tracks** | [**List&lt;TracksEnum&gt;**](#List&lt;TracksEnum&gt;) | Deprecated. Use trackIds instead. |  [optional] |



## Enum: List&lt;TracksEnum&gt;

| Name | Value |
|---- | -----|
| APP_TRACK_UNSPECIFIED | &quot;appTrackUnspecified&quot; |
| PRODUCTION | &quot;production&quot; |
| BETA | &quot;beta&quot; |
| ALPHA | &quot;alpha&quot; |



