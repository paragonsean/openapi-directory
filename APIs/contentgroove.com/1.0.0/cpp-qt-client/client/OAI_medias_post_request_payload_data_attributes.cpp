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

#include "OAI_medias_post_request_payload_data_attributes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_medias_post_request_payload_data_attributes::OAI_medias_post_request_payload_data_attributes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_medias_post_request_payload_data_attributes::OAI_medias_post_request_payload_data_attributes() {
    this->initializeModel();
}

OAI_medias_post_request_payload_data_attributes::~OAI_medias_post_request_payload_data_attributes() {}

void OAI_medias_post_request_payload_data_attributes::initializeModel() {

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_external_id_isSet = false;
    m_external_id_isValid = false;

    m_has_fetch_error_isSet = false;
    m_has_fetch_error_isValid = false;

    m_is_processing_isSet = false;
    m_is_processing_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_original_created_at_isSet = false;
    m_original_created_at_isValid = false;

    m_processing_started_at_isSet = false;
    m_processing_started_at_isValid = false;

    m_source_created_at_isSet = false;
    m_source_created_at_isValid = false;

    m_source_file_content_type_isSet = false;
    m_source_file_content_type_isValid = false;

    m_source_file_duration_isSet = false;
    m_source_file_duration_isValid = false;

    m_source_file_height_isSet = false;
    m_source_file_height_isValid = false;

    m_source_file_preview_image_url_isSet = false;
    m_source_file_preview_image_url_isValid = false;

    m_source_file_width_isSet = false;
    m_source_file_width_isValid = false;

    m_source_url_isSet = false;
    m_source_url_isValid = false;
}

void OAI_medias_post_request_payload_data_attributes::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_medias_post_request_payload_data_attributes::fromJsonObject(QJsonObject json) {

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_external_id_isValid = ::OpenAPI::fromJsonValue(m_external_id, json[QString("external_id")]);
    m_external_id_isSet = !json[QString("external_id")].isNull() && m_external_id_isValid;

    m_has_fetch_error_isValid = ::OpenAPI::fromJsonValue(m_has_fetch_error, json[QString("has_fetch_error")]);
    m_has_fetch_error_isSet = !json[QString("has_fetch_error")].isNull() && m_has_fetch_error_isValid;

    m_is_processing_isValid = ::OpenAPI::fromJsonValue(m_is_processing, json[QString("is_processing")]);
    m_is_processing_isSet = !json[QString("is_processing")].isNull() && m_is_processing_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_original_created_at_isValid = ::OpenAPI::fromJsonValue(m_original_created_at, json[QString("original_created_at")]);
    m_original_created_at_isSet = !json[QString("original_created_at")].isNull() && m_original_created_at_isValid;

    m_processing_started_at_isValid = ::OpenAPI::fromJsonValue(m_processing_started_at, json[QString("processing_started_at")]);
    m_processing_started_at_isSet = !json[QString("processing_started_at")].isNull() && m_processing_started_at_isValid;

    m_source_created_at_isValid = ::OpenAPI::fromJsonValue(m_source_created_at, json[QString("source_created_at")]);
    m_source_created_at_isSet = !json[QString("source_created_at")].isNull() && m_source_created_at_isValid;

    m_source_file_content_type_isValid = ::OpenAPI::fromJsonValue(m_source_file_content_type, json[QString("source_file_content_type")]);
    m_source_file_content_type_isSet = !json[QString("source_file_content_type")].isNull() && m_source_file_content_type_isValid;

    m_source_file_duration_isValid = ::OpenAPI::fromJsonValue(m_source_file_duration, json[QString("source_file_duration")]);
    m_source_file_duration_isSet = !json[QString("source_file_duration")].isNull() && m_source_file_duration_isValid;

    m_source_file_height_isValid = ::OpenAPI::fromJsonValue(m_source_file_height, json[QString("source_file_height")]);
    m_source_file_height_isSet = !json[QString("source_file_height")].isNull() && m_source_file_height_isValid;

    m_source_file_preview_image_url_isValid = ::OpenAPI::fromJsonValue(m_source_file_preview_image_url, json[QString("source_file_preview_image_url")]);
    m_source_file_preview_image_url_isSet = !json[QString("source_file_preview_image_url")].isNull() && m_source_file_preview_image_url_isValid;

    m_source_file_width_isValid = ::OpenAPI::fromJsonValue(m_source_file_width, json[QString("source_file_width")]);
    m_source_file_width_isSet = !json[QString("source_file_width")].isNull() && m_source_file_width_isValid;

    m_source_url_isValid = ::OpenAPI::fromJsonValue(m_source_url, json[QString("source_url")]);
    m_source_url_isSet = !json[QString("source_url")].isNull() && m_source_url_isValid;
}

