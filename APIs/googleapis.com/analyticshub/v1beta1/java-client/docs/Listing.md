

# Listing

A listing is what gets published into a data exchange that a subscriber can subscribe to. It contains a reference to the data source along with descriptive information that will help subscribers find and subscribe the data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigqueryDataset** | [**BigQueryDatasetSource**](BigQueryDatasetSource.md) |  |  [optional] |
|**categories** | [**List&lt;CategoriesEnum&gt;**](#List&lt;CategoriesEnum&gt;) | Optional. Categories of the listing. Up to two categories are allowed. |  [optional] |
|**dataProvider** | [**DataProvider**](DataProvider.md) |  |  [optional] |
|**description** | **String** | Optional. Short description of the listing. The description must not contain Unicode non-characters and C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes. |  [optional] |
|**displayName** | **String** | Required. Human-readable display name of the listing. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&amp;) and can&#39;t start or end with spaces. Default value is an empty string. Max length: 63 bytes. |  [optional] |
|**documentation** | **String** | Optional. Documentation describing the listing. |  [optional] |
|**icon** | **byte[]** | Optional. Base64 encoded image representing the listing. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the contents of the field are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire. |  [optional] |
|**name** | **String** | Output only. The resource name of the listing. e.g. &#x60;projects/myproject/locations/US/dataExchanges/123/listings/456&#x60; |  [optional] [readonly] |
|**primaryContact** | **String** | Optional. Email or URL of the primary point of contact of the listing. Max Length: 1000 bytes. |  [optional] |
|**publisher** | [**Publisher**](Publisher.md) |  |  [optional] |
|**requestAccess** | **String** | Optional. Email or URL of the request access of the listing. Subscribers can use this reference to request access. Max Length: 1000 bytes. |  [optional] |
|**restrictedExportConfig** | [**RestrictedExportConfig**](RestrictedExportConfig.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Current state of the listing. |  [optional] [readonly] |



## Enum: List&lt;CategoriesEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CATEGORY_UNSPECIFIED&quot; |
| OTHERS | &quot;CATEGORY_OTHERS&quot; |
| ADVERTISING_AND_MARKETING | &quot;CATEGORY_ADVERTISING_AND_MARKETING&quot; |
| COMMERCE | &quot;CATEGORY_COMMERCE&quot; |
| CLIMATE_AND_ENVIRONMENT | &quot;CATEGORY_CLIMATE_AND_ENVIRONMENT&quot; |
| DEMOGRAPHICS | &quot;CATEGORY_DEMOGRAPHICS&quot; |
| ECONOMICS | &quot;CATEGORY_ECONOMICS&quot; |
| EDUCATION | &quot;CATEGORY_EDUCATION&quot; |
| ENERGY | &quot;CATEGORY_ENERGY&quot; |
| FINANCIAL | &quot;CATEGORY_FINANCIAL&quot; |
| GAMING | &quot;CATEGORY_GAMING&quot; |
| GEOSPATIAL | &quot;CATEGORY_GEOSPATIAL&quot; |
| HEALTHCARE_AND_LIFE_SCIENCE | &quot;CATEGORY_HEALTHCARE_AND_LIFE_SCIENCE&quot; |
| MEDIA | &quot;CATEGORY_MEDIA&quot; |
| PUBLIC_SECTOR | &quot;CATEGORY_PUBLIC_SECTOR&quot; |
| RETAIL | &quot;CATEGORY_RETAIL&quot; |
| SPORTS | &quot;CATEGORY_SPORTS&quot; |
| SCIENCE_AND_RESEARCH | &quot;CATEGORY_SCIENCE_AND_RESEARCH&quot; |
| TRANSPORTATION_AND_LOGISTICS | &quot;CATEGORY_TRANSPORTATION_AND_LOGISTICS&quot; |
| TRAVEL_AND_TOURISM | &quot;CATEGORY_TRAVEL_AND_TOURISM&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |



