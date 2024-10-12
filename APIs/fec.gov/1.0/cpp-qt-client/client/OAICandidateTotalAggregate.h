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
 * OAICandidateTotalAggregate.h
 *
 * 
 */

#ifndef OAICandidateTotalAggregate_H
#define OAICandidateTotalAggregate_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICandidateTotalAggregate : public OAIObject {
public:
    OAICandidateTotalAggregate();
    OAICandidateTotalAggregate(QString json);
    ~OAICandidateTotalAggregate() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDistrict() const;
    void setDistrict(const QString &district);
    bool is_district_Set() const;
    bool is_district_Valid() const;

    qint32 getDistrictNumber() const;
    void setDistrictNumber(const qint32 &district_number);
    bool is_district_number_Set() const;
    bool is_district_number_Valid() const;

    qint32 getElectionYear() const;
    void setElectionYear(const qint32 &election_year);
    bool is_election_year_Set() const;
    bool is_election_year_Valid() const;

    QString getOffice() const;
    void setOffice(const QString &office);
    bool is_office_Set() const;
    bool is_office_Valid() const;

    QString getParty() const;
    void setParty(const QString &party);
    bool is_party_Set() const;
    bool is_party_Valid() const;

    QString getState() const;
    void setState(const QString &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QString getStateFull() const;
    void setStateFull(const QString &state_full);
    bool is_state_full_Set() const;
    bool is_state_full_Valid() const;

    double getTotalCashOnHandEndPeriod() const;
    void setTotalCashOnHandEndPeriod(const double &total_cash_on_hand_end_period);
    bool is_total_cash_on_hand_end_period_Set() const;
    bool is_total_cash_on_hand_end_period_Valid() const;

    double getTotalDebtsOwedByCommittee() const;
    void setTotalDebtsOwedByCommittee(const double &total_debts_owed_by_committee);
    bool is_total_debts_owed_by_committee_Set() const;
    bool is_total_debts_owed_by_committee_Valid() const;

    double getTotalDisbursements() const;
    void setTotalDisbursements(const double &total_disbursements);
    bool is_total_disbursements_Set() const;
    bool is_total_disbursements_Valid() const;

    double getTotalIndividualItemizedContributions() const;
    void setTotalIndividualItemizedContributions(const double &total_individual_itemized_contributions);
    bool is_total_individual_itemized_contributions_Set() const;
    bool is_total_individual_itemized_contributions_Valid() const;

    double getTotalOtherPoliticalCommitteeContributions() const;
    void setTotalOtherPoliticalCommitteeContributions(const double &total_other_political_committee_contributions);
    bool is_total_other_political_committee_contributions_Set() const;
    bool is_total_other_political_committee_contributions_Valid() const;

    double getTotalReceipts() const;
    void setTotalReceipts(const double &total_receipts);
    bool is_total_receipts_Set() const;
    bool is_total_receipts_Valid() const;

    double getTotalTransfersFromOtherAuthorizedCommittee() const;
    void setTotalTransfersFromOtherAuthorizedCommittee(const double &total_transfers_from_other_authorized_committee);
    bool is_total_transfers_from_other_authorized_committee_Set() const;
    bool is_total_transfers_from_other_authorized_committee_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_district;
    bool m_district_isSet;
    bool m_district_isValid;

    qint32 m_district_number;
    bool m_district_number_isSet;
    bool m_district_number_isValid;

    qint32 m_election_year;
    bool m_election_year_isSet;
    bool m_election_year_isValid;

    QString m_office;
    bool m_office_isSet;
    bool m_office_isValid;

    QString m_party;
    bool m_party_isSet;
    bool m_party_isValid;

    QString m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QString m_state_full;
    bool m_state_full_isSet;
    bool m_state_full_isValid;

    double m_total_cash_on_hand_end_period;
    bool m_total_cash_on_hand_end_period_isSet;
    bool m_total_cash_on_hand_end_period_isValid;

    double m_total_debts_owed_by_committee;
    bool m_total_debts_owed_by_committee_isSet;
    bool m_total_debts_owed_by_committee_isValid;

    double m_total_disbursements;
    bool m_total_disbursements_isSet;
    bool m_total_disbursements_isValid;

    double m_total_individual_itemized_contributions;
    bool m_total_individual_itemized_contributions_isSet;
    bool m_total_individual_itemized_contributions_isValid;

    double m_total_other_political_committee_contributions;
    bool m_total_other_political_committee_contributions_isSet;
    bool m_total_other_political_committee_contributions_isValid;

    double m_total_receipts;
    bool m_total_receipts_isSet;
    bool m_total_receipts_isValid;

    double m_total_transfers_from_other_authorized_committee;
    bool m_total_transfers_from_other_authorized_committee_isSet;
    bool m_total_transfers_from_other_authorized_committee_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICandidateTotalAggregate)

#endif // OAICandidateTotalAggregate_H
