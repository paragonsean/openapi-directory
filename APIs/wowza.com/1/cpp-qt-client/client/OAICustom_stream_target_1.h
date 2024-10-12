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
 * OAICustom_stream_target_1.h
 *
 * 
 */

#ifndef OAICustom_stream_target_1_H
#define OAICustom_stream_target_1_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICustom_stream_target_1 : public OAIObject {
public:
    OAICustom_stream_target_1();
    OAICustom_stream_target_1(QString json);
    ~OAICustom_stream_target_1() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isEnableHls() const;
    void setEnableHls(const bool &enable_hls);
    bool is_enable_hls_Set() const;
    bool is_enable_hls_Valid() const;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    QList<QString> getIngestIpWhitelist() const;
    void setIngestIpWhitelist(const QList<QString> &ingest_ip_whitelist);
    bool is_ingest_ip_whitelist_Set() const;
    bool is_ingest_ip_whitelist_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getProvider() const;
    void setProvider(const QString &provider);
    bool is_provider_Set() const;
    bool is_provider_Valid() const;

    QString getRegionOverride() const;
    void setRegionOverride(const QString &region_override);
    bool is_region_override_Set() const;
    bool is_region_override_Valid() const;

    QString getSourceDeliveryMethod() const;
    void setSourceDeliveryMethod(const QString &source_delivery_method);
    bool is_source_delivery_method_Set() const;
    bool is_source_delivery_method_Valid() const;

    QString getSourceUrl() const;
    void setSourceUrl(const QString &source_url);
    bool is_source_url_Set() const;
    bool is_source_url_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_enable_hls;
    bool m_enable_hls_isSet;
    bool m_enable_hls_isValid;

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;

    QList<QString> m_ingest_ip_whitelist;
    bool m_ingest_ip_whitelist_isSet;
    bool m_ingest_ip_whitelist_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_provider;
    bool m_provider_isSet;
    bool m_provider_isValid;

    QString m_region_override;
    bool m_region_override_isSet;
    bool m_region_override_isValid;

    QString m_source_delivery_method;
    bool m_source_delivery_method_isSet;
    bool m_source_delivery_method_isValid;

    QString m_source_url;
    bool m_source_url_isSet;
    bool m_source_url_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICustom_stream_target_1)

#endif // OAICustom_stream_target_1_H
