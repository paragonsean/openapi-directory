# DracoonApi.UpdateUploadSharesBulkRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration** | [**ObjectExpiration**](ObjectExpiration.md) |  | [optional] 
**filesExpiryPeriod** | **Number** | Number of days after which uploaded files expire | [optional] 
**maxSize** | **Number** | Maximal total size of uploaded files (in bytes) | [optional] 
**maxSlots** | **Number** | Maximal amount of files to upload | [optional] 
**objectIds** | **[Number]** | List of ids | 
**resetFilesExpiryPeriod** | **Boolean** | Set &#39;true&#39; to reset &#39;filesExpiryPeriod&#39; for Upload Share | [optional] 
**resetMaxSize** | **Boolean** | Set &#39;true&#39; to reset &#39;maxSize&#39; for Upload Share | [optional] 
**resetMaxSlots** | **Boolean** | Set &#39;true&#39; to reset &#39;maxSlots&#39; for Upload Share | [optional] 
**showCreatorName** | **Boolean** | Show creator first and last name. | [optional] 
**showCreatorUsername** | **Boolean** | Show creator email address. | [optional] 
**showUploadedFiles** | **Boolean** | Allow display of already uploaded files | [optional] 


