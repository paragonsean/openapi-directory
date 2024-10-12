/**
 * Health Repository Provider Specifications for HIU
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **_/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **_/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **_/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIHIUConsentNotificationEvent_notification.h
 *
 * 
 */

#ifndef OAIHIUConsentNotificationEvent_notification_H
#define OAIHIUConsentNotificationEvent_notification_H

#include <QJsonObject>

#include "OAIConsentArtefactReference.h"
#include "OAIConsentStatus.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIConsentArtefactReference;

class OAIHIUConsentNotificationEvent_notification : public OAIObject {
public:
    OAIHIUConsentNotificationEvent_notification();
    OAIHIUConsentNotificationEvent_notification(QString json);
    ~OAIHIUConsentNotificationEvent_notification() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIConsentArtefactReference> getConsentArtefacts() const;
    void setConsentArtefacts(const QList<OAIConsentArtefactReference> &consent_artefacts);
    bool is_consent_artefacts_Set() const;
    bool is_consent_artefacts_Valid() const;

    QString getConsentRequestId() const;
    void setConsentRequestId(const QString &consent_request_id);
    bool is_consent_request_id_Set() const;
    bool is_consent_request_id_Valid() const;

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

    QString m_consent_request_id;
    bool m_consent_request_id_isSet;
    bool m_consent_request_id_isValid;

    OAIConsentStatus m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHIUConsentNotificationEvent_notification)

#endif // OAIHIUConsentNotificationEvent_notification_H
