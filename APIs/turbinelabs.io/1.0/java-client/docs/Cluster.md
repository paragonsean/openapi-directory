

# Cluster


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**circuitBreakers** | [**CircuitBreakers**](CircuitBreakers.md) |  |  [optional] |
|**healthChecks** | [**List&lt;HealthCheck&gt;**](HealthCheck.md) |  |  [optional] |
|**instances** | [**List&lt;Instance&gt;**](Instance.md) |  |  [optional] |
|**name** | **String** |  |  |
|**outlierDetection** | [**OutlierDetection**](OutlierDetection.md) |  |  [optional] |
|**requireTls** | **Boolean** | If set, requests to this collection of hosts will be made via HTTPS. At this time neither certificate validation and certificate pinning are supported for proxy clients of this cluster.  |  [optional] |
|**zoneKey** | **String** |  |  |
|**checksum** | **String** |  |  |
|**clusterKey** | **String** |  |  |



