/**
 * OpenFEC
 * This application programming interface (API) allows you to explore the way candidates and committees fund their campaigns.    The Federal Election Commission (FEC) API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There are a lot of data, and a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in the `/schedule_a/` endpoints.    <b class=\"body\" id=\"getting_started_head\">Getting started with the openFEC API</b><br>    If you would like to use the FEC's API programmatically, you can sign up for your own API key using our form. Alternatively, you can still try out our API without an API key by using the web interface and using DEMO_KEY. Note that when you use the openFEC API you are subject to the [Terms of Service](https://github.com/fecgov/FEC/blob/master/TERMS-OF-SERVICE.md) and [Acceptable Use policy](https://github.com/fecgov/FEC/blob/master/ACCEPTABLE-USE-POLICY.md).    Signing up for an API key will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 7,200 calls an hour (120 calls per minute) to <a href=\"mailto:APIinfo@fec.gov\">APIinfo@fec.gov</a>. You can also ask questions and discuss the data in a community led [group](https://groups.google.com/forum/#!forum/fec-data).    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [Inspect our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!    <p><br></p> <h2 class=\"title\" id=\"signup_head\">Sign up for an API key</h2> <div id=\"apidatagov_signup\">Loading signup form...</div>
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAI_schedules_schedule_d__get_default_response_results_inner.h
 *
 * 
 */

#ifndef OAI_schedules_schedule_d__get_default_response_results_inner_H
#define OAI_schedules_schedule_d__get_default_response_results_inner_H

#include <QJsonObject>

#include "OAICommitteeHistory.h"
#include <QDate>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICommitteeHistory;

class OAI_schedules_schedule_d__get_default_response_results_inner : public OAIObject {
public:
    OAI_schedules_schedule_d__get_default_response_results_inner();
    OAI_schedules_schedule_d__get_default_response_results_inner(QString json);
    ~OAI_schedules_schedule_d__get_default_response_results_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getActionCode() const;
    void setActionCode(const QString &action_code);
    bool is_action_code_Set() const;
    bool is_action_code_Valid() const;

    QString getActionCodeFull() const;
    void setActionCodeFull(const QString &action_code_full);
    bool is_action_code_full_Set() const;
    bool is_action_code_full_Valid() const;

    float getAmountIncurredPeriod() const;
    void setAmountIncurredPeriod(const float &amount_incurred_period);
    bool is_amount_incurred_period_Set() const;
    bool is_amount_incurred_period_Valid() const;

    QString getCandidateFirstName() const;
    void setCandidateFirstName(const QString &candidate_first_name);
    bool is_candidate_first_name_Set() const;
    bool is_candidate_first_name_Valid() const;

    QString getCandidateId() const;
    void setCandidateId(const QString &candidate_id);
    bool is_candidate_id_Set() const;
    bool is_candidate_id_Valid() const;

    QString getCandidateLastName() const;
    void setCandidateLastName(const QString &candidate_last_name);
    bool is_candidate_last_name_Set() const;
    bool is_candidate_last_name_Valid() const;

    QString getCandidateName() const;
    void setCandidateName(const QString &candidate_name);
    bool is_candidate_name_Set() const;
    bool is_candidate_name_Valid() const;

    QString getCandidateOffice() const;
    void setCandidateOffice(const QString &candidate_office);
    bool is_candidate_office_Set() const;
    bool is_candidate_office_Valid() const;

    QString getCandidateOfficeDistrict() const;
    void setCandidateOfficeDistrict(const QString &candidate_office_district);
    bool is_candidate_office_district_Set() const;
    bool is_candidate_office_district_Valid() const;

    QString getCandidateOfficeState() const;
    void setCandidateOfficeState(const QString &candidate_office_state);
    bool is_candidate_office_state_Set() const;
    bool is_candidate_office_state_Valid() const;

    QString getCandidateOfficeStateFull() const;
    void setCandidateOfficeStateFull(const QString &candidate_office_state_full);
    bool is_candidate_office_state_full_Set() const;
    bool is_candidate_office_state_full_Valid() const;

    OAICommitteeHistory getCommittee() const;
    void setCommittee(const OAICommitteeHistory &committee);
    bool is_committee_Set() const;
    bool is_committee_Valid() const;

    QString getCommitteeId() const;
    void setCommitteeId(const QString &committee_id);
    bool is_committee_id_Set() const;
    bool is_committee_id_Valid() const;

    QString getCommitteeName() const;
    void setCommitteeName(const QString &committee_name);
    bool is_committee_name_Set() const;
    bool is_committee_name_Valid() const;

    QString getConduitCommitteeCity() const;
    void setConduitCommitteeCity(const QString &conduit_committee_city);
    bool is_conduit_committee_city_Set() const;
    bool is_conduit_committee_city_Valid() const;

