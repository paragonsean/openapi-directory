/**
 * Highways England API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAreaResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAreaResponse::OAIAreaResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAreaResponse::OAIAreaResponse() {
    this->initializeModel();
}

OAIAreaResponse::~OAIAreaResponse() {}

void OAIAreaResponse::initializeModel() {

    m_areas_isSet = false;
    m_areas_isValid = false;

    m_row_count_isSet = false;
    m_row_count_isValid = false;
}

void OAIAreaResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAreaResponse::fromJsonObject(QJsonObject json) {

    m_areas_isValid = ::OpenAPI::fromJsonValue(m_areas, json[QString("areas")]);
    m_areas_isSet = !json[QString("areas")].isNull() && m_areas_isValid;

    m_row_count_isValid = ::OpenAPI::fromJsonValue(m_row_count, json[QString("row_count")]);
    m_row_count_isSet = !json[QString("row_count")].isNull() && m_row_count_isValid;
}

QString OAIAreaResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAreaResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_areas.size() > 0) {
        obj.insert(QString("areas"), ::OpenAPI::toJsonValue(m_areas));
    }
    if (m_row_count_isSet) {
        obj.insert(QString("row_count"), ::OpenAPI::toJsonValue(m_row_count));
    }
    return obj;
}

QList<OAIArea> OAIAreaResponse::getAreas() const {
    return m_areas;
}
void OAIAreaResponse::setAreas(const QList<OAIArea> &areas) {
    m_areas = areas;
    m_areas_isSet = true;
}

bool OAIAreaResponse::is_areas_Set() const{
    return m_areas_isSet;
}

bool OAIAreaResponse::is_areas_Valid() const{
    return m_areas_isValid;
}

qint32 OAIAreaResponse::getRowCount() const {
    return m_row_count;
}
void OAIAreaResponse::setRowCount(const qint32 &row_count) {
    m_row_count = row_count;
    m_row_count_isSet = true;
}

bool OAIAreaResponse::is_row_count_Set() const{
    return m_row_count_isSet;
}

bool OAIAreaResponse::is_row_count_Valid() const{
    return m_row_count_isValid;
}

bool OAIAreaResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_areas.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_row_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAreaResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
