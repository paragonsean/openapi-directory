/**
 * SubscriptionsManagementClient
 * The Admin Subscriptions Management Client.
 *
 * The version of the OpenAPI document: 2015-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPlanAcquisition.h
 *
 * Represents the acquisition of an add-on plan for a subscription.
 */

#ifndef OAIPlanAcquisition_H
#define OAIPlanAcquisition_H

#include <QJsonObject>

#include "OAIProvisioningState.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPlanAcquisition : public OAIObject {
public:
    OAIPlanAcquisition();
    OAIPlanAcquisition(QString json);
    ~OAIPlanAcquisition() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAcquisitionId() const;
    void setAcquisitionId(const QString &acquisition_id);
    bool is_acquisition_id_Set() const;
    bool is_acquisition_id_Valid() const;

    QDateTime getAcquisitionTime() const;
    void setAcquisitionTime(const QDateTime &acquisition_time);
    bool is_acquisition_time_Set() const;
    bool is_acquisition_time_Valid() const;

    QString getExternalReferenceId() const;
    void setExternalReferenceId(const QString &external_reference_id);
    bool is_external_reference_id_Set() const;
    bool is_external_reference_id_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getPlanId() const;
    void setPlanId(const QString &plan_id);
    bool is_plan_id_Set() const;
    bool is_plan_id_Valid() const;

    OAIProvisioningState getProvisioningState() const;
    void setProvisioningState(const OAIProvisioningState &provisioning_state);
    bool is_provisioning_state_Set() const;
    bool is_provisioning_state_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_acquisition_id;
    bool m_acquisition_id_isSet;
    bool m_acquisition_id_isValid;

    QDateTime m_acquisition_time;
    bool m_acquisition_time_isSet;
    bool m_acquisition_time_isValid;

    QString m_external_reference_id;
    bool m_external_reference_id_isSet;
    bool m_external_reference_id_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_plan_id;
    bool m_plan_id_isSet;
    bool m_plan_id_isValid;

    OAIProvisioningState m_provisioning_state;
    bool m_provisioning_state_isSet;
    bool m_provisioning_state_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlanAcquisition)

#endif // OAIPlanAcquisition_H
