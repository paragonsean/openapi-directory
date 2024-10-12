

# Attachment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | The document in Base64-encoded string format. |  |
|**contentType** | **String** | The file format.   Possible values: **application/pdf**, **image/jpg**, **image/jpeg**, **image/png**.  |  [optional] |
|**filename** | **String** | The name of the file including the file extension. |  [optional] |
|**pageType** | **String** | Specifies which side of the ID card is uploaded.  * When &#x60;type&#x60; is **driversLicense** or **identityCard**, set this to **front** or **back**.  * When omitted, we infer the page number based on the order of attachments. |  [optional] |



