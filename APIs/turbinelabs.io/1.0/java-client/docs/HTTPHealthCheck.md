

# HTTPHealthCheck


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**host** | **String** | The value of the host header in the HTTP health check request. If left empty, the name of the cluster being health checked will be used.  |  [optional] |
|**path** | **String** | Specifies the HTTP path that will be requested during health checking.  |  [optional] |
|**requestHeadersToAdd** | [**List&lt;Metadatum&gt;**](Metadatum.md) | Specifies a list of HTTP headers that should be added to each request sent to the health checked cluster.  |  [optional] |
|**serviceName** | **String** | An optional service name parameter which is used to validate the identity of the health checked cluster.  |  [optional] |



