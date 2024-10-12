# CarboneApi.RenderTemplateIdPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complement** | **Object** | Optional - Object|Array, extra data accessible in the template with {c.} instead of {d.} | [optional] 
**convertTo** | **String** | Optional - Convert the document into another format. Accepted values: ods xlsx xls csv pdf txt odp ppt pptx jpg png odt doc docx txt jpg png epub html xml idml. List of supported formats: https://carbone.io/documentation.html#supported-files-and-features-list | [optional] 
**currencyRates** | **Object** | Optional - Currency exchange rates for conversions from &#x60;currencySource&#x60; to &#x60;currencyTarget&#x60;. Learn more: https://carbone.io/documentation.html#formatc-precisionorformat- | [optional] 
**currencySource** | **String** | Optional - Currency source coming from your JSON data. The option is used by &#x60;formatC&#x60; to convert the currency based on the &#x60;currencyTarget&#x60; and &#x60;currencyRates&#x60;. Learn more: https://carbone.io/documentation.html#formatc-precisionorformat- | [optional] 
**currencyTarget** | **String** | Optional - Target currency when the document is generated. The option is used by &#x60;formatC&#x60; to convert the currency based on the &#x60;currencySource&#x60; and &#x60;currencyRates&#x60;. Learn more: https://carbone.io/documentation.html#formatc-precisionorformat- | [optional] 
**data** | **Object** | Required - ️JSON data-set merged into the template to generate a document | 
**_enum** | **Object** | Optional - List of enumerations, use it in reports with &#x60;convEnum&#x60; formatters, documentation: https://carbone.io/documentation.html#convenum-type- | [optional] 
**hardRefresh** | **Boolean** | Optional - If true, the report content is refreshed at the end of the rendering process. To use this option, &#x60;convertTo&#x60; has to be defined. It is mostly used to refresh a table of content. | [optional] 
**lang** | **String** | Optional - Locale of the generated doocument, it will used for translation &#x60;{t()}&#x60;, formatting numbers with &#x60;:formatN&#x60;, and currencies &#x60;:formatC&#x60;. List of supported locales: https://github.com/carboneio/carbone/blob/master/formatters/_locale.js | [optional] 
**reportName** | **String** | Optional - Static or dynamic file name returned on the &#x60;content-disposition&#x60; header when the generated report is fetched with &#x60;GET /report/:renderI&#x60;. Multiple Carbone tags are accepted, such as &#x60;{d.type}-{d.date}.pdf&#x60; | [optional] 
**timezone** | **String** | Optional - Convert document dates to a timezone. The default timezone is &#x60;Europe/Paris&#x60;. The date must be chained with the &#x60;:formatD&#x60; formatter, for instance &#x60;{d.date:formatD(YYYY-MM-DD HH:MM)}&#x60;. List of accepted timezones (Column TZ identifier): https://en.wikipedia.org/wiki/List_of_tz_database_time_zones | [optional] 
**translations** | **Object** | Optional - When the report is generated, all text between &#x60;{t( )}&#x60; is replaced with the corresponding translation. The &#x60;lang&#x60; option is required to select the correct translation. Learn more: https://carbone.io/documentation.html#translations | [optional] 
**variableStr** | **String** | Optional - Predefine alias, related documenation: https://carbone.io/documentation.html#alias | [optional] 


