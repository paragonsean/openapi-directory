/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateDownloadProgress.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateDownloadProgress::OAIUpdateDownloadProgress(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateDownloadProgress::OAIUpdateDownloadProgress() {
    this->initializeModel();
}

OAIUpdateDownloadProgress::~OAIUpdateDownloadProgress() {}

void OAIUpdateDownloadProgress::initializeModel() {

    m_download_phase_isSet = false;
    m_download_phase_isValid = false;

    m_number_of_updates_downloaded_isSet = false;
    m_number_of_updates_downloaded_isValid = false;

    m_number_of_updates_to_download_isSet = false;
    m_number_of_updates_to_download_isValid = false;

    m_percent_complete_isSet = false;
    m_percent_complete_isValid = false;

    m_total_bytes_downloaded_isSet = false;
    m_total_bytes_downloaded_isValid = false;

    m_total_bytes_to_download_isSet = false;
    m_total_bytes_to_download_isValid = false;
}

void OAIUpdateDownloadProgress::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateDownloadProgress::fromJsonObject(QJsonObject json) {

    m_download_phase_isValid = ::OpenAPI::fromJsonValue(m_download_phase, json[QString("downloadPhase")]);
    m_download_phase_isSet = !json[QString("downloadPhase")].isNull() && m_download_phase_isValid;

    m_number_of_updates_downloaded_isValid = ::OpenAPI::fromJsonValue(m_number_of_updates_downloaded, json[QString("numberOfUpdatesDownloaded")]);
    m_number_of_updates_downloaded_isSet = !json[QString("numberOfUpdatesDownloaded")].isNull() && m_number_of_updates_downloaded_isValid;

    m_number_of_updates_to_download_isValid = ::OpenAPI::fromJsonValue(m_number_of_updates_to_download, json[QString("numberOfUpdatesToDownload")]);
    m_number_of_updates_to_download_isSet = !json[QString("numberOfUpdatesToDownload")].isNull() && m_number_of_updates_to_download_isValid;

    m_percent_complete_isValid = ::OpenAPI::fromJsonValue(m_percent_complete, json[QString("percentComplete")]);
    m_percent_complete_isSet = !json[QString("percentComplete")].isNull() && m_percent_complete_isValid;

    m_total_bytes_downloaded_isValid = ::OpenAPI::fromJsonValue(m_total_bytes_downloaded, json[QString("totalBytesDownloaded")]);
    m_total_bytes_downloaded_isSet = !json[QString("totalBytesDownloaded")].isNull() && m_total_bytes_downloaded_isValid;

    m_total_bytes_to_download_isValid = ::OpenAPI::fromJsonValue(m_total_bytes_to_download, json[QString("totalBytesToDownload")]);
    m_total_bytes_to_download_isSet = !json[QString("totalBytesToDownload")].isNull() && m_total_bytes_to_download_isValid;
}

QString OAIUpdateDownloadProgress::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateDownloadProgress::asJsonObject() const {
    QJsonObject obj;
    if (m_download_phase_isSet) {
        obj.insert(QString("downloadPhase"), ::OpenAPI::toJsonValue(m_download_phase));
    }
    if (m_number_of_updates_downloaded_isSet) {
        obj.insert(QString("numberOfUpdatesDownloaded"), ::OpenAPI::toJsonValue(m_number_of_updates_downloaded));
    }
    if (m_number_of_updates_to_download_isSet) {
        obj.insert(QString("numberOfUpdatesToDownload"), ::OpenAPI::toJsonValue(m_number_of_updates_to_download));
    }
    if (m_percent_complete_isSet) {
        obj.insert(QString("percentComplete"), ::OpenAPI::toJsonValue(m_percent_complete));
    }
    if (m_total_bytes_downloaded_isSet) {
        obj.insert(QString("totalBytesDownloaded"), ::OpenAPI::toJsonValue(m_total_bytes_downloaded));
    }
    if (m_total_bytes_to_download_isSet) {
        obj.insert(QString("totalBytesToDownload"), ::OpenAPI::toJsonValue(m_total_bytes_to_download));
    }
    return obj;
}

QString OAIUpdateDownloadProgress::getDownloadPhase() const {
    return m_download_phase;
}
void OAIUpdateDownloadProgress::setDownloadPhase(const QString &download_phase) {
    m_download_phase = download_phase;
    m_download_phase_isSet = true;
}

bool OAIUpdateDownloadProgress::is_download_phase_Set() const{
    return m_download_phase_isSet;
}

bool OAIUpdateDownloadProgress::is_download_phase_Valid() const{
    return m_download_phase_isValid;
}

qint32 OAIUpdateDownloadProgress::getNumberOfUpdatesDownloaded() const {
    return m_number_of_updates_downloaded;
}
void OAIUpdateDownloadProgress::setNumberOfUpdatesDownloaded(const qint32 &number_of_updates_downloaded) {
    m_number_of_updates_downloaded = number_of_updates_downloaded;
    m_number_of_updates_downloaded_isSet = true;
}

bool OAIUpdateDownloadProgress::is_number_of_updates_downloaded_Set() const{
    return m_number_of_updates_downloaded_isSet;
}

bool OAIUpdateDownloadProgress::is_number_of_updates_downloaded_Valid() const{
    return m_number_of_updates_downloaded_isValid;
}

qint32 OAIUpdateDownloadProgress::getNumberOfUpdatesToDownload() const {
    return m_number_of_updates_to_download;
}
void OAIUpdateDownloadProgress::setNumberOfUpdatesToDownload(const qint32 &number_of_updates_to_download) {
    m_number_of_updates_to_download = number_of_updates_to_download;
    m_number_of_updates_to_download_isSet = true;
}

bool OAIUpdateDownloadProgress::is_number_of_updates_to_download_Set() const{
    return m_number_of_updates_to_download_isSet;
}

bool OAIUpdateDownloadProgress::is_number_of_updates_to_download_Valid() const{
    return m_number_of_updates_to_download_isValid;
}

qint32 OAIUpdateDownloadProgress::getPercentComplete() const {
    return m_percent_complete;
}
void OAIUpdateDownloadProgress::setPercentComplete(const qint32 &percent_complete) {
    m_percent_complete = percent_complete;
    m_percent_complete_isSet = true;
}

bool OAIUpdateDownloadProgress::is_percent_complete_Set() const{
    return m_percent_complete_isSet;
}

bool OAIUpdateDownloadProgress::is_percent_complete_Valid() const{
    return m_percent_complete_isValid;
}

double OAIUpdateDownloadProgress::getTotalBytesDownloaded() const {
    return m_total_bytes_downloaded;
}
void OAIUpdateDownloadProgress::setTotalBytesDownloaded(const double &total_bytes_downloaded) {
    m_total_bytes_downloaded = total_bytes_downloaded;
    m_total_bytes_downloaded_isSet = true;
}

bool OAIUpdateDownloadProgress::is_total_bytes_downloaded_Set() const{
    return m_total_bytes_downloaded_isSet;
}

bool OAIUpdateDownloadProgress::is_total_bytes_downloaded_Valid() const{
    return m_total_bytes_downloaded_isValid;
}

double OAIUpdateDownloadProgress::getTotalBytesToDownload() const {
    return m_total_bytes_to_download;
}
void OAIUpdateDownloadProgress::setTotalBytesToDownload(const double &total_bytes_to_download) {
    m_total_bytes_to_download = total_bytes_to_download;
    m_total_bytes_to_download_isSet = true;
}

bool OAIUpdateDownloadProgress::is_total_bytes_to_download_Set() const{
    return m_total_bytes_to_download_isSet;
}

bool OAIUpdateDownloadProgress::is_total_bytes_to_download_Valid() const{
    return m_total_bytes_to_download_isValid;
}

bool OAIUpdateDownloadProgress::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_download_phase_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_of_updates_downloaded_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_of_updates_to_download_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_percent_complete_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_bytes_downloaded_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_bytes_to_download_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateDownloadProgress::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
