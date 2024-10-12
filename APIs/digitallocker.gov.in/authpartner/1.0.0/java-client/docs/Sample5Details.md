

# Sample5Details


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**digilockerid** | **String** | A unique 36 character DigiLocker Id of the user account. |  |
|**dob** | **String** | This is date of birth of the user as registered with DigiLocker in DDMMYYYY format. |  |
|**eaadhar** | [**EaadharEnum**](#EaadharEnum) | This indicates whether eAadhaar data is available for this account. Possible values are Y and N. |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) | This is gender of the user as registered with DigiLocker. The possible values are M, F, T for male, female and transgender respectively. |  |
|**name** | **String** | The name of the user as registered with DigiLocker. |  |



## Enum: EaadharEnum

| Name | Value |
|---- | -----|
| Y | &quot;Y&quot; |
| N | &quot;N&quot; |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| M | &quot;M&quot; |
| F | &quot;F&quot; |
| T | &quot;T&quot; |



