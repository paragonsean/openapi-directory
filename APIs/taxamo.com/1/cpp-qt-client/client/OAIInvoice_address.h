/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIInvoice_address.h
 *
 * 
 */

#ifndef OAIInvoice_address_H
#define OAIInvoice_address_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIInvoice_address : public OAIObject {
public:
    OAIInvoice_address();
    OAIInvoice_address(QString json);
    ~OAIInvoice_address() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAddressDetail() const;
    void setAddressDetail(const QString &address_detail);
    bool is_address_detail_Set() const;
    bool is_address_detail_Valid() const;

    QString getBuildingNumber() const;
    void setBuildingNumber(const QString &building_number);
    bool is_building_number_Set() const;
    bool is_building_number_Valid() const;

    QString getCity() const;
    void setCity(const QString &city);
    bool is_city_Set() const;
    bool is_city_Valid() const;

    QString getCountry() const;
    void setCountry(const QString &country);
    bool is_country_Set() const;
    bool is_country_Valid() const;

    QString getFreeformAddress() const;
    void setFreeformAddress(const QString &freeform_address);
    bool is_freeform_address_Set() const;
    bool is_freeform_address_Valid() const;

    QString getPostalCode() const;
    void setPostalCode(const QString &postal_code);
    bool is_postal_code_Set() const;
    bool is_postal_code_Valid() const;

    QString getRegion() const;
    void setRegion(const QString &region);
    bool is_region_Set() const;
    bool is_region_Valid() const;

    QString getStreetName() const;
    void setStreetName(const QString &street_name);
    bool is_street_name_Set() const;
    bool is_street_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_address_detail;
    bool m_address_detail_isSet;
    bool m_address_detail_isValid;

    QString m_building_number;
    bool m_building_number_isSet;
    bool m_building_number_isValid;

    QString m_city;
    bool m_city_isSet;
    bool m_city_isValid;

    QString m_country;
    bool m_country_isSet;
    bool m_country_isValid;

    QString m_freeform_address;
    bool m_freeform_address_isSet;
    bool m_freeform_address_isValid;

    QString m_postal_code;
    bool m_postal_code_isSet;
    bool m_postal_code_isValid;

    QString m_region;
    bool m_region_isSet;
    bool m_region_isValid;

    QString m_street_name;
    bool m_street_name_isSet;
    bool m_street_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInvoice_address)

#endif // OAIInvoice_address_H
