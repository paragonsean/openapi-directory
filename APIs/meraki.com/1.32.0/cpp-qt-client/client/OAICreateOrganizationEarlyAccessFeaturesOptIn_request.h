/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICreateOrganizationEarlyAccessFeaturesOptIn_request.h
 *
 * 
 */

#ifndef OAICreateOrganizationEarlyAccessFeaturesOptIn_request_H
#define OAICreateOrganizationEarlyAccessFeaturesOptIn_request_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICreateOrganizationEarlyAccessFeaturesOptIn_request : public OAIObject {
public:
    OAICreateOrganizationEarlyAccessFeaturesOptIn_request();
    OAICreateOrganizationEarlyAccessFeaturesOptIn_request(QString json);
    ~OAICreateOrganizationEarlyAccessFeaturesOptIn_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getLimitScopeToNetworks() const;
    void setLimitScopeToNetworks(const QList<QString> &limit_scope_to_networks);
    bool is_limit_scope_to_networks_Set() const;
    bool is_limit_scope_to_networks_Valid() const;

    QString getShortName() const;
    void setShortName(const QString &short_name);
    bool is_short_name_Set() const;
    bool is_short_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_limit_scope_to_networks;
    bool m_limit_scope_to_networks_isSet;
    bool m_limit_scope_to_networks_isValid;

    QString m_short_name;
    bool m_short_name_isSet;
    bool m_short_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateOrganizationEarlyAccessFeaturesOptIn_request)

#endif // OAICreateOrganizationEarlyAccessFeaturesOptIn_request_H
