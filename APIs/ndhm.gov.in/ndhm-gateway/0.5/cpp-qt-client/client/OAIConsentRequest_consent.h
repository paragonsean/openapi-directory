/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIConsentRequest_consent.h
 *
 * 
 */

#ifndef OAIConsentRequest_consent_H
#define OAIConsentRequest_consent_H

#include <QJsonObject>

#include "OAICareContextDefinition.h"
#include "OAIConsentArtefactResponse_consent_consentDetail_hip.h"
#include "OAIConsentArtefactResponse_consent_consentDetail_hiu.h"
#include "OAIConsentRequest_consent_patient.h"
#include "OAIHITypeEnum.h"
#include "OAIPermission.h"
#include "OAIRequester.h"
#include "OAIUsePurpose.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICareContextDefinition;
class OAIConsentArtefactResponse_consent_consentDetail_hip;
class OAIConsentArtefactResponse_consent_consentDetail_hiu;
class OAIConsentRequest_consent_patient;
class OAIPermission;
class OAIUsePurpose;
class OAIRequester;

class OAIConsentRequest_consent : public OAIObject {
public:
    OAIConsentRequest_consent();
    OAIConsentRequest_consent(QString json);
    ~OAIConsentRequest_consent() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAICareContextDefinition> getCareContexts() const;
    void setCareContexts(const QList<OAICareContextDefinition> &care_contexts);
    bool is_care_contexts_Set() const;
    bool is_care_contexts_Valid() const;

    QList<OAIHITypeEnum> getHiTypes() const;
    void setHiTypes(const QList<OAIHITypeEnum> &hi_types);
    bool is_hi_types_Set() const;
    bool is_hi_types_Valid() const;

    OAIConsentArtefactResponse_consent_consentDetail_hip getHip() const;
    void setHip(const OAIConsentArtefactResponse_consent_consentDetail_hip &hip);
    bool is_hip_Set() const;
    bool is_hip_Valid() const;

    OAIConsentArtefactResponse_consent_consentDetail_hiu getHiu() const;
    void setHiu(const OAIConsentArtefactResponse_consent_consentDetail_hiu &hiu);
    bool is_hiu_Set() const;
    bool is_hiu_Valid() const;

    OAIConsentRequest_consent_patient getPatient() const;
    void setPatient(const OAIConsentRequest_consent_patient &patient);
    bool is_patient_Set() const;
    bool is_patient_Valid() const;

    OAIPermission getPermission() const;
    void setPermission(const OAIPermission &permission);
    bool is_permission_Set() const;
    bool is_permission_Valid() const;

    OAIUsePurpose getPurpose() const;
    void setPurpose(const OAIUsePurpose &purpose);
    bool is_purpose_Set() const;
    bool is_purpose_Valid() const;

    OAIRequester getRequester() const;
    void setRequester(const OAIRequester &requester);
    bool is_requester_Set() const;
    bool is_requester_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAICareContextDefinition> m_care_contexts;
    bool m_care_contexts_isSet;
    bool m_care_contexts_isValid;

    QList<OAIHITypeEnum> m_hi_types;
    bool m_hi_types_isSet;
    bool m_hi_types_isValid;

    OAIConsentArtefactResponse_consent_consentDetail_hip m_hip;
    bool m_hip_isSet;
    bool m_hip_isValid;

    OAIConsentArtefactResponse_consent_consentDetail_hiu m_hiu;
    bool m_hiu_isSet;
    bool m_hiu_isValid;

    OAIConsentRequest_consent_patient m_patient;
    bool m_patient_isSet;
    bool m_patient_isValid;

    OAIPermission m_permission;
    bool m_permission_isSet;
    bool m_permission_isValid;

    OAIUsePurpose m_purpose;
    bool m_purpose_isSet;
    bool m_purpose_isValid;

    OAIRequester m_requester;
    bool m_requester_isSet;
    bool m_requester_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConsentRequest_consent)

#endif // OAIConsentRequest_consent_H
