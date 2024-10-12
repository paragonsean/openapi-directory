

# ExportTemplate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asAttachment** | **Boolean** | Download file as attachment |  [optional] |
|**contentTypes** | **Set&lt;String&gt;** |  |  |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**fileExtension** | **String** | Extension to append to the rendered filename |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**mimeType** | **String** | Defaults to &lt;code&gt;text/plain&lt;/code&gt; |  [optional] |
|**name** | **String** |  |  |
|**templateCode** | **String** | Jinja2 template code. The list of objects being exported is passed as a context variable named &lt;code&gt;queryset&lt;/code&gt;. |  |
|**url** | **URI** |  |  [optional] [readonly] |



