/**
 * Wowza Streaming Cloud REST API Reference Documentation
 *  # About the REST API  The Wowza Streaming Cloud<sup>TM</sup> REST API (application programming interface) offers complete programmatic control over live streams, transcoders, stream sources, and stream targets. Anything you can do in the Wowza Streaming Cloud UI can also be achieved by making HTTP-based requests to cloud-based servers through the REST API.  The Wowza Streaming Cloud REST API features *cross-origin resource sharing*, or CORS. CORS is a [W3C specification](https://www.w3.org/TR/cors/) that provides headers in HTTP requests to enable a web server to safely make a network request to another domain.  In order to protect shared resources, the Wowza Streaming Cloud REST API is subject to limits. For details, see [Wowza Streaming Cloud REST API limits](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api-limits). # About this documentation This reference documentation is based on the open-source [Swagger framework](http://swagger.io/specification/). It allows you to view the operations, parameters, and request and reponse schemas for every resource. Request samples are presented in cURL (Shell) and JavaScript; some samples also include just the JSON object. Response samples are all JSON.  For more information and examples on using the Wowza Streaming Cloud REST API, see our [library of Wowza Streaming Cloud REST API technical articles](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api).  # Query requirements The Wowza Streaming Cloud REST API uses HTTP requests to retrieve data from cloud-based servers. Requests must contain proper JSON, two authentication keys, and the correct version number in the base path.  ## JSON The Wowza Streaming Cloud REST API uses the [JSON API specification](http://jsonapi.org/format/) to request and return data. This means requests must include the header `Content-Type: application/json` and must include a single resource object in JSON format as primary data.  Responses include HTTP status codes that indicate whether the query was successful. If there was an error, a description explains the problem so that you can fix it and try again.  ## Authentication Requests to the Wowza Streaming Cloud REST API must be authenticated with two keys: an API key and an access key. Each key is a 64-character alphanumeric string that you can find on the **API Access** page in Wowza Streaming Cloud.  Use the `wsc-api-key` and `wsc-access-key` headers to authenticate requests, like this (in cURL):  ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]' ```  <!-- ReDoc-Inject: <security-definitions> -->  ## Version The Wowza Streaming Cloud API is currently at version 1.0.0. Use `v1` in your base path in every request, like this path to the live_streams endpoint: ``` https://api.cloud.wowza.com/api/v1/live_streams ``` ## Example query Here is a complete example POST request, in cURL, with proper JSON syntax, headers, authentication, and version information: ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]'   -H 'Content-Type: application/json' -X POST -d '{     \"live_stream\": {       \"name\": \"My live Stream\",       \"...\": \"...\"     }   }' https://api.cloud.wowza.com/api/v1/live_streams ``` 
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOutput.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOutput::OAIOutput(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOutput::OAIOutput() {
    this->initializeModel();
}

OAIOutput::~OAIOutput() {}

void OAIOutput::initializeModel() {

    m_aspect_ratio_height_isSet = false;
    m_aspect_ratio_height_isValid = false;

    m_aspect_ratio_width_isSet = false;
    m_aspect_ratio_width_isValid = false;

    m_bitrate_audio_isSet = false;
    m_bitrate_audio_isValid = false;

    m_bitrate_video_isSet = false;
    m_bitrate_video_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_framerate_reduction_isSet = false;
    m_framerate_reduction_isValid = false;

    m_h264_profile_isSet = false;
    m_h264_profile_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_keyframes_isSet = false;
    m_keyframes_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_output_stream_targets_isSet = false;
    m_output_stream_targets_isValid = false;

    m_passthrough_audio_isSet = false;
    m_passthrough_audio_isValid = false;

    m_passthrough_video_isSet = false;
    m_passthrough_video_isValid = false;

    m_stream_format_isSet = false;
    m_stream_format_isValid = false;

    m_transcoder_id_isSet = false;
    m_transcoder_id_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;
}

void OAIOutput::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOutput::fromJsonObject(QJsonObject json) {

    m_aspect_ratio_height_isValid = ::OpenAPI::fromJsonValue(m_aspect_ratio_height, json[QString("aspect_ratio_height")]);
    m_aspect_ratio_height_isSet = !json[QString("aspect_ratio_height")].isNull() && m_aspect_ratio_height_isValid;

    m_aspect_ratio_width_isValid = ::OpenAPI::fromJsonValue(m_aspect_ratio_width, json[QString("aspect_ratio_width")]);
    m_aspect_ratio_width_isSet = !json[QString("aspect_ratio_width")].isNull() && m_aspect_ratio_width_isValid;

    m_bitrate_audio_isValid = ::OpenAPI::fromJsonValue(m_bitrate_audio, json[QString("bitrate_audio")]);
    m_bitrate_audio_isSet = !json[QString("bitrate_audio")].isNull() && m_bitrate_audio_isValid;

    m_bitrate_video_isValid = ::OpenAPI::fromJsonValue(m_bitrate_video, json[QString("bitrate_video")]);
    m_bitrate_video_isSet = !json[QString("bitrate_video")].isNull() && m_bitrate_video_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_framerate_reduction_isValid = ::OpenAPI::fromJsonValue(m_framerate_reduction, json[QString("framerate_reduction")]);
    m_framerate_reduction_isSet = !json[QString("framerate_reduction")].isNull() && m_framerate_reduction_isValid;

    m_h264_profile_isValid = ::OpenAPI::fromJsonValue(m_h264_profile, json[QString("h264_profile")]);
    m_h264_profile_isSet = !json[QString("h264_profile")].isNull() && m_h264_profile_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_keyframes_isValid = ::OpenAPI::fromJsonValue(m_keyframes, json[QString("keyframes")]);
    m_keyframes_isSet = !json[QString("keyframes")].isNull() && m_keyframes_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_output_stream_targets_isValid = ::OpenAPI::fromJsonValue(m_output_stream_targets, json[QString("output_stream_targets")]);
    m_output_stream_targets_isSet = !json[QString("output_stream_targets")].isNull() && m_output_stream_targets_isValid;

    m_passthrough_audio_isValid = ::OpenAPI::fromJsonValue(m_passthrough_audio, json[QString("passthrough_audio")]);
    m_passthrough_audio_isSet = !json[QString("passthrough_audio")].isNull() && m_passthrough_audio_isValid;

    m_passthrough_video_isValid = ::OpenAPI::fromJsonValue(m_passthrough_video, json[QString("passthrough_video")]);
    m_passthrough_video_isSet = !json[QString("passthrough_video")].isNull() && m_passthrough_video_isValid;

    m_stream_format_isValid = ::OpenAPI::fromJsonValue(m_stream_format, json[QString("stream_format")]);
    m_stream_format_isSet = !json[QString("stream_format")].isNull() && m_stream_format_isValid;

    m_transcoder_id_isValid = ::OpenAPI::fromJsonValue(m_transcoder_id, json[QString("transcoder_id")]);
    m_transcoder_id_isSet = !json[QString("transcoder_id")].isNull() && m_transcoder_id_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;
}

QString OAIOutput::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOutput::asJsonObject() const {
    QJsonObject obj;
    if (m_aspect_ratio_height_isSet) {
        obj.insert(QString("aspect_ratio_height"), ::OpenAPI::toJsonValue(m_aspect_ratio_height));
    }
    if (m_aspect_ratio_width_isSet) {
        obj.insert(QString("aspect_ratio_width"), ::OpenAPI::toJsonValue(m_aspect_ratio_width));
    }
    if (m_bitrate_audio_isSet) {
        obj.insert(QString("bitrate_audio"), ::OpenAPI::toJsonValue(m_bitrate_audio));
    }
    if (m_bitrate_video_isSet) {
        obj.insert(QString("bitrate_video"), ::OpenAPI::toJsonValue(m_bitrate_video));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_framerate_reduction_isSet) {
        obj.insert(QString("framerate_reduction"), ::OpenAPI::toJsonValue(m_framerate_reduction));
    }
    if (m_h264_profile_isSet) {
        obj.insert(QString("h264_profile"), ::OpenAPI::toJsonValue(m_h264_profile));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_keyframes_isSet) {
        obj.insert(QString("keyframes"), ::OpenAPI::toJsonValue(m_keyframes));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_output_stream_targets.size() > 0) {
        obj.insert(QString("output_stream_targets"), ::OpenAPI::toJsonValue(m_output_stream_targets));
    }
    if (m_passthrough_audio_isSet) {
        obj.insert(QString("passthrough_audio"), ::OpenAPI::toJsonValue(m_passthrough_audio));
    }
    if (m_passthrough_video_isSet) {
        obj.insert(QString("passthrough_video"), ::OpenAPI::toJsonValue(m_passthrough_video));
    }
    if (m_stream_format_isSet) {
        obj.insert(QString("stream_format"), ::OpenAPI::toJsonValue(m_stream_format));
    }
    if (m_transcoder_id_isSet) {
        obj.insert(QString("transcoder_id"), ::OpenAPI::toJsonValue(m_transcoder_id));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    return obj;
}

qint32 OAIOutput::getAspectRatioHeight() const {
    return m_aspect_ratio_height;
}
void OAIOutput::setAspectRatioHeight(const qint32 &aspect_ratio_height) {
    m_aspect_ratio_height = aspect_ratio_height;
    m_aspect_ratio_height_isSet = true;
}

bool OAIOutput::is_aspect_ratio_height_Set() const{
    return m_aspect_ratio_height_isSet;
}

bool OAIOutput::is_aspect_ratio_height_Valid() const{
    return m_aspect_ratio_height_isValid;
}

qint32 OAIOutput::getAspectRatioWidth() const {
    return m_aspect_ratio_width;
}
void OAIOutput::setAspectRatioWidth(const qint32 &aspect_ratio_width) {
    m_aspect_ratio_width = aspect_ratio_width;
    m_aspect_ratio_width_isSet = true;
}

bool OAIOutput::is_aspect_ratio_width_Set() const{
    return m_aspect_ratio_width_isSet;
}

bool OAIOutput::is_aspect_ratio_width_Valid() const{
    return m_aspect_ratio_width_isValid;
}

qint32 OAIOutput::getBitrateAudio() const {
    return m_bitrate_audio;
}
void OAIOutput::setBitrateAudio(const qint32 &bitrate_audio) {
    m_bitrate_audio = bitrate_audio;
    m_bitrate_audio_isSet = true;
}

bool OAIOutput::is_bitrate_audio_Set() const{
    return m_bitrate_audio_isSet;
}

bool OAIOutput::is_bitrate_audio_Valid() const{
    return m_bitrate_audio_isValid;
}

qint32 OAIOutput::getBitrateVideo() const {
    return m_bitrate_video;
}
void OAIOutput::setBitrateVideo(const qint32 &bitrate_video) {
    m_bitrate_video = bitrate_video;
    m_bitrate_video_isSet = true;
}

bool OAIOutput::is_bitrate_video_Set() const{
    return m_bitrate_video_isSet;
}

bool OAIOutput::is_bitrate_video_Valid() const{
    return m_bitrate_video_isValid;
}

QDateTime OAIOutput::getCreatedAt() const {
    return m_created_at;
}
void OAIOutput::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIOutput::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIOutput::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIOutput::getFramerateReduction() const {
    return m_framerate_reduction;
}
void OAIOutput::setFramerateReduction(const QString &framerate_reduction) {
    m_framerate_reduction = framerate_reduction;
    m_framerate_reduction_isSet = true;
}

bool OAIOutput::is_framerate_reduction_Set() const{
    return m_framerate_reduction_isSet;
}

bool OAIOutput::is_framerate_reduction_Valid() const{
    return m_framerate_reduction_isValid;
}

QString OAIOutput::getH264Profile() const {
    return m_h264_profile;
}
void OAIOutput::setH264Profile(const QString &h264_profile) {
    m_h264_profile = h264_profile;
    m_h264_profile_isSet = true;
}

bool OAIOutput::is_h264_profile_Set() const{
    return m_h264_profile_isSet;
}

bool OAIOutput::is_h264_profile_Valid() const{
    return m_h264_profile_isValid;
}

QString OAIOutput::getId() const {
    return m_id;
}
void OAIOutput::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOutput::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOutput::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIOutput::getKeyframes() const {
    return m_keyframes;
}
void OAIOutput::setKeyframes(const QString &keyframes) {
    m_keyframes = keyframes;
    m_keyframes_isSet = true;
}

bool OAIOutput::is_keyframes_Set() const{
    return m_keyframes_isSet;
}

bool OAIOutput::is_keyframes_Valid() const{
    return m_keyframes_isValid;
}

QString OAIOutput::getName() const {
    return m_name;
}
void OAIOutput::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIOutput::is_name_Set() const{
    return m_name_isSet;
}

bool OAIOutput::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIOutput_stream_target> OAIOutput::getOutputStreamTargets() const {
    return m_output_stream_targets;
}
void OAIOutput::setOutputStreamTargets(const QList<OAIOutput_stream_target> &output_stream_targets) {
    m_output_stream_targets = output_stream_targets;
    m_output_stream_targets_isSet = true;
}

bool OAIOutput::is_output_stream_targets_Set() const{
    return m_output_stream_targets_isSet;
}

bool OAIOutput::is_output_stream_targets_Valid() const{
    return m_output_stream_targets_isValid;
}

bool OAIOutput::isPassthroughAudio() const {
    return m_passthrough_audio;
}
void OAIOutput::setPassthroughAudio(const bool &passthrough_audio) {
    m_passthrough_audio = passthrough_audio;
    m_passthrough_audio_isSet = true;
}

bool OAIOutput::is_passthrough_audio_Set() const{
    return m_passthrough_audio_isSet;
}

bool OAIOutput::is_passthrough_audio_Valid() const{
    return m_passthrough_audio_isValid;
}

bool OAIOutput::isPassthroughVideo() const {
    return m_passthrough_video;
}
void OAIOutput::setPassthroughVideo(const bool &passthrough_video) {
    m_passthrough_video = passthrough_video;
    m_passthrough_video_isSet = true;
}

bool OAIOutput::is_passthrough_video_Set() const{
    return m_passthrough_video_isSet;
}

bool OAIOutput::is_passthrough_video_Valid() const{
    return m_passthrough_video_isValid;
}

QString OAIOutput::getStreamFormat() const {
    return m_stream_format;
}
void OAIOutput::setStreamFormat(const QString &stream_format) {
    m_stream_format = stream_format;
    m_stream_format_isSet = true;
}

bool OAIOutput::is_stream_format_Set() const{
    return m_stream_format_isSet;
}

bool OAIOutput::is_stream_format_Valid() const{
    return m_stream_format_isValid;
}

QString OAIOutput::getTranscoderId() const {
    return m_transcoder_id;
}
void OAIOutput::setTranscoderId(const QString &transcoder_id) {
    m_transcoder_id = transcoder_id;
    m_transcoder_id_isSet = true;
}

bool OAIOutput::is_transcoder_id_Set() const{
    return m_transcoder_id_isSet;
}

bool OAIOutput::is_transcoder_id_Valid() const{
    return m_transcoder_id_isValid;
}

QDateTime OAIOutput::getUpdatedAt() const {
    return m_updated_at;
}
void OAIOutput::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIOutput::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIOutput::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

bool OAIOutput::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_aspect_ratio_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_aspect_ratio_width_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bitrate_audio_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bitrate_video_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_framerate_reduction_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_h264_profile_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_keyframes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_output_stream_targets.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_passthrough_audio_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passthrough_video_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stream_format_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transcoder_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOutput::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
