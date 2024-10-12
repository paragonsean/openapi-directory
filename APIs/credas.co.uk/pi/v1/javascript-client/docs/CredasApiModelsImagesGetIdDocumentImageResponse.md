# CredasApi.CredasApiModelsImagesGetIdDocumentImageResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressCity** | **String** |  | [optional] 
**addressFull** | **String** |  | [optional] 
**addressPostcode** | **String** |  | [optional] 
**country** | **String** |  | [optional] 
**countryCode** | **String** |  | [optional] 
**dateCreated** | **Date** |  | 
**dateOfBirth** | **Date** |  | [optional] 
**description** | **String** |  | 
**documentAnalysisResult** | **Number** | Unknown &#x3D; 0, Passed &#x3D; 1, Refer &#x3D; 2, Expired &#x3D; 3, NotSupported &#x3D; 4, Undefined &#x3D; 5, Fail &#x3D; 10, NotPerformed &#x3D; 11 | [optional] 
**documentNumber** | **String** |  | [optional] 
**documentSide** | **Number** | Front &#x3D; 1, Back &#x3D; 2 | [optional] 
**expiryDate** | **Date** |  | [optional] 
**facialMatch** | **Boolean** |  | 
**forename** | **String** |  | [optional] 
**fullName** | **String** |  | [optional] 
**hiResUrl** | **String** |  | 
**id** | **String** |  | 
**isUnderReview** | **Boolean** |  | [optional] 
**manuallyVerified** | **Boolean** |  | [optional] 
**middleName** | **String** |  | [optional] 
**mrz1** | **String** |  | [optional] 
**mrz2** | **String** |  | [optional] 
**mrz3** | **String** |  | [optional] 
**nameCheck** | **Boolean** |  | 
**nameCheckMethod** | **Number** | Unknown &#x3D; 0, Automatic &#x3D; 1, Manual &#x3D; 2 | 
**nfcCheck** | **Boolean** |  | 
**nfcFacialUrl** | **String** |  | [optional] 
**nfcReadStatus** | **Number** | Unknown &#x3D; 0, Passed &#x3D; 1, Failed &#x3D; 2, NotAttempted &#x3D; 3, Skipped &#x3D; 4, Unavailable &#x3D; 5, NotAllowed &#x3D; 6, NotTrusted &#x3D; 7, NotApplicable &#x3D; 8, Expired &#x3D; 9, UnavailableWebJourney &#x3D; 10 | 
**primaryScanId** | **String** |  | [optional] 
**status** | **Number** | Indicates the verification status of the document itself by combining visual analysis and NFC verification results. &lt;/br&gt;Note that this may be a pass even if facial or name matches have failed.&lt;br /&gt;  values&#x3D;&gt; Unknown &#x3D; 0, Pass &#x3D; 1, Refer &#x3D; 2, Fail &#x3D; 3 | 
**surname** | **String** |  | [optional] 
**url** | **String** |  | 



## Enum: DocumentAnalysisResultEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)

* `10` (value: `10`)

* `11` (value: `11`)





## Enum: DocumentSideEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)





## Enum: NameCheckMethodEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)





## Enum: NfcReadStatusEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)

* `6` (value: `6`)

* `7` (value: `7`)

* `8` (value: `8`)

* `9` (value: `9`)

* `10` (value: `10`)





## Enum: StatusEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)




