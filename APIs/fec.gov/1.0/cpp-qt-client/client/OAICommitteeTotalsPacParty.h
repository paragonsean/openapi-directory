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
 * OAICommitteeTotalsPacParty.h
 *
 * 
 */

#ifndef OAICommitteeTotalsPacParty_H
#define OAICommitteeTotalsPacParty_H

#include <QJsonObject>

#include "OAICommittee_sponsor_candidate_list_inner.h"
#include <QDate>
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICommittee_sponsor_candidate_list_inner;

class OAICommitteeTotalsPacParty : public OAIObject {
public:
    OAICommitteeTotalsPacParty();
    OAICommitteeTotalsPacParty(QString json);
    ~OAICommitteeTotalsPacParty() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getAllLoansReceived() const;
    void setAllLoansReceived(const double &all_loans_received);
    bool is_all_loans_received_Set() const;
    bool is_all_loans_received_Valid() const;

    double getAllocatedFederalElectionLevinShare() const;
    void setAllocatedFederalElectionLevinShare(const double &allocated_federal_election_levin_share);
    bool is_allocated_federal_election_levin_share_Set() const;
    bool is_allocated_federal_election_levin_share_Valid() const;

    double getCashOnHandBeginningPeriod() const;
    void setCashOnHandBeginningPeriod(const double &cash_on_hand_beginning_period);
    bool is_cash_on_hand_beginning_period_Set() const;
    bool is_cash_on_hand_beginning_period_Valid() const;

    QString getCommitteeDesignation() const;
    void setCommitteeDesignation(const QString &committee_designation);
    bool is_committee_designation_Set() const;
    bool is_committee_designation_Valid() const;

    QString getCommitteeDesignationFull() const;
    void setCommitteeDesignationFull(const QString &committee_designation_full);
    bool is_committee_designation_full_Set() const;
    bool is_committee_designation_full_Valid() const;

    QString getCommitteeId() const;
    void setCommitteeId(const QString &committee_id);
    bool is_committee_id_Set() const;
    bool is_committee_id_Valid() const;

    QString getCommitteeName() const;
    void setCommitteeName(const QString &committee_name);
    bool is_committee_name_Set() const;
    bool is_committee_name_Valid() const;

    QString getCommitteeState() const;
    void setCommitteeState(const QString &committee_state);
    bool is_committee_state_Set() const;
    bool is_committee_state_Valid() const;

    QString getCommitteeType() const;
    void setCommitteeType(const QString &committee_type);
    bool is_committee_type_Set() const;
    bool is_committee_type_Valid() const;

    QString getCommitteeTypeFull() const;
    void setCommitteeTypeFull(const QString &committee_type_full);
    bool is_committee_type_full_Set() const;
    bool is_committee_type_full_Valid() const;

    double getContributionRefunds() const;
    void setContributionRefunds(const double &contribution_refunds);
    bool is_contribution_refunds_Set() const;
    bool is_contribution_refunds_Valid() const;

    double getContributions() const;
    void setContributions(const double &contributions);
    bool is_contributions_Set() const;
    bool is_contributions_Valid() const;

    double getContributionsIeAndPartyExpendituresMadePercent() const;
    void setContributionsIeAndPartyExpendituresMadePercent(const double &contributions_ie_and_party_expenditures_made_percent);
    bool is_contributions_ie_and_party_expenditures_made_percent_Set() const;
    bool is_contributions_ie_and_party_expenditures_made_percent_Valid() const;

    double getConventionExp() const;
    void setConventionExp(const double &convention_exp);
    bool is_convention_exp_Set() const;
    bool is_convention_exp_Valid() const;

    double getCoordinatedExpendituresByPartyCommittee() const;
    void setCoordinatedExpendituresByPartyCommittee(const double &coordinated_expenditures_by_party_committee);
    bool is_coordinated_expenditures_by_party_committee_Set() const;
    bool is_coordinated_expenditures_by_party_committee_Valid() const;

    QDateTime getCoverageEndDate() const;
    void setCoverageEndDate(const QDateTime &coverage_end_date);
    bool is_coverage_end_date_Set() const;
    bool is_coverage_end_date_Valid() const;

    QDateTime getCoverageStartDate() const;
    void setCoverageStartDate(const QDateTime &coverage_start_date);
    bool is_coverage_start_date_Set() const;
    bool is_coverage_start_date_Valid() const;

