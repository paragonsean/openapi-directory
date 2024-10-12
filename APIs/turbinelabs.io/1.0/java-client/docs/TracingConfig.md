

# TracingConfig

Configures tracing operations to be performed on the given listener 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ingress** | **Boolean** | Determines whether spans sent from this listener should be treated as ingress or egress operations.  |  [optional] |
|**requestHeadersForTags** | **List&lt;String&gt;** | the headers specified here will be added to the generated spans as annotations  |  [optional] |



