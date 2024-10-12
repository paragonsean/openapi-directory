

# Database

Represents a database as well as an hourly status

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSets** | **List&lt;String&gt;** | List of data sets fed by the database. It can contain &#x60;&#x60;affiliations_and_insurances&#x60;&#x60;, &#x60;&#x60;alert_in:media&#x60;&#x60;, &#x60;&#x60;business_background&#x60;&#x60;, &#x60;&#x60;criminal_record&#x60;&#x60;, &#x60;&#x60;driving_licenses&#x60;&#x60;, &#x60;&#x60;international_background&#x60;&#x60;, &#x60;&#x60;legal_background&#x60;&#x60;, &#x60;&#x60;personal_identity&#x60;&#x60;, &#x60;&#x60;permiso_de_circulación_covid-19&#x60;&#x60;, &#x60;&#x60;professional_background&#x60;&#x60;, &#x60;&#x60;traffic_fines&#x60;&#x60;, &#x60;&#x60;vehicle_information&#x60;&#x60;, &#x60;&#x60;vehicle_permits&#x60;&#x60;, &#x60;&#x60;behaviour_and_reputation&#x60;&#x60;, or &#x60;&#x60;taxes_and_finances&#x60;&#x60; |  [optional] |
|**databaseId** | **String** | Database identifier |  [optional] |
|**databaseName** | **String** | Database name. Do not use this field to identify the database as it might change, use database_id instead |  [optional] |
|**hourlyStatus** | **List&lt;String&gt;** | An hourly list of the database statuses. The &#x60;&#x60;operational&#x60;&#x60; status means the database executions were at least 90% successful, &#x60;&#x60;degraded_performance&#x60;&#x60; means the database executions were from 50 to 90% successful, &#x60;&#x60;partial_outage&#x60;&#x60; means the database executions were from 10 to 50% sucessful, &#x60;&#x60;major_outage&#x60;&#x60; means the database executions were under 10% successful. &#x60;&#x60;under_maintenance&#x60;&#x60; means the database is temporarily out of service for maintenance, &#x60;&#x60;deprecated&#x60;&#x60; means the database is permanently out of service, &#x60;&#x60;undetermined&#x60;&#x60; means there was no enough data to assess the database status |  [optional] |



