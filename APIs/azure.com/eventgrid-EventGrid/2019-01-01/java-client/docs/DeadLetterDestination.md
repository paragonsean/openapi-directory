

# DeadLetterDestination

Information about the dead letter destination for an event subscription. To configure a deadletter destination, do not directly instantiate an object of this class. Instead, instantiate an object of a derived class. Currently, StorageBlobDeadLetterDestination is the only class that derives from this class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpointType** | [**EndpointTypeEnum**](#EndpointTypeEnum) | Type of the endpoint for the dead letter destination |  |



## Enum: EndpointTypeEnum

| Name | Value |
|---- | -----|
| STORAGE_BLOB | &quot;StorageBlob&quot; |



