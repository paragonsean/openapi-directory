# ContentApiForShopping.TransitTable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postalCodeGroupNames** | **[String]** | A list of postal group names. The last value can be &#x60;\&quot;all other locations\&quot;&#x60;. Example: &#x60;[\&quot;zone 1\&quot;, \&quot;zone 2\&quot;, \&quot;all other locations\&quot;]&#x60;. The referred postal code groups must match the delivery country of the service. | [optional] 
**rows** | [**[TransitTableTransitTimeRow]**](TransitTableTransitTimeRow.md) |  | [optional] 
**transitTimeLabels** | **[String]** | A list of transit time labels. The last value can be &#x60;\&quot;all other labels\&quot;&#x60;. Example: &#x60;[\&quot;food\&quot;, \&quot;electronics\&quot;, \&quot;all other labels\&quot;]&#x60;. | [optional] 


