# CloudTalentSolutionApi.JobQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commuteFilter** | [**CommuteFilter**](CommuteFilter.md) |  | [optional] 
**companyDisplayNames** | **[String]** | Optional. This filter specifies the company Company.display_name of the jobs to search against. The company name must match the value exactly. Alternatively, the value being searched for can be wrapped in different match operators. &#x60;SUBSTRING_MATCH([value])&#x60; The company name must contain a case insensitive substring match of the value. Using this function may increase latency. Sample Value: &#x60;SUBSTRING_MATCH(google)&#x60; &#x60;MULTI_WORD_TOKEN_MATCH([value])&#x60; The value will be treated as a multi word token and the company name must contain a case insensitive match of the value. Using this function may increase latency. Sample Value: &#x60;MULTI_WORD_TOKEN_MATCH(google)&#x60; If a value isn&#39;t specified, jobs within the search results are associated with any company. If multiple values are specified, jobs within the search results may be associated with any of the specified companies. At most 20 company display name filters are allowed. | [optional] 
**companyNames** | **[String]** | Optional. This filter specifies the company entities to search against. If a value isn&#39;t specified, jobs are searched for against all companies. If multiple values are specified, jobs are searched against the companies specified. The format is \&quot;projects/{project_id}/companies/{company_id}\&quot;, for example, \&quot;projects/api-test-project/companies/foo\&quot;. At most 20 company filters are allowed. | [optional] 
**compensationFilter** | [**CompensationFilter**](CompensationFilter.md) |  | [optional] 
**customAttributeFilter** | **String** | Optional. This filter specifies a structured syntax to match against the Job.custom_attributes marked as &#x60;filterable&#x60;. The syntax for this expression is a subset of SQL syntax. Supported operators are: &#x60;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x60;, and &#x60;&gt;&#x3D;&#x60; where the left of the operator is a custom field key and the right of the operator is a number or a quoted string. You must escape backslash (\\\\) and quote (\\\&quot;) characters. Supported functions are &#x60;LOWER([field_name])&#x60; to perform a case insensitive match and &#x60;EMPTY([field_name])&#x60; to filter on the existence of a key. Boolean expressions (AND/OR/NOT) are supported up to 3 levels of nesting (for example, \&quot;((A AND B AND C) OR NOT D) AND E\&quot;), a maximum of 100 comparisons or functions are allowed in the expression. The expression must be &lt; 10000 bytes in length. Sample Query: &#x60;(LOWER(driving_license)&#x3D;\&quot;class \\\&quot;a\\\&quot;\&quot; OR EMPTY(driving_license)) AND driving_years &gt; 10&#x60; | [optional] 
**disableSpellCheck** | **Boolean** | Optional. This flag controls the spell-check feature. If false, the service attempts to correct a misspelled query, for example, \&quot;enginee\&quot; is corrected to \&quot;engineer\&quot;. Defaults to false: a spell check is performed. | [optional] 
**employmentTypes** | **[String]** | Optional. The employment type filter specifies the employment type of jobs to search against, such as EmploymentType.FULL_TIME. If a value is not specified, jobs in the search results includes any employment type. If multiple values are specified, jobs in the search results include any of the specified employment types. | [optional] 
**jobCategories** | **[String]** | Optional. The category filter specifies the categories of jobs to search against. See Category for more information. If a value is not specified, jobs from any category are searched against. If multiple values are specified, jobs from any of the specified categories are searched against. | [optional] 
**languageCodes** | **[String]** | Optional. This filter specifies the locale of jobs to search against, for example, \&quot;en-US\&quot;. If a value isn&#39;t specified, the search results can contain jobs in any locale. Language codes should be in BCP-47 format, such as \&quot;en-US\&quot; or \&quot;sr-Latn\&quot;. For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47). At most 10 language code filters are allowed. | [optional] 
**locationFilters** | [**[LocationFilter]**](LocationFilter.md) | Optional. The location filter specifies geo-regions containing the jobs to search against. See LocationFilter for more information. If a location value isn&#39;t specified, jobs fitting the other search criteria are retrieved regardless of where they&#39;re located. If multiple values are specified, jobs are retrieved from any of the specified locations. If different values are specified for the LocationFilter.distance_in_miles parameter, the maximum provided distance is used for all locations. At most 5 location filters are allowed. | [optional] 
**publishTimeRange** | [**TimestampRange**](TimestampRange.md) |  | [optional] 
**query** | **String** | Optional. The query string that matches against the job title, description, and location fields. The maximum number of allowed characters is 255. | [optional] 
**queryLanguageCode** | **String** | The language code of query. For example, \&quot;en-US\&quot;. This field helps to better interpret the query. If a value isn&#39;t specified, the query language code is automatically detected, which may not be accurate. Language code should be in BCP-47 format, such as \&quot;en-US\&quot; or \&quot;sr-Latn\&quot;. For more information, see [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47). | [optional] 



