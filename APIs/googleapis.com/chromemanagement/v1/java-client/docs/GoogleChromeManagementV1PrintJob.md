

# GoogleChromeManagementV1PrintJob

Represents a request to print a document that has been submitted to a printer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**colorMode** | [**ColorModeEnum**](#ColorModeEnum) | Color mode. |  [optional] |
|**completeTime** | **String** | Print job completion timestamp. |  [optional] |
|**copyCount** | **Integer** | Number of copies. |  [optional] |
|**createTime** | **String** | Print job creation timestamp. |  [optional] |
|**documentPageCount** | **Integer** | Number of pages in the document. |  [optional] |
|**duplexMode** | [**DuplexModeEnum**](#DuplexModeEnum) | Duplex mode. |  [optional] |
|**id** | **String** | Unique ID of the print job. |  [optional] |
|**printer** | **String** | Name of the printer used for printing. |  [optional] |
|**printerId** | **String** | API ID of the printer used for printing. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The final state of the job. |  [optional] |
|**title** | **String** | The title of the document. |  [optional] |
|**userEmail** | **String** | The primary e-mail address of the user who submitted the print job. |  [optional] |
|**userId** | **String** | The unique Directory API ID of the user who submitted the print job. |  [optional] |



## Enum: ColorModeEnum

| Name | Value |
|---- | -----|
| COLOR_MODE_UNSPECIFIED | &quot;COLOR_MODE_UNSPECIFIED&quot; |
| BLACK_AND_WHITE | &quot;BLACK_AND_WHITE&quot; |
| COLOR | &quot;COLOR&quot; |



## Enum: DuplexModeEnum

| Name | Value |
|---- | -----|
| DUPLEX_MODE_UNSPECIFIED | &quot;DUPLEX_MODE_UNSPECIFIED&quot; |
| ONE_SIDED | &quot;ONE_SIDED&quot; |
| TWO_SIDED_LONG_EDGE | &quot;TWO_SIDED_LONG_EDGE&quot; |
| TWO_SIDED_SHORT_EDGE | &quot;TWO_SIDED_SHORT_EDGE&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PRINTED | &quot;PRINTED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| FAILED | &quot;FAILED&quot; |



