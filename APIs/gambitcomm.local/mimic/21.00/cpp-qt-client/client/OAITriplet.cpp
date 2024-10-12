/**
 * MIMIC REST API
 * This is the API for MIMIC client to connect to MIMIC daemon.
 *
 * The version of the OpenAPI document: 21.00
 * Contact: support@gambitcomm.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITriplet.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITriplet::OAITriplet(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITriplet::OAITriplet() {
    this->initializeModel();
}

OAITriplet::~OAITriplet() {}

void OAITriplet::initializeModel() {

    m_device_isSet = false;
    m_device_isValid = false;

    m_mib_isSet = false;
    m_mib_isValid = false;

    m_scenario_isSet = false;
    m_scenario_isValid = false;
}

void OAITriplet::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITriplet::fromJsonObject(QJsonObject json) {

    m_device_isValid = ::OpenAPI::fromJsonValue(m_device, json[QString("device")]);
    m_device_isSet = !json[QString("device")].isNull() && m_device_isValid;

    m_mib_isValid = ::OpenAPI::fromJsonValue(m_mib, json[QString("mib")]);
    m_mib_isSet = !json[QString("mib")].isNull() && m_mib_isValid;

    m_scenario_isValid = ::OpenAPI::fromJsonValue(m_scenario, json[QString("scenario")]);
    m_scenario_isSet = !json[QString("scenario")].isNull() && m_scenario_isValid;
}

QString OAITriplet::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITriplet::asJsonObject() const {
    QJsonObject obj;
    if (m_device_isSet) {
        obj.insert(QString("device"), ::OpenAPI::toJsonValue(m_device));
    }
    if (m_mib_isSet) {
        obj.insert(QString("mib"), ::OpenAPI::toJsonValue(m_mib));
    }
    if (m_scenario_isSet) {
        obj.insert(QString("scenario"), ::OpenAPI::toJsonValue(m_scenario));
    }
    return obj;
}

QString OAITriplet::getDevice() const {
    return m_device;
}
void OAITriplet::setDevice(const QString &device) {
    m_device = device;
    m_device_isSet = true;
}

bool OAITriplet::is_device_Set() const{
    return m_device_isSet;
}

bool OAITriplet::is_device_Valid() const{
    return m_device_isValid;
}

QString OAITriplet::getMib() const {
    return m_mib;
}
void OAITriplet::setMib(const QString &mib) {
    m_mib = mib;
    m_mib_isSet = true;
}

bool OAITriplet::is_mib_Set() const{
    return m_mib_isSet;
}

bool OAITriplet::is_mib_Valid() const{
    return m_mib_isValid;
}

qint32 OAITriplet::getScenario() const {
    return m_scenario;
}
void OAITriplet::setScenario(const qint32 &scenario) {
    m_scenario = scenario;
    m_scenario_isSet = true;
}

bool OAITriplet::is_scenario_Set() const{
    return m_scenario_isSet;
}

bool OAITriplet::is_scenario_Valid() const{
    return m_scenario_isValid;
}

bool OAITriplet::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_device_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mib_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scenario_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITriplet::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
