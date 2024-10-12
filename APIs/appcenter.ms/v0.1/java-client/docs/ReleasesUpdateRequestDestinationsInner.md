

# ReleasesUpdateRequestDestinationsInner

A unique identifier for a destination. A destination can be identified by an ID (guid) or by a name. DestinationId encapsulates both options. A destination can be either a distribution group or a store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Id of a distribution group / store. The release will be associated with this distribution group / store. If the distribution group / store doesn&#39;t exist a 400 is returned. If both distribution group / store name and id are passed, the id is taking precedence. |  [optional] |
|**name** | **String** | Name of a distribution group / distribution store. The release will be associated with this distribution group or store. If the distribution group / store doesn&#39;t exist a 400 is returned. If both distribution group / store name and id are passed, the id is taking precedence. |  [optional] |