    qint32 getCycle() const;
    void setCycle(const qint32 &cycle);
    bool is_cycle_Set() const;
    bool is_cycle_Valid() const;

    double getDisbursements() const;
    void setDisbursements(const double &disbursements);
    bool is_disbursements_Set() const;
    bool is_disbursements_Valid() const;

    double getExpPriorYearsSubjectLimits() const;
    void setExpPriorYearsSubjectLimits(const double &exp_prior_years_subject_limits);
    bool is_exp_prior_years_subject_limits_Set() const;
    bool is_exp_prior_years_subject_limits_Valid() const;

    double getExpSubjectLimits() const;
    void setExpSubjectLimits(const double &exp_subject_limits);
    bool is_exp_subject_limits_Set() const;
    bool is_exp_subject_limits_Valid() const;

    double getFedCandidateCommitteeContributions() const;
    void setFedCandidateCommitteeContributions(const double &fed_candidate_committee_contributions);
    bool is_fed_candidate_committee_contributions_Set() const;
    bool is_fed_candidate_committee_contributions_Valid() const;

    double getFedCandidateContributionRefunds() const;
    void setFedCandidateContributionRefunds(const double &fed_candidate_contribution_refunds);
    bool is_fed_candidate_contribution_refunds_Set() const;
    bool is_fed_candidate_contribution_refunds_Valid() const;

    double getFedDisbursements() const;
    void setFedDisbursements(const double &fed_disbursements);
    bool is_fed_disbursements_Set() const;
    bool is_fed_disbursements_Valid() const;

    double getFedElectionActivity() const;
    void setFedElectionActivity(const double &fed_election_activity);
    bool is_fed_election_activity_Set() const;
    bool is_fed_election_activity_Valid() const;

    double getFedOperatingExpenditures() const;
    void setFedOperatingExpenditures(const double &fed_operating_expenditures);
    bool is_fed_operating_expenditures_Set() const;
    bool is_fed_operating_expenditures_Valid() const;

    double getFedReceipts() const;
    void setFedReceipts(const double &fed_receipts);
    bool is_fed_receipts_Set() const;
    bool is_fed_receipts_Valid() const;

    double getFederalFunds() const;
    void setFederalFunds(const double &federal_funds);
    bool is_federal_funds_Set() const;
    bool is_federal_funds_Valid() const;

    QString getFilingFrequency() const;
    void setFilingFrequency(const QString &filing_frequency);
    bool is_filing_frequency_Set() const;
    bool is_filing_frequency_Valid() const;

    QString getFilingFrequencyFull() const;
    void setFilingFrequencyFull(const QString &filing_frequency_full);
    bool is_filing_frequency_full_Set() const;
    bool is_filing_frequency_full_Valid() const;

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

    double getIndividualContributions() const;
    void setIndividualContributions(const double &individual_contributions);
    bool is_individual_contributions_Set() const;
    bool is_individual_contributions_Valid() const;

    double getIndividualContributionsPercent() const;
    void setIndividualContributionsPercent(const double &individual_contributions_percent);
    bool is_individual_contributions_percent_Set() const;
    bool is_individual_contributions_percent_Valid() const;

    double getIndividualItemizedContributions() const;
    void setIndividualItemizedContributions(const double &individual_itemized_contributions);
    bool is_individual_itemized_contributions_Set() const;
    bool is_individual_itemized_contributions_Valid() const;

    double getIndividualUnitemizedContributions() const;
    void setIndividualUnitemizedContributions(const double &individual_unitemized_contributions);
    bool is_individual_unitemized_contributions_Set() const;
    bool is_individual_unitemized_contributions_Valid() const;

    double getItemizedConventionExp() const;
    void setItemizedConventionExp(const double &itemized_convention_exp);
    bool is_itemized_convention_exp_Set() const;
    bool is_itemized_convention_exp_Valid() const;

    double getItemizedOtherDisb() const;
    void setItemizedOtherDisb(const double &itemized_other_disb);
    bool is_itemized_other_disb_Set() const;
    bool is_itemized_other_disb_Valid() const;

    double getItemizedOtherIncome() const;
    void setItemizedOtherIncome(const double &itemized_other_income);
    bool is_itemized_other_income_Set() const;
    bool is_itemized_other_income_Valid() const;

    double getItemizedOtherRefunds() const;
    void setItemizedOtherRefunds(const double &itemized_other_refunds);
    bool is_itemized_other_refunds_Set() const;
    bool is_itemized_other_refunds_Valid() const;

