# TerraintilesApi

All URIs are relative to *https://vectortile.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vectortileTerraintilesGet**](TerraintilesApi.md#vectortileTerraintilesGet) | **GET** /v1/{name} |  |


<a id="vectortileTerraintilesGet"></a>
# **vectortileTerraintilesGet**
> TerrainTile vectortileTerraintilesGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, altitudePrecisionCentimeters, clientInfoApiClient, clientInfoApplicationId, clientInfoApplicationVersion, clientInfoDeviceModel, clientInfoOperatingSystem, clientInfoPlatform, clientInfoUserId, maxElevationResolutionCells, minElevationResolutionCells, terrainFormats, enableModeledVolumes, enablePoliticalFeatures, enablePrivateRoads, enableUnclippedBuildings, languageCode, regionCode)



Gets a terrain tile by its tile resource name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerraintilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vectortile.googleapis.com");

    TerraintilesApi apiInstance = new TerraintilesApi(defaultClient);
    String name = "name_example"; // String | Required. Resource name of the tile. The tile resource name is prefixed by its collection ID `terraintiles/` followed by the resource ID, which encodes the tile's global x and y coordinates and zoom level as `@,,z`. For example, `terraintiles/@1,2,3z`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer altitudePrecisionCentimeters = 56; // Integer | The precision of terrain altitudes in centimeters. Possible values: between 1 (cm level precision) and 1,000,000 (10-kilometer level precision).
    String clientInfoApiClient = "clientInfoApiClient_example"; // String | API client name and version. For example, the SDK calling the API. The exact format is up to the client.
    String clientInfoApplicationId = "clientInfoApplicationId_example"; // String | Application ID, such as the package name on Android and the bundle identifier on iOS platforms.
    String clientInfoApplicationVersion = "clientInfoApplicationVersion_example"; // String | Application version number, such as \"1.2.3\". The exact format is application-dependent.
    String clientInfoDeviceModel = "clientInfoDeviceModel_example"; // String | Device model as reported by the device. The exact format is platform-dependent.
    String clientInfoOperatingSystem = "clientInfoOperatingSystem_example"; // String | Operating system name and version as reported by the OS. For example, \"Mac OS X 10.10.4\". The exact format is platform-dependent.
    String clientInfoPlatform = "PLATFORM_UNSPECIFIED"; // String | Platform where the application is running.
    String clientInfoUserId = "clientInfoUserId_example"; // String | Required. A client-generated user ID. The ID should be generated and persisted during the first user session or whenever a pre-existing ID is not found. The exact format is up to the client. This must be non-empty in a GetFeatureTileRequest (whether via the header or GetFeatureTileRequest.client_info).
    Integer maxElevationResolutionCells = 56; // Integer | The maximum allowed resolution for the returned elevation heightmap. Possible values: between 1 and 1024 (and not less than min_elevation_resolution_cells). Over-sized heightmaps will be non-uniformly down-sampled such that each edge is no longer than this value. Non-uniformity is chosen to maximise the amount of preserved data. For example: Original resolution: 100px (width) * 30px (height) max_elevation_resolution: 30 New resolution: 30px (width) * 30px (height)
    Integer minElevationResolutionCells = 56; // Integer |  api-linter: core::0131::request-unknown-fields=disabled aip.dev/not-precedent: Maintaining existing request parameter pattern. The minimum allowed resolution for the returned elevation heightmap. Possible values: between 0 and 1024 (and not more than max_elevation_resolution_cells). Zero is supported for backward compatibility. Under-sized heightmaps will be non-uniformly up-sampled such that each edge is no shorter than this value. Non-uniformity is chosen to maximise the amount of preserved data. For example: Original resolution: 30px (width) * 10px (height) min_elevation_resolution: 30 New resolution: 30px (width) * 30px (height)
    List<String> terrainFormats = Arrays.asList(); // List<String> | Terrain formats that the client understands.
    Boolean enableModeledVolumes = true; // Boolean | Flag indicating whether 3D building models should be enabled. If this is set structures will be returned as 3D modeled volumes rather than 2.5D extruded areas where possible.
    Boolean enablePoliticalFeatures = true; // Boolean | Flag indicating whether political features should be returned.
    Boolean enablePrivateRoads = true; // Boolean | Flag indicating whether the returned tile will contain road features that are marked private. Private roads are indicated by the Feature.segment_info.road_info.is_private field.
    Boolean enableUnclippedBuildings = true; // Boolean | Flag indicating whether unclipped buildings should be returned. If this is set, building render ops will extend beyond the tile boundary. Buildings will only be returned on the tile that contains their centroid.
    String languageCode = "languageCode_example"; // String | Required. The BCP-47 language code corresponding to the language in which the name was requested, such as \"en-US\" or \"sr-Latn\". For more information, see http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
    String regionCode = "regionCode_example"; // String | Required. The Unicode country/region code (CLDR) of the location from which the request is coming from, such as \"US\" and \"419\". For more information, see http://www.unicode.org/reports/tr35/#unicode_region_subtag.
    try {
      TerrainTile result = apiInstance.vectortileTerraintilesGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, altitudePrecisionCentimeters, clientInfoApiClient, clientInfoApplicationId, clientInfoApplicationVersion, clientInfoDeviceModel, clientInfoOperatingSystem, clientInfoPlatform, clientInfoUserId, maxElevationResolutionCells, minElevationResolutionCells, terrainFormats, enableModeledVolumes, enablePoliticalFeatures, enablePrivateRoads, enableUnclippedBuildings, languageCode, regionCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerraintilesApi#vectortileTerraintilesGet");
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
| **name** | **String**| Required. Resource name of the tile. The tile resource name is prefixed by its collection ID &#x60;terraintiles/&#x60; followed by the resource ID, which encodes the tile&#39;s global x and y coordinates and zoom level as &#x60;@,,z&#x60;. For example, &#x60;terraintiles/@1,2,3z&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **altitudePrecisionCentimeters** | **Integer**| The precision of terrain altitudes in centimeters. Possible values: between 1 (cm level precision) and 1,000,000 (10-kilometer level precision). | [optional] |
| **clientInfoApiClient** | **String**| API client name and version. For example, the SDK calling the API. The exact format is up to the client. | [optional] |
| **clientInfoApplicationId** | **String**| Application ID, such as the package name on Android and the bundle identifier on iOS platforms. | [optional] |
| **clientInfoApplicationVersion** | **String**| Application version number, such as \&quot;1.2.3\&quot;. The exact format is application-dependent. | [optional] |
| **clientInfoDeviceModel** | **String**| Device model as reported by the device. The exact format is platform-dependent. | [optional] |
| **clientInfoOperatingSystem** | **String**| Operating system name and version as reported by the OS. For example, \&quot;Mac OS X 10.10.4\&quot;. The exact format is platform-dependent. | [optional] |
| **clientInfoPlatform** | **String**| Platform where the application is running. | [optional] [enum: PLATFORM_UNSPECIFIED, EDITOR, MAC_OS, WINDOWS, LINUX, ANDROID, IOS, WEB_GL] |
| **clientInfoUserId** | **String**| Required. A client-generated user ID. The ID should be generated and persisted during the first user session or whenever a pre-existing ID is not found. The exact format is up to the client. This must be non-empty in a GetFeatureTileRequest (whether via the header or GetFeatureTileRequest.client_info). | [optional] |
| **maxElevationResolutionCells** | **Integer**| The maximum allowed resolution for the returned elevation heightmap. Possible values: between 1 and 1024 (and not less than min_elevation_resolution_cells). Over-sized heightmaps will be non-uniformly down-sampled such that each edge is no longer than this value. Non-uniformity is chosen to maximise the amount of preserved data. For example: Original resolution: 100px (width) * 30px (height) max_elevation_resolution: 30 New resolution: 30px (width) * 30px (height) | [optional] |
| **minElevationResolutionCells** | **Integer**|  api-linter: core::0131::request-unknown-fields&#x3D;disabled aip.dev/not-precedent: Maintaining existing request parameter pattern. The minimum allowed resolution for the returned elevation heightmap. Possible values: between 0 and 1024 (and not more than max_elevation_resolution_cells). Zero is supported for backward compatibility. Under-sized heightmaps will be non-uniformly up-sampled such that each edge is no shorter than this value. Non-uniformity is chosen to maximise the amount of preserved data. For example: Original resolution: 30px (width) * 10px (height) min_elevation_resolution: 30 New resolution: 30px (width) * 30px (height) | [optional] |
| **terrainFormats** | [**List&lt;String&gt;**](String.md)| Terrain formats that the client understands. | [optional] [enum: TERRAIN_FORMAT_UNKNOWN, FIRST_DERIVATIVE, SECOND_DERIVATIVE] |
| **enableModeledVolumes** | **Boolean**| Flag indicating whether 3D building models should be enabled. If this is set structures will be returned as 3D modeled volumes rather than 2.5D extruded areas where possible. | [optional] |
| **enablePoliticalFeatures** | **Boolean**| Flag indicating whether political features should be returned. | [optional] |
| **enablePrivateRoads** | **Boolean**| Flag indicating whether the returned tile will contain road features that are marked private. Private roads are indicated by the Feature.segment_info.road_info.is_private field. | [optional] |
| **enableUnclippedBuildings** | **Boolean**| Flag indicating whether unclipped buildings should be returned. If this is set, building render ops will extend beyond the tile boundary. Buildings will only be returned on the tile that contains their centroid. | [optional] |
| **languageCode** | **String**| Required. The BCP-47 language code corresponding to the language in which the name was requested, such as \&quot;en-US\&quot; or \&quot;sr-Latn\&quot;. For more information, see http://www.unicode.org/reports/tr35/#Unicode_locale_identifier. | [optional] |
| **regionCode** | **String**| Required. The Unicode country/region code (CLDR) of the location from which the request is coming from, such as \&quot;US\&quot; and \&quot;419\&quot;. For more information, see http://www.unicode.org/reports/tr35/#unicode_region_subtag. | [optional] |

### Return type

[**TerrainTile**](TerrainTile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

