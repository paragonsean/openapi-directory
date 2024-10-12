

# DestinyDefinitionsDestinyDisplayCategoryDefinition

Display Categories are different from \"categories\" in that these are specifically for visual grouping and display of categories in Vendor UI. The \"categories\" structure is for validation of the contained items, and can be categorized entirely separately from \"Display Categories\", there need be and often will be no meaningful relationship between the two.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayCategoryHash** | **Integer** |  |  [optional] |
|**displayInBanner** | **Boolean** | If true, this category should be displayed in the \&quot;Banner\&quot; section of the vendor&#39;s UI. |  [optional] |
|**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  |  [optional] |
|**displayStyleHash** | **Integer** | An indicator of how the category will be displayed in the UI. It&#39;s up to you to do something cool or interesting in response to this, or just to treat it as a normal category. |  [optional] |
|**displayStyleIdentifier** | **String** | An indicator of how the category will be displayed in the UI. It&#39;s up to you to do something cool or interesting in response to this, or just to treat it as a normal category. |  [optional] |
|**identifier** | **String** | A string identifier for the display category. |  [optional] |
|**index** | **Integer** |  |  [optional] |
|**progressionHash** | **Integer** | If it exists, this is the hash identifier of a DestinyProgressionDefinition that represents the progression to show on this display category.  Specific categories can now have thier own distinct progression, apparently. So that&#39;s cool. |  [optional] |
|**sortOrder** | **Integer** | If this category sorts items in a nonstandard way, this will be the way we sort. |  [optional] |



