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
 * OAIPatientLinkReferenceResult_link.h
 *
 * 
 */

#ifndef OAIPatientLinkReferenceResult_link_H
#define OAIPatientLinkReferenceResult_link_H

#include <QJsonObject>

#include "OAIMeta.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIMeta;

class OAIPatientLinkReferenceResult_link : public OAIObject {
public:
    OAIPatientLinkReferenceResult_link();
    OAIPatientLinkReferenceResult_link(QString json);
    ~OAIPatientLinkReferenceResult_link() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAuthenticationType() const;
    void setAuthenticationType(const QString &authentication_type);
    bool is_authentication_type_Set() const;
    bool is_authentication_type_Valid() const;

    OAIMeta getMeta() const;
    void setMeta(const OAIMeta &meta);
    bool is_meta_Set() const;
    bool is_meta_Valid() const;

    QString getReferenceNumber() const;
    void setReferenceNumber(const QString &reference_number);
    bool is_reference_number_Set() const;
    bool is_reference_number_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_authentication_type;
    bool m_authentication_type_isSet;
    bool m_authentication_type_isValid;

    OAIMeta m_meta;
    bool m_meta_isSet;
    bool m_meta_isValid;

    QString m_reference_number;
    bool m_reference_number_isSet;
    bool m_reference_number_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPatientLinkReferenceResult_link)

#endif // OAIPatientLinkReferenceResult_link_H
