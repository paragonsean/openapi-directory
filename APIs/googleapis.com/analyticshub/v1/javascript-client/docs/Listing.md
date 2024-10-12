# AnalyticsHubApi.Listing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigqueryDataset** | [**BigQueryDatasetSource**](BigQueryDatasetSource.md) |  | [optional] 
**categories** | **[String]** | Optional. Categories of the listing. Up to two categories are allowed. | [optional] 
**dataProvider** | [**DataProvider**](DataProvider.md) |  | [optional] 
**description** | **String** | Optional. Short description of the listing. The description must not contain Unicode non-characters and C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes. | [optional] 
**displayName** | **String** | Required. Human-readable display name of the listing. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&amp;) and can&#39;t start or end with spaces. Default value is an empty string. Max length: 63 bytes. | [optional] 
**documentation** | **String** | Optional. Documentation describing the listing. | [optional] 
**icon** | **Blob** | Optional. Base64 encoded image representing the listing. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the contents of the field are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire. | [optional] 
**name** | **String** | Output only. The resource name of the listing. e.g. &#x60;projects/myproject/locations/US/dataExchanges/123/listings/456&#x60; | [optional] [readonly] 
**primaryContact** | **String** | Optional. Email or URL of the primary point of contact of the listing. Max Length: 1000 bytes. | [optional] 
**publisher** | [**Publisher**](Publisher.md) |  | [optional] 
**requestAccess** | **String** | Optional. Email or URL of the request access of the listing. Subscribers can use this reference to request access. Max Length: 1000 bytes. | [optional] 
**restrictedExportConfig** | [**RestrictedExportConfig**](RestrictedExportConfig.md) |  | [optional] 
**state** | **String** | Output only. Current state of the listing. | [optional] [readonly] 



## Enum: [CategoriesEnum]


* `UNSPECIFIED` (value: `"CATEGORY_UNSPECIFIED"`)

* `OTHERS` (value: `"CATEGORY_OTHERS"`)

* `ADVERTISING_AND_MARKETING` (value: `"CATEGORY_ADVERTISING_AND_MARKETING"`)

* `COMMERCE` (value: `"CATEGORY_COMMERCE"`)

* `CLIMATE_AND_ENVIRONMENT` (value: `"CATEGORY_CLIMATE_AND_ENVIRONMENT"`)

* `DEMOGRAPHICS` (value: `"CATEGORY_DEMOGRAPHICS"`)

* `ECONOMICS` (value: `"CATEGORY_ECONOMICS"`)

* `EDUCATION` (value: `"CATEGORY_EDUCATION"`)

* `ENERGY` (value: `"CATEGORY_ENERGY"`)

* `FINANCIAL` (value: `"CATEGORY_FINANCIAL"`)

* `GAMING` (value: `"CATEGORY_GAMING"`)

* `GEOSPATIAL` (value: `"CATEGORY_GEOSPATIAL"`)

* `HEALTHCARE_AND_LIFE_SCIENCE` (value: `"CATEGORY_HEALTHCARE_AND_LIFE_SCIENCE"`)

* `MEDIA` (value: `"CATEGORY_MEDIA"`)

* `PUBLIC_SECTOR` (value: `"CATEGORY_PUBLIC_SECTOR"`)

* `RETAIL` (value: `"CATEGORY_RETAIL"`)

* `SPORTS` (value: `"CATEGORY_SPORTS"`)

* `SCIENCE_AND_RESEARCH` (value: `"CATEGORY_SCIENCE_AND_RESEARCH"`)

* `TRANSPORTATION_AND_LOGISTICS` (value: `"CATEGORY_TRANSPORTATION_AND_LOGISTICS"`)

* `TRAVEL_AND_TOURISM` (value: `"CATEGORY_TRAVEL_AND_TOURISM"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)




