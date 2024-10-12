/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBackendPoolsSettings.h
 *
 * Settings that apply to all backend pools.
 */

#ifndef OAIBackendPoolsSettings_H
#define OAIBackendPoolsSettings_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBackendPoolsSettings : public OAIObject {
public:
    OAIBackendPoolsSettings();
    OAIBackendPoolsSettings(QString json);
    ~OAIBackendPoolsSettings() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEnforceCertificateNameCheck() const;
    void setEnforceCertificateNameCheck(const QString &enforce_certificate_name_check);
    bool is_enforce_certificate_name_check_Set() const;
    bool is_enforce_certificate_name_check_Valid() const;

    qint32 getSendRecvTimeoutSeconds() const;
    void setSendRecvTimeoutSeconds(const qint32 &send_recv_timeout_seconds);
    bool is_send_recv_timeout_seconds_Set() const;
    bool is_send_recv_timeout_seconds_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_enforce_certificate_name_check;
    bool m_enforce_certificate_name_check_isSet;
    bool m_enforce_certificate_name_check_isValid;

    qint32 m_send_recv_timeout_seconds;
    bool m_send_recv_timeout_seconds_isSet;
    bool m_send_recv_timeout_seconds_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBackendPoolsSettings)

#endif // OAIBackendPoolsSettings_H
