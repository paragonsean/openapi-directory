

# ClusterConstraint


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterKey** | **String** |  |  [optional] |
|**constraintKey** | **String** |  |  [optional] |
|**metadata** | [**List&lt;Metadatum&gt;**](Metadatum.md) |  |  [optional] |
|**properties** | [**List&lt;Metadatum&gt;**](Metadatum.md) |  |  [optional] |
|**responseData** | [**ResponseData**](ResponseData.md) | When a request is served by a cluster selected by this constraint annotate the response with the information specified within this ResponseData object. It&#39;s possible that multiple response data configurations will apply; if that&#39;s the case then the values from ClusterConstarint takes precedence over those from a Route or SharedRules object.  |  [optional] |
|**weight** | **Integer** |  |  [optional] |