    QString getConduitCommitteeId() const;
    void setConduitCommitteeId(const QString &conduit_committee_id);
    bool is_conduit_committee_id_Set() const;
    bool is_conduit_committee_id_Valid() const;

    QString getConduitCommitteeName() const;
    void setConduitCommitteeName(const QString &conduit_committee_name);
    bool is_conduit_committee_name_Set() const;
    bool is_conduit_committee_name_Valid() const;

    QString getConduitCommitteeState() const;
    void setConduitCommitteeState(const QString &conduit_committee_state);
    bool is_conduit_committee_state_Set() const;
    bool is_conduit_committee_state_Valid() const;

    QString getConduitCommitteeStreet1() const;
    void setConduitCommitteeStreet1(const QString &conduit_committee_street1);
    bool is_conduit_committee_street1_Set() const;
    bool is_conduit_committee_street1_Valid() const;

    QString getConduitCommitteeStreet2() const;
    void setConduitCommitteeStreet2(const QString &conduit_committee_street2);
    bool is_conduit_committee_street2_Set() const;
    bool is_conduit_committee_street2_Valid() const;

    qint32 getConduitCommitteeZip() const;
    void setConduitCommitteeZip(const qint32 &conduit_committee_zip);
    bool is_conduit_committee_zip_Set() const;
    bool is_conduit_committee_zip_Valid() const;

    QString getCreditorDebtorCity() const;
    void setCreditorDebtorCity(const QString &creditor_debtor_city);
    bool is_creditor_debtor_city_Set() const;
    bool is_creditor_debtor_city_Valid() const;

    QString getCreditorDebtorFirstName() const;
    void setCreditorDebtorFirstName(const QString &creditor_debtor_first_name);
    bool is_creditor_debtor_first_name_Set() const;
    bool is_creditor_debtor_first_name_Valid() const;

    QString getCreditorDebtorId() const;
    void setCreditorDebtorId(const QString &creditor_debtor_id);
    bool is_creditor_debtor_id_Set() const;
    bool is_creditor_debtor_id_Valid() const;

    QString getCreditorDebtorLastName() const;
    void setCreditorDebtorLastName(const QString &creditor_debtor_last_name);
    bool is_creditor_debtor_last_name_Set() const;
    bool is_creditor_debtor_last_name_Valid() const;

    QString getCreditorDebtorMiddleName() const;
    void setCreditorDebtorMiddleName(const QString &creditor_debtor_middle_name);
    bool is_creditor_debtor_middle_name_Set() const;
    bool is_creditor_debtor_middle_name_Valid() const;

    QString getCreditorDebtorName() const;
    void setCreditorDebtorName(const QString &creditor_debtor_name);
    bool is_creditor_debtor_name_Set() const;
    bool is_creditor_debtor_name_Valid() const;

    QString getCreditorDebtorPrefix() const;
    void setCreditorDebtorPrefix(const QString &creditor_debtor_prefix);
    bool is_creditor_debtor_prefix_Set() const;
    bool is_creditor_debtor_prefix_Valid() const;

    QString getCreditorDebtorState() const;
    void setCreditorDebtorState(const QString &creditor_debtor_state);
    bool is_creditor_debtor_state_Set() const;
    bool is_creditor_debtor_state_Valid() const;

    QString getCreditorDebtorStreet1() const;
    void setCreditorDebtorStreet1(const QString &creditor_debtor_street1);
    bool is_creditor_debtor_street1_Set() const;
    bool is_creditor_debtor_street1_Valid() const;

    QString getCreditorDebtorStreet2() const;
    void setCreditorDebtorStreet2(const QString &creditor_debtor_street2);
    bool is_creditor_debtor_street2_Set() const;
    bool is_creditor_debtor_street2_Valid() const;

    QString getCreditorDebtorSuffix() const;
    void setCreditorDebtorSuffix(const QString &creditor_debtor_suffix);
    bool is_creditor_debtor_suffix_Set() const;
    bool is_creditor_debtor_suffix_Valid() const;

    qint32 getElectionCycle() const;
    void setElectionCycle(const qint32 &election_cycle);
    bool is_election_cycle_Set() const;
    bool is_election_cycle_Valid() const;

    QString getEntityType() const;
    void setEntityType(const QString &entity_type);
    bool is_entity_type_Set() const;
    bool is_entity_type_Valid() const;

    qint32 getFileNumber() const;
    void setFileNumber(const qint32 &file_number);
    bool is_file_number_Set() const;
    bool is_file_number_Valid() const;

    QString getFilingForm() const;
    void setFilingForm(const QString &filing_form);
    bool is_filing_form_Set() const;
    bool is_filing_form_Valid() const;

