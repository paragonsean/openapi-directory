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
 * OAIHIRequest.h
 *
 * 
 */

#ifndef OAIHIRequest_H
#define OAIHIRequest_H

#include <QJsonObject>

#include "OAIHIRequest_hiRequest.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIHIRequest_hiRequest;

class OAIHIRequest : public OAIObject {
public:
    OAIHIRequest();
    OAIHIRequest(QString json);
    ~OAIHIRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIHIRequest_hiRequest getHiRequest() const;
    void setHiRequest(const OAIHIRequest_hiRequest &hi_request);
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

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIHIRequest_hiRequest m_hi_request;
    bool m_hi_request_isSet;
    bool m_hi_request_isValid;

    QString m_request_id;
    bool m_request_id_isSet;
    bool m_request_id_isValid;

    QDateTime m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHIRequest)

#endif // OAIHIRequest_H
