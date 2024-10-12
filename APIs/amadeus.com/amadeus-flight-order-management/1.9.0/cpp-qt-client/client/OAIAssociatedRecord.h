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
 * OAIAssociatedRecord.h
 *
 * record associated to the order
 */

#ifndef OAIAssociatedRecord_H
#define OAIAssociatedRecord_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAssociatedRecord : public OAIObject {
public:
    OAIAssociatedRecord();
    OAIAssociatedRecord(QString json);
    ~OAIAssociatedRecord() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCreationDate() const;
    void setCreationDate(const QString &creation_date);
    bool is_creation_date_Set() const;
    bool is_creation_date_Valid() const;

    QString getOriginSystemCode() const;
    void setOriginSystemCode(const QString &origin_system_code);
    bool is_origin_system_code_Set() const;
    bool is_origin_system_code_Valid() const;

    QString getReference() const;
    void setReference(const QString &reference);
    bool is_reference_Set() const;
    bool is_reference_Valid() const;

    QString getFlightOfferId() const;
    void setFlightOfferId(const QString &flight_offer_id);
    bool is_flight_offer_id_Set() const;
    bool is_flight_offer_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_creation_date;
    bool m_creation_date_isSet;
    bool m_creation_date_isValid;

    QString m_origin_system_code;
    bool m_origin_system_code_isSet;
    bool m_origin_system_code_isValid;

    QString m_reference;
    bool m_reference_isSet;
    bool m_reference_isValid;

    QString m_flight_offer_id;
    bool m_flight_offer_id_isSet;
    bool m_flight_offer_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAssociatedRecord)

#endif // OAIAssociatedRecord_H
