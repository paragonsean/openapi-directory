

# Promotion

Promotions generally offer a set amount of credit that can be used toward your Linode services, and the promotion expires after a specified date. As well, a monthly cap on the promotional offer is set.  Simply put, a promotion offers a certain amount of credit every month, until either the expiration date is passed, or until the total promotional credit is used, whichever comes first. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creditMonthlyCap** | **String** | The amount available to spend per month.  |  [optional] |
|**creditRemaining** | **String** | The total amount of credit left for this promotion.  |  [optional] |
|**description** | **String** | A detailed description of this promotion.  |  [optional] |
|**expireDt** | **String** | When this promotion&#39;s credits expire.  |  [optional] |
|**imageUrl** | **String** | The location of an image for this promotion.  |  [optional] |
|**serviceType** | [**ServiceTypeEnum**](#ServiceTypeEnum) | The service to which this promotion applies.  |  [optional] |
|**summary** | **String** | Short details of this promotion.  |  [optional] |
|**thisMonthCreditRemaining** | **String** | The amount of credit left for this month for this promotion.  |  [optional] |



## Enum: ServiceTypeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| BACKUP | &quot;backup&quot; |
| BLOCKSTORAGE | &quot;blockstorage&quot; |
| DB_MYSQL | &quot;db_mysql&quot; |
| IP_V4 | &quot;ip_v4&quot; |
| LINODE | &quot;linode&quot; |
| LINODE_DISK | &quot;linode_disk&quot; |
| LINODE_MEMORY | &quot;linode_memory&quot; |
| LONGVIEW | &quot;longview&quot; |
| MANAGED | &quot;managed&quot; |
| NODEBALANCER | &quot;nodebalancer&quot; |
| OBJECTSTORAGE | &quot;objectstorage&quot; |
| TRANSFER_TX | &quot;transfer_tx&quot; |



