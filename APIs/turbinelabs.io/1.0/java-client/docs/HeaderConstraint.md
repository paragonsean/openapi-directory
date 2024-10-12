

# HeaderConstraint

Indicates that a request's headers should meet some requirement before being selected for a rewrite. Must have zore or one elements. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caseSensitive** | **Boolean** | If set, the header value check will be case sensitive. |  [optional] |
|**invert** | **Boolean** | If set, the header constraint will succeed if the match described faile.  |  [optional] |
|**name** | **String** | The header that is being checked. This must match the regexp \&quot;^[0-9a-zA-Z-]+$\&quot;. This is checked in a case insensitive manner.  |  |
|**value** | **String** | If set the header&#39;s value will be compared to this. The default is to make case insensitive comparisons.  |  [optional] |



