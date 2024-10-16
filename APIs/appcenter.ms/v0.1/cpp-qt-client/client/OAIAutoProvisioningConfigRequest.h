/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAutoProvisioningConfigRequest.h
 *
 * A request containing information for creating a Auto Provisioning Config.
 */

#ifndef OAIAutoProvisioningConfigRequest_H
#define OAIAutoProvisioningConfigRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAutoProvisioningConfigRequest : public OAIObject {
public:
    OAIAutoProvisioningConfigRequest();
    OAIAutoProvisioningConfigRequest(QString json);
    ~OAIAutoProvisioningConfigRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAllowAutoProvisioning() const;
    void setAllowAutoProvisioning(const bool &allow_auto_provisioning);
    bool is_allow_auto_provisioning_Set() const;
    bool is_allow_auto_provisioning_Valid() const;

    QString getAppleDeveloperAccountKey() const;
    void setAppleDeveloperAccountKey(const QString &apple_developer_account_key);
    bool is_apple_developer_account_key_Set() const;
    bool is_apple_developer_account_key_Valid() const;

    QString getAppleDistributionCertificateKey() const;
    void setAppleDistributionCertificateKey(const QString &apple_distribution_certificate_key);
    bool is_apple_distribution_certificate_key_Set() const;
    bool is_apple_distribution_certificate_key_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_allow_auto_provisioning;
    bool m_allow_auto_provisioning_isSet;
    bool m_allow_auto_provisioning_isValid;

    QString m_apple_developer_account_key;
    bool m_apple_developer_account_key_isSet;
    bool m_apple_developer_account_key_isValid;

    QString m_apple_distribution_certificate_key;
    bool m_apple_distribution_certificate_key_isSet;
    bool m_apple_distribution_certificate_key_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAutoProvisioningConfigRequest)

#endif // OAIAutoProvisioningConfigRequest_H
