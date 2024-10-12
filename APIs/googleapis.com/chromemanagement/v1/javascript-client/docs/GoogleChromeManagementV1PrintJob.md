# ChromeManagementApi.GoogleChromeManagementV1PrintJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colorMode** | **String** | Color mode. | [optional] 
**completeTime** | **String** | Print job completion timestamp. | [optional] 
**copyCount** | **Number** | Number of copies. | [optional] 
**createTime** | **String** | Print job creation timestamp. | [optional] 
**documentPageCount** | **Number** | Number of pages in the document. | [optional] 
**duplexMode** | **String** | Duplex mode. | [optional] 
**id** | **String** | Unique ID of the print job. | [optional] 
**printer** | **String** | Name of the printer used for printing. | [optional] 
**printerId** | **String** | API ID of the printer used for printing. | [optional] 
**state** | **String** | The final state of the job. | [optional] 
**title** | **String** | The title of the document. | [optional] 
**userEmail** | **String** | The primary e-mail address of the user who submitted the print job. | [optional] 
**userId** | **String** | The unique Directory API ID of the user who submitted the print job. | [optional] 



## Enum: ColorModeEnum


* `COLOR_MODE_UNSPECIFIED` (value: `"COLOR_MODE_UNSPECIFIED"`)

* `BLACK_AND_WHITE` (value: `"BLACK_AND_WHITE"`)

* `COLOR` (value: `"COLOR"`)





## Enum: DuplexModeEnum


* `DUPLEX_MODE_UNSPECIFIED` (value: `"DUPLEX_MODE_UNSPECIFIED"`)

* `ONE_SIDED` (value: `"ONE_SIDED"`)

* `TWO_SIDED_LONG_EDGE` (value: `"TWO_SIDED_LONG_EDGE"`)

* `TWO_SIDED_SHORT_EDGE` (value: `"TWO_SIDED_SHORT_EDGE"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PRINTED` (value: `"PRINTED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `FAILED` (value: `"FAILED"`)




