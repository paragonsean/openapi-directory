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
 * OAIIndex_stream_target.h
 *
 * 
 */

#ifndef OAIIndex_stream_target_H
#define OAIIndex_stream_target_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIIndex_stream_target : public OAIObject {
public:
    OAIIndex_stream_target();
    OAIIndex_stream_target(QString json);
    ~OAIIndex_stream_target() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getChunkSize() const;
    void setChunkSize(const QString &chunk_size);
    bool is_chunk_size_Set() const;
    bool is_chunk_size_Valid() const;

    QString getConnectionCode() const;
    void setConnectionCode(const QString &connection_code);
    bool is_connection_code_Set() const;
    bool is_connection_code_Valid() const;

    QDateTime getConnectionCodeExpiresAt() const;
    void setConnectionCodeExpiresAt(const QDateTime &connection_code_expires_at);
    bool is_connection_code_expires_at_Set() const;
    bool is_connection_code_expires_at_Valid() const;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getHdsPlaybackUrl() const;
    void setHdsPlaybackUrl(const QString &hds_playback_url);
    bool is_hds_playback_url_Set() const;
    bool is_hds_playback_url_Valid() const;

    QString getHlsPlaybackUrl() const;
    void setHlsPlaybackUrl(const QString &hls_playback_url);
    bool is_hls_playback_url_Set() const;
    bool is_hls_playback_url_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getLocation() const;
    void setLocation(const QString &location);
    bool is_location_Set() const;
    bool is_location_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPrimaryUrl() const;
    void setPrimaryUrl(const QString &primary_url);
    bool is_primary_url_Set() const;
    bool is_primary_url_Valid() const;

    QString getProvider() const;
    void setProvider(const QString &provider);
    bool is_provider_Set() const;
    bool is_provider_Valid() const;

    QString getRtmpPlaybackUrl() const;
    void setRtmpPlaybackUrl(const QString &rtmp_playback_url);
    bool is_rtmp_playback_url_Set() const;
    bool is_rtmp_playback_url_Valid() const;

    QString getStreamName() const;
    void setStreamName(const QString &stream_name);
    bool is_stream_name_Set() const;
    bool is_stream_name_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QDateTime getUpdatedAt() const;
    void setUpdatedAt(const QDateTime &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_chunk_size;
    bool m_chunk_size_isSet;
    bool m_chunk_size_isValid;

    QString m_connection_code;
    bool m_connection_code_isSet;
    bool m_connection_code_isValid;

    QDateTime m_connection_code_expires_at;
    bool m_connection_code_expires_at_isSet;
    bool m_connection_code_expires_at_isValid;

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_hds_playback_url;
    bool m_hds_playback_url_isSet;
    bool m_hds_playback_url_isValid;

    QString m_hls_playback_url;
    bool m_hls_playback_url_isSet;
    bool m_hls_playback_url_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_location;
    bool m_location_isSet;
    bool m_location_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_primary_url;
    bool m_primary_url_isSet;
    bool m_primary_url_isValid;

    QString m_provider;
    bool m_provider_isSet;
    bool m_provider_isValid;

    QString m_rtmp_playback_url;
    bool m_rtmp_playback_url_isSet;
    bool m_rtmp_playback_url_isValid;

    QString m_stream_name;
    bool m_stream_name_isSet;
    bool m_stream_name_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QDateTime m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIndex_stream_target)

#endif // OAIIndex_stream_target_H
