

# ReplicaSelection

The directed read replica selector. Callers must provide one or more of the following fields for replica selection: * `location` - The location must be one of the regions within the multi-region configuration of your database. * `type` - The type of the replica. Some examples of using replica_selectors are: * `location:us-east1` --> The \"us-east1\" replica(s) of any available type will be used to process the request. * `type:READ_ONLY` --> The \"READ_ONLY\" type replica(s) in nearest available location will be used to process the request. * `location:us-east1 type:READ_ONLY` --> The \"READ_ONLY\" type replica(s) in location \"us-east1\" will be used to process the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | **String** | The location or region of the serving requests, e.g. \&quot;us-east1\&quot;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of replica. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| READ_WRITE | &quot;READ_WRITE&quot; |
| READ_ONLY | &quot;READ_ONLY&quot; |



