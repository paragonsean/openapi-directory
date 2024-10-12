/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICertificateProperties.h
 *
 * Certificate properties.
 */

#ifndef OAICertificateProperties_H
#define OAICertificateProperties_H

#include <QJsonObject>

#include "OAIDeleteCertificateError.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDeleteCertificateError;

class OAICertificateProperties : public OAIObject {
public:
    OAICertificateProperties();
    OAICertificateProperties(QString json);
    ~OAICertificateProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIDeleteCertificateError getDeleteCertificateError() const;
    void setDeleteCertificateError(const OAIDeleteCertificateError &delete_certificate_error);
    bool is_delete_certificate_error_Set() const;
    bool is_delete_certificate_error_Valid() const;

    QString getPreviousProvisioningState() const;
    void setPreviousProvisioningState(const QString &previous_provisioning_state);
    bool is_previous_provisioning_state_Set() const;
    bool is_previous_provisioning_state_Valid() const;

    QDateTime getPreviousProvisioningStateTransitionTime() const;
    void setPreviousProvisioningStateTransitionTime(const QDateTime &previous_provisioning_state_transition_time);
    bool is_previous_provisioning_state_transition_time_Set() const;
    bool is_previous_provisioning_state_transition_time_Valid() const;

    QString getProvisioningState() const;
    void setProvisioningState(const QString &provisioning_state);
    bool is_provisioning_state_Set() const;
    bool is_provisioning_state_Valid() const;

    QDateTime getProvisioningStateTransitionTime() const;
    void setProvisioningStateTransitionTime(const QDateTime &provisioning_state_transition_time);
    bool is_provisioning_state_transition_time_Set() const;
    bool is_provisioning_state_transition_time_Valid() const;

    QString getPublicData() const;
    void setPublicData(const QString &public_data);
    bool is_public_data_Set() const;
    bool is_public_data_Valid() const;

    QString getFormat() const;
    void setFormat(const QString &format);
    bool is_format_Set() const;
    bool is_format_Valid() const;

    QString getThumbprint() const;
    void setThumbprint(const QString &thumbprint);
    bool is_thumbprint_Set() const;
    bool is_thumbprint_Valid() const;

    QString getThumbprintAlgorithm() const;
    void setThumbprintAlgorithm(const QString &thumbprint_algorithm);
    bool is_thumbprint_algorithm_Set() const;
    bool is_thumbprint_algorithm_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIDeleteCertificateError m_delete_certificate_error;
    bool m_delete_certificate_error_isSet;
    bool m_delete_certificate_error_isValid;

    QString m_previous_provisioning_state;
    bool m_previous_provisioning_state_isSet;
    bool m_previous_provisioning_state_isValid;

    QDateTime m_previous_provisioning_state_transition_time;
    bool m_previous_provisioning_state_transition_time_isSet;
    bool m_previous_provisioning_state_transition_time_isValid;

    QString m_provisioning_state;
    bool m_provisioning_state_isSet;
    bool m_provisioning_state_isValid;

    QDateTime m_provisioning_state_transition_time;
    bool m_provisioning_state_transition_time_isSet;
    bool m_provisioning_state_transition_time_isValid;

    QString m_public_data;
    bool m_public_data_isSet;
    bool m_public_data_isValid;

    QString m_format;
    bool m_format_isSet;
    bool m_format_isValid;

    QString m_thumbprint;
    bool m_thumbprint_isSet;
    bool m_thumbprint_isValid;

    QString m_thumbprint_algorithm;
    bool m_thumbprint_algorithm_isSet;
    bool m_thumbprint_algorithm_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICertificateProperties)

#endif // OAICertificateProperties_H
