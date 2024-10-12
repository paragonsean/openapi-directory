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
 * OAIElection.h
 *
 * 
 */

#ifndef OAIElection_H
#define OAIElection_H

#include <QJsonObject>

#include <QDate>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIElection : public OAIObject {
public:
    OAIElection();
    OAIElection(QString json);
    ~OAIElection() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCandidateElectionYear() const;
    void setCandidateElectionYear(const qint32 &candidate_election_year);
    bool is_candidate_election_year_Set() const;
    bool is_candidate_election_year_Valid() const;

    QString getCandidateId() const;
    void setCandidateId(const QString &candidate_id);
    bool is_candidate_id_Set() const;
    bool is_candidate_id_Valid() const;

    QString getCandidateName() const;
    void setCandidateName(const QString &candidate_name);
    bool is_candidate_name_Set() const;
    bool is_candidate_name_Valid() const;

    QString getCandidatePccId() const;
    void setCandidatePccId(const QString &candidate_pcc_id);
    bool is_candidate_pcc_id_Set() const;
    bool is_candidate_pcc_id_Valid() const;

    QString getCandidatePccName() const;
    void setCandidatePccName(const QString &candidate_pcc_name);
    bool is_candidate_pcc_name_Set() const;
    bool is_candidate_pcc_name_Valid() const;

    double getCashOnHandEndPeriod() const;
    void setCashOnHandEndPeriod(const double &cash_on_hand_end_period);
    bool is_cash_on_hand_end_period_Set() const;
    bool is_cash_on_hand_end_period_Valid() const;

    QList<QString> getCommitteeIds() const;
    void setCommitteeIds(const QList<QString> &committee_ids);
    bool is_committee_ids_Set() const;
    bool is_committee_ids_Valid() const;

    QDate getCoverageEndDate() const;
    void setCoverageEndDate(const QDate &coverage_end_date);
    bool is_coverage_end_date_Set() const;
    bool is_coverage_end_date_Valid() const;

    QString getIncumbentChallengeFull() const;
    void setIncumbentChallengeFull(const QString &incumbent_challenge_full);
    bool is_incumbent_challenge_full_Set() const;
    bool is_incumbent_challenge_full_Valid() const;

    QString getPartyFull() const;
    void setPartyFull(const QString &party_full);
    bool is_party_full_Set() const;
    bool is_party_full_Valid() const;

    double getTotalDisbursements() const;
    void setTotalDisbursements(const double &total_disbursements);
    bool is_total_disbursements_Set() const;
    bool is_total_disbursements_Valid() const;

    double getTotalReceipts() const;
    void setTotalReceipts(const double &total_receipts);
    bool is_total_receipts_Set() const;
    bool is_total_receipts_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_candidate_election_year;
    bool m_candidate_election_year_isSet;
    bool m_candidate_election_year_isValid;

    QString m_candidate_id;
    bool m_candidate_id_isSet;
    bool m_candidate_id_isValid;

    QString m_candidate_name;
    bool m_candidate_name_isSet;
    bool m_candidate_name_isValid;

    QString m_candidate_pcc_id;
    bool m_candidate_pcc_id_isSet;
    bool m_candidate_pcc_id_isValid;

    QString m_candidate_pcc_name;
    bool m_candidate_pcc_name_isSet;
    bool m_candidate_pcc_name_isValid;

    double m_cash_on_hand_end_period;
    bool m_cash_on_hand_end_period_isSet;
    bool m_cash_on_hand_end_period_isValid;

    QList<QString> m_committee_ids;
    bool m_committee_ids_isSet;
    bool m_committee_ids_isValid;

    QDate m_coverage_end_date;
    bool m_coverage_end_date_isSet;
    bool m_coverage_end_date_isValid;

    QString m_incumbent_challenge_full;
    bool m_incumbent_challenge_full_isSet;
    bool m_incumbent_challenge_full_isValid;

    QString m_party_full;
    bool m_party_full_isSet;
    bool m_party_full_isValid;

    double m_total_disbursements;
    bool m_total_disbursements_isSet;
    bool m_total_disbursements_isValid;

    double m_total_receipts;
    bool m_total_receipts_isSet;
    bool m_total_receipts_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIElection)

#endif // OAIElection_H
