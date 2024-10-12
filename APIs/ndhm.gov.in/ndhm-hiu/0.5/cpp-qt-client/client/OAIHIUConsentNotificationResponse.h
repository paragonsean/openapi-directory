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
 * OAIHIUConsentNotificationResponse.h
 *
 * 
 */

#ifndef OAIHIUConsentNotificationResponse_H
#define OAIHIUConsentNotificationResponse_H

#include <QJsonObject>

#include "OAIConsentAcknowledgement.h"
#include "OAIError.h"
#include "OAIRequestReference.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIConsentAcknowledgement;
class OAIError;
class OAIRequestReference;

class OAIHIUConsentNotificationResponse : public OAIObject {
public:
    OAIHIUConsentNotificationResponse();
    OAIHIUConsentNotificationResponse(QString json);
    ~OAIHIUConsentNotificationResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIConsentAcknowledgement> getAcknowledgement() const;
    void setAcknowledgement(const QList<OAIConsentAcknowledgement> &acknowledgement);
    bool is_acknowledgement_Set() const;
    bool is_acknowledgement_Valid() const;

    OAIError getError() const;
    void setError(const OAIError &error);
    bool is_error_Set() const;
    bool is_error_Valid() const;

    QString getRequestId() const;
    void setRequestId(const QString &request_id);
    bool is_request_id_Set() const;
    bool is_request_id_Valid() const;

    OAIRequestReference getResp() const;
    void setResp(const OAIRequestReference &resp);
    bool is_resp_Set() const;
    bool is_resp_Valid() const;

    QDateTime getTimestamp() const;
    void setTimestamp(const QDateTime &timestamp);
    bool is_timestamp_Set() const;
    bool is_timestamp_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIConsentAcknowledgement> m_acknowledgement;
    bool m_acknowledgement_isSet;
    bool m_acknowledgement_isValid;

    OAIError m_error;
    bool m_error_isSet;
    bool m_error_isValid;

    QString m_request_id;
    bool m_request_id_isSet;
    bool m_request_id_isValid;

    OAIRequestReference m_resp;
    bool m_resp_isSet;
    bool m_resp_isValid;

    QDateTime m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHIUConsentNotificationResponse)

#endif // OAIHIUConsentNotificationResponse_H
