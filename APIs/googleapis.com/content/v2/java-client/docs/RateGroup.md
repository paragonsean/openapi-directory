

# RateGroup


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicableShippingLabels** | **List&lt;String&gt;** | A list of shipping labels defining the products to which this rate group applies to. This is a disjunction: only one of the labels has to match for the rate group to apply. May only be empty for the last rate group of a service. Required. |  [optional] |
|**carrierRates** | [**List&lt;CarrierRate&gt;**](CarrierRate.md) | A list of carrier rates that can be referred to by &#x60;mainTable&#x60; or &#x60;singleValue&#x60;. |  [optional] |
|**mainTable** | [**Table**](Table.md) |  |  [optional] |
|**name** | **String** | Name of the rate group. Optional. If set has to be unique within shipping service. |  [optional] |
|**singleValue** | [**Value**](Value.md) |  |  [optional] |
|**subtables** | [**List&lt;Table&gt;**](Table.md) | A list of subtables referred to by &#x60;mainTable&#x60;. Can only be set if &#x60;mainTable&#x60; is set. |  [optional] |



