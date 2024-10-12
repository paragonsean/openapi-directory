# AuthorizedPartnerApiSpecification.Sample3Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **String** | This contains the date of file upload in case of self uploaded documents | 
**description** | **String** | This is the descriptive document type stored in DigiLocker such as ‘Income Certificate’ or ‘Driving License’. | 
**id** | **Number** | The id if this item is a folder. | 
**issuer** | **String** | The name of the issuer. This is blank in case of uploaded documents and folders. | 
**mime** | **String** | The mime type of the file. This field will contain “application/PDF” for PDF files; “image/png” for PNG files and “image/jpg” or “image/jpeg” for JPG/JPEG files. This will be blank in case of folder. | 
**name** | **String** | The name of the file or folder. | 
**parent** | **String** | The id of the parent folder. | 
**size** | **String** | Size of file or folder. | 
**type** | **String** | String dir for folder and string file for file. | 
**uri** | **String** | This is the unique identifier of the document shared by the user in DigiLocker. You will use this identifier to get the actual file from DigiLocker using the API. URI will be blank in case of folder. | 


