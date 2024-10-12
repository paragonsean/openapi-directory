/**
 * Health Data Consent Manager
 * Entity which provides health information aggregation services to customers of health care services. It enables customers to fetch their health information from one or more Health Information Providers (e.g., Hospitals, Diagnostic Labs, Medical Device Companies), based on their explicit Consent and to share such aggregated information with Health Information Users i.e. entities in need of such data (e.g., Insurers, Doctors, Medical Researchers).  # Specifications 1. This document maintains only the Health Information Gateway relevant APIs.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPatientAuthModeQueryRequest.h
 *
 * 
 */

#ifndef OAIPatientAuthModeQueryRequest_H
#define OAIPatientAuthModeQueryRequest_H

#include <QJsonObject>

#include "OAIPatientAuthModeQueryRequest_query.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPatientAuthModeQueryRequest_query;

class OAIPatientAuthModeQueryRequest : public OAIObject {
public:
    OAIPatientAuthModeQueryRequest();
    OAIPatientAuthModeQueryRequest(QString json);
    ~OAIPatientAuthModeQueryRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPatientAuthModeQueryRequest_query getQuery() const;
    void setQuery(const OAIPatientAuthModeQueryRequest_query &query);
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

    OAIPatientAuthModeQueryRequest_query m_query;
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

Q_DECLARE_METATYPE(OpenAPI::OAIPatientAuthModeQueryRequest)

#endif // OAIPatientAuthModeQueryRequest_H
