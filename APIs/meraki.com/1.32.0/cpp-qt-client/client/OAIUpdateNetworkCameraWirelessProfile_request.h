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
 * OAIUpdateNetworkCameraWirelessProfile_request.h
 *
 * 
 */

#ifndef OAIUpdateNetworkCameraWirelessProfile_request_H
#define OAIUpdateNetworkCameraWirelessProfile_request_H

#include <QJsonObject>

#include "OAICreateNetworkCameraWirelessProfile_request_identity.h"
#include "OAICreateNetworkCameraWirelessProfile_request_ssid.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICreateNetworkCameraWirelessProfile_request_identity;
class OAICreateNetworkCameraWirelessProfile_request_ssid;

class OAIUpdateNetworkCameraWirelessProfile_request : public OAIObject {
public:
    OAIUpdateNetworkCameraWirelessProfile_request();
    OAIUpdateNetworkCameraWirelessProfile_request(QString json);
    ~OAIUpdateNetworkCameraWirelessProfile_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICreateNetworkCameraWirelessProfile_request_identity getIdentity() const;
    void setIdentity(const OAICreateNetworkCameraWirelessProfile_request_identity &identity);
    bool is_identity_Set() const;
    bool is_identity_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    OAICreateNetworkCameraWirelessProfile_request_ssid getSsid() const;
    void setSsid(const OAICreateNetworkCameraWirelessProfile_request_ssid &ssid);
    bool is_ssid_Set() const;
    bool is_ssid_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICreateNetworkCameraWirelessProfile_request_identity m_identity;
    bool m_identity_isSet;
    bool m_identity_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    OAICreateNetworkCameraWirelessProfile_request_ssid m_ssid;
    bool m_ssid_isSet;
    bool m_ssid_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkCameraWirelessProfile_request)

#endif // OAIUpdateNetworkCameraWirelessProfile_request_H
