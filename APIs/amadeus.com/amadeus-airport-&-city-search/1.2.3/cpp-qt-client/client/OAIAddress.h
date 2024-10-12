/**
 * Airport & City Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, in test this API only contains data from the United States, Spain, United Kingdom, Germany and India. 
 *
 * The version of the OpenAPI document: 1.2.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAddress.h
 *
 * 
 */

#ifndef OAIAddress_H
#define OAIAddress_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAddress : public OAIObject {
public:
    OAIAddress();
    OAIAddress(QString json);
    ~OAIAddress() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCityCode() const;
    void setCityCode(const QString &city_code);
    bool is_city_code_Set() const;
    bool is_city_code_Valid() const;

    QString getCityName() const;
    void setCityName(const QString &city_name);
    bool is_city_name_Set() const;
    bool is_city_name_Valid() const;

    QString getCountryCode() const;
    void setCountryCode(const QString &country_code);
    bool is_country_code_Set() const;
    bool is_country_code_Valid() const;

    QString getCountryName() const;
    void setCountryName(const QString &country_name);
    bool is_country_name_Set() const;
    bool is_country_name_Valid() const;

    QString getRegionCode() const;
    void setRegionCode(const QString &region_code);
    bool is_region_code_Set() const;
    bool is_region_code_Valid() const;

    QString getStateCode() const;
    void setStateCode(const QString &state_code);
    bool is_state_code_Set() const;
    bool is_state_code_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_city_code;
    bool m_city_code_isSet;
    bool m_city_code_isValid;

    QString m_city_name;
    bool m_city_name_isSet;
    bool m_city_name_isValid;

    QString m_country_code;
    bool m_country_code_isSet;
    bool m_country_code_isValid;

    QString m_country_name;
    bool m_country_name_isSet;
    bool m_country_name_isValid;

    QString m_region_code;
    bool m_region_code_isSet;
    bool m_region_code_isValid;

    QString m_state_code;
    bool m_state_code_isSet;
    bool m_state_code_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAddress)

#endif // OAIAddress_H
