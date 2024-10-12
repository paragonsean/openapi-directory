

# ServiceMeshType

A unique identifier for the type of message. Display_name is intended to be human-readable, code is intended to be machine readable. There should be a one-to-one mapping between display_name and code. (i.e. do not re-use display_names or codes between message types.) See istio.analysis.v1alpha1.AnalysisMessageBase.Type

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | A 7 character code matching &#x60;^IST[0-9]{4}$&#x60; or &#x60;^ASM[0-9]{4}$&#x60;, intended to uniquely identify the message type. (e.g. \&quot;IST0001\&quot; is mapped to the \&quot;InternalError\&quot; message type.) |  [optional] |
|**displayName** | **String** | A human-readable name for the message type. e.g. \&quot;InternalError\&quot;, \&quot;PodMissingProxy\&quot;. This should be the same for all messages of the same type. (This corresponds to the &#x60;name&#x60; field in open-source Istio.) |  [optional] |



