

# DomainStatus

The current status of the search domain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainId** | **String** | An internally generated unique identifier for a domain. |  |
|**domainName** | **String** | A string that represents the name of a domain. Domain names must be unique across the domains owned by an account within an AWS region. Domain names must start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen). Uppercase letters and underscores are not allowed. |  |
|**created** | [**Boolean**](Boolean.md) |  |  [optional] |
|**deleted** | [**Boolean**](Boolean.md) |  |  [optional] |
|**numSearchableDocs** | [**Integer**](Integer.md) |  |  [optional] |
|**docService** | [**DomainStatusDocService**](DomainStatusDocService.md) |  |  [optional] |
|**searchService** | [**DomainStatusSearchService**](DomainStatusSearchService.md) |  |  [optional] |
|**requiresIndexDocuments** | [**Boolean**](Boolean.md) |  |  |
|**processing** | [**Boolean**](Boolean.md) |  |  [optional] |
|**searchInstanceType** | [**String**](String.md) |  |  [optional] |
|**searchPartitionCount** | [**Integer**](Integer.md) |  |  [optional] |
|**searchInstanceCount** | [**Integer**](Integer.md) |  |  [optional] |



