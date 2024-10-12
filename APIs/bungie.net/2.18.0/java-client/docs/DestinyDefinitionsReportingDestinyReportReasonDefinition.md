

# DestinyDefinitionsReportingDestinyReportReasonDefinition

A specific reason for being banned. Only accessible under the related category (DestinyReportReasonCategoryDefinition) under which it is shown. Note that this means that report reasons' reasonHash are not globally unique: and indeed, entries like \"Other\" are defined under most categories for example.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  |  [optional] |
|**reasonHash** | **Integer** | The identifier for the reason: they are only guaranteed unique under the Category in which they are found. |  [optional] |



