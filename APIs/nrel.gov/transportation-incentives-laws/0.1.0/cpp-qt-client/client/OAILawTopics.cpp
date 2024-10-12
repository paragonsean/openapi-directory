/**
 * Transportation Laws and Incentives
 * Query our database of federal and state laws and incentives for alternative fuels and vehicles, air quality, fuel efficiency, and other transportation-related topics. This dataset powers the <a href=\"https://afdc.energy.gov/laws\">Federal and State Laws and Incentives</a> on the Alternative Fuels Data Center.
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILawTopics.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILawTopics::OAILawTopics(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILawTopics::OAILawTopics() {
    this->initializeModel();
}

OAILawTopics::~OAILawTopics() {}

void OAILawTopics::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_sort_order_isSet = false;
    m_sort_order_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAILawTopics::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILawTopics::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_sort_order_isValid = ::OpenAPI::fromJsonValue(m_sort_order, json[QString("sort_order")]);
    m_sort_order_isSet = !json[QString("sort_order")].isNull() && m_sort_order_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;
}

QString OAILawTopics::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILawTopics::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_sort_order_isSet) {
        obj.insert(QString("sort_order"), ::OpenAPI::toJsonValue(m_sort_order));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

qint32 OAILawTopics::getId() const {
    return m_id;
}
void OAILawTopics::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAILawTopics::is_id_Set() const{
    return m_id_isSet;
}

bool OAILawTopics::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAILawTopics::getSortOrder() const {
    return m_sort_order;
}
void OAILawTopics::setSortOrder(const qint32 &sort_order) {
    m_sort_order = sort_order;
    m_sort_order_isSet = true;
}

bool OAILawTopics::is_sort_order_Set() const{
    return m_sort_order_isSet;
}

bool OAILawTopics::is_sort_order_Valid() const{
    return m_sort_order_isValid;
}

QString OAILawTopics::getTitle() const {
    return m_title;
}
void OAILawTopics::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAILawTopics::is_title_Set() const{
    return m_title_isSet;
}

bool OAILawTopics::is_title_Valid() const{
    return m_title_isValid;
}

bool OAILawTopics::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sort_order_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILawTopics::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_sort_order_isValid && m_title_isValid && true;
}

} // namespace OpenAPI
