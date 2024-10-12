

# FhirNotificationConfig

Contains the configuration for FHIR notifications.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pubsubTopic** | **String** | The [Pub/Sub](https://cloud.google.com/pubsub/docs/) topic that notifications of changes are published on. Supplied by the client. The notification is a &#x60;PubsubMessage&#x60; with the following fields: * &#x60;PubsubMessage.Data&#x60; contains the resource name. * &#x60;PubsubMessage.MessageId&#x60; is the ID of this notification. It is guaranteed to be unique within the topic. * &#x60;PubsubMessage.PublishTime&#x60; is the time when the message was published. Note that notifications are only sent if the topic is non-empty. [Topic names](https://cloud.google.com/pubsub/docs/overview#names) must be scoped to a project. The Cloud Healthcare API service account, service-@gcp-sa-healthcare.iam.gserviceaccount.com, must have publisher permissions on the given Pub/Sub topic. Not having adequate permissions causes the calls that send notifications to fail (https://cloud.google.com/healthcare-api/docs/permissions-healthcare-api-gcp-products#dicom_fhir_and_hl7v2_store_cloud_pubsub_permissions). If a notification can&#39;t be published to Pub/Sub, errors are logged to Cloud Logging. For more information, see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare-api/docs/how-tos/logging). |  [optional] |
|**sendFullResource** | **Boolean** | Whether to send full FHIR resource to this Pub/Sub topic for Create and Update operation. Note that setting this to true does not guarantee that all resources will be sent in the format of full FHIR resource. When a resource change is too large or during heavy traffic, only the resource name will be sent. Clients should always check the \&quot;payloadType\&quot; label from a Pub/Sub message to determine whether it needs to fetch the full resource as a separate operation. |  [optional] |
|**sendPreviousResourceOnDelete** | **Boolean** | Whether to send full FHIR resource to this Pub/Sub topic for deleting FHIR resource. Note that setting this to true does not guarantee that all previous resources will be sent in the format of full FHIR resource. When a resource change is too large or during heavy traffic, only the resource name will be sent. Clients should always check the \&quot;payloadType\&quot; label from a Pub/Sub message to determine whether it needs to fetch the full previous resource as a separate operation. |  [optional] |



