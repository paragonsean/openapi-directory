# CarsMarketApiApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fareValue**](CarsMarketApiApi.md#fareValue) | **GET** /predict/car/uk/fmv | Predict fare value of car for UK based on YMMT &amp; miles |
| [**getDailyStats**](CarsMarketApiApi.md#getDailyStats) | **GET** /stats/car | Price, Miles and Days on Market stats |
| [**getMDS**](CarsMarketApiApi.md#getMDS) | **GET** /mds/car | Market Days Supply |
| [**getPopularCars**](CarsMarketApiApi.md#getPopularCars) | **GET** /popular/cars | Get make model wise top 50 popular cars on national, state, city level |
| [**getSalesCount**](CarsMarketApiApi.md#getSalesCount) | **GET** /sales/car | Get sales count by make, model, year, trim or taxonomy vin |
| [**predictCarPrice**](CarsMarketApiApi.md#predictCarPrice) | **GET** /predict/car/price | Predict car price based on it&#39;s specifications |
| [**predictUkCarPrice**](CarsMarketApiApi.md#predictUkCarPrice) | **GET** /predict/car/uk/price | Predict car price for UK based on it&#39;s specifications |


<a id="fareValue"></a>
# **fareValue**
> FareValue fareValue(apiKey, vrm, year, make, model, variant, miles, postalCode, radius)

Predict fare value of car for UK based on YMMT &amp; miles

Predict fare value of car for UK based on YMMT &amp; miles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarsMarketApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarsMarketApiApi apiInstance = new CarsMarketApiApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String vrm = "vrm_example"; // String | Predict price for a VRM
    Integer year = 56; // Integer | Car manufacturing year
    String make = "make_example"; // String | Car's make
    String model = "model_example"; // String | Car's model
    String variant = "variant_example"; // String | Car's variant
    Integer miles = 56; // Integer | miles vehicle has driven in total
    String postalCode = "postalCode_example"; // String | Postal code of the car
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    try {
      FareValue result = apiInstance.fareValue(apiKey, vrm, year, make, model, variant, miles, postalCode, radius);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarsMarketApiApi#fareValue");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **vrm** | **String**| Predict price for a VRM | [optional] |
| **year** | **Integer**| Car manufacturing year | [optional] |
| **make** | **String**| Car&#39;s make | [optional] |
| **model** | **String**| Car&#39;s model | [optional] |
| **variant** | **String**| Car&#39;s variant | [optional] |
| **miles** | **Integer**| miles vehicle has driven in total | [optional] |
| **postalCode** | **String**| Postal code of the car | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |

### Return type

[**FareValue**](FareValue.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Predict fare value of car for UK based on YMMT &amp; miles |  -  |
| **0** | Error |  -  |

<a id="getDailyStats"></a>
# **getDailyStats**
> DailyStats getDailyStats(apiKey, country, carType, ymm, ymmt, taxonomyVin, vin, state, cityState)

Price, Miles and Days on Market stats

National, state and city level stats for price, miles and dom

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarsMarketApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarsMarketApiApi apiInstance = new CarsMarketApiApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String country = "us"; // String | Country for which the stats are to be searched
    String carType = "new"; // String | Inventory type for which stats are to be searched, default is used
    String ymm = "ymm_example"; // String | Year, Make, Model of the car, Separated by pipe e.g. ymm=2015|ford|f-150
    String ymmt = "ymmt_example"; // String | Year, Make, Model, Trim of the car, Separated by pipe e.g. ymmt=2015|ford|f-150|platinum
    String taxonomyVin = "taxonomyVin_example"; // String | Taxonomy vin for referance to find stats of similar cars
    String vin = "vin_example"; // String | VIN that will be transformed to taxonomy_vin
    String state = "state_example"; // String | State level stats
    String cityState = "cityState_example"; // String | City level stats, pipe seperated like city_state=jacksonville|FL
    try {
      DailyStats result = apiInstance.getDailyStats(apiKey, country, carType, ymm, ymmt, taxonomyVin, vin, state, cityState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarsMarketApiApi#getDailyStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **country** | **String**| Country for which the stats are to be searched | [optional] [default to us] [enum: us, ca] |
| **carType** | **String**| Inventory type for which stats are to be searched, default is used | [optional] [default to used] [enum: new, used] |
| **ymm** | **String**| Year, Make, Model of the car, Separated by pipe e.g. ymm&#x3D;2015|ford|f-150 | [optional] |
| **ymmt** | **String**| Year, Make, Model, Trim of the car, Separated by pipe e.g. ymmt&#x3D;2015|ford|f-150|platinum | [optional] |
| **taxonomyVin** | **String**| Taxonomy vin for referance to find stats of similar cars | [optional] |
| **vin** | **String**| VIN that will be transformed to taxonomy_vin | [optional] |
| **state** | **String**| State level stats | [optional] |
| **cityState** | **String**| City level stats, pipe seperated like city_state&#x3D;jacksonville|FL | [optional] |

### Return type

[**DailyStats**](DailyStats.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data with Market averages and stats |  -  |
| **0** | Error |  -  |

<a id="getMDS"></a>
# **getMDS**
> Mds getMDS(apiKey, vin, exact, latitude, longitude, radius, zip, msaCode, debug, includeSold, country, state, city, ymmt, carType, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carfax1Owner, carfaxCleanTitle, year, make, model, trim, dealerId, source, bodyType, bodySubtype, vehicleType, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, dealershipGroupName, domActiveRange, dom180Range, fuelType, dealerType, engineSizeRange)

Market Days Supply

Get the basic information on specifications for a car identified by a valid VIN

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarsMarketApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarsMarketApiApi apiInstance = new CarsMarketApiApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String vin = "vin_example"; // String | VIN to decode
    Boolean exact = false; // Boolean | Exact parameter
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    String msaCode = "msaCode_example"; // String | To filter listing on msa code in which they are listed
    Boolean debug = false; // Boolean | Debug parameter
    Boolean includeSold = false; // Boolean | To fetch sold vins
    String country = "US"; // String | To filter listing on Country in which they are listed
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String ymmt = "ymmt_example"; // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
    String carType = "new"; // String | Car type. Allowed values are - new / used / certified
    String leaseTerm = "leaseTerm_example"; // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
    String leaseDownPayment = "leaseDownPayment_example"; // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
    String leaseEmp = "leaseEmp_example"; // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
    String financeLoanTerm = "financeLoanTerm_example"; // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
    String financeLoanApr = "financeLoanApr_example"; // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
    String financeEmp = "financeEmp_example"; // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
    String financeDownPayment = "financeDownPayment_example"; // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
    String financeDownPaymentPer = "financeDownPaymentPer_example"; // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
    String carfax1Owner = "true"; // String | Indicates whether car has had only one owner or not
    String carfaxCleanTitle = "true"; // String | Indicates whether car has clean ownership records
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String trim = "trim_example"; // String | To filter listing on their trim
    String dealerId = "dealerId_example"; // String | Dealer id to filter the listings.
    String source = "source_example"; // String | To filter listing on their source
    String bodyType = "bodyType_example"; // String | To filter listing on their body type
    String bodySubtype = "bodySubtype_example"; // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    String vehicleType = "vehicleType_example"; // String | To filter listing on their vehicle type
    String cylinders = "cylinders_example"; // String | To filter listing on their cylinders
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    String doors = "doors_example"; // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    String drivetrain = "drivetrain_example"; // String | To filter listing on their drivetrain
    String exteriorColor = "exteriorColor_example"; // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    String interiorColor = "interiorColor_example"; // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    String baseExteriorColor = "baseExteriorColor_example"; // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    String baseInteriorColor = "baseInteriorColor_example"; // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    String engine = "engine_example"; // String | To filter listing on their engine
    String engineSize = "engineSize_example"; // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    String engineAspiration = "engineAspiration_example"; // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    String engineBlock = "engineBlock_example"; // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    String highwayMpgRange = "highwayMpgRange_example"; // String | Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String cityMpgRange = "cityMpgRange_example"; // String | City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String milesRange = "milesRange_example"; // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    String priceRange = "priceRange_example"; // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String msrpRange = "msrpRange_example"; // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String domRange = "domRange_example"; // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String dealershipGroupName = "dealershipGroupName_example"; // String | Name of the dealership group to search for
    String domActiveRange = "domActiveRange_example"; // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String dom180Range = "dom180Range_example"; // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String dealerType = "franchise"; // String | Filter based on dealer type independant or franchise
    String engineSizeRange = "engineSizeRange_example"; // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    try {
      Mds result = apiInstance.getMDS(apiKey, vin, exact, latitude, longitude, radius, zip, msaCode, debug, includeSold, country, state, city, ymmt, carType, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carfax1Owner, carfaxCleanTitle, year, make, model, trim, dealerId, source, bodyType, bodySubtype, vehicleType, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, dealershipGroupName, domActiveRange, dom180Range, fuelType, dealerType, engineSizeRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarsMarketApiApi#getMDS");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **vin** | **String**| VIN to decode | [optional] |
| **exact** | **Boolean**| Exact parameter | [optional] [default to false] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] |
| **debug** | **Boolean**| Debug parameter | [optional] [default to false] |
| **includeSold** | **Boolean**| To fetch sold vins | [optional] [default to false] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to US] [enum: US, CA, us, ca] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] |
| **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] [enum: new, used, certified] |
| **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] |
| **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] |
| **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] |
| **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] |
| **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] |
| **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] |
| **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] |
| **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] |
| **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] [enum: true, false] |
| **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] [enum: true, false] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
| **dealerId** | **String**| Dealer id to filter the listings. | [optional] |
| **source** | **String**| To filter listing on their source | [optional] |
| **bodyType** | **String**| To filter listing on their body type | [optional] |
| **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] |
| **vehicleType** | **String**| To filter listing on their vehicle type | [optional] |
| **cylinders** | **String**| To filter listing on their cylinders | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |
| **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] |
| **drivetrain** | **String**| To filter listing on their drivetrain | [optional] |
| **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] |
| **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] |
| **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **engine** | **String**| To filter listing on their engine | [optional] |
| **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] |
| **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] |
| **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] |
| **highwayMpgRange** | **String**| Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **cityMpgRange** | **String**| City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **dealershipGroupName** | **String**| Name of the dealership group to search for | [optional] |
| **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] [enum: franchise, independent] |
| **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] |

