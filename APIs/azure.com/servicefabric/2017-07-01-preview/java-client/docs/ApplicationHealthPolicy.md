

# ApplicationHealthPolicy

Defines a health policy used to evaluate the health of an application or one of its children entities. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**considerWarningAsError** | **Boolean** | Indicates whether warnings are treated with the same severity as errors. |  [optional] |
|**defaultServiceTypeHealthPolicy** | [**ServiceTypeHealthPolicy**](ServiceTypeHealthPolicy.md) |  |  [optional] |
|**maxPercentUnhealthyDeployedApplications** | **Integer** | The maximum allowed percentage of unhealthy deployed applications. Allowed values are Byte values from zero to 100. The percentage represents the maximum tolerated percentage of deployed applications that can be unhealthy before the application is considered in error. This is calculated by dividing the number of unhealthy deployed applications over the number of nodes where the application is currently deployed on in the cluster. The computation rounds up to tolerate one failure on small numbers of nodes. Default percentage is zero.  |  [optional] |
|**serviceTypeHealthPolicyMap** | [**List&lt;ServiceTypeHealthPolicyMapItem&gt;**](ServiceTypeHealthPolicyMapItem.md) | Defines a ServiceTypeHealthPolicy per service type name.  The entries in the map replace the default service type health policy for each specified service type. For example, in an application that contains both a stateless gateway service type and a stateful engine service type, the health policies for the stateless and stateful services can be configured differently. With policy per service type, there&#39;s more granular control of the health of the service.  If no policy is specified for a service type name, the DefaultServiceTypeHealthPolicy is used for evaluation.  |  [optional] |