    QString getImageNumber() const;
    void setImageNumber(const QString &image_number);
    bool is_image_number_Set() const;
    bool is_image_number_Valid() const;

    QString getLineNumber() const;
    void setLineNumber(const QString &line_number);
    bool is_line_number_Set() const;
    bool is_line_number_Valid() const;

    qint32 getLinkId() const;
    void setLinkId(const qint32 &link_id);
    bool is_link_id_Set() const;
    bool is_link_id_Valid() const;

    QDate getLoadDate() const;
    void setLoadDate(const QDate &load_date);
    bool is_load_date_Set() const;
    bool is_load_date_Valid() const;

    QString getNatureOfDebt() const;
    void setNatureOfDebt(const QString &nature_of_debt);
    bool is_nature_of_debt_Set() const;
    bool is_nature_of_debt_Valid() const;

    qint32 getOriginalSubId() const;
    void setOriginalSubId(const qint32 &original_sub_id);
    bool is_original_sub_id_Set() const;
    bool is_original_sub_id_Valid() const;

    float getOutstandingBalanceBeginningOfPeriod() const;
    void setOutstandingBalanceBeginningOfPeriod(const float &outstanding_balance_beginning_of_period);
    bool is_outstanding_balance_beginning_of_period_Set() const;
    bool is_outstanding_balance_beginning_of_period_Valid() const;

    float getOutstandingBalanceCloseOfPeriod() const;
    void setOutstandingBalanceCloseOfPeriod(const float &outstanding_balance_close_of_period);
    bool is_outstanding_balance_close_of_period_Set() const;
    bool is_outstanding_balance_close_of_period_Valid() const;

    float getPaymentPeriod() const;
    void setPaymentPeriod(const float &payment_period);
    bool is_payment_period_Set() const;
    bool is_payment_period_Valid() const;

    QString getPdfUrl() const;
    void setPdfUrl(const QString &pdf_url);
    bool is_pdf_url_Set() const;
    bool is_pdf_url_Valid() const;

    QString getReportType() const;
    void setReportType(const QString &report_type);
    bool is_report_type_Set() const;
    bool is_report_type_Valid() const;

    qint32 getReportYear() const;
    void setReportYear(const qint32 &report_year);
    bool is_report_year_Set() const;
    bool is_report_year_Valid() const;

    QString getScheduleType() const;
    void setScheduleType(const QString &schedule_type);
    bool is_schedule_type_Set() const;
    bool is_schedule_type_Valid() const;

    QString getScheduleTypeFull() const;
    void setScheduleTypeFull(const QString &schedule_type_full);
    bool is_schedule_type_full_Set() const;
    bool is_schedule_type_full_Valid() const;

    QString getSubId() const;
    void setSubId(const QString &sub_id);
    bool is_sub_id_Set() const;
    bool is_sub_id_Valid() const;

    QString getTransactionId() const;
    void setTransactionId(const QString &transaction_id);
    bool is_transaction_id_Set() const;
    bool is_transaction_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_action_code;
    bool m_action_code_isSet;
    bool m_action_code_isValid;

    QString m_action_code_full;
    bool m_action_code_full_isSet;
    bool m_action_code_full_isValid;

    float m_amount_incurred_period;
    bool m_amount_incurred_period_isSet;
    bool m_amount_incurred_period_isValid;

    QString m_candidate_first_name;
    bool m_candidate_first_name_isSet;
    bool m_candidate_first_name_isValid;

    QString m_candidate_id;
    bool m_candidate_id_isSet;
    bool m_candidate_id_isValid;

    QString m_candidate_last_name;
    bool m_candidate_last_name_isSet;
    bool m_candidate_last_name_isValid;

    QString m_candidate_name;
    bool m_candidate_name_isSet;
    bool m_candidate_name_isValid;

    QString m_candidate_office;
    bool m_candidate_office_isSet;
    bool m_candidate_office_isValid;

    QString m_candidate_office_district;
    bool m_candidate_office_district_isSet;
    bool m_candidate_office_district_isValid;

    QString m_candidate_office_state;
    bool m_candidate_office_state_isSet;
    bool m_candidate_office_state_isValid;

    QString m_candidate_office_state_full;
    bool m_candidate_office_state_full_isSet;
    bool m_candidate_office_state_full_isValid;

    OAICommitteeHistory m_committee;
    bool m_committee_isSet;
    bool m_committee_isValid;

    QString m_committee_id;
    bool m_committee_id_isSet;
    bool m_committee_id_isValid;

    QString m_committee_name;
    bool m_committee_name_isSet;
    bool m_committee_name_isValid;

    QString m_conduit_committee_city;
    bool m_conduit_committee_city_isSet;
    bool m_conduit_committee_city_isValid;

    QString m_conduit_committee_id;
    bool m_conduit_committee_id_isSet;
    bool m_conduit_committee_id_isValid;