QString OAI_medias_post_request_payload_data_attributes::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_medias_post_request_payload_data_attributes::asJsonObject() const {
    QJsonObject obj;
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_external_id_isSet) {
        obj.insert(QString("external_id"), ::OpenAPI::toJsonValue(m_external_id));
    }
    if (m_has_fetch_error_isSet) {
        obj.insert(QString("has_fetch_error"), ::OpenAPI::toJsonValue(m_has_fetch_error));
    }
    if (m_is_processing_isSet) {
        obj.insert(QString("is_processing"), ::OpenAPI::toJsonValue(m_is_processing));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_original_created_at_isSet) {
        obj.insert(QString("original_created_at"), ::OpenAPI::toJsonValue(m_original_created_at));
    }
    if (m_processing_started_at_isSet) {
        obj.insert(QString("processing_started_at"), ::OpenAPI::toJsonValue(m_processing_started_at));
    }
    if (m_source_created_at_isSet) {
        obj.insert(QString("source_created_at"), ::OpenAPI::toJsonValue(m_source_created_at));
    }
    if (m_source_file_content_type_isSet) {
        obj.insert(QString("source_file_content_type"), ::OpenAPI::toJsonValue(m_source_file_content_type));
    }
    if (m_source_file_duration_isSet) {
        obj.insert(QString("source_file_duration"), ::OpenAPI::toJsonValue(m_source_file_duration));
    }
    if (m_source_file_height_isSet) {
        obj.insert(QString("source_file_height"), ::OpenAPI::toJsonValue(m_source_file_height));
    }
    if (m_source_file_preview_image_url_isSet) {
        obj.insert(QString("source_file_preview_image_url"), ::OpenAPI::toJsonValue(m_source_file_preview_image_url));
    }
    if (m_source_file_width_isSet) {
        obj.insert(QString("source_file_width"), ::OpenAPI::toJsonValue(m_source_file_width));
    }
    if (m_source_url_isSet) {
        obj.insert(QString("source_url"), ::OpenAPI::toJsonValue(m_source_url));
    }
    return obj;
}

