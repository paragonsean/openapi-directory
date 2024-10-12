# TcGdexApi.FiltersApi

All URIs are relative to *https://api.tcgdex.net/v2/en*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoriesCategoryGet**](FiltersApi.md#categoriesCategoryGet) | **GET** /categories/{category} | 
[**categoriesGet**](FiltersApi.md#categoriesGet) | **GET** /categories | 
[**dexIdsDexIdGet**](FiltersApi.md#dexIdsDexIdGet) | **GET** /dex-ids/{dexId} | 
[**dexIdsGet**](FiltersApi.md#dexIdsGet) | **GET** /dex-ids | 
[**energyTypesEnergyTypeGet**](FiltersApi.md#energyTypesEnergyTypeGet) | **GET** /energy-types/{energy-type} | 
[**energyTypesGet**](FiltersApi.md#energyTypesGet) | **GET** /energy-types | 
[**hpGet**](FiltersApi.md#hpGet) | **GET** /hp | 
[**hpHpGet**](FiltersApi.md#hpHpGet) | **GET** /hp/{hp} | 
[**illustratorsGet**](FiltersApi.md#illustratorsGet) | **GET** /illustrators | 
[**illustratorsIllustratorGet**](FiltersApi.md#illustratorsIllustratorGet) | **GET** /illustrators/{illustrator} | 
[**raritiesGet**](FiltersApi.md#raritiesGet) | **GET** /rarities | 
[**raritiesRarityGet**](FiltersApi.md#raritiesRarityGet) | **GET** /rarities/{rarity} | 
[**regulationMarksGet**](FiltersApi.md#regulationMarksGet) | **GET** /regulation-marks | 
[**regulationMarksRegulationMarkGet**](FiltersApi.md#regulationMarksRegulationMarkGet) | **GET** /regulation-marks/{regulation-mark} | 
[**retreatsGet**](FiltersApi.md#retreatsGet) | **GET** /retreats | 
[**retreatsRetreatGet**](FiltersApi.md#retreatsRetreatGet) | **GET** /retreats/{retreat} | 
[**seriesGet**](FiltersApi.md#seriesGet) | **GET** /series | 
[**seriesSerieGet**](FiltersApi.md#seriesSerieGet) | **GET** /series/{serie} | 
[**setsGet**](FiltersApi.md#setsGet) | **GET** /sets | 
[**setsSetGet**](FiltersApi.md#setsSetGet) | **GET** /sets/{set} | 
[**stagesGet**](FiltersApi.md#stagesGet) | **GET** /stages | 
[**stagesStageGet**](FiltersApi.md#stagesStageGet) | **GET** /stages/{stage} | 
[**suffixesGet**](FiltersApi.md#suffixesGet) | **GET** /suffixes | 
[**suffixesSuffixGet**](FiltersApi.md#suffixesSuffixGet) | **GET** /suffixes/{suffix} | 
[**trainerTypesGet**](FiltersApi.md#trainerTypesGet) | **GET** /trainer-types | 
[**trainerTypesTrainerTypeGet**](FiltersApi.md#trainerTypesTrainerTypeGet) | **GET** /trainer-types/{trainer-type} | 
[**typesGet**](FiltersApi.md#typesGet) | **GET** /types | 
[**typesTypeGet**](FiltersApi.md#typesTypeGet) | **GET** /types/{type} | 
[**variantsGet**](FiltersApi.md#variantsGet) | **GET** /variants | 
[**variantsVariantGet**](FiltersApi.md#variantsVariantGet) | **GET** /variants/{variant} | 



## categoriesCategoryGet

> StringEndpoint categoriesCategoryGet(category)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let category = "category_example"; // String | 
apiInstance.categoriesCategoryGet(category, (error, data, response) => {
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
 **category** | **String**|  | 

### Return type

[**StringEndpoint**](StringEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesGet

> [String] categoriesGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.categoriesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dexIdsDexIdGet

> [CardResume] dexIdsDexIdGet(dexId)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let dexId = "dexId_example"; // String | 
apiInstance.dexIdsDexIdGet(dexId, (error, data, response) => {
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
 **dexId** | **String**|  | 

### Return type

[**[CardResume]**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dexIdsGet

> [String] dexIdsGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.dexIdsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## energyTypesEnergyTypeGet

> [CardResume] energyTypesEnergyTypeGet(energyType)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let energyType = "energyType_example"; // String | 
apiInstance.energyTypesEnergyTypeGet(energyType, (error, data, response) => {
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
 **energyType** | **String**|  | 

### Return type

[**[CardResume]**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## energyTypesGet

> [String] energyTypesGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.energyTypesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hpGet

> [String] hpGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.hpGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hpHpGet

> StringEndpoint hpHpGet(hp)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let hp = "hp_example"; // String | 
apiInstance.hpHpGet(hp, (error, data, response) => {
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
 **hp** | **String**|  | 

### Return type

[**StringEndpoint**](StringEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## illustratorsGet

> [String] illustratorsGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.illustratorsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## illustratorsIllustratorGet

> StringEndpoint illustratorsIllustratorGet(illustrator)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let illustrator = "illustrator_example"; // String | 
apiInstance.illustratorsIllustratorGet(illustrator, (error, data, response) => {
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
 **illustrator** | **String**|  | 

### Return type

[**StringEndpoint**](StringEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## raritiesGet

> [String] raritiesGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.raritiesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## raritiesRarityGet

> StringEndpoint raritiesRarityGet(rarity)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let rarity = "rarity_example"; // String | 
apiInstance.raritiesRarityGet(rarity, (error, data, response) => {
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
 **rarity** | **String**|  | 

### Return type

[**StringEndpoint**](StringEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## regulationMarksGet

> [String] regulationMarksGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.regulationMarksGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## regulationMarksRegulationMarkGet

> [CardResume] regulationMarksRegulationMarkGet(regulationMark)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let regulationMark = "regulationMark_example"; // String | 
apiInstance.regulationMarksRegulationMarkGet(regulationMark, (error, data, response) => {
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
 **regulationMark** | **String**|  | 

### Return type

[**[CardResume]**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retreatsGet

> [String] retreatsGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.retreatsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retreatsRetreatGet

> StringEndpoint retreatsRetreatGet(retreat)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let retreat = "retreat_example"; // String | 
apiInstance.retreatsRetreatGet(retreat, (error, data, response) => {
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
 **retreat** | **String**|  | 

### Return type

[**StringEndpoint**](StringEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## seriesGet

> [SerieResume] seriesGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.seriesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[SerieResume]**](SerieResume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## seriesSerieGet

> Serie seriesSerieGet(serie)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let serie = "serie_example"; // String | the serie ID or name
apiInstance.seriesSerieGet(serie, (error, data, response) => {
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
 **serie** | **String**| the serie ID or name | 

### Return type

[**Serie**](Serie.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setsGet

> [SetResume] setsGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.setsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[SetResume]**](SetResume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setsSetGet

> Set setsSetGet(set)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let set = "set_example"; // String | the set ID or the set name
apiInstance.setsSetGet(set, (error, data, response) => {
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
 **set** | **String**| the set ID or the set name | 

### Return type

[**Set**](Set.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stagesGet

> [String] stagesGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.stagesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stagesStageGet

> [CardResume] stagesStageGet(stage)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let stage = "stage_example"; // String | 
apiInstance.stagesStageGet(stage, (error, data, response) => {
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
 **stage** | **String**|  | 

### Return type

[**[CardResume]**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## suffixesGet

> [String] suffixesGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.suffixesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## suffixesSuffixGet

> [CardResume] suffixesSuffixGet(suffix)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let suffix = "suffix_example"; // String | 
apiInstance.suffixesSuffixGet(suffix, (error, data, response) => {
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
 **suffix** | **String**|  | 

### Return type

[**[CardResume]**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainerTypesGet

> [String] trainerTypesGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.trainerTypesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trainerTypesTrainerTypeGet

> [CardResume] trainerTypesTrainerTypeGet(trainerType)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let trainerType = "trainerType_example"; // String | 
apiInstance.trainerTypesTrainerTypeGet(trainerType, (error, data, response) => {
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
 **trainerType** | **String**|  | 

### Return type

[**[CardResume]**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## typesGet

> [String] typesGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.typesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## typesTypeGet

> [CardResume] typesTypeGet(type)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let type = "type_example"; // String | 
apiInstance.typesTypeGet(type, (error, data, response) => {
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
 **type** | **String**|  | 

### Return type

[**[CardResume]**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## variantsGet

> [String] variantsGet()



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
apiInstance.variantsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## variantsVariantGet

> [CardResume] variantsVariantGet(variant)



### Example

```javascript
import TcGdexApi from 'tc_gdex_api';

let apiInstance = new TcGdexApi.FiltersApi();
let variant = "variant_example"; // String | 
apiInstance.variantsVariantGet(variant, (error, data, response) => {
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
 **variant** | **String**|  | 

### Return type

[**[CardResume]**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

