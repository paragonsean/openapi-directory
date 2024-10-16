/**
 * Personnel Data
 * API for reading and writing personnel data incl. data about attendances and absences
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEmployee_attributes_inner.h
 *
 * 
 */

#ifndef OAIEmployee_attributes_inner_H
#define OAIEmployee_attributes_inner_H

#include <QJsonObject>

#include "OAIAbsenceEntitlement.h"
#include "OAIAttribute.h"
#include "OAICostCenters.h"
#include "OAIDepartment.h"
#include "OAIHolidayCalendar.h"
#include "OAIOffice.h"
#include "OAISupervisor.h"
#include "OAIWorkSchedule.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAbsenceEntitlement;
class OAIAttribute;
class OAICostCenters;
class OAIDepartment;
class OAIHolidayCalendar;
class OAIOffice;
class OAISupervisor;
class OAIWorkSchedule;

class OAIEmployee_attributes_inner : public OAIObject {
public:
    OAIEmployee_attributes_inner();
    OAIEmployee_attributes_inner(QString json);
    ~OAIEmployee_attributes_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAbsenceEntitlement getAbsenceEntitlement() const;
    void setAbsenceEntitlement(const OAIAbsenceEntitlement &absence_entitlement);
    bool is_absence_entitlement_Set() const;
    bool is_absence_entitlement_Valid() const;

    OAIAttribute getContractEndDate() const;
    void setContractEndDate(const OAIAttribute &contract_end_date);
    bool is_contract_end_date_Set() const;
    bool is_contract_end_date_Valid() const;

    OAICostCenters getCostCenters() const;
    void setCostCenters(const OAICostCenters &cost_centers);
    bool is_cost_centers_Set() const;
    bool is_cost_centers_Valid() const;

