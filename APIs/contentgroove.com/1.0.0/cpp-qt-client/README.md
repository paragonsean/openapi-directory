# C++ Qt API client

# 

ContentGroove API

- API version: 1.0.0
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

1. CMake 3.2+
2. Qt
3. C++ Compiler

## Getting Started

example.h:
```c++

#include <iostream>
#include "../client/OAIDefaultApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    OAICreateClip_request create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIDefaultApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

OAICreateClip_request Example::create(){
    OAICreateClip_request obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIDefaultApi apiInstance;
     
      // Configure API key authorization: BearerHeader
      apiInstance.setApiKey("YOUR API KEY NAME","YOUR API KEY");

      QEventLoop loop;
      connect(&apiInstance, &OAIDefaultApi::createClipSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIDefaultApi::createClipSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      OAICreateClip_request oai_create_clip_request = create(); // OAICreateClip_request | 
      apiInstance.createClip(oai_create_clip_request);
      QTimer::singleShot(5000, &loop, &QEventLoop::quit);
      loop.exec();
  }

```

## Documentation for Servers

Parameterized Servers are supported. Define a server in the API for each endpoint with arbitrary numbers of variables:

```yaml
servers:
- url: http://{server}:{port}/{basePath}
  description: Description of the Server
  variables:
    server:
        enum:
          - 'petstore'
          - 'qa-petstore'
          - 'dev-petstore'
        default: 'petstore'
    port:
      enum:
        - '3000'
        - '1000'
      default: '3000'
    basePath:
      default: v1
```
To change the default variable, use this function in each Api:
```c++
int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
```
The parameter "serverIndex" will choose a server from the server list for each endpoint. There is always at least one server with index 0. The Parameter "operation" should be the desired endpoint operationid.
Variable is the name of the variable you wish to change and the value is the new default Value.
The function will return -1 when the variable does not exists, -2 if value is not defined in the variable enum and -3 if the operation is not found.

If your endpoint has multiple server objects in the servers array, you can set the server that will be used with this function:
```c++
void setServerIndex(const QString &operation, int serverIndex);
```
Parameter "operation" should be your operationid. "serverIndex" is the index you want to set as your default server. The function will check if there is a server with your index.
Here is an example of multiple servers in the servers array. The first server will have index 0 and the second will have index 1.
```yaml
servers:
- url: http://{server}:8080/
  description: Description of the Server
  variables:
    server:
        enum:
          - 'petstore'
          - 'qa-petstore'
          - 'dev-petstore'
        default: 'petstore'
- url: https://localhost:8080/v1
```

## Documentation for Authorization

Authentication schemes defined for the API:
### BearerHeader


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## License

 for more information visit []()