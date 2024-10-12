

# KeywordAssignedTargetingOptionDetails

Details for assigned keyword targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_KEYWORD`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyword** | **String** | Required. The keyword, for example &#x60;car insurance&#x60;. Positive keyword cannot be offensive word. Must be UTF-8 encoded with a maximum size of 255 bytes. Maximum number of characters is 80. Maximum number of words is 10. |  [optional] |
|**negative** | **Boolean** | Indicates if this option is being negatively targeted. |  [optional] |



