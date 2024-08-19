

# ServiceDependency


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requestedPermissions** | **List&lt;String&gt;** | Requested permissions regarding the access of the application to the service. See clause 8.2 of ETSI GS MEC 009 [4]. The format of this attribute is left for the data model design stage. |  [optional] |
|**serCategory** | **Object** | See MEC011 |  [optional] |
|**serName** | **String** | The name of the service, for example, RNIS, LocationService, etc. |  |
|**serTransportDependencies** | [**List&lt;TransportDependency&gt;**](TransportDependency.md) | Indicates transport and serialization format dependencies of consuming the service. Defaults to REST + JSON if absent. See note. |  [optional] |
|**version** | **String** | The version of the service. |  |



