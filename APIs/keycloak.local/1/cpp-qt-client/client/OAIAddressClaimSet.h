/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAddressClaimSet.h
 *
 * 
 */

#ifndef OAIAddressClaimSet_H
#define OAIAddressClaimSet_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAddressClaimSet : public OAIObject {
public:
    OAIAddressClaimSet();
    OAIAddressClaimSet(QString json);
    ~OAIAddressClaimSet() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCountry() const;
    void setCountry(const QString &country);
    bool is_country_Set() const;
    bool is_country_Valid() const;

    QString getFormatted() const;
    void setFormatted(const QString &formatted);
    bool is_formatted_Set() const;
    bool is_formatted_Valid() const;

    QString getLocality() const;
    void setLocality(const QString &locality);
    bool is_locality_Set() const;
    bool is_locality_Valid() const;

    QString getPostalCode() const;
    void setPostalCode(const QString &postal_code);
    bool is_postal_code_Set() const;
    bool is_postal_code_Valid() const;

    QString getRegion() const;
    void setRegion(const QString &region);
    bool is_region_Set() const;
    bool is_region_Valid() const;

    QString getStreetAddress() const;
    void setStreetAddress(const QString &street_address);
    bool is_street_address_Set() const;
    bool is_street_address_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_country;
    bool m_country_isSet;
    bool m_country_isValid;

    QString m_formatted;
    bool m_formatted_isSet;
    bool m_formatted_isValid;

    QString m_locality;
    bool m_locality_isSet;
    bool m_locality_isValid;

    QString m_postal_code;
    bool m_postal_code_isSet;
    bool m_postal_code_isValid;

    QString m_region;
    bool m_region_isSet;
    bool m_region_isValid;

    QString m_street_address;
    bool m_street_address_isSet;
    bool m_street_address_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAddressClaimSet)

#endif // OAIAddressClaimSet_H
