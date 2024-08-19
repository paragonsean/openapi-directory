# EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmNotificationsApi

All URIs are relative to *http://etsi.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appPkgNotificationPOST**](AppPkgmNotificationsApi.md#appPkgNotificationPOST) | **POST** /user_defined_notification | Registers a notification endpoint to notify application package operations



## appPkgNotificationPOST

> appPkgNotificationPOST(appPkgNotification)

Registers a notification endpoint to notify application package operations

Registers a notification endpoint to notify application package operations

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmNotificationsApi();
let appPkgNotification = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgNotification(); // AppPkgNotification | Notification endpoint to be created
apiInstance.appPkgNotificationPOST(appPkgNotification, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appPkgNotification** | [**AppPkgNotification**](AppPkgNotification.md)| Notification endpoint to be created | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

