# UnitConverterApi

All URIs are relative to *https://api.exoapi.dev*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**unitConverterGet**](UnitConverterApi.md#unitConverterGet) | **GET** /unit-converter |  |


<a id="unitConverterGet"></a>
# **unitConverterGet**
> UnitConverterGet200Response unitConverterGet(from, to, value)



Quickly convert between all different kinds of measurement units

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UnitConverterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exoapi.dev");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    UnitConverterApi apiInstance = new UnitConverterApi(defaultClient);
    String from = "m/s2"; // String | 
    String to = "m/s2"; // String | 
    BigDecimal value = new BigDecimal(78); // BigDecimal | 
    try {
      UnitConverterGet200Response result = apiInstance.unitConverterGet(from, to, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UnitConverterApi#unitConverterGet");
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
| **from** | **String**|  | [enum: m/s2, ', '', deg, gon, rad, rad/s, [acr_us], [sft_i], [sin_i], [smi_us], [syd_i], ar, cm2, har, km2, m2, mm2, AUD, BGN, BRL, CAD, CHF, CNY, CZK, DKK, EUR, GBP, HKD, HUF, IDR, ILS, INR, ISK, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PLN, RON, SEK, SGD, THB, TRY, USD, ZAR, F, C, S, A, V, Ohm, [Btu_IT], J, kW.h, MJ, kW.h/100km, m/J, W.h/km, N, %, bpm, Hz, rpm, [mi_i]/[gal_br], L/100km, m/m3, lx, H, [ft_i], [in_i], [mi_i], [nmi_i], [yd_i], cm, dm, km, m, mm, g/km, kg/m, lm, Wb, T, [lb_av], g, kg, t, [HP_e], [HP_m], [HP_s], [HP], kW, W, Pa, Bq, [kn_i], km/h, m/s, [degF], Cel, K, a, d, h, min, mo, s, wk, N.m, [gal_br], [pk_br], L, m3] |
| **to** | **String**|  | [enum: m/s2, ', '', deg, gon, rad, rad/s, [acr_us], [sft_i], [sin_i], [smi_us], [syd_i], ar, cm2, har, km2, m2, mm2, AUD, BGN, BRL, CAD, CHF, CNY, CZK, DKK, EUR, GBP, HKD, HUF, IDR, ILS, INR, ISK, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PLN, RON, SEK, SGD, THB, TRY, USD, ZAR, F, C, S, A, V, Ohm, [Btu_IT], J, kW.h, MJ, kW.h/100km, m/J, W.h/km, N, %, bpm, Hz, rpm, [mi_i]/[gal_br], L/100km, m/m3, lx, H, [ft_i], [in_i], [mi_i], [nmi_i], [yd_i], cm, dm, km, m, mm, g/km, kg/m, lm, Wb, T, [lb_av], g, kg, t, [HP_e], [HP_m], [HP_s], [HP], kW, W, Pa, Bq, [kn_i], km/h, m/s, [degF], Cel, K, a, d, h, min, mo, s, wk, N.m, [gal_br], [pk_br], L, m3] |
| **value** | **BigDecimal**|  | |

### Return type

[**UnitConverterGet200Response**](UnitConverterGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 🟢 200 OK |  -  |
| **400** | 🟡 400 Bad request |  -  |
| **401** | 🟡 401 Unauthorized |  -  |
| **429** | 🟡 429 Too many requests |  -  |
| **500** | 🔴 500 Internal server error |  -  |