    double getItemizedRefundsRelatingConventionExp() const;
    void setItemizedRefundsRelatingConventionExp(const double &itemized_refunds_relating_convention_exp);
    bool is_itemized_refunds_relating_convention_exp_Set() const;
    bool is_itemized_refunds_relating_convention_exp_Valid() const;

    QString getLastBeginningImageNumber() const;
    void setLastBeginningImageNumber(const QString &last_beginning_image_number);
    bool is_last_beginning_image_number_Set() const;
    bool is_last_beginning_image_number_Valid() const;

    double getLastCashOnHandEndPeriod() const;
    void setLastCashOnHandEndPeriod(const double &last_cash_on_hand_end_period);
    bool is_last_cash_on_hand_end_period_Set() const;
    bool is_last_cash_on_hand_end_period_Valid() const;

    double getLastDebtsOwedByCommittee() const;
    void setLastDebtsOwedByCommittee(const double &last_debts_owed_by_committee);
    bool is_last_debts_owed_by_committee_Set() const;
    bool is_last_debts_owed_by_committee_Valid() const;

    double getLastDebtsOwedToCommittee() const;
    void setLastDebtsOwedToCommittee(const double &last_debts_owed_to_committee);
    bool is_last_debts_owed_to_committee_Set() const;
    bool is_last_debts_owed_to_committee_Valid() const;

    QString getLastReportTypeFull() const;
    void setLastReportTypeFull(const QString &last_report_type_full);
    bool is_last_report_type_full_Set() const;
    bool is_last_report_type_full_Valid() const;

    qint32 getLastReportYear() const;
    void setLastReportYear(const qint32 &last_report_year);
    bool is_last_report_year_Set() const;
    bool is_last_report_year_Valid() const;

    double getLoanRepaymentsMade() const;
    void setLoanRepaymentsMade(const double &loan_repayments_made);
    bool is_loan_repayments_made_Set() const;
    bool is_loan_repayments_made_Valid() const;

    double getLoanRepaymentsReceived() const;
    void setLoanRepaymentsReceived(const double &loan_repayments_received);
    bool is_loan_repayments_received_Set() const;
    bool is_loan_repayments_received_Valid() const;

    double getLoansAndLoanRepaymentsMade() const;
    void setLoansAndLoanRepaymentsMade(const double &loans_and_loan_repayments_made);
    bool is_loans_and_loan_repayments_made_Set() const;
    bool is_loans_and_loan_repayments_made_Valid() const;

    double getLoansAndLoanRepaymentsReceived() const;
    void setLoansAndLoanRepaymentsReceived(const double &loans_and_loan_repayments_received);
    bool is_loans_and_loan_repayments_received_Set() const;
    bool is_loans_and_loan_repayments_received_Valid() const;

    double getLoansMade() const;
    void setLoansMade(const double &loans_made);
    bool is_loans_made_Set() const;
    bool is_loans_made_Valid() const;

    double getNetContributions() const;
    void setNetContributions(const double &net_contributions);
    bool is_net_contributions_Set() const;
    bool is_net_contributions_Valid() const;

    double getNetOperatingExpenditures() const;
    void setNetOperatingExpenditures(const double &net_operating_expenditures);
    bool is_net_operating_expenditures_Set() const;
    bool is_net_operating_expenditures_Valid() const;

    double getNonAllocatedFedElectionActivity() const;
    void setNonAllocatedFedElectionActivity(const double &non_allocated_fed_election_activity);
    bool is_non_allocated_fed_election_activity_Set() const;
    bool is_non_allocated_fed_election_activity_Valid() const;

    double getOffsetsToOperatingExpenditures() const;
    void setOffsetsToOperatingExpenditures(const double &offsets_to_operating_expenditures);
    bool is_offsets_to_operating_expenditures_Set() const;
    bool is_offsets_to_operating_expenditures_Valid() const;

    double getOperatingExpenditures() const;
    void setOperatingExpenditures(const double &operating_expenditures);
    bool is_operating_expenditures_Set() const;
    bool is_operating_expenditures_Valid() const;

    double getOperatingExpendituresPercent() const;
    void setOperatingExpendituresPercent(const double &operating_expenditures_percent);
    bool is_operating_expenditures_percent_Set() const;
    bool is_operating_expenditures_percent_Valid() const;

