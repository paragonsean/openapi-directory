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

#include "OAICandidateTotal.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICandidateTotal::OAICandidateTotal(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICandidateTotal::OAICandidateTotal() {
    this->initializeModel();
}

OAICandidateTotal::~OAICandidateTotal() {}

void OAICandidateTotal::initializeModel() {

    m_candidate_id_isSet = false;
    m_candidate_id_isValid = false;

    m_candidate_inactive_isSet = false;
    m_candidate_inactive_isValid = false;

    m_cash_on_hand_end_period_isSet = false;
    m_cash_on_hand_end_period_isValid = false;

    m_coverage_end_date_isSet = false;
    m_coverage_end_date_isValid = false;

    m_coverage_start_date_isSet = false;
    m_coverage_start_date_isValid = false;

    m_cycle_isSet = false;
    m_cycle_isValid = false;

    m_debts_owed_by_committee_isSet = false;
    m_debts_owed_by_committee_isValid = false;

    m_disbursements_isSet = false;
    m_disbursements_isValid = false;

    m_district_isSet = false;
    m_district_isValid = false;

    m_district_number_isSet = false;
    m_district_number_isValid = false;

    m_election_year_isSet = false;
    m_election_year_isValid = false;

    m_federal_funds_flag_isSet = false;
    m_federal_funds_flag_isValid = false;

    m_has_raised_funds_isSet = false;
    m_has_raised_funds_isValid = false;

    m_individual_itemized_contributions_isSet = false;
    m_individual_itemized_contributions_isValid = false;

    m_is_election_isSet = false;
    m_is_election_isValid = false;

    m_office_isSet = false;
    m_office_isValid = false;

    m_other_political_committee_contributions_isSet = false;
    m_other_political_committee_contributions_isValid = false;

    m_party_isSet = false;
    m_party_isValid = false;

    m_receipts_isSet = false;
    m_receipts_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_state_full_isSet = false;
    m_state_full_isValid = false;

    m_transfers_from_other_authorized_committee_isSet = false;
    m_transfers_from_other_authorized_committee_isValid = false;
}

