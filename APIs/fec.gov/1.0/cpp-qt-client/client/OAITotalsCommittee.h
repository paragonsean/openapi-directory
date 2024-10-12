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
 * OAITotalsCommittee.h
 *
 * 
 */

#ifndef OAITotalsCommittee_H
#define OAITotalsCommittee_H

#include <QJsonObject>

#include "OAICommitteeDetail_jfc_committee_inner.h"
#include <QDate>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICommitteeDetail_jfc_committee_inner;

class OAITotalsCommittee : public OAIObject {
public:
    OAITotalsCommittee();
    OAITotalsCommittee(QString json);
    ~OAITotalsCommittee() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAffiliatedCommitteeName() const;
    void setAffiliatedCommitteeName(const QString &affiliated_committee_name);
    bool is_affiliated_committee_name_Set() const;
    bool is_affiliated_committee_name_Valid() const;

    QList<QString> getCandidateIds() const;
    void setCandidateIds(const QList<QString> &candidate_ids);
    bool is_candidate_ids_Set() const;
    bool is_candidate_ids_Valid() const;

    double getCashOnHandEndPeriod() const;
    void setCashOnHandEndPeriod(const double &cash_on_hand_end_period);
    bool is_cash_on_hand_end_period_Set() const;
    bool is_cash_on_hand_end_period_Valid() const;

    QString getCity() const;
    void setCity(const QString &city);
    bool is_city_Set() const;
    bool is_city_Valid() const;

    QString getCommitteeId() const;
    void setCommitteeId(const QString &committee_id);
    bool is_committee_id_Set() const;
    bool is_committee_id_Valid() const;

    QString getCommitteeType() const;
    void setCommitteeType(const QString &committee_type);
    bool is_committee_type_Set() const;
    bool is_committee_type_Valid() const;

    QString getCommitteeTypeFull() const;
    void setCommitteeTypeFull(const QString &committee_type_full);
    bool is_committee_type_full_Set() const;
    bool is_committee_type_full_Valid() const;

    qint32 getCycle() const;
    void setCycle(const qint32 &cycle);
    bool is_cycle_Set() const;
    bool is_cycle_Valid() const;

    QList<qint32> getCycles() const;
    void setCycles(const QList<qint32> &cycles);
    bool is_cycles_Set() const;
    bool is_cycles_Valid() const;

    QList<qint32> getCyclesHasActivity() const;
    void setCyclesHasActivity(const QList<qint32> &cycles_has_activity);
    bool is_cycles_has_activity_Set() const;
    bool is_cycles_has_activity_Valid() const;

    QList<qint32> getCyclesHasFinancial() const;
    void setCyclesHasFinancial(const QList<qint32> &cycles_has_financial);
    bool is_cycles_has_financial_Set() const;
    bool is_cycles_has_financial_Valid() const;

    double getDebtsOwedByCommittee() const;
    void setDebtsOwedByCommittee(const double &debts_owed_by_committee);
    bool is_debts_owed_by_committee_Set() const;
    bool is_debts_owed_by_committee_Valid() const;

    QString getDesignation() const;
    void setDesignation(const QString &designation);
    bool is_designation_Set() const;
    bool is_designation_Valid() const;

    QString getDesignationFull() const;
    void setDesignationFull(const QString &designation_full);
    bool is_designation_full_Set() const;
    bool is_designation_full_Valid() const;

    double getDisbursements() const;
    void setDisbursements(const double &disbursements);
    bool is_disbursements_Set() const;
    bool is_disbursements_Valid() const;

    QString getFilingFrequency() const;
    void setFilingFrequency(const QString &filing_frequency);
    bool is_filing_frequency_Set() const;
    bool is_filing_frequency_Valid() const;

    QDate getFirstF1Date() const;
    void setFirstF1Date(const QDate &first_f1_date);
    bool is_first_f1_date_Set() const;
    bool is_first_f1_date_Valid() const;

    QDate getFirstFileDate() const;
    void setFirstFileDate(const QDate &first_file_date);
    bool is_first_file_date_Set() const;
    bool is_first_file_date_Valid() const;

    double getIndependentExpenditures() const;
    void setIndependentExpenditures(const double &independent_expenditures);
    bool is_independent_expenditures_Set() const;
    bool is_independent_expenditures_Valid() const;