    QString getOrganizationType() const;
    void setOrganizationType(const QString &organization_type);
    bool is_organization_type_Set() const;
    bool is_organization_type_Valid() const;

    QString getOrganizationTypeFull() const;
    void setOrganizationTypeFull(const QString &organization_type_full);
    bool is_organization_type_full_Set() const;
    bool is_organization_type_full_Valid() const;

    double getOtherDisbursements() const;
    void setOtherDisbursements(const double &other_disbursements);
    bool is_other_disbursements_Set() const;
    bool is_other_disbursements_Valid() const;

    double getOtherFedOperatingExpenditures() const;
    void setOtherFedOperatingExpenditures(const double &other_fed_operating_expenditures);
    bool is_other_fed_operating_expenditures_Set() const;
    bool is_other_fed_operating_expenditures_Valid() const;

    double getOtherFedReceipts() const;
    void setOtherFedReceipts(const double &other_fed_receipts);
    bool is_other_fed_receipts_Set() const;
    bool is_other_fed_receipts_Valid() const;

    double getOtherPoliticalCommitteeContributions() const;
    void setOtherPoliticalCommitteeContributions(const double &other_political_committee_contributions);
    bool is_other_political_committee_contributions_Set() const;
    bool is_other_political_committee_contributions_Valid() const;

    double getOtherRefunds() const;
    void setOtherRefunds(const double &other_refunds);
    bool is_other_refunds_Set() const;
    bool is_other_refunds_Valid() const;

    double getPartyAndOtherCommitteeContributionsPercent() const;
    void setPartyAndOtherCommitteeContributionsPercent(const double &party_and_other_committee_contributions_percent);
    bool is_party_and_other_committee_contributions_percent_Set() const;
    bool is_party_and_other_committee_contributions_percent_Valid() const;

    QString getPartyFull() const;
    void setPartyFull(const QString &party_full);
    bool is_party_full_Set() const;
    bool is_party_full_Valid() const;

    QString getPdfUrl() const;
    void setPdfUrl(const QString &pdf_url);
    bool is_pdf_url_Set() const;
    bool is_pdf_url_Valid() const;

    double getPoliticalPartyCommitteeContributions() const;
    void setPoliticalPartyCommitteeContributions(const double &political_party_committee_contributions);
    bool is_political_party_committee_contributions_Set() const;
    bool is_political_party_committee_contributions_Valid() const;

    double getReceipts() const;
    void setReceipts(const double &receipts);
    bool is_receipts_Set() const;
    bool is_receipts_Valid() const;

    double getRefundedIndividualContributions() const;
    void setRefundedIndividualContributions(const double &refunded_individual_contributions);
    bool is_refunded_individual_contributions_Set() const;
    bool is_refunded_individual_contributions_Valid() const;

    double getRefundedOtherPoliticalCommitteeContributions() const;
    void setRefundedOtherPoliticalCommitteeContributions(const double &refunded_other_political_committee_contributions);
    bool is_refunded_other_political_committee_contributions_Set() const;
    bool is_refunded_other_political_committee_contributions_Valid() const;

    double getRefundedPoliticalPartyCommitteeContributions() const;
    void setRefundedPoliticalPartyCommitteeContributions(const double &refunded_political_party_committee_contributions);
    bool is_refunded_political_party_committee_contributions_Set() const;
    bool is_refunded_political_party_committee_contributions_Valid() const;

    double getRefundsRelatingConventionExp() const;
    void setRefundsRelatingConventionExp(const double &refunds_relating_convention_exp);
    bool is_refunds_relating_convention_exp_Set() const;
    bool is_refunds_relating_convention_exp_Valid() const;

    QString getReportForm() const;
    void setReportForm(const QString &report_form);
    bool is_report_form_Set() const;
    bool is_report_form_Valid() const;

    double getSharedFedActivity() const;
    void setSharedFedActivity(const double &shared_fed_activity);
    bool is_shared_fed_activity_Set() const;
    bool is_shared_fed_activity_Valid() const;

    double getSharedFedActivityNonfed() const;
    void setSharedFedActivityNonfed(const double &shared_fed_activity_nonfed);
    bool is_shared_fed_activity_nonfed_Set() const;
    bool is_shared_fed_activity_nonfed_Valid() const;

