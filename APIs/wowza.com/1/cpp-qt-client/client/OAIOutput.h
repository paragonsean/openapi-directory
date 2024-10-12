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

/*
 * OAIOutput.h
 *
 * 
 */

#ifndef OAIOutput_H
#define OAIOutput_H

#include <QJsonObject>

#include "OAIOutput_stream_target.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIOutput_stream_target;

class OAIOutput : public OAIObject {
public:
    OAIOutput();
    OAIOutput(QString json);
    ~OAIOutput() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAspectRatioHeight() const;
    void setAspectRatioHeight(const qint32 &aspect_ratio_height);
    bool is_aspect_ratio_height_Set() const;
    bool is_aspect_ratio_height_Valid() const;

    qint32 getAspectRatioWidth() const;
    void setAspectRatioWidth(const qint32 &aspect_ratio_width);
    bool is_aspect_ratio_width_Set() const;
    bool is_aspect_ratio_width_Valid() const;

    qint32 getBitrateAudio() const;
    void setBitrateAudio(const qint32 &bitrate_audio);
    bool is_bitrate_audio_Set() const;
    bool is_bitrate_audio_Valid() const;

    qint32 getBitrateVideo() const;
    void setBitrateVideo(const qint32 &bitrate_video);
    bool is_bitrate_video_Set() const;
    bool is_bitrate_video_Valid() const;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getFramerateReduction() const;
    void setFramerateReduction(const QString &framerate_reduction);
    bool is_framerate_reduction_Set() const;
    bool is_framerate_reduction_Valid() const;

    QString getH264Profile() const;
    void setH264Profile(const QString &h264_profile);
    bool is_h264_profile_Set() const;
    bool is_h264_profile_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getKeyframes() const;
    void setKeyframes(const QString &keyframes);
    bool is_keyframes_Set() const;
    bool is_keyframes_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAIOutput_stream_target> getOutputStreamTargets() const;
    void setOutputStreamTargets(const QList<OAIOutput_stream_target> &output_stream_targets);
    bool is_output_stream_targets_Set() const;
    bool is_output_stream_targets_Valid() const;

    bool isPassthroughAudio() const;
    void setPassthroughAudio(const bool &passthrough_audio);
    bool is_passthrough_audio_Set() const;
    bool is_passthrough_audio_Valid() const;

    bool isPassthroughVideo() const;
    void setPassthroughVideo(const bool &passthrough_video);
    bool is_passthrough_video_Set() const;
    bool is_passthrough_video_Valid() const;

    QString getStreamFormat() const;
    void setStreamFormat(const QString &stream_format);
    bool is_stream_format_Set() const;
    bool is_stream_format_Valid() const;

    QString getTranscoderId() const;
    void setTranscoderId(const QString &transcoder_id);
    bool is_transcoder_id_Set() const;
    bool is_transcoder_id_Valid() const;

    QDateTime getUpdatedAt() const;
    void setUpdatedAt(const QDateTime &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_aspect_ratio_height;
    bool m_aspect_ratio_height_isSet;
    bool m_aspect_ratio_height_isValid;

    qint32 m_aspect_ratio_width;
    bool m_aspect_ratio_width_isSet;
    bool m_aspect_ratio_width_isValid;

    qint32 m_bitrate_audio;
    bool m_bitrate_audio_isSet;
    bool m_bitrate_audio_isValid;

    qint32 m_bitrate_video;
    bool m_bitrate_video_isSet;
    bool m_bitrate_video_isValid;

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_framerate_reduction;
    bool m_framerate_reduction_isSet;
    bool m_framerate_reduction_isValid;

    QString m_h264_profile;
    bool m_h264_profile_isSet;
    bool m_h264_profile_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_keyframes;
    bool m_keyframes_isSet;
    bool m_keyframes_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAIOutput_stream_target> m_output_stream_targets;
    bool m_output_stream_targets_isSet;
    bool m_output_stream_targets_isValid;

    bool m_passthrough_audio;
    bool m_passthrough_audio_isSet;
    bool m_passthrough_audio_isValid;

    bool m_passthrough_video;
    bool m_passthrough_video_isSet;
    bool m_passthrough_video_isValid;

    QString m_stream_format;
    bool m_stream_format_isSet;
    bool m_stream_format_isValid;

    QString m_transcoder_id;
    bool m_transcoder_id_isSet;
    bool m_transcoder_id_isValid;

    QDateTime m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOutput)

#endif // OAIOutput_H
