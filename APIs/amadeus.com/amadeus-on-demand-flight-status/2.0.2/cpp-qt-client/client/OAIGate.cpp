/**
 * On-Demand Flight Status
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.     Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGate.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGate::OAIGate(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGate::OAIGate() {
    this->initializeModel();
}

OAIGate::~OAIGate() {}

void OAIGate::initializeModel() {

    m_main_gate_isSet = false;
    m_main_gate_isValid = false;
}

void OAIGate::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGate::fromJsonObject(QJsonObject json) {

    m_main_gate_isValid = ::OpenAPI::fromJsonValue(m_main_gate, json[QString("mainGate")]);
    m_main_gate_isSet = !json[QString("mainGate")].isNull() && m_main_gate_isValid;
}

QString OAIGate::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGate::asJsonObject() const {
    QJsonObject obj;
    if (m_main_gate_isSet) {
        obj.insert(QString("mainGate"), ::OpenAPI::toJsonValue(m_main_gate));
    }
    return obj;
}

QString OAIGate::getMainGate() const {
    return m_main_gate;
}
void OAIGate::setMainGate(const QString &main_gate) {
    m_main_gate = main_gate;
    m_main_gate_isSet = true;
}

bool OAIGate::is_main_gate_Set() const{
    return m_main_gate_isSet;
}

bool OAIGate::is_main_gate_Valid() const{
    return m_main_gate_isValid;
}

bool OAIGate::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_main_gate_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGate::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
