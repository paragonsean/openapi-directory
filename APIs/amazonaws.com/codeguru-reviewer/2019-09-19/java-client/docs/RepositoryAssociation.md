

# RepositoryAssociation

Information about a repository association. The <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_DescribeRepositoryAssociation.html\">DescribeRepositoryAssociation</a> operation returns a <code>RepositoryAssociation</code> object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associationId** | [**String**](String.md) |  |  [optional] |
|**associationArn** | [**String**](String.md) |  |  [optional] |
|**connectionArn** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**owner** | [**String**](String.md) |  |  [optional] |
|**providerType** | [**ProviderType**](ProviderType.md) |  |  [optional] |
|**state** | [**RepositoryAssociationState**](RepositoryAssociationState.md) |  |  [optional] |
|**stateReason** | [**String**](String.md) |  |  [optional] |
|**lastUpdatedTimeStamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**createdTimeStamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**kmSKeyDetails** | [**AssociateRepositoryRequestKMSKeyDetails**](AssociateRepositoryRequestKMSKeyDetails.md) |  |  [optional] |
|**s3RepositoryDetails** | [**S3RepositoryDetails**](S3RepositoryDetails.md) |  |  [optional] |



