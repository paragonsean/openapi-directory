/**
 * City Context
 * City Context provides a straightforward API to access UK Open Data: crime statistics, schools, demographics and more.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPointInfo_schools_inner.h
 *
 * 
 */

#ifndef OAIPointInfo_schools_inner_H
#define OAIPointInfo_schools_inner_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPointInfo_schools_inner : public OAIObject {
public:
    OAIPointInfo_schools_inner();
    OAIPointInfo_schools_inner(QString json);
    ~OAIPointInfo_schools_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getDistanceMeters() const;
    void setDistanceMeters(const qint32 &distance_meters);
    bool is_distance_meters_Set() const;
    bool is_distance_meters_Valid() const;

    QString getLastInpectionUrl() const;
    void setLastInpectionUrl(const QString &last_inpection_url);
    bool is_last_inpection_url_Set() const;
    bool is_last_inpection_url_Valid() const;

    QDateTime getLastInspectionDate() const;
    void setLastInspectionDate(const QDateTime &last_inspection_date);
    bool is_last_inspection_date_Set() const;
    bool is_last_inspection_date_Valid() const;

    qint32 getLeadershipAndManagement() const;
    void setLeadershipAndManagement(const qint32 &leadership_and_management);
    bool is_leadership_and_management_Set() const;
    bool is_leadership_and_management_Valid() const;

    OAIObject getLocation() const;
    void setLocation(const OAIObject &location);
    bool is_location_Set() const;
    bool is_location_Valid() const;

    qint32 getOverallEffectiveness() const;
    void setOverallEffectiveness(const qint32 &overall_effectiveness);
    bool is_overall_effectiveness_Set() const;
    bool is_overall_effectiveness_Valid() const;

    QString getPhase() const;
    void setPhase(const QString &phase);
    bool is_phase_Set() const;
    bool is_phase_Valid() const;

    qint32 getQualityOfTeaching() const;
    void setQualityOfTeaching(const qint32 &quality_of_teaching);
    bool is_quality_of_teaching_Set() const;
    bool is_quality_of_teaching_Valid() const;

    QString getSchoolName() const;
    void setSchoolName(const QString &school_name);
    bool is_school_name_Set() const;
    bool is_school_name_Valid() const;

    QString getTypeOfEstablishment() const;
    void setTypeOfEstablishment(const QString &type_of_establishment);
    bool is_type_of_establishment_Set() const;
    bool is_type_of_establishment_Valid() const;

    qint32 getUrn() const;
    void setUrn(const qint32 &urn);
    bool is_urn_Set() const;
    bool is_urn_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_distance_meters;
    bool m_distance_meters_isSet;
    bool m_distance_meters_isValid;

    QString m_last_inpection_url;
    bool m_last_inpection_url_isSet;
    bool m_last_inpection_url_isValid;

    QDateTime m_last_inspection_date;
    bool m_last_inspection_date_isSet;
    bool m_last_inspection_date_isValid;

    qint32 m_leadership_and_management;
    bool m_leadership_and_management_isSet;
    bool m_leadership_and_management_isValid;

    OAIObject m_location;
    bool m_location_isSet;
    bool m_location_isValid;

    qint32 m_overall_effectiveness;
    bool m_overall_effectiveness_isSet;
    bool m_overall_effectiveness_isValid;

    QString m_phase;
    bool m_phase_isSet;
    bool m_phase_isValid;

    qint32 m_quality_of_teaching;
    bool m_quality_of_teaching_isSet;
    bool m_quality_of_teaching_isValid;

    QString m_school_name;
    bool m_school_name_isSet;
    bool m_school_name_isValid;

    QString m_type_of_establishment;
    bool m_type_of_establishment_isSet;
    bool m_type_of_establishment_isValid;

    qint32 m_urn;
    bool m_urn_isSet;
    bool m_urn_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPointInfo_schools_inner)

#endif // OAIPointInfo_schools_inner_H
