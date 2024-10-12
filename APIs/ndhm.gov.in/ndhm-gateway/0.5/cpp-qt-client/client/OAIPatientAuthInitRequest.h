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
 * OAIPatientAuthInitRequest.h
 *
 * 
 */

#ifndef OAIPatientAuthInitRequest_H
#define OAIPatientAuthInitRequest_H

#include <QJsonObject>

#include "OAIPatientAuthInitRequest_query.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPatientAuthInitRequest_query;

class OAIPatientAuthInitRequest : public OAIObject {
public:
    OAIPatientAuthInitRequest();
    OAIPatientAuthInitRequest(QString json);
    ~OAIPatientAuthInitRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPatientAuthInitRequest_query getQuery() const;
    void setQuery(const OAIPatientAuthInitRequest_query &query);
    bool is_query_Set() const;
    bool is_query_Valid() const;

    QString getRequestId() const;
    void setRequestId(const QString &request_id);
    bool is_request_id_Set() const;
    bool is_request_id_Valid() const;

    QDateTime getTimestamp() const;
    void setTimestamp(const QDateTime &timestamp);
    bool is_timestamp_Set() const;
    bool is_timestamp_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPatientAuthInitRequest_query m_query;
    bool m_query_isSet;
    bool m_query_isValid;

    QString m_request_id;
    bool m_request_id_isSet;
    bool m_request_id_isValid;

    QDateTime m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPatientAuthInitRequest)

#endif // OAIPatientAuthInitRequest_H
