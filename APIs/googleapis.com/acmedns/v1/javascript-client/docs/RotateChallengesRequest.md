# AcmeDnsApi.RotateChallengesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **Blob** | Required. ACME DNS access token. This is a base64 token secret that is procured from the Google Domains website. It authorizes ACME TXT record updates for a domain. | [optional] 
**keepExpiredRecords** | **Boolean** | Keep records older than 30 days that were used for previous requests. | [optional] 
**recordsToAdd** | [**[AcmeTxtRecord]**](AcmeTxtRecord.md) | ACME TXT record challenges to add. Supports multiple challenges on the same FQDN. | [optional] 
**recordsToRemove** | [**[AcmeTxtRecord]**](AcmeTxtRecord.md) | ACME TXT record challenges to remove. | [optional] 


