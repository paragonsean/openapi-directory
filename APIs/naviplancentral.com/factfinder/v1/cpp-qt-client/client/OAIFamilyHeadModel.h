/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFamilyHeadModel.h
 *
 * 
 */

#ifndef OAIFamilyHeadModel_H
#define OAIFamilyHeadModel_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFamilyHeadModel : public OAIObject {
public:
    OAIFamilyHeadModel();
    OAIFamilyHeadModel(QString json);
    ~OAIFamilyHeadModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAlreadyRetired() const;
    void setAlreadyRetired(const bool &already_retired);
    bool is_already_retired_Set() const;
    bool is_already_retired_Valid() const;

    QDateTime getBirthDate() const;
    void setBirthDate(const QDateTime &birth_date);
    bool is_birth_date_Set() const;
    bool is_birth_date_Valid() const;

    QString getExternalDestinationId() const;
    void setExternalDestinationId(const QString &external_destination_id);
    bool is_external_destination_id_Set() const;
    bool is_external_destination_id_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    QString getGender() const;
    void setGender(const QString &gender);
    bool is_gender_Set() const;
    bool is_gender_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    qint32 getTaxFilingStatus() const;
    void setTaxFilingStatus(const qint32 &tax_filing_status);
    bool is_tax_filing_status_Set() const;
    bool is_tax_filing_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_already_retired;
    bool m_already_retired_isSet;
    bool m_already_retired_isValid;

    QDateTime m_birth_date;
    bool m_birth_date_isSet;
    bool m_birth_date_isValid;

    QString m_external_destination_id;
    bool m_external_destination_id_isSet;
    bool m_external_destination_id_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    QString m_gender;
    bool m_gender_isSet;
    bool m_gender_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    qint32 m_tax_filing_status;
    bool m_tax_filing_status_isSet;
    bool m_tax_filing_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFamilyHeadModel)

#endif // OAIFamilyHeadModel_H