    double getSharedFedOperatingExpenditures() const;
    void setSharedFedOperatingExpenditures(const double &shared_fed_operating_expenditures);
    bool is_shared_fed_operating_expenditures_Set() const;
    bool is_shared_fed_operating_expenditures_Valid() const;

    double getSharedNonfedOperatingExpenditures() const;
    void setSharedNonfedOperatingExpenditures(const double &shared_nonfed_operating_expenditures);
    bool is_shared_nonfed_operating_expenditures_Set() const;
    bool is_shared_nonfed_operating_expenditures_Valid() const;

    QList<QString> getSponsorCandidateIds() const;
    void setSponsorCandidateIds(const QList<QString> &sponsor_candidate_ids);
    bool is_sponsor_candidate_ids_Set() const;
    bool is_sponsor_candidate_ids_Valid() const;

    QList<OAICommittee_sponsor_candidate_list_inner> getSponsorCandidateList() const;
    void setSponsorCandidateList(const QList<OAICommittee_sponsor_candidate_list_inner> &sponsor_candidate_list);
    bool is_sponsor_candidate_list_Set() const;
    bool is_sponsor_candidate_list_Valid() const;

    double getTotalExpSubjectLimits() const;
    void setTotalExpSubjectLimits(const double &total_exp_subject_limits);
    bool is_total_exp_subject_limits_Set() const;
    bool is_total_exp_subject_limits_Valid() const;

    double getTotalTransfers() const;
    void setTotalTransfers(const double &total_transfers);
    bool is_total_transfers_Set() const;
    bool is_total_transfers_Valid() const;

    QDate getTransactionCoverageDate() const;
    void setTransactionCoverageDate(const QDate &transaction_coverage_date);
    bool is_transaction_coverage_date_Set() const;
    bool is_transaction_coverage_date_Valid() const;

    double getTransfersFromAffiliatedParty() const;
    void setTransfersFromAffiliatedParty(const double &transfers_from_affiliated_party);
    bool is_transfers_from_affiliated_party_Set() const;
    bool is_transfers_from_affiliated_party_Valid() const;

    double getTransfersFromNonfedAccount() const;
    void setTransfersFromNonfedAccount(const double &transfers_from_nonfed_account);
    bool is_transfers_from_nonfed_account_Set() const;
    bool is_transfers_from_nonfed_account_Valid() const;

    double getTransfersFromNonfedLevin() const;
    void setTransfersFromNonfedLevin(const double &transfers_from_nonfed_levin);
    bool is_transfers_from_nonfed_levin_Set() const;
    bool is_transfers_from_nonfed_levin_Valid() const;

    double getTransfersToAffiliatedCommittee() const;
    void setTransfersToAffiliatedCommittee(const double &transfers_to_affiliated_committee);
    bool is_transfers_to_affiliated_committee_Set() const;
    bool is_transfers_to_affiliated_committee_Valid() const;

    QString getTreasurerName() const;
    void setTreasurerName(const QString &treasurer_name);
    bool is_treasurer_name_Set() const;
    bool is_treasurer_name_Valid() const;

    double getUnitemizedConventionExp() const;
    void setUnitemizedConventionExp(const double &unitemized_convention_exp);
    bool is_unitemized_convention_exp_Set() const;
    bool is_unitemized_convention_exp_Valid() const;

    double getUnitemizedOtherDisb() const;
    void setUnitemizedOtherDisb(const double &unitemized_other_disb);
    bool is_unitemized_other_disb_Set() const;
    bool is_unitemized_other_disb_Valid() const;

    double getUnitemizedOtherIncome() const;
    void setUnitemizedOtherIncome(const double &unitemized_other_income);
    bool is_unitemized_other_income_Set() const;
    bool is_unitemized_other_income_Valid() const;

    double getUnitemizedOtherRefunds() const;
    void setUnitemizedOtherRefunds(const double &unitemized_other_refunds);
    bool is_unitemized_other_refunds_Set() const;
    bool is_unitemized_other_refunds_Valid() const;

    double getUnitemizedRefundsRelatingConventionExp() const;
    void setUnitemizedRefundsRelatingConventionExp(const double &unitemized_refunds_relating_convention_exp);
    bool is_unitemized_refunds_relating_convention_exp_Set() const;
    bool is_unitemized_refunds_relating_convention_exp_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_all_loans_received;
    bool m_all_loans_received_isSet;
    bool m_all_loans_received_isValid;

