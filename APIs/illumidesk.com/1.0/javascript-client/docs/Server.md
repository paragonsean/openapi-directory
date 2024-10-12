# IllumiDesk.Server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **Object** | Server configuration option. Values are jupyter, restful and cron. | [optional] 
**connected** | **[String]** | Array that represents what other servers the server is connected to. | [optional] 
**createdAt** | **String** | Date and time when server was created. | [optional] 
**createdBy** | **String** | User that created server. | [optional] 
**endpoint** | **String** | Server endpoint path. | [optional] 
**host** | **String** | Value that represents user defined host, otherwise known as BYON (Bring Your Own Node).  | [optional] 
**id** | **String** | Server unique identifier in UUID format. | [optional] 
**imageName** | **String** | Server image source, such as 3blades/tensorflow-notebook.  | [optional] 
**logsUrl** | **String** | A WebSocket URL for streaming stdout and stderr logs from the server.  | [optional] 
**name** | **String** | Server name. | 
**project** | **String** | Project name. | [optional] 
**serverSize** | **String** | Server size unique identifier. | [optional] 
**startupScript** | **String** | Optional startup script to use when launching server. | [optional] 
**status** | **String** | Server status, such as Running or Error. | [optional] 
**statusUrl** | **String** | A WebSocket URL for listening to server status changes.  | [optional] 



## Enum: StatusEnum


* `Stopped` (value: `"Stopped"`)

* `Running` (value: `"Running"`)

* `Error` (value: `"Error"`)




