/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISimplePortRange.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISimplePortRange::OAISimplePortRange(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISimplePortRange::OAISimplePortRange() {
    this->initializeModel();
}

OAISimplePortRange::~OAISimplePortRange() {}

void OAISimplePortRange::initializeModel() {

    m_end_isSet = false;
    m_end_isValid = false;

    m_start_isSet = false;
    m_start_isValid = false;
}

void OAISimplePortRange::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISimplePortRange::fromJsonObject(QJsonObject json) {

    m_end_isValid = ::OpenAPI::fromJsonValue(m_end, json[QString("end")]);
    m_end_isSet = !json[QString("end")].isNull() && m_end_isValid;

    m_start_isValid = ::OpenAPI::fromJsonValue(m_start, json[QString("start")]);
    m_start_isSet = !json[QString("start")].isNull() && m_start_isValid;
}

QString OAISimplePortRange::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISimplePortRange::asJsonObject() const {
    QJsonObject obj;
    if (m_end_isSet) {
        obj.insert(QString("end"), ::OpenAPI::toJsonValue(m_end));
    }
    if (m_start_isSet) {
        obj.insert(QString("start"), ::OpenAPI::toJsonValue(m_start));
    }
    return obj;
}

qint32 OAISimplePortRange::getEnd() const {
    return m_end;
}
void OAISimplePortRange::setEnd(const qint32 &end) {
    m_end = end;
    m_end_isSet = true;
}

bool OAISimplePortRange::is_end_Set() const{
    return m_end_isSet;
}

bool OAISimplePortRange::is_end_Valid() const{
    return m_end_isValid;
}

qint32 OAISimplePortRange::getStart() const {
    return m_start;
}
void OAISimplePortRange::setStart(const qint32 &start) {
    m_start = start;
    m_start_isSet = true;
}

bool OAISimplePortRange::is_start_Set() const{
    return m_start_isSet;
}

bool OAISimplePortRange::is_start_Valid() const{
    return m_start_isValid;
}

bool OAISimplePortRange::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_end_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISimplePortRange::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
