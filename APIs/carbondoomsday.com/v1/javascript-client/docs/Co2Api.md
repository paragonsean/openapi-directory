# CarbonDoomsDay.Co2Api

All URIs are relative to *https://api.carbondoomsday.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**co2List**](Co2Api.md#co2List) | **GET** /co2/ | 
[**co2Read**](Co2Api.md#co2Read) | **GET** /co2/{date}/ | 



## co2List

> Co2List200Response co2List(opts)



CO2 measurements from the Mauna Loa observatory.  This data is made available through the good work of the people at the Mauna Loa observatory. Their release notes say:      These data are made freely available to the public and the scientific     community in the belief that their wide dissemination will lead to greater     understanding and new scientific insights.  We currently scrape the following sources:    * [co2_mlo_weekly.csv]   * [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]   * [weekly_mlo.csv]  We have daily CO2 measurements as far back as 1958.  Learn about using pagination via [the 3rd party documentation].  [co2_mlo_weekly.csv]: https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]: ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/mlo/co2_mlo_surface-insitu_1_ccgg_DailyData.txt [weekly_mlo.csv]: http://scrippsco2.ucsd.edu/sites/default/files/data/in_situ_co2/weekly_mlo.csv [the 3rd party documentation]: http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination

### Example

```javascript
import CarbonDoomsDay from 'carbon_dooms_day';
let defaultClient = CarbonDoomsDay.ApiClient.instance;
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new CarbonDoomsDay.Co2Api();
let opts = {
  'ppm': 3.4, // Number | 
  'date': "date_example", // String | 
  'dateRange': "dateRange_example", // String | Multiple values may be separated by commas.
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'page': 56, // Number | A page number within the paginated result set.
  'limit': 56 // Number | Number of results to return per page.
};
apiInstance.co2List(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ppm** | **Number**|  | [optional] 
 **date** | **String**|  | [optional] 
 **dateRange** | **String**| Multiple values may be separated by commas. | [optional] 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] 
 **page** | **Number**| A page number within the paginated result set. | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 

### Return type

[**Co2List200Response**](Co2List200Response.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## co2Read

> CO2 co2Read(date)



CO2 measurements from the Mauna Loa observatory.  This data is made available through the good work of the people at the Mauna Loa observatory. Their release notes say:      These data are made freely available to the public and the scientific     community in the belief that their wide dissemination will lead to greater     understanding and new scientific insights.  We currently scrape the following sources:    * [co2_mlo_weekly.csv]   * [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]   * [weekly_mlo.csv]  We have daily CO2 measurements as far back as 1958.  Learn about using pagination via [the 3rd party documentation].  [co2_mlo_weekly.csv]: https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv [co2_mlo_surface-insitu_1_ccgg_DailyData.txt]: ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/mlo/co2_mlo_surface-insitu_1_ccgg_DailyData.txt [weekly_mlo.csv]: http://scrippsco2.ucsd.edu/sites/default/files/data/in_situ_co2/weekly_mlo.csv [the 3rd party documentation]: http://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination

### Example

```javascript
import CarbonDoomsDay from 'carbon_dooms_day';
let defaultClient = CarbonDoomsDay.ApiClient.instance;
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new CarbonDoomsDay.Co2Api();
let date = new Date("2013-10-20"); // Date | 
apiInstance.co2Read(date, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **Date**|  | 

### Return type

[**CO2**](CO2.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

