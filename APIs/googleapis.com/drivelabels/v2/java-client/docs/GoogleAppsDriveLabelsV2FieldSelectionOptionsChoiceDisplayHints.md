

# GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHints

UI display hints for rendering an option.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**badgeColors** | [**GoogleAppsDriveLabelsV2BadgeColors**](GoogleAppsDriveLabelsV2BadgeColors.md) |  |  [optional] |
|**badgePriority** | **String** | The priority of this badge. Used to compare and sort between multiple badges. A lower number means the badge should be shown first. When a badging configuration is not present, this will be 0. Otherwise, this will be set to &#x60;BadgeConfig.priority_override&#x60; or the default heuristic which prefers creation date of the label, and field and option priority. |  [optional] |
|**darkBadgeColors** | [**GoogleAppsDriveLabelsV2BadgeColors**](GoogleAppsDriveLabelsV2BadgeColors.md) |  |  [optional] |
|**disabled** | **Boolean** | Whether the option should be shown in the UI as disabled. |  [optional] |
|**hiddenInSearch** | **Boolean** | This option should be hidden in the search menu when searching for Drive items. |  [optional] |
|**shownInApply** | **Boolean** | This option should be shown in the apply menu when applying values to a Drive item. |  [optional] |



