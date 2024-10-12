# CloudSpannerApi.ListBackupsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups** | [**[Backup]**](Backup.md) | The list of matching backups. Backups returned are ordered by &#x60;create_time&#x60; in descending order, starting from the most recent &#x60;create_time&#x60;. | [optional] 
**nextPageToken** | **String** | &#x60;next_page_token&#x60; can be sent in a subsequent ListBackups call to fetch more of the matching backups. | [optional] 


