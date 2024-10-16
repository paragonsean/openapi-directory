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
 * OAIGetNetworkWirelessSsidEapOverride_200_response.h
 *
 * 
 */

#ifndef OAIGetNetworkWirelessSsidEapOverride_200_response_H
#define OAIGetNetworkWirelessSsidEapOverride_200_response_H

#include <QJsonObject>

#include "OAIGetNetworkWirelessSsidEapOverride_200_response_eapolKey.h"
#include "OAIGetNetworkWirelessSsidEapOverride_200_response_identity.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetNetworkWirelessSsidEapOverride_200_response_eapolKey;
class OAIGetNetworkWirelessSsidEapOverride_200_response_identity;

class OAIGetNetworkWirelessSsidEapOverride_200_response : public OAIObject {
public:
    OAIGetNetworkWirelessSsidEapOverride_200_response();
    OAIGetNetworkWirelessSsidEapOverride_200_response(QString json);
    ~OAIGetNetworkWirelessSsidEapOverride_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGetNetworkWirelessSsidEapOverride_200_response_eapolKey getEapolKey() const;
    void setEapolKey(const OAIGetNetworkWirelessSsidEapOverride_200_response_eapolKey &eapol_key);
    bool is_eapol_key_Set() const;
    bool is_eapol_key_Valid() const;

    OAIGetNetworkWirelessSsidEapOverride_200_response_identity getIdentity() const;
    void setIdentity(const OAIGetNetworkWirelessSsidEapOverride_200_response_identity &identity);
    bool is_identity_Set() const;
    bool is_identity_Valid() const;

    qint32 getMaxRetries() const;
    void setMaxRetries(const qint32 &max_retries);
    bool is_max_retries_Set() const;
    bool is_max_retries_Valid() const;

    qint32 getTimeout() const;
    void setTimeout(const qint32 &timeout);
    bool is_timeout_Set() const;
    bool is_timeout_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGetNetworkWirelessSsidEapOverride_200_response_eapolKey m_eapol_key;
    bool m_eapol_key_isSet;
    bool m_eapol_key_isValid;

    OAIGetNetworkWirelessSsidEapOverride_200_response_identity m_identity;
    bool m_identity_isSet;
    bool m_identity_isValid;

    qint32 m_max_retries;
    bool m_max_retries_isSet;
    bool m_max_retries_isValid;

    qint32 m_timeout;
    bool m_timeout_isSet;
    bool m_timeout_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkWirelessSsidEapOverride_200_response)

#endif // OAIGetNetworkWirelessSsidEapOverride_200_response_H
