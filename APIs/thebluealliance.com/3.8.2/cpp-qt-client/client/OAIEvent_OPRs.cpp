/**
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEvent_OPRs.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEvent_OPRs::OAIEvent_OPRs(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEvent_OPRs::OAIEvent_OPRs() {
    this->initializeModel();
}

OAIEvent_OPRs::~OAIEvent_OPRs() {}

void OAIEvent_OPRs::initializeModel() {

    m_ccwms_isSet = false;
    m_ccwms_isValid = false;

    m_dprs_isSet = false;
    m_dprs_isValid = false;

    m_oprs_isSet = false;
    m_oprs_isValid = false;
}

void OAIEvent_OPRs::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEvent_OPRs::fromJsonObject(QJsonObject json) {

    m_ccwms_isValid = ::OpenAPI::fromJsonValue(m_ccwms, json[QString("ccwms")]);
    m_ccwms_isSet = !json[QString("ccwms")].isNull() && m_ccwms_isValid;

    m_dprs_isValid = ::OpenAPI::fromJsonValue(m_dprs, json[QString("dprs")]);
    m_dprs_isSet = !json[QString("dprs")].isNull() && m_dprs_isValid;

    m_oprs_isValid = ::OpenAPI::fromJsonValue(m_oprs, json[QString("oprs")]);
    m_oprs_isSet = !json[QString("oprs")].isNull() && m_oprs_isValid;
}

QString OAIEvent_OPRs::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEvent_OPRs::asJsonObject() const {
    QJsonObject obj;
    if (m_ccwms.size() > 0) {
        obj.insert(QString("ccwms"), ::OpenAPI::toJsonValue(m_ccwms));
    }
    if (m_dprs.size() > 0) {
        obj.insert(QString("dprs"), ::OpenAPI::toJsonValue(m_dprs));
    }
    if (m_oprs.size() > 0) {
        obj.insert(QString("oprs"), ::OpenAPI::toJsonValue(m_oprs));
    }
    return obj;
}

QMap<QString, float> OAIEvent_OPRs::getCcwms() const {
    return m_ccwms;
}
void OAIEvent_OPRs::setCcwms(const QMap<QString, float> &ccwms) {
    m_ccwms = ccwms;
    m_ccwms_isSet = true;
}

bool OAIEvent_OPRs::is_ccwms_Set() const{
    return m_ccwms_isSet;
}

bool OAIEvent_OPRs::is_ccwms_Valid() const{
    return m_ccwms_isValid;
}

QMap<QString, float> OAIEvent_OPRs::getDprs() const {
    return m_dprs;
}
void OAIEvent_OPRs::setDprs(const QMap<QString, float> &dprs) {
    m_dprs = dprs;
    m_dprs_isSet = true;
}

bool OAIEvent_OPRs::is_dprs_Set() const{
    return m_dprs_isSet;
}

bool OAIEvent_OPRs::is_dprs_Valid() const{
    return m_dprs_isValid;
}

QMap<QString, float> OAIEvent_OPRs::getOprs() const {
    return m_oprs;
}
void OAIEvent_OPRs::setOprs(const QMap<QString, float> &oprs) {
    m_oprs = oprs;
    m_oprs_isSet = true;
}

bool OAIEvent_OPRs::is_oprs_Set() const{
    return m_oprs_isSet;
}

bool OAIEvent_OPRs::is_oprs_Valid() const{
    return m_oprs_isValid;
}

bool OAIEvent_OPRs::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ccwms.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_dprs.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_oprs.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEvent_OPRs::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