    bool isIsActive() const;
    void setIsActive(const bool &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    QList<OAICommitteeDetail_jfc_committee_inner> getJfcCommittee() const;
    void setJfcCommittee(const QList<OAICommitteeDetail_jfc_committee_inner> &jfc_committee);
    bool is_jfc_committee_Set() const;
    bool is_jfc_committee_Valid() const;

    qint32 getLastCycleHasActivity() const;
    void setLastCycleHasActivity(const qint32 &last_cycle_has_activity);
    bool is_last_cycle_has_activity_Set() const;
    bool is_last_cycle_has_activity_Valid() const;

    qint32 getLastCycleHasFinancial() const;
    void setLastCycleHasFinancial(const qint32 &last_cycle_has_financial);
    bool is_last_cycle_has_financial_Set() const;
    bool is_last_cycle_has_financial_Valid() const;

    QDate getLastF1Date() const;
    void setLastF1Date(const QDate &last_f1_date);
    bool is_last_f1_date_Set() const;
    bool is_last_f1_date_Valid() const;

    QDate getLastFileDate() const;
    void setLastFileDate(const QDate &last_file_date);
    bool is_last_file_date_Set() const;
    bool is_last_file_date_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOrganizationType() const;
    void setOrganizationType(const QString &organization_type);
    bool is_organization_type_Set() const;
    bool is_organization_type_Valid() const;

    QString getOrganizationTypeFull() const;
    void setOrganizationTypeFull(const QString &organization_type_full);
    bool is_organization_type_full_Set() const;
    bool is_organization_type_full_Valid() const;

    QString getParty() const;
    void setParty(const QString &party);
    bool is_party_Set() const;
    bool is_party_Valid() const;

    QString getPartyFull() const;
    void setPartyFull(const QString &party_full);
    bool is_party_full_Set() const;
    bool is_party_full_Valid() const;

    double getReceipts() const;
    void setReceipts(const double &receipts);
    bool is_receipts_Set() const;
    bool is_receipts_Valid() const;

    QString getState() const;
    void setState(const QString &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QString getStateFull() const;
    void setStateFull(const QString &state_full);
    bool is_state_full_Set() const;
    bool is_state_full_Valid() const;

    QString getStreet1() const;
    void setStreet1(const QString &street_1);
    bool is_street_1_Set() const;
    bool is_street_1_Valid() const;

    QString getStreet2() const;
    void setStreet2(const QString &street_2);
    bool is_street_2_Set() const;
    bool is_street_2_Valid() const;

    QString getTreasurerName() const;
    void setTreasurerName(const QString &treasurer_name);
    bool is_treasurer_name_Set() const;
    bool is_treasurer_name_Valid() const;

    QString getZip() const;
    void setZip(const QString &zip);
    bool is_zip_Set() const;
    bool is_zip_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_affiliated_committee_name;
    bool m_affiliated_committee_name_isSet;
    bool m_affiliated_committee_name_isValid;

    QList<QString> m_candidate_ids;
    bool m_candidate_ids_isSet;
    bool m_candidate_ids_isValid;

    double m_cash_on_hand_end_period;
    bool m_cash_on_hand_end_period_isSet;
    bool m_cash_on_hand_end_period_isValid;

    QString m_city;
    bool m_city_isSet;
    bool m_city_isValid;

    QString m_committee_id;
    bool m_committee_id_isSet;
    bool m_committee_id_isValid;

    QString m_committee_type;
    bool m_committee_type_isSet;
    bool m_committee_type_isValid;

    QString m_committee_type_full;
    bool m_committee_type_full_isSet;
    bool m_committee_type_full_isValid;

    qint32 m_cycle;
    bool m_cycle_isSet;
    bool m_cycle_isValid;

    QList<qint32> m_cycles;
    bool m_cycles_isSet;
    bool m_cycles_isValid;

    QList<qint32> m_cycles_has_activity;
    bool m_cycles_has_activity_isSet;
    bool m_cycles_has_activity_isValid;

    QList<qint32> m_cycles_has_financial;
    bool m_cycles_has_financial_isSet;
    bool m_cycles_has_financial_isValid;

    double m_debts_owed_by_committee;
    bool m_debts_owed_by_committee_isSet;
    bool m_debts_owed_by_committee_isValid;

    QString m_designation;
    bool m_designation_isSet;
    bool m_designation_isValid;

    QString m_designation_full;
    bool m_designation_full_isSet;
    bool m_designation_full_isValid;

    double m_disbursements;
    bool m_disbursements_isSet;
    bool m_disbursements_isValid;

    QString m_filing_frequency;
    bool m_filing_frequency_isSet;
    bool m_filing_frequency_isValid;

    QDate m_first_f1_date;
    bool m_first_f1_date_isSet;
    bool m_first_f1_date_isValid;

    QDate m_first_file_date;
    bool m_first_file_date_isSet;
    bool m_first_file_date_isValid;

    double m_independent_expenditures;
    bool m_independent_expenditures_isSet;
    bool m_independent_expenditures_isValid;

    bool m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    QList<OAICommitteeDetail_jfc_committee_inner> m_jfc_committee;
    bool m_jfc_committee_isSet;
    bool m_jfc_committee_isValid;

    qint32 m_last_cycle_has_activity;
    bool m_last_cycle_has_activity_isSet;
    bool m_last_cycle_has_activity_isValid;

    qint32 m_last_cycle_has_financial;
    bool m_last_cycle_has_financial_isSet;
    bool m_last_cycle_has_financial_isValid;

    QDate m_last_f1_date;
    bool m_last_f1_date_isSet;
    bool m_last_f1_date_isValid;

    QDate m_last_file_date;
    bool m_last_file_date_isSet;
    bool m_last_file_date_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_organization_type;
    bool m_organization_type_isSet;
    bool m_organization_type_isValid;

    QString m_organization_type_full;
    bool m_organization_type_full_isSet;
    bool m_organization_type_full_isValid;

    QString m_party;
    bool m_party_isSet;
    bool m_party_isValid;

    QString m_party_full;
    bool m_party_full_isSet;
    bool m_party_full_isValid;

    double m_receipts;
    bool m_receipts_isSet;
    bool m_receipts_isValid;

    QString m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QString m_state_full;
    bool m_state_full_isSet;
    bool m_state_full_isValid;

    QString m_street_1;
    bool m_street_1_isSet;
    bool m_street_1_isValid;

    QString m_street_2;
    bool m_street_2_isSet;
    bool m_street_2_isValid;

    QString m_treasurer_name;
    bool m_treasurer_name_isSet;
    bool m_treasurer_name_isValid;

    QString m_zip;
    bool m_zip_isSet;
    bool m_zip_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITotalsCommittee)

#endif // OAITotalsCommittee_H
