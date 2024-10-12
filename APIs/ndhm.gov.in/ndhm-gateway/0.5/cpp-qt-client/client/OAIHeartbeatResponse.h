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
 * OAIHeartbeatResponse.h
 *
 * 
 */

#ifndef OAIHeartbeatResponse_H
#define OAIHeartbeatResponse_H

#include <QJsonObject>

#include "OAIError.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIError;

class OAIHeartbeatResponse : public OAIObject {
public:
    OAIHeartbeatResponse();
    OAIHeartbeatResponse(QString json);
    ~OAIHeartbeatResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIError getError() const;
    void setError(const OAIError &error);
    bool is_error_Set() const;
    bool is_error_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

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

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QDateTime m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHeartbeatResponse)

#endif // OAIHeartbeatResponse_H