void OAICandidateTotal::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICandidateTotal::fromJsonObject(QJsonObject json) {

    m_candidate_id_isValid = ::OpenAPI::fromJsonValue(m_candidate_id, json[QString("candidate_id")]);
    m_candidate_id_isSet = !json[QString("candidate_id")].isNull() && m_candidate_id_isValid;

    m_candidate_inactive_isValid = ::OpenAPI::fromJsonValue(m_candidate_inactive, json[QString("candidate_inactive")]);
    m_candidate_inactive_isSet = !json[QString("candidate_inactive")].isNull() && m_candidate_inactive_isValid;

    m_cash_on_hand_end_period_isValid = ::OpenAPI::fromJsonValue(m_cash_on_hand_end_period, json[QString("cash_on_hand_end_period")]);
    m_cash_on_hand_end_period_isSet = !json[QString("cash_on_hand_end_period")].isNull() && m_cash_on_hand_end_period_isValid;

    m_coverage_end_date_isValid = ::OpenAPI::fromJsonValue(m_coverage_end_date, json[QString("coverage_end_date")]);
    m_coverage_end_date_isSet = !json[QString("coverage_end_date")].isNull() && m_coverage_end_date_isValid;

    m_coverage_start_date_isValid = ::OpenAPI::fromJsonValue(m_coverage_start_date, json[QString("coverage_start_date")]);
    m_coverage_start_date_isSet = !json[QString("coverage_start_date")].isNull() && m_coverage_start_date_isValid;

    m_cycle_isValid = ::OpenAPI::fromJsonValue(m_cycle, json[QString("cycle")]);
    m_cycle_isSet = !json[QString("cycle")].isNull() && m_cycle_isValid;

    m_debts_owed_by_committee_isValid = ::OpenAPI::fromJsonValue(m_debts_owed_by_committee, json[QString("debts_owed_by_committee")]);
    m_debts_owed_by_committee_isSet = !json[QString("debts_owed_by_committee")].isNull() && m_debts_owed_by_committee_isValid;

    m_disbursements_isValid = ::OpenAPI::fromJsonValue(m_disbursements, json[QString("disbursements")]);
    m_disbursements_isSet = !json[QString("disbursements")].isNull() && m_disbursements_isValid;

    m_district_isValid = ::OpenAPI::fromJsonValue(m_district, json[QString("district")]);
    m_district_isSet = !json[QString("district")].isNull() && m_district_isValid;

    m_district_number_isValid = ::OpenAPI::fromJsonValue(m_district_number, json[QString("district_number")]);
    m_district_number_isSet = !json[QString("district_number")].isNull() && m_district_number_isValid;

    m_election_year_isValid = ::OpenAPI::fromJsonValue(m_election_year, json[QString("election_year")]);
    m_election_year_isSet = !json[QString("election_year")].isNull() && m_election_year_isValid;

    m_federal_funds_flag_isValid = ::OpenAPI::fromJsonValue(m_federal_funds_flag, json[QString("federal_funds_flag")]);
    m_federal_funds_flag_isSet = !json[QString("federal_funds_flag")].isNull() && m_federal_funds_flag_isValid;

    m_has_raised_funds_isValid = ::OpenAPI::fromJsonValue(m_has_raised_funds, json[QString("has_raised_funds")]);
    m_has_raised_funds_isSet = !json[QString("has_raised_funds")].isNull() && m_has_raised_funds_isValid;

    m_individual_itemized_contributions_isValid = ::OpenAPI::fromJsonValue(m_individual_itemized_contributions, json[QString("individual_itemized_contributions")]);
    m_individual_itemized_contributions_isSet = !json[QString("individual_itemized_contributions")].isNull() && m_individual_itemized_contributions_isValid;

    m_is_election_isValid = ::OpenAPI::fromJsonValue(m_is_election, json[QString("is_election")]);
    m_is_election_isSet = !json[QString("is_election")].isNull() && m_is_election_isValid;

    m_office_isValid = ::OpenAPI::fromJsonValue(m_office, json[QString("office")]);
    m_office_isSet = !json[QString("office")].isNull() && m_office_isValid;

    m_other_political_committee_contributions_isValid = ::OpenAPI::fromJsonValue(m_other_political_committee_contributions, json[QString("other_political_committee_contributions")]);
    m_other_political_committee_contributions_isSet = !json[QString("other_political_committee_contributions")].isNull() && m_other_political_committee_contributions_isValid;

    m_party_isValid = ::OpenAPI::fromJsonValue(m_party, json[QString("party")]);
    m_party_isSet = !json[QString("party")].isNull() && m_party_isValid;

    m_receipts_isValid = ::OpenAPI::fromJsonValue(m_receipts, json[QString("receipts")]);
    m_receipts_isSet = !json[QString("receipts")].isNull() && m_receipts_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_state_full_isValid = ::OpenAPI::fromJsonValue(m_state_full, json[QString("state_full")]);
    m_state_full_isSet = !json[QString("state_full")].isNull() && m_state_full_isValid;

    m_transfers_from_other_authorized_committee_isValid = ::OpenAPI::fromJsonValue(m_transfers_from_other_authorized_committee, json[QString("transfers_from_other_authorized_committee")]);
    m_transfers_from_other_authorized_committee_isSet = !json[QString("transfers_from_other_authorized_committee")].isNull() && m_transfers_from_other_authorized_committee_isValid;
}

