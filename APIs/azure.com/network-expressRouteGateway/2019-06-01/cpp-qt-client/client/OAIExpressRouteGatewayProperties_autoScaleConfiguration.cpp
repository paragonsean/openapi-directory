/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIExpressRouteGatewayProperties_autoScaleConfiguration.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExpressRouteGatewayProperties_autoScaleConfiguration::OAIExpressRouteGatewayProperties_autoScaleConfiguration(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExpressRouteGatewayProperties_autoScaleConfiguration::OAIExpressRouteGatewayProperties_autoScaleConfiguration() {
    this->initializeModel();
}

OAIExpressRouteGatewayProperties_autoScaleConfiguration::~OAIExpressRouteGatewayProperties_autoScaleConfiguration() {}

void OAIExpressRouteGatewayProperties_autoScaleConfiguration::initializeModel() {

    m_bounds_isSet = false;
    m_bounds_isValid = false;
}

void OAIExpressRouteGatewayProperties_autoScaleConfiguration::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExpressRouteGatewayProperties_autoScaleConfiguration::fromJsonObject(QJsonObject json) {

    m_bounds_isValid = ::OpenAPI::fromJsonValue(m_bounds, json[QString("bounds")]);
    m_bounds_isSet = !json[QString("bounds")].isNull() && m_bounds_isValid;
}

QString OAIExpressRouteGatewayProperties_autoScaleConfiguration::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExpressRouteGatewayProperties_autoScaleConfiguration::asJsonObject() const {
    QJsonObject obj;
    if (m_bounds.isSet()) {
        obj.insert(QString("bounds"), ::OpenAPI::toJsonValue(m_bounds));
    }
    return obj;
}

OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds OAIExpressRouteGatewayProperties_autoScaleConfiguration::getBounds() const {
    return m_bounds;
}
void OAIExpressRouteGatewayProperties_autoScaleConfiguration::setBounds(const OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds &bounds) {
    m_bounds = bounds;
    m_bounds_isSet = true;
}

bool OAIExpressRouteGatewayProperties_autoScaleConfiguration::is_bounds_Set() const{
    return m_bounds_isSet;
}

bool OAIExpressRouteGatewayProperties_autoScaleConfiguration::is_bounds_Valid() const{
    return m_bounds_isValid;
}

bool OAIExpressRouteGatewayProperties_autoScaleConfiguration::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bounds.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExpressRouteGatewayProperties_autoScaleConfiguration::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
