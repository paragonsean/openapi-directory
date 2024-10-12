# SemanticTileApi.TerraintilesApi

All URIs are relative to *https://vectortile.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vectortileTerraintilesGet**](TerraintilesApi.md#vectortileTerraintilesGet) | **GET** /v1/{name} | 



## vectortileTerraintilesGet

> TerrainTile vectortileTerraintilesGet(name, opts)



Gets a terrain tile by its tile resource name.

### Example

```javascript
import SemanticTileApi from 'semantic_tile_api';

let apiInstance = new SemanticTileApi.TerraintilesApi();
let name = "name_example"; // String | Required. Resource name of the tile. The tile resource name is prefixed by its collection ID `terraintiles/` followed by the resource ID, which encodes the tile's global x and y coordinates and zoom level as `@,,z`. For example, `terraintiles/@1,2,3z`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'altitudePrecisionCentimeters': 56, // Number | The precision of terrain altitudes in centimeters. Possible values: between 1 (cm level precision) and 1,000,000 (10-kilometer level precision).
  'clientInfoApiClient': "clientInfoApiClient_example", // String | API client name and version. For example, the SDK calling the API. The exact format is up to the client.
  'clientInfoApplicationId': "clientInfoApplicationId_example", // String | Application ID, such as the package name on Android and the bundle identifier on iOS platforms.
  'clientInfoApplicationVersion': "clientInfoApplicationVersion_example", // String | Application version number, such as \"1.2.3\". The exact format is application-dependent.
  'clientInfoDeviceModel': "clientInfoDeviceModel_example", // String | Device model as reported by the device. The exact format is platform-dependent.
  'clientInfoOperatingSystem': "clientInfoOperatingSystem_example", // String | Operating system name and version as reported by the OS. For example, \"Mac OS X 10.10.4\". The exact format is platform-dependent.
  'clientInfoPlatform': "clientInfoPlatform_example", // String | Platform where the application is running.
  'clientInfoUserId': "clientInfoUserId_example", // String | Required. A client-generated user ID. The ID should be generated and persisted during the first user session or whenever a pre-existing ID is not found. The exact format is up to the client. This must be non-empty in a GetFeatureTileRequest (whether via the header or GetFeatureTileRequest.client_info).
  'maxElevationResolutionCells': 56, // Number | The maximum allowed resolution for the returned elevation heightmap. Possible values: between 1 and 1024 (and not less than min_elevation_resolution_cells). Over-sized heightmaps will be non-uniformly down-sampled such that each edge is no longer than this value. Non-uniformity is chosen to maximise the amount of preserved data. For example: Original resolution: 100px (width) * 30px (height) max_elevation_resolution: 30 New resolution: 30px (width) * 30px (height)
  'minElevationResolutionCells': 56, // Number |  api-linter: core::0131::request-unknown-fields=disabled aip.dev/not-precedent: Maintaining existing request parameter pattern. The minimum allowed resolution for the returned elevation heightmap. Possible values: between 0 and 1024 (and not more than max_elevation_resolution_cells). Zero is supported for backward compatibility. Under-sized heightmaps will be non-uniformly up-sampled such that each edge is no shorter than this value. Non-uniformity is chosen to maximise the amount of preserved data. For example: Original resolution: 30px (width) * 10px (height) min_elevation_resolution: 30 New resolution: 30px (width) * 30px (height)
  'terrainFormats': ["null"], // [String] | Terrain formats that the client understands.
  'enableModeledVolumes': true, // Boolean | Flag indicating whether 3D building models should be enabled. If this is set structures will be returned as 3D modeled volumes rather than 2.5D extruded areas where possible.
  'enablePoliticalFeatures': true, // Boolean | Flag indicating whether political features should be returned.
  'enablePrivateRoads': true, // Boolean | Flag indicating whether the returned tile will contain road features that are marked private. Private roads are indicated by the Feature.segment_info.road_info.is_private field.
  'enableUnclippedBuildings': true, // Boolean | Flag indicating whether unclipped buildings should be returned. If this is set, building render ops will extend beyond the tile boundary. Buildings will only be returned on the tile that contains their centroid.
  'languageCode': "languageCode_example", // String | Required. The BCP-47 language code corresponding to the language in which the name was requested, such as \"en-US\" or \"sr-Latn\". For more information, see http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
  'regionCode': "regionCode_example" // String | Required. The Unicode country/region code (CLDR) of the location from which the request is coming from, such as \"US\" and \"419\". For more information, see http://www.unicode.org/reports/tr35/#unicode_region_subtag.
};
apiInstance.vectortileTerraintilesGet(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name of the tile. The tile resource name is prefixed by its collection ID &#x60;terraintiles/&#x60; followed by the resource ID, which encodes the tile&#39;s global x and y coordinates and zoom level as &#x60;@,,z&#x60;. For example, &#x60;terraintiles/@1,2,3z&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **altitudePrecisionCentimeters** | **Number**| The precision of terrain altitudes in centimeters. Possible values: between 1 (cm level precision) and 1,000,000 (10-kilometer level precision). | [optional] 
 **clientInfoApiClient** | **String**| API client name and version. For example, the SDK calling the API. The exact format is up to the client. | [optional] 
 **clientInfoApplicationId** | **String**| Application ID, such as the package name on Android and the bundle identifier on iOS platforms. | [optional] 
 **clientInfoApplicationVersion** | **String**| Application version number, such as \&quot;1.2.3\&quot;. The exact format is application-dependent. | [optional] 
 **clientInfoDeviceModel** | **String**| Device model as reported by the device. The exact format is platform-dependent. | [optional] 
 **clientInfoOperatingSystem** | **String**| Operating system name and version as reported by the OS. For example, \&quot;Mac OS X 10.10.4\&quot;. The exact format is platform-dependent. | [optional] 
 **clientInfoPlatform** | **String**| Platform where the application is running. | [optional] 
 **clientInfoUserId** | **String**| Required. A client-generated user ID. The ID should be generated and persisted during the first user session or whenever a pre-existing ID is not found. The exact format is up to the client. This must be non-empty in a GetFeatureTileRequest (whether via the header or GetFeatureTileRequest.client_info). | [optional] 
 **maxElevationResolutionCells** | **Number**| The maximum allowed resolution for the returned elevation heightmap. Possible values: between 1 and 1024 (and not less than min_elevation_resolution_cells). Over-sized heightmaps will be non-uniformly down-sampled such that each edge is no longer than this value. Non-uniformity is chosen to maximise the amount of preserved data. For example: Original resolution: 100px (width) * 30px (height) max_elevation_resolution: 30 New resolution: 30px (width) * 30px (height) | [optional] 
 **minElevationResolutionCells** | **Number**|  api-linter: core::0131::request-unknown-fields&#x3D;disabled aip.dev/not-precedent: Maintaining existing request parameter pattern. The minimum allowed resolution for the returned elevation heightmap. Possible values: between 0 and 1024 (and not more than max_elevation_resolution_cells). Zero is supported for backward compatibility. Under-sized heightmaps will be non-uniformly up-sampled such that each edge is no shorter than this value. Non-uniformity is chosen to maximise the amount of preserved data. For example: Original resolution: 30px (width) * 10px (height) min_elevation_resolution: 30 New resolution: 30px (width) * 30px (height) | [optional] 
 **terrainFormats** | [**[String]**](String.md)| Terrain formats that the client understands. | [optional] 
 **enableModeledVolumes** | **Boolean**| Flag indicating whether 3D building models should be enabled. If this is set structures will be returned as 3D modeled volumes rather than 2.5D extruded areas where possible. | [optional] 
 **enablePoliticalFeatures** | **Boolean**| Flag indicating whether political features should be returned. | [optional] 
 **enablePrivateRoads** | **Boolean**| Flag indicating whether the returned tile will contain road features that are marked private. Private roads are indicated by the Feature.segment_info.road_info.is_private field. | [optional] 
 **enableUnclippedBuildings** | **Boolean**| Flag indicating whether unclipped buildings should be returned. If this is set, building render ops will extend beyond the tile boundary. Buildings will only be returned on the tile that contains their centroid. | [optional] 
 **languageCode** | **String**| Required. The BCP-47 language code corresponding to the language in which the name was requested, such as \&quot;en-US\&quot; or \&quot;sr-Latn\&quot;. For more information, see http://www.unicode.org/reports/tr35/#Unicode_locale_identifier. | [optional] 
 **regionCode** | **String**| Required. The Unicode country/region code (CLDR) of the location from which the request is coming from, such as \&quot;US\&quot; and \&quot;419\&quot;. For more information, see http://www.unicode.org/reports/tr35/#unicode_region_subtag. | [optional] 

### Return type

[**TerrainTile**](TerrainTile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

