# IncreaseApi.Export

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The category of the Export. We may add additional possible values for this enum over time; your application should be able to handle that gracefully. | 
**createdAt** | **Date** | The time the Export was created. | 
**fileDownloadUrl** | **String** | A URL at which the Export&#39;s file can be downloaded. This will be present when the Export&#39;s status transitions to &#x60;complete&#x60;. | 
**fileId** | **String** | The File containing the contents of the Export. This will be present when the Export&#39;s status transitions to &#x60;complete&#x60;. | 
**id** | **String** | The Export identifier. | 
**status** | **String** | The status of the Export. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;export&#x60;. | 



## Enum: CategoryEnum


* `transaction_csv` (value: `"transaction_csv"`)

* `balance_csv` (value: `"balance_csv"`)





## Enum: StatusEnum


* `pending` (value: `"pending"`)

* `complete` (value: `"complete"`)





## Enum: TypeEnum


* `export` (value: `"export"`)




