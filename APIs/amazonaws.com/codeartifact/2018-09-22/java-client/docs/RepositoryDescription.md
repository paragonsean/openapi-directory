

# RepositoryDescription

 The details of a repository stored in CodeArtifact. A CodeArtifact repository contains a set of package versions, each of which maps to a set of assets. Repositories are polyglot—a single repository can contain packages of any supported type. Each repository exposes endpoints for fetching and publishing packages using tools like the <code>npm</code> CLI, the Maven CLI (<code>mvn</code>), and <code>pip</code>. You can create up to 100 repositories per Amazon Web Services account. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  [optional] |
|**administratorAccount** | [**String**](String.md) |  |  [optional] |
|**domainName** | [**String**](String.md) |  |  [optional] |
|**domainOwner** | [**String**](String.md) |  |  [optional] |
|**arn** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**upstreams** | [**List**](List.md) |  |  [optional] |
|**externalConnections** | [**List**](List.md) |  |  [optional] |
|**createdTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



