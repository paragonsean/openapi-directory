/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWannabeAddonBilling.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWannabeAddonBilling::OAIWannabeAddonBilling(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWannabeAddonBilling::OAIWannabeAddonBilling() {
    this->initializeModel();
}

OAIWannabeAddonBilling::~OAIWannabeAddonBilling() {}

void OAIWannabeAddonBilling::initializeModel() {

    m_cost_isSet = false;
    m_cost_isValid = false;
}

void OAIWannabeAddonBilling::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWannabeAddonBilling::fromJsonObject(QJsonObject json) {

    m_cost_isValid = ::OpenAPI::fromJsonValue(m_cost, json[QString("cost")]);
    m_cost_isSet = !json[QString("cost")].isNull() && m_cost_isValid;
}

QString OAIWannabeAddonBilling::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWannabeAddonBilling::asJsonObject() const {
    QJsonObject obj;
    if (m_cost_isSet) {
        obj.insert(QString("cost"), ::OpenAPI::toJsonValue(m_cost));
    }
    return obj;
}

double OAIWannabeAddonBilling::getCost() const {
    return m_cost;
}
void OAIWannabeAddonBilling::setCost(const double &cost) {
    m_cost = cost;
    m_cost_isSet = true;
}

bool OAIWannabeAddonBilling::is_cost_Set() const{
    return m_cost_isSet;
}

bool OAIWannabeAddonBilling::is_cost_Valid() const{
    return m_cost_isValid;
}

bool OAIWannabeAddonBilling::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cost_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWannabeAddonBilling::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_cost_isValid && true;
}

} // namespace OpenAPI
