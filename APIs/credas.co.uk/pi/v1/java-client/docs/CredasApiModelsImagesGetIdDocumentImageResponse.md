

# CredasApiModelsImagesGetIdDocumentImageResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressCity** | **String** |  |  [optional] |
|**addressFull** | **String** |  |  [optional] |
|**addressPostcode** | **String** |  |  [optional] |
|**country** | **String** |  |  [optional] |
|**countryCode** | **String** |  |  [optional] |
|**dateCreated** | **OffsetDateTime** |  |  |
|**dateOfBirth** | **OffsetDateTime** |  |  [optional] |
|**description** | **String** |  |  |
|**documentAnalysisResult** | [**DocumentAnalysisResultEnum**](#DocumentAnalysisResultEnum) | Unknown &#x3D; 0, Passed &#x3D; 1, Refer &#x3D; 2, Expired &#x3D; 3, NotSupported &#x3D; 4, Undefined &#x3D; 5, Fail &#x3D; 10, NotPerformed &#x3D; 11 |  [optional] |
|**documentNumber** | **String** |  |  [optional] |
|**documentSide** | [**DocumentSideEnum**](#DocumentSideEnum) | Front &#x3D; 1, Back &#x3D; 2 |  [optional] |
|**expiryDate** | **OffsetDateTime** |  |  [optional] |
|**facialMatch** | **Boolean** |  |  |
|**forename** | **String** |  |  [optional] |
|**fullName** | **String** |  |  [optional] |
|**hiResUrl** | **String** |  |  |
|**id** | **UUID** |  |  |
|**isUnderReview** | **Boolean** |  |  [optional] |
|**manuallyVerified** | **Boolean** |  |  [optional] |
|**middleName** | **String** |  |  [optional] |
|**mrz1** | **String** |  |  [optional] |
|**mrz2** | **String** |  |  [optional] |
|**mrz3** | **String** |  |  [optional] |
|**nameCheck** | **Boolean** |  |  |
|**nameCheckMethod** | [**NameCheckMethodEnum**](#NameCheckMethodEnum) | Unknown &#x3D; 0, Automatic &#x3D; 1, Manual &#x3D; 2 |  |
|**nfcCheck** | **Boolean** |  |  |
|**nfcFacialUrl** | **String** |  |  [optional] |
|**nfcReadStatus** | [**NfcReadStatusEnum**](#NfcReadStatusEnum) | Unknown &#x3D; 0, Passed &#x3D; 1, Failed &#x3D; 2, NotAttempted &#x3D; 3, Skipped &#x3D; 4, Unavailable &#x3D; 5, NotAllowed &#x3D; 6, NotTrusted &#x3D; 7, NotApplicable &#x3D; 8, Expired &#x3D; 9, UnavailableWebJourney &#x3D; 10 |  |
|**primaryScanId** | **UUID** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Indicates the verification status of the document itself by combining visual analysis and NFC verification results. &lt;/br&gt;Note that this may be a pass even if facial or name matches have failed.&lt;br /&gt;  values&#x3D;&gt; Unknown &#x3D; 0, Pass &#x3D; 1, Refer &#x3D; 2, Fail &#x3D; 3 |  |
|**surname** | **String** |  |  [optional] |
|**url** | **String** |  |  |



## Enum: DocumentAnalysisResultEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |
| NUMBER_10 | 10 |
| NUMBER_11 | 11 |



## Enum: DocumentSideEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: NameCheckMethodEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: NfcReadStatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |
| NUMBER_6 | 6 |
| NUMBER_7 | 7 |
| NUMBER_8 | 8 |
| NUMBER_9 | 9 |
| NUMBER_10 | 10 |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |



