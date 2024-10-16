/**
 * Api Documentation
 * Api Documentation
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICustomer.h
 *
 * 
 */

#ifndef OAICustomer_H
#define OAICustomer_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICustomer : public OAIObject {
public:
    OAICustomer();
    OAICustomer(QString json);
    ~OAICustomer() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCity() const;
    void setCity(const QString &city);
    bool is_city_Set() const;
    bool is_city_Valid() const;

    QString getCompanyDescription() const;
    void setCompanyDescription(const QString &company_description);
    bool is_company_description_Set() const;
    bool is_company_description_Valid() const;

    QString getCompanyName() const;
    void setCompanyName(const QString &company_name);
    bool is_company_name_Set() const;
    bool is_company_name_Valid() const;

    QString getCountry() const;
    void setCountry(const QString &country);
    bool is_country_Set() const;
    bool is_country_Valid() const;

    QString getFaceRecognitionType() const;
    void setFaceRecognitionType(const QString &face_recognition_type);
    bool is_face_recognition_type_Set() const;
    bool is_face_recognition_type_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    QString getPhone() const;
    void setPhone(const QString &phone);
    bool is_phone_Set() const;
    bool is_phone_Valid() const;

    QString getState() const;
    void setState(const QString &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QString getStreetAddress() const;
    void setStreetAddress(const QString &street_address);
    bool is_street_address_Set() const;
    bool is_street_address_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    QString getZip() const;
    void setZip(const QString &zip);
    bool is_zip_Set() const;
    bool is_zip_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_city;
    bool m_city_isSet;
    bool m_city_isValid;

    QString m_company_description;
    bool m_company_description_isSet;
    bool m_company_description_isValid;

    QString m_company_name;
    bool m_company_name_isSet;
    bool m_company_name_isValid;

    QString m_country;
    bool m_country_isSet;
    bool m_country_isValid;

    QString m_face_recognition_type;
    bool m_face_recognition_type_isSet;
    bool m_face_recognition_type_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    QString m_phone;
    bool m_phone_isSet;
    bool m_phone_isValid;

    QString m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QString m_street_address;
    bool m_street_address_isSet;
    bool m_street_address_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;

    QString m_zip;
    bool m_zip_isSet;
    bool m_zip_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICustomer)

#endif // OAICustomer_H
