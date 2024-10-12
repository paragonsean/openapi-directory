# FeedApi.CreateInventoryTaskRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedType** | **String** | The feed type associated with the inventory task you are about to create. Use a &lt;strong&gt;feedType&lt;/strong&gt; that is available for your API. Presently, only one feed type is available:&lt;ul&gt;&lt;li&gt;&lt;code&gt;LMS_ACTIVE_INVENTORY_REPORT&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt;&lt;br/&gt;See &lt;a href&#x3D;\&quot;/api-docs/sell/static/feed/lms-feeds-quick-reference.html#merchant-data-reports-download-feed-types\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Report download feed types&lt;/a&gt; for more information. | [optional] 
**filterCriteria** | [**InventoryFilterCriteria**](InventoryFilterCriteria.md) |  | [optional] 
**schemaVersion** | **String** | The schemaVersion/version number of the file format (use the schema version of the API to which you are programming):&lt;ul&gt;&lt;li&gt;&lt;a href&#x3D;\&quot;/api-docs/sell/static/feed/lms-feeds-quick-reference.html#Version\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Version Details / Schema Version&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href&#x3D;\&quot;/api-docs/sell/static/feed/fx-feeds-quick-reference.html#schema\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Seller Hub feed schema version&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 


