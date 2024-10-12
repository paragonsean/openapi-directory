# VertexAiApi.UtilStatusProto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonicalCode** | **Number** | The canonical error code (see codes.proto) that most closely corresponds to this status. This may be missing, and in the common case of the generic space, it definitely will be. | [optional] 
**code** | **Number** | Numeric code drawn from the space specified below. Often, this is the canonical error space, and code is drawn from google3/util/task/codes.proto | [optional] 
**message** | **String** | Detail message | [optional] 
**messageSet** | **Object** | This is proto2&#39;s version of MessageSet. | [optional] 
**space** | **String** | The following are usually only present when code !&#x3D; 0 Space to which this status belongs | [optional] 


