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

#include "OAIVlan.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVlan::OAIVlan(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVlan::OAIVlan() {
    this->initializeModel();
}

OAIVlan::~OAIVlan() {}

void OAIVlan::initializeModel() {

    m_begin_isSet = false;
    m_begin_isValid = false;

    m_end_isSet = false;
    m_end_isValid = false;
}

void OAIVlan::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVlan::fromJsonObject(QJsonObject json) {

    m_begin_isValid = ::OpenAPI::fromJsonValue(m_begin, json[QString("begin")]);
    m_begin_isSet = !json[QString("begin")].isNull() && m_begin_isValid;

    m_end_isValid = ::OpenAPI::fromJsonValue(m_end, json[QString("end")]);
    m_end_isSet = !json[QString("end")].isNull() && m_end_isValid;
}

QString OAIVlan::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVlan::asJsonObject() const {
    QJsonObject obj;
    if (m_begin_isSet) {
        obj.insert(QString("begin"), ::OpenAPI::toJsonValue(m_begin));
    }
    if (m_end_isSet) {
        obj.insert(QString("end"), ::OpenAPI::toJsonValue(m_end));
    }
    return obj;
}

qint32 OAIVlan::getBegin() const {
    return m_begin;
}
void OAIVlan::setBegin(const qint32 &begin) {
    m_begin = begin;
    m_begin_isSet = true;
}

bool OAIVlan::is_begin_Set() const{
    return m_begin_isSet;
}

bool OAIVlan::is_begin_Valid() const{
    return m_begin_isValid;
}

qint32 OAIVlan::getEnd() const {
    return m_end;
}
void OAIVlan::setEnd(const qint32 &end) {
    m_end = end;
    m_end_isSet = true;
}

bool OAIVlan::is_end_Set() const{
    return m_end_isSet;
}

bool OAIVlan::is_end_Valid() const{
    return m_end_isValid;
}

bool OAIVlan::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_begin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVlan::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
