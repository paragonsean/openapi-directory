

# ListBackupsResponse

ListBackupsResponse is the result of ListBackupsRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backups** | [**List&lt;Backup&gt;**](Backup.md) | A list of backups in the project for the specified location. If the &#x60;{location}&#x60; value in the request is \&quot;-\&quot;, the response contains a list of backups from all locations. If any location is unreachable, the response will only return backups in reachable locations and the \&quot;unreachable\&quot; field will be populated with a list of unreachable locations. |  [optional] |
|**nextPageToken** | **String** | The token you can use to retrieve the next page of results. Not returned if there are no more results in the list. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