QString OAICandidateTotal::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICandidateTotal::asJsonObject() const {
    QJsonObject obj;
    if (m_candidate_id_isSet) {
        obj.insert(QString("candidate_id"), ::OpenAPI::toJsonValue(m_candidate_id));
    }
    if (m_candidate_inactive_isSet) {
        obj.insert(QString("candidate_inactive"), ::OpenAPI::toJsonValue(m_candidate_inactive));
    }
    if (m_cash_on_hand_end_period_isSet) {
        obj.insert(QString("cash_on_hand_end_period"), ::OpenAPI::toJsonValue(m_cash_on_hand_end_period));
    }
    if (m_coverage_end_date_isSet) {
        obj.insert(QString("coverage_end_date"), ::OpenAPI::toJsonValue(m_coverage_end_date));
    }
    if (m_coverage_start_date_isSet) {
        obj.insert(QString("coverage_start_date"), ::OpenAPI::toJsonValue(m_coverage_start_date));
    }
    if (m_cycle_isSet) {
        obj.insert(QString("cycle"), ::OpenAPI::toJsonValue(m_cycle));
    }
    if (m_debts_owed_by_committee_isSet) {
        obj.insert(QString("debts_owed_by_committee"), ::OpenAPI::toJsonValue(m_debts_owed_by_committee));
    }
    if (m_disbursements_isSet) {
        obj.insert(QString("disbursements"), ::OpenAPI::toJsonValue(m_disbursements));
    }
    if (m_district_isSet) {
        obj.insert(QString("district"), ::OpenAPI::toJsonValue(m_district));
    }
    if (m_district_number_isSet) {
        obj.insert(QString("district_number"), ::OpenAPI::toJsonValue(m_district_number));
    }
    if (m_election_year_isSet) {
        obj.insert(QString("election_year"), ::OpenAPI::toJsonValue(m_election_year));
    }
    if (m_federal_funds_flag_isSet) {
        obj.insert(QString("federal_funds_flag"), ::OpenAPI::toJsonValue(m_federal_funds_flag));
    }
    if (m_has_raised_funds_isSet) {
        obj.insert(QString("has_raised_funds"), ::OpenAPI::toJsonValue(m_has_raised_funds));
    }
    if (m_individual_itemized_contributions_isSet) {
        obj.insert(QString("individual_itemized_contributions"), ::OpenAPI::toJsonValue(m_individual_itemized_contributions));
    }
    if (m_is_election_isSet) {
        obj.insert(QString("is_election"), ::OpenAPI::toJsonValue(m_is_election));
    }
    if (m_office_isSet) {
        obj.insert(QString("office"), ::OpenAPI::toJsonValue(m_office));
    }
    if (m_other_political_committee_contributions_isSet) {
        obj.insert(QString("other_political_committee_contributions"), ::OpenAPI::toJsonValue(m_other_political_committee_contributions));
    }
    if (m_party_isSet) {
        obj.insert(QString("party"), ::OpenAPI::toJsonValue(m_party));
    }
    if (m_receipts_isSet) {
        obj.insert(QString("receipts"), ::OpenAPI::toJsonValue(m_receipts));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_state_full_isSet) {
        obj.insert(QString("state_full"), ::OpenAPI::toJsonValue(m_state_full));
    }
    if (m_transfers_from_other_authorized_committee_isSet) {
        obj.insert(QString("transfers_from_other_authorized_committee"), ::OpenAPI::toJsonValue(m_transfers_from_other_authorized_committee));
    }
    return obj;
}

QString OAICandidateTotal::getCandidateId() const {
    return m_candidate_id;
}
void OAICandidateTotal::setCandidateId(const QString &candidate_id) {
    m_candidate_id = candidate_id;
    m_candidate_id_isSet = true;
}

bool OAICandidateTotal::is_candidate_id_Set() const{
    return m_candidate_id_isSet;
}

bool OAICandidateTotal::is_candidate_id_Valid() const{
    return m_candidate_id_isValid;
}

bool OAICandidateTotal::isCandidateInactive() const {
    return m_candidate_inactive;
}
void OAICandidateTotal::setCandidateInactive(const bool &candidate_inactive) {
    m_candidate_inactive = candidate_inactive;
    m_candidate_inactive_isSet = true;
}

bool OAICandidateTotal::is_candidate_inactive_Set() const{
    return m_candidate_inactive_isSet;
}

bool OAICandidateTotal::is_candidate_inactive_Valid() const{
    return m_candidate_inactive_isValid;
}

double OAICandidateTotal::getCashOnHandEndPeriod() const {
    return m_cash_on_hand_end_period;
}
void OAICandidateTotal::setCashOnHandEndPeriod(const double &cash_on_hand_end_period) {
    m_cash_on_hand_end_period = cash_on_hand_end_period;
    m_cash_on_hand_end_period_isSet = true;
}

bool OAICandidateTotal::is_cash_on_hand_end_period_Set() const{
    return m_cash_on_hand_end_period_isSet;
}

bool OAICandidateTotal::is_cash_on_hand_end_period_Valid() const{
    return m_cash_on_hand_end_period_isValid;
}

QDate OAICandidateTotal::getCoverageEndDate() const {
    return m_coverage_end_date;
}
void OAICandidateTotal::setCoverageEndDate(const QDate &coverage_end_date) {
    m_coverage_end_date = coverage_end_date;
    m_coverage_end_date_isSet = true;
}

bool OAICandidateTotal::is_coverage_end_date_Set() const{
    return m_coverage_end_date_isSet;
}

bool OAICandidateTotal::is_coverage_end_date_Valid() const{
    return m_coverage_end_date_isValid;
}

QDate OAICandidateTotal::getCoverageStartDate() const {
    return m_coverage_start_date;
}
void OAICandidateTotal::setCoverageStartDate(const QDate &coverage_start_date) {
    m_coverage_start_date = coverage_start_date;
    m_coverage_start_date_isSet = true;
}

