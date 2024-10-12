

# ApplicationHealthPolicy

Defines a health policy used to evaluate the health of an application or one of its children entities. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultServiceTypeHealthPolicy** | [**ServiceTypeHealthPolicy**](ServiceTypeHealthPolicy.md) |  |  [optional] |
|**serviceTypeHealthPolicies** | [**Map&lt;String, ServiceTypeHealthPolicy&gt;**](ServiceTypeHealthPolicy.md) | Defines a ServiceTypeHealthPolicy per service type name.  The entries in the map replace the default service type health policy for each specified service type. For example, in an application that contains both a stateless gateway service type and a stateful engine service type, the health policies for the stateless and stateful services can be configured differently. With policy per service type, there&#39;s more granular control of the health of the service.  If no policy is specified for a service type name, the DefaultServiceTypeHealthPolicy is used for evaluation.  |  [optional] |



