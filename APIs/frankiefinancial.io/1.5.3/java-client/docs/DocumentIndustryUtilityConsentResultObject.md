

# DocumentIndustryUtilityConsentResultObject

Utility industry explicit consent response object. Used to wrap up industry-specific resultsets.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentId** | **UUID** | The document that was used to generate these results. |  [optional] |
|**industryProcess** | **String** |  |  [optional] |
|**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  |  [optional] |
|**utilityConsentResult** | [**DocumentIndustryUtilityConsentResultObjectUtilityConsentResult**](DocumentIndustryUtilityConsentResultObjectUtilityConsentResult.md) |  |  [optional] |



