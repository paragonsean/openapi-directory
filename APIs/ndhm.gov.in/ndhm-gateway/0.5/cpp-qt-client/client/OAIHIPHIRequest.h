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
 * OAIHIPHIRequest.h
 *
 * 
 */

#ifndef OAIHIPHIRequest_H
#define OAIHIPHIRequest_H

#include <QJsonObject>

#include "OAIHIPHIRequest_hiRequest.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIHIPHIRequest_hiRequest;

class OAIHIPHIRequest : public OAIObject {
public:
    OAIHIPHIRequest();
    OAIHIPHIRequest(QString json);
    ~OAIHIPHIRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIHIPHIRequest_hiRequest getHiRequest() const;
    void setHiRequest(const OAIHIPHIRequest_hiRequest &hi_request);
    bool is_hi_request_Set() const;
    bool is_hi_request_Valid() const;

    QString getRequestId() const;
    void setRequestId(const QString &request_id);
    bool is_request_id_Set() const;
    bool is_request_id_Valid() const;

    QDateTime getTimestamp() const;
    void setTimestamp(const QDateTime &timestamp);
    bool is_timestamp_Set() const;
    bool is_timestamp_Valid() const;

    QString getTransactionId() const;
    void setTransactionId(const QString &transaction_id);
    bool is_transaction_id_Set() const;
    bool is_transaction_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIHIPHIRequest_hiRequest m_hi_request;
    bool m_hi_request_isSet;
    bool m_hi_request_isValid;

    QString m_request_id;
    bool m_request_id_isSet;
    bool m_request_id_isValid;

    QDateTime m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;

    QString m_transaction_id;
    bool m_transaction_id_isSet;
    bool m_transaction_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHIPHIRequest)

#endif // OAIHIPHIRequest_H
