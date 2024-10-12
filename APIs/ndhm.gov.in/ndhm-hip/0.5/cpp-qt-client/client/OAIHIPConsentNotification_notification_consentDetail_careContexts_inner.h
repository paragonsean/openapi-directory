/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIHIPConsentNotification_notification_consentDetail_careContexts_inner.h
 *
 * 
 */

#ifndef OAIHIPConsentNotification_notification_consentDetail_careContexts_inner_H
#define OAIHIPConsentNotification_notification_consentDetail_careContexts_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIHIPConsentNotification_notification_consentDetail_careContexts_inner : public OAIObject {
public:
    OAIHIPConsentNotification_notification_consentDetail_careContexts_inner();
    OAIHIPConsentNotification_notification_consentDetail_careContexts_inner(QString json);
    ~OAIHIPConsentNotification_notification_consentDetail_careContexts_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCareContextReference() const;
    void setCareContextReference(const QString &care_context_reference);
    bool is_care_context_reference_Set() const;
    bool is_care_context_reference_Valid() const;

    QString getPatientReference() const;
    void setPatientReference(const QString &patient_reference);
    bool is_patient_reference_Set() const;
    bool is_patient_reference_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_care_context_reference;
    bool m_care_context_reference_isSet;
    bool m_care_context_reference_isValid;

    QString m_patient_reference;
    bool m_patient_reference_isSet;
    bool m_patient_reference_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHIPConsentNotification_notification_consentDetail_careContexts_inner)

#endif // OAIHIPConsentNotification_notification_consentDetail_careContexts_inner_H
