# content_groove_api

ContentGrooveApi - JavaScript client for content_groove_api
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

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install content_groove_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your content_groove_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var ContentGrooveApi = require('content_groove_api');

var defaultClient = ContentGrooveApi.ApiClient.instance;
// Configure API key authorization: BearerHeader
var BearerHeader = defaultClient.authentications['BearerHeader'];
BearerHeader.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//BearerHeader.apiKeyPrefix['Authorization'] = "Token"

var api = new ContentGrooveApi.DefaultApi()
var createClipRequest = new ContentGrooveApi.CreateClipRequest(); // {CreateClipRequest} 
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.createClip(createClipRequest, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.contentgroove.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContentGrooveApi.DefaultApi* | [**createClip**](docs/DefaultApi.md#createClip) | **POST** /clips | create clip
*ContentGrooveApi.DefaultApi* | [**createMedia**](docs/DefaultApi.md#createMedia) | **POST** /medias | create media
*ContentGrooveApi.DefaultApi* | [**createWebhookSubscription**](docs/DefaultApi.md#createWebhookSubscription) | **POST** /webhook_subscriptions | create webhook subscription
*ContentGrooveApi.DefaultApi* | [**deleteClipById**](docs/DefaultApi.md#deleteClipById) | **DELETE** /clips/{id} | delete clip
*ContentGrooveApi.DefaultApi* | [**deleteMediaById**](docs/DefaultApi.md#deleteMediaById) | **DELETE** /medias/{id} | delete media
*ContentGrooveApi.DefaultApi* | [**deleteWebhookSubscriptionById**](docs/DefaultApi.md#deleteWebhookSubscriptionById) | **DELETE** /webhook_subscriptions/{id} | delete webhook subscription
*ContentGrooveApi.DefaultApi* | [**getClipById**](docs/DefaultApi.md#getClipById) | **GET** /clips/{id} | show clip
*ContentGrooveApi.DefaultApi* | [**getClips**](docs/DefaultApi.md#getClips) | **GET** /clips | list clips
*ContentGrooveApi.DefaultApi* | [**getMediaById**](docs/DefaultApi.md#getMediaById) | **GET** /medias/{id} | show media
*ContentGrooveApi.DefaultApi* | [**getMedias**](docs/DefaultApi.md#getMedias) | **GET** /medias | list medias
*ContentGrooveApi.DefaultApi* | [**getUploadUrl**](docs/DefaultApi.md#getUploadUrl) | **GET** /direct_uploads | prepare presigned upload url
*ContentGrooveApi.DefaultApi* | [**getWebhookSubscriptionById**](docs/DefaultApi.md#getWebhookSubscriptionById) | **GET** /webhook_subscriptions/{id} | show webhook subscription
*ContentGrooveApi.DefaultApi* | [**getWebhookSubscriptions**](docs/DefaultApi.md#getWebhookSubscriptions) | **GET** /webhook_subscriptions | list webhook subscriptions
*ContentGrooveApi.DefaultApi* | [**updateClipById**](docs/DefaultApi.md#updateClipById) | **PUT** /clips/{id} | update clip
*ContentGrooveApi.DefaultApi* | [**updateMediaById**](docs/DefaultApi.md#updateMediaById) | **PUT** /medias/{id} | update media


## Documentation for Models

 - [ContentGrooveApi.ClipResponseObject](docs/ClipResponseObject.md)
 - [ContentGrooveApi.ClipResponseObjectData](docs/ClipResponseObjectData.md)
 - [ContentGrooveApi.ClipResponseObjectDataAttributes](docs/ClipResponseObjectDataAttributes.md)
 - [ContentGrooveApi.ClipResponseObjectDataRelationships](docs/ClipResponseObjectDataRelationships.md)
 - [ContentGrooveApi.ClipResponseObjectDataRelationshipsMedia](docs/ClipResponseObjectDataRelationshipsMedia.md)
 - [ContentGrooveApi.ClipResponseObjectDataRelationshipsMediaData](docs/ClipResponseObjectDataRelationshipsMediaData.md)
 - [ContentGrooveApi.ClipsResponseObject](docs/ClipsResponseObject.md)
 - [ContentGrooveApi.CreateClipRequest](docs/CreateClipRequest.md)
 - [ContentGrooveApi.CreateClipRequestData](docs/CreateClipRequestData.md)
 - [ContentGrooveApi.CreateClipRequestDataAttributes](docs/CreateClipRequestDataAttributes.md)
 - [ContentGrooveApi.CreateMediaRequest](docs/CreateMediaRequest.md)
 - [ContentGrooveApi.CreateMediaRequestData](docs/CreateMediaRequestData.md)
 - [ContentGrooveApi.CreateMediaRequestDataAttributes](docs/CreateMediaRequestDataAttributes.md)
 - [ContentGrooveApi.CreateWebhookSubscriptionRequest](docs/CreateWebhookSubscriptionRequest.md)
 - [ContentGrooveApi.CreateWebhookSubscriptionRequestData](docs/CreateWebhookSubscriptionRequestData.md)
 - [ContentGrooveApi.CreateWebhookSubscriptionRequestDataAttributes](docs/CreateWebhookSubscriptionRequestDataAttributes.md)
 - [ContentGrooveApi.DirectUploadResponseObject](docs/DirectUploadResponseObject.md)
 - [ContentGrooveApi.DirectUploadResponseObjectData](docs/DirectUploadResponseObjectData.md)
 - [ContentGrooveApi.DirectUploadResponseObjectDataAttributes](docs/DirectUploadResponseObjectDataAttributes.md)
 - [ContentGrooveApi.LinksObjectData](docs/LinksObjectData.md)
 - [ContentGrooveApi.MediaResponseObject](docs/MediaResponseObject.md)
 - [ContentGrooveApi.MediaResponseObjectData](docs/MediaResponseObjectData.md)
 - [ContentGrooveApi.MediaResponseObjectDataAttributes](docs/MediaResponseObjectDataAttributes.md)
 - [ContentGrooveApi.MediaResponseObjectDataRelationships](docs/MediaResponseObjectDataRelationships.md)
 - [ContentGrooveApi.MediaResponseObjectDataRelationshipsClips](docs/MediaResponseObjectDataRelationshipsClips.md)
 - [ContentGrooveApi.MediasPostRequest](docs/MediasPostRequest.md)
 - [ContentGrooveApi.MediasPostRequestPayload](docs/MediasPostRequestPayload.md)
 - [ContentGrooveApi.MediasPostRequestPayloadData](docs/MediasPostRequestPayloadData.md)
 - [ContentGrooveApi.MediasPostRequestPayloadDataAttributes](docs/MediasPostRequestPayloadDataAttributes.md)
 - [ContentGrooveApi.MediasPostRequestPayloadDataRelationships](docs/MediasPostRequestPayloadDataRelationships.md)
 - [ContentGrooveApi.MediasPostRequestPayloadDataRelationshipsClips](docs/MediasPostRequestPayloadDataRelationshipsClips.md)
 - [ContentGrooveApi.MediasPostRequestPayloadDataRelationshipsClipsDataInner](docs/MediasPostRequestPayloadDataRelationshipsClipsDataInner.md)
 - [ContentGrooveApi.MediasPostRequestPayloadDataTranscription](docs/MediasPostRequestPayloadDataTranscription.md)
 - [ContentGrooveApi.MediasPostRequestPayloadDataTranscriptionData](docs/MediasPostRequestPayloadDataTranscriptionData.md)
 - [ContentGrooveApi.MediasPostRequestPayloadIncludedInner](docs/MediasPostRequestPayloadIncludedInner.md)
 - [ContentGrooveApi.MediasPostRequestPayloadIncludedInnerOneOf](docs/MediasPostRequestPayloadIncludedInnerOneOf.md)
 - [ContentGrooveApi.MediasPostRequestPayloadIncludedInnerOneOf1](docs/MediasPostRequestPayloadIncludedInnerOneOf1.md)
 - [ContentGrooveApi.MediasPostRequestPayloadIncludedInnerOneOf1Attributes](docs/MediasPostRequestPayloadIncludedInnerOneOf1Attributes.md)
 - [ContentGrooveApi.MediasPostRequestPayloadIncludedInnerOneOfAttributes](docs/MediasPostRequestPayloadIncludedInnerOneOfAttributes.md)
 - [ContentGrooveApi.MediasPostRequestPayloadIncludedInnerOneOfRelationships](docs/MediasPostRequestPayloadIncludedInnerOneOfRelationships.md)
 - [ContentGrooveApi.MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMedia](docs/MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMedia.md)
 - [ContentGrooveApi.MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMediaData](docs/MediasPostRequestPayloadIncludedInnerOneOfRelationshipsMediaData.md)
 - [ContentGrooveApi.MediasResponseObject](docs/MediasResponseObject.md)
 - [ContentGrooveApi.PaymentRequiredErrorResponseObject](docs/PaymentRequiredErrorResponseObject.md)
 - [ContentGrooveApi.PaymentRequiredErrorResponseObjectErrorsInner](docs/PaymentRequiredErrorResponseObjectErrorsInner.md)
 - [ContentGrooveApi.PaymentRequiredErrorResponseObjectErrorsInnerSource](docs/PaymentRequiredErrorResponseObjectErrorsInnerSource.md)
 - [ContentGrooveApi.TooManyRequestsErrorResponseObject](docs/TooManyRequestsErrorResponseObject.md)
 - [ContentGrooveApi.TooManyRequestsErrorResponseObjectErrorsInner](docs/TooManyRequestsErrorResponseObjectErrorsInner.md)
 - [ContentGrooveApi.UnauthorizedErrorResponseObject](docs/UnauthorizedErrorResponseObject.md)
 - [ContentGrooveApi.UnauthorizedErrorResponseObjectErrorsInner](docs/UnauthorizedErrorResponseObjectErrorsInner.md)
 - [ContentGrooveApi.UpdateClipByIdRequest](docs/UpdateClipByIdRequest.md)
 - [ContentGrooveApi.UpdateClipByIdRequestData](docs/UpdateClipByIdRequestData.md)
 - [ContentGrooveApi.UpdateClipByIdRequestDataAttributes](docs/UpdateClipByIdRequestDataAttributes.md)
 - [ContentGrooveApi.UpdateMediaByIdRequest](docs/UpdateMediaByIdRequest.md)
 - [ContentGrooveApi.UpdateMediaByIdRequestData](docs/UpdateMediaByIdRequestData.md)
 - [ContentGrooveApi.UpdateMediaByIdRequestDataAttributes](docs/UpdateMediaByIdRequestDataAttributes.md)
 - [ContentGrooveApi.WebhookSubscriptionResponseObject](docs/WebhookSubscriptionResponseObject.md)
 - [ContentGrooveApi.WebhookSubscriptionResponseObjectData](docs/WebhookSubscriptionResponseObjectData.md)
 - [ContentGrooveApi.WebhookSubscriptionResponseObjectDataAttributes](docs/WebhookSubscriptionResponseObjectDataAttributes.md)
 - [ContentGrooveApi.WebhookSubscriptionResponseObjectDataRelationships](docs/WebhookSubscriptionResponseObjectDataRelationships.md)
 - [ContentGrooveApi.WebhookSubscriptionsResponseObject](docs/WebhookSubscriptionsResponseObject.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### BearerHeader


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