## Enum: [EmploymentTypesEnum]


* `EMPLOYMENT_TYPE_UNSPECIFIED` (value: `"EMPLOYMENT_TYPE_UNSPECIFIED"`)

* `FULL_TIME` (value: `"FULL_TIME"`)

* `PART_TIME` (value: `"PART_TIME"`)

* `CONTRACTOR` (value: `"CONTRACTOR"`)

* `CONTRACT_TO_HIRE` (value: `"CONTRACT_TO_HIRE"`)

* `TEMPORARY` (value: `"TEMPORARY"`)

* `INTERN` (value: `"INTERN"`)

* `VOLUNTEER` (value: `"VOLUNTEER"`)

* `PER_DIEM` (value: `"PER_DIEM"`)

* `FLY_IN_FLY_OUT` (value: `"FLY_IN_FLY_OUT"`)

* `OTHER_EMPLOYMENT_TYPE` (value: `"OTHER_EMPLOYMENT_TYPE"`)





## Enum: [JobCategoriesEnum]


* `JOB_CATEGORY_UNSPECIFIED` (value: `"JOB_CATEGORY_UNSPECIFIED"`)

* `ACCOUNTING_AND_FINANCE` (value: `"ACCOUNTING_AND_FINANCE"`)

* `ADMINISTRATIVE_AND_OFFICE` (value: `"ADMINISTRATIVE_AND_OFFICE"`)

* `ADVERTISING_AND_MARKETING` (value: `"ADVERTISING_AND_MARKETING"`)

* `ANIMAL_CARE` (value: `"ANIMAL_CARE"`)

* `ART_FASHION_AND_DESIGN` (value: `"ART_FASHION_AND_DESIGN"`)

* `BUSINESS_OPERATIONS` (value: `"BUSINESS_OPERATIONS"`)

* `CLEANING_AND_FACILITIES` (value: `"CLEANING_AND_FACILITIES"`)

* `COMPUTER_AND_IT` (value: `"COMPUTER_AND_IT"`)

* `CONSTRUCTION` (value: `"CONSTRUCTION"`)

* `CUSTOMER_SERVICE` (value: `"CUSTOMER_SERVICE"`)

* `EDUCATION` (value: `"EDUCATION"`)

* `ENTERTAINMENT_AND_TRAVEL` (value: `"ENTERTAINMENT_AND_TRAVEL"`)

* `FARMING_AND_OUTDOORS` (value: `"FARMING_AND_OUTDOORS"`)

* `HEALTHCARE` (value: `"HEALTHCARE"`)

* `HUMAN_RESOURCES` (value: `"HUMAN_RESOURCES"`)

* `INSTALLATION_MAINTENANCE_AND_REPAIR` (value: `"INSTALLATION_MAINTENANCE_AND_REPAIR"`)

* `LEGAL` (value: `"LEGAL"`)

* `MANAGEMENT` (value: `"MANAGEMENT"`)

* `MANUFACTURING_AND_WAREHOUSE` (value: `"MANUFACTURING_AND_WAREHOUSE"`)

* `MEDIA_COMMUNICATIONS_AND_WRITING` (value: `"MEDIA_COMMUNICATIONS_AND_WRITING"`)

* `OIL_GAS_AND_MINING` (value: `"OIL_GAS_AND_MINING"`)

* `PERSONAL_CARE_AND_SERVICES` (value: `"PERSONAL_CARE_AND_SERVICES"`)

* `PROTECTIVE_SERVICES` (value: `"PROTECTIVE_SERVICES"`)

* `REAL_ESTATE` (value: `"REAL_ESTATE"`)

* `RESTAURANT_AND_HOSPITALITY` (value: `"RESTAURANT_AND_HOSPITALITY"`)

* `SALES_AND_RETAIL` (value: `"SALES_AND_RETAIL"`)

* `SCIENCE_AND_ENGINEERING` (value: `"SCIENCE_AND_ENGINEERING"`)

* `SOCIAL_SERVICES_AND_NON_PROFIT` (value: `"SOCIAL_SERVICES_AND_NON_PROFIT"`)

* `SPORTS_FITNESS_AND_RECREATION` (value: `"SPORTS_FITNESS_AND_RECREATION"`)

* `TRANSPORTATION_AND_LOGISTICS` (value: `"TRANSPORTATION_AND_LOGISTICS"`)




