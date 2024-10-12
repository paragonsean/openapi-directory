/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-10-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIExpressRouteGatewayList.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExpressRouteGatewayList::OAIExpressRouteGatewayList(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExpressRouteGatewayList::OAIExpressRouteGatewayList() {
    this->initializeModel();
}

OAIExpressRouteGatewayList::~OAIExpressRouteGatewayList() {}

void OAIExpressRouteGatewayList::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIExpressRouteGatewayList::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExpressRouteGatewayList::fromJsonObject(QJsonObject json) {

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIExpressRouteGatewayList::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExpressRouteGatewayList::asJsonObject() const {
    QJsonObject obj;
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QList<OAIExpressRouteGateway> OAIExpressRouteGatewayList::getValue() const {
    return m_value;
}
void OAIExpressRouteGatewayList::setValue(const QList<OAIExpressRouteGateway> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIExpressRouteGatewayList::is_value_Set() const{
    return m_value_isSet;
}

bool OAIExpressRouteGatewayList::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIExpressRouteGatewayList::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_value.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExpressRouteGatewayList::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