    double m_allocated_federal_election_levin_share;
    bool m_allocated_federal_election_levin_share_isSet;
    bool m_allocated_federal_election_levin_share_isValid;

    double m_cash_on_hand_beginning_period;
    bool m_cash_on_hand_beginning_period_isSet;
    bool m_cash_on_hand_beginning_period_isValid;

    QString m_committee_designation;
    bool m_committee_designation_isSet;
    bool m_committee_designation_isValid;

    QString m_committee_designation_full;
    bool m_committee_designation_full_isSet;
    bool m_committee_designation_full_isValid;

    QString m_committee_id;
    bool m_committee_id_isSet;
    bool m_committee_id_isValid;

    QString m_committee_name;
    bool m_committee_name_isSet;
    bool m_committee_name_isValid;

    QString m_committee_state;
    bool m_committee_state_isSet;
    bool m_committee_state_isValid;

    QString m_committee_type;
    bool m_committee_type_isSet;
    bool m_committee_type_isValid;

    QString m_committee_type_full;
    bool m_committee_type_full_isSet;
    bool m_committee_type_full_isValid;

    double m_contribution_refunds;
    bool m_contribution_refunds_isSet;
    bool m_contribution_refunds_isValid;

    double m_contributions;
    bool m_contributions_isSet;
    bool m_contributions_isValid;

    double m_contributions_ie_and_party_expenditures_made_percent;
    bool m_contributions_ie_and_party_expenditures_made_percent_isSet;
    bool m_contributions_ie_and_party_expenditures_made_percent_isValid;

    double m_convention_exp;
    bool m_convention_exp_isSet;
    bool m_convention_exp_isValid;

    double m_coordinated_expenditures_by_party_committee;
    bool m_coordinated_expenditures_by_party_committee_isSet;
    bool m_coordinated_expenditures_by_party_committee_isValid;

    QDateTime m_coverage_end_date;
    bool m_coverage_end_date_isSet;
    bool m_coverage_end_date_isValid;

    QDateTime m_coverage_start_date;
    bool m_coverage_start_date_isSet;
    bool m_coverage_start_date_isValid;

    qint32 m_cycle;
    bool m_cycle_isSet;
    bool m_cycle_isValid;

    double m_disbursements;
    bool m_disbursements_isSet;
    bool m_disbursements_isValid;

    double m_exp_prior_years_subject_limits;
    bool m_exp_prior_years_subject_limits_isSet;
    bool m_exp_prior_years_subject_limits_isValid;

    double m_exp_subject_limits;
    bool m_exp_subject_limits_isSet;
    bool m_exp_subject_limits_isValid;

    double m_fed_candidate_committee_contributions;
    bool m_fed_candidate_committee_contributions_isSet;
    bool m_fed_candidate_committee_contributions_isValid;

    double m_fed_candidate_contribution_refunds;
    bool m_fed_candidate_contribution_refunds_isSet;
    bool m_fed_candidate_contribution_refunds_isValid;

    double m_fed_disbursements;
    bool m_fed_disbursements_isSet;
    bool m_fed_disbursements_isValid;

    double m_fed_election_activity;
    bool m_fed_election_activity_isSet;
    bool m_fed_election_activity_isValid;

    double m_fed_operating_expenditures;
    bool m_fed_operating_expenditures_isSet;
    bool m_fed_operating_expenditures_isValid;

    double m_fed_receipts;
    bool m_fed_receipts_isSet;
    bool m_fed_receipts_isValid;

    double m_federal_funds;
    bool m_federal_funds_isSet;
    bool m_federal_funds_isValid;

    QString m_filing_frequency;
    bool m_filing_frequency_isSet;
    bool m_filing_frequency_isValid;

    QString m_filing_frequency_full;
    bool m_filing_frequency_full_isSet;
    bool m_filing_frequency_full_isValid;

    QDate m_first_f1_date;
    bool m_first_f1_date_isSet;
    bool m_first_f1_date_isValid;

    QDate m_first_file_date;
    bool m_first_file_date_isSet;
    bool m_first_file_date_isValid;

    double m_independent_expenditures;
    bool m_independent_expenditures_isSet;
    bool m_independent_expenditures_isValid;

    double m_individual_contributions;
    bool m_individual_contributions_isSet;
    bool m_individual_contributions_isValid;

    double m_individual_contributions_percent;
    bool m_individual_contributions_percent_isSet;
    bool m_individual_contributions_percent_isValid;