bool OAICandidateTotal::is_coverage_start_date_Set() const{
    return m_coverage_start_date_isSet;
}

bool OAICandidateTotal::is_coverage_start_date_Valid() const{
    return m_coverage_start_date_isValid;
}

qint32 OAICandidateTotal::getCycle() const {
    return m_cycle;
}
void OAICandidateTotal::setCycle(const qint32 &cycle) {
    m_cycle = cycle;
    m_cycle_isSet = true;
}

bool OAICandidateTotal::is_cycle_Set() const{
    return m_cycle_isSet;
}

bool OAICandidateTotal::is_cycle_Valid() const{
    return m_cycle_isValid;
}

double OAICandidateTotal::getDebtsOwedByCommittee() const {
    return m_debts_owed_by_committee;
}
void OAICandidateTotal::setDebtsOwedByCommittee(const double &debts_owed_by_committee) {
    m_debts_owed_by_committee = debts_owed_by_committee;
    m_debts_owed_by_committee_isSet = true;
}

bool OAICandidateTotal::is_debts_owed_by_committee_Set() const{
    return m_debts_owed_by_committee_isSet;
}

bool OAICandidateTotal::is_debts_owed_by_committee_Valid() const{
    return m_debts_owed_by_committee_isValid;
}

double OAICandidateTotal::getDisbursements() const {
    return m_disbursements;
}
void OAICandidateTotal::setDisbursements(const double &disbursements) {
    m_disbursements = disbursements;
    m_disbursements_isSet = true;
}

bool OAICandidateTotal::is_disbursements_Set() const{
    return m_disbursements_isSet;
}

bool OAICandidateTotal::is_disbursements_Valid() const{
    return m_disbursements_isValid;
}

QString OAICandidateTotal::getDistrict() const {
    return m_district;
}
void OAICandidateTotal::setDistrict(const QString &district) {
    m_district = district;
    m_district_isSet = true;
}

bool OAICandidateTotal::is_district_Set() const{
    return m_district_isSet;
}

bool OAICandidateTotal::is_district_Valid() const{
    return m_district_isValid;
}

qint32 OAICandidateTotal::getDistrictNumber() const {
    return m_district_number;
}
void OAICandidateTotal::setDistrictNumber(const qint32 &district_number) {
    m_district_number = district_number;
    m_district_number_isSet = true;
}

bool OAICandidateTotal::is_district_number_Set() const{
    return m_district_number_isSet;
}

bool OAICandidateTotal::is_district_number_Valid() const{
    return m_district_number_isValid;
}

qint32 OAICandidateTotal::getElectionYear() const {
    return m_election_year;
}
void OAICandidateTotal::setElectionYear(const qint32 &election_year) {
    m_election_year = election_year;
    m_election_year_isSet = true;
}

bool OAICandidateTotal::is_election_year_Set() const{
    return m_election_year_isSet;
}

bool OAICandidateTotal::is_election_year_Valid() const{
    return m_election_year_isValid;
}

bool OAICandidateTotal::isFederalFundsFlag() const {
    return m_federal_funds_flag;
}
void OAICandidateTotal::setFederalFundsFlag(const bool &federal_funds_flag) {
    m_federal_funds_flag = federal_funds_flag;
    m_federal_funds_flag_isSet = true;
}

bool OAICandidateTotal::is_federal_funds_flag_Set() const{
    return m_federal_funds_flag_isSet;
}

bool OAICandidateTotal::is_federal_funds_flag_Valid() const{
    return m_federal_funds_flag_isValid;
}

bool OAICandidateTotal::isHasRaisedFunds() const {
    return m_has_raised_funds;
}
void OAICandidateTotal::setHasRaisedFunds(const bool &has_raised_funds) {
    m_has_raised_funds = has_raised_funds;
    m_has_raised_funds_isSet = true;
}

bool OAICandidateTotal::is_has_raised_funds_Set() const{
    return m_has_raised_funds_isSet;
}

bool OAICandidateTotal::is_has_raised_funds_Valid() const{
    return m_has_raised_funds_isValid;
}

double OAICandidateTotal::getIndividualItemizedContributions() const {
    return m_individual_itemized_contributions;
}
void OAICandidateTotal::setIndividualItemizedContributions(const double &individual_itemized_contributions) {
    m_individual_itemized_contributions = individual_itemized_contributions;
    m_individual_itemized_contributions_isSet = true;
}

