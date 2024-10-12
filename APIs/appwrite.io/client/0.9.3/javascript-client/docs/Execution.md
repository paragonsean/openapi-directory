# Appwrite.Execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Execution ID. | 
**dateCreated** | **Number** | The execution creation date in Unix timestamp. | 
**exitCode** | **Number** | The script exit code. | 
**functionId** | **String** | Function ID. | 
**status** | **String** | The status of the function execution. Possible values can be: &#x60;waiting&#x60;, &#x60;processing&#x60;, &#x60;completed&#x60;, or &#x60;failed&#x60;. | 
**stderr** | **String** | The script stderr output string. Logs the last 4,000 characters of the execution stderr output | 
**stdout** | **String** | The script stdout output string. Logs the last 4,000 characters of the execution stdout output. | 
**time** | **Number** | The script execution time in seconds. | 
**trigger** | **String** | The trigger that caused the function to execute. Possible values can be: &#x60;http&#x60;, &#x60;schedule&#x60;, or &#x60;event&#x60;. | 


