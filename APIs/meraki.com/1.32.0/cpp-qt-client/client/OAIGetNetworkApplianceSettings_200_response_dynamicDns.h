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
 * OAIGetNetworkApplianceSettings_200_response_dynamicDns.h
 *
 * Dynamic DNS settings for a network
 */

#ifndef OAIGetNetworkApplianceSettings_200_response_dynamicDns_H
#define OAIGetNetworkApplianceSettings_200_response_dynamicDns_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetNetworkApplianceSettings_200_response_dynamicDns : public OAIObject {
public:
    OAIGetNetworkApplianceSettings_200_response_dynamicDns();
    OAIGetNetworkApplianceSettings_200_response_dynamicDns(QString json);
    ~OAIGetNetworkApplianceSettings_200_response_dynamicDns() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    QString getPrefix() const;
    void setPrefix(const QString &prefix);
    bool is_prefix_Set() const;
    bool is_prefix_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;

    QString m_prefix;
    bool m_prefix_isSet;
    bool m_prefix_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkApplianceSettings_200_response_dynamicDns)

#endif // OAIGetNetworkApplianceSettings_200_response_dynamicDns_H
