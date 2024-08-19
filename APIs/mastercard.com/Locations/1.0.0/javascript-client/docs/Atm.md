# LocationsApi.Atm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessFees** | **String** | This value indicates under what conditions access fees are charged. Options are UNKNOWN, DOMESTIC, INTERNATIONAL, DOMESTIC_AND_INTERNATIONAL, NO_FEE. | [optional] 
**availability** | **String** | This value indicates the availability hours of the ATM. Options are UNKNOWN, ALWAYS_AVAILABLE, BUSINESS_HOURS, IRREGULAR_HOURS. | [optional] 
**camera** | **String** | This value indicates whether or not a security camera is present or near ATM. Options are UNKNOWN, YES, NO. | [optional] 
**handicapAccessible** | **String** | This value indicates whether or not the ATM is accessible by wheelchair. Options are UNKNOWN, YES, NO. | [optional] 
**internationalMaestroAccepted** | **Number** | This field will provide ATM Terminals which can still process Maestro transactions but are not yet EMV chip reader enabled. Information available only for USA and Argentina till October 2014. 1&#x3D;Yes. | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**owner** | **String** | This is the DBA name of the financial institution affiliate or independent service organization. | [optional] 
**sharedDeposit** | **String** | This value indicates whether or not the ATM participates in the MasterCard Shared Deposit network. Options are YES or NO. | [optional] 
**sponsor** | **String** | This is the legal or business name of the entity that sponsors the owner of the ATM into the MasterCard network. | [optional] 
**supportEMV** | **Number** | This indicates whether the ATM has the ability to read chip cards or not. Options are 1 &#x3D; Yes 2 &#x3D; No or Empty &#x3D; Unknown. | [optional] 
**surchargeFreeAlliance** | **String** | This value indicates whether or not the ATM participates in the MasterCard Shared (only) Surcharge Free Alliance network. Options are YES or NO. | [optional] 
**surchargeFreeAllianceNetwork** | **String** | This value indicates whether or not the ATM participates in the MasterCard Shared (only) Surcharge Free Alliance network. Options are DOES_NOT_PARTICIPATE_IN_SFA, ALLPOINT_PREPAID, MONEYPASS_DEBIT, and ALL_SURCHARGE_FREE. | [optional] 


