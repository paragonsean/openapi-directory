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
 * OAIHIPHealthInformationRequestAcknowledgement.h
 *
 * 
 */

#ifndef OAIHIPHealthInformationRequestAcknowledgement_H
#define OAIHIPHealthInformationRequestAcknowledgement_H

#include <QJsonObject>

#include "OAIError.h"
#include "OAIHIPHealthInformationRequestAcknowledgement_hiRequest.h"
#include "OAIRequestReference.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIError;
class OAIHIPHealthInformationRequestAcknowledgement_hiRequest;
class OAIRequestReference;

class OAIHIPHealthInformationRequestAcknowledgement : public OAIObject {
public:
    OAIHIPHealthInformationRequestAcknowledgement();
    OAIHIPHealthInformationRequestAcknowledgement(QString json);
    ~OAIHIPHealthInformationRequestAcknowledgement() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIError getError() const;
    void setError(const OAIError &error);
    bool is_error_Set() const;
    bool is_error_Valid() const;

    OAIHIPHealthInformationRequestAcknowledgement_hiRequest getHiRequest() const;
    void setHiRequest(const OAIHIPHealthInformationRequestAcknowledgement_hiRequest &hi_request);
    bool is_hi_request_Set() const;
    bool is_hi_request_Valid() const;

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

    OAIError m_error;
    bool m_error_isSet;
    bool m_error_isValid;

    OAIHIPHealthInformationRequestAcknowledgement_hiRequest m_hi_request;
    bool m_hi_request_isSet;
    bool m_hi_request_isValid;

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

Q_DECLARE_METATYPE(OpenAPI::OAIHIPHealthInformationRequestAcknowledgement)

#endif // OAIHIPHealthInformationRequestAcknowledgement_H
