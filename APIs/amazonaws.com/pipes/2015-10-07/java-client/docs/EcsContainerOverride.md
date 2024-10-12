

# EcsContainerOverride

The overrides that are sent to a container. An empty container override can be passed in. An example of an empty container override is <code>{\"containerOverrides\": [ ] }</code>. If a non-empty container override is specified, the <code>name</code> parameter must be included.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**command** | [**List**](List.md) |  |  [optional] |
|**cpu** | [**Integer**](Integer.md) |  |  [optional] |
|**environment** | [**List**](List.md) |  |  [optional] |
|**environmentFiles** | [**List**](List.md) |  |  [optional] |
|**memory** | [**Integer**](Integer.md) |  |  [optional] |
|**memoryReservation** | [**Integer**](Integer.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**resourceRequirements** | [**List**](List.md) |  |  [optional] |



