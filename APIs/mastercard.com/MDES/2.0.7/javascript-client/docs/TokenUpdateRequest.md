# MdesCustomerService.TokenUpdateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountPanSequenceNumber** | **String** | New PAN sequence number to be applied to the updated token(s). Conditional field, must not be present when IssuerProductConfigurationId is present. Optional if updating PAN mapping or Expiration Date. | [optional] 
**auditInfo** | [**AuditInfo**](AuditInfo.md) |  | 
**commentText** | **String** | Comment related to the updated token(s). | [optional] 
**currentAccountPan** | **String** | Current Account PAN of the token(s) to be updated. Conditional field, used for updating all tokens mapped to a single Account PAN and must not be present when TokenUniqueReference is present. | [optional] 
**expirationDate** | **String** | New expiration date to be applied to the updated token(s). Conditional field, must not be present when IssuerProductConfigurationId is present. Optional if updating PAN mapping or PAN Sequence Number. | [optional] 
**issuerProductConfigurationId** | **String** | New product configuration ID to be applied to the updated token(s). Conditional field, must not be present if any of the following are present; NewAccountPan, ExpirationDate, AccountPanSequenceNumber. | [optional] 
**newAccountPan** | **String** | New Account PAN to be applied to the updated token(s) if there is in fact a new Account PAN. Optional if updating Expiration Date or PAN Sequence Number. | [optional] 
**tokenUniqueReference** | **String** | Unique reference of the token to be updated. Conditional field, used for updating a single token and not used when CurrentAccountPan is present. | [optional] 
**updateWalletProviderIndicator** | **String** | Indicates whether the updated token information should be provided to the Wallet Provider. Valid values:&lt;br /&gt;    \&quot;0\&quot; - Pass the updated information to the Wallet Provider&lt;br /&gt;    \&quot;1\&quot; - Do not pass the updated information to the Wallet Provider.&lt;br /&gt;Optional parameter. The default is 1 if not present. | [optional] 


