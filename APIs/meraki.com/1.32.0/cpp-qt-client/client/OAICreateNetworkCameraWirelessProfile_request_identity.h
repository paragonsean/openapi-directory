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
 * OAICreateNetworkCameraWirelessProfile_request_identity.h
 *
 * The identity of the wireless profile. Required for creating wireless profiles in 8021x-radius auth mode.
 */

#ifndef OAICreateNetworkCameraWirelessProfile_request_identity_H
#define OAICreateNetworkCameraWirelessProfile_request_identity_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICreateNetworkCameraWirelessProfile_request_identity : public OAIObject {
public:
    OAICreateNetworkCameraWirelessProfile_request_identity();
    OAICreateNetworkCameraWirelessProfile_request_identity(QString json);
    ~OAICreateNetworkCameraWirelessProfile_request_identity() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateNetworkCameraWirelessProfile_request_identity)

#endif // OAICreateNetworkCameraWirelessProfile_request_identity_H