QString OAI_medias_post_request_payload_data_attributes::getCreatedAt() const {
    return m_created_at;
}
void OAI_medias_post_request_payload_data_attributes::setCreatedAt(const QString &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAI_medias_post_request_payload_data_attributes::getDescription() const {
    return m_description;
}
void OAI_medias_post_request_payload_data_attributes::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_description_Set() const{
    return m_description_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_description_Valid() const{
    return m_description_isValid;
}

QString OAI_medias_post_request_payload_data_attributes::getExternalId() const {
    return m_external_id;
}
void OAI_medias_post_request_payload_data_attributes::setExternalId(const QString &external_id) {
    m_external_id = external_id;
    m_external_id_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_external_id_Set() const{
    return m_external_id_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_external_id_Valid() const{
    return m_external_id_isValid;
}

bool OAI_medias_post_request_payload_data_attributes::isHasFetchError() const {
    return m_has_fetch_error;
}
void OAI_medias_post_request_payload_data_attributes::setHasFetchError(const bool &has_fetch_error) {
    m_has_fetch_error = has_fetch_error;
    m_has_fetch_error_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_has_fetch_error_Set() const{
    return m_has_fetch_error_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_has_fetch_error_Valid() const{
    return m_has_fetch_error_isValid;
}

bool OAI_medias_post_request_payload_data_attributes::isIsProcessing() const {
    return m_is_processing;
}
void OAI_medias_post_request_payload_data_attributes::setIsProcessing(const bool &is_processing) {
    m_is_processing = is_processing;
    m_is_processing_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_is_processing_Set() const{
    return m_is_processing_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_is_processing_Valid() const{
    return m_is_processing_isValid;
}

QString OAI_medias_post_request_payload_data_attributes::getName() const {
    return m_name;
}
void OAI_medias_post_request_payload_data_attributes::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_name_Set() const{
    return m_name_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_name_Valid() const{
    return m_name_isValid;
}

QString OAI_medias_post_request_payload_data_attributes::getOriginalCreatedAt() const {
    return m_original_created_at;
}
void OAI_medias_post_request_payload_data_attributes::setOriginalCreatedAt(const QString &original_created_at) {
    m_original_created_at = original_created_at;
    m_original_created_at_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_original_created_at_Set() const{
    return m_original_created_at_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_original_created_at_Valid() const{
    return m_original_created_at_isValid;
}

QString OAI_medias_post_request_payload_data_attributes::getProcessingStartedAt() const {
    return m_processing_started_at;
}
void OAI_medias_post_request_payload_data_attributes::setProcessingStartedAt(const QString &processing_started_at) {
    m_processing_started_at = processing_started_at;
    m_processing_started_at_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_processing_started_at_Set() const{
    return m_processing_started_at_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_processing_started_at_Valid() const{
    return m_processing_started_at_isValid;
}

QString OAI_medias_post_request_payload_data_attributes::getSourceCreatedAt() const {
    return m_source_created_at;
}
void OAI_medias_post_request_payload_data_attributes::setSourceCreatedAt(const QString &source_created_at) {
    m_source_created_at = source_created_at;
    m_source_created_at_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_created_at_Set() const{
    return m_source_created_at_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_created_at_Valid() const{
    return m_source_created_at_isValid;
}

QString OAI_medias_post_request_payload_data_attributes::getSourceFileContentType() const {
    return m_source_file_content_type;
}
void OAI_medias_post_request_payload_data_attributes::setSourceFileContentType(const QString &source_file_content_type) {
    m_source_file_content_type = source_file_content_type;
    m_source_file_content_type_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_file_content_type_Set() const{
    return m_source_file_content_type_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_file_content_type_Valid() const{
    return m_source_file_content_type_isValid;
}

double OAI_medias_post_request_payload_data_attributes::getSourceFileDuration() const {
    return m_source_file_duration;
}
void OAI_medias_post_request_payload_data_attributes::setSourceFileDuration(const double &source_file_duration) {
    m_source_file_duration = source_file_duration;
    m_source_file_duration_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_file_duration_Set() const{
    return m_source_file_duration_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_file_duration_Valid() const{
    return m_source_file_duration_isValid;
}

double OAI_medias_post_request_payload_data_attributes::getSourceFileHeight() const {
    return m_source_file_height;
}
void OAI_medias_post_request_payload_data_attributes::setSourceFileHeight(const double &source_file_height) {
    m_source_file_height = source_file_height;
    m_source_file_height_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_file_height_Set() const{
    return m_source_file_height_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_file_height_Valid() const{
    return m_source_file_height_isValid;
}

QString OAI_medias_post_request_payload_data_attributes::getSourceFilePreviewImageUrl() const {
    return m_source_file_preview_image_url;
}
void OAI_medias_post_request_payload_data_attributes::setSourceFilePreviewImageUrl(const QString &source_file_preview_image_url) {
    m_source_file_preview_image_url = source_file_preview_image_url;
    m_source_file_preview_image_url_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_file_preview_image_url_Set() const{
    return m_source_file_preview_image_url_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_file_preview_image_url_Valid() const{
    return m_source_file_preview_image_url_isValid;
}

double OAI_medias_post_request_payload_data_attributes::getSourceFileWidth() const {
    return m_source_file_width;
}
void OAI_medias_post_request_payload_data_attributes::setSourceFileWidth(const double &source_file_width) {
    m_source_file_width = source_file_width;
    m_source_file_width_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_file_width_Set() const{
    return m_source_file_width_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_file_width_Valid() const{
    return m_source_file_width_isValid;
}

QString OAI_medias_post_request_payload_data_attributes::getSourceUrl() const {
    return m_source_url;
}
void OAI_medias_post_request_payload_data_attributes::setSourceUrl(const QString &source_url) {
    m_source_url = source_url;
    m_source_url_isSet = true;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_url_Set() const{
    return m_source_url_isSet;
}

bool OAI_medias_post_request_payload_data_attributes::is_source_url_Valid() const{
    return m_source_url_isValid;
}

bool OAI_medias_post_request_payload_data_attributes::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_fetch_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_processing_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_original_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_processing_started_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_file_content_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_file_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_file_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_file_preview_image_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_file_width_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_medias_post_request_payload_data_attributes::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
