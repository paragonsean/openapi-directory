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
 * OAIHIUConsentRequestStatus_consentRequest.h
 *
 * 
 */

#ifndef OAIHIUConsentRequestStatus_consentRequest_H
#define OAIHIUConsentRequestStatus_consentRequest_H

#include <QJsonObject>

#include "OAIConsentArtefactReference.h"
#include "OAIConsentStatus.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIConsentArtefactReference;

class OAIHIUConsentRequestStatus_consentRequest : public OAIObject {
public:
    OAIHIUConsentRequestStatus_consentRequest();
    OAIHIUConsentRequestStatus_consentRequest(QString json);
    ~OAIHIUConsentRequestStatus_consentRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIConsentArtefactReference> getConsentArtefacts() const;
    void setConsentArtefacts(const QList<OAIConsentArtefactReference> &consent_artefacts);
    bool is_consent_artefacts_Set() const;
    bool is_consent_artefacts_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIConsentStatus getStatus() const;
    void setStatus(const OAIConsentStatus &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIConsentArtefactReference> m_consent_artefacts;
    bool m_consent_artefacts_isSet;
    bool m_consent_artefacts_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIConsentStatus m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHIUConsentRequestStatus_consentRequest)

#endif // OAIHIUConsentRequestStatus_consentRequest_H
