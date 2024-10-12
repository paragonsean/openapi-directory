# ContentDepot.ApiV2MetapubProgramInformationBatchPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **String** | The format of the metadata file defining the create or update actions to be performed on one or more EPG programs. For more information on how RadioDNS EPG maps to ContentDepot &lt;a href&#x3D;\&quot;/api/epg-cd-mapping.html\&quot;&gt;click here &lt;/a&gt; | 
**name** | **String** | An optional human readable name for the batch. | [optional] 
**program** | [**ApiV2MetapubProgramInformationBatchPostRequestProgram**](ApiV2MetapubProgramInformationBatchPostRequestProgram.md) |  | [optional] 
**uri** | **String** | The URI to the metadata file. Currently only the &#x60;&#x60;&#x60;cddrive&#x60;&#x60;&#x60; scheme is supported. | 



## Enum: FormatEnum


* `radiodns` (value: `"radiodns"`)




