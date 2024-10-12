

# GetEAadhaarDataInXMLFormatId404Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  [optional] |
|**errorDescription** | [**ErrorDescriptionEnum**](#ErrorDescriptionEnum) |  |  [optional] |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| LINKED | &quot;aadhaar_not_linked&quot; |
| AVAILABLE | &quot;aadhaar_not_available&quot; |



## Enum: ErrorDescriptionEnum

| Name | Value |
|---- | -----|
| IS_NOT_LINKED_TO_THE_ACCOUNT | &quot;Aadhaar is not linked to the account&quot; |
| DATA_IS_NOT_AVAILABLE_FOR_THIS_USER_PLEASE_PERFORM_AADHAAR_E_KYC_AGAIN_ | &quot;Aadhaar data is not available for this user. Please perform Aadhaar eKYC again.&quot; |



