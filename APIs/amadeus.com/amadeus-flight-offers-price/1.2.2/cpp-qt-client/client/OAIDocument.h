/**
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDocument.h
 *
 * the information that are found on an ID document
 */

#ifndef OAIDocument_H
#define OAIDocument_H

#include <QJsonObject>

#include <QDate>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDocument : public OAIObject {
public:
    OAIDocument();
    OAIDocument(QString json);
    ~OAIDocument() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBirthPlace() const;
    void setBirthPlace(const QString &birth_place);
    bool is_birth_place_Set() const;
    bool is_birth_place_Valid() const;

    QDate getExpiryDate() const;
    void setExpiryDate(const QDate &expiry_date);
    bool is_expiry_date_Set() const;
    bool is_expiry_date_Valid() const;

    QString getIssuanceCountry() const;
    void setIssuanceCountry(const QString &issuance_country);
    bool is_issuance_country_Set() const;
    bool is_issuance_country_Valid() const;

    QDate getIssuanceDate() const;
    void setIssuanceDate(const QDate &issuance_date);
    bool is_issuance_date_Set() const;
    bool is_issuance_date_Valid() const;

    QString getIssuanceLocation() const;
    void setIssuanceLocation(const QString &issuance_location);
    bool is_issuance_location_Set() const;
    bool is_issuance_location_Valid() const;

    QString getNationality() const;
    void setNationality(const QString &nationality);
    bool is_nationality_Set() const;
    bool is_nationality_Valid() const;

    QString getNumber() const;
    void setNumber(const QString &number);
    bool is_number_Set() const;
    bool is_number_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_birth_place;
    bool m_birth_place_isSet;
    bool m_birth_place_isValid;

    QDate m_expiry_date;
    bool m_expiry_date_isSet;
    bool m_expiry_date_isValid;

    QString m_issuance_country;
    bool m_issuance_country_isSet;
    bool m_issuance_country_isValid;

    QDate m_issuance_date;
    bool m_issuance_date_isSet;
    bool m_issuance_date_isValid;

    QString m_issuance_location;
    bool m_issuance_location_isSet;
    bool m_issuance_location_isValid;

    QString m_nationality;
    bool m_nationality_isSet;
    bool m_nationality_isValid;

    QString m_number;
    bool m_number_isSet;
    bool m_number_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDocument)

#endif // OAIDocument_H
