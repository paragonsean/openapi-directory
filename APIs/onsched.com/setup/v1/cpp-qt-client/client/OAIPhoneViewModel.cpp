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

#include "OAIPhoneViewModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPhoneViewModel::OAIPhoneViewModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPhoneViewModel::OAIPhoneViewModel() {
    this->initializeModel();
}

OAIPhoneViewModel::~OAIPhoneViewModel() {}

void OAIPhoneViewModel::initializeModel() {

    m_business_phone_isSet = false;
    m_business_phone_isValid = false;

    m_business_phone_ext_isSet = false;
    m_business_phone_ext_isValid = false;

    m_home_phone_isSet = false;
    m_home_phone_isValid = false;

    m_mobile_phone_isSet = false;
    m_mobile_phone_isValid = false;

    m_phone_type_isSet = false;
    m_phone_type_isValid = false;
}

void OAIPhoneViewModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPhoneViewModel::fromJsonObject(QJsonObject json) {

    m_business_phone_isValid = ::OpenAPI::fromJsonValue(m_business_phone, json[QString("businessPhone")]);
    m_business_phone_isSet = !json[QString("businessPhone")].isNull() && m_business_phone_isValid;

    m_business_phone_ext_isValid = ::OpenAPI::fromJsonValue(m_business_phone_ext, json[QString("businessPhoneExt")]);
    m_business_phone_ext_isSet = !json[QString("businessPhoneExt")].isNull() && m_business_phone_ext_isValid;

    m_home_phone_isValid = ::OpenAPI::fromJsonValue(m_home_phone, json[QString("homePhone")]);
    m_home_phone_isSet = !json[QString("homePhone")].isNull() && m_home_phone_isValid;

    m_mobile_phone_isValid = ::OpenAPI::fromJsonValue(m_mobile_phone, json[QString("mobilePhone")]);
    m_mobile_phone_isSet = !json[QString("mobilePhone")].isNull() && m_mobile_phone_isValid;

    m_phone_type_isValid = ::OpenAPI::fromJsonValue(m_phone_type, json[QString("phoneType")]);
    m_phone_type_isSet = !json[QString("phoneType")].isNull() && m_phone_type_isValid;
}

QString OAIPhoneViewModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPhoneViewModel::asJsonObject() const {
    QJsonObject obj;
    if (m_business_phone_isSet) {
        obj.insert(QString("businessPhone"), ::OpenAPI::toJsonValue(m_business_phone));
    }
    if (m_business_phone_ext_isSet) {
        obj.insert(QString("businessPhoneExt"), ::OpenAPI::toJsonValue(m_business_phone_ext));
    }
    if (m_home_phone_isSet) {
        obj.insert(QString("homePhone"), ::OpenAPI::toJsonValue(m_home_phone));
    }
    if (m_mobile_phone_isSet) {
        obj.insert(QString("mobilePhone"), ::OpenAPI::toJsonValue(m_mobile_phone));
    }
    if (m_phone_type_isSet) {
        obj.insert(QString("phoneType"), ::OpenAPI::toJsonValue(m_phone_type));
    }
    return obj;
}

QString OAIPhoneViewModel::getBusinessPhone() const {
    return m_business_phone;
}
void OAIPhoneViewModel::setBusinessPhone(const QString &business_phone) {
    m_business_phone = business_phone;
    m_business_phone_isSet = true;
}

bool OAIPhoneViewModel::is_business_phone_Set() const{
    return m_business_phone_isSet;
}

bool OAIPhoneViewModel::is_business_phone_Valid() const{
    return m_business_phone_isValid;
}

QString OAIPhoneViewModel::getBusinessPhoneExt() const {
    return m_business_phone_ext;
}
void OAIPhoneViewModel::setBusinessPhoneExt(const QString &business_phone_ext) {
    m_business_phone_ext = business_phone_ext;
    m_business_phone_ext_isSet = true;
}

bool OAIPhoneViewModel::is_business_phone_ext_Set() const{
    return m_business_phone_ext_isSet;
}

bool OAIPhoneViewModel::is_business_phone_ext_Valid() const{
    return m_business_phone_ext_isValid;
}

QString OAIPhoneViewModel::getHomePhone() const {
    return m_home_phone;
}
void OAIPhoneViewModel::setHomePhone(const QString &home_phone) {
    m_home_phone = home_phone;
    m_home_phone_isSet = true;
}

bool OAIPhoneViewModel::is_home_phone_Set() const{
    return m_home_phone_isSet;
}

bool OAIPhoneViewModel::is_home_phone_Valid() const{
    return m_home_phone_isValid;
}

QString OAIPhoneViewModel::getMobilePhone() const {
    return m_mobile_phone;
}
void OAIPhoneViewModel::setMobilePhone(const QString &mobile_phone) {
    m_mobile_phone = mobile_phone;
    m_mobile_phone_isSet = true;
}

bool OAIPhoneViewModel::is_mobile_phone_Set() const{
    return m_mobile_phone_isSet;
}

bool OAIPhoneViewModel::is_mobile_phone_Valid() const{
    return m_mobile_phone_isValid;
}

QString OAIPhoneViewModel::getPhoneType() const {
    return m_phone_type;
}
void OAIPhoneViewModel::setPhoneType(const QString &phone_type) {
    m_phone_type = phone_type;
    m_phone_type_isSet = true;
}

bool OAIPhoneViewModel::is_phone_type_Set() const{
    return m_phone_type_isSet;
}

bool OAIPhoneViewModel::is_phone_type_Valid() const{
    return m_phone_type_isValid;
}

bool OAIPhoneViewModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_business_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_business_phone_ext_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mobile_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPhoneViewModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
