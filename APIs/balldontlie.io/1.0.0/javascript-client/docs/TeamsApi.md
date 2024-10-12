# Balldontlie.TeamsApi

All URIs are relative to *https://balldontlie.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allTeams**](TeamsApi.md#allTeams) | **GET** /api/v1/teams | all teams
[**specificTeam**](TeamsApi.md#specificTeam) | **GET** /api/v1/teams/1 | specific team



## allTeams

> allTeams()

all teams

all teams

### Example

```javascript
import Balldontlie from 'balldontlie';

let apiInstance = new Balldontlie.TeamsApi();
apiInstance.allTeams((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## specificTeam

> specificTeam()

specific team

specific team

### Example

```javascript
import Balldontlie from 'balldontlie';

let apiInstance = new Balldontlie.TeamsApi();
apiInstance.specificTeam((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

