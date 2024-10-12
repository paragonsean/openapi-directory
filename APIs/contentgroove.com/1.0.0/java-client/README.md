# openapi-java-client

ContentGroove API
- API version: 1.0.0
  - Build date: 2024-10-12T11:59:27.157946-04:00[America/New_York]
  - Generator version: 7.9.0

# Overview

The ContentGroove Developer API enables you to add the power of ContentGroove's video AI to your own applications and workflows.

Webhooks are a way for ContentGroove to send video information
to your application, to update your system and/or trigger other business processes.

You can use Webhooks and the Developer API separately or together.

# Getting Started with Webhooks

- Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com)
- Read \"Using Webhooks\" on the [API Reference page](https://developers.contentgroove.com/api_reference)
- Visit the [Webhooks page](https://app.contentgroove.com/webhook_subscriptions) and create a new webhook

# Using Webhooks

Webhooks, also known as callbacks, are a way for ContentGroove to notify your application as soon as possible after an event has occurred in ContentGroove.
For example after a media completes processing, ContentGroove can use a webhook to notify your application with information about the video: Suggested clips, transcription, and so on.
You can use the information sent to update your system and/or use the
webhook to trigger other business processes.

The webhook request is sent as an HTTP POST containing a payload of JSON-formatted data.
For the details of the payload format see the \"CALLBACKS\" sections below.

When your application receives the webhook request, it must respond with
a 200 HTTP status code (success).
If a 200 HTTP status code is not returned,
ContentGroove will assume that the webhook was not delivered and
will retry a limited number of times, using an exponential backoff algorithm.

ContentGroove makes a best effort to attempt to send the webhook at
least once.
Applications receiving webhooks must tolerate the
possibility of a single webhook payload being sent more than once
(idempotent behavior).
Applications receiving webhooks should tolerate the possibility that
a webhook could not be delivered
(for example your application was down when delivery was attempted).

# Getting Started with the Developer API

- Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com)
- Visit the [API Keys page](https://app.contentgroove.com/api_keys)
  - Create a new API Key then copy and save the value.
    > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️
- View all available endpoints, and try the API, on our [API Reference page](https://developers.contentgroove.com/api_reference)

# Using the Developer API

- Create a new media (video or audio) in ContentGroove
  - If the video or audio is available from a URL, you can create a media by providing the `source_url` parameter. ContentGroove will fetch the video or audio from the URL if possible.
  - Or, you can create a media from a video or audio file which you upload directly to ContentGroove (see File Uploading section below).
- After the new media is created, at first it will be in a \"processing\" state.
  Depending on the size and duration of the video or audio file, it will take some time for processing to complete.
  - You can use ContentGroove Webhooks to be notified immediately when processing has completed. (Details coming soon.)
  - You can also use the API to read the state of the media, to determine if the media has completed processing yet.
- After the media has completed processing, you can access all of these details about the media:
  - The media name and description
  - The transcription of spoken words
  - Topics and keywords which were discussed in the transcription
  - Suggested video clips are automatically created
- In addition to the automatically created video clips, you can create more video clips from the media

# Response Codes

The following is a comprehensive list of the status codes you may receive while using the ContentGroove API:

- 200 \"Ok\"
  - The request was valid
- 400 \"Bad Request
  - This is returned when there was a problem parsing the JSON body of your request if you supplied the 'Content-Type': 'application/json' header, or if your request is missing the 'Content-Type' header altogether
- 401 \"Unauthorized\"
  - This is returned when you are attempting to perform an action on a resource that you are not authorized to do
- 402 \"Payment Required\"
  - This is returned when you are attempting to perform an action that would push your account above a usage limit. You can view your usage at: https://app.contentgroove.com/quota_usage
- 404 \"Not Found\"
  - This is returned when the resource you are trying to view does not exist
- 429 \"Too Many Requests\"
  - This is returned when you have performed too many requests within a given period of time
- 500 \"Internal Server Error\"
  - This is returned when your request was valid but there was a problem on our end

# File Uploading

- Step 1: Make a GET request to the direct uploads URL endpoint (/api/v1/direct_uploads) to receive an upload URL to upload the file to and an upload id.
- Step 2: Make a PUT request with the file as the body to the upload URL received in step 1. The response will have a 200 status with no body if the upload is successful.
  ```
  curl -T /path/to/file upload_url
  ```
- Step 3: After uploading the file to the upload URL, make a POST request to the create medias endpoint (/api/v1/medias), with the upload id and optionally a name and description for the new media.
  > At this time, file uploads are limited to 5gb per file.

# Allowed media types

Video:

- Supported: Most common video formats and codecs are supported.
- Recommended: mp4

Audio:

- Supported: aac, mp3, flac, ogg, wav, and wma
- Recommended: aac

# Authentication

You can use the API Key to authenticate your API requests using any of these methods. (Replace abc123 with your actual API Key.)

- Request header `Authorization: Bearer abc123`
- Request header `X-API-KEY: abc123`
- Query parameter `api_key=abc123`
  > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️

# Link to openapi.json spec

- https://api.contentgroove.com/api-docs/v1/openapi.json



*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>1.0.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:1.0.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-1.0.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contentgroove.com/api/v1");
    
    // Configure API key authorization: BearerHeader
    ApiKeyAuth BearerHeader = (ApiKeyAuth) defaultClient.getAuthentication("BearerHeader");
    BearerHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //BearerHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateClipRequest createClipRequest = new CreateClipRequest(); // CreateClipRequest | 
    try {
      ClipResponseObject result = apiInstance.createClip(createClipRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createClip");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://api.contentgroove.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**createClip**](docs/DefaultApi.md#createClip) | **POST** /clips | create clip
*DefaultApi* | [**createMedia**](docs/DefaultApi.md#createMedia) | **POST** /medias | create media
*DefaultApi* | [**createWebhookSubscription**](docs/DefaultApi.md#createWebhookSubscription) | **POST** /webhook_subscriptions | create webhook subscription
*DefaultApi* | [**deleteClipById**](docs/DefaultApi.md#deleteClipById) | **DELETE** /clips/{id} | delete clip
*DefaultApi* | [**deleteMediaById**](docs/DefaultApi.md#deleteMediaById) | **DELETE** /medias/{id} | delete media
*DefaultApi* | [**deleteWebhookSubscriptionById**](docs/DefaultApi.md#deleteWebhookSubscriptionById) | **DELETE** /webhook_subscriptions/{id} | delete webhook subscription
*DefaultApi* | [**getClipById**](docs/DefaultApi.md#getClipById) | **GET** /clips/{id} | show clip
*DefaultApi* | [**getClips**](docs/DefaultApi.md#getClips) | **GET** /clips | list clips
*DefaultApi* | [**getMediaById**](docs/DefaultApi.md#getMediaById) | **GET** /medias/{id} | show media
*DefaultApi* | [**getMedias**](docs/DefaultApi.md#getMedias) | **GET** /medias | list medias
*DefaultApi* | [**getUploadUrl**](docs/DefaultApi.md#getUploadUrl) | **GET** /direct_uploads | prepare presigned upload url
*DefaultApi* | [**getWebhookSubscriptionById**](docs/DefaultApi.md#getWebhookSubscriptionById) | **GET** /webhook_subscriptions/{id} | show webhook subscription
*DefaultApi* | [**getWebhookSubscriptions**](docs/DefaultApi.md#getWebhookSubscriptions) | **GET** /webhook_subscriptions | list webhook subscriptions
*DefaultApi* | [**updateClipById**](docs/DefaultApi.md#updateClipById) | **PUT** /clips/{id} | update clip
*DefaultApi* | [**updateMediaById**](docs/DefaultApi.md#updateMediaById) | **PUT** /medias/{id} | update media


## Documentation for Models

 - [ClipResponseObject](docs/ClipResponseObject.md)
 - [ClipResponseObjectData](docs/ClipResponseObjectData.md)
 - [ClipResponseObjectDataAttributes](docs/ClipResponseObjectDataAttributes.md)
 - [ClipResponseObjectDataRelationships](docs/ClipResponseObjectDataRelationships.md)
 - [ClipResponseObjectDataRelationshipsMedia](docs/ClipResponseObjectDataRelationshipsMedia.md)
 - [ClipResponseObjectDataRelationshipsMediaData](docs/ClipResponseObjectDataRelationshipsMediaData.md)
 - [ClipsResponseObject](docs/ClipsResponseObject.md)
 - [CreateClipRequest](docs/CreateClipRequest.md)
 - [CreateClipRequestData](docs/CreateClipRequestData.md)
 - [CreateClipRequestDataAttributes](docs/CreateClipRequestDataAttributes.md)
 - [CreateMediaRequest](docs/CreateMediaRequest.md)
 - [CreateMediaRequestData](docs/CreateMediaRequestData.md)
 - [CreateMediaRequestDataAttributes](docs/CreateMediaRequestDataAttributes.md)
 - [CreateWebhookSubscriptionRequest](docs/CreateWebhookSubscriptionRequest.md)
 - [CreateWebhookSubscriptionRequestData](docs/CreateWebhookSubscriptionRequestData.md)
 - [CreateWebhookSubscriptionRequestDataAttributes](docs/CreateWebhookSubscriptionRequestDataAttributes.md)
 - [DirectUploadResponseObject](docs/DirectUploadResponseObject.md)
 - [DirectUploadResponseObjectData](docs/DirectUploadResponseObjectData.md)
 - [DirectUploadResponseObjectDataAttributes](docs/DirectUploadResponseObjectDataAttributes.md)
 - [LinksObjectData](docs/LinksObjectData.md)
 - [MediaResponseObject](docs/MediaResponseObject.md)
 - [MediaResponseObjectData](docs/MediaResponseObjectData.md)
 - [MediaResponseObjectDataAttributes](docs/MediaResponseObjectDataAttributes.md)
 - [MediaResponseObjectDataRelationships](docs/MediaResponseObjectDataRelationships.md)
 - [MediaResponseObjectDataRelationshipsClips](docs/MediaResponseObjectDataRelationshipsClips.md)
 - [MediasPostRequest](docs/MediasPostRequest.md)
 - [MediasPostRequestPayload](docs/MediasPostRequestPayload.md)
 - [MediasPostRequestPayloadData](docs/MediasPostRequestPayloadData.md)
 - [MediasPostRequestPayloadDataAttributes](docs/MediasPostRequestPayloadDataAttributes.md)
 - [MediasPostRequestPayloadDataRelationships](docs/MediasPostRequestPayloadDataRelationships.md)
 - [MediasPostRequestPayloadDataRelationshipsClips](docs/MediasPostRequestPayloadDataRelationshipsClips.md)
 - [MediasPostRequestPayloadDataRelationshipsClipsDataInner](docs/MediasPostRequestPayloadDataRelationshipsClipsDataInner.md)
 - [MediasPostRequestPayloadDataTranscription](docs/MediasPostRequestPayloadDataTranscription.md)
 - [MediasPostRequestPayloadDataTranscriptionData](docs/MediasPostRequestPayloadDataTranscriptionData.md)
 - [MediasPostRequestPayloadIncludedInner](docs/MediasPostRequestPayloadIncludedInner.md)
 - [MediasPostRequestPayloadIncludedInnerOneOf](docs/MediasPostRequestPayloadIncludedInnerOneOf.md)
 - [MediasPostRequestPayloadIncludedInnerOneOf1](docs/MediasPostRequestPayloadIncludedInnerOneOf1.md)
 - [MediasPostRequestPayloadIncludedInnerOneOf1Attributes](docs/MediasPostRequestPayloadIncludedInnerOneOf1Attributes.md)
 - [MediasPostRequestPayloadIncludedInnerOneOfAttributes](docs/MediasPostRequestPayloadIncludedInnerOneOfAttributes.md)
 - [MediasPostRequestPayloadIncludedInnerOneOfRelationships](docs/MediasPostRequestPayloadIncludedInnerOneOfRelationships.md)
 - [MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMedia](docs/MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMedia.md)
 - [MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMediaData](docs/MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMediaData.md)
 - [MediasResponseObject](docs/MediasResponseObject.md)
 - [PaymentRequiredErrorResponseObject](docs/PaymentRequiredErrorResponseObject.md)
 - [PaymentRequiredErrorResponseObjectErrorsInner](docs/PaymentRequiredErrorResponseObjectErrorsInner.md)
 - [PaymentRequiredErrorResponseObjectErrorsInnerSource](docs/PaymentRequiredErrorResponseObjectErrorsInnerSource.md)
 - [TooManyRequestsErrorResponseObject](docs/TooManyRequestsErrorResponseObject.md)
 - [TooManyRequestsErrorResponseObjectErrorsInner](docs/TooManyRequestsErrorResponseObjectErrorsInner.md)
 - [UnauthorizedErrorResponseObject](docs/UnauthorizedErrorResponseObject.md)
 - [UnauthorizedErrorResponseObjectErrorsInner](docs/UnauthorizedErrorResponseObjectErrorsInner.md)
 - [UpdateClipByIdRequest](docs/UpdateClipByIdRequest.md)
 - [UpdateClipByIdRequestData](docs/UpdateClipByIdRequestData.md)
 - [UpdateClipByIdRequestDataAttributes](docs/UpdateClipByIdRequestDataAttributes.md)
 - [UpdateMediaByIdRequest](docs/UpdateMediaByIdRequest.md)
 - [UpdateMediaByIdRequestData](docs/UpdateMediaByIdRequestData.md)
 - [UpdateMediaByIdRequestDataAttributes](docs/UpdateMediaByIdRequestDataAttributes.md)
 - [WebhookSubscriptionResponseObject](docs/WebhookSubscriptionResponseObject.md)
 - [WebhookSubscriptionResponseObjectData](docs/WebhookSubscriptionResponseObjectData.md)
 - [WebhookSubscriptionResponseObjectDataAttributes](docs/WebhookSubscriptionResponseObjectDataAttributes.md)
 - [WebhookSubscriptionResponseObjectDataRelationships](docs/WebhookSubscriptionResponseObjectDataRelationships.md)
 - [WebhookSubscriptionsResponseObject](docs/WebhookSubscriptionsResponseObject.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="BearerHeader"></a>
### BearerHeader

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



