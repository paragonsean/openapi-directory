/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRma_data_track_search_result_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRma_data_track_search_result_interface::OAIRma_data_track_search_result_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRma_data_track_search_result_interface::OAIRma_data_track_search_result_interface() {
    this->initializeModel();
}

OAIRma_data_track_search_result_interface::~OAIRma_data_track_search_result_interface() {}

void OAIRma_data_track_search_result_interface::initializeModel() {

    m_items_isSet = false;
    m_items_isValid = false;

    m_search_criteria_isSet = false;
    m_search_criteria_isValid = false;

    m_total_count_isSet = false;
    m_total_count_isValid = false;
}

void OAIRma_data_track_search_result_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRma_data_track_search_result_interface::fromJsonObject(QJsonObject json) {

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;

    m_search_criteria_isValid = ::OpenAPI::fromJsonValue(m_search_criteria, json[QString("search_criteria")]);
    m_search_criteria_isSet = !json[QString("search_criteria")].isNull() && m_search_criteria_isValid;

    m_total_count_isValid = ::OpenAPI::fromJsonValue(m_total_count, json[QString("total_count")]);
    m_total_count_isSet = !json[QString("total_count")].isNull() && m_total_count_isValid;
}

QString OAIRma_data_track_search_result_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRma_data_track_search_result_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_search_criteria.isSet()) {
        obj.insert(QString("search_criteria"), ::OpenAPI::toJsonValue(m_search_criteria));
    }
    if (m_total_count_isSet) {
        obj.insert(QString("total_count"), ::OpenAPI::toJsonValue(m_total_count));
    }
    return obj;
}

QList<OAIRma_data_track_interface> OAIRma_data_track_search_result_interface::getItems() const {
    return m_items;
}
void OAIRma_data_track_search_result_interface::setItems(const QList<OAIRma_data_track_interface> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIRma_data_track_search_result_interface::is_items_Set() const{
    return m_items_isSet;
}

bool OAIRma_data_track_search_result_interface::is_items_Valid() const{
    return m_items_isValid;
}

OAIFramework_search_criteria_interface OAIRma_data_track_search_result_interface::getSearchCriteria() const {
    return m_search_criteria;
}
void OAIRma_data_track_search_result_interface::setSearchCriteria(const OAIFramework_search_criteria_interface &search_criteria) {
    m_search_criteria = search_criteria;
    m_search_criteria_isSet = true;
}

bool OAIRma_data_track_search_result_interface::is_search_criteria_Set() const{
    return m_search_criteria_isSet;
}

bool OAIRma_data_track_search_result_interface::is_search_criteria_Valid() const{
    return m_search_criteria_isValid;
}

qint32 OAIRma_data_track_search_result_interface::getTotalCount() const {
    return m_total_count;
}
void OAIRma_data_track_search_result_interface::setTotalCount(const qint32 &total_count) {
    m_total_count = total_count;
    m_total_count_isSet = true;
}

bool OAIRma_data_track_search_result_interface::is_total_count_Set() const{
    return m_total_count_isSet;
}

bool OAIRma_data_track_search_result_interface::is_total_count_Valid() const{
    return m_total_count_isValid;
}

bool OAIRma_data_track_search_result_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_search_criteria.isSet()) {
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

bool OAIRma_data_track_search_result_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_items_isValid && m_search_criteria_isValid && m_total_count_isValid && true;
}

} // namespace OpenAPI
