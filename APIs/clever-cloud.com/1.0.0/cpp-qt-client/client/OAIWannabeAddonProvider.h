/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIWannabeAddonProvider.h
 *
 * 
 */

#ifndef OAIWannabeAddonProvider_H
#define OAIWannabeAddonProvider_H

#include <QJsonObject>

#include "OAIWannabeAddonProviderAPI.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIWannabeAddonProviderAPI;

class OAIWannabeAddonProvider : public OAIObject {
public:
    OAIWannabeAddonProvider();
    OAIWannabeAddonProvider(QString json);
    ~OAIWannabeAddonProvider() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIWannabeAddonProviderAPI getApi() const;
    void setApi(const OAIWannabeAddonProviderAPI &api);
    bool is_api_Set() const;
    bool is_api_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIWannabeAddonProviderAPI m_api;
    bool m_api_isSet;
    bool m_api_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWannabeAddonProvider)

#endif // OAIWannabeAddonProvider_H
