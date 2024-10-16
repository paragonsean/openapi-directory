/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAnalytics_LogFlow_200_response.h
 *
 * 
 */

#ifndef OAIAnalytics_LogFlow_200_response_H
#define OAIAnalytics_LogFlow_200_response_H

#include <QJsonObject>

#include "OAIAnalytics_LogFlow_200_response_logs_inner.h"
#include <QDateTime>
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAnalytics_LogFlow_200_response_logs_inner;

class OAIAnalytics_LogFlow_200_response : public OAIObject {
public:
    OAIAnalytics_LogFlow_200_response();
    OAIAnalytics_LogFlow_200_response(QString json);
    ~OAIAnalytics_LogFlow_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isExceededMaxLimit() const;
    void setExceededMaxLimit(const bool &exceeded_max_limit);
    bool is_exceeded_max_limit_Set() const;
    bool is_exceeded_max_limit_Valid() const;

    QDateTime getLastReceivedLogTimestamp() const;
    void setLastReceivedLogTimestamp(const QDateTime &last_received_log_timestamp);
    bool is_last_received_log_timestamp_Set() const;
    bool is_last_received_log_timestamp_Valid() const;

    QList<OAIAnalytics_LogFlow_200_response_logs_inner> getLogs() const;
    void setLogs(const QList<OAIAnalytics_LogFlow_200_response_logs_inner> &logs);
    bool is_logs_Set() const;
    bool is_logs_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_exceeded_max_limit;
    bool m_exceeded_max_limit_isSet;
    bool m_exceeded_max_limit_isValid;

    QDateTime m_last_received_log_timestamp;
    bool m_last_received_log_timestamp_isSet;
    bool m_last_received_log_timestamp_isValid;

    QList<OAIAnalytics_LogFlow_200_response_logs_inner> m_logs;
    bool m_logs_isSet;
    bool m_logs_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAnalytics_LogFlow_200_response)

#endif // OAIAnalytics_LogFlow_200_response_H
