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
 * OAIRedisAccessKeys.h
 *
 * Redis cache access keys.
 */

#ifndef OAIRedisAccessKeys_H
#define OAIRedisAccessKeys_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIRedisAccessKeys : public OAIObject {
public:
    OAIRedisAccessKeys();
    OAIRedisAccessKeys(QString json);
    ~OAIRedisAccessKeys() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getPrimaryKey() const;
    void setPrimaryKey(const QString &primary_key);
    bool is_primary_key_Set() const;
    bool is_primary_key_Valid() const;

    QString getSecondaryKey() const;
    void setSecondaryKey(const QString &secondary_key);
    bool is_secondary_key_Set() const;
    bool is_secondary_key_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_primary_key;
    bool m_primary_key_isSet;
    bool m_primary_key_isValid;

    QString m_secondary_key;
    bool m_secondary_key_isSet;
    bool m_secondary_key_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRedisAccessKeys)

#endif // OAIRedisAccessKeys_H
