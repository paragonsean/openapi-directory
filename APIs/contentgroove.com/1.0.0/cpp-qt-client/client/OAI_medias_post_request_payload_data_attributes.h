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

/*
 * OAI_medias_post_request_payload_data_attributes.h
 *
 * 
 */

#ifndef OAI_medias_post_request_payload_data_attributes_H
#define OAI_medias_post_request_payload_data_attributes_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAI_medias_post_request_payload_data_attributes : public OAIObject {
public:
    OAI_medias_post_request_payload_data_attributes();
    OAI_medias_post_request_payload_data_attributes(QString json);
    ~OAI_medias_post_request_payload_data_attributes() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getExternalId() const;
    void setExternalId(const QString &external_id);
    bool is_external_id_Set() const;
    bool is_external_id_Valid() const;

    bool isHasFetchError() const;
    void setHasFetchError(const bool &has_fetch_error);
    bool is_has_fetch_error_Set() const;
    bool is_has_fetch_error_Valid() const;

    bool isIsProcessing() const;
    void setIsProcessing(const bool &is_processing);
    bool is_is_processing_Set() const;
    bool is_is_processing_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOriginalCreatedAt() const;
    void setOriginalCreatedAt(const QString &original_created_at);
    bool is_original_created_at_Set() const;
    bool is_original_created_at_Valid() const;

    QString getProcessingStartedAt() const;
    void setProcessingStartedAt(const QString &processing_started_at);
    bool is_processing_started_at_Set() const;
    bool is_processing_started_at_Valid() const;

    QString getSourceCreatedAt() const;
    void setSourceCreatedAt(const QString &source_created_at);
    bool is_source_created_at_Set() const;
    bool is_source_created_at_Valid() const;

    QString getSourceFileContentType() const;
    void setSourceFileContentType(const QString &source_file_content_type);
    bool is_source_file_content_type_Set() const;
    bool is_source_file_content_type_Valid() const;

    double getSourceFileDuration() const;
    void setSourceFileDuration(const double &source_file_duration);
    bool is_source_file_duration_Set() const;
    bool is_source_file_duration_Valid() const;

    double getSourceFileHeight() const;
    void setSourceFileHeight(const double &source_file_height);
    bool is_source_file_height_Set() const;
    bool is_source_file_height_Valid() const;

    QString getSourceFilePreviewImageUrl() const;
    void setSourceFilePreviewImageUrl(const QString &source_file_preview_image_url);
    bool is_source_file_preview_image_url_Set() const;
    bool is_source_file_preview_image_url_Valid() const;

    double getSourceFileWidth() const;
    void setSourceFileWidth(const double &source_file_width);
    bool is_source_file_width_Set() const;
    bool is_source_file_width_Valid() const;

    QString getSourceUrl() const;
    void setSourceUrl(const QString &source_url);
    bool is_source_url_Set() const;
    bool is_source_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_external_id;
    bool m_external_id_isSet;
    bool m_external_id_isValid;

    bool m_has_fetch_error;
    bool m_has_fetch_error_isSet;
    bool m_has_fetch_error_isValid;

    bool m_is_processing;
    bool m_is_processing_isSet;
    bool m_is_processing_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_original_created_at;
    bool m_original_created_at_isSet;
    bool m_original_created_at_isValid;

    QString m_processing_started_at;
    bool m_processing_started_at_isSet;
    bool m_processing_started_at_isValid;

    QString m_source_created_at;
    bool m_source_created_at_isSet;
    bool m_source_created_at_isValid;

    QString m_source_file_content_type;
    bool m_source_file_content_type_isSet;
    bool m_source_file_content_type_isValid;

    double m_source_file_duration;
    bool m_source_file_duration_isSet;
    bool m_source_file_duration_isValid;

    double m_source_file_height;
    bool m_source_file_height_isSet;
    bool m_source_file_height_isValid;

    QString m_source_file_preview_image_url;
    bool m_source_file_preview_image_url_isSet;
    bool m_source_file_preview_image_url_isValid;

    double m_source_file_width;
    bool m_source_file_width_isSet;
    bool m_source_file_width_isValid;

    QString m_source_url;
    bool m_source_url_isSet;
    bool m_source_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_medias_post_request_payload_data_attributes)

#endif // OAI_medias_post_request_payload_data_attributes_H
