/**
 * LetMC Api V2, Basic (Tier 2)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-basic-tier
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBranchModel.h
 *
 * Defines a single branch of a client.
 */

#ifndef OAIBranchModel_H
#define OAIBranchModel_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBranchModel : public OAIObject {
public:
    OAIBranchModel();
    OAIBranchModel(QString json);
    ~OAIBranchModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAddress1() const;
    void setAddress1(const QString &address1);
    bool is_address1_Set() const;
    bool is_address1_Valid() const;

    QString getAddress2() const;
    void setAddress2(const QString &address2);
    bool is_address2_Set() const;
    bool is_address2_Valid() const;

    QString getAddress3() const;
    void setAddress3(const QString &address3);
    bool is_address3_Set() const;
    bool is_address3_Valid() const;

    QString getAddress4() const;
    void setAddress4(const QString &address4);
    bool is_address4_Set() const;
    bool is_address4_Valid() const;

    QString getCompanyName() const;
    void setCompanyName(const QString &company_name);
    bool is_company_name_Set() const;
    bool is_company_name_Valid() const;

    QString getCounty() const;
    void setCounty(const QString &county);
    bool is_county_Set() const;
    bool is_county_Valid() const;

    QString getEMailAddress() const;
    void setEMailAddress(const QString &e_mail_address);
    bool is_e_mail_address_Set() const;
    bool is_e_mail_address_Valid() const;

    QString getETag() const;
    void setETag(const QString &e_tag);
    bool is_e_tag_Set() const;
    bool is_e_tag_Valid() const;

    QString getFaxPhone() const;
    void setFaxPhone(const QString &fax_phone);
    bool is_fax_phone_Set() const;
    bool is_fax_phone_Valid() const;

    QString getLandPhone() const;
    void setLandPhone(const QString &land_phone);
    bool is_land_phone_Set() const;
    bool is_land_phone_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOid() const;
    void setOid(const QString &oid);
    bool is_oid_Set() const;
    bool is_oid_Valid() const;

    QString getPostcode() const;
    void setPostcode(const QString &postcode);
    bool is_postcode_Set() const;
    bool is_postcode_Valid() const;

    QString getWebAddress() const;
    void setWebAddress(const QString &web_address);
    bool is_web_address_Set() const;
    bool is_web_address_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_address1;
    bool m_address1_isSet;
    bool m_address1_isValid;

    QString m_address2;
    bool m_address2_isSet;
    bool m_address2_isValid;

    QString m_address3;
    bool m_address3_isSet;
    bool m_address3_isValid;

    QString m_address4;
    bool m_address4_isSet;
    bool m_address4_isValid;

    QString m_company_name;
    bool m_company_name_isSet;
    bool m_company_name_isValid;

    QString m_county;
    bool m_county_isSet;
    bool m_county_isValid;

    QString m_e_mail_address;
    bool m_e_mail_address_isSet;
    bool m_e_mail_address_isValid;

    QString m_e_tag;
    bool m_e_tag_isSet;
    bool m_e_tag_isValid;

    QString m_fax_phone;
    bool m_fax_phone_isSet;
    bool m_fax_phone_isValid;

    QString m_land_phone;
    bool m_land_phone_isSet;
    bool m_land_phone_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_oid;
    bool m_oid_isSet;
    bool m_oid_isValid;

    QString m_postcode;
    bool m_postcode_isSet;
    bool m_postcode_isValid;

    QString m_web_address;
    bool m_web_address_isSet;
    bool m_web_address_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBranchModel)

#endif // OAIBranchModel_H
