/**
 * Spotify Web API with fixes and improvements from sonallux
 * You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 
 *
 * The version of the OpenAPI document: 2023.2.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAudioAnalysisObject_meta.h
 *
 * 
 */

#ifndef OAIAudioAnalysisObject_meta_H
#define OAIAudioAnalysisObject_meta_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAudioAnalysisObject_meta : public OAIObject {
public:
    OAIAudioAnalysisObject_meta();
    OAIAudioAnalysisObject_meta(QString json);
    ~OAIAudioAnalysisObject_meta() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getAnalysisTime() const;
    void setAnalysisTime(const double &analysis_time);
    bool is_analysis_time_Set() const;
    bool is_analysis_time_Valid() const;

    QString getAnalyzerVersion() const;
    void setAnalyzerVersion(const QString &analyzer_version);
    bool is_analyzer_version_Set() const;
    bool is_analyzer_version_Valid() const;

    QString getDetailedStatus() const;
    void setDetailedStatus(const QString &detailed_status);
    bool is_detailed_status_Set() const;
    bool is_detailed_status_Valid() const;

    QString getInputProcess() const;
    void setInputProcess(const QString &input_process);
    bool is_input_process_Set() const;
    bool is_input_process_Valid() const;

    QString getPlatform() const;
    void setPlatform(const QString &platform);
    bool is_platform_Set() const;
    bool is_platform_Valid() const;

    qint32 getStatusCode() const;
    void setStatusCode(const qint32 &status_code);
    bool is_status_code_Set() const;
    bool is_status_code_Valid() const;

    qint32 getTimestamp() const;
    void setTimestamp(const qint32 &timestamp);
    bool is_timestamp_Set() const;
    bool is_timestamp_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_analysis_time;
    bool m_analysis_time_isSet;
    bool m_analysis_time_isValid;

    QString m_analyzer_version;
    bool m_analyzer_version_isSet;
    bool m_analyzer_version_isValid;

    QString m_detailed_status;
    bool m_detailed_status_isSet;
    bool m_detailed_status_isValid;

    QString m_input_process;
    bool m_input_process_isSet;
    bool m_input_process_isValid;

    QString m_platform;
    bool m_platform_isSet;
    bool m_platform_isValid;

    qint32 m_status_code;
    bool m_status_code_isSet;
    bool m_status_code_isValid;

    qint32 m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAudioAnalysisObject_meta)

#endif // OAIAudioAnalysisObject_meta_H
