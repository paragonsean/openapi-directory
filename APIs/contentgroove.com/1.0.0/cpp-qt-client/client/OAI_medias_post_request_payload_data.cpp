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

#include "OAI_medias_post_request_payload_data.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_medias_post_request_payload_data::OAI_medias_post_request_payload_data(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_medias_post_request_payload_data::OAI_medias_post_request_payload_data() {
    this->initializeModel();
}

OAI_medias_post_request_payload_data::~OAI_medias_post_request_payload_data() {}

void OAI_medias_post_request_payload_data::initializeModel() {

    m_attributes_isSet = false;
    m_attributes_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_relationships_isSet = false;
    m_relationships_isValid = false;

    m_transcription_isSet = false;
    m_transcription_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAI_medias_post_request_payload_data::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_medias_post_request_payload_data::fromJsonObject(QJsonObject json) {

    m_attributes_isValid = ::OpenAPI::fromJsonValue(m_attributes, json[QString("attributes")]);
    m_attributes_isSet = !json[QString("attributes")].isNull() && m_attributes_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_relationships_isValid = ::OpenAPI::fromJsonValue(m_relationships, json[QString("relationships")]);
    m_relationships_isSet = !json[QString("relationships")].isNull() && m_relationships_isValid;

    m_transcription_isValid = ::OpenAPI::fromJsonValue(m_transcription, json[QString("transcription")]);
    m_transcription_isSet = !json[QString("transcription")].isNull() && m_transcription_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAI_medias_post_request_payload_data::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_medias_post_request_payload_data::asJsonObject() const {
    QJsonObject obj;
    if (m_attributes.isSet()) {
        obj.insert(QString("attributes"), ::OpenAPI::toJsonValue(m_attributes));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_relationships.isSet()) {
        obj.insert(QString("relationships"), ::OpenAPI::toJsonValue(m_relationships));
    }
    if (m_transcription.isSet()) {
        obj.insert(QString("transcription"), ::OpenAPI::toJsonValue(m_transcription));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAI_medias_post_request_payload_data_attributes OAI_medias_post_request_payload_data::getAttributes() const {
    return m_attributes;
}
void OAI_medias_post_request_payload_data::setAttributes(const OAI_medias_post_request_payload_data_attributes &attributes) {
    m_attributes = attributes;
    m_attributes_isSet = true;
}

bool OAI_medias_post_request_payload_data::is_attributes_Set() const{
    return m_attributes_isSet;
}

bool OAI_medias_post_request_payload_data::is_attributes_Valid() const{
    return m_attributes_isValid;
}

QString OAI_medias_post_request_payload_data::getId() const {
    return m_id;
}
void OAI_medias_post_request_payload_data::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAI_medias_post_request_payload_data::is_id_Set() const{
    return m_id_isSet;
}

bool OAI_medias_post_request_payload_data::is_id_Valid() const{
    return m_id_isValid;
}

OAI_medias_post_request_payload_data_relationships OAI_medias_post_request_payload_data::getRelationships() const {
    return m_relationships;
}
void OAI_medias_post_request_payload_data::setRelationships(const OAI_medias_post_request_payload_data_relationships &relationships) {
    m_relationships = relationships;
    m_relationships_isSet = true;
}

bool OAI_medias_post_request_payload_data::is_relationships_Set() const{
    return m_relationships_isSet;
}

bool OAI_medias_post_request_payload_data::is_relationships_Valid() const{
    return m_relationships_isValid;
}

OAI_medias_post_request_payload_data_transcription OAI_medias_post_request_payload_data::getTranscription() const {
    return m_transcription;
}
void OAI_medias_post_request_payload_data::setTranscription(const OAI_medias_post_request_payload_data_transcription &transcription) {
    m_transcription = transcription;
    m_transcription_isSet = true;
}

bool OAI_medias_post_request_payload_data::is_transcription_Set() const{
    return m_transcription_isSet;
}

bool OAI_medias_post_request_payload_data::is_transcription_Valid() const{
    return m_transcription_isValid;
}

QString OAI_medias_post_request_payload_data::getType() const {
    return m_type;
}
void OAI_medias_post_request_payload_data::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAI_medias_post_request_payload_data::is_type_Set() const{
    return m_type_isSet;
}

bool OAI_medias_post_request_payload_data::is_type_Valid() const{
    return m_type_isValid;
}

bool OAI_medias_post_request_payload_data::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_attributes.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_relationships.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_transcription.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_medias_post_request_payload_data::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
