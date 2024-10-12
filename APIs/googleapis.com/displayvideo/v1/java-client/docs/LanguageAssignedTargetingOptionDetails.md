

# LanguageAssignedTargetingOptionDetails

Details for assigned language targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_LANGUAGE`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Output only. The display name of the language (e.g., \&quot;French\&quot;). |  [optional] [readonly] |
|**negative** | **Boolean** | Indicates if this option is being negatively targeted. All assigned language targeting options on the same resource must have the same value for this field. |  [optional] |
|**targetingOptionId** | **String** | Required. The targeting_option_id of a TargetingOption of type &#x60;TARGETING_TYPE_LANGUAGE&#x60;. |  [optional] |