    OAIAttribute getCreatedAt() const;
    void setCreatedAt(const OAIAttribute &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    OAIDepartment getDepartment() const;
    void setDepartment(const OAIDepartment &department);
    bool is_department_Set() const;
    bool is_department_Valid() const;

    OAIAttribute getEmail() const;
    void setEmail(const OAIAttribute &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    OAIAttribute getEmploymentType() const;
    void setEmploymentType(const OAIAttribute &employment_type);
    bool is_employment_type_Set() const;
    bool is_employment_type_Valid() const;

    OAIAttribute getFirstName() const;
    void setFirstName(const OAIAttribute &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    OAIAttribute getFixSalary() const;
    void setFixSalary(const OAIAttribute &fix_salary);
    bool is_fix_salary_Set() const;
    bool is_fix_salary_Valid() const;

    OAIAttribute getGender() const;
    void setGender(const OAIAttribute &gender);
    bool is_gender_Set() const;
    bool is_gender_Valid() const;

    OAIAttribute getHireDate() const;
    void setHireDate(const OAIAttribute &hire_date);
    bool is_hire_date_Set() const;
    bool is_hire_date_Valid() const;

    OAIHolidayCalendar getHolidayCalendar() const;
    void setHolidayCalendar(const OAIHolidayCalendar &holiday_calendar);
    bool is_holiday_calendar_Set() const;
    bool is_holiday_calendar_Valid() const;

    OAIAttribute getHourlySalary() const;
    void setHourlySalary(const OAIAttribute &hourly_salary);
    bool is_hourly_salary_Set() const;
    bool is_hourly_salary_Valid() const;

    OAIAttribute getId() const;
    void setId(const OAIAttribute &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIAttribute getLastName() const;
    void setLastName(const OAIAttribute &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    OAIOffice getOffice() const;
    void setOffice(const OAIOffice &office);
    bool is_office_Set() const;
    bool is_office_Valid() const;

    OAIAttribute getPosition() const;
    void setPosition(const OAIAttribute &position);
    bool is_position_Set() const;
    bool is_position_Valid() const;

    OAIAttribute getProbationPeriodEnd() const;
    void setProbationPeriodEnd(const OAIAttribute &probation_period_end);
    bool is_probation_period_end_Set() const;
    bool is_probation_period_end_Valid() const;

    OAIAttribute getStatus() const;
    void setStatus(const OAIAttribute &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    OAISupervisor getSupervisor() const;
    void setSupervisor(const OAISupervisor &supervisor);
    bool is_supervisor_Set() const;
    bool is_supervisor_Valid() const;

    OAIAttribute getTerminationDate() const;
    void setTerminationDate(const OAIAttribute &termination_date);
    bool is_termination_date_Set() const;
    bool is_termination_date_Valid() const;

    OAIAttribute getTerminationReason() const;
    void setTerminationReason(const OAIAttribute &termination_reason);
    bool is_termination_reason_Set() const;
    bool is_termination_reason_Valid() const;

    OAIAttribute getTerminationType() const;
    void setTerminationType(const OAIAttribute &termination_type);
    bool is_termination_type_Set() const;
    bool is_termination_type_Valid() const;

    OAIAttribute getVacationDayBalance() const;
    void setVacationDayBalance(const OAIAttribute &vacation_day_balance);
    bool is_vacation_day_balance_Set() const;
    bool is_vacation_day_balance_Valid() const;

    OAIAttribute getWeeklyWorkingHours() const;
    void setWeeklyWorkingHours(const OAIAttribute &weekly_working_hours);
    bool is_weekly_working_hours_Set() const;
    bool is_weekly_working_hours_Valid() const;

    OAIWorkSchedule getWorkSchedule() const;
    void setWorkSchedule(const OAIWorkSchedule &work_schedule);
    bool is_work_schedule_Set() const;
    bool is_work_schedule_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAbsenceEntitlement m_absence_entitlement;
    bool m_absence_entitlement_isSet;
    bool m_absence_entitlement_isValid;

    OAIAttribute m_contract_end_date;
    bool m_contract_end_date_isSet;
    bool m_contract_end_date_isValid;

    OAICostCenters m_cost_centers;
    bool m_cost_centers_isSet;
    bool m_cost_centers_isValid;

    OAIAttribute m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    OAIDepartment m_department;
    bool m_department_isSet;
    bool m_department_isValid;

    OAIAttribute m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    OAIAttribute m_employment_type;
    bool m_employment_type_isSet;
    bool m_employment_type_isValid;

    OAIAttribute m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    OAIAttribute m_fix_salary;
    bool m_fix_salary_isSet;
    bool m_fix_salary_isValid;

    OAIAttribute m_gender;
    bool m_gender_isSet;
    bool m_gender_isValid;

    OAIAttribute m_hire_date;
    bool m_hire_date_isSet;
    bool m_hire_date_isValid;

    OAIHolidayCalendar m_holiday_calendar;
    bool m_holiday_calendar_isSet;
    bool m_holiday_calendar_isValid;

    OAIAttribute m_hourly_salary;
    bool m_hourly_salary_isSet;
    bool m_hourly_salary_isValid;

    OAIAttribute m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIAttribute m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    OAIOffice m_office;
    bool m_office_isSet;
    bool m_office_isValid;

    OAIAttribute m_position;
    bool m_position_isSet;
    bool m_position_isValid;

    OAIAttribute m_probation_period_end;
    bool m_probation_period_end_isSet;
    bool m_probation_period_end_isValid;

    OAIAttribute m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    OAISupervisor m_supervisor;
    bool m_supervisor_isSet;
    bool m_supervisor_isValid;

    OAIAttribute m_termination_date;
    bool m_termination_date_isSet;
    bool m_termination_date_isValid;

    OAIAttribute m_termination_reason;
    bool m_termination_reason_isSet;
    bool m_termination_reason_isValid;

    OAIAttribute m_termination_type;
    bool m_termination_type_isSet;
    bool m_termination_type_isValid;

    OAIAttribute m_vacation_day_balance;
    bool m_vacation_day_balance_isSet;
    bool m_vacation_day_balance_isValid;

    OAIAttribute m_weekly_working_hours;
    bool m_weekly_working_hours_isSet;
    bool m_weekly_working_hours_isValid;

    OAIWorkSchedule m_work_schedule;
    bool m_work_schedule_isSet;
    bool m_work_schedule_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEmployee_attributes_inner)

#endif // OAIEmployee_attributes_inner_H
