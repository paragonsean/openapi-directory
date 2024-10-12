# FrankieFinancialApi.IndividualData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**[AddressObject]**](AddressObject.md) | List of all found addresses associated with this person  | [optional] 
**beneficiallyHeld** | **Boolean** | If describing an (ultimate) beneficial owner, then if any of the shared held are not benefially held, this field will be set to \&quot;false\&quot;  | 
**dateOfBirth** | **Date** | RFC3339 formatted date | [optional] 
**name** | **String** | Name of the individual  | [optional] 
**percentOwned** | **Number** | If describing an (ultimate) beneficial owner, the percentage of the company owned by this Individual  | 
**role** | **String** | If this individual has a role as an officeholder, such as director, then this will be described here. May be blank.  | 
**screeningResult** | [**ScreeningResult**](ScreeningResult.md) |  | [optional] 


