

# DatabaseInstanceProperties

Properties of the database instance resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**discoveryData** | [**List&lt;DatabaseInstanceDiscoveryDetails&gt;**](DatabaseInstanceDiscoveryDetails.md) | Gets or sets the assessment details of the database instance published by various sources. |  [optional] |
|**lastUpdatedTime** | **OffsetDateTime** | Gets or sets the time of the last modification of the database. |  [optional] |
|**summary** | [**Map&lt;String, DatabaseInstanceSummary&gt;**](DatabaseInstanceSummary.md) | Gets or sets the database instances summary per solution. The key of dictionary is the solution name and value is the corresponding database instance summary object. |  [optional] |



