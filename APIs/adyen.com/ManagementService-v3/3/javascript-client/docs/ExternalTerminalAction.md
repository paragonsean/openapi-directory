# ManagementApi.ExternalTerminalAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionType** | **String** | The type of terminal action: **InstallAndroidApp**, **UninstallAndroidApp**, **InstallAndroidCertificate**, or **UninstallAndroidCertificate**. | [optional] 
**config** | **String** | Technical information about the terminal action. | [optional] 
**confirmedAt** | **Date** | The date and time when the action was carried out. | [optional] 
**id** | **String** | The unique ID of the terminal action. | [optional] 
**result** | **String** | The result message for the action. | [optional] 
**scheduledAt** | **Date** | The date and time when the action was scheduled to happen. | [optional] 
**status** | **String** | The status of the terminal action: **pending**, **successful**, **failed**, **cancelled**, or **tryLater**. | [optional] 
**terminalId** | **String** | The unique ID of the terminal that the action applies to. | [optional] 


