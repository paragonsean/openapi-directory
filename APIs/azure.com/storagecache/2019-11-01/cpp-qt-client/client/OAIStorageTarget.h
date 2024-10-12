/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage Caches.
 *
 * The version of the OpenAPI document: 2019-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIStorageTarget.h
 *
 * A storage system being cached by a Cache.
 */

#ifndef OAIStorageTarget_H
#define OAIStorageTarget_H

#include <QJsonObject>

#include "OAIStorageTarget_properties.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIStorageTarget_properties;

class OAIStorageTarget : public OAIObject {
public:
    OAIStorageTarget();
    OAIStorageTarget(QString json);
    ~OAIStorageTarget() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    OAIStorageTarget_properties getProperties() const;
    void setProperties(const OAIStorageTarget_properties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    OAIStorageTarget_properties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStorageTarget)

#endif // OAIStorageTarget_H