    double m_individual_itemized_contributions;
    bool m_individual_itemized_contributions_isSet;
    bool m_individual_itemized_contributions_isValid;

    double m_individual_unitemized_contributions;
    bool m_individual_unitemized_contributions_isSet;
    bool m_individual_unitemized_contributions_isValid;

    double m_itemized_convention_exp;
    bool m_itemized_convention_exp_isSet;
    bool m_itemized_convention_exp_isValid;

    double m_itemized_other_disb;
    bool m_itemized_other_disb_isSet;
    bool m_itemized_other_disb_isValid;

    double m_itemized_other_income;
    bool m_itemized_other_income_isSet;
    bool m_itemized_other_income_isValid;

    double m_itemized_other_refunds;
    bool m_itemized_other_refunds_isSet;
    bool m_itemized_other_refunds_isValid;

    double m_itemized_refunds_relating_convention_exp;
    bool m_itemized_refunds_relating_convention_exp_isSet;
    bool m_itemized_refunds_relating_convention_exp_isValid;

    QString m_last_beginning_image_number;
    bool m_last_beginning_image_number_isSet;
    bool m_last_beginning_image_number_isValid;

    double m_last_cash_on_hand_end_period;
    bool m_last_cash_on_hand_end_period_isSet;
    bool m_last_cash_on_hand_end_period_isValid;

    double m_last_debts_owed_by_committee;
    bool m_last_debts_owed_by_committee_isSet;
    bool m_last_debts_owed_by_committee_isValid;

    double m_last_debts_owed_to_committee;
    bool m_last_debts_owed_to_committee_isSet;
    bool m_last_debts_owed_to_committee_isValid;

    QString m_last_report_type_full;
    bool m_last_report_type_full_isSet;
    bool m_last_report_type_full_isValid;

    qint32 m_last_report_year;
    bool m_last_report_year_isSet;
    bool m_last_report_year_isValid;

    double m_loan_repayments_made;
    bool m_loan_repayments_made_isSet;
    bool m_loan_repayments_made_isValid;

    double m_loan_repayments_received;
    bool m_loan_repayments_received_isSet;
    bool m_loan_repayments_received_isValid;

    double m_loans_and_loan_repayments_made;
    bool m_loans_and_loan_repayments_made_isSet;
    bool m_loans_and_loan_repayments_made_isValid;

    double m_loans_and_loan_repayments_received;
    bool m_loans_and_loan_repayments_received_isSet;
    bool m_loans_and_loan_repayments_received_isValid;

    double m_loans_made;
    bool m_loans_made_isSet;
    bool m_loans_made_isValid;

    double m_net_contributions;
    bool m_net_contributions_isSet;
    bool m_net_contributions_isValid;

    double m_net_operating_expenditures;
    bool m_net_operating_expenditures_isSet;
    bool m_net_operating_expenditures_isValid;

    double m_non_allocated_fed_election_activity;
    bool m_non_allocated_fed_election_activity_isSet;
    bool m_non_allocated_fed_election_activity_isValid;

    double m_offsets_to_operating_expenditures;
    bool m_offsets_to_operating_expenditures_isSet;
    bool m_offsets_to_operating_expenditures_isValid;

    double m_operating_expenditures;
    bool m_operating_expenditures_isSet;
    bool m_operating_expenditures_isValid;

    double m_operating_expenditures_percent;
    bool m_operating_expenditures_percent_isSet;
    bool m_operating_expenditures_percent_isValid;

    QString m_organization_type;
    bool m_organization_type_isSet;
    bool m_organization_type_isValid;

    QString m_organization_type_full;
    bool m_organization_type_full_isSet;
    bool m_organization_type_full_isValid;

    double m_other_disbursements;
    bool m_other_disbursements_isSet;
    bool m_other_disbursements_isValid;

    double m_other_fed_operating_expenditures;
    bool m_other_fed_operating_expenditures_isSet;
    bool m_other_fed_operating_expenditures_isValid;

    double m_other_fed_receipts;
    bool m_other_fed_receipts_isSet;
    bool m_other_fed_receipts_isValid;

    double m_other_political_committee_contributions;
    bool m_other_political_committee_contributions_isSet;
    bool m_other_political_committee_contributions_isValid;

    double m_other_refunds;
    bool m_other_refunds_isSet;
    bool m_other_refunds_isValid;

