

# AccountDetails

Contains the account information such as the licensing status for the user in the scope.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountActivity** | [**AccountActivity**](AccountActivity.md) |  |  [optional] |
|**appLicensingVerdict** | [**AppLicensingVerdictEnum**](#AppLicensingVerdictEnum) | Required. Details about the licensing status of the user for the app in the scope. |  [optional] |



## Enum: AppLicensingVerdictEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| LICENSED | &quot;LICENSED&quot; |
| UNLICENSED | &quot;UNLICENSED&quot; |
| UNEVALUATED | &quot;UNEVALUATED&quot; |



