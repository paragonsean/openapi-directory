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
 * OAICareContextRepresentation.h
 *
 * 
 */

#ifndef OAICareContextRepresentation_H
#define OAICareContextRepresentation_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICareContextRepresentation : public OAIObject {
public:
    OAICareContextRepresentation();
    OAICareContextRepresentation(QString json);
    ~OAICareContextRepresentation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDisplay() const;
    void setDisplay(const QString &display);
    bool is_display_Set() const;
    bool is_display_Valid() const;

    QString getReferenceNumber() const;
    void setReferenceNumber(const QString &reference_number);
    bool is_reference_number_Set() const;
    bool is_reference_number_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_display;
    bool m_display_isSet;
    bool m_display_isValid;

    QString m_reference_number;
    bool m_reference_number_isSet;
    bool m_reference_number_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICareContextRepresentation)

#endif // OAICareContextRepresentation_H