    double m_party_and_other_committee_contributions_percent;
    bool m_party_and_other_committee_contributions_percent_isSet;
    bool m_party_and_other_committee_contributions_percent_isValid;

    QString m_party_full;
    bool m_party_full_isSet;
    bool m_party_full_isValid;

    QString m_pdf_url;
    bool m_pdf_url_isSet;
    bool m_pdf_url_isValid;

    double m_political_party_committee_contributions;
    bool m_political_party_committee_contributions_isSet;
    bool m_political_party_committee_contributions_isValid;

    double m_receipts;
    bool m_receipts_isSet;
    bool m_receipts_isValid;

    double m_refunded_individual_contributions;
    bool m_refunded_individual_contributions_isSet;
    bool m_refunded_individual_contributions_isValid;

    double m_refunded_other_political_committee_contributions;
    bool m_refunded_other_political_committee_contributions_isSet;
    bool m_refunded_other_political_committee_contributions_isValid;

    double m_refunded_political_party_committee_contributions;
    bool m_refunded_political_party_committee_contributions_isSet;
    bool m_refunded_political_party_committee_contributions_isValid;

    double m_refunds_relating_convention_exp;
    bool m_refunds_relating_convention_exp_isSet;
    bool m_refunds_relating_convention_exp_isValid;

    QString m_report_form;
    bool m_report_form_isSet;
    bool m_report_form_isValid;

    double m_shared_fed_activity;
    bool m_shared_fed_activity_isSet;
    bool m_shared_fed_activity_isValid;

    double m_shared_fed_activity_nonfed;
    bool m_shared_fed_activity_nonfed_isSet;
    bool m_shared_fed_activity_nonfed_isValid;

    double m_shared_fed_operating_expenditures;
    bool m_shared_fed_operating_expenditures_isSet;
    bool m_shared_fed_operating_expenditures_isValid;

    double m_shared_nonfed_operating_expenditures;
    bool m_shared_nonfed_operating_expenditures_isSet;
    bool m_shared_nonfed_operating_expenditures_isValid;

    QList<QString> m_sponsor_candidate_ids;
    bool m_sponsor_candidate_ids_isSet;
    bool m_sponsor_candidate_ids_isValid;

    QList<OAICommittee_sponsor_candidate_list_inner> m_sponsor_candidate_list;
    bool m_sponsor_candidate_list_isSet;
    bool m_sponsor_candidate_list_isValid;

    double m_total_exp_subject_limits;
    bool m_total_exp_subject_limits_isSet;
    bool m_total_exp_subject_limits_isValid;

    double m_total_transfers;
    bool m_total_transfers_isSet;
    bool m_total_transfers_isValid;

    QDate m_transaction_coverage_date;
    bool m_transaction_coverage_date_isSet;
    bool m_transaction_coverage_date_isValid;

    double m_transfers_from_affiliated_party;
    bool m_transfers_from_affiliated_party_isSet;
    bool m_transfers_from_affiliated_party_isValid;

    double m_transfers_from_nonfed_account;
    bool m_transfers_from_nonfed_account_isSet;
    bool m_transfers_from_nonfed_account_isValid;

    double m_transfers_from_nonfed_levin;
    bool m_transfers_from_nonfed_levin_isSet;
    bool m_transfers_from_nonfed_levin_isValid;

    double m_transfers_to_affiliated_committee;
    bool m_transfers_to_affiliated_committee_isSet;
    bool m_transfers_to_affiliated_committee_isValid;

    QString m_treasurer_name;
    bool m_treasurer_name_isSet;
    bool m_treasurer_name_isValid;

    double m_unitemized_convention_exp;
    bool m_unitemized_convention_exp_isSet;
    bool m_unitemized_convention_exp_isValid;

    double m_unitemized_other_disb;
    bool m_unitemized_other_disb_isSet;
    bool m_unitemized_other_disb_isValid;

    double m_unitemized_other_income;
    bool m_unitemized_other_income_isSet;
    bool m_unitemized_other_income_isValid;

    double m_unitemized_other_refunds;
    bool m_unitemized_other_refunds_isSet;
    bool m_unitemized_other_refunds_isValid;

    double m_unitemized_refunds_relating_convention_exp;
    bool m_unitemized_refunds_relating_convention_exp_isSet;
    bool m_unitemized_refunds_relating_convention_exp_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICommitteeTotalsPacParty)

#endif // OAICommitteeTotalsPacParty_H
