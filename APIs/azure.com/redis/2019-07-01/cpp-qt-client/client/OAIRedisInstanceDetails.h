/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2019-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRedisInstanceDetails.h
 *
 * Details of single instance of redis.
 */

#ifndef OAIRedisInstanceDetails_H
#define OAIRedisInstanceDetails_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIRedisInstanceDetails : public OAIObject {
public:
    OAIRedisInstanceDetails();
    OAIRedisInstanceDetails(QString json);
    ~OAIRedisInstanceDetails() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getNonSslPort() const;
    void setNonSslPort(const qint32 &non_ssl_port);
    bool is_non_ssl_port_Set() const;
    bool is_non_ssl_port_Valid() const;

    qint32 getShardId() const;
    void setShardId(const qint32 &shard_id);
    bool is_shard_id_Set() const;
    bool is_shard_id_Valid() const;

    qint32 getSslPort() const;
    void setSslPort(const qint32 &ssl_port);
    bool is_ssl_port_Set() const;
    bool is_ssl_port_Valid() const;

    QString getZone() const;
    void setZone(const QString &zone);
    bool is_zone_Set() const;
    bool is_zone_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_non_ssl_port;
    bool m_non_ssl_port_isSet;
    bool m_non_ssl_port_isValid;

    qint32 m_shard_id;
    bool m_shard_id_isSet;
    bool m_shard_id_isValid;

    qint32 m_ssl_port;
    bool m_ssl_port_isSet;
    bool m_ssl_port_isValid;

    QString m_zone;
    bool m_zone_isSet;
    bool m_zone_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRedisInstanceDetails)

#endif // OAIRedisInstanceDetails_H
