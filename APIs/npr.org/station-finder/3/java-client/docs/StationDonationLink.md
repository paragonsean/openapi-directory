

# StationDonationLink

A link to a pledge page for the station

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**href** | **URI** | The link to be followed |  |
|**guid** | **String** | The system&#39;s internal unique identifier for a link, not typically used by consumers |  [optional] |
|**title** | **String** | The link text, provided by the station, for the URL |  [optional] |
|**typeName** | **String** | The semantic name corresponding to the &#x60;typeId&#x60; |  |
|**typeId** | [**TypeIdEnum**](#TypeIdEnum) | An identifier for the type of link; &#39;4&#39; denotes a generic pledge page, while &#39;27&#39; is an NPR One-specific pledge page |  |



## Enum: TypeIdEnum

| Name | Value |
|---- | -----|
| _4 | &quot;4&quot; |
| _27 | &quot;27&quot; |
| _28 | &quot;28&quot; |
| _29 | &quot;29&quot; |



