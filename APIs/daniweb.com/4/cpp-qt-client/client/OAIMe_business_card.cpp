/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIMe_business_card.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMe_business_card::OAIMe_business_card(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMe_business_card::OAIMe_business_card() {
    this->initializeModel();
}

OAIMe_business_card::~OAIMe_business_card() {}

void OAIMe_business_card::initializeModel() {

    m_company_name_isSet = false;
    m_company_name_isValid = false;

    m_company_size_isSet = false;
    m_company_size_isValid = false;

    m_headline_isSet = false;
    m_headline_isValid = false;

    m_industry_isSet = false;
    m_industry_isValid = false;

    m_interest_tags_isSet = false;
    m_interest_tags_isValid = false;

    m_job_position_isSet = false;
    m_job_position_isValid = false;

    m_summary_isSet = false;
    m_summary_isValid = false;

    m_website_isSet = false;
    m_website_isValid = false;
}

void OAIMe_business_card::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMe_business_card::fromJsonObject(QJsonObject json) {

    m_company_name_isValid = ::OpenAPI::fromJsonValue(m_company_name, json[QString("company_name")]);
    m_company_name_isSet = !json[QString("company_name")].isNull() && m_company_name_isValid;

    m_company_size_isValid = ::OpenAPI::fromJsonValue(m_company_size, json[QString("company_size")]);
    m_company_size_isSet = !json[QString("company_size")].isNull() && m_company_size_isValid;

    m_headline_isValid = ::OpenAPI::fromJsonValue(m_headline, json[QString("headline")]);
    m_headline_isSet = !json[QString("headline")].isNull() && m_headline_isValid;

    m_industry_isValid = ::OpenAPI::fromJsonValue(m_industry, json[QString("industry")]);
    m_industry_isSet = !json[QString("industry")].isNull() && m_industry_isValid;

    m_interest_tags_isValid = ::OpenAPI::fromJsonValue(m_interest_tags, json[QString("interest_tags")]);
    m_interest_tags_isSet = !json[QString("interest_tags")].isNull() && m_interest_tags_isValid;

    m_job_position_isValid = ::OpenAPI::fromJsonValue(m_job_position, json[QString("job_position")]);
    m_job_position_isSet = !json[QString("job_position")].isNull() && m_job_position_isValid;

    m_summary_isValid = ::OpenAPI::fromJsonValue(m_summary, json[QString("summary")]);
    m_summary_isSet = !json[QString("summary")].isNull() && m_summary_isValid;

    m_website_isValid = ::OpenAPI::fromJsonValue(m_website, json[QString("website")]);
    m_website_isSet = !json[QString("website")].isNull() && m_website_isValid;
}

QString OAIMe_business_card::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMe_business_card::asJsonObject() const {
    QJsonObject obj;
    if (m_company_name_isSet) {
        obj.insert(QString("company_name"), ::OpenAPI::toJsonValue(m_company_name));
    }
    if (m_company_size_isSet) {
        obj.insert(QString("company_size"), ::OpenAPI::toJsonValue(m_company_size));
    }
    if (m_headline_isSet) {
        obj.insert(QString("headline"), ::OpenAPI::toJsonValue(m_headline));
    }
    if (m_industry_isSet) {
        obj.insert(QString("industry"), ::OpenAPI::toJsonValue(m_industry));
    }
    if (m_interest_tags.size() > 0) {
        obj.insert(QString("interest_tags"), ::OpenAPI::toJsonValue(m_interest_tags));
    }
    if (m_job_position_isSet) {
        obj.insert(QString("job_position"), ::OpenAPI::toJsonValue(m_job_position));
    }
    if (m_summary_isSet) {
        obj.insert(QString("summary"), ::OpenAPI::toJsonValue(m_summary));
    }
    if (m_website.isSet()) {
        obj.insert(QString("website"), ::OpenAPI::toJsonValue(m_website));
    }
    return obj;
}

QString OAIMe_business_card::getCompanyName() const {
    return m_company_name;
}
void OAIMe_business_card::setCompanyName(const QString &company_name) {
    m_company_name = company_name;
    m_company_name_isSet = true;
}

bool OAIMe_business_card::is_company_name_Set() const{
    return m_company_name_isSet;
}

bool OAIMe_business_card::is_company_name_Valid() const{
    return m_company_name_isValid;
}

QString OAIMe_business_card::getCompanySize() const {
    return m_company_size;
}
void OAIMe_business_card::setCompanySize(const QString &company_size) {
    m_company_size = company_size;
    m_company_size_isSet = true;
}

bool OAIMe_business_card::is_company_size_Set() const{
    return m_company_size_isSet;
}

bool OAIMe_business_card::is_company_size_Valid() const{
    return m_company_size_isValid;
}

QString OAIMe_business_card::getHeadline() const {
    return m_headline;
}
void OAIMe_business_card::setHeadline(const QString &headline) {
    m_headline = headline;
    m_headline_isSet = true;
}

bool OAIMe_business_card::is_headline_Set() const{
    return m_headline_isSet;
}

bool OAIMe_business_card::is_headline_Valid() const{
    return m_headline_isValid;
}

QString OAIMe_business_card::getIndustry() const {
    return m_industry;
}
void OAIMe_business_card::setIndustry(const QString &industry) {
    m_industry = industry;
    m_industry_isSet = true;
}

bool OAIMe_business_card::is_industry_Set() const{
    return m_industry_isSet;
}

bool OAIMe_business_card::is_industry_Valid() const{
    return m_industry_isValid;
}

QList<QString> OAIMe_business_card::getInterestTags() const {
    return m_interest_tags;
}
void OAIMe_business_card::setInterestTags(const QList<QString> &interest_tags) {
    m_interest_tags = interest_tags;
    m_interest_tags_isSet = true;
}

bool OAIMe_business_card::is_interest_tags_Set() const{
    return m_interest_tags_isSet;
}

bool OAIMe_business_card::is_interest_tags_Valid() const{
    return m_interest_tags_isValid;
}

QString OAIMe_business_card::getJobPosition() const {
    return m_job_position;
}
void OAIMe_business_card::setJobPosition(const QString &job_position) {
    m_job_position = job_position;
    m_job_position_isSet = true;
}

bool OAIMe_business_card::is_job_position_Set() const{
    return m_job_position_isSet;
}

bool OAIMe_business_card::is_job_position_Valid() const{
    return m_job_position_isValid;
}

QString OAIMe_business_card::getSummary() const {
    return m_summary;
}
void OAIMe_business_card::setSummary(const QString &summary) {
    m_summary = summary;
    m_summary_isSet = true;
}

bool OAIMe_business_card::is_summary_Set() const{
    return m_summary_isSet;
}

bool OAIMe_business_card::is_summary_Valid() const{
    return m_summary_isValid;
}

OAIMe_business_card_website OAIMe_business_card::getWebsite() const {
    return m_website;
}
void OAIMe_business_card::setWebsite(const OAIMe_business_card_website &website) {
    m_website = website;
    m_website_isSet = true;
}

bool OAIMe_business_card::is_website_Set() const{
    return m_website_isSet;
}

bool OAIMe_business_card::is_website_Valid() const{
    return m_website_isValid;
}

bool OAIMe_business_card::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_company_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_headline_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_industry_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_interest_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_summary_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_website.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMe_business_card::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