bool OAICandidateTotal::is_individual_itemized_contributions_Set() const{
    return m_individual_itemized_contributions_isSet;
}

bool OAICandidateTotal::is_individual_itemized_contributions_Valid() const{
    return m_individual_itemized_contributions_isValid;
}

bool OAICandidateTotal::isIsElection() const {
    return m_is_election;
}
void OAICandidateTotal::setIsElection(const bool &is_election) {
    m_is_election = is_election;
    m_is_election_isSet = true;
}

bool OAICandidateTotal::is_is_election_Set() const{
    return m_is_election_isSet;
}

bool OAICandidateTotal::is_is_election_Valid() const{
    return m_is_election_isValid;
}

QString OAICandidateTotal::getOffice() const {
    return m_office;
}
void OAICandidateTotal::setOffice(const QString &office) {
    m_office = office;
    m_office_isSet = true;
}

bool OAICandidateTotal::is_office_Set() const{
    return m_office_isSet;
}

bool OAICandidateTotal::is_office_Valid() const{
    return m_office_isValid;
}

double OAICandidateTotal::getOtherPoliticalCommitteeContributions() const {
    return m_other_political_committee_contributions;
}
void OAICandidateTotal::setOtherPoliticalCommitteeContributions(const double &other_political_committee_contributions) {
    m_other_political_committee_contributions = other_political_committee_contributions;
    m_other_political_committee_contributions_isSet = true;
}

bool OAICandidateTotal::is_other_political_committee_contributions_Set() const{
    return m_other_political_committee_contributions_isSet;
}

bool OAICandidateTotal::is_other_political_committee_contributions_Valid() const{
    return m_other_political_committee_contributions_isValid;
}

QString OAICandidateTotal::getParty() const {
    return m_party;
}
void OAICandidateTotal::setParty(const QString &party) {
    m_party = party;
    m_party_isSet = true;
}

bool OAICandidateTotal::is_party_Set() const{
    return m_party_isSet;
}

bool OAICandidateTotal::is_party_Valid() const{
    return m_party_isValid;
}

double OAICandidateTotal::getReceipts() const {
    return m_receipts;
}
void OAICandidateTotal::setReceipts(const double &receipts) {
    m_receipts = receipts;
    m_receipts_isSet = true;
}

bool OAICandidateTotal::is_receipts_Set() const{
    return m_receipts_isSet;
}

bool OAICandidateTotal::is_receipts_Valid() const{
    return m_receipts_isValid;
}

QString OAICandidateTotal::getState() const {
    return m_state;
}
void OAICandidateTotal::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAICandidateTotal::is_state_Set() const{
    return m_state_isSet;
}

bool OAICandidateTotal::is_state_Valid() const{
    return m_state_isValid;
}

QString OAICandidateTotal::getStateFull() const {
    return m_state_full;
}
void OAICandidateTotal::setStateFull(const QString &state_full) {
    m_state_full = state_full;
    m_state_full_isSet = true;
}

bool OAICandidateTotal::is_state_full_Set() const{
    return m_state_full_isSet;
}

bool OAICandidateTotal::is_state_full_Valid() const{
    return m_state_full_isValid;
}

double OAICandidateTotal::getTransfersFromOtherAuthorizedCommittee() const {
    return m_transfers_from_other_authorized_committee;
}
void OAICandidateTotal::setTransfersFromOtherAuthorizedCommittee(const double &transfers_from_other_authorized_committee) {
    m_transfers_from_other_authorized_committee = transfers_from_other_authorized_committee;
    m_transfers_from_other_authorized_committee_isSet = true;
}

bool OAICandidateTotal::is_transfers_from_other_authorized_committee_Set() const{
    return m_transfers_from_other_authorized_committee_isSet;
}

bool OAICandidateTotal::is_transfers_from_other_authorized_committee_Valid() const{
    return m_transfers_from_other_authorized_committee_isValid;
}

bool OAICandidateTotal::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_candidate_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_candidate_inactive_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cash_on_hand_end_period_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coverage_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coverage_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cycle_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_debts_owed_by_committee_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_disbursements_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_district_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_district_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_election_year_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_federal_funds_flag_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_raised_funds_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_individual_itemized_contributions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_election_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_office_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_other_political_committee_contributions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_party_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_receipts_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_full_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transfers_from_other_authorized_committee_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICandidateTotal::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_candidate_id_isValid && m_cycle_isValid && m_is_election_isValid && true;
}

} // namespace OpenAPI
