# AzureMediaServices.JobInputClip

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | [**ClipTime**](ClipTime.md) |  | [optional] 
**files** | **[String]** | List of files. Required for JobInputHttp. Maximum of 4000 characters each. | [optional] 
**label** | **String** | A label that is assigned to a JobInputClip, that is used to satisfy a reference used in the Transform. For example, a Transform can be authored so as to take an image file with the label &#39;xyz&#39; and apply it as an overlay onto the input video before it is encoded. When submitting a Job, exactly one of the JobInputs should be the image file, and it should have the label &#39;xyz&#39;. | [optional] 
**start** | [**ClipTime**](ClipTime.md) |  | [optional] 


