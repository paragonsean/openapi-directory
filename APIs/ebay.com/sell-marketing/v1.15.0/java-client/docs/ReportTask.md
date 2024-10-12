

# ReportTask

This type defines the fields in a report task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaignIds** | **List&lt;String&gt;** | A list of IDs for the campaigns that are included in the report. A campaign ID is a unique eBay-assigned identifier of the campaign that&#39;s generated when the campaign is created.&lt;br /&gt;&lt;br /&gt;Call &lt;b&gt;getCampaigns&lt;/b&gt; to return the current campaign IDs for a seller. |  [optional] |
|**dateFrom** | **String** | The date defining the start of the timespan covered by the report, formatted as an &lt;a href&#x3D;\&quot;https://www.iso.org/iso-8601-date-and-time-format.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 8601&lt;/a&gt; timestamp. |  [optional] |
|**dateTo** | **String** | The date defining the end of the timespan covered by the report, formatted as an &lt;a href&#x3D;\&quot;https://www.iso.org/iso-8601-date-and-time-format.html \&quot; title&#x3D;\&quot;https://www.iso.org \&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 8601&lt;/a&gt; timestamp. |  [optional] |
|**dimensions** | [**List&lt;Dimension&gt;**](Dimension.md) | A list containing the dimension in the report. |  [optional] |
|**fundingModels** | **List&lt;String&gt;** | The funding model for the campaign that shall be included in the report.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#004680\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt;&lt;/span&gt; The default funding model for Promoted Listings reports is &lt;code&gt;COST_PER_SALE&lt;/code&gt;.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Valid Values:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;&lt;code&gt;COST_PER_SALE&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;COST_PER_CLICK&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt; |  [optional] |
|**inventoryReferences** | [**List&lt;InventoryReference&gt;**](InventoryReference.md) | If supplied in the request, this field returns a list of the seller&#39;s inventory reference IDs included in the report.  &lt;p&gt;Each item is referenced by a pair of &lt;b&gt;inventoryRefernceID&lt;/b&gt; and &lt;b&gt;inventoryReferenceType&lt;/b&gt; values, where an inventory reference ID can be either a seller-defined &lt;b&gt;SKU&lt;/b&gt; value or an &lt;b&gt;inventoryItemGroupKey&lt;/b&gt;. An &lt;b&gt;inventoryItemGroupKey&lt;/b&gt; is seller-defined ID for an inventory item group (a multiple-variation listing), and is created and used by the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot;&gt;Inventory API&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**listingIds** | **List&lt;String&gt;** | If supplied in the request, this field returns a list of the listing IDs included in the report. A listing ID is an eBay-assigned ID that&#39;s generated when a listing is created. |  [optional] |
|**marketplaceId** | **String** | The ID of the eBay marketplace used by the report task. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/marketing/types/ba:MarketplaceIdEnum&#39;&gt;eBay API documentation&lt;/a&gt; |  [optional] |
|**metricKeys** | **List&lt;String&gt;** | A list of metrics for the report task. |  [optional] |
|**reportExpirationDate** | **String** | The date after which the report is no longer be available. Reports are available for 30 days and you cannot download a report after it has expired.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Format (UTC): &lt;/b&gt; yyyy-MM-ddThh:mm:ss.sssZ |  [optional] |
|**reportFormat** | **String** | Indicates the format of the report. Currently, only &lt;code&gt;TSV_GZIP&lt;/code&gt; is supported. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/marketing/types/plr:ReportFormatEnum&#39;&gt;eBay API documentation&lt;/a&gt; |  [optional] |
|**reportHref** | **String** | The URL of the generated report, which can be used to download the report once it has been generated. |  [optional] |
|**reportId** | **String** | A unique eBay-assigned ID for the report. |  [optional] |
|**reportName** | **String** | An eBay-assigned name for the report that&#39;s created by the &lt;b&gt;createReportTask&lt;/b&gt; call. This name is unique for the seller. |  [optional] |
|**reportTaskCompletionDate** | **String** | The date the report task completed the report generation.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Format (UTC): &lt;/b&gt; yyyy-MM-ddThh:mm:ss.sssZ |  [optional] |
|**reportTaskCreationDate** | **String** | The date the report task was created.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Format (UTC): &lt;/b&gt; yyyy-MM-ddThh:mm:ss.sssZ |  [optional] |
|**reportTaskExpectedCompletionDate** | **String** | The date the report task is expected to complete the report generation.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Format (UTC): &lt;/b&gt; yyyy-MM-ddThh:mm:ss.sssZ |  [optional] |
|**reportTaskId** | **String** | The unique eBay-assigned ID of the report task. This value is generated when the report task is created with a call to &lt;b&gt;createReportTask&lt;/b&gt;. |  [optional] |
|**reportTaskStatus** | **String** | Indicates the current state of the report task. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/marketing/types/plr:TaskStatusEnum&#39;&gt;eBay API documentation&lt;/a&gt; |  [optional] |
|**reportTaskStatusMessage** | **String** | A status message with additional information about the report task. |  [optional] |
|**reportType** | **String** | Indicates type of report associated with the report task.&lt;br/&gt;&lt;br/&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; INVENTORY_PERFORMANCE_REPORT is not currently available; availability date is pending.&lt;/span&gt; For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/marketing/types/plr:ReportTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; |  [optional] |



