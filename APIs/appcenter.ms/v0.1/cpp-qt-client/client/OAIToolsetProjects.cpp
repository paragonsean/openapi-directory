/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIToolsetProjects.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIToolsetProjects::OAIToolsetProjects(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIToolsetProjects::OAIToolsetProjects() {
    this->initializeModel();
}

OAIToolsetProjects::~OAIToolsetProjects() {}

void OAIToolsetProjects::initializeModel() {

    m_android_isSet = false;
    m_android_isValid = false;

    m_buildscripts_isSet = false;
    m_buildscripts_isValid = false;

    m_commit_isSet = false;
    m_commit_isValid = false;

    m_javascript_isSet = false;
    m_javascript_isValid = false;

    m_testcloud_isSet = false;
    m_testcloud_isValid = false;

    m_uwp_isSet = false;
    m_uwp_isValid = false;

    m_xamarin_isSet = false;
    m_xamarin_isValid = false;

    m_xcode_isSet = false;
    m_xcode_isValid = false;
}

void OAIToolsetProjects::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIToolsetProjects::fromJsonObject(QJsonObject json) {

    m_android_isValid = ::OpenAPI::fromJsonValue(m_android, json[QString("android")]);
    m_android_isSet = !json[QString("android")].isNull() && m_android_isValid;

    m_buildscripts_isValid = ::OpenAPI::fromJsonValue(m_buildscripts, json[QString("buildscripts")]);
    m_buildscripts_isSet = !json[QString("buildscripts")].isNull() && m_buildscripts_isValid;

    m_commit_isValid = ::OpenAPI::fromJsonValue(m_commit, json[QString("commit")]);
    m_commit_isSet = !json[QString("commit")].isNull() && m_commit_isValid;

    m_javascript_isValid = ::OpenAPI::fromJsonValue(m_javascript, json[QString("javascript")]);
    m_javascript_isSet = !json[QString("javascript")].isNull() && m_javascript_isValid;

    m_testcloud_isValid = ::OpenAPI::fromJsonValue(m_testcloud, json[QString("testcloud")]);
    m_testcloud_isSet = !json[QString("testcloud")].isNull() && m_testcloud_isValid;

    m_uwp_isValid = ::OpenAPI::fromJsonValue(m_uwp, json[QString("uwp")]);
    m_uwp_isSet = !json[QString("uwp")].isNull() && m_uwp_isValid;

    m_xamarin_isValid = ::OpenAPI::fromJsonValue(m_xamarin, json[QString("xamarin")]);
    m_xamarin_isSet = !json[QString("xamarin")].isNull() && m_xamarin_isValid;

    m_xcode_isValid = ::OpenAPI::fromJsonValue(m_xcode, json[QString("xcode")]);
    m_xcode_isSet = !json[QString("xcode")].isNull() && m_xcode_isValid;
}

QString OAIToolsetProjects::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIToolsetProjects::asJsonObject() const {
    QJsonObject obj;
    if (m_android.isSet()) {
        obj.insert(QString("android"), ::OpenAPI::toJsonValue(m_android));
    }
    if (m_buildscripts.size() > 0) {
        obj.insert(QString("buildscripts"), ::OpenAPI::toJsonValue(m_buildscripts));
    }
    if (m_commit_isSet) {
        obj.insert(QString("commit"), ::OpenAPI::toJsonValue(m_commit));
    }
    if (m_javascript.isSet()) {
        obj.insert(QString("javascript"), ::OpenAPI::toJsonValue(m_javascript));
    }
    if (m_testcloud.isSet()) {
        obj.insert(QString("testcloud"), ::OpenAPI::toJsonValue(m_testcloud));
    }
    if (m_uwp.isSet()) {
        obj.insert(QString("uwp"), ::OpenAPI::toJsonValue(m_uwp));
    }
    if (m_xamarin.isSet()) {
        obj.insert(QString("xamarin"), ::OpenAPI::toJsonValue(m_xamarin));
    }
    if (m_xcode.isSet()) {
        obj.insert(QString("xcode"), ::OpenAPI::toJsonValue(m_xcode));
    }
    return obj;
}

OAIBuilds_listToolsetProjects_200_response_android OAIToolsetProjects::getAndroid() const {
    return m_android;
}
void OAIToolsetProjects::setAndroid(const OAIBuilds_listToolsetProjects_200_response_android &android) {
    m_android = android;
    m_android_isSet = true;
}

bool OAIToolsetProjects::is_android_Set() const{
    return m_android_isSet;
}

bool OAIToolsetProjects::is_android_Valid() const{
    return m_android_isValid;
}

QMap<QString, OAIBuilds_listToolsetProjects_200_response_buildscripts_value> OAIToolsetProjects::getBuildscripts() const {
    return m_buildscripts;
}
void OAIToolsetProjects::setBuildscripts(const QMap<QString, OAIBuilds_listToolsetProjects_200_response_buildscripts_value> &buildscripts) {
    m_buildscripts = buildscripts;
    m_buildscripts_isSet = true;
}

bool OAIToolsetProjects::is_buildscripts_Set() const{
    return m_buildscripts_isSet;
}

bool OAIToolsetProjects::is_buildscripts_Valid() const{
    return m_buildscripts_isValid;
}

QString OAIToolsetProjects::getCommit() const {
    return m_commit;
}
void OAIToolsetProjects::setCommit(const QString &commit) {
    m_commit = commit;
    m_commit_isSet = true;
}

bool OAIToolsetProjects::is_commit_Set() const{
    return m_commit_isSet;
}

bool OAIToolsetProjects::is_commit_Valid() const{
    return m_commit_isValid;
}

OAIBuilds_listToolsetProjects_200_response_javascript OAIToolsetProjects::getJavascript() const {
    return m_javascript;
}
void OAIToolsetProjects::setJavascript(const OAIBuilds_listToolsetProjects_200_response_javascript &javascript) {
    m_javascript = javascript;
    m_javascript_isSet = true;
}

bool OAIToolsetProjects::is_javascript_Set() const{
    return m_javascript_isSet;
}

bool OAIToolsetProjects::is_javascript_Valid() const{
    return m_javascript_isValid;
}

OAIBuilds_listToolsetProjects_200_response_testcloud OAIToolsetProjects::getTestcloud() const {
    return m_testcloud;
}
void OAIToolsetProjects::setTestcloud(const OAIBuilds_listToolsetProjects_200_response_testcloud &testcloud) {
    m_testcloud = testcloud;
    m_testcloud_isSet = true;
}

bool OAIToolsetProjects::is_testcloud_Set() const{
    return m_testcloud_isSet;
}

bool OAIToolsetProjects::is_testcloud_Valid() const{
    return m_testcloud_isValid;
}

OAIBuilds_listToolsetProjects_200_response_uwp OAIToolsetProjects::getUwp() const {
    return m_uwp;
}
void OAIToolsetProjects::setUwp(const OAIBuilds_listToolsetProjects_200_response_uwp &uwp) {
    m_uwp = uwp;
    m_uwp_isSet = true;
}

bool OAIToolsetProjects::is_uwp_Set() const{
    return m_uwp_isSet;
}

bool OAIToolsetProjects::is_uwp_Valid() const{
    return m_uwp_isValid;
}

OAIBuilds_listToolsetProjects_200_response_xamarin OAIToolsetProjects::getXamarin() const {
    return m_xamarin;
}
void OAIToolsetProjects::setXamarin(const OAIBuilds_listToolsetProjects_200_response_xamarin &xamarin) {
    m_xamarin = xamarin;
    m_xamarin_isSet = true;
}

bool OAIToolsetProjects::is_xamarin_Set() const{
    return m_xamarin_isSet;
}

bool OAIToolsetProjects::is_xamarin_Valid() const{
    return m_xamarin_isValid;
}

OAIBuilds_listToolsetProjects_200_response_xcode OAIToolsetProjects::getXcode() const {
    return m_xcode;
}
void OAIToolsetProjects::setXcode(const OAIBuilds_listToolsetProjects_200_response_xcode &xcode) {
    m_xcode = xcode;
    m_xcode_isSet = true;
}

bool OAIToolsetProjects::is_xcode_Set() const{
    return m_xcode_isSet;
}

bool OAIToolsetProjects::is_xcode_Valid() const{
    return m_xcode_isValid;
}

bool OAIToolsetProjects::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_android.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_buildscripts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_commit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_javascript.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_testcloud.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_uwp.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_xamarin.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_xcode.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIToolsetProjects::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
