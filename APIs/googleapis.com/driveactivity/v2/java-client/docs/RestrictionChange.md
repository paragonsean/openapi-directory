

# RestrictionChange

Information about restriction policy changes to a feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**feature** | [**FeatureEnum**](#FeatureEnum) | The feature which had a change in restriction policy. |  [optional] |
|**newRestriction** | [**NewRestrictionEnum**](#NewRestrictionEnum) | The restriction in place after the change. |  [optional] |



## Enum: FeatureEnum

| Name | Value |
|---- | -----|
| FEATURE_UNSPECIFIED | &quot;FEATURE_UNSPECIFIED&quot; |
| SHARING_OUTSIDE_DOMAIN | &quot;SHARING_OUTSIDE_DOMAIN&quot; |
| DIRECT_SHARING | &quot;DIRECT_SHARING&quot; |
| ITEM_DUPLICATION | &quot;ITEM_DUPLICATION&quot; |
| DRIVE_FILE_STREAM | &quot;DRIVE_FILE_STREAM&quot; |
| FILE_ORGANIZER_CAN_SHARE_FOLDERS | &quot;FILE_ORGANIZER_CAN_SHARE_FOLDERS&quot; |



## Enum: NewRestrictionEnum

| Name | Value |
|---- | -----|
| RESTRICTION_UNSPECIFIED | &quot;RESTRICTION_UNSPECIFIED&quot; |
| UNRESTRICTED | &quot;UNRESTRICTED&quot; |
| FULLY_RESTRICTED | &quot;FULLY_RESTRICTED&quot; |