### Return type

[**Mds**](Mds.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Provides Market Days supply for year make model or trim combination |  -  |
| **0** | Error |  -  |

<a id="getPopularCars"></a>
# **getPopularCars**
> PopularCars getPopularCars(carType, apiKey, state, cityState, country)

Get make model wise top 50 popular cars on national, state, city level

Get make model wise top 50 popular cars on national, state, city level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarsMarketApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarsMarketApiApi apiInstance = new CarsMarketApiApi(defaultClient);
    String carType = "new"; // String | Inventory type for which popular count is to be searched
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String state = "state_example"; // String | State level sales count
    String cityState = "cityState_example"; // String | City level sales count, pipe seperated like city_state=jacksonville|FL
    String country = "us"; // String | Country for which the popular cars are to be searched
    try {
      PopularCars result = apiInstance.getPopularCars(carType, apiKey, state, cityState, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarsMarketApiApi#getPopularCars");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **carType** | **String**| Inventory type for which popular count is to be searched | [enum: new, used] |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **state** | **String**| State level sales count | [optional] |
| **cityState** | **String**| City level sales count, pipe seperated like city_state&#x3D;jacksonville|FL | [optional] |
| **country** | **String**| Country for which the popular cars are to be searched | [optional] [default to us] [enum: us, ca, US, CA] |

### Return type

[**PopularCars**](PopularCars.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of most popular top 50 cars |  -  |
| **0** | Error |  -  |

<a id="getSalesCount"></a>
# **getSalesCount**
> Sales getSalesCount(apiKey, carType, make, mm, ymm, ymmt, taxonomyVin, state, cityState, vin, country)

Get sales count by make, model, year, trim or taxonomy vin

Get a sales count for city, state or national level by make, model, year, trim or taxonomy vin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarsMarketApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarsMarketApiApi apiInstance = new CarsMarketApiApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String carType = "new"; // String | Inventory type for which sales count is to be searched, default is used
    String make = "make_example"; // String | Make for which sales count is to be searched
    String mm = "mm_example"; // String | Make-Model for which sales count is to be searched, pipe seperated like mm=ford|f-150
    String ymm = "ymm_example"; // String | Year-Make-Model for which sales count is to be searched, pipe seperated like ymm=2015|ford|f-150
    String ymmt = "ymmt_example"; // String | Year-Make-Model-Trim for which sales count is to be searched, pipe seperated like ymmt=2015|ford|f-150|platinum
    String taxonomyVin = "taxonomyVin_example"; // String | taxonomy_vin for which sales count is to be searched
    String state = "state_example"; // String | State level sales count
    String cityState = "cityState_example"; // String | City level sales count, pipe seperated like city_state=jacksonville|FL
    String vin = "vin_example"; // String | VIN that will be transformed to taxonomy_vin
    String country = "us"; // String | Country for which the sales records are to be searched
    try {
      Sales result = apiInstance.getSalesCount(apiKey, carType, make, mm, ymm, ymmt, taxonomyVin, state, cityState, vin, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarsMarketApiApi#getSalesCount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **carType** | **String**| Inventory type for which sales count is to be searched, default is used | [optional] [default to used] [enum: new, used] |
| **make** | **String**| Make for which sales count is to be searched | [optional] |
| **mm** | **String**| Make-Model for which sales count is to be searched, pipe seperated like mm&#x3D;ford|f-150 | [optional] |
| **ymm** | **String**| Year-Make-Model for which sales count is to be searched, pipe seperated like ymm&#x3D;2015|ford|f-150 | [optional] |
| **ymmt** | **String**| Year-Make-Model-Trim for which sales count is to be searched, pipe seperated like ymmt&#x3D;2015|ford|f-150|platinum | [optional] |
| **taxonomyVin** | **String**| taxonomy_vin for which sales count is to be searched | [optional] |
| **state** | **String**| State level sales count | [optional] |
| **cityState** | **String**| City level sales count, pipe seperated like city_state&#x3D;jacksonville|FL | [optional] |
| **vin** | **String**| VIN that will be transformed to taxonomy_vin | [optional] |
| **country** | **String**| Country for which the sales records are to be searched | [optional] [default to us] [enum: us, ca, US, CA] |

### Return type

[**Sales**](Sales.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sales count for given parameters |  -  |
| **0** | Error |  -  |

<a id="predictCarPrice"></a>
# **predictCarPrice**
> PricePrediction predictCarPrice(carType, apiKey, vin, year, make, model, trim, isCertified, carfax1Owner, carfaxCleanTitle, baseExteriorColor, baseInteriorColor, transmission, drivetrain, engineSize, engineBlock, cylinders, doors, highwayMpg, cityMpg, latitude, longitude, miles, zip, country)

Predict car price based on it&#39;s specifications

Predict car price based on it&#39;s specifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarsMarketApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarsMarketApiApi apiInstance = new CarsMarketApiApi(defaultClient);
    String carType = "used"; // String | Car condition
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String vin = "vin_example"; // String | Predict price for a VIN
    Integer year = 56; // Integer | Car manufacturing year
    String make = "make_example"; // String | Car's make
    String model = "model_example"; // String | Car's model
    String trim = "trim_example"; // String | Car's trim
    Boolean isCertified = true; // Boolean | Boolean to indicate car is certified or not
    Boolean carfax1Owner = true; // Boolean | Boolean to indicate car is carfax one owner or not
    Boolean carfaxCleanTitle = true; // Boolean | Boolean to indicate car has clean title or not
    String baseExteriorColor = "baseExteriorColor_example"; // String | Base exterior color of the car
    String baseInteriorColor = "baseInteriorColor_example"; // String | Base interior color of the car
    String transmission = "Manual"; // String | Transmission on the car
    String drivetrain = "4WD"; // String | Drivetrain on the car
    BigDecimal engineSize = new BigDecimal(78); // BigDecimal | Engine Size of the car
    String engineBlock = "I"; // String | Engine Block of the car
    Integer cylinders = 56; // Integer | Number of cylinders in the vehicle
    Integer doors = 56; // Integer | Number of doors in the vehicle
    Integer highwayMpg = 56; // Integer | Highway mileage
    Integer cityMpg = 56; // Integer | City mileage of the car
    BigDecimal latitude = new BigDecimal(78); // BigDecimal | Latitude component of the location
    BigDecimal longitude = new BigDecimal(78); // BigDecimal | Longitude component of the location
    Integer miles = 56; // Integer | miles vehicle has driven in total
    String zip = "zip_example"; // String | Location zip
    String country = "us"; // String | Country for which car price will be predicted
    try {
      PricePrediction result = apiInstance.predictCarPrice(carType, apiKey, vin, year, make, model, trim, isCertified, carfax1Owner, carfaxCleanTitle, baseExteriorColor, baseInteriorColor, transmission, drivetrain, engineSize, engineBlock, cylinders, doors, highwayMpg, cityMpg, latitude, longitude, miles, zip, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarsMarketApiApi#predictCarPrice");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **carType** | **String**| Car condition | [enum: used, new] |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **vin** | **String**| Predict price for a VIN | [optional] |
| **year** | **Integer**| Car manufacturing year | [optional] |
| **make** | **String**| Car&#39;s make | [optional] |
| **model** | **String**| Car&#39;s model | [optional] |
| **trim** | **String**| Car&#39;s trim | [optional] |
| **isCertified** | **Boolean**| Boolean to indicate car is certified or not | [optional] |
| **carfax1Owner** | **Boolean**| Boolean to indicate car is carfax one owner or not | [optional] |
| **carfaxCleanTitle** | **Boolean**| Boolean to indicate car has clean title or not | [optional] |
| **baseExteriorColor** | **String**| Base exterior color of the car | [optional] |
| **baseInteriorColor** | **String**| Base interior color of the car | [optional] |
| **transmission** | **String**| Transmission on the car | [optional] [enum: Manual, Automatic] |
| **drivetrain** | **String**| Drivetrain on the car | [optional] [enum: 4WD, AWD, FWD, RWD] |
| **engineSize** | **BigDecimal**| Engine Size of the car | [optional] |
| **engineBlock** | **String**| Engine Block of the car | [optional] [enum: I, V, H] |
| **cylinders** | **Integer**| Number of cylinders in the vehicle | [optional] |
| **doors** | **Integer**| Number of doors in the vehicle | [optional] |
| **highwayMpg** | **Integer**| Highway mileage | [optional] |
| **cityMpg** | **Integer**| City mileage of the car | [optional] |
| **latitude** | **BigDecimal**| Latitude component of the location | [optional] |
| **longitude** | **BigDecimal**| Longitude component of the location | [optional] |
| **miles** | **Integer**| miles vehicle has driven in total | [optional] |
| **zip** | **String**| Location zip | [optional] |
| **country** | **String**| Country for which car price will be predicted | [optional] [default to us] [enum: us, ca] |

### Return type

[**PricePrediction**](PricePrediction.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Predicted price of the car along with it&#39;s specifications |  -  |
| **0** | Error |  -  |

<a id="predictUkCarPrice"></a>
# **predictUkCarPrice**
> PricePrediction predictUkCarPrice(apiKey, vrm, year, make, model, trim, baseExteriorColor, transmission, drivetrain, engineSize, cylinders, doors, fuelType, highwayMpg, cityMpg, combinedMpg, latitude, longitude, miles, zip)

Predict car price for UK based on it&#39;s specifications

Predict car price for UK based on it&#39;s specifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarsMarketApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarsMarketApiApi apiInstance = new CarsMarketApiApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String vrm = "vrm_example"; // String | Predict price for a VRM
    Integer year = 56; // Integer | Car manufacturing year
    String make = "make_example"; // String | Car's make
    String model = "model_example"; // String | Car's model
    String trim = "trim_example"; // String | Car's trim
    String baseExteriorColor = "baseExteriorColor_example"; // String | Base exterior color of the car
    String transmission = "Manual"; // String | Transmission on the car
    String drivetrain = "drivetrain_example"; // String | Drivetrain on the car
    Double engineSize = 3.4D; // Double | Engine Size of the car
    Integer cylinders = 56; // Integer | Number of cylinders in the vehicle
    Integer doors = 56; // Integer | Number of doors in the vehicle
    String fuelType = "fuelType_example"; // String | Fuel type of the car
    Double highwayMpg = 3.4D; // Double | Highway mileage
    Double cityMpg = 3.4D; // Double | City mileage of the car
    Double combinedMpg = 3.4D; // Double | Combiined mileage of the car
    BigDecimal latitude = new BigDecimal(78); // BigDecimal | Latitude component of the location
    BigDecimal longitude = new BigDecimal(78); // BigDecimal | Longitude component of the location
    Integer miles = 56; // Integer | miles vehicle has driven in total
    String zip = "zip_example"; // String | Location zip
    try {
      PricePrediction result = apiInstance.predictUkCarPrice(apiKey, vrm, year, make, model, trim, baseExteriorColor, transmission, drivetrain, engineSize, cylinders, doors, fuelType, highwayMpg, cityMpg, combinedMpg, latitude, longitude, miles, zip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarsMarketApiApi#predictUkCarPrice");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **vrm** | **String**| Predict price for a VRM | [optional] |
| **year** | **Integer**| Car manufacturing year | [optional] |
| **make** | **String**| Car&#39;s make | [optional] |
| **model** | **String**| Car&#39;s model | [optional] |
| **trim** | **String**| Car&#39;s trim | [optional] |
| **baseExteriorColor** | **String**| Base exterior color of the car | [optional] |
| **transmission** | **String**| Transmission on the car | [optional] [enum: Manual, Automatic] |
| **drivetrain** | **String**| Drivetrain on the car | [optional] |
| **engineSize** | **Double**| Engine Size of the car | [optional] |
| **cylinders** | **Integer**| Number of cylinders in the vehicle | [optional] |
| **doors** | **Integer**| Number of doors in the vehicle | [optional] |
| **fuelType** | **String**| Fuel type of the car | [optional] |
| **highwayMpg** | **Double**| Highway mileage | [optional] |
| **cityMpg** | **Double**| City mileage of the car | [optional] |
| **combinedMpg** | **Double**| Combiined mileage of the car | [optional] |
| **latitude** | **BigDecimal**| Latitude component of the location | [optional] |
| **longitude** | **BigDecimal**| Longitude component of the location | [optional] |
| **miles** | **Integer**| miles vehicle has driven in total | [optional] |
| **zip** | **String**| Location zip | [optional] |

### Return type

[**PricePrediction**](PricePrediction.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Predicted price of the car along with it&#39;s specifications |  -  |
| **0** | Error |  -  |

