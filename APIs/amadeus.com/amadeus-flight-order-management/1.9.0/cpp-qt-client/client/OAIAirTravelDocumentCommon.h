/**
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAirTravelDocumentCommon.h
 *
 * 
 */

#ifndef OAIAirTravelDocumentCommon_H
#define OAIAirTravelDocumentCommon_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAirTravelDocumentCommon : public OAIObject {
public:
    OAIAirTravelDocumentCommon();
    OAIAirTravelDocumentCommon(QString json);
    ~OAIAirTravelDocumentCommon() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDocumentNumber() const;
    void setDocumentNumber(const QString &document_number);
    bool is_document_number_Set() const;
    bool is_document_number_Valid() const;

    QString getDocumentStatus() const;
    void setDocumentStatus(const QString &document_status);
    bool is_document_status_Set() const;
    bool is_document_status_Valid() const;

    QString getDocumentType() const;
    void setDocumentType(const QString &document_type);
    bool is_document_type_Set() const;
    bool is_document_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_document_number;
    bool m_document_number_isSet;
    bool m_document_number_isValid;

    QString m_document_status;
    bool m_document_status_isSet;
    bool m_document_status_isValid;

    QString m_document_type;
    bool m_document_type_isSet;
    bool m_document_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAirTravelDocumentCommon)

#endif // OAIAirTravelDocumentCommon_H
