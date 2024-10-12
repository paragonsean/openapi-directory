

# Connector

Definition of a Serverless VPC Access connector.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectedProjects** | **List&lt;String&gt;** | Output only. List of projects using the connector. |  [optional] [readonly] |
|**createTime** | **String** | Output only. The creation time of the connector. |  [optional] [readonly] |
|**ipCidrRange** | **String** | The range of internal addresses that follows RFC 4632 notation. Example: &#x60;10.132.0.0/28&#x60;. |  [optional] |
|**lastRestartTime** | **String** | Output only. The last restart time of the connector. |  [optional] [readonly] |
|**machineType** | **String** | Machine type of VM Instance underlying connector. Default is e2-micro |  [optional] |
|**maxInstances** | **Integer** | Maximum value of instances in autoscaling group underlying the connector. |  [optional] |
|**maxThroughput** | **Integer** | Maximum throughput of the connector in Mbps. Refers to the expected throughput when using an &#x60;e2-micro&#x60; machine type. Value must be a multiple of 100 from 300 through 1000. Must be higher than the value specified by --min-throughput. If both max-throughput and max-instances are provided, max-instances takes precedence over max-throughput. The use of &#x60;max-throughput&#x60; is discouraged in favor of &#x60;max-instances&#x60;. |  [optional] |
|**minInstances** | **Integer** | Minimum value of instances in autoscaling group underlying the connector. |  [optional] |
|**minThroughput** | **Integer** | Minimum throughput of the connector in Mbps. Refers to the expected throughput when using an &#x60;e2-micro&#x60; machine type. Value must be a multiple of 100 from 200 through 900. Must be lower than the value specified by --max-throughput. If both min-throughput and min-instances are provided, min-instances takes precedence over min-throughput. The use of &#x60;min-throughput&#x60; is discouraged in favor of &#x60;min-instances&#x60;. |  [optional] |
|**name** | **String** | The resource name in the format &#x60;projects/_*_/locations/_*_/connectors/_*&#x60;. |  [optional] |
|**network** | **String** | Name of a VPC network. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the VPC access connector. |  [optional] [readonly] |
|**subnet** | [**Subnet**](Subnet.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| READY | &quot;READY&quot; |
| CREATING | &quot;CREATING&quot; |
| DELETING | &quot;DELETING&quot; |
| ERROR | &quot;ERROR&quot; |
| UPDATING | &quot;UPDATING&quot; |



