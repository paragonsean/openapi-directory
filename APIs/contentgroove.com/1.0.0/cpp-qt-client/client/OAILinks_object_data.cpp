/**
 * ContentGroove API
 * # Overview  The ContentGroove Developer API enables you to add the power of ContentGroove's video AI to your own applications and workflows.  Webhooks are a way for ContentGroove to send video information to your application, to update your system and/or trigger other business processes.  You can use Webhooks and the Developer API separately or together.  # Getting Started with Webhooks  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Read \"Using Webhooks\" on the [API Reference page](https://developers.contentgroove.com/api_reference) - Visit the [Webhooks page](https://app.contentgroove.com/webhook_subscriptions) and create a new webhook  # Using Webhooks  Webhooks, also known as callbacks, are a way for ContentGroove to notify your application as soon as possible after an event has occurred in ContentGroove. For example after a media completes processing, ContentGroove can use a webhook to notify your application with information about the video: Suggested clips, transcription, and so on. You can use the information sent to update your system and/or use the webhook to trigger other business processes.  The webhook request is sent as an HTTP POST containing a payload of JSON-formatted data. For the details of the payload format see the \"CALLBACKS\" sections below.  When your application receives the webhook request, it must respond with a 200 HTTP status code (success). If a 200 HTTP status code is not returned, ContentGroove will assume that the webhook was not delivered and will retry a limited number of times, using an exponential backoff algorithm.  ContentGroove makes a best effort to attempt to send the webhook at least once. Applications receiving webhooks must tolerate the possibility of a single webhook payload being sent more than once (idempotent behavior). Applications receiving webhooks should tolerate the possibility that a webhook could not be delivered (for example your application was down when delivery was attempted).  # Getting Started with the Developer API  - Sign up for an account at [app.contentgroove.com](https://app.contentgroove.com) - Visit the [API Keys page](https://app.contentgroove.com/api_keys)   - Create a new API Key then copy and save the value.     > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️ - View all available endpoints, and try the API, on our [API Reference page](https://developers.contentgroove.com/api_reference)  # Using the Developer API  - Create a new media (video or audio) in ContentGroove   - If the video or audio is available from a URL, you can create a media by providing the `source_url` parameter. ContentGroove will fetch the video or audio from the URL if possible.   - Or, you can create a media from a video or audio file which you upload directly to ContentGroove (see File Uploading section below). - After the new media is created, at first it will be in a \"processing\" state.   Depending on the size and duration of the video or audio file, it will take some time for processing to complete.   - You can use ContentGroove Webhooks to be notified immediately when processing has completed. (Details coming soon.)   - You can also use the API to read the state of the media, to determine if the media has completed processing yet. - After the media has completed processing, you can access all of these details about the media:   - The media name and description   - The transcription of spoken words   - Topics and keywords which were discussed in the transcription   - Suggested video clips are automatically created - In addition to the automatically created video clips, you can create more video clips from the media  # Response Codes  The following is a comprehensive list of the status codes you may receive while using the ContentGroove API:  - 200 \"Ok\"   - The request was valid - 400 \"Bad Request   - This is returned when there was a problem parsing the JSON body of your request if you supplied the 'Content-Type': 'application/json' header, or if your request is missing the 'Content-Type' header altogether - 401 \"Unauthorized\"   - This is returned when you are attempting to perform an action on a resource that you are not authorized to do - 402 \"Payment Required\"   - This is returned when you are attempting to perform an action that would push your account above a usage limit. You can view your usage at: https://app.contentgroove.com/quota_usage - 404 \"Not Found\"   - This is returned when the resource you are trying to view does not exist - 429 \"Too Many Requests\"   - This is returned when you have performed too many requests within a given period of time - 500 \"Internal Server Error\"   - This is returned when your request was valid but there was a problem on our end  # File Uploading  - Step 1: Make a GET request to the direct uploads URL endpoint (/api/v1/direct_uploads) to receive an upload URL to upload the file to and an upload id. - Step 2: Make a PUT request with the file as the body to the upload URL received in step 1. The response will have a 200 status with no body if the upload is successful.   ```   curl -T /path/to/file upload_url   ``` - Step 3: After uploading the file to the upload URL, make a POST request to the create medias endpoint (/api/v1/medias), with the upload id and optionally a name and description for the new media.   > At this time, file uploads are limited to 5gb per file.  # Allowed media types  Video:  - Supported: Most common video formats and codecs are supported. - Recommended: mp4  Audio:  - Supported: aac, mp3, flac, ogg, wav, and wma - Recommended: aac  # Authentication  You can use the API Key to authenticate your API requests using any of these methods. (Replace abc123 with your actual API Key.)  - Request header `Authorization: Bearer abc123` - Request header `X-API-KEY: abc123` - Query parameter `api_key=abc123`   > ⚠️ **IMPORTANT**: This API Key is intended only for use on the server side. Be sure never to use a server-side API Key in client-side (web, mobile, or otherwise) code. ⚠️  # Link to openapi.json spec  - https://api.contentgroove.com/api-docs/v1/openapi.json 
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILinks_object_data.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILinks_object_data::OAILinks_object_data(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILinks_object_data::OAILinks_object_data() {
    this->initializeModel();
}

OAILinks_object_data::~OAILinks_object_data() {}

void OAILinks_object_data::initializeModel() {

    m_current_isSet = false;
    m_current_isValid = false;

    m_first_isSet = false;
    m_first_isValid = false;

    m_last_isSet = false;
    m_last_isValid = false;

    m_next_isSet = false;
    m_next_isValid = false;

    m_prev_isSet = false;
    m_prev_isValid = false;

    m_self_isSet = false;
    m_self_isValid = false;
}

void OAILinks_object_data::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILinks_object_data::fromJsonObject(QJsonObject json) {

    m_current_isValid = ::OpenAPI::fromJsonValue(m_current, json[QString("current")]);
    m_current_isSet = !json[QString("current")].isNull() && m_current_isValid;

    m_first_isValid = ::OpenAPI::fromJsonValue(m_first, json[QString("first")]);
    m_first_isSet = !json[QString("first")].isNull() && m_first_isValid;

    m_last_isValid = ::OpenAPI::fromJsonValue(m_last, json[QString("last")]);
    m_last_isSet = !json[QString("last")].isNull() && m_last_isValid;

    m_next_isValid = ::OpenAPI::fromJsonValue(m_next, json[QString("next")]);
    m_next_isSet = !json[QString("next")].isNull() && m_next_isValid;

    m_prev_isValid = ::OpenAPI::fromJsonValue(m_prev, json[QString("prev")]);
    m_prev_isSet = !json[QString("prev")].isNull() && m_prev_isValid;

    m_self_isValid = ::OpenAPI::fromJsonValue(m_self, json[QString("self")]);
    m_self_isSet = !json[QString("self")].isNull() && m_self_isValid;
}

QString OAILinks_object_data::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILinks_object_data::asJsonObject() const {
    QJsonObject obj;
    if (m_current_isSet) {
        obj.insert(QString("current"), ::OpenAPI::toJsonValue(m_current));
    }
    if (m_first_isSet) {
        obj.insert(QString("first"), ::OpenAPI::toJsonValue(m_first));
    }
    if (m_last_isSet) {
        obj.insert(QString("last"), ::OpenAPI::toJsonValue(m_last));
    }
    if (m_next_isSet) {
        obj.insert(QString("next"), ::OpenAPI::toJsonValue(m_next));
    }
    if (m_prev_isSet) {
        obj.insert(QString("prev"), ::OpenAPI::toJsonValue(m_prev));
    }
    if (m_self_isSet) {
        obj.insert(QString("self"), ::OpenAPI::toJsonValue(m_self));
    }
    return obj;
}

QString OAILinks_object_data::getCurrent() const {
    return m_current;
}
void OAILinks_object_data::setCurrent(const QString &current) {
    m_current = current;
    m_current_isSet = true;
}

bool OAILinks_object_data::is_current_Set() const{
    return m_current_isSet;
}

bool OAILinks_object_data::is_current_Valid() const{
    return m_current_isValid;
}

QString OAILinks_object_data::getFirst() const {
    return m_first;
}
void OAILinks_object_data::setFirst(const QString &first) {
    m_first = first;
    m_first_isSet = true;
}

bool OAILinks_object_data::is_first_Set() const{
    return m_first_isSet;
}

bool OAILinks_object_data::is_first_Valid() const{
    return m_first_isValid;
}

QString OAILinks_object_data::getLast() const {
    return m_last;
}
void OAILinks_object_data::setLast(const QString &last) {
    m_last = last;
    m_last_isSet = true;
}

bool OAILinks_object_data::is_last_Set() const{
    return m_last_isSet;
}

bool OAILinks_object_data::is_last_Valid() const{
    return m_last_isValid;
}

QString OAILinks_object_data::getNext() const {
    return m_next;
}
void OAILinks_object_data::setNext(const QString &next) {
    m_next = next;
    m_next_isSet = true;
}

bool OAILinks_object_data::is_next_Set() const{
    return m_next_isSet;
}

bool OAILinks_object_data::is_next_Valid() const{
    return m_next_isValid;
}

QString OAILinks_object_data::getPrev() const {
    return m_prev;
}
void OAILinks_object_data::setPrev(const QString &prev) {
    m_prev = prev;
    m_prev_isSet = true;
}

bool OAILinks_object_data::is_prev_Set() const{
    return m_prev_isSet;
}

bool OAILinks_object_data::is_prev_Valid() const{
    return m_prev_isValid;
}

QString OAILinks_object_data::getSelf() const {
    return m_self;
}
void OAILinks_object_data::setSelf(const QString &self) {
    m_self = self;
    m_self_isSet = true;
}

bool OAILinks_object_data::is_self_Set() const{
    return m_self_isSet;
}

bool OAILinks_object_data::is_self_Valid() const{
    return m_self_isValid;
}

bool OAILinks_object_data::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_current_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_prev_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_self_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILinks_object_data::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
