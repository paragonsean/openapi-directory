# FirebaseHostingApi.PopulateVersionFilesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uploadRequiredHashes** | **[String]** | The content hashes of the specified files that need to be uploaded to the specified URL. | [optional] 
**uploadUrl** | **String** | The URL to which the files should be uploaded, in the format: \&quot;https://upload-firebasehosting.googleapis.com/upload/sites/SITE_ID /versions/VERSION_ID/files\&quot; Perform a multipart &#x60;POST&#x60; of the Gzipped file contents to the URL using a forward slash and the hash of the file appended to the end. | [optional] 


