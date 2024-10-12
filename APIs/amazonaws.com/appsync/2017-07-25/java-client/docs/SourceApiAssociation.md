

# SourceApiAssociation

<p>Describes the configuration of a source API. A source API is a GraphQL API that is linked to a merged API. There can be multiple source APIs attached to each merged API. When linked to a merged API, the source API's schema, data sources, and resolvers will be combined with other linked source API data to form a new, singular API. </p> <p>Source APIs can originate from your account or from other accounts via Amazon Web Services Resource Access Manager. For more information about sharing resources from other accounts, see <a href=\"https://docs.aws.amazon.com/ram/latest/userguide/what-is.html\">What is Amazon Web Services Resource Access Manager?</a> in the <i>Amazon Web Services Resource Access Manager</i> guide.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associationId** | [**String**](String.md) |  |  [optional] |
|**associationArn** | [**String**](String.md) |  |  [optional] |
|**sourceApiId** | [**String**](String.md) |  |  [optional] |
|**sourceApiArn** | [**String**](String.md) |  |  [optional] |
|**mergedApiArn** | [**String**](String.md) |  |  [optional] |
|**mergedApiId** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**sourceApiAssociationConfig** | [**AssociateMergedGraphqlApiRequestSourceApiAssociationConfig**](AssociateMergedGraphqlApiRequestSourceApiAssociationConfig.md) |  |  [optional] |
|**sourceApiAssociationStatus** | [**SourceApiAssociationStatus**](SourceApiAssociationStatus.md) |  |  [optional] |
|**sourceApiAssociationStatusDetail** | [**String**](String.md) |  |  [optional] |
|**lastSuccessfulMergeDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



