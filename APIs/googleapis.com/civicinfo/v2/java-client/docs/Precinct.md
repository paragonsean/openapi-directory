

# Precinct


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**administrationRegionId** | **String** | ID of the AdministrationRegion message for this precinct. Corresponds to LocalityId xml tag. |  [optional] |
|**contestId** | **List&lt;String&gt;** | ID(s) of the Contest message(s) for this precinct. |  [optional] |
|**datasetId** | **String** | Required. Dataset ID. What datasets our Precincts come from. |  [optional] |
|**earlyVoteSiteId** | **List&lt;String&gt;** | ID(s) of the PollingLocation message(s) for this precinct. |  [optional] |
|**electoralDistrictId** | **List&lt;String&gt;** | ID(s) of the ElectoralDistrict message(s) for this precinct. |  [optional] |
|**id** | **String** | Required. A unique identifier for this precinct. |  [optional] |
|**mailOnly** | **Boolean** | Specifies if the precinct runs mail-only elections. |  [optional] |
|**name** | **String** | Required. The name of the precinct. |  [optional] |
|**number** | **String** | The number of the precinct. |  [optional] |
|**ocdId** | **List&lt;String&gt;** | Encouraged. The OCD ID of the precinct |  [optional] |
|**pollingLocationId** | **List&lt;String&gt;** | ID(s) of the PollingLocation message(s) for this precinct. |  [optional] |
|**spatialBoundaryId** | **List&lt;String&gt;** | ID(s) of the SpatialBoundary message(s) for this precinct. Used to specify a geometrical boundary of the precinct. |  [optional] |
|**splitName** | **String** | If present, this proto corresponds to one portion of split precinct. Other portions of this precinct are guaranteed to have the same &#x60;name&#x60;. If not present, this proto represents a full precicnt. |  [optional] |
|**ward** | **String** | Specifies the ward the precinct is contained within. |  [optional] |



