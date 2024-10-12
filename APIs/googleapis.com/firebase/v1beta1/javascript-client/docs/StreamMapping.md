# FirebaseManagementApi.StreamMapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | **String** | The resource name of the Firebase App associated with the Google Analytics data stream, in the format: projects/PROJECT_IDENTIFIER/androidApps/APP_ID or projects/PROJECT_IDENTIFIER/iosApps/APP_ID or projects/PROJECT_IDENTIFIER /webApps/APP_ID Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. | [optional] 
**measurementId** | **String** | Applicable for Firebase Web Apps only. The unique Google-assigned identifier of the Google Analytics web stream associated with the Firebase Web App. Firebase SDKs use this ID to interact with Google Analytics APIs. Learn more about this ID and Google Analytics web streams in the [Analytics documentation](https://support.google.com/analytics/answer/9304153). | [optional] 
**streamId** | **String** | The unique Google-assigned identifier of the Google Analytics data stream associated with the Firebase App. Learn more about Google Analytics data streams in the [Analytics documentation](https://support.google.com/analytics/answer/9303323). | [optional] 


