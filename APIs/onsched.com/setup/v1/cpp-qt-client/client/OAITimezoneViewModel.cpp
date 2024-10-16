/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITimezoneViewModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITimezoneViewModel::OAITimezoneViewModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITimezoneViewModel::OAITimezoneViewModel() {
    this->initializeModel();
}

OAITimezoneViewModel::~OAITimezoneViewModel() {}

void OAITimezoneViewModel::initializeModel() {

    m_object_isSet = false;
    m_object_isValid = false;

    m_regions_isSet = false;
    m_regions_isValid = false;

    m_timezones_isSet = false;
    m_timezones_isValid = false;
}

void OAITimezoneViewModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITimezoneViewModel::fromJsonObject(QJsonObject json) {

    m_object_isValid = ::OpenAPI::fromJsonValue(m_object, json[QString("object")]);
    m_object_isSet = !json[QString("object")].isNull() && m_object_isValid;

    m_regions_isValid = ::OpenAPI::fromJsonValue(m_regions, json[QString("regions")]);
    m_regions_isSet = !json[QString("regions")].isNull() && m_regions_isValid;

    m_timezones_isValid = ::OpenAPI::fromJsonValue(m_timezones, json[QString("timezones")]);
    m_timezones_isSet = !json[QString("timezones")].isNull() && m_timezones_isValid;
}

QString OAITimezoneViewModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITimezoneViewModel::asJsonObject() const {
    QJsonObject obj;
    if (m_object_isSet) {
        obj.insert(QString("object"), ::OpenAPI::toJsonValue(m_object));
    }
    if (m_regions.size() > 0) {
        obj.insert(QString("regions"), ::OpenAPI::toJsonValue(m_regions));
    }
    if (m_timezones.size() > 0) {
        obj.insert(QString("timezones"), ::OpenAPI::toJsonValue(m_timezones));
    }
    return obj;
}

QString OAITimezoneViewModel::getObject() const {
    return m_object;
}
void OAITimezoneViewModel::setObject(const QString &object) {
    m_object = object;
    m_object_isSet = true;
}

bool OAITimezoneViewModel::is_object_Set() const{
    return m_object_isSet;
}

bool OAITimezoneViewModel::is_object_Valid() const{
    return m_object_isValid;
}

QList<QString> OAITimezoneViewModel::getRegions() const {
    return m_regions;
}
void OAITimezoneViewModel::setRegions(const QList<QString> &regions) {
    m_regions = regions;
    m_regions_isSet = true;
}

bool OAITimezoneViewModel::is_regions_Set() const{
    return m_regions_isSet;
}

bool OAITimezoneViewModel::is_regions_Valid() const{
    return m_regions_isValid;
}

QList<OAITimezonesViewModel> OAITimezoneViewModel::getTimezones() const {
    return m_timezones;
}
void OAITimezoneViewModel::setTimezones(const QList<OAITimezonesViewModel> &timezones) {
    m_timezones = timezones;
    m_timezones_isSet = true;
}

bool OAITimezoneViewModel::is_timezones_Set() const{
    return m_timezones_isSet;
}

bool OAITimezoneViewModel::is_timezones_Valid() const{
    return m_timezones_isValid;
}

bool OAITimezoneViewModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_object_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_regions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_timezones.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITimezoneViewModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
