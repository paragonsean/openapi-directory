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
 * OAIUnknownTarget.h
 *
 * Storage container for use as an Unknown Storage Target.
 */

#ifndef OAIUnknownTarget_H
#define OAIUnknownTarget_H

#include <QJsonObject>

#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUnknownTarget : public OAIObject {
public:
    OAIUnknownTarget();
    OAIUnknownTarget(QString json);
    ~OAIUnknownTarget() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QMap<QString, QString> getUnknownMap() const;
    void setUnknownMap(const QMap<QString, QString> &unknown_map);
    bool is_unknown_map_Set() const;
    bool is_unknown_map_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QMap<QString, QString> m_unknown_map;
    bool m_unknown_map_isSet;
    bool m_unknown_map_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUnknownTarget)

#endif // OAIUnknownTarget_H
