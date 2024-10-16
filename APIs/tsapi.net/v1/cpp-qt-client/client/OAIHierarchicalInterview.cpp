/**
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHierarchicalInterview.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHierarchicalInterview::OAIHierarchicalInterview(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHierarchicalInterview::OAIHierarchicalInterview() {
    this->initializeModel();
}

OAIHierarchicalInterview::~OAIHierarchicalInterview() {}

void OAIHierarchicalInterview::initializeModel() {

    m_data_items_isSet = false;
    m_data_items_isValid = false;

    m_hierarchical_interviews_isSet = false;
    m_hierarchical_interviews_isValid = false;

    m_ident_isSet = false;
    m_ident_isValid = false;

    m_level_isSet = false;
    m_level_isValid = false;
}

void OAIHierarchicalInterview::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHierarchicalInterview::fromJsonObject(QJsonObject json) {

    m_data_items_isValid = ::OpenAPI::fromJsonValue(m_data_items, json[QString("dataItems")]);
    m_data_items_isSet = !json[QString("dataItems")].isNull() && m_data_items_isValid;

    m_hierarchical_interviews_isValid = ::OpenAPI::fromJsonValue(m_hierarchical_interviews, json[QString("hierarchicalInterviews")]);
    m_hierarchical_interviews_isSet = !json[QString("hierarchicalInterviews")].isNull() && m_hierarchical_interviews_isValid;

    m_ident_isValid = ::OpenAPI::fromJsonValue(m_ident, json[QString("ident")]);
    m_ident_isSet = !json[QString("ident")].isNull() && m_ident_isValid;

    m_level_isValid = ::OpenAPI::fromJsonValue(m_level, json[QString("level")]);
    m_level_isSet = !json[QString("level")].isNull() && m_level_isValid;
}

QString OAIHierarchicalInterview::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHierarchicalInterview::asJsonObject() const {
    QJsonObject obj;
    if (m_data_items.size() > 0) {
        obj.insert(QString("dataItems"), ::OpenAPI::toJsonValue(m_data_items));
    }
    if (m_hierarchical_interviews.size() > 0) {
        obj.insert(QString("hierarchicalInterviews"), ::OpenAPI::toJsonValue(m_hierarchical_interviews));
    }
    if (m_ident_isSet) {
        obj.insert(QString("ident"), ::OpenAPI::toJsonValue(m_ident));
    }
    if (m_level.isSet()) {
        obj.insert(QString("level"), ::OpenAPI::toJsonValue(m_level));
    }
    return obj;
}

QList<OAIDataItem> OAIHierarchicalInterview::getDataItems() const {
    return m_data_items;
}
void OAIHierarchicalInterview::setDataItems(const QList<OAIDataItem> &data_items) {
    m_data_items = data_items;
    m_data_items_isSet = true;
}

bool OAIHierarchicalInterview::is_data_items_Set() const{
    return m_data_items_isSet;
}

bool OAIHierarchicalInterview::is_data_items_Valid() const{
    return m_data_items_isValid;
}

QList<OAIHierarchicalInterview> OAIHierarchicalInterview::getHierarchicalInterviews() const {
    return m_hierarchical_interviews;
}
void OAIHierarchicalInterview::setHierarchicalInterviews(const QList<OAIHierarchicalInterview> &hierarchical_interviews) {
    m_hierarchical_interviews = hierarchical_interviews;
    m_hierarchical_interviews_isSet = true;
}

bool OAIHierarchicalInterview::is_hierarchical_interviews_Set() const{
    return m_hierarchical_interviews_isSet;
}

bool OAIHierarchicalInterview::is_hierarchical_interviews_Valid() const{
    return m_hierarchical_interviews_isValid;
}

QString OAIHierarchicalInterview::getIdent() const {
    return m_ident;
}
void OAIHierarchicalInterview::setIdent(const QString &ident) {
    m_ident = ident;
    m_ident_isSet = true;
}

bool OAIHierarchicalInterview::is_ident_Set() const{
    return m_ident_isSet;
}

bool OAIHierarchicalInterview::is_ident_Valid() const{
    return m_ident_isValid;
}

OAILevel OAIHierarchicalInterview::getLevel() const {
    return m_level;
}
void OAIHierarchicalInterview::setLevel(const OAILevel &level) {
    m_level = level;
    m_level_isSet = true;
}

bool OAIHierarchicalInterview::is_level_Set() const{
    return m_level_isSet;
}

bool OAIHierarchicalInterview::is_level_Valid() const{
    return m_level_isValid;
}

bool OAIHierarchicalInterview::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_hierarchical_interviews.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_ident_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_level.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHierarchicalInterview::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
