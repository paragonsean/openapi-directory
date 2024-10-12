

# Export

Exports are batch summaries of your Increase data. You can make them from the API or dashboard. Since they can take a while, they are generated asynchronously. We send a webhook when they are ready. For more information, please read our [Exports documentation](https://increase.com/documentation/exports).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of the Export. We may add additional possible values for this enum over time; your application should be able to handle that gracefully. |  |
|**createdAt** | **OffsetDateTime** | The time the Export was created. |  |
|**fileDownloadUrl** | **String** | A URL at which the Export&#39;s file can be downloaded. This will be present when the Export&#39;s status transitions to &#x60;complete&#x60;. |  |
|**fileId** | **String** | The File containing the contents of the Export. This will be present when the Export&#39;s status transitions to &#x60;complete&#x60;. |  |
|**id** | **String** | The Export identifier. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the Export. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;export&#x60;. |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| TRANSACTION_CSV | &quot;transaction_csv&quot; |
| BALANCE_CSV | &quot;balance_csv&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| COMPLETE | &quot;complete&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EXPORT | &quot;export&quot; |



