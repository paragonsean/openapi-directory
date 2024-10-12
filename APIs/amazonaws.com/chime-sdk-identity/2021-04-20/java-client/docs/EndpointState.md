

# EndpointState

<p>A read-only field that represents the state of an <code>AppInstanceUserEndpoint</code>. Supported values:</p> <ul> <li> <p> <code>ACTIVE</code>: The <code>AppInstanceUserEndpoint</code> is active and able to receive messages. When <code>ACTIVE</code>, the <code>EndpointStatusReason</code> remains empty.</p> </li> <li> <p> <code>INACTIVE</code>: The <code>AppInstanceUserEndpoint</code> is inactive and can't receive message. When INACTIVE, the corresponding reason will be conveyed through EndpointStatusReason.</p> </li> <li> <p> <code>INVALID_DEVICE_TOKEN</code> indicates that an <code>AppInstanceUserEndpoint</code> is <code>INACTIVE</code> due to invalid device token</p> </li> <li> <p> <code>INVALID_PINPOINT_ARN</code> indicates that an <code>AppInstanceUserEndpoint</code> is <code>INACTIVE</code> due to an invalid pinpoint ARN that was input through the <code>ResourceArn</code> field.</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**EndpointStatus**](EndpointStatus.md) |  |  |
|**statusReason** | [**EndpointStatusReason**](EndpointStatusReason.md) |  |  [optional] |



