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
 * OAIApplicationStaffModel.h
 *
 * Holds the information about a member of staff.
 */

#ifndef OAIApplicationStaffModel_H
#define OAIApplicationStaffModel_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIApplicationStaffModel : public OAIObject {
public:
    OAIApplicationStaffModel();
    OAIApplicationStaffModel(QString json);
    ~OAIApplicationStaffModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getContactEMail() const;
    void setContactEMail(const QString &contact_e_mail);
    bool is_contact_e_mail_Set() const;
    bool is_contact_e_mail_Valid() const;

    QString getContactMobile() const;
    void setContactMobile(const QString &contact_mobile);
    bool is_contact_mobile_Set() const;
    bool is_contact_mobile_Valid() const;

    QDateTime getDateOfBirth() const;
    void setDateOfBirth(const QDateTime &date_of_birth);
    bool is_date_of_birth_Set() const;
    bool is_date_of_birth_Valid() const;

    QString getETag() const;
    void setETag(const QString &e_tag);
    bool is_e_tag_Set() const;
    bool is_e_tag_Valid() const;

    QString getForename() const;
    void setForename(const QString &forename);
    bool is_forename_Set() const;
    bool is_forename_Valid() const;

    QString getGlobalReference() const;
    void setGlobalReference(const QString &global_reference);
    bool is_global_reference_Set() const;
    bool is_global_reference_Valid() const;

    bool isIsEnabled() const;
    void setIsEnabled(const bool &is_enabled);
    bool is_is_enabled_Set() const;
    bool is_is_enabled_Valid() const;

    QString getManagedBy() const;
    void setManagedBy(const QString &managed_by);
    bool is_managed_by_Set() const;
    bool is_managed_by_Valid() const;

    QString getMiddlename() const;
    void setMiddlename(const QString &middlename);
    bool is_middlename_Set() const;
    bool is_middlename_Valid() const;

    QString getOid() const;
    void setOid(const QString &oid);
    bool is_oid_Set() const;
    bool is_oid_Valid() const;

    QString getSurname() const;
    void setSurname(const QString &surname);
    bool is_surname_Set() const;
    bool is_surname_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_contact_e_mail;
    bool m_contact_e_mail_isSet;
    bool m_contact_e_mail_isValid;

    QString m_contact_mobile;
    bool m_contact_mobile_isSet;
    bool m_contact_mobile_isValid;

    QDateTime m_date_of_birth;
    bool m_date_of_birth_isSet;
    bool m_date_of_birth_isValid;

    QString m_e_tag;
    bool m_e_tag_isSet;
    bool m_e_tag_isValid;

    QString m_forename;
    bool m_forename_isSet;
    bool m_forename_isValid;

    QString m_global_reference;
    bool m_global_reference_isSet;
    bool m_global_reference_isValid;

    bool m_is_enabled;
    bool m_is_enabled_isSet;
    bool m_is_enabled_isValid;

    QString m_managed_by;
    bool m_managed_by_isSet;
    bool m_managed_by_isValid;

    QString m_middlename;
    bool m_middlename_isSet;
    bool m_middlename_isValid;

    QString m_oid;
    bool m_oid_isSet;
    bool m_oid_isValid;

    QString m_surname;
    bool m_surname_isSet;
    bool m_surname_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApplicationStaffModel)

#endif // OAIApplicationStaffModel_H
