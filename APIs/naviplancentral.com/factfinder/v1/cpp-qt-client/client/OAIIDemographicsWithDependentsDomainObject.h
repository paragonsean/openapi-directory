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
 * OAIIDemographicsWithDependentsDomainObject.h
 *
 * 
 */

#ifndef OAIIDemographicsWithDependentsDomainObject_H
#define OAIIDemographicsWithDependentsDomainObject_H

#include <QJsonObject>

#include "OAIIDemographicsDependentDomainObject.h"
#include "OAIIFamilyHeadDomainObject.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIDemographicsDependentDomainObject;
class OAIIFamilyHeadDomainObject;

class OAIIDemographicsWithDependentsDomainObject : public OAIObject {
public:
    OAIIDemographicsWithDependentsDomainObject();
    OAIIDemographicsWithDependentsDomainObject(QString json);
    ~OAIIDemographicsWithDependentsDomainObject() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCity() const;
    void setCity(const QString &city);
    bool is_city_Set() const;
    bool is_city_Valid() const;

    QDateTime getCreated() const;
    void setCreated(const QDateTime &created);
    bool is_created_Set() const;
    bool is_created_Valid() const;

    qint32 getDemographicsId() const;
    void setDemographicsId(const qint32 &demographics_id);
    bool is_demographics_id_Set() const;
    bool is_demographics_id_Valid() const;

    QList<OAIIDemographicsDependentDomainObject> getDependents() const;
    void setDependents(const QList<OAIIDemographicsDependentDomainObject> &dependents);
    bool is_dependents_Set() const;
    bool is_dependents_Valid() const;

    QString getExternalDestinationId() const;
    void setExternalDestinationId(const QString &external_destination_id);
    bool is_external_destination_id_Set() const;
    bool is_external_destination_id_Valid() const;

    QString getExternalSourceId() const;
    void setExternalSourceId(const QString &external_source_id);
    bool is_external_source_id_Set() const;
    bool is_external_source_id_Valid() const;

    qint32 getFactFinderId() const;
    void setFactFinderId(const qint32 &fact_finder_id);
    bool is_fact_finder_id_Set() const;
    bool is_fact_finder_id_Valid() const;

    OAIIFamilyHeadDomainObject getHead1() const;
    void setHead1(const OAIIFamilyHeadDomainObject &head1);
    bool is_head1_Set() const;
    bool is_head1_Valid() const;

    OAIIFamilyHeadDomainObject getHead2() const;
    void setHead2(const OAIIFamilyHeadDomainObject &head2);
    bool is_head2_Set() const;
    bool is_head2_Valid() const;

    bool isJointAnalysis() const;
    void setJointAnalysis(const bool &joint_analysis);
    bool is_joint_analysis_Set() const;
    bool is_joint_analysis_Valid() const;

    bool isLockRetirement() const;
    void setLockRetirement(const bool &lock_retirement);
    bool is_lock_retirement_Set() const;
    bool is_lock_retirement_Valid() const;

    qint32 getState() const;
    void setState(const qint32 &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_city;
    bool m_city_isSet;
    bool m_city_isValid;

    QDateTime m_created;
    bool m_created_isSet;
    bool m_created_isValid;

    qint32 m_demographics_id;
    bool m_demographics_id_isSet;
    bool m_demographics_id_isValid;

    QList<OAIIDemographicsDependentDomainObject> m_dependents;
    bool m_dependents_isSet;
    bool m_dependents_isValid;

    QString m_external_destination_id;
    bool m_external_destination_id_isSet;
    bool m_external_destination_id_isValid;

    QString m_external_source_id;
    bool m_external_source_id_isSet;
    bool m_external_source_id_isValid;

    qint32 m_fact_finder_id;
    bool m_fact_finder_id_isSet;
    bool m_fact_finder_id_isValid;

    OAIIFamilyHeadDomainObject m_head1;
    bool m_head1_isSet;
    bool m_head1_isValid;

    OAIIFamilyHeadDomainObject m_head2;
    bool m_head2_isSet;
    bool m_head2_isValid;

    bool m_joint_analysis;
    bool m_joint_analysis_isSet;
    bool m_joint_analysis_isValid;

    bool m_lock_retirement;
    bool m_lock_retirement_isSet;
    bool m_lock_retirement_isValid;

    qint32 m_state;
    bool m_state_isSet;
    bool m_state_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIDemographicsWithDependentsDomainObject)

#endif // OAIIDemographicsWithDependentsDomainObject_H
