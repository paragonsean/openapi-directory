

# ResourceUtilizationReport

Worker metrics exported from workers. This contains resource utilization metrics accumulated from a variety of sources. For more information, see go/df-resource-signals.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containers** | [**Map&lt;String, ResourceUtilizationReport&gt;**](ResourceUtilizationReport.md) | Per container information. Key: container name. |  [optional] |
|**cpuTime** | [**List&lt;CPUTime&gt;**](CPUTime.md) | CPU utilization samples. |  [optional] |
|**memoryInfo** | [**List&lt;MemInfo&gt;**](MemInfo.md) | Memory utilization samples. |  [optional] |



