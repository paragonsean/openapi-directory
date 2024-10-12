/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIShareProfileRequest_patient_userDemographics.h
 *
 * 
 */

#ifndef OAIShareProfileRequest_patient_userDemographics_H
#define OAIShareProfileRequest_patient_userDemographics_H

#include <QJsonObject>

#include "OAIIdentifier.h"
#include "OAIPatientAddress.h"
#include "OAIPatientGender.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPatientAddress;
class OAIIdentifier;

class OAIShareProfileRequest_patient_userDemographics : public OAIObject {
public:
    OAIShareProfileRequest_patient_userDemographics();
    OAIShareProfileRequest_patient_userDemographics(QString json);
    ~OAIShareProfileRequest_patient_userDemographics() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPatientAddress getAddress() const;
    void setAddress(const OAIPatientAddress &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    qint32 getDayOfBirth() const;
    void setDayOfBirth(const qint32 &day_of_birth);
    bool is_day_of_birth_Set() const;
    bool is_day_of_birth_Valid() const;

    OAIPatientGender getGender() const;
    void setGender(const OAIPatientGender &gender);
    bool is_gender_Set() const;
    bool is_gender_Valid() const;

    QString getHealthId() const;
    void setHealthId(const QString &health_id);
    bool is_health_id_Set() const;
    bool is_health_id_Valid() const;

    QString getHealthIdNumber() const;
    void setHealthIdNumber(const QString &health_id_number);
    bool is_health_id_number_Set() const;
    bool is_health_id_number_Valid() const;

    QList<OAIIdentifier> getIdentifiers() const;
    void setIdentifiers(const QList<OAIIdentifier> &identifiers);
    bool is_identifiers_Set() const;
    bool is_identifiers_Valid() const;

    qint32 getMonthOfBirth() const;
    void setMonthOfBirth(const qint32 &month_of_birth);
    bool is_month_of_birth_Set() const;
    bool is_month_of_birth_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getYearOfBirth() const;
    void setYearOfBirth(const qint32 &year_of_birth);
    bool is_year_of_birth_Set() const;
    bool is_year_of_birth_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPatientAddress m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    qint32 m_day_of_birth;
    bool m_day_of_birth_isSet;
    bool m_day_of_birth_isValid;

    OAIPatientGender m_gender;
    bool m_gender_isSet;
    bool m_gender_isValid;

    QString m_health_id;
    bool m_health_id_isSet;
    bool m_health_id_isValid;

    QString m_health_id_number;
    bool m_health_id_number_isSet;
    bool m_health_id_number_isValid;

    QList<OAIIdentifier> m_identifiers;
    bool m_identifiers_isSet;
    bool m_identifiers_isValid;

    qint32 m_month_of_birth;
    bool m_month_of_birth_isSet;
    bool m_month_of_birth_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_year_of_birth;
    bool m_year_of_birth_isSet;
    bool m_year_of_birth_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIShareProfileRequest_patient_userDemographics)

#endif // OAIShareProfileRequest_patient_userDemographics_H
