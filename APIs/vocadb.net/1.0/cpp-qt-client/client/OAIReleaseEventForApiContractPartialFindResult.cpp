/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIReleaseEventForApiContractPartialFindResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIReleaseEventForApiContractPartialFindResult::OAIReleaseEventForApiContractPartialFindResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIReleaseEventForApiContractPartialFindResult::OAIReleaseEventForApiContractPartialFindResult() {
    this->initializeModel();
}

OAIReleaseEventForApiContractPartialFindResult::~OAIReleaseEventForApiContractPartialFindResult() {}

void OAIReleaseEventForApiContractPartialFindResult::initializeModel() {

    m_items_isSet = false;
    m_items_isValid = false;

    m_term_isSet = false;
    m_term_isValid = false;

    m_total_count_isSet = false;
    m_total_count_isValid = false;
}

void OAIReleaseEventForApiContractPartialFindResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIReleaseEventForApiContractPartialFindResult::fromJsonObject(QJsonObject json) {

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;

    m_term_isValid = ::OpenAPI::fromJsonValue(m_term, json[QString("term")]);
    m_term_isSet = !json[QString("term")].isNull() && m_term_isValid;

    m_total_count_isValid = ::OpenAPI::fromJsonValue(m_total_count, json[QString("totalCount")]);
    m_total_count_isSet = !json[QString("totalCount")].isNull() && m_total_count_isValid;
}

QString OAIReleaseEventForApiContractPartialFindResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIReleaseEventForApiContractPartialFindResult::asJsonObject() const {
    QJsonObject obj;
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_term_isSet) {
        obj.insert(QString("term"), ::OpenAPI::toJsonValue(m_term));
    }
    if (m_total_count_isSet) {
        obj.insert(QString("totalCount"), ::OpenAPI::toJsonValue(m_total_count));
    }
    return obj;
}

QList<OAIReleaseEventForApiContract> OAIReleaseEventForApiContractPartialFindResult::getItems() const {
    return m_items;
}
void OAIReleaseEventForApiContractPartialFindResult::setItems(const QList<OAIReleaseEventForApiContract> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIReleaseEventForApiContractPartialFindResult::is_items_Set() const{
    return m_items_isSet;
}

bool OAIReleaseEventForApiContractPartialFindResult::is_items_Valid() const{
    return m_items_isValid;
}

QString OAIReleaseEventForApiContractPartialFindResult::getTerm() const {
    return m_term;
}
void OAIReleaseEventForApiContractPartialFindResult::setTerm(const QString &term) {
    m_term = term;
    m_term_isSet = true;
}

bool OAIReleaseEventForApiContractPartialFindResult::is_term_Set() const{
    return m_term_isSet;
}

bool OAIReleaseEventForApiContractPartialFindResult::is_term_Valid() const{
    return m_term_isValid;
}

qint32 OAIReleaseEventForApiContractPartialFindResult::getTotalCount() const {
    return m_total_count;
}
void OAIReleaseEventForApiContractPartialFindResult::setTotalCount(const qint32 &total_count) {
    m_total_count = total_count;
    m_total_count_isSet = true;
}

bool OAIReleaseEventForApiContractPartialFindResult::is_total_count_Set() const{
    return m_total_count_isSet;
}

bool OAIReleaseEventForApiContractPartialFindResult::is_total_count_Valid() const{
    return m_total_count_isValid;
}

bool OAIReleaseEventForApiContractPartialFindResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_term_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIReleaseEventForApiContractPartialFindResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
