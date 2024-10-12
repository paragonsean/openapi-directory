

# Export

Client request to export data from a user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) | Content type representing data being exported (e.g. application/vnd.climate.acrsi.geojson). |  |
|**definition** | **Object** | Additional specifications for a client&#39;s data export request, dependent on the content type. |  [optional] |



## Enum: ContentTypeEnum

| Name | Value |
|---- | -----|
| ACRSI_GEOJSON | &quot;application/vnd.climate.acrsi.geojson&quot; |
| HARVEST_GEOJSON | &quot;application/vnd.climate.harvest.geojson&quot; |



