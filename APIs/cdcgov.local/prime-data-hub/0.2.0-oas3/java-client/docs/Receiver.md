

# Receiver

A receiver of reports from the data hub

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Display ready description of the receiver |  |
|**jurisdictionalFilters** | [**List&lt;ReceiverJurisdictionalFiltersInner&gt;**](ReceiverJurisdictionalFiltersInner.md) | What items to include in the report. |  [optional] |
|**meta** | [**SettingMetadata**](SettingMetadata.md) |  |  [optional] |
|**name** | **String** | The unique name for the receiver. Should include the organization name as a prefix. |  |
|**organizationName** | **String** | The name of the organization that this receiver belongs to |  [optional] [readonly] |
|**timing** | [**ReceiverTiming**](ReceiverTiming.md) |  |  |
|**topic** | **String** | The topic of for this receiver. Must match the supported topics. |  |
|**translations** | [**List&lt;ReceiverTranslationsInner&gt;**](ReceiverTranslationsInner.md) | How the report is translated from the sender. A report can be sent in multiple ways. |  [optional] |



