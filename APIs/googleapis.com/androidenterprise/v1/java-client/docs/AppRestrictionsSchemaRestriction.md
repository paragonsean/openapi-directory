

# AppRestrictionsSchemaRestriction

A restriction in the App Restriction Schema represents a piece of configuration that may be pre-applied.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultValue** | [**AppRestrictionsSchemaRestrictionRestrictionValue**](AppRestrictionsSchemaRestrictionRestrictionValue.md) |  |  [optional] |
|**description** | **String** | A longer description of the restriction, giving more detail of what it affects. |  [optional] |
|**entry** | **List&lt;String&gt;** | For choice or multiselect restrictions, the list of possible entries&#39; human-readable names. |  [optional] |
|**entryValue** | **List&lt;String&gt;** | For choice or multiselect restrictions, the list of possible entries&#39; machine-readable values. These values should be used in the configuration, either as a single string value for a choice restriction or in a stringArray for a multiselect restriction. |  [optional] |
|**key** | **String** | The unique key that the product uses to identify the restriction, e.g. \&quot;com.google.android.gm.fieldname\&quot;. |  [optional] |
|**nestedRestriction** | [**List&lt;AppRestrictionsSchemaRestriction&gt;**](AppRestrictionsSchemaRestriction.md) | For bundle or bundleArray restrictions, the list of nested restrictions. A bundle restriction is always nested within a bundleArray restriction, and a bundleArray restriction is at most two levels deep. |  [optional] |
|**restrictionType** | [**RestrictionTypeEnum**](#RestrictionTypeEnum) | The type of the restriction. |  [optional] |
|**title** | **String** | The name of the restriction. |  [optional] |



## Enum: RestrictionTypeEnum

| Name | Value |
|---- | -----|
| BOOL | &quot;bool&quot; |
| STRING | &quot;string&quot; |
| INTEGER | &quot;integer&quot; |
| CHOICE | &quot;choice&quot; |
| MULTISELECT | &quot;multiselect&quot; |
| HIDDEN | &quot;hidden&quot; |
| BUNDLE | &quot;bundle&quot; |
| BUNDLE_ARRAY | &quot;bundleArray&quot; |