    QString m_conduit_committee_name;
    bool m_conduit_committee_name_isSet;
    bool m_conduit_committee_name_isValid;

    QString m_conduit_committee_state;
    bool m_conduit_committee_state_isSet;
    bool m_conduit_committee_state_isValid;

    QString m_conduit_committee_street1;
    bool m_conduit_committee_street1_isSet;
    bool m_conduit_committee_street1_isValid;

    QString m_conduit_committee_street2;
    bool m_conduit_committee_street2_isSet;
    bool m_conduit_committee_street2_isValid;

    qint32 m_conduit_committee_zip;
    bool m_conduit_committee_zip_isSet;
    bool m_conduit_committee_zip_isValid;

    QString m_creditor_debtor_city;
    bool m_creditor_debtor_city_isSet;
    bool m_creditor_debtor_city_isValid;

    QString m_creditor_debtor_first_name;
    bool m_creditor_debtor_first_name_isSet;
    bool m_creditor_debtor_first_name_isValid;

    QString m_creditor_debtor_id;
    bool m_creditor_debtor_id_isSet;
    bool m_creditor_debtor_id_isValid;

    QString m_creditor_debtor_last_name;
    bool m_creditor_debtor_last_name_isSet;
    bool m_creditor_debtor_last_name_isValid;

    QString m_creditor_debtor_middle_name;
    bool m_creditor_debtor_middle_name_isSet;
    bool m_creditor_debtor_middle_name_isValid;

    QString m_creditor_debtor_name;
    bool m_creditor_debtor_name_isSet;
    bool m_creditor_debtor_name_isValid;

    QString m_creditor_debtor_prefix;
    bool m_creditor_debtor_prefix_isSet;
    bool m_creditor_debtor_prefix_isValid;

    QString m_creditor_debtor_state;
    bool m_creditor_debtor_state_isSet;
    bool m_creditor_debtor_state_isValid;

    QString m_creditor_debtor_street1;
    bool m_creditor_debtor_street1_isSet;
    bool m_creditor_debtor_street1_isValid;

    QString m_creditor_debtor_street2;
    bool m_creditor_debtor_street2_isSet;
    bool m_creditor_debtor_street2_isValid;

    QString m_creditor_debtor_suffix;
    bool m_creditor_debtor_suffix_isSet;
    bool m_creditor_debtor_suffix_isValid;

    qint32 m_election_cycle;
    bool m_election_cycle_isSet;
    bool m_election_cycle_isValid;

    QString m_entity_type;
    bool m_entity_type_isSet;
    bool m_entity_type_isValid;

    qint32 m_file_number;
    bool m_file_number_isSet;
    bool m_file_number_isValid;

    QString m_filing_form;
    bool m_filing_form_isSet;
    bool m_filing_form_isValid;

    QString m_image_number;
    bool m_image_number_isSet;
    bool m_image_number_isValid;

    QString m_line_number;
    bool m_line_number_isSet;
    bool m_line_number_isValid;

    qint32 m_link_id;
    bool m_link_id_isSet;
    bool m_link_id_isValid;

    QDate m_load_date;
    bool m_load_date_isSet;
    bool m_load_date_isValid;

    QString m_nature_of_debt;
    bool m_nature_of_debt_isSet;
    bool m_nature_of_debt_isValid;

    qint32 m_original_sub_id;
    bool m_original_sub_id_isSet;
    bool m_original_sub_id_isValid;

    float m_outstanding_balance_beginning_of_period;
    bool m_outstanding_balance_beginning_of_period_isSet;
    bool m_outstanding_balance_beginning_of_period_isValid;

    float m_outstanding_balance_close_of_period;
    bool m_outstanding_balance_close_of_period_isSet;
    bool m_outstanding_balance_close_of_period_isValid;

    float m_payment_period;
    bool m_payment_period_isSet;
    bool m_payment_period_isValid;

    QString m_pdf_url;
    bool m_pdf_url_isSet;
    bool m_pdf_url_isValid;

    QString m_report_type;
    bool m_report_type_isSet;
    bool m_report_type_isValid;

    qint32 m_report_year;
    bool m_report_year_isSet;
    bool m_report_year_isValid;

    QString m_schedule_type;
    bool m_schedule_type_isSet;
    bool m_schedule_type_isValid;

    QString m_schedule_type_full;
    bool m_schedule_type_full_isSet;
    bool m_schedule_type_full_isValid;

    QString m_sub_id;
    bool m_sub_id_isSet;
    bool m_sub_id_isValid;

    QString m_transaction_id;
    bool m_transaction_id_isSet;
    bool m_transaction_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_schedules_schedule_d__get_default_response_results_inner)

#endif // OAI_schedules_schedule_d__get_default_response_results_inner_H
