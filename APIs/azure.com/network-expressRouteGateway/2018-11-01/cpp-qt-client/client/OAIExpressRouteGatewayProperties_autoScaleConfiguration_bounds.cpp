/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds() {
    this->initializeModel();
}

OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::~OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds() {}

void OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::initializeModel() {

    m_max_isSet = false;
    m_max_isValid = false;

    m_min_isSet = false;
    m_min_isValid = false;
}

void OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::fromJsonObject(QJsonObject json) {

    m_max_isValid = ::OpenAPI::fromJsonValue(m_max, json[QString("max")]);
    m_max_isSet = !json[QString("max")].isNull() && m_max_isValid;

    m_min_isValid = ::OpenAPI::fromJsonValue(m_min, json[QString("min")]);
    m_min_isSet = !json[QString("min")].isNull() && m_min_isValid;
}

QString OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::asJsonObject() const {
    QJsonObject obj;
    if (m_max_isSet) {
        obj.insert(QString("max"), ::OpenAPI::toJsonValue(m_max));
    }
    if (m_min_isSet) {
        obj.insert(QString("min"), ::OpenAPI::toJsonValue(m_min));
    }
    return obj;
}

qint32 OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::getMax() const {
    return m_max;
}
void OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::setMax(const qint32 &max) {
    m_max = max;
    m_max_isSet = true;
}

bool OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::is_max_Set() const{
    return m_max_isSet;
}

bool OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::is_max_Valid() const{
    return m_max_isValid;
}

qint32 OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::getMin() const {
    return m_min;
}
void OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::setMin(const qint32 &min) {
    m_min = min;
    m_min_isSet = true;
}

bool OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::is_min_Set() const{
    return m_min_isSet;
}

bool OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::is_min_Valid() const{
    return m_min_isValid;
}

bool OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_max_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_min_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
