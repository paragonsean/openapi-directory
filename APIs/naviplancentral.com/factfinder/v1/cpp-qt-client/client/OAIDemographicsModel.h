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
 * OAIDemographicsModel.h
 *
 * 
 */

#ifndef OAIDemographicsModel_H
#define OAIDemographicsModel_H

#include <QJsonObject>

#include "OAIFamilyHeadModel.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFamilyHeadModel;

class OAIDemographicsModel : public OAIObject {
public:
    OAIDemographicsModel();
    OAIDemographicsModel(QString json);
    ~OAIDemographicsModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCity() const;
    void setCity(const QString &city);
    bool is_city_Set() const;
    bool is_city_Valid() const;

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

    OAIFamilyHeadModel getHead1() const;
    void setHead1(const OAIFamilyHeadModel &head1);
    bool is_head1_Set() const;
    bool is_head1_Valid() const;

    OAIFamilyHeadModel getHead2() const;
    void setHead2(const OAIFamilyHeadModel &head2);
    bool is_head2_Set() const;
    bool is_head2_Valid() const;

    bool isJointAnalysis() const;
    void setJointAnalysis(const bool &joint_analysis);
    bool is_joint_analysis_Set() const;
    bool is_joint_analysis_Valid() const;

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

    QString m_external_destination_id;
    bool m_external_destination_id_isSet;
    bool m_external_destination_id_isValid;

    QString m_external_source_id;
    bool m_external_source_id_isSet;
    bool m_external_source_id_isValid;

    qint32 m_fact_finder_id;
    bool m_fact_finder_id_isSet;
    bool m_fact_finder_id_isValid;

    OAIFamilyHeadModel m_head1;
    bool m_head1_isSet;
    bool m_head1_isValid;

    OAIFamilyHeadModel m_head2;
    bool m_head2_isSet;
    bool m_head2_isValid;

    bool m_joint_analysis;
    bool m_joint_analysis_isSet;
    bool m_joint_analysis_isValid;

    qint32 m_state;
    bool m_state_isSet;
    bool m_state_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDemographicsModel)

#endif // OAIDemographicsModel_H
