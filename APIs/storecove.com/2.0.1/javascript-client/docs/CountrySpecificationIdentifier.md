# StorecoveApi.CountrySpecificationIdentifier

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**centalizedIdentifierTest** | **String** | The centralized identifier to use for routing in test cases, if the \&quot;centralized\&quot; proprerty is true. May not always be available depending on the country and network. | [optional] 
**centralized** | **Boolean** | Whether or not the identifier represents a centralized routing identifier. This is used in SG, AT and FR where all government invoices are routed to a central accesspoint with a single identifier. This field can only be present for routing identifiers. | [optional] 
**centralizedIdentifier** | **String** | The centralized identifier to use for routing, if the \&quot;centralized\&quot; proprerty is true. | [optional] 
**description** | **String** | Identifier description. | [optional] 
**scheme** | **String** | The scheme of the identifier | [optional] 
**schemeNumercial** | **String** | The numerical version of the scheme of the identifier | [optional] 
**schemeType** | **String** | The scheme type of the identifier. Currently always \&quot;iso6523-actorid-upis\&quot; | [optional] 



## Enum: SchemeTypeEnum


* `iso6523-actorid-upis` (value: `"iso6523-actorid-upis"`)




