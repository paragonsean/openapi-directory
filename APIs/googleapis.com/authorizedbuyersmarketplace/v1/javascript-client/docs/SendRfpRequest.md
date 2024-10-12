# AuthorizedBuyersMarketplaceApi.SendRfpRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyerContacts** | [**[Contact]**](Contact.md) | Contact information for the buyer. | [optional] 
**client** | **String** | If the current buyer is sending the RFP on behalf of its client, use this field to specify the name of the client in the format: &#x60;buyers/{accountId}/clients/{clientAccountid}&#x60;. | [optional] 
**displayName** | **String** | Required. The display name of the proposal being created by this RFP. | [optional] 
**estimatedGrossSpend** | [**Money**](Money.md) |  | [optional] 
**flightEndTime** | **String** | Required. Proposed flight end time of the RFP. A timestamp in RFC3339 UTC \&quot;Zulu\&quot; format. Note that the specified value will be truncated to a granularity of one second. | [optional] 
**flightStartTime** | **String** | Required. Proposed flight start time of the RFP. A timestamp in RFC3339 UTC \&quot;Zulu\&quot; format. Note that the specified value will be truncated to a granularity of one second. | [optional] 
**geoTargeting** | [**CriteriaTargeting**](CriteriaTargeting.md) |  | [optional] 
**inventorySizeTargeting** | [**InventorySizeTargeting**](InventorySizeTargeting.md) |  | [optional] 
**note** | **String** | A message that is sent to the publisher. Maximum length is 1024 characters. | [optional] 
**preferredDealTerms** | [**PreferredDealTerms**](PreferredDealTerms.md) |  | [optional] 
**programmaticGuaranteedTerms** | [**ProgrammaticGuaranteedTerms**](ProgrammaticGuaranteedTerms.md) |  | [optional] 
**publisherProfile** | **String** | Required. The profile of the publisher who will receive this RFP in the format: &#x60;buyers/{accountId}/publisherProfiles/{publisherProfileId}&#x60;. | [optional] 


