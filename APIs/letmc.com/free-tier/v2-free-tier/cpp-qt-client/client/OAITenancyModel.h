/**
 * LetMC Api V2, Free (Tier 1)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-free-tier
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITenancyModel.h
 *
 * Represents a single tenancy on a property structure. This class may              be considered to be the context of the tenancy strategy pattern. The              strategy is the tenancy service, that dictates the algorithm applied              to the tenancy. This class therefore holds the raw data of a tenancy,              and ignores any tenancy service (fully managed, let only) parameters.
 */

#ifndef OAITenancyModel_H
#define OAITenancyModel_H

#include <QJsonObject>

#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITenancyModel : public OAIObject {
public:
    OAITenancyModel();
    OAITenancyModel(QString json);
    ~OAITenancyModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getAdvertiseFrom() const;
    void setAdvertiseFrom(const QDateTime &advertise_from);
    bool is_advertise_from_Set() const;
    bool is_advertise_from_Valid() const;

    QString getArea() const;
    void setArea(const QString &area);
    bool is_area_Set() const;
    bool is_area_Valid() const;

    double getBondRequired() const;
    void setBondRequired(const double &bond_required);
    bool is_bond_required_Set() const;
    bool is_bond_required_Valid() const;

    QString getBranch() const;
    void setBranch(const QString &branch);
    bool is_branch_Set() const;
    bool is_branch_Valid() const;

    QString getETag() const;
    void setETag(const QString &e_tag);
    bool is_e_tag_Set() const;
    bool is_e_tag_Valid() const;

    QString getFurnished() const;
    void setFurnished(const QString &furnished);
    bool is_furnished_Set() const;
    bool is_furnished_Valid() const;

    QString getGlobalReference() const;
    void setGlobalReference(const QString &global_reference);
    bool is_global_reference_Set() const;
    bool is_global_reference_Valid() const;

    bool isIsShareProperty() const;
    void setIsShareProperty(const bool &is_share_property);
    bool is_is_share_property_Set() const;
    bool is_is_share_property_Valid() const;

    bool isIsStudentProperty() const;
    void setIsStudentProperty(const bool &is_student_property);
    bool is_is_student_property_Set() const;
    bool is_is_student_property_Valid() const;

    bool isIsTenancyAdvertised() const;
    void setIsTenancyAdvertised(const bool &is_tenancy_advertised);
    bool is_is_tenancy_advertised_Set() const;
    bool is_is_tenancy_advertised_Valid() const;

    bool isIsTenancyProposed() const;
    void setIsTenancyProposed(const bool &is_tenancy_proposed);
    bool is_is_tenancy_proposed_Set() const;
    bool is_is_tenancy_proposed_Valid() const;

    qint32 getMaximumTenants() const;
    void setMaximumTenants(const qint32 &maximum_tenants);
    bool is_maximum_tenants_Set() const;
    bool is_maximum_tenants_Valid() const;

    qint32 getMinimumTenants() const;
    void setMinimumTenants(const qint32 &minimum_tenants);
    bool is_minimum_tenants_Set() const;
    bool is_minimum_tenants_Valid() const;

    QString getOid() const;
    void setOid(const QString &oid);
    bool is_oid_Set() const;
    bool is_oid_Valid() const;

    double getRentAdvertised() const;
    void setRentAdvertised(const double &rent_advertised);
    bool is_rent_advertised_Set() const;
    bool is_rent_advertised_Valid() const;

    qint32 getRentRecurrence() const;
    void setRentRecurrence(const qint32 &rent_recurrence);
    bool is_rent_recurrence_Set() const;
    bool is_rent_recurrence_Valid() const;

    QString getRentSchedule() const;
    void setRentSchedule(const QString &rent_schedule);
    bool is_rent_schedule_Set() const;
    bool is_rent_schedule_Valid() const;

    QString getTenancyProperty() const;
    void setTenancyProperty(const QString &tenancy_property);
    bool is_tenancy_property_Set() const;
    bool is_tenancy_property_Valid() const;

    QList<QString> getTenantSystemTypes() const;
    void setTenantSystemTypes(const QList<QString> &tenant_system_types);
    bool is_tenant_system_types_Set() const;
    bool is_tenant_system_types_Valid() const;

    qint32 getTermMaximum() const;
    void setTermMaximum(const qint32 &term_maximum);
    bool is_term_maximum_Set() const;
    bool is_term_maximum_Valid() const;

    qint32 getTermMinimum() const;
    void setTermMinimum(const qint32 &term_minimum);
    bool is_term_minimum_Set() const;
    bool is_term_minimum_Valid() const;

    QDateTime getTermStart() const;
    void setTermStart(const QDateTime &term_start);
    bool is_term_start_Set() const;
    bool is_term_start_Valid() const;

    QString getUtilityCouncilTax() const;
    void setUtilityCouncilTax(const QString &utility_council_tax);
    bool is_utility_council_tax_Set() const;
    bool is_utility_council_tax_Valid() const;

    QString getUtilityElectricity() const;
    void setUtilityElectricity(const QString &utility_electricity);
    bool is_utility_electricity_Set() const;
    bool is_utility_electricity_Valid() const;

    QString getUtilityGas() const;
    void setUtilityGas(const QString &utility_gas);
    bool is_utility_gas_Set() const;
    bool is_utility_gas_Valid() const;

    QString getUtilityTelephone() const;
    void setUtilityTelephone(const QString &utility_telephone);
    bool is_utility_telephone_Set() const;
    bool is_utility_telephone_Valid() const;

    QString getUtilityWater() const;
    void setUtilityWater(const QString &utility_water);
    bool is_utility_water_Set() const;
    bool is_utility_water_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_advertise_from;
    bool m_advertise_from_isSet;
    bool m_advertise_from_isValid;

    QString m_area;
    bool m_area_isSet;
    bool m_area_isValid;

    double m_bond_required;
    bool m_bond_required_isSet;
    bool m_bond_required_isValid;

    QString m_branch;
    bool m_branch_isSet;
    bool m_branch_isValid;

    QString m_e_tag;
    bool m_e_tag_isSet;
    bool m_e_tag_isValid;

    QString m_furnished;
    bool m_furnished_isSet;
    bool m_furnished_isValid;

    QString m_global_reference;
    bool m_global_reference_isSet;
    bool m_global_reference_isValid;

    bool m_is_share_property;
    bool m_is_share_property_isSet;
    bool m_is_share_property_isValid;

    bool m_is_student_property;
    bool m_is_student_property_isSet;
    bool m_is_student_property_isValid;

    bool m_is_tenancy_advertised;
    bool m_is_tenancy_advertised_isSet;
    bool m_is_tenancy_advertised_isValid;

    bool m_is_tenancy_proposed;
    bool m_is_tenancy_proposed_isSet;
    bool m_is_tenancy_proposed_isValid;

    qint32 m_maximum_tenants;
    bool m_maximum_tenants_isSet;
    bool m_maximum_tenants_isValid;

    qint32 m_minimum_tenants;
    bool m_minimum_tenants_isSet;
    bool m_minimum_tenants_isValid;

    QString m_oid;
    bool m_oid_isSet;
    bool m_oid_isValid;

    double m_rent_advertised;
    bool m_rent_advertised_isSet;
    bool m_rent_advertised_isValid;

    qint32 m_rent_recurrence;
    bool m_rent_recurrence_isSet;
    bool m_rent_recurrence_isValid;

    QString m_rent_schedule;
    bool m_rent_schedule_isSet;
    bool m_rent_schedule_isValid;

    QString m_tenancy_property;
    bool m_tenancy_property_isSet;
    bool m_tenancy_property_isValid;

    QList<QString> m_tenant_system_types;
    bool m_tenant_system_types_isSet;
    bool m_tenant_system_types_isValid;

    qint32 m_term_maximum;
    bool m_term_maximum_isSet;
    bool m_term_maximum_isValid;

    qint32 m_term_minimum;
    bool m_term_minimum_isSet;
    bool m_term_minimum_isValid;

    QDateTime m_term_start;
    bool m_term_start_isSet;
    bool m_term_start_isValid;

    QString m_utility_council_tax;
    bool m_utility_council_tax_isSet;
    bool m_utility_council_tax_isValid;

    QString m_utility_electricity;
    bool m_utility_electricity_isSet;
    bool m_utility_electricity_isValid;

    QString m_utility_gas;
    bool m_utility_gas_isSet;
    bool m_utility_gas_isValid;

    QString m_utility_telephone;
    bool m_utility_telephone_isSet;
    bool m_utility_telephone_isValid;

    QString m_utility_water;
    bool m_utility_water_isSet;
    bool m_utility_water_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITenancyModel)

#endif // OAITenancyModel_H
