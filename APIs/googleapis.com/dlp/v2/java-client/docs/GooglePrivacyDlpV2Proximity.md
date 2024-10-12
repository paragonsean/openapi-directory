

# GooglePrivacyDlpV2Proximity

Message for specifying a window around a finding to apply a detection rule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**windowAfter** | **Integer** | Number of characters after the finding to consider. |  [optional] |
|**windowBefore** | **Integer** | Number of characters before the finding to consider. For tabular data, if you want to modify the likelihood of an entire column of findngs, set this to 1. For more information, see [Hotword example: Set the match likelihood of a table column] (https://cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood#match-column-values). |  [optional] |



