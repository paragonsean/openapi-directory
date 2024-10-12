/**
 * Open States API v3
 *  * [More documentation](https://docs.openstates.org/en/latest/api/v3/index.html) * [Register for an account](https://openstates.org/accounts/signup/)   **We are currently working to restore experimental support for committees & events.**  During this period please note that data is not yet available for all states and the exact format of the new endpoints may change slightly depending on user feedback.  If you have any issues or questions use our [GitHub Issues](https://github.com/openstates/issues/issues) to give feedback. 
 *
 * The version of the OpenAPI document: 2021.11.12
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIJurisdictionList.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIJurisdictionList::OAIJurisdictionList(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIJurisdictionList::OAIJurisdictionList() {
    this->initializeModel();
}

OAIJurisdictionList::~OAIJurisdictionList() {}

void OAIJurisdictionList::initializeModel() {

    m_pagination_isSet = false;
    m_pagination_isValid = false;

    m_results_isSet = false;
    m_results_isValid = false;
}

void OAIJurisdictionList::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIJurisdictionList::fromJsonObject(QJsonObject json) {

    m_pagination_isValid = ::OpenAPI::fromJsonValue(m_pagination, json[QString("pagination")]);
    m_pagination_isSet = !json[QString("pagination")].isNull() && m_pagination_isValid;

    m_results_isValid = ::OpenAPI::fromJsonValue(m_results, json[QString("results")]);
    m_results_isSet = !json[QString("results")].isNull() && m_results_isValid;
}

QString OAIJurisdictionList::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIJurisdictionList::asJsonObject() const {
    QJsonObject obj;
    if (m_pagination.isSet()) {
        obj.insert(QString("pagination"), ::OpenAPI::toJsonValue(m_pagination));
    }
    if (m_results.size() > 0) {
        obj.insert(QString("results"), ::OpenAPI::toJsonValue(m_results));
    }
    return obj;
}

OAIPaginationMeta OAIJurisdictionList::getPagination() const {
    return m_pagination;
}
void OAIJurisdictionList::setPagination(const OAIPaginationMeta &pagination) {
    m_pagination = pagination;
    m_pagination_isSet = true;
}

bool OAIJurisdictionList::is_pagination_Set() const{
    return m_pagination_isSet;
}

bool OAIJurisdictionList::is_pagination_Valid() const{
    return m_pagination_isValid;
}

QList<OAIJurisdiction> OAIJurisdictionList::getResults() const {
    return m_results;
}
void OAIJurisdictionList::setResults(const QList<OAIJurisdiction> &results) {
    m_results = results;
    m_results_isSet = true;
}

bool OAIJurisdictionList::is_results_Set() const{
    return m_results_isSet;
}

bool OAIJurisdictionList::is_results_Valid() const{
    return m_results_isValid;
}

bool OAIJurisdictionList::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_pagination.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_results.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIJurisdictionList::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_pagination_isValid && m_results_isValid && true;
}

} // namespace OpenAPI
